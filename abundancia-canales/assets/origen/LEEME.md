# Materia prima permanente

Aquí vive el origen de los videos, **dentro del repositorio**, para que no dependa
de enlaces externos que caducan. Con esta carpeta puedes reconstruir cualquier
video en tu equipo cuando quieras, aunque haya pasado un año.

## Qué hay

| Carpeta | Contenido | Peso |
|---|---|---|
| `musica/` | 7 pistas instrumentales originales, libres de regalías | 28 MB |
| `img/` | 21 imágenes de fondo, 1280x720 | 4,9 MB |

Las imágenes están a 1280x720, que es su resolución real de generación. Durante
la producción se amplían a 2560 px, pero eso es interpolación: no añade detalle,
así que guardarlas ampliadas solo ocupaba espacio (77 MB en vez de 4,9 MB).

## Nota sobre los archivos de música
Se llaman `.wav` pero por dentro son MP3 — así los entrega el generador. Se
conservan tal cual, sin reconvertir: pasarlos a FLAC los inflaba de 4 MB a 26 MB
sin ganar nada, porque la pérdida de calidad ya venía de origen.

## Cómo usarlos

```bash
cp assets/origen/musica/lakshmi-01.wav bases/
mkdir -p salida/lakshmi-01/img
cp assets/origen/img/lakshmi-01-*.jpg salida/lakshmi-01/img/

python3 scripts/03_audio.py --id lakshmi-01 --base bases/lakshmi-01.wav
python3 scripts/04_video.py --id lakshmi-01
python3 scripts/06_miniatura.py --id lakshmi-01 --img salida/lakshmi-01/img/lakshmi-01-1.jpg
python3 scripts/08_short.py --id lakshmi-01 --seg 45
```

El script de video acepta `.jpg` y `.png` por igual.
