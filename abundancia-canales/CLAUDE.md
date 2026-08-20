# Red de Canales de Abundancia — contexto del proyecto

Claude Code lee este archivo automáticamente al abrir la carpeta. El estado
completo y estructurado está en `PROYECTO.json`.

## Qué es esto

Una fábrica para producir y publicar **100 videos** de música de frecuencias en
**tres canales de YouTube en inglés**, hasta llegar a la monetización.
No es un repositorio de videos: es el sistema que los produce.

| Canal | Nicho | Momento |
|---|---|---|
| Maha Lakshmi Sanctuary | Riqueza y fortuna | Mañana |
| Lord Ganesha 432Hz | Abrecaminos y negocios | Mañana |
| Archangel Uriel Divine Light | Provisión divina y sueño | Noche |

## Herramienta preferida del usuario: VideoExpress.ai

El usuario quiere que **toda** la producción visual pase por **https://videoexpress.ai/**.

**No confundir con InVideo** (invideo.io): son productos distintos. InVideo sí tiene
servidor MCP, pero **no es el que el usuario usa**. Ya hubo una confusión por esto.

A día de hoy no se ha confirmado que VideoExpress.ai ofrezca MCP. Si en la sesión local
tienes acceso al navegador, entra a su web y busca Integrations, API o Developers.
Si tiene MCP, conéctalo y úsalo para todo. Si no, el usuario genera allí y los archivos
se colocan en `salida/<id>/img/`.

## Cómo se habla con el usuario

Español. Todo el contenido que se publica en YouTube va en inglés, porque el
RPM es de 3 a 5 veces mayor. El usuario no habla inglés: cada texto en inglés
va acompañado de una instrucción en español que dice exactamente dónde pegarlo.

## El comando que produce todo

```bash
python scripts/05_lote.py --canal lakshmi --lluvia -19
```

Hace por cada video: audio → video → miniatura → Short → gemelo en pantalla
negra → limpieza. Retoma si se interrumpe, no se detiene ante un fallo y se
frena antes de llenar el disco.

## Reglas que no se rompen

1. **Siempre `--prueba 60` antes de un render largo.** Media hora de CPU se
   pierde rápido cuando la lluvia quedó demasiado alta.
2. **Un video y su gemelo en pantalla negra nunca se publican el mismo día.**
   Mínimo 48 horas: si no, compiten por la misma búsqueda.
3. **La materia prima vive en `assets/origen/`.** No dependas de enlaces
   externos, caducan.
4. **Los videos armados no van al repositorio.** Pesan de 0,5 a 4 GB y se
   reconstruyen con dos comandos.
5. **Nunca prometer resultados económicos garantizados** en las descripciones.
   El descargo de responsabilidad ya está escrito; no quitarlo.

## Lo que decide la estrategia

Hacen falta **9.600 vistas** para las 4.000 horas de reproducción pero
**66.667** para los 1.000 suscriptores. Quien se duerme con un video de 8 horas
aporta 8 horas de una sentada, pero no se suscribe: está dormido.

Por eso los **Shorts son el motor**, no un complemento, y las **listas de
reproducción** son la palanca más barata para el tiempo de visión.

## Dónde está cada cosa

| Ruta | Contenido |
|---|---|
| `GUIA.md` | La estrategia completa, sección por sección |
| `datos/competencia.md` | Qué le funciona a la competencia, con datos de vidIQ |
| `datos/catalogo.json` | Los 63 videos con título, frecuencia y duración |
| `salida/<canal>/*.md` | Textos listos para copiar en YouTube Studio |
| `salida/_calendario/` | Fecha y hora exactas de cada publicación |
| `assets/origen/` | Música e imágenes de los videos ya producidos |
| `assets/marca/` | Avatares y banners de los tres canales |

## Antes de proponer cambios de estrategia

Lee `datos/competencia.md`. Ahí está registrado qué se probó, qué funcionó y
qué se descartó, con los números que lo respaldan. Varias decisiones que
parecen obvias ya se evaluaron y se rechazaron por razones concretas.
