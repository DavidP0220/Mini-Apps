"""Rutas portables y fuentes, compartidas por los scripts sueltos `_*.py`.

Por que existe: los scripts de un solo uso (`_final_assembly.py`,
`_render_subtitle_pngs.py`, `_transcribe_voiceover.py`, `_make_long_badge.py`,
`_generate_resilience_batch.py`) nacieron con rutas absolutas clavadas a la
maquina de David:

    C:\\Users\\David Penuela\\Documents\\CLAUDE AUTOMATIC\\...
    C:\\Users\\David Penuela\\AppData\\Local\\Microsoft\\WinGet\\Packages\\...
    C:\\Windows\\Fonts\\arialbd.ttf

La auditoria del 2026-08-25 quito ese patron de `video_express_bot.py`,
`video_understand.py` y `_assemble_visual_track.py`, pero estos cinco quedaron
fuera: siguen reventando con FileNotFoundError en cualquier clon limpio, en
otra maquina, o si David renombra la carpeta. Aqui se resuelve igual que en
`video_express_bot._anchored`: anclado al repo, con variable de entorno que
manda si esta puesta.

Ojo con la equivalencia: este archivo vive en <repo>/video_express_ai/, asi
que REPO_ROOT es <repo>, que en la maquina de David ES "CLAUDE AUTOMATIC".
Las rutas resultantes son EXACTAMENTE las mismas que las viejas alli - no
cambia nada para el, solo deja de estar clavado.
"""
import os
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MODULE_DIR = Path(__file__).resolve().parent

# Salidas del pipeline del canal (voiceover.mp3, resilience_v2/, subs/...).
CHANNEL_OUTPUT = Path(
    os.getenv("CHANNEL_OUTPUT_DIR")
    or REPO_ROOT / "youtube_pipeline" / "channels" / "mindset_mechanics" / "output"
)
RESILIENCE_V2 = CHANNEL_OUTPUT / "resilience_v2"
VOICEOVER_MP3 = CHANNEL_OUTPUT / "voiceover.mp3"

# outputs/ de este modulo (badges, previews, stills importados).
VE_OUTPUTS = Path(os.getenv("OUTPUT_DIR") or MODULE_DIR / "outputs")


def ffmpeg_bin(name: str = "ffmpeg") -> str:
    """ffmpeg/ffprobe del PATH (o de la variable FFMPEG/FFPROBE).

    Antes estaba clavado a una instalacion WinGet concreta, con el numero de
    version dentro de la ruta ("ffmpeg-9.0-full_build"): una actualizacion de
    ffmpeg en la propia maquina de David tambien lo habria roto, no solo un
    equipo distinto.
    """
    override = os.getenv(name.upper())
    if override:
        return override
    found = shutil.which(name)
    if found:
        return found
    raise FileNotFoundError(
        f"No se encontro '{name}' en el PATH. Instalalo, o exporta {name.upper()} "
        f"con la ruta completa al binario."
    )


# Fuentes en negrita, por orden de preferencia. La lista incluye Windows,
# Linux y macOS: los scripts que hacen ImageFont.truetype(r"C:\\Windows\\...")
# sin alternativa fallan en seco fuera de Windows. `visuals.py` ya usaba una
# lista de candidatas con respaldo - es el mismo patron, aplicado aqui.
_BOLD_FONT_CANDIDATES = (
    r"C:\Windows\Fonts\arialbd.ttf",
    r"C:\Windows\Fonts\segoeuib.ttf",
    r"C:\Windows\Fonts\calibrib.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
)


def bold_font(size: int):
    """Fuente negrita con respaldo garantizado (nunca lanza)."""
    from PIL import ImageFont

    override = os.getenv("SUBTITLE_FONT")
    candidates = (override, *_BOLD_FONT_CANDIDATES) if override else _BOLD_FONT_CANDIDATES
    for path in candidates:
        if path and Path(path).exists():
            return ImageFont.truetype(path, size)
    # Sin ninguna TTF a mano: el bitmap por defecto se ve peor, pero es
    # preferible a abortar el render entero.
    print(
        "[fuentes] AVISO: ninguna fuente negrita encontrada; se usa la de "
        "respaldo de Pillow. El resultado NO cumple el estilo del canal - "
        "instala una TTF o exporta SUBTITLE_FONT.",
        flush=True,
    )
    return ImageFont.load_default(size=size)
