# -*- coding: utf-8 -*-
"""Convierte una imagen de IA en miniatura 1280x720 lista para YouTube:
recorte 16:9 + vineta + texto grande con contorno + frecuencia + duracion.

Uso: python3 scripts/06_miniatura.py --id lakshmi-01 --img salida/lakshmi-01/img/1.png
"""
import argparse, json, pathlib, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE = pathlib.Path(__file__).resolve().parent.parent
CAT = json.loads((BASE/"datos"/"catalogo.json").read_text(encoding="utf-8"))
W, H = 1280, 720
FUENTES = ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
           "C:/Windows/Fonts/arialbd.ttf", "/Library/Fonts/Arial Bold.ttf",
           "/System/Library/Fonts/Supplemental/Arial Bold.ttf"]

def fuente(sz):
    for f in FUENTES:
        if pathlib.Path(f).exists():
            return ImageFont.truetype(f, sz)
    return ImageFont.load_default()

def buscar(vid):
    for c in CAT["canales"]:
        for v in c["videos"]:
            if v["id"] == vid: return c, v
    sys.exit("id invalido")

def contorno(d, xy, txt, f, relleno, borde=6):
    x, y = xy
    for dx in range(-borde, borde+1, 2):
        for dy in range(-borde, borde+1, 2):
            d.text((x+dx, y+dy), txt, font=f, fill=(0, 0, 0, 230))
    d.text((x, y), txt, font=f, fill=relleno)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--id", required=True); ap.add_argument("--img", required=True)
    a = ap.parse_args()
    canal, v = buscar(a.id)
    im = Image.open(a.img).convert("RGB")
    # recorte centrado 16:9
    r = max(W/im.width, H/im.height)
    im = im.resize((int(im.width*r), int(im.height*r)), Image.LANCZOS)
    im = im.crop(((im.width-W)//2, (im.height-H)//2, (im.width-W)//2+W, (im.height-H)//2+H))
    # oscurecer la mitad izquierda para que el texto resalte
    capa = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    dc = ImageDraw.Draw(capa)
    for x in range(W//2):
        dc.line([(x, 0), (x, H)], fill=(0, 0, 0, int(165*(1-x/(W/2)))))
    im = Image.alpha_composite(im.convert("RGBA"), capa.filter(ImageFilter.GaussianBlur(2)))
    d = ImageDraw.Draw(im)
    lineas = v["miniatura_texto"].split()
    if len(lineas) > 2:
        mitad = len(lineas)//2 + len(lineas) % 2
        lineas = [" ".join(lineas[:mitad]), " ".join(lineas[mitad:])]
    f = fuente(118 if max(map(len, lineas)) <= 9 else 88)
    y = H//2 - len(lineas)*(f.size+10)//2 - 30
    for ln in lineas:
        contorno(d, (60, y), ln, f, (255, 215, 0)); y += f.size + 12
    fs = fuente(46)
    plural = "" if v["horas"] == 1 else "S"
    contorno(d, (62, y+18), f"{v['hz']} Hz  •  {v['horas']} HOUR{plural}", fs, (255, 255, 255), 4)
    fm = fuente(30)
    contorno(d, (62, H-58), canal["nombre"].upper(), fm, (255, 255, 255), 3)
    out = BASE/"salida"/a.id/"miniatura.jpg"
    out.parent.mkdir(parents=True, exist_ok=True)
    im.convert("RGB").save(out, quality=92)
    print(f"LISTO -> {out}  (1280x720, <2MB para YouTube)")

if __name__ == "__main__":
    main()
