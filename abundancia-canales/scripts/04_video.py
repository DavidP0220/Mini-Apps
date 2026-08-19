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
    ap.add_argument("--oscuro", action="store_true",
        help="version 'pantalla oscura' para dormir: imagen muy atenuada, "
             "pesa mucho menos y es el formato con mas velocidad de vistas del nicho")
    ap.add_argument("--seg-imagen", type=int, default=SEG_POR_IMAGEN,
                    help="segundos que se ve cada imagen (por defecto 40)")
    a = ap.parse_args()
    canal, v = buscar(a.id)
    d = BASE / "salida" / a.id
    imgs = sorted([p for p in (d/"img").glob("*") if p.suffix.lower() in (".png",".jpg",".jpeg")])
    if len(imgs) < 3: sys.exit(f"Pon al menos 3 imagenes en {d/'img'}")
    audio = next((d/f"audio{e}" for e in (".flac", ".wav") if (d/f"audio{e}").exists()), None)
    if not audio: sys.exit(f"Falta {d}/audio.flac. Corre antes 03_audio.py")

    W,H = (3840,2160) if a.uhd else (1920,1080)
    SEG = a.seg_imagen
    ciclo = len(imgs)*SEG - 3*(len(imgs)-1)
    frames = SEG*FPS

    partes, filtros = [], []
    for i,p in enumerate(imgs):
        # 1 SOLO fotograma de entrada: zoompan expande CADA fotograma que recibe,
        # asi que alimentarlo con SEG*fps imagenes multiplica el render por ~200
        partes += ["-loop","1","-framerate","1","-t","1","-i",str(p)]
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
    # cada xfade acorta la linea de tiempo 3 s: el texto se calcula sobre
    # la duracion REAL para que nunca se superpongan dos afirmaciones
    paso = SEG - 3
    draws = []
    for i,txt in enumerate(AFIRM[:len(imgs)]):
        ini = i*paso + 2; fin = ini + max(4, paso - 4)
        draws.append(f"drawtext=text='{esc(txt)}':fontcolor=white@0.92:fontsize={H//26}:"
                     f"x=(w-text_w)/2:y=h*0.82:shadowcolor=black@0.6:shadowx=2:shadowy=2:"
                     f"enable='between(t,{ini},{fin})'")
    marca = (f"drawtext=text='{esc(canal['nombre'])}':fontcolor=white@0.35:fontsize={H//45}:"
             f"x=w-text_w-40:y=40")
    # en modo oscuro la imagen se atenua ANTES del texto, para que la
    # afirmacion siga legible sobre el fondo casi negro
    atenua = ["eq=brightness=-0.42:saturation=0.55"] if a.oscuro else []
    fc = ";".join(filtros + cad) + f";[{prev}]" + ",".join(atenua+draws+[marca]) + "[vout]"

    ciclo_mp4 = d/"_ciclo.mp4"
    print(f"[1/2] Ciclo visual de {ciclo}s con {len(imgs)} imagenes a {W}x{H}")
    subprocess.run(["ffmpeg","-y","-v","error",*partes,"-filter_complex",fc,"-map","[vout]",
        "-c:v","libx264","-preset","veryfast","-crf","23","-maxrate","2200k","-bufsize","4400k","-g","240","-threads","0","-pix_fmt","yuv420p",str(ciclo_mp4)],check=True)

    # duracion exacta del audio: -shortest no corta bien con -stream_loop -1
    dur = float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
        "-of","default=nw=1:nk=1",str(audio)],capture_output=True,text=True).stdout.strip())
    final = d/(f"{a.id}-oscuro.mp4" if a.oscuro else f"{a.id}.mp4")
    print(f"[2/2] Bucle a {v['horas']} h + audio -> {final}")
    subprocess.run(["ffmpeg","-y","-v","error","-stream_loop","-1","-i",str(ciclo_mp4),
        "-i",str(audio),"-t",f"{dur:.3f}","-c:v","copy","-c:a","aac","-b:a","320k",
        "-movflags","+faststart",str(final)],check=True)
    ciclo_mp4.unlink(missing_ok=True)
    print(f"LISTO -> {final}")

if __name__ == "__main__":
    main()
