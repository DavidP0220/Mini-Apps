# video_express_ai — automatización de VideoExpress.ai

Bot Playwright para generar imágenes/videos en VideoExpress.ai (https://app.videoexpress.ai/)
sin depender del navegador del usuario ni de clicks por coordenadas — más rápido y
confiable que controlar la app a través del navegador visible.

## Setup (una sola vez, o si la sesión expira)

```bash
pip install -r requirements.txt
python -m playwright install chromium
python setup_auth.py   # abre una ventana visible; el USUARIO inicia sesión manualmente
```

**Nunca** rellenar el email/contraseña del usuario automáticamente — `setup_auth.py`
existe justo para que el login lo haga la persona, no el bot. Una vez guardada la
sesión en `auth_state.json`, el resto de los comandos corren headless sin pedir login.

## Uso

> ⚠️ **ANTES DE GENERAR NADA PARA MINDSET MECHANICS**, leer
> `../ESTILO_MINDSET_MECHANICS.md`. Los prompts de tipo `"Flat 2D vector comic
> panel..."` que aparecían aquí **producen el estilo equivocado** — fueron la causa
> de que el 5º video del canal (Resiliencia) saliera en estilo cómic americano con
> tramas de semitono y viñetas, sin nada que ver con lo publicado, y quedara
> inservible. Ese archivo tiene la plantilla de prompt correcta ya validada.

```bash
# Reestilizar una imagen/personaje ya generado (preserva identidad — MEJOR
# que un prompt de texto libre cuando ya existe una imagen base del personaje)
python generate_video.py stylize --style "Comic Book" --out personaje_comic.jpg

# Imagen suelta desde cero — usar SIEMPRE la plantilla de ESTILO_MINDSET_MECHANICS.md
python generate_video.py image "$(cat prompt.txt)" --type 2D --out escena1.jpg

# Imagen + marcarla como personaje reutilizable (para lipsync consistente entre clips)
python generate_video.py image "..." --type 2D --consistent-character

# Clip con lipsync (personaje hablando)
python generate_video.py lipsync \
    --video-prompt "Actor 1 is a bald man in a black cap, talking to camera" \
    --script "Frase corta, menos de 100 caracteres." \
    --out clip1.mp4
```

Los archivos generados se guardan en `outputs/` (configurable vía `OUTPUT_DIR` en `.env`).

## Reglas duras (aprendidas a mano en la sesión 2026-08-19/20, antes de que existiera este bot)

1. **Límite de 100 caracteres en `--script`/Actor Script.** La app rechaza cualquier
   línea de diálogo más larga con el error "Sorry, the number of characters in the
   actors scripts cannot exceed 100 characters." Para un guion largo, trocearlo en
   frases cortas y generar un clip por frase.
2. **`Image Type: 2D`** da ilustración plana genuina (estilo cómic/vector). Dejar el
   tipo por defecto (`Human`) o el auto-enhance activado empuja el resultado hacia
   foto-realista con stickers de cómic superpuestos — no es lo mismo.
3. **El checkbox "Automatically enhance my image prompt" se re-marca solo** cada vez
   que se abre el modal de creación. `create_image()` ya lo desmarca explícitamente
   antes de cada generación — no quitar esa línea.
4. **Los botones "Save Image"/"Download" de la UI no son confiables** (no siempre
   descargan nada al disco). Este bot nunca los usa: captura la URL real
   (`s3.renderplatform.com/user-assets/preview/{id}.jpg|mp4`) interceptando la
   respuesta de red con `page.expect_response(...)`, y descarga esa URL directo.
   Si se agregan nuevas funciones al bot, seguir este mismo patrón.
5. **El disclaimer de "Consistent Character" solo aparece la primera vez** por
   sesión — `mark_consistent_character()` ya maneja el caso en que no aparece
   (timeout corto, sigue de largo).
6. **No usar `page.mouse.wheel()` / scroll manual sin necesidad.** El bug que
   colgaba el navegador en la exploración manual (antes de este bot) estaba
   asociado a scroll — con Playwright y selectores por texto/rol normalmente no
   hace falta scrollear nada, los `.click()`/`.fill()` de Playwright autoscrollean
   el elemento a la vista de forma segura. Si algún selector nuevo sí necesita
   scroll explícito, usar `locator.scroll_into_view_if_needed()` (método nativo de
   Playwright), nunca `mouse.wheel`.

7. **Nunca dos procesos a la vez sobre la misma cuenta.** `session.py` toma un
   lock (`.videoexpress.lock`) al arrancar cualquier comando; el segundo proceso
   falla con `SessionBusyError` en vez de arrancar. Motivo real: el polling que
   identifica el render terminado mira Media Library > My AI Videos, que es
   **global de la cuenta** — con dos corridas simultáneas cada una puede
   descargar el clip de la otra y las dos quedan registradas como correctas.
   Si el lock quedó huérfano (proceso muerto), caduca solo a las 2h, o se borra
   a mano.
8. **`snapshot_video_ids(page)` antes de cada animación.** El CLI ya lo hace.
   Si escribes un script nuevo que llame a `create_silent_video()` o
   `animate_library_image()` directo, toma la foto de IDs ANTES de abrir el
   modal y pásala como `known_ids=`. Sin eso, `_poll_for_latest_video()` no
   puede distinguir el clip nuevo del anterior.
9. **Nada de togglear checkboxes a ciegas.** Usar `_set_checkbox_by_label(page,
   texto, deseado)`, que LEE el `<input>` real antes de tocarlo. El patrón
   viejo (`get_by_text(...).click()`) asume el estado inicial; si la app cambia
   un default, el mismo click hace lo contrario de lo que se quería — en el caso
   de "Share this in the public gallery" eso significa **publicar un borrador
   en la galería pública sin autorización**.

10. **La duración del clip hay que PEDIRLA, y el máximo es 10s.** Si no se pasa
    `duration_seconds=`, VideoExpress elige la duración sola y devuelve 5s / 6s /
    8s de forma impredecible — medido con ffprobe sobre los 20 clips del lote de
    Resiliencia. Eso hizo creer durante un tiempo que la plataforma tenía un
    **techo duro de 8s**; es falso. El modal esconde tras el checkbox
    **"Advanced Mode"** un `manual_video_length` y un
    `<input type="range" name="video_duration" min="3" max="10">`.
    **Rango real: 3-10 segundos.** 12s no existen en esta plataforma (lo confirma
    la petición abierta del roadmap oficial "Increase maximum AI video clip length
    to 10 seconds or more", roadmap.videoexpress.ai/feedback/205505).
    Usar siempre `animate_library_image(..., duration_seconds=N)` /
    `create_silent_video(..., duration_seconds=N)`. La telemetría D6 ahora guarda
    `requested_duration_s` y `actual_duration_s` (ffprobe) en cada evento, para que
    un descuadre así se detecte solo y no dentro de tres semanas en el montaje.

## Catálogo de tutoriales oficiales

https://videoexpress.ai/tutorials/ tiene decenas de video-tutoriales cortos organizados
por categoría (Tutoriales V3.0, V2.0, Conceptos básicos del editor, Capacitación del
cliente, Clases magistrales). Útil para descubrir funciones de la app que este bot
todavía no cubre (ej. "Stylize Character" se encontró ahí) antes de asumir que algo
no existe. No requiere login para verse.

## Contexto de por qué existe este bot

Antes de este bot, VideoExpress.ai se operaba controlando el navegador real del
usuario por clicks en coordenadas de pantalla (`claude-in-chrome` MCP) — funcionaba
pero era lento, frágil ante cualquier cambio de layout, y consumía muchos tokens por
cada captura de pantalla. Este proyecto reemplaza esa vía para producción en
cantidad; usar `claude-in-chrome` solo si hace falta explorar una función nueva de
la UI que este bot todavía no cubre (y después portarla aquí).

Ver también, en la memoria persistente del usuario: `reference_videoexpress_ai.md`
(gotchas de la app) y `project_mindset_mechanics.md` (canal para el que se construyó
esto — evolutionary-psychology, host calvo/gorra negra/hoodie gris, paleta
navy/amarillo/rojo).
