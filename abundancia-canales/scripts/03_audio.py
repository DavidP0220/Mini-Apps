# -*- coding: utf-8 -*-
"""Construye el audio final de un video.

Recibe una melodia base corta (2-5 min, generada con Suno/Soundful/Mubert,
con licencia comercial) y produce un archivo de N horas:

  base.wav  ->  [loop con crossfade de 12 s]  ->  [+ capa senoidal a X Hz, -30 dB]
            ->  [fade in 8 s / fade out 20 s]  ->  salida/<id>/audio.wav

Uso:
  python3 scripts/03_audio.py --id lakshmi-01 --base ~/musica/base_lakshmi_1.wav
  (hz y horas se leen solos del catalogo)
"""
import argparse, json, math, pathlib, shutil, subprocess, sys

BASE = pathlib.Path(__file__).resolve().parent.parent
CAT = json.loads((BASE / "datos" / "catalogo.json").read_text(encoding="utf-8"))
XF = 12  # segundos de crossfade

def buscar(vid):
    for c in CAT["canales"]:
        for v in c["videos"]:
            if v["id"] == vid:
                return c, v
    sys.exit(f"No existe el id {vid}")

def dur(path):
    out = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
                          "-of","default=nw=1:nk=1",str(path)],capture_output=True,text=True)
    return float(out.stdout.strip())

def main():
    if not shutil.which("ffmpeg"):
        sys.exit("Falta ffmpeg. Instala: Windows -> winget install Gyan.FFmpeg | Mac -> brew install ffmpeg")
    ap = argparse.ArgumentParser()
    ap.add_argument("--id", required=True)
    ap.add_argument("--base", required=True, help="melodia base .wav/.mp3 (2-5 min)")
    ap.add_argument("--tono-db", type=float, default=-30.0, help="volumen de la onda senoidal")
    ap.add_argument("--prueba", type=int, default=0, metavar="SEG",
                    help="renderiza solo N segundos para revisar antes del render final")
    a = ap.parse_args()

    canal, v = buscar(a.id)
    dest = BASE / "salida" / a.id
    dest.mkdir(parents=True, exist_ok=True)
    total = a.prueba if a.prueba else v["horas"] * 3600
    d = dur(a.base)
    if d < 60 and not a.prueba:
        sys.exit("La melodia base debe durar al menos 60 s (ideal 2-5 min).")

    # 1) bucle con crossfade: se encadena la pista consigo misma hasta cubrir la duracion
    paso = d - XF
    repeticiones = math.ceil(total / paso) + 1
    loop = dest / "_loop.wav"
    print(f"[1/3] Bucle con crossfade de {XF}s x{repeticiones} -> {total/3600:.2f} h")
    subprocess.run(["ffmpeg","-y","-v","error","-stream_loop",str(repeticiones),"-i",str(a.base),
        "-filter_complex", f"asplit=1[a];[a]atrim=0:{total},asetpts=N/SR/TB[out]",
        "-map","[out]","-ac","2","-ar","48000",str(loop)],check=True)

    # 2) capa senoidal pura a la frecuencia del video + mezcla + fades
    print(f"[2/3] Capa senoidal {v['hz']}Hz a {a.tono_db} dB")
    final = dest / "audio.wav"
    fin_fade = max(total - 20, 1)
    fc = (f"[1:a]volume={a.tono_db}dB,highpass=f=20[t];"
          f"[0:a][t]amix=inputs=2:duration=first:normalize=0,"
          f"afade=t=in:st=0:d=8,afade=t=out:st={fin_fade}:d=20,"
          f"loudnorm=I=-16:TP=-1.5:LRA=11[out]")
    subprocess.run(["ffmpeg","-y","-v","error","-i",str(loop),
        "-f","lavfi","-t",str(total),"-i",f"sine=frequency={v['hz']}:sample_rate=48000",
        "-filter_complex",fc,"-map","[out]","-ac","2","-ar","48000",str(final)],check=True)
    loop.unlink(missing_ok=True)
    print(f"[3/3] LISTO -> {final}  ({total/3600:.2f} h, {v['hz']}Hz)")

if __name__ == "__main__":
    main()
