"""Orquestador: conecta las etapas del pipeline en orden.

Cada etapa que requiere una API key que no está configurada lanza un
RuntimeError con instrucciones claras; el orquestador lo captura, lo
reporta y continúa con lo que sí puede ejecutar, para que puedas ir
activando etapas a medida que consigues cada key.
"""
from dataclasses import dataclass, field
from pathlib import Path

from .models import ChannelConfig, VideoBrief, VisualAsset
from .stages import assembly, publish, research, script_writer, visuals, voice


@dataclass
class PipelineReport:
    completed_stages: list[str] = field(default_factory=list)
    skipped_stages: dict[str, str] = field(default_factory=dict)
    brief: VideoBrief | None = None
    thumbnail_path: Path | None = None
    video_path: Path | None = None
    publish_url: str | None = None


def run_pipeline(
    channel: ChannelConfig,
    topic: str,
    reference_channel_ids: list[str] | None = None,
    client_secret_path: Path | None = None,
    auto_publish: bool = False,
) -> PipelineReport:
    """Corre el pipeline completo de una sola pasada: research -> guion ->
    miniatura/escenas -> voz -> ensamblado -> (opcional) publish.

    Si quieres revisar/editar el guion a mano antes de gastar créditos de voz
    e imagen, usa `write_script` + `render_from_script` en vez de esta función.
    """
    report = PipelineReport()
    output_dir = channel.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    insights = []
    if reference_channel_ids:
        try:
            for channel_id in reference_channel_ids:
                insights.extend(research.research_channel(channel_id))
            report.completed_stages.append("research")
        except Exception as e:
            report.skipped_stages["research"] = str(e)

    try:
        brief = script_writer.write_brief(topic, insights)
        report.brief = brief
        report.completed_stages.append("script")
    except Exception as e:
        report.skipped_stages["script"] = str(e)
        brief = VideoBrief(topic=topic, title=topic, hook="", script="")

    _render_from_brief(channel, brief, report, client_secret_path, auto_publish)
    return report


def write_script(
    channel: ChannelConfig,
    topic: str,
    reference_channel_ids: list[str] | None = None,
) -> tuple[VideoBrief, Path]:
    """Corre research + guion y guarda el resultado en `output/script.txt`,
    un archivo de texto editable a mano, sin seguir con voz/video todavía.
    """
    output_dir = channel.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    insights = []
    if reference_channel_ids:
        for channel_id in reference_channel_ids:
            insights.extend(research.research_channel(channel_id))

    brief = script_writer.write_brief(topic, insights)
    script_path = output_dir / "script.txt"
    script_path.write_text(script_writer.format_brief(brief), encoding="utf-8")
    return brief, script_path


def render_from_script(
    channel: ChannelConfig,
    script_path: Path,
    client_secret_path: Path | None = None,
    auto_publish: bool = False,
) -> PipelineReport:
    """Lee un archivo de guion (el que genera `write_script`, editado o no) y
    corre el resto del pipeline: miniatura/escenas, voz, ensamblado y,
    opcionalmente, publish.
    """
    brief = script_writer.parse_brief(script_path.read_text(encoding="utf-8"))
    report = PipelineReport(brief=brief, completed_stages=["script"])
    _render_from_brief(channel, brief, report, client_secret_path, auto_publish)
    return report


def _render_from_brief(
    channel: ChannelConfig,
    brief: VideoBrief,
    report: PipelineReport,
    client_secret_path: Path | None,
    auto_publish: bool,
) -> None:
    output_dir = channel.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    thumbnail = visuals.make_thumbnail(brief.title or brief.topic, output_dir / "thumbnail.png")
    report.thumbnail_path = thumbnail.image_path
    report.completed_stages.append("visuals")

    audio_path = None
    audio_duration = None
    word_timings = None
    if brief.script:
        narration = brief.script
        if brief.closing_hook:
            narration = f"{narration}\n\n{brief.closing_hook}"
        try:
            voice_result = voice.synthesize(
                narration, channel.elevenlabs_voice_id or "", output_dir / "voiceover.mp3"
            )
            audio_path = voice_result.audio_path
            audio_duration = voice_result.duration_seconds
            word_timings = voice_result.word_timings
            report.completed_stages.append("voice")
        except Exception as e:
            report.skipped_stages["voice"] = str(e)

    scenes = _build_scenes(brief, channel.niche, audio_duration, output_dir)
    assembly_result = assembly.render_video(
        scenes, output_dir / "video.mp4", audio_path, word_timings
    )
    report.video_path = assembly_result.video_path
    report.completed_stages.append("assembly")

    if auto_publish and client_secret_path:
        try:
            publish_result = publish.publish_video(
                channel,
                assembly_result.video_path,
                brief.title or brief.topic,
                brief.seo_description,
                brief.seo_keywords,
                client_secret_path,
            )
            report.publish_url = publish_result.url
            report.completed_stages.append("publish")
        except RuntimeError as e:
            report.skipped_stages["publish"] = str(e)


def _build_scenes(
    brief: VideoBrief, niche: str, audio_duration: float | None, output_dir: Path
) -> list[VisualAsset]:
    """Genera una imagen por escena del guion, con duración proporcional a la
    porción de la narración que le corresponde (si hay audio real) o una
    duración fija de placeholder (si la etapa de voz no corrió).

    Intenta generar cada imagen como b-roll con IA (`visuals.generate_ai_scene_image`,
    requiere GEMINI_API_KEY, usando el texto real narrado en la escena para que
    la imagen ilustre justo lo que se está diciendo); si esa etapa falla o no
    está configurada, cae de vuelta al fondo degradado simple
    (`visuals.make_scene_image`) para que el pipeline nunca se rompa por falta
    de esa clave.
    """
    scenes_text = script_writer.split_scenes(brief.script) if brief.script else []
    if brief.closing_hook:
        scenes_text.append(("Cierre", brief.closing_hook))
    if not scenes_text:
        scenes_text = [(brief.title or brief.topic or "Escena 1", brief.script or brief.topic or "")]

    total_words = sum(len(text.split()) for _, text in scenes_text) or 1

    scenes = []
    for i, (title, text) in enumerate(scenes_text):
        if audio_duration:
            share = len(text.split()) / total_words
            duration = max(audio_duration * share, 1.5)
        else:
            duration = 4.0
        try:
            asset = visuals.generate_ai_scene_image(
                title, text, niche, output_dir / f"scene_{i}.png", duration
            )
        except Exception:
            asset = visuals.make_scene_image(
                title, output_dir / f"scene_{i}.png", (15, 17, 26), (35, 20, 60), duration
            )
        scenes.append(asset)
    return scenes
