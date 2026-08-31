# -*- coding: utf-8 -*-
"""Le anade a una imagen plana el detalle que una miniatura necesita.

El problema: las imagenes del video 7 son planas a proposito —cel-shading,
contorno duro, cara neutra—. Recortar un fotograma da una miniatura sosa.

La solucion no es generar otra imagen: es dibujarle encima lo que le falta.
Todo lo que hace fuerte a una miniatura del canal es procedural:

  · venas rojas             · gotas de sudor
  · rayas de glitch          · franjas de luz dura
  · division calido/frio     · grano y suciedad

Uso:
    from detalle import realzar
    realzar('SH019.png', 'base_v7.png', ojo=(0.63, 0.44), radio=0.13)
"""
from PIL import Image, ImageDraw, ImageFilter, ImageChops
import random, math

def _venas(cap, cx, cy, r, n=26, semilla=11):
    """Venas rojas irradiando desde el borde del iris hacia afuera."""
    rnd = random.Random(semilla)
    d = ImageDraw.Draw(cap)
    for _ in range(n):
        a = rnd.uniform(0, math.tau)
        x, y = cx + math.cos(a)*r*0.55, cy + math.sin(a)*r*0.55
        largo = r * rnd.uniform(0.5, 1.05)
        pasos = rnd.randint(3, 6)
        pts = [(x, y)]
        for i in range(pasos):
            a += rnd.uniform(-0.5, 0.5)
            x += math.cos(a) * largo/pasos
            y += math.sin(a) * largo/pasos
            pts.append((x, y))
        col = (rnd.randint(150, 205), rnd.randint(20, 45), rnd.randint(25, 50),
               rnd.randint(150, 225))
        d.line(pts, fill=col, width=rnd.choice([1,1,2,2,3]), joint='curve')

def _sudor(cap, w, h, cx, cy, r, n=10, semilla=5):
    """Gotas alargadas cayendo, agrupadas alrededor del ojo. Repartidas por
    todo el cuadro parecen lluvia; cerca de la cara parecen sudor."""
    rnd = random.Random(semilla)
    d = ImageDraw.Draw(cap)
    for _ in range(n):
        a = rnd.uniform(0, math.tau); dist = r * rnd.uniform(1.4, 3.2)
        x = cx + math.cos(a)*dist; y = cy + abs(math.sin(a))*dist*0.9
        if not (0 < x < w*0.82 and 0 < y < h): continue
        rx = rnd.uniform(w*0.004, w*0.009); ry = rx * rnd.uniform(2.0, 3.4)
        d.ellipse([x-rx, y-ry, x+rx, y+ry], fill=(196, 214, 228, 150),
                  outline=(30, 40, 52, 190), width=2)
        d.ellipse([x-rx*0.4, y-ry*0.55, x+rx*0.1, y-ry*0.1], fill=(255,255,255,205))

def _glitch(im, x0, semilla=3):
    """Desplaza bandas horizontales y separa el rojo del cian, a la derecha."""
    rnd = random.Random(semilla)
    w, h = im.size
    for _ in range(16):
        y = rnd.randint(0, h-1); alto = rnd.randint(3, 22)
        banda = im.crop((x0, y, w, min(h, y+alto)))
        im.paste(banda, (x0 + rnd.randint(-26, 26), y))
    der = im.crop((x0, 0, w, h))
    r, g, b = der.split()[:3]
    r = ImageChops.offset(r, 4, 0); b = ImageChops.offset(b, -4, 0)
    im.paste(Image.merge('RGB', (r, g, b)), (x0, 0))

def _frio_calido(im, x0):
    """Calido a la izquierda, frio a la derecha. Separa los dos mundos."""
    w, h = im.size
    capa = Image.new('RGB', (w, h))
    d = ImageDraw.Draw(capa)
    for x in range(w):
        t = 0.0 if x < x0 else min(1.0, (x-x0)/max(1, w*0.10))
        d.line([(x,0),(x,h)], fill=(int(255-120*t), int(232-90*t), int(196+30*t)))
    return ImageChops.multiply(im, capa)

def _grano(im, fuerza=16, semilla=7):
    rnd = random.Random(semilla)
    w, h = im.size
    ruido = Image.new('L', (w//2, h//2))
    ruido.putdata([rnd.randint(128-fuerza, 128+fuerza) for _ in range(w//2*h//2)])
    ruido = ruido.resize((w, h), Image.BILINEAR)
    return ImageChops.overlay(im, Image.merge('RGB', (ruido, ruido, ruido)))

def realzar(entrada, salida, ojo=(0.62, 0.44), radio=0.12, corte=0.78, zoom=1.0):
    """ojo: centro del ojo en fracciones del ancho y alto. radio: fraccion del ancho.
    corte: donde empieza el mundo frio. zoom: acercamiento antes de todo."""
    im = Image.open(entrada).convert('RGB')
    if zoom > 1.0:
        w, h = im.size
        nw, nh = int(w/zoom), int(h/zoom)
        im = im.crop(((w-nw)//2, (h-nh)//2, (w-nw)//2+nw, (h-nh)//2+nh)).resize((w, h), Image.LANCZOS)
    w, h = im.size
    x0 = int(w*corte)

    im = _frio_calido(im, x0)
    _glitch(im, x0)

    cap = Image.new('RGBA', (w, h), (0,0,0,0))
    _venas(cap, w*ojo[0], h*ojo[1], w*radio, n=34)
    _sudor(cap, w, h, w*ojo[0], h*ojo[1], w*radio)
    im = Image.alpha_composite(im.convert('RGBA'), cap).convert('RGB')

    # franja dura de reflector, en diagonal sobre el ojo
    # franja de reflector: angosta, en diagonal y con el borde difuminado.
    # Ancha y dura se come la imagen en vez de cortarla.
    luz = Image.new('L', (w, h), 0)
    ImageDraw.Draw(luz).polygon(
        [(w*0.30, 0), (w*0.40, 0), (w*0.66, h), (w*0.56, h)], fill=58)
    luz = luz.filter(ImageFilter.GaussianBlur(w*0.012))
    im = ImageChops.add(im, Image.merge('RGB', (luz, luz, luz)))

    im = _grano(im)
    im.save(salida)
    print('realzada ->', salida)
