"""Estructuras de datos compartidas entre todas las etapas del pipeline."""
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class ChannelConfig:
    name: str
    niche: str
    language: str = "es"
    elevenlabs_voice_id: str | None = None
    oauth_token_path: Path | None = None  # credenciales propias de ESTE canal, aisladas de los demás
    output_dir: Path = Path("output")


@dataclass
class TrendInsight:
    """Resultado de la etapa de investigación (research.py)."""
    reference_channel: str
    video_title: str
    views: int
    duration_seconds: int
    published_hour_utc: int
    thumbnail_style_notes: str = ""


@dataclass
class VideoBrief:
    """Resultado de la etapa de guion (script_writer.py)."""
    topic: str
    title: str
    hook: str
    script: str
    closing_hook: str = ""  # gancho de cierre que genera intriga hacia el siguiente video
    seo_keywords: list[str] = field(default_factory=list)
    seo_description: str = ""


@dataclass
class WordTiming:
    word: str
    start_seconds: float
    end_seconds: float


@dataclass
class VoiceOverResult:
    audio_path: Path
    duration_seconds: float
    word_timings: list[WordTiming] = field(default_factory=list)


@dataclass
class VisualAsset:
    image_path: Path
    duration_seconds: float = 4.0


@dataclass
class AssemblyResult:
    video_path: Path
    duration_seconds: float


@dataclass
class PublishResult:
    channel_name: str
    video_id: str | None
    url: str | None
    status: str
