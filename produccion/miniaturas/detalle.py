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

def _ojo(cap, cx, cy, r, semilla=17):
    """Dibuja un ojo anatomico encima del ovalo negro plano del video.

    Es el paso que faltaba. Las venas sobre un ovalo negro macizo parecen
    grietas en la cara; sobre un blanco de ojo con iris parecen lo que son.
    El personaje del video es plano a proposito y no tiene donde llevarlas,
    asi que se le dibuja el ojo.
    """
    rnd = random.Random(semilla)
    d = ImageDraw.Draw(cap)
    # blanco del ojo: almendra ancha alrededor del ovalo negro original
    d.ellipse([cx-r*1.75, cy-r*1.12, cx+r*1.75, cy+r*1.12],
              fill=(247, 240, 232, 255), outline=(14, 12, 14, 255), width=max(3, int(r*0.13)))
    # iris
    d.ellipse([cx-r*0.86, cy-r*0.86, cx+r*0.86, cy+r*0.86],
              fill=(96, 62, 48, 255), outline=(20, 14, 12, 255), width=max(2, int(r*0.09)))
    # fibras del iris
    for _ in range(30):
        a = rnd.uniform(0, math.tau)
        d.line([(cx+math.cos(a)*r*0.36, cy+math.sin(a)*r*0.36),
                (cx+math.cos(a)*r*0.80, cy+math.sin(a)*r*0.80)],
               fill=(58, 36, 28, 190), width=1)
    # pupila
    d.ellipse([cx-r*0.40, cy-r*0.40, cx+r*0.40, cy+r*0.40], fill=(10, 8, 10, 255))
    # brillo: lo que hace que un ojo parezca humedo
    d.ellipse([cx-r*0.62, cy-r*0.70, cx-r*0.20, cy-r*0.30], fill=(255, 255, 255, 235))
    d.ellipse([cx+r*0.30, cy+r*0.24, cx+r*0.50, cy+r*0.44], fill=(255, 255, 255, 130))
    # sombra del parpado superior, que le da volumen
    d.chord([cx-r*1.75, cy-r*1.60, cx+r*1.75, cy+r*0.60], 200, 340, fill=(120, 96, 78, 90))

def _venas(cap, cx, cy, r, n=26, semilla=11):
    """Venas rojas sobre el blanco del ojo.

    Cada trazo se detiene solo al llegar al borde de la almendra: la
    restriccion es geometrica, no una mascara aplicada despues. Asi no hay
    forma de que una vena termine dibujada sobre la mejilla, que es lo que
    las convertia en aranazos.
    """
    A, B = r*1.68, r*1.05          # semiejes del blanco del ojo
    IRIS = r*0.90
    def dentro(x, y):
        return (((x-cx)/A)**2 + ((y-cy)/B)**2) < 0.93 and \
               math.hypot(x-cx, y-cy) > IRIS*0.98
    rnd = random.Random(semilla)
    d = ImageDraw.Draw(cap)
    for _ in range(n):
        a = rnd.uniform(0, math.tau)
        x, y = cx + math.cos(a)*IRIS, cy + math.sin(a)*IRIS
        if not dentro(x, y):
            continue
        pts = [(x, y)]
        paso = r*0.16
        for _ in range(rnd.randint(3, 7)):
            a += rnd.uniform(-0.55, 0.55)
            nx, ny = x + math.cos(a)*paso, y + math.sin(a)*paso
            if not dentro(nx, ny):
                break
            x, y = nx, ny
            pts.append((x, y))
        if len(pts) < 2:
            continue
        col = (rnd.randint(150, 205), rnd.randint(20, 45), rnd.randint(25, 50),
               rnd.randint(150, 225))
        d.line(pts, fill=col, width=rnd.choice([1,1,2,2,3]), joint='curve')

def _sudor(cap, w, h, cx, cy, r, n=6, semilla=5):
    """Gotas alargadas cayendo, agrupadas alrededor del ojo. Repartidas por
    todo el cuadro parecen lluvia; cerca de la cara parecen sudor."""
    rnd = random.Random(semilla)
    d = ImageDraw.Draw(cap)
    for _ in range(n):
        a = rnd.uniform(-2.6, -0.5); dist = r * rnd.uniform(1.6, 2.9)
        x = cx + math.cos(a)*dist; y = cy + abs(math.sin(a))*dist*0.9
        if not (0 < x < w*0.82 and 0 < y < h): continue
        rx = rnd.uniform(w*0.0025, w*0.005); ry = rx * rnd.uniform(2.4, 3.6)
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
        d.line([(x,0),(x,h)], fill=(int(255-118*t), int(246-84*t), int(238+16*t)))
    return ImageChops.multiply(im, capa)

def _grano(im, fuerza=16, semilla=7):
    rnd = random.Random(semilla)
    w, h = im.size
    ruido = Image.new('L', (w//2, h//2))
    ruido.putdata([rnd.randint(128-fuerza, 128+fuerza) for _ in range(w//2*h//2)])
    ruido = ruido.resize((w, h), Image.BILINEAR)
    return ImageChops.overlay(im, Image.merge('RGB', (ruido, ruido, ruido)))

def realzar(entrada, salida, ojo=(0.62, 0.44), radio=0.12, corte=0.78, zoom=1.0,
            dibujar_ojo=True):
    """ojo: centro del ojo en fracciones del ancho y alto. radio: fraccion del ancho.
    corte: donde empieza el mundo frio. zoom: acercamiento antes de todo.
    dibujar_ojo: pinta un ojo anatomico sobre el ovalo plano del personaje.
    Ponerlo en False solo si la imagen base ya trae un ojo dibujado."""
    im = Image.open(entrada).convert('RGB')
    if zoom > 1.0:
        w, h = im.size
        nw, nh = int(w/zoom), int(h/zoom)
        im = im.crop(((w-nw)//2, (h-nh)//2, (w-nw)//2+nw, (h-nh)//2+nh)).resize((w, h), Image.LANCZOS)
    w, h = im.size
    x0 = int(w*corte)

    im = _frio_calido(im, x0)
    _glitch(im, x0)

    cx, cy, r = w*ojo[0], h*ojo[1], w*radio
    cap = Image.new('RGBA', (w, h), (0,0,0,0))
    if dibujar_ojo:
        _ojo(cap, cx, cy, r)

    _venas(cap, cx, cy, r, n=44)

    _sudor(cap, w, h, cx, cy, r)
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
