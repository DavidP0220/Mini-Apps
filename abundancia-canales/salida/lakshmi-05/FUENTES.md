# Fuentes del video lakshmi-05 (generadas con IA vía vidIQ)

Este contenedor es temporal: el .mp4 NO sobrevive a la sesión.

**Título:** Everything Starts Changing For You Today 🍀 The Wealth Gate Opens Tonight • 777 Hz • 1 Hour

## Música base (instrumental original, libre de regalías, 169 s)
https://ai-music-tracks.s3.us-east-1.amazonaws.com/db0bbcfc-841e-4d3f-bd3f-6d9733b4f1fb/304c0cdd-9ae6-4180-811b-6021fe94198e.wav
→ guárdala como `bases/lakshmi-05.wav`

## Imágenes de fondo (1280x720, amplíalas a 2560 antes de renderizar)
1. https://ai-thumbnails.s3.amazonaws.com/editor/db0bbcfc-841e-4d3f-bd3f-6d9733b4f1fb/9d400df1-fa7d-4a9c-9cf8-060433003fab.png  (puerta dorada abriéndose)
2. https://ai-thumbnails.s3.amazonaws.com/editor/db0bbcfc-841e-4d3f-bd3f-6d9733b4f1fb/8bd72bef-2de0-4ff5-8ec7-c192aab7aa03.png  (corredor de arcos hacia el amanecer)
3. https://ai-thumbnails.s3.amazonaws.com/editor/db0bbcfc-841e-4d3f-bd3f-6d9733b4f1fb/d3bf4df8-3b55-40f6-b6fb-b1cd1a1abdea.png  (llave dorada sobre altar)
→ guárdalas en `salida/lakshmi-05/img/`

## Reconstruirlo
```bash
python3 scripts/03_audio.py --id lakshmi-05 --base bases/lakshmi-05.wav
python3 scripts/04_video.py --id lakshmi-05
python3 scripts/06_miniatura.py --id lakshmi-05 --img salida/lakshmi-05/img/1.png
python3 scripts/08_short.py --id lakshmi-05 --seg 45
```

## Verificado en esta sesión
- Audio: 1 h · 585 MB · 3 min 33 s de proceso
- Video: 1 h · 473 MB · 1080p · 777 Hz · 3 min 59 s de render
- Short: 45 s · 1080x1920
- Miniatura: GATE OPENS · 1280x720

> Descarga estos archivos pronto: los enlaces de S3 pueden caducar.
