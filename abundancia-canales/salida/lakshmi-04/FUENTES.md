# Fuentes del video lakshmi-04 (generadas con IA vía vidIQ)

Este contenedor es temporal: el .mp4 de 8 horas NO sobrevive a la sesión.
Con estos enlaces lo reconstruyes idéntico en tu PC.

**Título:** Receive Unexpected Money This Week 💰 Sacred Lotus of Prosperity • 432 Hz • 8 Hours

Es el video de **sueño** del canal: estética oscura, no dorada. Para "sleep music"
la imagen tiene que invitar a cerrar los ojos, no a mirar la pantalla.

## Música base (instrumental original, libre de regalías, 176 s)
https://ai-music-tracks.s3.us-east-1.amazonaws.com/db0bbcfc-841e-4d3f-bd3f-6d9733b4f1fb/314e96a7-c865-430b-a94d-d665ace2a27f.wav
→ guárdala como `bases/lakshmi-04.wav`

## Imágenes de fondo (1280x720, amplíalas a 2560 antes de renderizar)
1. https://ai-thumbnails.s3.amazonaws.com/editor/db0bbcfc-841e-4d3f-bd3f-6d9733b4f1fb/7ceec97b-5c54-48f1-8f35-57f7a824fa21.png  (loto sobre lago nocturno, 75/100)
2. https://ai-thumbnails.s3.amazonaws.com/editor/db0bbcfc-841e-4d3f-bd3f-6d9733b4f1fb/c5b65d2b-9da2-46dc-b32d-ea7b67fe24b8.png  (templo bajo las estrellas)
3. https://ai-thumbnails.s3.amazonaws.com/editor/db0bbcfc-841e-4d3f-bd3f-6d9733b4f1fb/541bf6f5-f3d9-412e-b4c0-c64bd0850f23.png  (estanque con luciérnagas, **96/100**)
→ guárdalas en `salida/lakshmi-04/img/`

## Reconstruirlo
```bash
python3 scripts/03_audio.py --id lakshmi-04 --base bases/lakshmi-04.wav
python3 scripts/04_video.py --id lakshmi-04
python3 scripts/06_miniatura.py --id lakshmi-04 --img salida/lakshmi-04/img/1.png
python3 scripts/08_short.py --id lakshmi-04 --seg 45
```

⚠️ **Reserva tiempo y disco.** Este es el más pesado del proyecto:
- Audio: 27 minutos de proceso y **4.167 MB** de FLAC intermedio
- Video final: ~4 GB
- Borra el `audio.flac` en cuanto tengas el mp4

Consejo: corre primero `--prueba 60` para revisar la mezcla antes de comprometer
media hora de CPU.

> Descarga estos archivos pronto: los enlaces de S3 pueden caducar.
