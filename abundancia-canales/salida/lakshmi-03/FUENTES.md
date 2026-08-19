# Fuentes del video lakshmi-03 (generadas con IA vía vidIQ)

Este contenedor es temporal: el .mp4 NO sobrevive a la sesión.
Con estos enlaces lo reconstruyes idéntico en tu PC.

**Título:** Big Money Is On Its Way To You Today 💸 Rain of Gold Coins Meditation • 888 Hz • 1 Hour

## Música base (instrumental original, libre de regalías, 156 s)
https://ai-music-tracks.s3.us-east-1.amazonaws.com/db0bbcfc-841e-4d3f-bd3f-6d9733b4f1fb/957217bb-2043-4629-9607-433b068a8072.wav
→ guárdala como `bases/lakshmi-03.wav`

## Imágenes de fondo (1280x720, amplíalas a 2560 antes de renderizar)
1. https://ai-thumbnails.s3.amazonaws.com/editor/db0bbcfc-841e-4d3f-bd3f-6d9733b4f1fb/f31aa387-99fc-49e1-854f-958702396a80.png  ← esta sacó 98/100 en el evaluador de vidIQ
2. https://ai-thumbnails.s3.amazonaws.com/editor/db0bbcfc-841e-4d3f-bd3f-6d9733b4f1fb/bdb42e8c-0c5f-41f4-a5b3-a248a69e48df.png  (88/100)
3. https://ai-thumbnails.s3.amazonaws.com/editor/db0bbcfc-841e-4d3f-bd3f-6d9733b4f1fb/bdba7fca-83e5-4b4f-8bbb-89398fa946e0.png
→ guárdalas en `salida/lakshmi-03/img/`

## Reconstruirlo
```bash
python3 scripts/03_audio.py --id lakshmi-03 --base bases/lakshmi-03.wav
python3 scripts/04_video.py --id lakshmi-03
python3 scripts/06_miniatura.py --id lakshmi-03 --img salida/lakshmi-03/img/1.png
python3 scripts/08_short.py --id lakshmi-03 --seg 45
```

## Verificado en esta sesión
- Video: 1 h 00 min · 440 MB · 1080p · 888 Hz · 3 min 53 s de render
- Short: 45 s · 1080x1920 · 6,8 MB · con audio verificado
- Miniatura: RAIN OF GOLD · 1280x720

> Descarga estos archivos pronto: los enlaces de S3 pueden caducar.
