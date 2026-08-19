# Fuentes del video lakshmi-09

**Título:** Wealth Is Being Attracted To You Right Now 💰 Gaja Lakshmi: Royal Fortune • 528 Hz • 1 Hour
**Bloque:** Ashta Lakshmi

## Materia prima permanente (ya en el repositorio)
- Música: `assets/origen/musica/lakshmi-09.wav`
- Imágenes: `assets/origen/img/lakshmi-09-1.jpg`, `-2.jpg`, `-3.jpg`

Estos archivos están versionados en GitHub y no dependen de enlaces externos.

## Reconstruirlo
```bash
cp assets/origen/musica/lakshmi-09.wav bases/
mkdir -p salida/lakshmi-09/img && cp assets/origen/img/lakshmi-09-*.jpg salida/lakshmi-09/img/

python3 scripts/03_audio.py --id lakshmi-09 --base bases/lakshmi-09.wav
python3 scripts/04_video.py --id lakshmi-09
python3 scripts/06_miniatura.py --id lakshmi-09 --img salida/lakshmi-09/img/lakshmi-09-1.jpg
python3 scripts/08_short.py --id lakshmi-09 --seg 45
```
