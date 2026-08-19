# Fuentes del video lakshmi-06 (generadas con IA vía vidIQ)

**Título:** Open The Door To Sudden Abundance Tonight 🔮 Adi Lakshmi: Primordial Abundance • 963 Hz • 3 Hours
**Bloque:** Ashta Lakshmi — estética **cósmica**, distinta a los templos dorados del bloque 1.
Ese cambio es deliberado: evita que el canal se vea repetitivo.

## Música base (instrumental original, libre de regalías, 177 s)
https://ai-music-tracks.s3.us-east-1.amazonaws.com/db0bbcfc-841e-4d3f-bd3f-6d9733b4f1fb/46c65cf2-7178-4d21-84a5-fcfb73be08b1.wav
→ guárdala como `bases/lakshmi-06.wav`

## Imágenes de fondo (1280x720, amplíalas a 2560 antes de renderizar)
1. https://ai-thumbnails.s3.amazonaws.com/editor/db0bbcfc-841e-4d3f-bd3f-6d9733b4f1fb/a6e760cb-0031-4d87-90ff-cdca34699a1d.png  (mandala dorado en el espacio, **86/100**)
2. https://ai-thumbnails.s3.amazonaws.com/editor/db0bbcfc-841e-4d3f-bd3f-6d9733b4f1fb/f1cb9b6b-c73a-4834-9726-cd52e06acfa9.png  (nebulosa dorada)
3. https://ai-thumbnails.s3.amazonaws.com/editor/db0bbcfc-841e-4d3f-bd3f-6d9733b4f1fb/4fa4df63-0a4f-4482-9d1e-ee953535a706.png  (loto de luz cósmico)
→ guárdalas en `salida/lakshmi-06/img/`

## Reconstruirlo
```bash
python3 scripts/03_audio.py --id lakshmi-06 --base bases/lakshmi-06.wav
python3 scripts/04_video.py --id lakshmi-06
python3 scripts/06_miniatura.py --id lakshmi-06 --img salida/lakshmi-06/img/1.png
python3 scripts/08_short.py --id lakshmi-06 --seg 45
```

> Descarga estos archivos pronto: los enlaces de S3 pueden caducar.
