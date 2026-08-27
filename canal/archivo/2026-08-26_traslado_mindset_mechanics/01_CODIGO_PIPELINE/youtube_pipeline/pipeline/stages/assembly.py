"""Etapa 4b: Ensamblado de video (b-roll animado + transiciones + subtítulos + voz en off).

Esta etapa SÍ funciona hoy sin ninguna API key de pago: anima imágenes
estáticas con variantes de zoom/paneo ("Ken Burns"), aplica transiciones de
crossfade entre escenas, y las sincroniza con un audio de narración. Usa
moviepy + imageio-ffmpeg (ffmpeg viene incluido, no hace falta instalarlo
aparte). Si se le pasan `word_timings` (de la etapa de voz), superpone
subtítulos palabra por palabra sincronizados con la narración.
"""
import os
from pathlib import Path

from ..models import AssemblyResult, VisualAsset, WordTiming

# 1080p, no 720p. Esta etapa venía fija en 1280x720, lo que contradice la
# regla dura del proyecto ("calidad mínima 1080p en Shorts y videos largos;
# siempre subir el nivel, nunca bajarlo") y además chocaba con el resto del
# pipeline: video_express_ai/_assemble_visual_track.py ya ensambla a
# 1920x1080. El resultado era un video largo publicado a 720p sin que nadie
# lo hubiera decidido. Coste del cambio: solo tiempo de render (~2.25x más
# píxeles), cero dinero y cero créditos. Overrideable por si hiciera falta
# una prueba rápida y barata.
WIDTH = int(os.getenv("PIPELINE_WIDTH", "1920"))
HEIGHT = int(os.getenv("PIPELINE_HEIGHT", "1080"))
FPS = 30

# El tamaño de los subtítulos y su separación del borde inferior se calculan
# proporcionalmente a la altura: fijarlos en píxeles (54px / 160px) hacía que
# al subir a 1080p los subtítulos quedaran diminutos y pegados al borde.
_CAPTION_FONT_SIZE = max(32, round(HEIGHT * 0.075))
_CAPTION_BOTTOM_MARGIN = round(HEIGHT * 0.22)

_CAPTION_FONT_CANDIDATES = [
    r"C:\Windows\Fonts\arialbd.ttf",
    r"C:\Windows\Fonts\segoeuib.ttf",
    r"C:\Windows\Fonts\calibrib.ttf",
]


def _caption_font() -> str | None:
    for path in _CAPTION_FONT_CANDIDATES:
        if Path(path).exists():
            return path
    return None


def _ease(p: float) -> float:
    """Curva 'smoothstep': arranca y termina suave, en vez de velocidad
    constante — se ve más cinematográfico que un movimiento lineal."""
    return p * p * (3 - 2 * p)


# Duración de un ciclo completo de "respiración" de cámara (ida y vuelta).
# CLAVE: el movimiento se repite en ciclos cortos en vez de recorrer todo su
# rango una sola vez a lo largo de la escena completa — si una escena dura
# 90+ segundos y el zoom solo hace UN barrido en toda esa duración, los
# primeros 20-30s casi no se mueven (bug real detectado: dos frames a 27s de
# distancia salían pixel-por-pixel idénticos). Con un ciclo corto, siempre
# hay movimiento visible sin importar cuánto dure la escena.
_CYCLE_SECONDS = 7.0


def _oscillating_progress(t: float, cycle: float = _CYCLE_SECONDS) -> float:
    """0 -> 1 -> 0 con curva suave, repitiendo cada `cycle` segundos."""
    phase = (t % cycle) / cycle
    p = phase * 2 if phase < 0.5 else 2 - phase * 2
    return _ease(p)


# Zoom bien notorio (antes 1.15, casi imperceptible en escenas largas).
_ZOOM = 1.35

# 6 variantes: zoom puro in/out, y zoom+paneo combinado en las 4 diagonales,
# para que cada escena se mueva distinto y nunca se sienta como "foto fija".
_STYLES = [
    ("zoom_in", 0, 0),
    ("zoom_out", 0, 0),
    ("pan", 1, 0),
    ("pan", -1, 0),
    ("pan", 0, 1),
    ("pan", 0, -1),
]


def _ken_burns_clip(asset: VisualAsset, style_index: int):
    """Anima la imagen de la escena con zoom+paneo combinados en un ciclo
    corto que se repite (respiración de cámara), alternando 6 variantes de
    movimiento por índice de escena para que cada una se sienta animada de
    principio a fin, sin importar cuánto dure — no solo un corte entre fotos
    fijas.
    """
    from moviepy import CompositeVideoClip, ImageClip

    duration = asset.duration_seconds or 0.001
    base = ImageClip(str(asset.image_path)).resized((WIDTH, HEIGHT)).with_duration(duration)

    kind, dir_x, dir_y = _STYLES[style_index % len(_STYLES)]

    if kind == "zoom_in":
        zoomed = base.resized(lambda t: 1.0 + (_ZOOM - 1.0) * _oscillating_progress(t))
        zoomed = zoomed.with_position("center")
    elif kind == "zoom_out":
        zoomed = base.resized(lambda t: _ZOOM - (_ZOOM - 1.0) * _oscillating_progress(t))
        zoomed = zoomed.with_position("center")
    else:
        # Zoom fijo + paneo animado en la diagonal que toque (dir_x/dir_y).
        zoomed = base.resized(_ZOOM)
        excess_x = WIDTH * _ZOOM - WIDTH
        excess_y = HEIGHT * _ZOOM - HEIGHT

        def pos(t):
            p = _oscillating_progress(t) * 2 - 1  # de -1 a 1
            x = -excess_x / 2 - dir_x * (excess_x / 2) * p
            y = -excess_y / 2 - dir_y * (excess_y / 2) * p
            return (x, y)

        zoomed = zoomed.with_position(pos)

    return CompositeVideoClip([zoomed], size=(WIDTH, HEIGHT)).with_duration(duration)


def _build_caption_clips(word_timings: list[WordTiming], duration_cap: float):
    font_path = _caption_font()
    if not font_path:
        return []

    from moviepy import TextClip

    clips = []
    for w in word_timings:
        if w.start_seconds >= duration_cap:
            break
        end = min(w.end_seconds, duration_cap)
        if end <= w.start_seconds:
            continue
        txt = (
            TextClip(
                font=font_path,
                text=w.word,
                font_size=_CAPTION_FONT_SIZE,
                color="white",
                stroke_color="black",
                stroke_width=max(2, round(_CAPTION_FONT_SIZE / 18)),
                method="label",
            )
            .with_start(w.start_seconds)
            .with_end(end)
            .with_position(("center", HEIGHT - _CAPTION_BOTTOM_MARGIN))
        )
        clips.append(txt)
    return clips


def render_video(
    scenes: list[VisualAsset],
    output_path: Path,
    audio_path: Path | None = None,
    word_timings: list[WordTiming] | None = None,
) -> AssemblyResult:
    if not scenes:
        raise ValueError("Se necesita al menos una escena (VisualAsset) para ensamblar el video.")

    from moviepy import AudioFileClip, CompositeVideoClip, concatenate_videoclips, vfx

    shortest_scene = min(s.duration_seconds for s in scenes if s.duration_seconds) or 1.0
    fade_duration = min(0.6, shortest_scene * 0.3)

    clips = []
    for i, scene in enumerate(scenes):
        clip = _ken_burns_clip(scene, i)
        if i > 0 and fade_duration > 0:
            clip = clip.with_effects([vfx.CrossFadeIn(fade_duration)])
        clips.append(clip)

    video = concatenate_videoclips(
        clips, method="compose", padding=-fade_duration if fade_duration > 0 else 0
    )

    if audio_path is not None:
        audio = AudioFileClip(str(audio_path))
        video = video.with_duration(min(video.duration, audio.duration))
        video = video.with_audio(audio.subclipped(0, video.duration))

    if word_timings:
        caption_clips = _build_caption_clips(word_timings, video.duration)
        if caption_clips:
            video = CompositeVideoClip(
                [video, *caption_clips], size=(WIDTH, HEIGHT)
            ).with_duration(video.duration)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    video.write_videofile(
        str(output_path),
        fps=FPS,
        codec="libx264",
        audio_codec="aac",
        logger=None,
        remove_temp=False,  # Windows a veces mantiene el temp-audio bloqueado
        # tras el muxeo; moviepy intenta borrarlo y lanza PermissionError
        # incluso cuando el video final ya se escribió bien. No borrar el
        # temp evita que ese error tumbe todo el pipeline en el último paso.
    )

    return AssemblyResult(video_path=output_path, duration_seconds=video.duration)
