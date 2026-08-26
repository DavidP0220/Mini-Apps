#!/usr/bin/env python3
"""
Guardian determinista (capa 1) para Mindset Mechanics.
Revisa especificaciones OBJETIVAS de un video/imagen antes de publicar:
resolucion, duracion, existencia de archivo. No juzga nada subjetivo
(eso es trabajo del thumbnail-consistency-guardian, capa 2).

Uso:
    python check_video_specs.py <ruta_archivo> [--min-width 1080] [--min-height 1080] [--min-duration-s 0]

Sale con codigo 0 y "PASS" si todo cumple, codigo 1 y "FAIL" con la
lista de fallos si algo no cumple. Pensado para ser llamado por un
agente o por un humano, y para que su resultado nunca dependa de
interpretacion de lenguaje natural.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

FFPROBE_CANDIDATES = [
    "ffprobe",
    r"C:\Users\David Peñuela\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0-full_build\bin\ffprobe.exe",
]


def find_ffprobe():
    for candidate in FFPROBE_CANDIDATES:
        try:
            subprocess.run([candidate, "-version"], capture_output=True, check=True)
            return candidate
        except (FileNotFoundError, subprocess.CalledProcessError, OSError):
            continue
    return None


def probe(path, ffprobe):
    cmd = [
        ffprobe, "-v", "error",
        "-select_streams", "v:0",
        "-show_entries", "stream=width,height",
        "-show_entries", "format=duration",
        "-of", "json",
        str(path),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        return None
    data = json.loads(result.stdout)
    stream = (data.get("streams") or [{}])[0]
    fmt = data.get("format") or {}
    return {
        "width": stream.get("width"),
        "height": stream.get("height"),
        "duration": float(fmt["duration"]) if fmt.get("duration") else None,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--min-width", type=int, default=1080)
    ap.add_argument("--min-height", type=int, default=1080)
    ap.add_argument("--min-duration-s", type=float, default=0.0)
    args = ap.parse_args()

    path = Path(args.path)
    failures = []

    if not path.exists():
        print("FAIL")
        print(f"- El archivo no existe: {path}")
        sys.exit(1)

    ffprobe = find_ffprobe()
    if not ffprobe:
        print("FAIL")
        print("- ffprobe no encontrado en este sistema; no se puede verificar de forma determinista.")
        sys.exit(1)

    info = probe(path, ffprobe)
    if info is None:
        print("FAIL")
        print(f"- ffprobe no pudo leer el archivo: {path}")
        sys.exit(1)

    w, h, dur = info["width"], info["height"], info["duration"]

    if w is None or h is None:
        failures.append("No se pudo leer resolución del video (¿tiene stream de video?).")
    else:
        if w < args.min_width and h < args.min_width:
            failures.append(f"Resolución {w}x{h} por debajo del mínimo requerido ({args.min_width}p).")
        # para video vertical, el lado relevante es el mayor de los dos
        max_side = max(w, h)
        if max_side < args.min_height:
            failures.append(f"Resolución {w}x{h} — lado mayor ({max_side}) por debajo de {args.min_height}p.")

    if args.min_duration_s > 0:
        if dur is None:
            failures.append("No se pudo leer la duración del video.")
        elif dur < args.min_duration_s:
            failures.append(f"Duración {dur:.1f}s por debajo del mínimo requerido ({args.min_duration_s}s).")

    if failures:
        print("FAIL")
        for f in failures:
            print(f"- {f}")
        sys.exit(1)
    else:
        print("PASS")
        print(f"- Resolución: {w}x{h}")
        if dur is not None:
            print(f"- Duración: {dur:.1f}s")
        sys.exit(0)


if __name__ == "__main__":
    main()
