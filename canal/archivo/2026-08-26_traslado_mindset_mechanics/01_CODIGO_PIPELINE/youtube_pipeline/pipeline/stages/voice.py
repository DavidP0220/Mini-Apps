"""Etapa 3: Voz en off (text-to-speech).

Requiere: ELEVENLABS_API_KEY en el archivo .env
Revisa tu suscripción/créditos en: https://elevenlabs.io/app/subscription
"""
import base64
import os
from pathlib import Path

from ..models import VoiceOverResult, WordTiming

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")


def synthesize(script: str, voice_id: str, output_path: Path) -> VoiceOverResult:
    """Genera el audio de narración junto con el timing de cada palabra
    (usado para los subtítulos animados en la etapa de ensamblado).
    """
    if not ELEVENLABS_API_KEY:
        raise RuntimeError(
            "Falta ELEVENLABS_API_KEY en .env, o tu suscripción de ElevenLabs "
            "está vencida. Revisa https://elevenlabs.io/app/subscription. "
            "Ver instrucciones en el README, sección 'Etapa 3'."
        )

    from elevenlabs.client import ElevenLabs

    client = ElevenLabs(api_key=ELEVENLABS_API_KEY, timeout=300)
    result = client.text_to_speech.convert_with_timestamps(
        voice_id=voice_id,
        text=script,
        model_id="eleven_multilingual_v2",
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(base64.b64decode(result["audio_base64"]))

    duration = _get_audio_duration(output_path)
    word_timings = _words_from_alignment(result["alignment"])
    return VoiceOverResult(
        audio_path=output_path, duration_seconds=duration, word_timings=word_timings
    )


def _words_from_alignment(alignment: dict) -> list[WordTiming]:
    """Agrupa el alineado carácter-por-carácter de ElevenLabs en palabras
    con su tiempo de inicio/fin, para poder mostrarlas como subtítulos.
    """
    chars = alignment["characters"]
    starts = alignment["character_start_times_seconds"]
    ends = alignment["character_end_times_seconds"]

    words = []
    current = ""
    word_start = None
    for char, start, end in zip(chars, starts, ends):
        if char.isspace():
            if current:
                words.append(WordTiming(word=current, start_seconds=word_start, end_seconds=end))
                current = ""
                word_start = None
            continue
        if not current:
            word_start = start
        current += char
    if current:
        words.append(WordTiming(word=current, start_seconds=word_start, end_seconds=ends[-1]))
    return words


def _get_audio_duration(path: Path) -> float:
    from mutagen.mp3 import MP3

    return MP3(path).info.length
