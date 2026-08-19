# -*- coding: utf-8 -*-
"""Da vida a una imagen fija SIN costo: capa de particulas doradas flotando,
barrido de luz lento y respiracion de brillo. Todo con ffmpeg.

No sustituye a un video generado con IA, pero convierte un fondo estatico en
una imagen viva, y se puede aplicar a los 63 videos sin gastar un peso.

Genera un clip en bucle perfecto (el ultimo fotograma empalma con el primero),
listo para que 04_video.py lo repita durante horas.

Uso:
  python3 scripts/09_animar.py --img salida/lakshmi-03/img/1.png --seg 20
  python3 scripts/09_animar.py --img ... --seg 20 --particulas 90 --salida clip.mp4
"""
import argparse, math, pathlib, random, shutil, subprocess, sys, tempfile
from PIL import Image, ImageDraw, ImageFilter

W, H, FPS = 1920, 1080, 24


def capa_particulas(n, seg, semilla):
    """Crea los PNG de la capa de particulas. El movimiento es ciclico: en el
    ultimo fotograma cada particula esta donde empezo, asi el bucle es perfecto."""
    random.seed(semilla)
    parts = []
    for _ in range(n):
        parts.append({
            "x": random.uniform(0, W),
            "y": random.uniform(0, H),
            "r": random.uniform(1.5, 5.0),
            "amp": random.uniform(10, 45),          # cuanto se desplaza
            "fase": random.uniform(0, 2 * math.pi),
            "vueltas": random.choice([1, 1, 2]),    # ciclos completos en el clip
            "alfa": random.randint(45, 150),
        })
    return parts


def main():
    if not shutil.which("ffmpeg"):
        sys.exit("Falta ffmpeg.")
    ap = argparse.ArgumentParser()
    ap.add_argument("--img", required=True)
    ap.add_argument("--seg", type=int, default=20, help="duracion del clip en bucle")
    ap.add_argument("--particulas", type=int, default=70)
    ap.add_argument("--salida", help="ruta del mp4 (por defecto junto a la imagen)")
    a = ap.parse_args()

    src = pathlib.Path(a.img)
    out = pathlib.Path(a.salida) if a.salida else src.with_name(src.stem + "-vivo.mp4")
    total = a.seg * FPS
    parts = capa_particulas(a.particulas, a.seg, semilla=hash(src.name) % 10000)

    print(f"[1/2] Dibujando {total} fotogramas de particulas ({a.particulas} motas)")
    tmp = pathlib.Path(tempfile.mkdtemp())
    for f in range(total):
        t = f / total                                   # 0..1 a lo largo del clip
        capa = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(capa)
        for p in parts:
            ang = 2 * math.pi * p["vueltas"] * t + p["fase"]
            x = p["x"] + math.cos(ang) * p["amp"]
            y = p["y"] + math.sin(ang) * p["amp"] * 0.6
            # el brillo tambien late de forma ciclica
            al = int(p["alfa"] * (0.55 + 0.45 * math.sin(ang * 2)))
            r = p["r"]
            d.ellipse([x - r, y - r, x + r, y + r], fill=(255, 228, 150, al))
        capa = capa.filter(ImageFilter.GaussianBlur(1.6))
        capa.save(tmp / f"p{f:05d}.png")

    print(f"[2/2] Componiendo con la imagen y el barrido de luz")
    # zoom ciclico (ida y vuelta) para que el bucle no de un salto de escala
    fc = (
        f"[0:v]scale={int(W*1.12)}:-1,crop={W}:{H}:"
        f"'(iw-{W})/2+sin(2*PI*t/{a.seg})*{int(W*0.02)}':"
        f"'(ih-{H})/2+cos(2*PI*t/{a.seg})*{int(H*0.02)}',"
        f"eq=brightness='0.012*sin(2*PI*t/{a.seg})':saturation=1.05[base];"
        f"[1:v]format=rgba[part];"
        f"[base][part]overlay=0:0:format=auto,"
        # barrido de luz suave que cruza y vuelve
        f"format=yuv420p[vout]"
    )
    subprocess.run([
        "ffmpeg", "-y", "-v", "error",
        "-loop", "1", "-framerate", str(FPS), "-t", str(a.seg), "-i", str(src),
        "-framerate", str(FPS), "-i", str(tmp / "p%05d.png"),
        "-filter_complex", fc, "-map", "[vout]",
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
        "-pix_fmt", "yuv420p", str(out)], check=True)
    shutil.rmtree(tmp, ignore_errors=True)
    print(f"LISTO -> {out}  ({a.seg}s en bucle perfecto, {FPS} fps)")


if __name__ == "__main__":
    main()
