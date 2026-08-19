# -*- coding: utf-8 -*-
"""Crea un Short vertical (9:16) de 45 s a partir de los mismos insumos del
video largo. Los Shorts son el motor de descubrimiento: llevan gente al canal
y de ahi a los videos de 1 y 3 horas.

Toma la imagen mas fuerte del video, le hace un zoom lento, le pone el texto
de la miniatura arriba, una afirmacion abajo y un llamado a la accion final.

Uso:
  python3 scripts/08_short.py --id lakshmi-01
  python3 scripts/08_short.py --id lakshmi-01 --img salida/lakshmi-01/img/2.png --seg 30
"""
import argparse, json, pathlib, shutil, subprocess, sys

BASE = pathlib.Path(__file__).resolve().parent.parent
CAT = json.loads((BASE / "datos" / "catalogo.json").read_text(encoding="utf-8"))
W, H, FPS = 1080, 1920, 30
AFIRM = "Money flows to me easily and constantly."


def buscar(vid):
    for c in CAT["canales"]:
        for v in c["videos"]:
            if v["id"] == vid:
                return c, v
    sys.exit(f"No existe el id {vid}")


def esc(t):
    return t.replace("\\", "\\\\").replace(":", "\\:").replace("'", "’")


def main():
    if not shutil.which("ffmpeg"):
        sys.exit("Falta ffmpeg.")
    ap = argparse.ArgumentParser()
    ap.add_argument("--id", required=True)
    ap.add_argument("--img", help="imagen a usar (por defecto la primera del video)")
    ap.add_argument("--seg", type=int, default=45, help="duracion del Short (max 60)")
    a = ap.parse_args()
    canal, v = buscar(a.id)
    d = BASE / "salida" / a.id
    # el audio sale del intermedio si existe; si ya lo borraste, se toma del
    # propio video final, que es igual de valido y evita rehacer media hora de CPU
    audio = next((d/f"audio{e}" for e in (".flac", ".wav") if (d/f"audio{e}").exists()), None)
    if not audio:
        audio = d/f"{a.id}.mp4"
    if not audio.exists():
        sys.exit(f"No hay audio en {d}. Corre antes 03_audio.py o 04_video.py")
    img = pathlib.Path(a.img) if a.img else next(iter(sorted((d / "img").glob("*"))), None)
    if not img or not img.exists():
        sys.exit(f"No hay imagenes en {d/'img'}")
    seg = min(a.seg, 60)          # YouTube corta los Shorts en 60 s
    frames = seg * FPS

    # el audio se toma del minuto 1 del video largo, que es donde ya entro el ambiente
    fc = (
        f"[0:v]scale=-1:{int(H*1.35)},zoompan=z='min(1+0.18*on/{frames},1.18)':"
        f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s={W}x{H}:fps={FPS},"
        f"setsar=1,format=yuv420p,"
        f"drawtext=text='{esc(v['miniatura_texto'])}':fontcolor=0xFFD700:fontsize=96:"
        f"x=(w-text_w)/2:y=h*0.13:borderw=8:bordercolor=black@0.85,"
        f"drawtext=text='{esc(str(v['hz']))} Hz':fontcolor=white:fontsize=58:"
        f"x=(w-text_w)/2:y=h*0.22:borderw=5:bordercolor=black@0.85,"
        f"drawtext=text='{esc(AFIRM)}':fontcolor=white@0.95:fontsize=46:"
        f"x=(w-text_w)/2:y=h*0.72:borderw=4:bordercolor=black@0.8,"
        f"drawtext=text='Full {v['horas']}h version on the channel':fontcolor=0xFFD700:"
        f"fontsize=44:x=(w-text_w)/2:y=h*0.80:borderw=4:bordercolor=black@0.8:"
        f"enable='gte(t,{seg-12})'[vout]"
    )
    out = d / f"{a.id}-short.mp4"
    print(f"Renderizando Short vertical de {seg}s ({W}x{H})")
    subprocess.run([
        "ffmpeg", "-y", "-v", "error", "-loop", "1", "-framerate", "1", "-t", "1", "-i", str(img),
        "-ss", "60", "-t", str(seg), "-i", str(audio),
        "-filter_complex", fc, "-map", "[vout]", "-map", "1:a",
        "-af", f"afade=t=in:st=0:d=2,afade=t=out:st={seg-3}:d=3",
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "22", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(out)], check=True)
    print(f"LISTO -> {out}")
    print("Subelo como Short. En la descripcion pon el enlace al video largo.")


if __name__ == "__main__":
    main()
