from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter
import os, random, warnings
warnings.filterwarnings('ignore')
random.seed(7)

F='_fuentes/Anton-Regular.ttf'
if not os.path.exists(F):
    raise SystemExit(f'falta la fuente {F}. Sin Anton la tipografia no es la del canal.')
D='imagenes_1080p'
W,H=1280,720

def textura_rayada(mask_size, densidad=70):
    """Arañazos blancos/oscuros como los de las miniaturas reales."""
    t=Image.new('L', mask_size, 255)
    d=ImageDraw.Draw(t)
    w,h=mask_size
    for _ in range(densidad):
        x=random.randint(0,w); y=random.randint(0,h)
        L=random.randint(8,60); ang=random.choice([0,0,0,1])
        x2=x+(L if ang==0 else random.randint(-6,6))
        y2=y+(random.randint(-4,4) if ang==0 else L)
        d.line([(x,y),(x2,y2)], fill=random.randint(90,170), width=random.choice([1,1,2]))
    for _ in range(densidad//2):
        x=random.randint(0,w); y=random.randint(0,h)
        d.ellipse([x,y,x+random.randint(1,4),y+random.randint(1,3)], fill=random.randint(100,180))
    return t

def texto_texturado(base, xy, txt, font, color, contorno=6):
    """Dibuja texto con contorno negro grueso y textura de desgaste encima."""
    bb=font.getbbox(txt)
    pw,ph=bb[2]-bb[0]+contorno*4, bb[3]-bb[1]+contorno*4
    cap=Image.new('RGBA',(pw,ph),(0,0,0,0))
    dc=ImageDraw.Draw(cap)
    ox,oy=contorno*2-bb[0], contorno*2-bb[1]
    for dx in range(-contorno,contorno+1,2):
        for dy in range(-contorno,contorno+1,2):
            dc.text((ox+dx,oy+dy),txt,font=font,fill=(0,0,0,255))
    dc.text((ox,oy),txt,font=font,fill=color+(255,))
    # textura solo sobre el relleno
    relleno=Image.new('L',(pw,ph),0)
    ImageDraw.Draw(relleno).text((ox,oy),txt,font=font,fill=255)
    tex=textura_rayada((pw,ph))
    oscuro=cap.copy()
    oscuro.putalpha(Image.composite(tex, Image.new('L',(pw,ph),255), relleno))
    base.alpha_composite(oscuro, xy)
    return bb[2]-bb[0]                      # ancho real del texto dibujado

def banda_brocha(d, x, y, w, h, color=(196,26,26)):
    pts=[(x-6,y+8)]
    for i in range(1,7):
        pts.append((x+w*i/6, y-6+random.randint(-4,5)))
    pts.append((x+w+4, y+h-2))
    for i in range(5,-1,-1):
        pts.append((x+w*i/6, y+h+4+random.randint(-5,4)))
    d.polygon(pts, fill=color)

def buscar_base(base):
    """Acepta el numero de un fotograma de Flow o la ruta de una imagen."""
    if isinstance(base, str):
        if not os.path.exists(base):
            raise SystemExit(f'no existe la imagen base: {base}')
        return base
    cand=[x for x in os.listdir(D) if x.startswith('flow_%03d'%base)]
    if not cand:
        raise SystemExit(f'no hay ningun fotograma flow_{base:03d} en {D}/')
    return os.path.join(D,cand[0])

def render(base, setup, cuerpo, remate, sub1, sub_rojo, salida, desplazar=0):
    """desplazar: pixeles que se corre el encuadre a la izquierda. Positivo
    empuja al personaje hacia la derecha y le deja mas aire al texto."""
    im=Image.open(buscar_base(base)).convert('RGB')
    im=im.resize((int(W*1.2), int(H*1.2)), Image.LANCZOS)
    x0=max(0, min(im.width-W, im.width-W+desplazar))
    im=im.crop((x0, (im.height-H)//2, x0+W, (im.height-H)//2+H))
    ov=Image.new('L',(W,H),0); dv=ImageDraw.Draw(ov)
    for x in range(W):
        t=max(0.0, 1.0-x/(W*0.66))
        dv.line([(x,0),(x,H)], fill=int(242*(t**1.15)))
    im=Image.composite(Image.new('RGB',(W,H),(5,5,9)), im, ov.filter(ImageFilter.GaussianBlur(3)))
    im=ImageEnhance.Contrast(im).enhance(1.15).convert('RGBA')
    d=ImageDraw.Draw(im)

    fset=ImageFont.truetype(F,54)
    fbig=ImageFont.truetype(F,132)
    fsub=ImageFont.truetype(F,44)

    bb=fset.getbbox(setup); bw=bb[2]-bb[0]+52; bh=bb[3]-bb[1]+30
    banda_brocha(d, 52, 44, bw, bh)
    d.text((52+26, 44+15-bb[1]), setup, font=fset, fill=(255,255,255))

    y=44+bh+30
    texto_texturado(im,(44,y),cuerpo,fbig,(255,255,255)); y+=140
    wrem=texto_texturado(im,(44,y),remate,fbig,(255,206,8)); y+=150

    # linea roja de brocha: sigue el ancho real de la palabra amarilla,
    # nunca un ancho fijo. Con una palabra corta la raya ya no sobresale.
    xr=56+wrem
    d.polygon([(56,y-14),(xr,y-24),(xr+4,y-6),(60,y+4)], fill=(196,26,26))
    y+=14
    texto_texturado(im,(52,y),sub1,fsub,(255,255,255),contorno=4)
    wsub=fsub.getbbox(sub1)[2]-fsub.getbbox(sub1)[0]
    texto_texturado(im,(52+wsub+18,y),sub_rojo,fsub,(228,42,42),contorno=4)

    im=im.convert('RGB')
    im.save(salida, quality=95)

    # prueba de legibilidad: el tamano al que la ve media audiencia
    prueba=salida.replace('.jpg','_210x118.jpg')
    im.resize((210,118), Image.LANCZOS).save(prueba, quality=92)
    print('ok', salida, '| prueba:', prueba)

if __name__ == '__main__':
    # ---- video 5, las tres variantes ----
    render(183,"YOUR BRAIN THINKS","IT'S STILL","HUNTING","THE 40,000 YEAR OLD","GLITCH","MINIATURA_A.jpg")
    render(110,"NOBODY TOLD YOU","YOU CAN'T","STOP","IT WAS NEVER YOUR","WILLPOWER","MINIATURA_B.jpg")
    render(125,"THE REAL REASON","YOU KEEP","SCROLLING","AN ANCIENT SURVIVAL","INSTINCT","MINIATURA_C.jpg")

    # la misma A, corriendo el encuadre para darle mas aire al texto
    render(183,"YOUR BRAIN THINKS","IT'S STILL","HUNTING","THE 40,000 YEAR OLD","GLITCH",
           "MINIATURA_A_aire.jpg", desplazar=140)

    # ---- video 7 ----
    # La base NO se recorta de un fotograma: las imagenes del video 7 son
    # planas a proposito y un recorte plano da una miniatura sosa. Se genera
    # aparte con volumen y expresion, y entra por aqui como ruta.
    if os.path.exists('miniatura_v7_base.png'):
        render('miniatura_v7_base.png',"YOUR BRAIN SAYS","DON'T BE","SEEN",
               "THE 300,000 YEAR OLD","CAMOUFLAGE","MINIATURA_V7.jpg")
