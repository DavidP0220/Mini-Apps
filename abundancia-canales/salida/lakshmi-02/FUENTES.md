# Fuentes del video lakshmi-02 (generadas con IA vía vidIQ)

Este contenedor es temporal: el .mp4 de 3 horas NO sobrevive a la sesión.
Con estos enlaces lo reconstruyes idéntico en tu PC.

**Título:** Let The Universe Send You Unexpected Money 💸 Lakshmi's Infinite Wealth Current • 888 Hz • 3 Hours

## Música base (instrumental original, libre de regalías, 172 s)
https://ai-music-tracks.s3.us-east-1.amazonaws.com/db0bbcfc-841e-4d3f-bd3f-6d9733b4f1fb/509a408f-4f21-45c3-95c8-2820de2706de.wav
→ guárdala como `bases/lakshmi-02.wav`

## Imágenes de fondo (1280x720, amplíalas a 2560 antes de renderizar)
1. https://ai-thumbnails.s3.amazonaws.com/editor/db0bbcfc-841e-4d3f-bd3f-6d9733b4f1fb/64f9a733-a4fe-4331-9e59-269c7e027c5a.png
2. https://ai-thumbnails.s3.amazonaws.com/editor/db0bbcfc-841e-4d3f-bd3f-6d9733b4f1fb/242f46f9-22de-4bfb-899d-0f212261fd49.png
3. https://ai-thumbnails.s3.amazonaws.com/editor/db0bbcfc-841e-4d3f-bd3f-6d9733b4f1fb/e2f933a8-39c5-4a5d-bdee-d75a069068e7.png
→ guárdalas en `salida/lakshmi-02/img/`

## Reconstruirlo
```bash
python3 scripts/03_audio.py --id lakshmi-02 --base bases/lakshmi-02.wav
python3 scripts/04_video.py --id lakshmi-02
python3 scripts/06_miniatura.py --id lakshmi-02 --img salida/lakshmi-02/img/1.png
python3 scripts/08_short.py --id lakshmi-02 --seg 45
```

## Verificado en esta sesión
- Video: 3 h 00 min · 1,7 GB · 1080p · 888 Hz · 9 min 15 s de render
- Short: 45 s · 1080x1920 · 9,6 MB
- Bucle sin saltos: en las uniones (segundos 160, 320, 480...) el salto máximo
  entre muestras fue de 1465 y 939, **por debajo** de los 2450 y 2816 de zonas
  normales de la música. El crossfade funciona.

> Descarga estos archivos pronto: los enlaces de S3 pueden caducar.
