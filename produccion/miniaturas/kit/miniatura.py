"""GENERADOR DE MINIATURAS — Mindset Mechanics

Aplica la formula medida sobre las miniaturas del canal que rinden 13-14% de CTR:
texto a la izquierda, personaje a la derecha, fondo oscuro, banda roja de brocha,
remate en amarillo, subtitulo abajo con una palabra en rojo, y textura de desgaste.

USO:
  python miniatura.py IMAGEN "SETUP" "CUERPO" "REMATE" "SUBTITULO" "PALABRA_ROJA" salida.jpg

EJEMPLO:
  python miniatura.py imagenes_1080p/flow_110.jpg "YOUR BRAIN THINKS" "IT'S STILL" \
      "HUNTING" "THE 40,000 YEAR OLD" "GLITCH" mini.jpg

REGLAS DE LA FORMULA (no cambiar sin medir CTR antes):
  - Fuente Anton (NO Impact, NO Arial) — descargada en _fuentes/
  - Setup pequeno en banda roja · cuerpo blanco · remate AMARILLO (la palabra que vende)
  - Composicion fija: texto izquierda / personaje derecha
  - Fondo casi negro con el sujeto recortado por la luz
  - Densidad alta: en este nicho, limpio = invisible
"""
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter
import sys, os, random, urllib.request
from pathlib import Path

AQUI = Path(__file__).parent
FUENTE = AQUI / "_fuentes" / "Anton-Regular.ttf"
W, H = 1280, 720

def asegurar_fuente():
    if FUENTE.exists():
        return
    FUENTE.parent.mkdir(exist_ok=True)
    url = "https://github.com/google/fonts/raw/main/ofl/anton/Anton-Regular.ttf"
    urllib.request.urlretrieve(url, FUENTE)
    print(f"Fuente Anton descargada en {FUENTE}")

def _textura(size, densidad=70):
    t = Image.new('L', size, 255); d = ImageDraw.Draw(t); w, h = size
    for _ in range(densidad):
        x, y = random.randint(0, w), random.randint(0, h)
        L = random.randint(8, 60); vert = random.choice([0, 0, 0, 1])
        x2 = x + (L if not vert else random.randint(-6, 6))
        y2 = y + (random.randint(-4, 4) if not vert else L)
        d.line([(x, y), (x2, y2)], fill=random.randint(90, 170), width=random.choice([1, 1, 2]))
    for _ in range(densidad // 2):
        x, y = random.randint(0, w), random.randint(0, h)
        d.ellipse([x, y, x + random.randint(1, 4), y + random.randint(1, 3)],
                  fill=random.randint(100, 180))
    return t

def _texto(base, xy, txt, font, color, contorno=6):
    bb = font.getbbox(txt)
    pw, ph = bb[2] - bb[0] + contorno * 4, bb[3] - bb[1] + contorno * 4
    cap = Image.new('RGBA', (pw, ph), (0, 0, 0, 0)); dc = ImageDraw.Draw(cap)
    ox, oy = contorno * 2 - bb[0], contorno * 2 - bb[1]
    for dx in range(-contorno, contorno + 1, 2):
        for dy in range(-contorno, contorno + 1, 2):
            dc.text((ox + dx, oy + dy), txt, font=font, fill=(0, 0, 0, 255))
    dc.text((ox, oy), txt, font=font, fill=color + (255,))
    relleno = Image.new('L', (pw, ph), 0)
    ImageDraw.Draw(relleno).text((ox, oy), txt, font=font, fill=255)
    cap.putalpha(Image.composite(_textura((pw, ph)), Image.new('L', (pw, ph), 255), relleno))
    base.alpha_composite(cap, xy)

def _banda(d, x, y, w, h, color=(196, 26, 26)):
    pts = [(x - 6, y + 8)]
    pts += [(x + w * i / 6, y - 6 + random.randint(-4, 5)) for i in range(1, 7)]
    pts += [(x + w + 4, y + h - 2)]
    pts += [(x + w * i / 6, y + h + 4 + random.randint(-5, 4)) for i in range(5, -1, -1)]
    d.polygon(pts, fill=color)

def crear(imagen, setup, cuerpo, remate, sub, sub_rojo, salida, semilla=7,
          esc=1.22, encuadrar=True):
    """esc: escala del texto. 1.22 = la revision del 2026-08-30 medida contra los
    outliers actuales del nicho (dedican casi la mitad del ancho al texto).
    Se descarto 1.40: gana legibilidad pero tapa la expresion del personaje.
    encuadrar=False si la imagen ya viene compuesta a 1280x720 (no reencuadrar)."""
    asegurar_fuente(); random.seed(semilla)
    im = Image.open(imagen).convert('RGB')
    if encuadrar:
        im = im.resize((int(W * 1.2), int(H * 1.2)), Image.LANCZOS)
        im = im.crop((im.width - W, (im.height - H) // 2, im.width, (im.height - H) // 2 + H))
    elif im.size != (W, H):
        im = im.resize((W, H), Image.LANCZOS)
    ov = Image.new('L', (W, H), 0); dv = ImageDraw.Draw(ov)
    for x in range(W):
        t = max(0.0, 1.0 - x / (W * 0.74))
        dv.line([(x, 0), (x, H)], fill=int(242 * (t ** 1.15)))
    im = Image.composite(Image.new('RGB', (W, H), (5, 5, 9)), im, ov.filter(ImageFilter.GaussianBlur(3)))
    im = ImageEnhance.Contrast(im).enhance(1.15).convert('RGBA')
    d = ImageDraw.Draw(im)

    esc = float(esc)
    fset = ImageFont.truetype(str(FUENTE), int(54 * esc))
    fbig = ImageFont.truetype(str(FUENTE), int(132 * esc))
    fsub = ImageFont.truetype(str(FUENTE), int(44 * esc))

    bb = fset.getbbox(setup); bw, bh = bb[2] - bb[0] + 52, bb[3] - bb[1] + 30
    _banda(d, 52, 44, bw, bh)
    d.text((78, 59 - bb[1]), setup, font=fset, fill=(255, 255, 255))

    y = 44 + bh + 30
    _texto(im, (44, y), cuerpo, fbig, (255, 255, 255)); y += int(140 * esc)
    _texto(im, (44, y), remate, fbig, (255, 206, 8)); y += int(150 * esc)
    xr = int(600 * esc)
    d.polygon([(56, y - 14), (xr, y - 24), (xr + 4, y - 6), (60, y + 4)], fill=(196, 26, 26))
    y += 14
    if sub:
        _texto(im, (52, y), sub, fsub, (255, 255, 255), contorno=4)
        w = fsub.getbbox(sub)[2] - fsub.getbbox(sub)[0]
        if sub_rojo:
            _texto(im, (52 + w + 18, y), sub_rojo, fsub, (228, 42, 42), contorno=4)

    im.convert('RGB').save(salida, quality=95)
    kb = os.path.getsize(salida) / 1024
    print(f"{salida}  —  1280x720  —  {kb:.0f} KB")
    return salida

if __name__ == "__main__":
    if len(sys.argv) < 8:
        print(__doc__); sys.exit(1)
    crear(*sys.argv[1:8])
