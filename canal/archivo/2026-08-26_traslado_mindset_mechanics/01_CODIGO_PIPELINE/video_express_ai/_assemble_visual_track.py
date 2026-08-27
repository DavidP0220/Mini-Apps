"""OBSOLETO - NO USAR PARA VIDEO NUEVO. Ver el aviso de abajo.

Arma la pista visual de Resiliencia: por cada escena, el clip real
(camara en movimiento) seguido de un sostenido con zoom sutil sobre su
ultimo frame hasta completar la duracion del bloque narrativo (tabla de
timestamps de RESILIENCE_SCENE_PLAN.md v2). Sin audio todavia.

=============================================================================
ARQUITECTURA PROHIBIDA DESDE 2026-08-25
=============================================================================
Kimi prohibio esta arquitectura en
handoffs/HANDOFF_2026-08-25_decision_tercera_via_resiliencia.md (Decision 2):
"PROHIBIDO sostener un frame congelado mas de 4 segundos".

Este script hace exactamente lo contrario. Medido en la auditoria del
2026-08-25 sobre los 12 clips reales del lote:

    movimiento real : 80s   (los 12 clips suman 5-8s cada uno)
    frame congelado : 474s
    total           : 554s  ->  85,6% del video es una imagen fija

Ese 85,6% ES la causa raiz de la queja de QA de David ("cuadriculado, sin
transiciones, sin cambios de angulo"). No era un problema de prompt: dos
pasadas de prompt (§6.1 y §8) no podian arreglar un video que por diseno es
imagen fija en su mayor parte.

Caso extremo, escena 12: el clip es un pull-back que a los ~4s ya dejo al
personaje fuera de cuadro (verificado extrayendo frames). El script congelaba
el ULTIMO frame - una calle vacia en picado - y lo sostenia 46 segundos.
Eso es el "clip de ciudad 3D que aparece hacia 545s" que se venia
investigando: no era una generacion desviada ni un error de la lista de
escenas, era esta arquitectura congelando el peor frame de la escena 12.
CLIP_TRIM_OVERRIDE (abajo) parchea el sintoma pero alarga el congelado a 52s.

La arquitectura nueva (3 sub-clips reales de 12-18s por escena, planos
distintos, transiciones cinematograficas) esta especificada en ese mismo
handoff. Este archivo se conserva solo como referencia historica del
ensamblaje del lote viejo.
=============================================================================
"""
import os
import shutil
import subprocess
import sys
from pathlib import Path

# Antes: rutas absolutas clavadas a "C:\Users\David Penuela\Documents\
# CLAUDE AUTOMATIC\..." y a la instalacion WinGet de esa maquina. El repo ya
# no vive ahi (esta en "CLAUDE AUTOMATIC PC 3"), asi que el script fallaba
# con FileNotFoundError en cualquier equipo, incluido el de David. Ahora las
# rutas se derivan del propio archivo y ffmpeg se busca en el PATH.
FFMPEG = os.getenv("FFMPEG") or shutil.which("ffmpeg") or "ffmpeg"
_MODULE_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _MODULE_DIR.parent

SRC = Path(os.getenv("ASSEMBLE_SRC") or _MODULE_DIR / "outputs")
WORK = Path(
    os.getenv("ASSEMBLE_WORK")
    or _REPO_ROOT / "youtube_pipeline/channels/mindset_mechanics/output/resilience_v2"
)

# Techo de frame congelado (Decision 2 de Kimi). Superarlo aborta en vez de
# producir en silencio el video "cuadriculado" que ya fallo el QA.
MAX_HOLD_S = float(os.getenv("MAX_HOLD_S", "4"))
ALLOW_LEGACY = os.getenv("ALLOW_LEGACY_ASSEMBLY") == "1"

# (numero, duracion_bloque_segundos) de la tabla de timestamps v2
BLOCKS = [
    (1, 48), (2, 46), (3, 49), (4, 50), (5, 43), (6, 44),
    (7, 34), (8, 39), (9, 40), (10, 46), (11, 61), (12, 54),
]

def probe_duration(path: Path) -> float:
    """Duracion real del clip via ffprobe - nunca confiar en un valor fijo a
    mano, porque VideoExpress.ai no siempre genera la misma duracion para el
    mismo tipo de plano (confirmado: mismos planos con 6.04s y 8.04s)."""
    ffprobe = os.getenv("FFPROBE") or shutil.which("ffprobe") or "ffprobe"
    result = subprocess.run(
        [ffprobe, "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        capture_output=True, text=True,
    )
    return float(result.stdout.strip())


# Escenas donde el clip completo NO sirve (la camara se aleja tanto hacia el
# final que el personaje desaparece del cuadro). Se recorta el clip a un
# punto donde el personaje sigue visible y se usa ESE mismo instante como
# base del sostenido - evita el salto brusco de "vuelve a aparecer" que
# saldria si solo se cambiara el frame del sostenido sin recortar el clip.
# Escena 12: a partir de ~3s el pull-back deja una calle vacia sin personaje
# - detectado en QA 2026-08-23.
CLIP_TRIM_OVERRIDE = {12: 2.0}


def run(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Comando fallo:\n{' '.join(cmd)}\n{result.stderr[-2000:]}")
    return result


def build_segment(num: int, block_duration: int) -> Path:
    clip = SRC / f"resilience_scene_{num:02d}.mp4"
    clip_dur = CLIP_TRIM_OVERRIDE.get(num) or probe_duration(clip)
    hold_dur = max(block_duration - clip_dur, 1.0)

    if hold_dur > MAX_HOLD_S and not ALLOW_LEGACY:
        raise SystemExit(
            f"\nABORTADO - escena {num}: el frame congelado duraria {hold_dur:.1f}s "
            f"(techo {MAX_HOLD_S}s).\n\n"
            "Kimi prohibio sostener un frame congelado mas de 4s en\n"
            "handoffs/HANDOFF_2026-08-25_decision_tercera_via_resiliencia.md (Decision 2).\n"
            "Esta arquitectura ('1 clip corto + frame congelado el resto del bloque')\n"
            "es la causa raiz del QA fallido: 85,6% del video era imagen fija.\n\n"
            "Lo correcto es generar 3 sub-clips reales de 12-18s por escena.\n"
            "Si aun asi necesitas reproducir el ensamblaje viejo tal cual estaba\n"
            "(solo para comparar), relanza con ALLOW_LEGACY_ASSEMBLY=1."
        )

    last_frame = WORK / f"last_frame_{num:02d}.png"
    if num in CLIP_TRIM_OVERRIDE:
        run([FFMPEG, "-y", "-ss", str(clip_dur - 0.05), "-i", str(clip), "-frames:v", "1", str(last_frame)])
    else:
        run([FFMPEG, "-y", "-sseof", "-0.1", "-i", str(clip), "-frames:v", "1", str(last_frame)])

    held = WORK / f"held_{num:02d}.mp4"
    zoom_frames = int(hold_dur * 30)
    vf = (
        f"zoompan=z='min(zoom+0.0006,1.12)':d={zoom_frames}:s=1920x1080:fps=30"
    )
    run([
        FFMPEG, "-y", "-loop", "1", "-i", str(last_frame),
        "-vf", vf, "-t", str(hold_dur),
        "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
        str(held),
    ])

    # Normalizar el clip original (mismo códec/preset/pix_fmt/framerate) antes
    # de concatenar, para que el concat demuxer no truene por streams distintos.
    # Si la escena tiene CLIP_TRIM_OVERRIDE, cortar ahi (ver comentario arriba).
    clip_norm = WORK / f"clip_norm_{num:02d}.mp4"
    trim_args = ["-t", str(clip_dur)] if num in CLIP_TRIM_OVERRIDE else []
    run([
        FFMPEG, "-y", "-i", str(clip), *trim_args,
        # minterpolate en vez de "-r 30": VideoExpress.ai entrega a 24fps: "-r 30"
        # a secas solo duplica/descarta frames (video "cuadriculado"/entrecortado,
        # confirmado como causa tecnica probable de la queja de David en
        # REPORTE_2026-08-23c). minterpolate interpola movimiento real.
        "-vf", "minterpolate=fps=30:mi_mode=mci:mc_mode=aobmc:vsbmc=1",
        "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
        "-an",
        str(clip_norm),
    ])

    concat_list = WORK / f"concat_{num:02d}.txt"
    concat_list.write_text(
        f"file '{clip_norm.name}'\nfile '{held.name}'\n", encoding="utf-8"
    )
    segment = WORK / f"segment_{num:02d}.mp4"
    run([
        FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", str(concat_list),
        "-c", "copy", str(segment),
    ])
    print(f"Segmento {num}: clip {clip_dur:.1f}s + hold {hold_dur:.1f}s = {block_duration}s -> {segment.name}", flush=True)
    return segment


def main():
    WORK.mkdir(parents=True, exist_ok=True)
    segments = []
    for num, block_duration in BLOCKS:
        segments.append(build_segment(num, block_duration))

    final_list = WORK / "concat_all.txt"
    final_list.write_text(
        "\n".join(f"file '{s.name}'" for s in segments), encoding="utf-8"
    )
    out = WORK / "visual_track.mp4"
    run([
        FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", str(final_list),
        "-c", "copy", str(out),
    ])
    print(f"\nPista visual completa: {out}", flush=True)


if __name__ == "__main__":
    main()
