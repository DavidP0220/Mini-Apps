"""Transcribe voiceover.mp3 con faster-whisper (word timestamps) y agrupa en
bloques de 3-4 palabras para subtitulos quemados, siguiendo ESTILO_MINDSET_MECHANICS.md
§4. Guarda el resultado en JSON para el paso de renderizado."""
import json

from _paths import RESILIENCE_V2, VOICEOVER_MP3

AUDIO = VOICEOVER_MP3
OUT_JSON = RESILIENCE_V2 / "subtitle_blocks.json"
OUT_JSON.parent.mkdir(parents=True, exist_ok=True)

from faster_whisper import WhisperModel

print("Cargando modelo faster-whisper...", flush=True)
model = WhisperModel("small", device="cpu", compute_type="int8")

print("Transcribiendo con timestamps por palabra...", flush=True)
segments, info = model.transcribe(str(AUDIO), word_timestamps=True, vad_filter=True)
print(f"Idioma: {info.language} (p={info.language_probability:.2f})", flush=True)

words = []
for seg in segments:
    for w in seg.words:
        words.append({"word": w.word.strip(), "start": w.start, "end": w.end})

print(f"{len(words)} palabras transcritas", flush=True)

# Agrupar en bloques de 3-4 palabras (alternando para variar el ritmo un poco)
blocks = []
i = 0
toggle = True
while i < len(words):
    size = 4 if toggle else 3
    toggle = not toggle
    chunk = words[i:i + size]
    if not chunk:
        break
    text = " ".join(w["word"] for w in chunk).upper()
    blocks.append({
        "text": text,
        "start": chunk[0]["start"],
        "end": chunk[-1]["end"],
    })
    i += size

OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
OUT_JSON.write_text(json.dumps(blocks, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"\n{len(blocks)} bloques de subtitulos -> {OUT_JSON}", flush=True)
print("Primeros 5:", flush=True)
for b in blocks[:5]:
    print(f"  [{b['start']:.2f}-{b['end']:.2f}] {b['text']}", flush=True)
