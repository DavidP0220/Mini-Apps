"""Motor de automatización Playwright para VideoExpress.ai.

Encapsula el flujo real descubierto a mano (sesión 2026-08-20):
- El bug que congelaba el navegador venía de acciones de scroll manual —
  aquí no aplica: Playwright interactúa por selector, nunca por coordenadas
  de scroll, así que ese problema no existe en esta ruta.
- El checkbox "Automatically enhance my image prompt" se re-marca solo cada
  vez que se abre el modal — siempre se desmarca explícitamente antes de
  generar.
- La forma más confiable de obtener el archivo generado NO es el botón
  "Save Image"/"Download" (no descargaba nada de forma fiable en pruebas
  manuales) sino interceptar la respuesta de red hacia
  s3.renderplatform.com/user-assets/preview/*.jpg (o .mp4 para video).
- El diálogo de Lipsync tiene un límite duro de 100 caracteres en
  "Actor 1 Script" — validado aquí antes de enviar, para fallar rápido con
  un mensaje claro en vez de que la app lo rechace silenciosamente.
"""
import json
import os
import re
import shutil
import subprocess
import time
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError

APP_URL = "https://app.videoexpress.ai/"
ASSET_URL_RE = re.compile(r"https://s3\.renderplatform\.com/user-assets/preview/[a-f0-9-]+\.(jpg|png|mp4)")

# Anclados a la carpeta del modulo, NO al directorio de trabajo. Con rutas
# relativas ("outputs"/"logs") el destino dependia de desde donde se lanzara
# el script: ejecutandolo desde la raiz del repo, todo caia en
# <raiz>/outputs y <raiz>/logs, que la lista blanca del .gitignore raiz
# (regla "/*") ignora en silencio -> imagenes, videos y la telemetria D6 se
# escribian a disco pero NUNCA entraban en git, y Recraft/VideoExpress
# borran el original a los 60 dias. Las variables de entorno siguen mandando
# si estan puestas (se resuelven contra el modulo si son relativas).
_MODULE_DIR = Path(__file__).resolve().parent


def _anchored(env_var: str, default: str) -> Path:
    p = Path(os.getenv(env_var, default))
    return p if p.is_absolute() else _MODULE_DIR / p


OUTPUT_DIR = _anchored("OUTPUT_DIR", "outputs")
LOG_DIR = _anchored("LOG_DIR", "logs")

# ffprobe: se resuelve del PATH (o de la variable FFPROBE) en vez de estar
# clavado a la instalacion WinGet de una maquina concreta - esa ruta absoluta
# hacia que _check_aspect_ratio explotara en cualquier otro equipo o clon
# limpio del repo.
FFPROBE = os.getenv("FFPROBE") or shutil.which("ffprobe") or "ffprobe"


def _check_aspect_ratio(image_path: Path) -> None:
    """VideoExpress rechaza animar (Create Video queda deshabilitado, sin
    error claro en pantalla mas alla de un banner que aparece DESPUES de
    elegir la imagen) cualquier imagen que no sea 16:9 o 9:16 exacto/casi
    exacto. Confirmado en vivo 2026-08-25 con true_character_ref.jpg
    (650x900, retrato de ficha de personaje) - por eso las imagenes de
    Recraft para el pivot de Kimi deben exportarse a 1920x1080 (escena
    completa), NUNCA como el retrato aislado de referencia de personaje.
    Falla aqui, antes de subir, en vez de descubrirlo a mitad del flujo en
    la UI."""
    try:
        result = subprocess.run(
            [FFPROBE, "-v", "error", "-select_streams", "v:0",
             "-show_entries", "stream=width,height", "-of", "csv=p=0", str(image_path)],
            capture_output=True, text=True, timeout=30,
        )
    except subprocess.TimeoutExpired:
        # Un ffprobe colgado (archivo corrupto o en red) bloqueaba el
        # proceso indefinidamente justo antes de subir la imagen.
        raise VideoExpressError(f"ffprobe se colgó leyendo {image_path.name} (>30s)")
    except FileNotFoundError:
        raise VideoExpressError(
            f"No se encontro ffprobe ('{FFPROBE}'). Instala ffmpeg o apunta la "
            "variable de entorno FFPROBE al ejecutable."
        )
    # Sin este chequeo, un fallo de ffprobe (archivo corrupto, formato no
    # soportado) dejaba stdout vacio y reventaba mas abajo con un
    # "not enough values to unpack" que no dice nada de la causa real.
    if result.returncode != 0 or not result.stdout.strip():
        raise VideoExpressError(
            f"ffprobe no pudo leer {image_path.name}: {result.stderr.strip()[:300] or 'sin salida'}"
        )
    width, height = (int(x) for x in result.stdout.strip().split(","))
    ratio = width / height
    if not (abs(ratio - 16 / 9) < 0.02 or abs(ratio - 9 / 16) < 0.02):
        raise VideoExpressError(
            f"{image_path.name} es {width}x{height} (ratio {ratio:.3f}) - "
            "VideoExpress solo anima imagenes 16:9 o 9:16. Exporta la escena "
            "completa de Recraft a 1920x1080 (o 1080x1920 vertical), no el "
            "retrato aislado de referencia del personaje."
        )


def _log_generation_event(event: dict) -> None:
    """Persiste un evento de generación (JSONL, un objeto por línea) en
    logs/generation_log_YYYY-MM-DD.jsonl. Ver handoffs/HANDOFF_2026-08-23_
    autorizacion_regeneracion_y_qa.md item D6: sin esto no se puede auditar
    cuántos créditos se gastaron realmente en cada corrida. No debe romper
    la generación si falla (best-effort, nunca lanza)."""
    try:
        LOG_DIR.mkdir(parents=True, exist_ok=True)
        day = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        log_path = LOG_DIR / f"generation_log_{day}.jsonl"
        event = {"timestamp": datetime.now(timezone.utc).isoformat(), **event}
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(event, ensure_ascii=False) + "\n")
    except Exception as exc:  # nunca interrumpir la generación por un fallo de logging
        print(f"[log] no se pudo escribir el log de generación: {exc}", flush=True)


def _probe_duration_seconds(path: Path) -> float | None:
    """Duración real de un .mp4 en segundos, o None si no se pudo medir.

    Best-effort a propósito: si ffprobe falta o falla, NO debe tumbar una
    generación cuyo crédito ya está gastado — solo se pierde la telemetría.
    """
    try:
        out = subprocess.run(
            [FFPROBE, "-v", "error", "-show_entries", "format=duration",
             "-of", "default=nw=1:nk=1", str(path)],
            capture_output=True, text=True, timeout=60, check=True,
        )
        return round(float(out.stdout.strip()), 3)
    except Exception as exc:
        print(f"[duracion] no se pudo medir {path.name}: {exc}", flush=True)
        return None


class VideoExpressError(RuntimeError):
    pass


@dataclass
class GeneratedAsset:
    url: str
    local_path: Path


DOWNLOAD_TIMEOUT_S = 180
DOWNLOAD_ATTEMPTS = 3


def _download(url: str, dest: Path) -> Path:
    """Descarga con timeout, reintento y escritura atómica.

    Antes era `urllib.request.urlretrieve(url, dest)` a secas. Tres problemas
    reales, todos con el crédito YA gastado en ese punto:
    1. Sin timeout: una conexión que se queda colgada bloquea el proceso
       para siempre (mismo modo de fallo que dejó a un agente atascado 10
       minutos en otra parte del proyecto). Ahora corta a los 180s.
    2. Sin reintento: un hipo de red = asset pagado perdido, y la URL del
       CDN de VideoExpress es temporal.
    3. Sin atomicidad: si el proceso moría a mitad, quedaba un .mp4/.jpg
       truncado con el nombre correcto — se ensamblaba después y el fallo
       aparecía mucho más tarde, lejos de su causa. Ahora se escribe a
       .part y se renombra solo al terminar.
    """
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(dest.suffix + ".part")
    last_exc = None
    for attempt in range(1, DOWNLOAD_ATTEMPTS + 1):
        try:
            with urllib.request.urlopen(url, timeout=DOWNLOAD_TIMEOUT_S) as resp:
                data = resp.read()
            if not data:
                raise VideoExpressError("la descarga vino vacía (0 bytes)")
            tmp.write_bytes(data)
            tmp.replace(dest)
            return dest
        except Exception as exc:
            last_exc = exc
            print(f"[descarga] intento {attempt}/{DOWNLOAD_ATTEMPTS} falló ({exc})", flush=True)
            if attempt < DOWNLOAD_ATTEMPTS:
                time.sleep(3 * attempt)
    tmp.unlink(missing_ok=True)
    _log_generation_event({"kind": "download_error", "url": url, "dest": str(dest), "error": str(last_exc)[:500]})
    raise VideoExpressError(
        f"No se pudo descargar {url} tras {DOWNLOAD_ATTEMPTS} intentos: {last_exc}. "
        "El crédito ya se gastó — el archivo sigue en Media Library de VideoExpress, "
        "recuperarlo desde ahí antes de regenerar."
    )


def open_editor(page: Page) -> None:
    # app.videoexpress.ai responde lento de forma habitual (se han medido ~10s solo
    # para el primer byte), asi que el timeout por defecto de 30s de Playwright se
    # agota antes de que cargue. 120s cubre el peor caso observado.
    page.set_default_navigation_timeout(120_000)
    page.set_default_timeout(60_000)
    page.goto(APP_URL, wait_until="domcontentloaded")
    try:
        page.wait_for_load_state("networkidle", timeout=60_000)
    except PlaywrightTimeoutError:
        pass  # la app mantiene conexiones abiertas; con el DOM listo alcanza
    # Cierra el panel "Latest News and Updates" si aparece
    close_news = page.get_by_role("button", name="Close")
    try:
        close_news.click(timeout=3000)
    except PlaywrightTimeoutError:
        pass


def _open_create_with_ai_panel(page: Page) -> None:
    """El primer click en 'Create with AI' a veces no registra si la página
    aún está inicializando su JS — reintenta hasta ver una tarjeta conocida
    del panel (evita una carrera de timing observada en pruebas reales).

    Confirmado 2026-08-22 (2 fallos reproducibles con el mismo stack trace):
    si el panel ya estaba abierto de una sesión anterior — el tab activo del
    dock lateral persiste por cuenta, no por sesión de navegador — el nav
    item deja de resolver como role="link" (probablemente cambia de rol/
    estado al estar "activo") y el click se queda esperando el timeout por
    defecto completo (60s) sin encontrar nunca el elemento, sin que el bucle
    de reintento llegue a actuar. Por eso ahora se comprueba primero si el
    marcador del panel ya es visible — caso confirmado por captura de
    pantalla real — antes de intentar clickear nada, y cada click usa un
    timeout corto para que el reintento sea real y no agote el presupuesto
    en el primer intento."""
    marker = page.get_by_text("Create Video From Prompt").first
    try:
        marker.wait_for(state="visible", timeout=2000)
        return  # el panel ya estaba abierto de una sesión anterior
    except PlaywrightTimeoutError:
        pass

    ai_link = page.get_by_role("link", name="Create with AI")
    for _ in range(3):
        try:
            ai_link.click(timeout=5000)
        except PlaywrightTimeoutError:
            continue
        try:
            marker.wait_for(state="visible", timeout=4000)
            return
        except PlaywrightTimeoutError:
            continue
    marker.wait_for(state="visible", timeout=10000)


def open_create_video_from_prompt(page: Page, landscape: bool = True) -> None:
    """Abre el modal 'Create Video From Prompt' desde el panel 'Create with AI'."""
    _open_create_with_ai_panel(page)

    card = page.locator("text=Create Video From Prompt").first
    card.scroll_into_view_if_needed(timeout=15000)
    card.wait_for(state="visible", timeout=15000)
    # El botón flecha está dentro de la misma tarjeta
    card.locator("xpath=ancestor::div[.//button][1]").get_by_role("button").last.click()

    modal_heading = page.locator("#modals-container").get_by_role("heading", name="Create Video From Prompt")
    modal_heading.wait_for(state="visible", timeout=15000)

    aspect_btn = page.locator("#modals-container").get_by_role(
        "button", name="Landscape 16:9" if landscape else "Vertical 9:16"
    )
    try:
        aspect_btn.click(timeout=3000)
    except PlaywrightTimeoutError:
        pass


def _set_image_type(page: Page, image_type: str) -> None:
    """image_type: uno de 'Human', '2D', '3D', 'Photorealistic (Cinematic)', 'Other'."""
    select = page.locator("select").filter(has_text="Image Type").first
    if not select.count():
        # fallback: primer <select> visible dentro del modal
        select = page.get_by_role("combobox").first
    select.select_option(label=f"Image Type: {image_type}")


def _set_checkbox_by_label(page: Page, label_text: str, desired: bool, required: bool = True) -> None:
    """Deja un checkbox en el estado `desired`, leyendo su estado REAL antes
    de tocarlo.

    Por qué existe (2026-08-25): el patrón que había repartido por el archivo
    era `page.get_by_text("...").click()`, es decir, un *toggle a ciegas*
    asumiendo el estado inicial. Eso es un bug latente en todos los casos, y
    en uno concreto es peligroso: en animate_library_image() se clickeaba
    "Share this in the public gallery" asumiendo que venía marcado, para
    desmarcarlo. Si un día viene DESMARCADO (cambio de default de la app,
    preferencia recordada por cuenta), ese mismo click lo MARCA — y el
    piloto de David acaba publicado en la galería pública de VideoExpress
    sin que nadie lo autorice. Leer el estado antes de actuar convierte un
    riesgo de publicación accidental en un no-evento.

    Se apoya en el <input type=checkbox> real (oculto tras un <label> que
    pinta el check con CSS) para LEER, y clickea el <label>/texto visible
    para ESCRIBIR — que es lo que de verdad togglea un input oculto.
    """
    container = page.locator("label", has_text=label_text).first
    checkbox = container.locator('input[type="checkbox"]')
    try:
        checkbox.wait_for(state="attached", timeout=5000)
    except PlaywrightTimeoutError:
        # Plan B: no hay <input> localizable (layout distinto). Se usa el
        # texto visible, pero SIN togglear a ciegas: se avisa y se sale.
        msg = f"No se encontró el checkbox '{label_text}' para dejarlo en {desired}"
        if required:
            raise VideoExpressError(
                msg + ". Se aborta en vez de clickear a ciegas: un toggle sin leer el "
                "estado puede activar justo lo contrario de lo que se pide."
            )
        print(f"[checkbox] {msg} - se continúa (no era obligatorio)", flush=True)
        return

    if checkbox.is_checked() != desired:
        container.click()
        if checkbox.is_checked() != desired:
            raise VideoExpressError(
                f"El checkbox '{label_text}' no quedó en {desired} después de clickearlo."
            )


def _ensure_auto_enhance_off(page: Page) -> None:
    """Confirmado 2026-08-22 vía inspección de DOM real: el checkbox es un
    <input type=checkbox name="auto_enhance_prompt"> genuino, pero vive
    dentro de un <label class="custom-checkbox"> que lo oculta visualmente
    y pinta el check con CSS sobre el <span> hermano — por eso el intento
    anterior (xpath a un input "preceding" del texto, con fallback de click
    por coordenadas) no lo desmarcaba de forma confiable: se comprobó con
    una captura que quedaba marcado pese a haber "corrido" la función, y la
    IA reescribía el prompt entero por su cuenta (auto-enhance seguía
    activo). Fix: apuntar directo al name real (estable, no depende de
    texto ni de xpath frágil) y clickear el <label> visible — que es lo que
    de verdad togglea un <input> oculto tras un <label> nativo — en vez de
    intentar togglear el <input> mismo, que Playwright puede rechazar por
    no ser "visible" aunque esté presente en el DOM."""
    checkbox = page.locator('input[name="auto_enhance_prompt"]')
    # wait_for(attached): is_checked() sobre un locator que aún no existe
    # lanza un error genérico de Playwright difícil de leer. Con la espera,
    # o está y se lee bien, o falla con un mensaje propio.
    try:
        checkbox.wait_for(state="attached", timeout=10000)
    except PlaywrightTimeoutError:
        raise VideoExpressError(
            "No apareció el checkbox 'auto_enhance_prompt'. Se aborta antes de generar: "
            "con auto-enhance activo, VideoExpress reescribe el prompt y el estilo del "
            "canal se rompe (ver ESTILO_MINDSET_MECHANICS.md)."
        )
    if checkbox.is_checked():
        page.locator('label.custom-checkbox', has=checkbox).click()


# Rango real del control de duración de VideoExpress, leído del DOM en vivo
# (2026-08-25): <input type="range" name="video_duration" min="3" max="10"
# value="5">. NO es un valor inventado ni copiado de la documentación.
VIDEO_DURATION_MIN_S = 3
VIDEO_DURATION_MAX_S = 10
VIDEO_DURATION_DEFAULT_S = 5


def _set_video_duration(page: Page, seconds: int) -> None:
    """Fija la duración EXACTA del clip a generar.

    ## Por qué existe (hallazgo 2026-08-25, causa raíz de un falso "techo de 8s")

    Hasta hoy el bot NUNCA tocaba la duración: generaba siempre en modo
    automático y VideoExpress elegía la longitud por su cuenta. Midiendo con
    ffprobe los 20 clips del lote anterior, las duraciones salían cuantizadas
    en 5,04s / 6,04s / 8,04s sin ningún patrón — y como ninguna pasaba de
    8,04s, se concluyó (razonablemente, pero mal) que la plataforma tenía un
    techo duro de 8 segundos.

    No es un techo: es que nadie estaba pidiendo la duración. El modal
    "Create Video From Prompt" esconde tras el checkbox **"Advanced Mode"**
    dos controles que el bot ignoraba:
      - `manual_video_length` (checkbox): activa la duración manual.
      - `video_duration` (range): min=3, max=10, default=5.

    Consecuencias prácticas:
      1. Se pueden pedir clips de hasta **10 segundos**, no 8.
      2. La duración deja de ser una lotería y pasa a ser determinista, que es
         lo que hace posible cuadrar los paneles con el timecode fijo de la
         voz en off.
      3. **12 segundos NO son posibles** en esta plataforma: el propio slider
         tope en 10. Corroborado por la petición abierta en el roadmap oficial
         "Increase maximum AI video clip length to 10 seconds or more"
         (roadmap.videoexpress.ai/feedback/205505) — si piden subirlo A 10 o
         más, el máximo de hoy es exactamente 10.

    Por eso el storyboard del piloto se rediseñó a paneles de 10s (ver
    handoffs/REPORTE_2026-08-25_duracion_resuelta.md).
    """
    if not isinstance(seconds, int):
        raise VideoExpressError(f"La duración debe ser un entero de segundos, no {seconds!r}.")
    if not (VIDEO_DURATION_MIN_S <= seconds <= VIDEO_DURATION_MAX_S):
        raise VideoExpressError(
            f"Duración pedida: {seconds}s. VideoExpress solo admite "
            f"{VIDEO_DURATION_MIN_S}-{VIDEO_DURATION_MAX_S}s por clip. "
            "Se aborta ANTES de gastar el crédito: pedir una duración fuera de "
            "rango no falla de forma visible, simplemente devuelve otra "
            "duración y rompe el cuadre con la voz en off."
        )

    # El slider vive oculto hasta que Advanced Mode está activo.
    # "Advanced Mode" sí es texto visible del modal -> se usa el helper que lee
    # el estado real antes de tocarlo (regla 9 de video_express_ai/CLAUDE.md).
    _set_checkbox_by_label(page, "Advanced Mode", True, required=True)

    # `manual_video_length` en cambio NO tiene texto visible estable asociado:
    # se apunta por el atributo name real, igual que auto_enhance_prompt. Sin
    # marcarlo, el slider existe pero la app sigue eligiendo la duración sola.
    manual = page.locator('input[name="manual_video_length"]')
    try:
        manual.wait_for(state="attached", timeout=10000)
    except PlaywrightTimeoutError:
        raise VideoExpressError(
            "No apareció el checkbox 'manual_video_length' tras activar Advanced Mode. "
            "Se aborta antes de generar: sin duración manual el clip sale de 5-8s "
            "aleatorios y no cuadra con el timecode de la voz en off."
        )
    if not manual.is_checked():
        # El <input> está oculto tras un <label> que pinta el check con CSS:
        # se clickea el label, que es lo que de verdad togglea el input.
        page.locator("label", has=manual).first.click()
        if not manual.is_checked():
            raise VideoExpressError("No se pudo activar la duración manual ('manual_video_length').")

    slider = page.locator('input[name="video_duration"]')
    try:
        slider.wait_for(state="attached", timeout=10000)
    except PlaywrightTimeoutError:
        raise VideoExpressError(
            "No apareció el control 'video_duration' tras activar Advanced Mode. "
            "Se aborta antes de generar: sin él la duración vuelve a ser automática "
            "(5-8s aleatorios) y el clip no cuadra con el storyboard."
        )

    # Un <input type=range> pintado por JS no reacciona a .fill() a secas en
    # todos los frameworks: hay que emitir 'input' y 'change' a mano para que
    # el estado de la app se entere del nuevo valor.
    slider.evaluate(
        """(el, value) => {
            const setter = Object.getOwnPropertyDescriptor(
                window.HTMLInputElement.prototype, 'value').set;
            setter.call(el, String(value));
            el.dispatchEvent(new Event('input', { bubbles: true }));
            el.dispatchEvent(new Event('change', { bubbles: true }));
        }""",
        seconds,
    )

    # Verificación explícita: si el valor no quedó puesto, abortar ANTES de
    # gastar el crédito es mucho más barato que descubrirlo con ffprobe después.
    actual = slider.input_value()
    if str(actual) != str(seconds):
        raise VideoExpressError(
            f"El slider de duración quedó en {actual}s en vez de {seconds}s. "
            "Se aborta antes de generar."
        )
    print(f"[duracion] clip solicitado a {seconds}s (Advanced Mode + duración manual)", flush=True)


def create_image(
    page: Page,
    prompt: str,
    image_type: str = "2D",
    filename: str | None = None,
) -> GeneratedAsset:
    """Genera una imagen (sin video) y la descarga localmente.

    image_type='2D' es el recomendado para estilo ilustración/cómic plano;
    'Human'/'Photorealistic (Cinematic)' para b-roll fotorrealista.
    """
    image_prompt_box = page.get_by_placeholder("A man drinking coffee in a rainy cafe")
    image_prompt_box.click()
    page.keyboard.press("Control+A")
    image_prompt_box.fill(prompt)

    _set_image_type(page, image_type)
    _ensure_auto_enhance_off(page)

    # 60s no alcanza cuando el servicio esta degradado (visto el 2026-08-22: la
    # generacion tardo >60s y reventaba aqui aunque el render si se completaba).
    # .jpg o .png: el regex de arriba acepta ambos, pero este filtro solo
    # miraba .jpg — si VideoExpress devolvía un .png, la respuesta nunca
    # matcheaba y se agotaban los 240s DESPUÉS de haber gastado el crédito.
    with page.expect_response(lambda r: ASSET_URL_RE.match(r.url) and r.url.endswith((".jpg", ".png")), timeout=240000) as resp_info:
        page.get_by_role("button", name="Create Image").click()
    response = resp_info.value
    url = response.url

    filename = filename or url.rsplit("/", 1)[-1]
    local_path = _download(url, OUTPUT_DIR / filename)
    print(f"Imagen generada: {local_path}")
    _log_generation_event({
        "kind": "image",
        "label": filename,
        "prompt": prompt,
        "image_type": image_type,
        "status": "completed",
        "url": url,
        "local_path": str(local_path),
    })
    return GeneratedAsset(url=url, local_path=local_path)


def _click_first_picker_thumbnail(page: Page) -> None:
    """Clickea la primera miniatura del picker 'Select Image'. Las miniaturas
    se pintan como CSS background-image sobre un div (NO <img src>), así que
    page.locator('img') no las encuentra confiablemente. Se hace click por
    coordenadas relativas al heading 'Select Image' del diálogo (offset
    calibrado a mano viendo el layout real: la primera tarjeta queda ~60px a
    la derecha y ~200px abajo del heading)."""
    heading = page.get_by_text("Select Image", exact=True)
    heading.wait_for(state="visible", timeout=15000)
    page.wait_for_timeout(1000)  # deja que las miniaturas terminen de pintarse
    box = heading.bounding_box()
    if not box:
        raise VideoExpressError("No se pudo ubicar el diálogo 'Select Image'")
    page.mouse.click(box["x"] + 60, box["y"] + 200)


def mark_consistent_character(page: Page, folder: str = "My AI Images") -> None:
    """Marca una imagen como 'Consistent Character' (personaje reutilizable).

    `folder` controla de dónde se toma la Reference Photo en el picker:
    - "My AI Images" (default): la última imagen generada en la app.
    - "Images": una imagen subida a mano con import_local_image(), p.ej.
      REFERENCIA_personaje.png o una de sus vistas front/back/left/right.
      Usar esto es la vía recomendada en MANUAL_PRODUCCION.md §2 Técnica A
      para fijar la identidad del host en vez de depender de texto solo.

    Confirmado 2026-08-22 vía captura de pantalla real: marcar el checkbox
    "Use Consistent Character" dispara INMEDIATAMENTE un modal "Disclaimer"
    que tapa el resto del panel (incl. "Reference Photo" y el botón
    "Consistent Character", que queda disabled) hasta que se acepta con
    "I Agree". El orden anterior (clickear "Consistent Character" antes de
    resolver el disclaimer) fallaba siempre por esto — el botón nunca
    llegaba a habilitarse. Orden correcto: checkbox -> aceptar disclaimer ->
    elegir Reference Photo -> recién ahí el botón "Consistent Character"
    queda disponible.
    """
    checkbox_label = page.get_by_text("Use Consistent Character")
    checkbox_label.click()

    try:
        agree_btn = page.get_by_role("button", name="I Agree")
        agree_btn.click(timeout=8000)
    except PlaywrightTimeoutError:
        pass  # ya se había aceptado antes en esta sesión, no vuelve a aparecer

    # Selecciona la imagen de referencia como Reference Photo
    ref_slot = page.get_by_text("Reference Photo", exact=True)
    ref_slot.click()
    # Carpeta dentro del picker (segunda fila, primera carpeta del picker)
    page.get_by_text(folder, exact=True).last.click()
    _click_first_picker_thumbnail(page)
    page.get_by_role("button", name="Choose").click()

    consistent_btn = page.get_by_role("button", name="Consistent Character")
    consistent_btn.click()


def create_lipsync_video(
    page: Page,
    video_prompt: str,
    actor_script: str,
    filename: str | None = None,
) -> GeneratedAsset:
    """Genera un clip con lipsync (personaje hablando). `actor_script` debe
    ser UNA frase corta: la app rechaza más de 100 caracteres por clip."""
    if len(actor_script) > 100:
        raise VideoExpressError(
            f"actor_script tiene {len(actor_script)} caracteres, máximo 100. "
            "Divide el guion en frases más cortas, un clip por frase."
        )

    video_prompt_box = page.get_by_placeholder("He takes a sip of coffee. Include the sound of")
    video_prompt_box.click()
    page.keyboard.press("Control+A")
    video_prompt_box.fill(video_prompt)

    _set_checkbox_by_label(page, "Lipsync HD Video", True, required=False)

    page.get_by_role("button", name="Create Video").click()
    _dismiss_aspect_ratio_confirm(page)

    # Sub-modal "Create Lipsync Audio"
    sub_modal = page.get_by_role("heading", name="Create Lipsync Audio")
    sub_modal.wait_for(state="visible", timeout=15000)

    sub_video_prompt = page.get_by_placeholder(re.compile("Actor 1 is the father"))
    sub_video_prompt.fill(video_prompt)

    sub_script = page.get_by_placeholder(re.compile("Hi son, how are you doing today"))
    sub_script.fill(actor_script)

    with page.expect_response(lambda r: ASSET_URL_RE.match(r.url) and r.url.endswith(".mp4"), timeout=180000) as resp_info:
        sub_modal.get_by_role("button", name="Create").click()
    response = resp_info.value
    url = response.url

    filename = filename or url.rsplit("/", 1)[-1]
    local_path = _download(url, OUTPUT_DIR / filename)
    print(f"Video generado: {local_path}")
    _log_generation_event({
        "kind": "lipsync_video",
        "label": filename,
        "video_prompt": video_prompt,
        "actor_script": actor_script,
        "status": "completed",
        "url": url,
        "local_path": str(local_path),
    })
    return GeneratedAsset(url=url, local_path=local_path)


def stylize_character(
    page: Page,
    style: str = "Comic Book",
    filename: str | None = None,
) -> GeneratedAsset:
    """Re-renderiza la última imagen seleccionada en 'My AI Images' con un
    estilo preset, preservando la identidad del personaje (mismo rostro,
    ropa, pose) — más confiable que un prompt de texto libre para mantener
    consistencia visual entre escenas.

    style: uno de 'Realistic', '3D Pixar', 'Anime', 'Comic Book', 'Line Art',
    'Watercolor'.
    """
    _open_create_with_ai_panel(page)

    card = page.get_by_text("Stylize Character", exact=True).first
    card.scroll_into_view_if_needed(timeout=15000)
    card.wait_for(state="visible", timeout=15000)
    card.locator("xpath=ancestor::div[.//button][1]").get_by_role("button").last.click()

    page.get_by_text("select", exact=True).click()  # "Please [select] an image."
    page.get_by_text("My AI Images", exact=True).click()
    _click_first_picker_thumbnail(page)
    page.get_by_role("button", name="Choose").click()

    style_select = page.get_by_role("combobox").first
    style_select.select_option(label=f"Style: {style}")

    with page.expect_response(lambda r: ASSET_URL_RE.match(r.url), timeout=60000) as resp_info:
        page.get_by_role("button", name="Create Image").click()
    url = resp_info.value.url

    filename = filename or url.rsplit("/", 1)[-1]
    local_path = _download(url, OUTPUT_DIR / filename)
    print(f"Personaje reestilizado ({style}): {local_path}")
    # Faltaba la línea de telemetría D6: esta función gasta crédito igual que
    # create_image() y no dejaba rastro en logs/, así que la auditoría de
    # créditos por corrida salía incompleta.
    _log_generation_event({
        "kind": "stylize",
        "label": filename,
        "style": style,
        "status": "completed",
        "url": url,
        "local_path": str(local_path),
    })
    return GeneratedAsset(url=url, local_path=local_path)


def create_silent_video(
    page: Page,
    image_prompt: str,
    video_prompt: str,
    image_type: str = "2D",
    filename: str | None = None,
    known_ids: set | None = None,
    duration_seconds: int | None = None,
) -> GeneratedAsset:
    """Genera una imagen y la anima SIN diálogo (b-roll con movimiento real,
    no Ken Burns) — usa 'Video Only (No Sound)', evita el sub-modal de
    Lipsync y su límite de 100 caracteres, ideal para escenas narrativas sin
    un personaje hablando a cámara.

    `video_prompt` es donde va la DIRECCIÓN DE CÁMARA (dolly in, paneo con
    paralaje, retroceso revelador...), que es lo que da vida real al plano.
    El default de `image_type` es "2D" porque este bot se usa para Mindset
    Mechanics; "Photorealistic (Cinematic)" rompe el estilo del canal."""
    image_prompt_box = page.get_by_placeholder("A man drinking coffee in a rainy cafe")
    image_prompt_box.click()
    page.keyboard.press("Control+A")
    image_prompt_box.fill(image_prompt)

    _set_image_type(page, image_type)
    _ensure_auto_enhance_off(page)

    # mismo motivo que en create_image(): 60s no alcanza con el servicio lento
    # .jpg o .png: el regex de arriba acepta ambos, pero este filtro solo
    # miraba .jpg — si VideoExpress devolvía un .png, la respuesta nunca
    # matcheaba y se agotaban los 240s DESPUÉS de haber gastado el crédito.
    with page.expect_response(lambda r: ASSET_URL_RE.match(r.url) and r.url.endswith((".jpg", ".png")), timeout=240000):
        page.get_by_role("button", name="Create Image").click()

    video_prompt_box = page.get_by_placeholder("He takes a sip of coffee. Include the sound of")
    video_prompt_box.click()
    page.keyboard.press("Control+A")
    video_prompt_box.fill(video_prompt)

    _set_checkbox_by_label(page, "Video Only (No Sound)", True, required=False)

    if duration_seconds is not None:
        _set_video_duration(page, duration_seconds)

    page.get_by_role("button", name="Create Video").click()
    _dismiss_aspect_ratio_confirm(page)
    close_modal(page)

    label = filename or "unnamed"
    url = _poll_for_latest_video(page, max_wait=1800, label=label, known_ids=known_ids)
    filename = filename or url.rsplit("/", 1)[-1]
    local_path = _download(url, OUTPUT_DIR / filename)
    print(f"Video (sin dialogo) generado: {local_path}")
    _log_generation_event({
        "kind": "silent_video",
        "label": label,
        "image_prompt": image_prompt,
        "video_prompt": video_prompt,
        "image_type": image_type,
        "status": "completed",
        "requested_duration_s": duration_seconds,
        "actual_duration_s": _probe_duration_seconds(local_path),
        "url": url,
        "local_path": str(local_path),
    })
    return GeneratedAsset(url=url, local_path=local_path)


def animate_library_image(
    page: Page,
    image_name: str,
    video_prompt: str,
    folder: str = "Images",
    filename: str | None = None,
    public_gallery: bool = False,
    known_ids: set | None = None,
    duration_seconds: int | None = None,
) -> GeneratedAsset:
    """Anima una imagen YA SUBIDA a Media Library (via import_local_image())
    con un Video Action Prompt real - image-to-video genuino, sin generar
    una imagen nueva desde texto. Pieza que faltaba para el pivot de Kimi
    (HANDOFF_2026-08-25_decision_tercera_via_resiliencia.md, Decision 1): las
    imagenes se generan en Recraft AI (fuera de este bot) y se validan a
    mano antes de subirlas aqui - este bot solo las anima.

    Confirmado en vivo 2026-08-25: 'Create Video From Prompt' tiene un boton
    'Use from Library' junto al checkbox 'Use Consistent Character' que abre
    el mismo picker 'Select Image' que ya usan mark_consistent_character() y
    add_media_to_timeline() - reusa ese patron en vez de escribir un Image
    Prompt de texto.

    `image_name`: texto visible bajo la miniatura en el picker (el nombre de
    archivo subido, sin extension - ej. 'recraft_escena01_v1').
    `public_gallery`: False por defecto - un piloto/borrador no debe quedar
    publico en la galeria de VideoExpress hasta que David lo apruebe.

    `duration_seconds`: duracion EXACTA del clip (3-10s). Si se deja en None,
    VideoExpress elige sola y devuelve 5-8s impredecibles - ver
    _set_video_duration(). Para el piloto de la 3a via se usa 10.
    """
    use_from_library = page.get_by_role("button", name="Use from Library")
    use_from_library.click()

    heading = page.get_by_text("Select Image", exact=True)
    heading.wait_for(state="visible", timeout=15000)
    page.get_by_text(folder, exact=True).last.click()
    page.wait_for_timeout(1000)

    thumb = page.get_by_text(image_name, exact=False).first
    thumb.wait_for(state="visible", timeout=15000)
    thumb.click()
    page.get_by_role("button", name="Choose").click()

    video_prompt_box = page.get_by_placeholder("He takes a sip of coffee. Include the sound of")
    video_prompt_box.click()
    page.keyboard.press("Control+A")
    video_prompt_box.fill(video_prompt)

    _set_checkbox_by_label(page, "Video Only (No Sound)", True, required=False)

    # `required=True` a propósito: si no se puede LEER el estado del
    # checkbox de galería pública, se aborta antes de generar. Es preferible
    # perder una corrida a publicar un borrador en la galería pública de
    # VideoExpress sin autorización de David.
    _set_checkbox_by_label(page, "Share this in the public gallery", public_gallery, required=True)

    if duration_seconds is not None:
        _set_video_duration(page, duration_seconds)

    page.get_by_role("button", name="Create Video").click()
    _dismiss_aspect_ratio_confirm(page)
    close_modal(page)

    label = filename or image_name
    url = _poll_for_latest_video(page, max_wait=1800, label=label, known_ids=known_ids)
    filename = filename or url.rsplit("/", 1)[-1]
    local_path = _download(url, OUTPUT_DIR / filename)
    print(f"Video animado desde imagen de librería ({image_name}): {local_path}")
    # Telemetría D6: se registra la duración PEDIDA junto a la REAL medida con
    # ffprobe. Es lo que faltaba para detectar el problema del "techo de 8s"
    # sin tener que auditar los .mp4 a mano meses después.
    actual = _probe_duration_seconds(local_path)
    if duration_seconds is not None and actual is not None and abs(actual - duration_seconds) > 1.0:
        print(
            f"[duracion] AVISO: se pidieron {duration_seconds}s pero el clip mide "
            f"{actual:.2f}s. El storyboard no va a cuadrar con la voz en off.",
            flush=True,
        )
    _log_generation_event({
        "kind": "animate_library_image",
        "label": label,
        "image_name": image_name,
        "folder": folder,
        "video_prompt": video_prompt,
        "status": "completed",
        "requested_duration_s": duration_seconds,
        "actual_duration_s": actual,
        "url": url,
        "local_path": str(local_path),
    })
    return GeneratedAsset(url=url, local_path=local_path)


def snapshot_video_ids(page: Page, folder: str = "My AI Videos") -> set:
    """Devuelve los IDs de los videos que YA existen en `folder`.

    Se llama ANTES de lanzar una generación y su resultado se pasa a
    create_silent_video()/animate_library_image() como `known_ids`. Ver el
    bug documentado en _poll_for_latest_video: sin esta foto previa, el
    polling puede devolver un video viejo como si fuera el recién generado.
    """
    try:
        with page.expect_response(lambda r: "get_media" in r.url, timeout=20000) as resp_info:
            open_media_library_folder(page, folder)
        ids = {item.get("id") for item in resp_info.value.json().get("results", [])}
    except Exception as exc:
        print(f"[snapshot] no se pudieron leer los videos existentes: {exc}", flush=True)
        ids = set()
    finally:
        close_modal(page)
    print(f"[snapshot] {len(ids)} videos ya existentes en '{folder}'", flush=True)
    return ids


def _poll_for_latest_video(
    page: Page,
    max_wait: int = 300,
    interval: int = 15,
    label: str = "unnamed",
    known_ids: set | None = None,
) -> str:
    """'Video Only'/Image-to-Video NO devuelve el mp4 como respuesta directa
    del click — la app renderiza en background y avisa 'aparecerá en tu
    Media Library cuando esté listo'. Confirmado con curl al endpoint real:
    `api/library/get_media` trae `status` ('completed'/'pending') y
    `mediaPath` (URL CDN final) por cada item — mucho más confiable que
    adivinar por DOM o esperar una respuesta de red que puede no llegar
    nunca en ese request. Se hace polling reabriendo la carpeta hasta que
    el item más nuevo aparezca 'completed'.

    BUG CORREGIDO 2026-08-25 (silencioso, el peor tipo): la versión anterior
    aceptaba `results[0]` en cuanto lo veía 'completed', SIN comprobar que
    fuera un item nuevo. Como un render tarda ~210s, en el primer tick el
    item más reciente es casi siempre el video ANTERIOR, ya completado —
    así que la función devolvía la URL del clip viejo, el bot lo descargaba
    con el nombre del clip nuevo, y la telemetría lo registraba como
    'completed'. Nada fallaba: simplemente el video ensamblado tenía la
    escena equivocada, y encima el clip que sí se pagó quedaba sin
    descargar. `known_ids` (foto previa vía snapshot_video_ids) elimina la
    ambigüedad. Si no se pasa, se usa el primer tick como línea base — sirve
    porque ningún render termina en menos de 15s, pero es un plan B: lo
    correcto es pasar known_ids.
    """
    # CORREGIDO 2026-08-23 tras 4 fallos en vivo: "My AI Videos" en la
    # GRILLA de Media Library (antes de entrar) es una tarjeta de carpeta,
    # resuelve a 1 solo elemento con get_by_text(exact=True). El selector
    # ".library-panel-category-title" (el título de "ya estoy adentro")
    # NO existe todavía en ese punto — usarlo para decidir si hacer click
    # dejaba el bucle esperando por algo que nunca aparecía sin haber
    # entrado antes. Diagnosticado con capturas: el click en la carpeta SÍ
    # funcionaba siempre (confirmado con un video real quedando en estado
    # 'processing', estimatedTimeSeconds=210) — el bug era 100% de lectura
    # de estado, no de generación. Fix: reusar open_media_library_folder(),
    # ya probada con las carpetas Audio/Images, y capturar el get_media que
    # dispara su propio click.
    deadline = time.time() + max_wait
    baseline = set(known_ids) if known_ids is not None else None
    while time.time() < deadline:
        with page.expect_response(lambda r: "get_media" in r.url, timeout=20000) as resp_info:
            open_media_library_folder(page, "My AI Videos")
        results = resp_info.value.json().get("results", [])

        if baseline is None:
            baseline = {item.get("id") for item in results}
            print(f"[poll] linea base tomada del primer tick ({len(baseline)} items). "
                  "Pasa known_ids=snapshot_video_ids(page) para hacerlo bien.", flush=True)
            _log_generation_event({"kind": "poll_baseline_fallback", "label": label, "count": len(baseline)})

        # Solo interesan los items que NO existían antes de lanzar esta
        # generación. `results[0]` sin este filtro devolvía videos viejos.
        fresh = [item for item in results if item.get("id") not in baseline]
        if fresh:
            newest = fresh[0]
            print(f"[poll] nuevo: status={newest.get('status')!r} mediaPath={newest.get('mediaPath')!r} id={newest.get('id')!r}", flush=True)
            _log_generation_event({
                "kind": "poll_tick",
                "label": label,
                "status": newest.get("status"),
                "mediaPath": newest.get("mediaPath"),
                "id": newest.get("id"),
            })
            if newest.get("status") == "completed" and newest.get("mediaPath"):
                close_modal(page)
                return newest["mediaPath"]
            if newest.get("status") == "failed":
                # Sin esto el bucle seguía esperando hasta el timeout completo
                # (30 min) por un render que la propia app ya dio por muerto.
                _log_generation_event({"kind": "render_failed", "label": label, "id": newest.get("id")})
                close_modal(page)
                raise VideoExpressError(
                    f"VideoExpress reporta el render como 'failed' (id={newest.get('id')}). "
                    "El crédito puede haberse consumido igual — revisar en la app antes de reintentar."
                )
        else:
            print(f"[poll] aun no aparece ningun video nuevo ({len(results)} items, todos conocidos)", flush=True)
            _log_generation_event({"kind": "poll_tick", "label": label, "status": None, "note": "sin items nuevos"})
        close_modal(page)
        page.wait_for_timeout(interval * 1000)
    _log_generation_event({"kind": "poll_timeout", "label": label, "max_wait": max_wait})
    raise VideoExpressError(
        f"El video no terminó de renderizar en {max_wait}s. El crédito ya se gastó: "
        "busca el clip a mano en Media Library > My AI Videos antes de reintentar."
    )


def _import_local_file(page: Page, file_path: Path, folder: str) -> None:
    """Sube un archivo local a una carpeta de 'My Media'.

    Unifica import_local_audio() e import_local_image(), que eran el mismo
    procedimiento copiado dos veces y solo diferían en la carpeta destino.
    La duplicación ya había costado divergencia: los comentarios con el
    diagnóstico real (por qué .last, por qué "+ Add files", por qué hace
    falta confirmar con "Upload files") solo existían en la copia de audio.

    IMPORTANTE: 'Import Media' en el panel 'Create with AI' es para servicios
    externos (Text to Speech, CloneVoice.ai, Artistly) — NO tiene un input de
    archivo local. El upload real está en el picker de Media Library, botón
    '↑ Upload file'. Confirmado 2026-08-20 vía captura de pantalla, tras
    fallar el primer intento silenciosamente (0 <input type=file>).
    """
    file_path = Path(file_path)
    # Fallar aquí y no a mitad del flujo en la UI, donde el error aparece
    # como un timeout sin causa aparente.
    if not file_path.exists():
        raise VideoExpressError(f"No existe el archivo a subir: {file_path}")

    page.get_by_role("link", name="Media Library").click()
    page.wait_for_timeout(1000)
    # OJO: el nombre de carpeta matchea DOS elementos — el tab superior
    # (Stock) y la carpeta real dentro de "My Media" — .last es la carpeta.
    # Usar .first aterriza en la pestaña de stock, que no tiene upload propio.
    page.get_by_text(folder, exact=True).last.click()
    page.get_by_role("button", name="Upload file").click(timeout=10000)
    # Se abre un modal intermedio "Upload Media" con un botón "+ Add files".
    # No dispara un file-chooser nativo real (Playwright nunca ve el evento
    # "filechooser"): solo revela un <input type=file> oculto en el DOM, así
    # que set_input_files directo funciona (confirmado 2026-08-20).
    page.get_by_role("button", name="Add files").click(timeout=10000)
    page.locator("input[type=file]").first.set_input_files(str(file_path))
    page.wait_for_timeout(1000)
    # El archivo queda "staged" con su nombre editable — falta confirmar con
    # el botón "Upload files" para que realmente suba.
    with page.expect_response(lambda r: "upload" in r.url.lower() and r.request.method == "POST", timeout=30000):
        page.get_by_role("button", name="Upload files").click()
    page.wait_for_timeout(2000)
    close_modal(page)
    page.wait_for_timeout(4000)  # deja que la subida aparezca en la carpeta
    _log_generation_event({"kind": "import", "folder": folder, "file": str(file_path)})


def import_local_audio(page: Page, audio_path: Path) -> None:
    """Sube un archivo de audio local (ej. voz en off de ElevenLabs) a la
    carpeta 'Audio' de Media Library."""
    _import_local_file(page, audio_path, "Audio")


def import_local_image(page: Page, image_path: Path) -> None:
    """Sube una imagen local (ej. un still de Recraft, o REFERENCIA_personaje
    .png) a la carpeta 'Images' de Media Library, para animarla después con
    animate_library_image() o usarla como Reference Photo de 'Consistent
    Character' (ver mark_consistent_character).

    Valida la proporción ANTES de subir: VideoExpress solo anima 16:9/9:16."""
    _check_aspect_ratio(Path(image_path))
    _import_local_file(page, image_path, "Images")


def open_media_library_folder(page: Page, folder_name: str) -> None:
    """Abre el panel Media Library y navega a una carpeta de 'My Media' por
    su nombre exacto (ej. 'My AI Videos', 'Audio', 'Images'). Usa el mismo
    patrón de reintento por timing que _open_create_with_ai_panel."""
    media_link = page.get_by_role("link", name="Media Library")
    folder = page.get_by_text(folder_name, exact=True).last
    for _ in range(3):
        media_link.click()
        try:
            folder.wait_for(state="visible", timeout=4000)
            break
        except PlaywrightTimeoutError:
            continue
    folder.click()
    page.wait_for_timeout(1000)


def add_media_to_timeline(page: Page, caption_text: str, folder_name: str = "My AI Videos") -> None:
    """Agrega a la línea de tiempo el primer clip/imagen dentro de
    `folder_name` cuyo caption visible contenga `caption_text` (ej. un
    fragmento del prompt usado para generarlo). Doble click abre un menú
    contextual con 'Add to Timeline' entre otras opciones (confirmado
    2026-08-20 vía captura de pantalla: Play/Download/Add to Timeline/
    Redesign/Fix Video/Voice Changer/Save Audio/.../Delete)."""
    open_media_library_folder(page, folder_name)
    item = page.get_by_text(caption_text, exact=False).first
    item.wait_for(state="visible", timeout=15000)
    item.dblclick()
    page.get_by_text("Add to Timeline", exact=True).click(timeout=10000)
    close_modal(page)


def enable_automatic_captions(page: Page) -> None:
    """Activa el generador de subtítulos automáticos sincronizados sobre
    todo el audio de la línea de tiempo (recomendado 2026 para retención:
    captions animados obligatorios en Shorts/Reels)."""
    page.get_by_role("link", name="Automatic Captions").click()
    generate_btn = page.get_by_role("button", name=re.compile("Generate", re.I))
    generate_btn.click()
    # La transcripción + generación de captions puede tardar según duración
    page.wait_for_selector("text=/Captions? (added|generated|ready)/i", timeout=120000)


def export_video(page: Page, filename: str | None = None) -> GeneratedAsset:
    """Exporta el video final de la línea de tiempo completa y lo descarga."""
    with page.expect_response(
        lambda r: ASSET_URL_RE.match(r.url) and r.url.endswith(".mp4"), timeout=300000
    ) as resp_info:
        page.get_by_role("button", name="Export Video").click()
        # Algunas apps piden confirmar calidad/resolución en un segundo modal
        confirm_btn = page.locator("#modals-container").get_by_role("button", name=re.compile("Export|Download", re.I))
        try:
            confirm_btn.click(timeout=5000)
        except PlaywrightTimeoutError:
            pass
    url = resp_info.value.url
    filename = filename or url.rsplit("/", 1)[-1]
    local_path = _download(url, OUTPUT_DIR / filename)
    print(f"Video final exportado: {local_path}")
    _log_generation_event({
        "kind": "export",
        "label": filename,
        "status": "completed",
        "url": url,
        "local_path": str(local_path),
    })
    return GeneratedAsset(url=url, local_path=local_path)


def _dismiss_aspect_ratio_confirm(page: Page) -> None:
    """La PRIMERA vez que se hace click en 'Create Video' en una sesión,
    aparece un popup 'Confirm — Would you like to create 16:9 media by
    default going forward?' que bloquea el job hasta que se responde. Sin
    esto, expect_response() nunca ve la respuesta .mp4 y hace timeout a los
    180s (bug real encontrado 2026-08-20 vía captura de pantalla antes/
    después de Create Video, no por adivinar)."""
    confirm = page.locator("#modals-container").get_by_text("Confirm", exact=True)
    try:
        confirm.wait_for(state="visible", timeout=4000)
        page.locator("#modals-container").get_by_role("button", name="Yes").click()
    except PlaywrightTimeoutError:
        pass  # no apareció esta vez (ya se respondió antes en la sesión)


def close_modal(page: Page) -> None:
    try:
        page.get_by_role("button", name="Close").last.click(timeout=3000)
    except PlaywrightTimeoutError:
        pass
