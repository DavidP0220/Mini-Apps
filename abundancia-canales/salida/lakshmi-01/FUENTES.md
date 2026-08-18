# Fuentes del video lakshmi-01 (generadas con IA vía vidIQ)

Este contenedor es temporal: el .mp4 de 1 hora NO sobrevive a la sesión.
Con estos enlaces reconstruyes el video idéntico en tu PC en ~5 minutos.

## Música base (instrumental original, libre de regalías, 160 s)
https://ai-music-tracks.s3.us-east-1.amazonaws.com/db0bbcfc-841e-4d3f-bd3f-6d9733b4f1fb/e9927e05-95fc-48bd-b75e-66eab8412f72.wav
→ guárdala como `bases/lakshmi-01.wav`

## Imágenes de fondo (1280x720, amplíalas a 2560 antes de renderizar)
1. https://ai-thumbnails.s3.amazonaws.com/editor/db0bbcfc-841e-4d3f-bd3f-6d9733b4f1fb/b3bd5303-7575-47f6-ad2c-df82fcbbfbbd.png
2. https://ai-thumbnails.s3.amazonaws.com/editor/db0bbcfc-841e-4d3f-bd3f-6d9733b4f1fb/e57a9a90-139b-43e1-a81b-af6df0187942.png
3. https://ai-thumbnails.s3.amazonaws.com/editor/db0bbcfc-841e-4d3f-bd3f-6d9733b4f1fb/e9a82257-34fa-4e5e-9d5d-0114453c94b3.png
→ guárdalas en `salida/lakshmi-01/img/`

## Miniatura final (con el texto MONEY FLOWS ya puesto)
https://ai-thumbnails.s3.amazonaws.com/editor/db0bbcfc-841e-4d3f-bd3f-6d9733b4f1fb/ee7fc495-9b96-42ef-b44a-0ab1f6c4cfa3.png

## Reconstruirlo
```bash
python3 scripts/03_audio.py --id lakshmi-01 --base bases/lakshmi-01.wav
python3 scripts/04_video.py --id lakshmi-01
```
Resultado verificado: 1 h 00 min · 506 MB · 1080p · 528 Hz · 4 min 35 s de render.

> Descarga estos archivos pronto: los enlaces de S3 pueden caducar.
