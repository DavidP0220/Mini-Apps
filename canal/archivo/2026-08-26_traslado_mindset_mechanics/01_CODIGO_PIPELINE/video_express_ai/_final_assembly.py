"""Ensamblaje final: pista visual + voiceover + 412 subtitulos quemados +
badge de suscripcion (ultimos 20s). Aplica los overlays de subtitulos en
lotes incrementales (evita el limite de linea de comandos de Windows sin
depender de -filter_complex_script, que este build de ffmpeg no soporta,
ni de @archivo, que no parseo bien aqui)."""
import json
import shutil
import subprocess

from _paths import RESILIENCE_V2, VE_OUTPUTS, VOICEOVER_MP3, ffmpeg_bin

FFMPEG = ffmpeg_bin("ffmpeg")
FFPROBE = ffmpeg_bin("ffprobe")

WORK = RESILIENCE_V2
VISUAL = WORK / "visual_track.mp4"
AUDIO = VOICEOVER_MP3
SUBS_DIR = WORK / "subs"
MANIFEST = WORK / "subs_manifest.json"
BADGE = VE_OUTPUTS / "subscribe_badge_long.png"
OUT = WORK / "resilience_final.mp4"
BATCH_SIZE = 100

shutil.copy(BADGE, WORK / "badge.png")

manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
print(f"{len(manifest)} bloques de subtitulos a superponer, en lotes de {BATCH_SIZE}", flush=True)

def probe_duration(path: Path) -> float:
    probe = subprocess.run(
        [FFPROBE, "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        capture_output=True, text=True,
    )
    return float(probe.stdout.strip())


total_duration = probe_duration(VISUAL)
print(f"Duracion total (visual): {total_duration:.1f}s", flush=True)

audio_duration = probe_duration(AUDIO)
print(f"Duracion total (audio):  {audio_duration:.1f}s", flush=True)
if abs(total_duration - audio_duration) > 0.5:
    # -shortest trunca en silencio el mas largo - con >0.5s de diferencia eso
    # corta audio o deja video mudo a mitad de frase sin ningun aviso. Mejor
    # fallar aqui con un mensaje claro que entregar un video roto.
    raise RuntimeError(
        f"Desfase de {abs(total_duration - audio_duration):.1f}s entre video "
        f"({total_duration:.1f}s) y audio ({audio_duration:.1f}s) - revisa "
        f"CLIP_DURATIONS/CLIP_TRIM_OVERRIDE en _assemble_visual_track.py antes "
        f"de ensamblar el final."
    )


def run(cmd, cwd):
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=str(cwd))
    if result.returncode != 0:
        raise RuntimeError(f"ffmpeg fallo:\n{' '.join(cmd)}\n{result.stderr[-3000:]}")


current = "visual_track.mp4"
n_batches = -(-len(manifest) // BATCH_SIZE)
for b in range(n_batches):
    chunk = manifest[b * BATCH_SIZE:(b + 1) * BATCH_SIZE]
    out_name = f"pass_{b:03d}.mp4"

    cmd = [FFMPEG, "-y", "-i", current]
    for m in chunk:
        cmd += ["-i", f"subs/{m['file']}"]

    filters = []
    prev = "0:v"
    for i, m in enumerate(chunk):
        in_idx = i + 1
        out_label = f"v{i}" if i < len(chunk) - 1 else "vout"
        filters.append(
            f"[{prev}][{in_idx}:v]overlay=x=0:y=850:"
            f"enable='between(t,{m['start']:.3f},{m['end']:.3f})'[{out_label}]"
        )
        prev = out_label

    cmd += [
        "-filter_complex", ";".join(filters),
        "-map", "[vout]",
        "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
        "-an",
        out_name,
    ]
    run(cmd, WORK)
    print(f"Lote {b + 1}/{n_batches} listo -> {out_name}", flush=True)

    if current != "visual_track.mp4":
        (WORK / current).unlink(missing_ok=True)
    current = out_name

# Badge en los ultimos 20s + audio final normalizado a -14 LUFS (estandar de
# YouTube). Antes esto se aplicaba como comando ffmpeg manual fuera de git
# (RESILIENCIA_AUDIO_ARREGLADO.mp4) - quedaba sin registrar y se perdia en
# cada corrida nueva de este script. Codificado aqui para que no sea una
# regresion silenciosa la proxima vez.
badge_start = max(total_duration - 20, 0)
cmd = [
    FFMPEG, "-y",
    "-i", current, "-i", "badge.png", "-i", "voiceover.mp3",
    "-filter_complex",
    f"[0:v][1:v]overlay=x=W-w-40:y=40:enable='gte(t,{badge_start:.3f})'[vout];"
    "[2:a]loudnorm=I=-14:TP=-1.5:LRA=11[aout]",
    "-map", "[vout]", "-map", "[aout]",
    "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-shortest",
    "resilience_final.mp4",
]
run(cmd, WORK)
print(f"\nListo: {OUT}", flush=True)
