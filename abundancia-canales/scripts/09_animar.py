# -*- coding: utf-8 -*-
"""Convierte una imagen fija en un plano con profundidad real y vida propia.

No es un zoom lento: separa la imagen en capas por profundidad y las mueve a
distinta velocidad, que es como el ojo percibe el volumen. Encima suma
particulas con profundidad, un barrido de luz volumetrica, respiracion de
brillo y grano fino de pelicula.

Todo en bucle PERFECTO: el ultimo fotograma empalma con el primero, asi que se
puede repetir 8 horas sin que se note el corte.

Capas (de fondo a frente):
  1. Fondo desenfocado, se mueve poco  -> lejania
  2. Imagen nitida, se mueve medio     -> plano principal
  3. Particulas lejanas, pequenas y lentas
  4. Barrido de luz volumetrica
  5. Particulas cercanas, grandes y rapidas, con desenfoque
  6. Vineta que respira + grano

Uso:
  python3 scripts/09_animar.py --img salida/lakshmi-11/img/1.png --seg 20
  python3 scripts/09_animar.py --img ... --seg 24 --intensidad 1.3 --4k
"""
import argparse, math, pathlib, random, shutil, subprocess, sys, tempfile
from PIL import Image, ImageDraw, ImageFilter, ImageChops

FPS = 24


def capa_particulas(n, semilla, w, h, cerca):
    """Particulas con trayectoria ciclica: al final del clip vuelven al inicio."""
    random.seed(semilla)
    ps = []
    for _ in range(n):
        ps.append({
            "x": random.uniform(-0.05, 1.05) * w,
            "y": random.uniform(-0.05, 1.05) * h,
            "r": random.uniform(2.5, 7.0) if cerca else random.uniform(0.8, 2.6),
            "amp": random.uniform(25, 70) if cerca else random.uniform(6, 22),
            "fase": random.uniform(0, 2 * math.pi),
            "vueltas": random.choice([1, 1, 2]),
            "alfa": random.randint(70, 190) if cerca else random.randint(30, 95),
            "deriva": random.uniform(-1, 1),
        })
    return ps


def dibuja(ps, t, w, h, desenfoque):
    capa = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    for p in ps:
        ang = 2 * math.pi * p["vueltas"] * t + p["fase"]
        x = p["x"] + math.cos(ang) * p["amp"] + p["deriva"] * math.sin(2 * math.pi * t) * 18
        y = p["y"] + math.sin(ang) * p["amp"] * 0.55
        al = int(p["alfa"] * (0.5 + 0.5 * math.sin(ang * 2)))
        r = p["r"]
        d.ellipse([x - r, y - r, x + r, y + r], fill=(255, 231, 163, al))
        if r > 4:                                     # halo suave en las grandes
            d.ellipse([x - r*2.4, y - r*2.4, x + r*2.4, y + r*2.4],
                      fill=(255, 216, 130, al // 6))
    return capa.filter(ImageFilter.GaussianBlur(desenfoque))


def rayo_de_luz(w, h, t, fuerza):
    """Barrido de luz volumetrica que cruza la escena y vuelve, sin salto."""
    capa = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(capa)
    cx = w * (0.5 + 0.42 * math.sin(2 * math.pi * t))
    ancho = w * 0.20
    for i in range(int(ancho)):
        v = int(255 * (1 - abs(i - ancho / 2) / (ancho / 2)) ** 2)
        d.line([(cx - ancho/2 + i, 0), (cx - ancho/2 + i - w*0.12, h)], fill=v)
    capa = capa.filter(ImageFilter.GaussianBlur(w * 0.035))
    color = Image.new("RGB", (w, h), (255, 226, 168))
    out = Image.new("RGBA", (w, h))
    out.paste(color, (0, 0))
    out.putalpha(capa.point(lambda p: int(p * fuerza)))
    return out


def main():
    if not shutil.which("ffmpeg"):
        sys.exit("Falta ffmpeg.")
    ap = argparse.ArgumentParser()
    ap.add_argument("--img", required=True)
    ap.add_argument("--seg", type=int, default=20)
    ap.add_argument("--intensidad", type=float, default=1.0,
                    help="multiplica el movimiento y los efectos (0.6 sutil, 1.5 marcado)")
    ap.add_argument("--particulas", type=int, default=110)
    ap.add_argument("--4k", dest="uhd", action="store_true")
    ap.add_argument("--salida")
    a = ap.parse_args()

    W, H = (3840, 2160) if a.uhd else (1920, 1080)
    src = pathlib.Path(a.img)
    out = pathlib.Path(a.salida) if a.salida else src.with_name(src.stem + "-vivo.mp4")
    total = a.seg * FPS
    k = a.intensidad

    base = Image.open(src).convert("RGB")
    # el fondo se amplia mas: al moverse menos, necesita menos margen
    fondo = base.resize((int(W * 1.22), int(H * 1.22)), Image.LANCZOS).filter(
        ImageFilter.GaussianBlur(W * 0.006))
    frente = base.resize((int(W * 1.14), int(H * 1.14)), Image.LANCZOS)

    # mascara de profundidad por luminancia: lo brillante se toma como cercano
    lum = base.convert("L").resize(frente.size, Image.LANCZOS).filter(
        ImageFilter.GaussianBlur(W * 0.012))
    mask = lum.point(lambda p: min(255, int(p * 1.25)))

    lejanas = capa_particulas(int(a.particulas * 0.62), hash(src.name) % 9999, W, H, False)
    cercanas = capa_particulas(int(a.particulas * 0.38), hash(src.name) % 7777, W, H, True)

    print(f"[1/2] Componiendo {total} fotogramas con profundidad ({W}x{H})")
    tmp = pathlib.Path(tempfile.mkdtemp())
    vineta = Image.new("L", (W, H), 0)
    dv = ImageDraw.Draw(vineta)
    dv.ellipse([-W*0.25, -H*0.25, W*1.25, H*1.25], fill=255)
    vineta = vineta.filter(ImageFilter.GaussianBlur(W * 0.09))

    for f in range(total):
        t = f / total
        ang = 2 * math.pi * t
        # 1) fondo: deriva minima
        fx = (fondo.width - W) / 2 + math.cos(ang) * W * 0.010 * k
        fy = (fondo.height - H) / 2 + math.sin(ang) * H * 0.008 * k
        cuadro = fondo.crop((int(fx), int(fy), int(fx) + W, int(fy) + H)).convert("RGBA")

        # 2) frente: se mueve el triple -> paralaje
        px = (frente.width - W) / 2 + math.cos(ang) * W * 0.030 * k
        py = (frente.height - H) / 2 + math.sin(ang) * H * 0.024 * k
        cap_f = frente.crop((int(px), int(py), int(px) + W, int(py) + H))
        m = mask.crop((int(px), int(py), int(px) + W, int(py) + H))
        cuadro.paste(cap_f, (0, 0), m)

        # 3) particulas lejanas
        cuadro = Image.alpha_composite(cuadro, dibuja(lejanas, t, W, H, 1.0))
        # 4) rayo de luz
        cuadro = Image.alpha_composite(cuadro, rayo_de_luz(W, H, t, 0.13 * k))
        # 5) particulas cercanas, con desenfoque de profundidad de campo
        cuadro = Image.alpha_composite(cuadro, dibuja(cercanas, t, W, H, 2.6))
        # 6) vineta que respira
        v = vineta.point(lambda p, s=(0.86 + 0.06 * math.sin(ang)): int(p * s))
        oscuro = Image.new("RGB", (W, H), (0, 0, 0))
        cuadro = Image.composite(cuadro.convert("RGB"), oscuro, v)
        cuadro.save(tmp / f"f{f:05d}.jpg", quality=95)

        if f % 60 == 0:
            print(f"    {f}/{total}")

    print("[2/2] Codificando con grano fino")
    subprocess.run([
        "ffmpeg", "-y", "-v", "error", "-framerate", str(FPS),
        "-i", str(tmp / "f%05d.jpg"),
        "-vf", "noise=alls=3:allf=t+u,format=yuv420p",
        "-c:v", "libx264", "-preset", "medium", "-crf", "19",
        str(out)], check=True)
    shutil.rmtree(tmp, ignore_errors=True)
    print(f"LISTO -> {out}  ({a.seg}s, bucle perfecto, {FPS} fps)")


if __name__ == "__main__":
    main()
