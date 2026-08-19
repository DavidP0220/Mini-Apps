# Fuentes del video lakshmi-07 (generadas con IA vía vidIQ)

**Título:** Your Money Blocks Dissolve In 5 Minutes 💸 Dhana Lakshmi: Magnet for Money • 888 Hz • 1 Hour
**Bloque:** Ashta Lakshmi

## Música base (instrumental original, libre de regalías, 175 s)
https://ai-music-tracks.s3.us-east-1.amazonaws.com/db0bbcfc-841e-4d3f-bd3f-6d9733b4f1fb/4534fa24-8de6-4a47-b774-9a8f445125f1.wav
→ guárdala como `bases/lakshmi-07.wav`

## Imágenes de fondo (1280x720, amplíalas a 2560 antes de renderizar)
1. https://ai-thumbnails.s3.amazonaws.com/editor/db0bbcfc-841e-4d3f-bd3f-6d9733b4f1fb/94f5012f-434f-4e90-b623-c8db87c52e2f.png  (anillos concéntricos de energía, **86/100** — es la de la miniatura)
2. https://ai-thumbnails.s3.amazonaws.com/editor/db0bbcfc-841e-4d3f-bd3f-6d9733b4f1fb/397d2bd1-82bb-40d2-b9fe-49bd1fb391be.png  (vórtice dorado atrayendo monedas, 75/100)
3. https://ai-thumbnails.s3.amazonaws.com/editor/db0bbcfc-841e-4d3f-bd3f-6d9733b4f1fb/f03d659a-ebd1-497a-bdd6-e668ad4fa4cf.png  (espiral de monedas sobre agua)
→ guárdalas en `salida/lakshmi-07/img/`

## Reconstruirlo
```bash
python3 scripts/03_audio.py --id lakshmi-07 --base bases/lakshmi-07.wav
python3 scripts/04_video.py --id lakshmi-07
python3 scripts/06_miniatura.py --id lakshmi-07 --img salida/lakshmi-07/img/1.png
python3 scripts/08_short.py --id lakshmi-07 --seg 45
```

## Nota sobre los prompts de imagen
A partir del video 06 los prompts incluyen siempre: *"Pure background artwork, absolutely
NO text, no letters, no numbers, no logos, no people"* más la paleta exacta
(deep midnight blue / warm gold) y el acabado *"cinematic painterly ultra detailed 8k"*.
Desde ese cambio las imágenes pasaron de 20-30 puntos a 75-96 en el evaluador de vidIQ.
Copia ese formato para las que generes tú.

> Descarga estos archivos pronto: los enlaces de S3 pueden caducar.
