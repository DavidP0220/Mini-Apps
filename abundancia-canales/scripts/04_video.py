# -*- coding: utf-8 -*-
"""Renderiza el video final 1080p (o 4K) con efecto Ken Burns y afirmaciones.

Entradas:
  salida/<id>/img/*.png|jpg   -> 5+ imagenes generadas con IA
  salida/<id>/audio.wav       -> audio ya construido con 03_audio.py
Salida:
  salida/<id>/<id>.mp4

Truco de rendimiento: en vez de renderizar 8 h de video, se crea UN ciclo
visual de ~10 min (imagenes con paneo lento + afirmaciones) y se repite en
bucle a nivel de contenedor. El resultado pesa poco y sube rapido.

Uso:
  python3 scripts/04_video.py --id lakshmi-01
  python3 scripts/04_video.py --id lakshmi-01 --4k
"""
import argparse, json, pathlib, shutil, subprocess, sys

BASE = pathlib.Path(__file__).resolve().parent.parent
CAT = json.loads((BASE / "datos" / "catalogo.json").read_text(encoding="utf-8"))
SEG_POR_IMAGEN = 40      # cada imagen se ve 40 s
FPS = 24            # el paneo es lento: 24 fps basta y el render es mucho mas rapido

AFIRM = ["Money flows to me easily and constantly.","I am a magnet for wealth and opportunity.",
 "Everything I need is already on its way to me.","I receive with gratitude and I give with joy.",
 "My income grows while I rest.","Doors open for me in the perfect timing."]

def buscar(vid):
    for c in CAT["canales"]:
        for v in c["videos"]:
            if v["id"] == vid: return c, v
    sys.exit(f"No existe el id {vid}")

def esc(t):
    return t.replace("\\","\\\\").replace(":","\\:").replace("'","\u2019")

def main():
    if not shutil.which("ffmpeg"):
        sys.exit("Falta ffmpeg. Windows -> winget install Gyan.FFmpeg | Mac -> brew install ffmpeg")
    ap = argparse.ArgumentParser()
    ap.add_argument("--id", required=True)
    ap.add_argument("--4k", dest="uhd", action="store_true")
    ap.add_argument("--seg-imagen", type=int, default=SEG_POR_IMAGEN,
                    help="segundos que se ve cada imagen (por defecto 40)")
    a = ap.parse_args()
    canal, v = buscar(a.id)
    d = BASE / "salida" / a.id
    imgs = sorted([p for p in (d/"img").glob("*") if p.suffix.lower() in (".png",".jpg",".jpeg")])
    if len(imgs) < 3: sys.exit(f"Pon al menos 3 imagenes en {d/'img'}")
    audio = d/"audio.wav"
    if not audio.exists(): sys.exit(f"Falta {audio}. Corre antes 03_audio.py")

    W,H = (3840,2160) if a.uhd else (1920,1080)
    SEG = a.seg_imagen
    ciclo = len(imgs)*SEG
    frames = SEG*FPS

    partes, filtros = [], []
    for i,p in enumerate(imgs):
        partes += ["-loop","1","-t",str(SEG),"-i",str(p)]
        # Ken Burns: zoom lento 1.00 -> 1.12 con leve paneo
        filtros.append(
            f"[{i}:v]scale={int(W*1.25)}:-1,zoompan=z='min(1+0.12*on/{frames},1.12)':"
            f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s={W}x{H}:fps={FPS},"
            f"setsar=1,format=yuv420p[v{i}]")
    # encadenar con cross dissolve de 3 s
    cad, prev = [], "v0"
    for i in range(1,len(imgs)):
        off = SEG*i - 3*i
        cad.append(f"[{prev}][v{i}]xfade=transition=fade:duration=3:offset={off}[x{i}]")
        prev = f"x{i}"
    # afirmaciones: una cada SEG_POR_IMAGEN, con fade
    draws = []
    for i,txt in enumerate(AFIRM[:len(imgs)]):
        ini = i*SEG + max(2, SEG//7); fin = ini + max(6, SEG//2)
        draws.append(f"drawtext=text='{esc(txt)}':fontcolor=white@0.92:fontsize={H//26}:"
                     f"x=(w-text_w)/2:y=h*0.82:shadowcolor=black@0.6:shadowx=2:shadowy=2:"
                     f"enable='between(t,{ini},{fin})'")
    marca = (f"drawtext=text='{esc(canal['nombre'])}':fontcolor=white@0.35:fontsize={H//45}:"
             f"x=w-text_w-40:y=40")
    fc = ";".join(filtros + cad) + f";[{prev}]" + ",".join(draws+[marca]) + "[vout]"

    ciclo_mp4 = d/"_ciclo.mp4"
    print(f"[1/2] Ciclo visual de {ciclo}s con {len(imgs)} imagenes a {W}x{H}")
    subprocess.run(["ffmpeg","-y","-v","error",*partes,"-filter_complex",fc,"-map","[vout]",
        "-c:v","libx264","-preset","veryfast","-crf","21","-threads","0","-pix_fmt","yuv420p",str(ciclo_mp4)],check=True)

    final = d/f"{a.id}.mp4"
    print(f"[2/2] Bucle a {v['horas']} h + audio -> {final}")
    subprocess.run(["ffmpeg","-y","-v","error","-stream_loop","-1","-i",str(ciclo_mp4),
        "-i",str(audio),"-shortest","-c:v","copy","-c:a","aac","-b:a","320k",
        "-movflags","+faststart",str(final)],check=True)
    ciclo_mp4.unlink(missing_ok=True)
    print(f"LISTO -> {final}")

if __name__ == "__main__":
    main()
