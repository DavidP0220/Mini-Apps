# Red de Canales de Abundancia — Sistema de Produccion

Fabrica de contenido para 3 canales de YouTube de musica de frecuencias.
**60 videos por mes** (20 por canal), producidos con un pipeline semi-automatico.

| Canal | Handle | Deidad | Nicho |
|---|---|---|---|
| Maha Lakshmi Sanctuary | @MahaLakshmiSanctuary | Goddess Maha Lakshmi | Riqueza, fortuna, oro |
| Lord Ganesha 432Hz | @LordGanesha432Hz | Lord Ganesha | Abrecaminos, negocios |
| Archangel Uriel Divine Light | @ArchangelUrielLight | Archangel Uriel | Provision divina, sueno |

## Estructura

```
abundancia-canales/
  datos/catalogo.json     <- los 60 videos (titulo, Hz, duracion, escena, miniatura)
  salida/<canal>/*.md     <- paquete listo para copiar/pegar en YouTube Studio
  salida/<id>/            <- carpeta de trabajo de cada video (img/, audio.wav, mp4)
  bases/<id>.wav          <- melodias base que TU generas con IA (2-5 min)
  scripts/                <- generadores y renderizadores
  panel/index.html        <- tablero de produccion (marca A/I/R/P y guarda el avance)
  GUIA.md                 <- guia completa paso a paso + estrategia de ingresos
```

## Uso rapido

```bash
python3 scripts/01_catalogo.py                                  # regenera el catalogo
python3 scripts/02_paquetes.py                                  # regenera los 60 paquetes
python3 scripts/03_audio.py --id lakshmi-01 --base bases/lakshmi-01.wav
python3 scripts/04_video.py --id lakshmi-01                     # anade --4k si quieres 2160p
python3 scripts/05_lote.py --canal lakshmi                      # lote completo del canal
```

Requisito unico: **ffmpeg** (Windows: `winget install Gyan.FFmpeg` · Mac: `brew install ffmpeg`).

Abre el panel con el `serve.ps1` del repo y entra a `/abundancia-canales/panel/`.

Lee **GUIA.md** antes de empezar.
