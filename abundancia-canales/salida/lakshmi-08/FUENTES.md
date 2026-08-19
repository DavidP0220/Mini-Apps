# Fuentes del video lakshmi-08

**Título:** Prepare Now, Your Abundance Is Arriving 💸 Dhanya Lakshmi: Abundant Harvest • 888 Hz • 3 Hours
**Bloque:** Ashta Lakshmi

## Materia prima permanente (ya en el repositorio)
- Música: `assets/origen/musica/lakshmi-08.wav`
- Imágenes: `assets/origen/img/lakshmi-08-1.jpg`, `-2.jpg`, `-3.jpg`

Estos archivos están versionados en GitHub y no dependen de enlaces externos.

## Reconstruirlo
```bash
cp assets/origen/musica/lakshmi-08.wav bases/
mkdir -p salida/lakshmi-08/img && cp assets/origen/img/lakshmi-08-*.jpg salida/lakshmi-08/img/

python3 scripts/03_audio.py --id lakshmi-08 --base bases/lakshmi-08.wav
python3 scripts/04_video.py --id lakshmi-08
python3 scripts/06_miniatura.py --id lakshmi-08 --img salida/lakshmi-08/img/lakshmi-08-1.jpg
python3 scripts/08_short.py --id lakshmi-08 --seg 45
```
