# -*- coding: utf-8 -*-
"""Convierte una imagen de IA en los formatos EXACTOS que pide YouTube:

  --avatar  -> 800x800 px, recorte centrado (YouTube lo muestra en circulo)
  --banner  -> 2560x1440 px con el area segura respetada: lo unico que se ve
               en todos los dispositivos es el centro de 1546x423, asi que el
               texto del canal se coloca ahi y los bordes quedan de relleno.

Uso:
  python3 scripts/07_marca.py --canal lakshmi --img arte.png --avatar
  python3 scripts/07_marca.py --canal lakshmi --img arte.png --banner
  python3 scripts/07_marca.py --canal lakshmi --img arte.png --banner --sin-texto
"""
import argparse, json, pathlib, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE = pathlib.Path(__file__).resolve().parent.parent
CAT = json.loads((BASE / "datos" / "catalogo.json").read_text(encoding="utf-8"))
SEGURA = (1546, 423)          # area visible en TV, escritorio, tablet y movil
FUENTES = ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
           "C:/Windows/Fonts/arialbd.ttf",
           "/System/Library/Fonts/Supplemental/Arial Bold.ttf"]


def fuente(sz):
    for f in FUENTES:
        if pathlib.Path(f).exists():
            return ImageFont.truetype(f, sz)
    return ImageFont.load_default()


def encajar(im, w, h):
    """Escala y recorta al centro para llenar exactamente w x h sin deformar."""
    r = max(w / im.width, h / im.height)
    im = im.resize((max(w, int(im.width * r)), max(h, int(im.height * r))), Image.LANCZOS)
    x, y = (im.width - w) // 2, (im.height - h) // 2
    return im.crop((x, y, x + w, y + h))


def contorno(d, xy, txt, f, relleno, borde=5):
    x, y = xy
    for dx in range(-borde, borde + 1, 2):
        for dy in range(-borde, borde + 1, 2):
            d.text((x + dx, y + dy), txt, font=f, fill=(0, 0, 0, 235))
    d.text((x, y), txt, font=f, fill=relleno)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--canal", required=True, help="lakshmi | ganesha | uriel")
    ap.add_argument("--img", required=True)
    ap.add_argument("--avatar", action="store_true")
    ap.add_argument("--banner", action="store_true")
    ap.add_argument("--sin-texto", action="store_true", help="banner sin el nombre encima")
    a = ap.parse_args()
    if not (a.avatar or a.banner):
        sys.exit("Elige --avatar o --banner")
    canal = next((c for c in CAT["canales"] if c["slug"] == a.canal), None)
    if not canal:
        sys.exit("canal invalido: usa lakshmi, ganesha o uriel")

    im = Image.open(a.img).convert("RGB")
    dest = BASE / "assets" / "marca"   # en assets/ para que si quede versionado
    dest.mkdir(parents=True, exist_ok=True)

    if a.avatar:
        out = dest / f"{a.canal}-avatar.png"
        encajar(im, 800, 800).save(out)
        print(f"AVATAR -> {out}  (800x800; YouTube lo recorta en circulo)")

    if a.banner:
        # Composicion: la deidad ocupa el tercio derecho y el texto va a la
        # izquierda sobre un fondo desenfocado de la misma imagen (sin costuras).
        fondo = encajar(im, 2560, 1440).filter(ImageFilter.GaussianBlur(45))
        sujeto = encajar(im, 1500, 1440)
        lienzo = fondo.copy()
        # el sujeto se funde con el fondo mediante una mascara degradada
        mask = Image.new("L", (1500, 1440), 255)
        dm = ImageDraw.Draw(mask)
        for x in range(320):
            dm.line([(x, 0), (x, 1440)], fill=int(255 * (x / 320) ** 1.4))
        lienzo.paste(sujeto, (1060, 0), mask)

        sx, sy = (2560 - SEGURA[0]) // 2, (1440 - SEGURA[1]) // 2
        cap = Image.new("RGBA", (2560, 1440), (0, 0, 0, 0))
        dc = ImageDraw.Draw(cap)
        # velo lateral degradado para que el texto siempre tenga contraste
        for x in range(1450):
            dc.line([(x, 0), (x, 1440)], fill=(4, 8, 24, int(220 * (1 - x / 1450) ** 0.8)))
        # oscurecido progresivo arriba y abajo (fuera del area segura), sin bandas duras
        for y in range(sy):
            al = int(150 * (1 - y / sy) ** 1.2)
            dc.line([(0, y), (2560, y)], fill=(0, 0, 0, al))
            dc.line([(0, 1439 - y), (2560, 1439 - y)], fill=(0, 0, 0, al))
        lienzo = Image.alpha_composite(lienzo.convert("RGBA"), cap)

        if not a.sin_texto:
            d = ImageDraw.Draw(lienzo)
            palabras = canal["nombre"].upper().split()
            if len(palabras) > 2:
                mitad = len(palabras) // 2 + len(palabras) % 2
                lineas = [" ".join(palabras[:mitad]), " ".join(palabras[mitad:])]
            else:
                lineas = [canal["nombre"].upper()]
            f1 = fuente(112 if max(len(l) for l in lineas) <= 16 else 88)
            y = sy + 55
            for ln in lineas:
                contorno(d, (sx + 20, y), ln, f1, (255, 215, 0), 6)
                y += f1.size + 12
            f2 = fuente(40)
            contorno(d, (sx + 24, y + 12),
                     "NEW ABUNDANCE FREQUENCY EVERY 36 HOURS", f2, (255, 255, 255), 3)

        out = dest / f"{a.canal}-banner.png"
        lienzo.convert("RGB").save(out)
        print(f"BANNER -> {out}  (2560x1440; texto dentro del area segura de 1546x423)")


if __name__ == "__main__":
    main()
