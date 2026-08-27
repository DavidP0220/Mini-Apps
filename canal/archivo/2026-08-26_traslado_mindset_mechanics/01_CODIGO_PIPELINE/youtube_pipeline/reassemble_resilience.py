"""Re-ensambla el video de Resiliencia reusando escenas/voz ya generadas
(evita re-gastar creditos Gemini/ElevenLabs), tras el fix de remove_temp=False
en assembly.py que causaba un video.mp4 corrupto por un PermissionError de
Windows al limpiar el temp-audio.
"""
from pathlib import Path

from dotenv import load_dotenv
load_dotenv()

from pipeline.models import VisualAsset
from pipeline.stages import assembly, script_writer

OUTPUT = Path("channels/mindset_mechanics/output")
SCRIPT_FILE = Path("output/resilience_script.txt")

brief = script_writer.parse_brief(SCRIPT_FILE.read_text(encoding="utf-8"))

scenes_text = script_writer.split_scenes(brief.script)
if brief.closing_hook:
    scenes_text.append(("Cierre", brief.closing_hook))

from moviepy import AudioFileClip
audio_path = OUTPUT / "voiceover.mp3"
audio_duration = AudioFileClip(str(audio_path)).duration

total_words = sum(len(text.split()) for _, text in scenes_text) or 1
scenes = []
for i, (title, text) in enumerate(scenes_text):
    share = len(text.split()) / total_words
    duration = max(audio_duration * share, 1.5)
    img = OUTPUT / f"scene_{i}.png"
    if not img.exists():
        raise FileNotFoundError(f"Falta {img}, no se puede reensamblar sin regenerar")
    scenes.append(VisualAsset(image_path=img, duration_seconds=duration))

print(f"{len(scenes)} escenas, audio_duration={audio_duration:.1f}s")
result = assembly.render_video(scenes, OUTPUT / "video.mp4", audio_path)
print(f"Listo: {result.video_path} ({result.duration_seconds:.1f}s)")
