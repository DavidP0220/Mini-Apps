"""Renderiza cada bloque de subtitulos como PNG transparente con Pillow
(ffmpeg drawtext SEGFALLA en esta maquina, nunca usarlo). Estilo fijo del
canal: mayusculas, negrita condensada, amarillo con contorno negro grueso,
centrado, tercio inferior (ESTILO_MINDSET_MECHANICS.md §4)."""
import json
from PIL import Image, ImageDraw

from _paths import RESILIENCE_V2, bold_font

BLOCKS_JSON = RESILIENCE_V2 / "subtitle_blocks.json"
OUT_DIR = RESILIENCE_V2 / "subs"
OUT_DIR.mkdir(parents=True, exist_ok=True)

WIDTH, HEIGHT = 1920, 1080
FONT_SIZE = 72
YELLOW = (255, 224, 0, 255)
BLACK = (0, 0, 0, 255)
OUTLINE_PX = 6
Y_POS = 850  # tercio inferior

font = bold_font(FONT_SIZE)
blocks = json.loads(BLOCKS_JSON.read_text(encoding="utf-8"))

manifest = []
for idx, b in enumerate(blocks):
    text = b["text"]
    img = Image.new("RGBA", (WIDTH, 160), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (WIDTH - tw) / 2 - bbox[0]
    y = (160 - th) / 2 - bbox[1]

    # Contorno negro grueso: dibujar el texto desplazado en un anillo alrededor
    for dx in range(-OUTLINE_PX, OUTLINE_PX + 1):
        for dy in range(-OUTLINE_PX, OUTLINE_PX + 1):
            if dx * dx + dy * dy <= OUTLINE_PX * OUTLINE_PX:
                draw.text((x + dx, y + dy), text, font=font, fill=BLACK)
    draw.text((x, y), text, font=font, fill=YELLOW)

    fname = f"sub_{idx:04d}.png"
    img.save(OUT_DIR / fname)
    manifest.append({"file": fname, "start": b["start"], "end": b["end"]})

manifest_path = OUT_DIR.parent / "subs_manifest.json"
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"{len(manifest)} PNGs de subtitulos generados en {OUT_DIR}", flush=True)
print(f"Manifest: {manifest_path}", flush=True)
