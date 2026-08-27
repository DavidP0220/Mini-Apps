"""Genera la voz en off del reel de animales del oceano, reusando el modulo
de voz ya probado del pipeline de youtube_pipeline (ElevenLabs + timings por
palabra para captions sincronizados)."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "youtube_pipeline"))

from dotenv import load_dotenv
load_dotenv(Path(__file__).parent.parent / "youtube_pipeline" / ".env")

from pipeline.stages import voice

SCRIPT = (
    "These three ocean animals might be smarter than you. "
    "Dolphins recognize themselves in mirrors and call each other by unique names. "
    "Octopuses solve puzzles, open jars, and can outsmart their own tank walls, with no bones and three hearts. "
    "Orcas hunt in coordinated packs and pass down hunting traditions across generations. "
    "Which one surprised you most? Comment below."
)

VOICE_ID = "SAz9YHcvj6GT2YYXdXww"  # "River" - calmada, autoritativa, ya usada en el pipeline

OUT = Path("outputs")
OUT.mkdir(exist_ok=True)

result = voice.synthesize(SCRIPT, VOICE_ID, OUT / "ocean_voiceover.mp3")
print(f"Audio: {result.audio_path} ({result.duration_seconds:.2f}s)")

timings = [{"word": w.word, "start": w.start_seconds, "end": w.end_seconds} for w in result.word_timings]
(OUT / "ocean_word_timings.json").write_text(json.dumps(timings, indent=2))
print(f"Timings guardados: {len(timings)} palabras")
