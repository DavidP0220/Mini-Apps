# -*- coding: utf-8 -*-
"""Construye el audio final de un video, de una melodia corta a N horas.

Metodo del bucle SIN saltos (esto es lo que hace que se pueda escuchar 8 h
seguidas sin molestar):

  1. Se toma la cola de la pista y se funde con su propia cabeza (acrossfade).
  2. Ese fundido se pega delante del cuerpo -> queda una "unidad" cuyo final
     empalma exactamente con su principio.
  3. La unidad se repite las veces necesarias: las uniones son inaudibles.
  4. Encima se suma la onda senoidal pura de la frecuencia del video y se
     normaliza el volumen al estandar de YouTube (-16 LUFS).

El resultado se guarda en FLAC (sin perdida y la mitad de peso que WAV: un
video de 8 h ocupa ~1,5 GB en vez de ~5 GB).

Uso:
  python3 scripts/03_audio.py --id lakshmi-01 --base bases/lakshmi-01.wav
  python3 scripts/03_audio.py --id lakshmi-01 --base ... --prueba 60
"""
import argparse, json, math, pathlib, shutil, subprocess, sys

BASE = pathlib.Path(__file__).resolve().parent.parent
CAT = json.loads((BASE / "datos" / "catalogo.json").read_text(encoding="utf-8"))
XF = 12          # segundos de fundido en la union del bucle


def buscar(vid):
    for c in CAT["canales"]:
        for v in c["videos"]:
            if v["id"] == vid:
                return c, v
    sys.exit(f"No existe el id {vid}")


def dur(path):
    o = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "default=nw=1:nk=1", str(path)], capture_output=True, text=True)
    return float(o.stdout.strip())


def main():
    if not shutil.which("ffmpeg"):
        sys.exit("Falta ffmpeg. Windows: winget install Gyan.FFmpeg | Mac: brew install ffmpeg")
    ap = argparse.ArgumentParser()
    ap.add_argument("--id", required=True)
    ap.add_argument("--base", required=True, help="melodia base (2-5 min)")
    ap.add_argument("--tono-db", type=float, default=-30.0, help="volumen de la onda senoidal")
    ap.add_argument("--prueba", type=int, default=0, metavar="SEG",
                    help="renderiza solo N segundos para revisar antes del render final")
    a = ap.parse_args()

    canal, v = buscar(a.id)
    dest = BASE / "salida" / a.id
    dest.mkdir(parents=True, exist_ok=True)
    total = a.prueba if a.prueba else v["horas"] * 3600
    d = dur(a.base)
    if d < 3 * XF:
        sys.exit(f"La melodia base debe durar al menos {3*XF} s (ideal 2-5 min). Dura {d:.0f} s.")

    # 1) unidad que empalma consigo misma
    unidad = dest / "_unidad.flac"
    print(f"[1/3] Creando unidad de bucle sin saltos (fundido de {XF} s)")
    fc = (f"[0:a]atrim={d-XF}:{d},asetpts=N/SR/TB[cola];"
          f"[0:a]atrim=0:{XF},asetpts=N/SR/TB[cabeza];"
          f"[cola][cabeza]acrossfade=d={XF}:c1=tri:c2=tri[union];"
          f"[0:a]atrim={XF}:{d-XF},asetpts=N/SR/TB[cuerpo];"
          f"[union][cuerpo]concat=n=2:v=0:a=1[out]")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(a.base),
                    "-filter_complex", fc, "-map", "[out]",
                    "-ac", "2", "-ar", "48000", str(unidad)], check=True)

    paso = dur(unidad)
    reps = math.ceil(total / paso)
    print(f"[2/3] Repitiendo x{reps} y sumando la senoidal de {v['hz']} Hz a {a.tono_db} dB")

    # 2) bucle + capa de frecuencia + fundidos + normalizacion
    final = dest / "audio.flac"
    fin_fade = max(total - 20, 1)
    fc2 = (f"[1:a]volume={a.tono_db}dB,highpass=f=20[t];"
           f"[0:a][t]amix=inputs=2:duration=first:normalize=0,"
           f"atrim=0:{total},"
           f"afade=t=in:st=0:d=8,afade=t=out:st={fin_fade}:d=20,"
           f"loudnorm=I=-16:TP=-1.5:LRA=11[out]")
    subprocess.run(["ffmpeg", "-y", "-v", "error",
                    "-stream_loop", str(reps), "-i", str(unidad),
                    "-f", "lavfi", "-t", str(total),
                    "-i", f"sine=frequency={v['hz']}:sample_rate=48000",
                    "-filter_complex", fc2, "-map", "[out]",
                    "-ac", "2", "-ar", "48000", str(final)], check=True)
    unidad.unlink(missing_ok=True)
    mb = final.stat().st_size / 1e6
    print(f"[3/3] LISTO -> {final}  ({total/3600:.2f} h, {v['hz']} Hz, {mb:.0f} MB)")


if __name__ == "__main__":
    main()
