"""Cliente minimo de la API real de Recraft AI (external.api.recraft.ai).

Reemplaza la automatizacion por navegador (fragil: se atasca, choca con
otras sesiones/agentes que usan el mismo Chrome compartido - ver
handoffs/ 2026-08-25 "conflicto de pestanas"). Con la API no hay
navegador de por medio: nada que se atasque, nada con que chocar, y el
gasto de creditos queda exacto (antes/despues via get_credits()).

Requiere RECRAFT_API_KEY en recraft_ai/.env (obtenida a mano una vez desde
el dashboard de Recraft -> Settings -> API, NUNCA commitear el valor real,
solo vive en .env que esta en .gitignore).

Referencia oficial usada para validar parametros (consultada 2026-08-25):
  https://www.recraft.ai/docs/api-reference/endpoints
  https://www.recraft.ai/docs/api-reference/appendix   (tamanos + rate limits)
"""
import json
import os
import threading
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

import requests

BASE_URL = "https://external.api.recraft.ai/v1"

# Anclados a la carpeta del modulo, NO al directorio de trabajo. Con rutas
# relativas ("outputs"/"logs") el destino dependia de desde donde se lanzara
# el script: ejecutandolo desde la raiz del repo, todo caia en <raiz>/outputs
# y <raiz>/logs, que la lista blanca del .gitignore raiz (regla "/*") ignora
# en silencio -> imagenes y telemetria escritas a disco pero NUNCA
# commiteadas, y Recraft borra el original a los 60 dias. Las variables de
# entorno siguen mandando si estan puestas.
_MODULE_DIR = Path(__file__).resolve().parent


def _anchored(env_var: str, default: str) -> Path:
    p = Path(os.getenv(env_var, default))
    return p if p.is_absolute() else _MODULE_DIR / p


OUTPUT_DIR = _anchored("RECRAFT_OUTPUT_DIR", "outputs")
LOG_DIR = _anchored("RECRAFT_LOG_DIR", "logs")

# Reintentos SOLO ante 429 (rate limit): un 429 es rechazo puro, no se ha
# generado nada ni se han gastado creditos, asi que repetir es seguro. Los
# 5xx NO se reintentan a proposito - la peticion pudo haberse ejecutado del
# lado de Recraft y reintentar cobraria la imagen dos veces.
RATE_LIMIT_RETRIES = 3
RATE_LIMIT_BACKOFF_S = (5, 15, 45)
# Tope para un Retry-After absurdo: nunca dormir mas de 5 min por un 429.
RATE_LIMIT_MAX_WAIT_S = 300

# Rate limit documentado por Recraft (Appendix): 100 imagenes por minuto y
# ademas 5 por segundo, por usuario. Un bucle de generacion en lote dispara
# peticiones tan rapido como el proceso pueda, asi que se auto-limita aqui a
# 1 cada 0.25s (4/s, con margen). Es preferible frenar solos a comernos 429s
# y depender del backoff.
_MIN_INTERVAL_S = 0.25
_throttle_lock = threading.Lock()
_last_request_at = 0.0

# === Tamanos validos por familia de modelo (Appendix oficial) ===
# Este es el bug mas caro que se corrigio aqui: el default anterior era
# model="recraftv4_1" + size="1820x1024". 1820x1024 SOLO existe en V2/V3;
# V4.x lo rechaza. Se enviaba una combinacion imposible en cada llamada.
_SIZES_V4 = {
    "1024x1024", "1536x768", "768x1536", "1280x832", "832x1280",
    "1216x896", "896x1216", "1152x896", "896x1152", "832x1344",
    "1280x896", "896x1280", "1344x768", "768x1344",
}
_SIZES_V4_PRO = {
    "2048x2048", "3072x1536", "1536x3072", "2560x1664", "1664x2560",
    "2432x1792", "1792x2432", "2304x1792", "1792x2304", "1664x2688",
    "2560x1792", "1792x2560", "2688x1536", "1536x2688",
}
_SIZES_V2_V3 = {
    "1024x1024", "2048x1024", "1024x2048", "1536x1024", "1024x1536",
    "1365x1024", "1024x1365", "1280x1024", "1024x1280", "1024x1707",
    "1707x1024", "1434x1024", "1024x1434", "1820x1024", "1024x1820",
}

# negative_prompt solo lo soportan V2/V3 segun la referencia de endpoints.
_MODELS_WITH_NEGATIVE_PROMPT = ("recraftv2", "recraftv3")

# 16:9 exacto = 1.77778. VideoExpress rechaza animar cualquier cosa que no
# sea 16:9 o 9:16 (confirmado en vivo 2026-08-25), y video_express_bot.
# _check_aspect_ratio aplica una tolerancia de 0.02 antes de subir. Estos
# son los unicos tamanos raster de Recraft que caen dentro de esa tolerancia:
#   1820x1024 -> 1.7773  (solo V2/V3)
#   1536x768  -> 2.000   NO
#   1344x768  -> 1.7500  NO (se pasa por 0.028 -> lo rechaza el bot)
# Es decir: por API, el unico 16:9 aceptable "de fabrica" es V3 @ 1820x1024.
# Con V4.1 hay que generar 1344x768 y recortar 12px de alto -> 1344x756,
# que si es 16:9 exacto (ver crop_to_16_9=True mas abajo).
SIZE_16_9_V3 = "1820x1024"
SIZE_16_9_V4_SOURCE = "1344x768"  # recortar a 1344x756 para 16:9 exacto


def _valid_sizes_for(model: str) -> set:
    m = model.lower()
    if "pro" in m:
        return _SIZES_V4_PRO
    if m.startswith("recraftv4"):
        return _SIZES_V4
    if m.startswith(("recraftv2", "recraftv3")):
        return _SIZES_V2_V3
    return set()  # modelo desconocido: no validamos, deja que la API decida


class RecraftError(RuntimeError):
    pass


def _validate_request(model: str, size: str, negative_prompt: str | None, n: int) -> None:
    """Falla ANTES de la llamada HTTP. Un 400 de Recraft no cuesta creditos,
    pero si cuesta tiempo y produce un mensaje opaco a mitad de un lote; peor
    aun, en un bucle de 12 escenas se descubre al final. Aqui se falla en
    seco con el motivo exacto y la lista de tamanos validos."""
    if not 1 <= n <= 6:
        raise RecraftError(f"n={n} fuera de rango: la API acepta entre 1 y 6 imagenes por peticion.")

    valid = _valid_sizes_for(model)
    if valid and size not in valid:
        raise RecraftError(
            f"size='{size}' no es valido para model='{model}'.\n"
            f"Tamanos aceptados por ese modelo: {', '.join(sorted(valid))}.\n"
            f"Para 16:9 (obligatorio si la imagen se va a animar en VideoExpress): "
            f"usa model='recraftv3' con size='{SIZE_16_9_V3}', o model V4.1 con "
            f"size='{SIZE_16_9_V4_SOURCE}' y crop_to_16_9=True."
        )

    if negative_prompt and not model.lower().startswith(_MODELS_WITH_NEGATIVE_PROMPT):
        raise RecraftError(
            f"negative_prompt solo lo soportan los modelos V2/V3 (model='{model}' no). "
            "O quitas el negativo, o cambias a model='recraftv3'. "
            "Con V4.x, los negativos van redactados dentro del propio prompt."
        )


def _api_key() -> str:
    key = os.getenv("RECRAFT_API_KEY")
    if not key:
        raise RecraftError(
            "RECRAFT_API_KEY no esta configurada. Ponla en recraft_ai/.env "
            "(obtenerla en recraft.ai -> Settings -> API)."
        )
    return key


def _headers() -> dict:
    return {"Authorization": f"Bearer {_api_key()}"}


def _retry_after_seconds(resp, fallback: int) -> int:
    """Segundos a esperar tras un 429, leidos de la cabecera Retry-After.

    RFC 9110 permite DOS formatos: segundos ("120") o fecha HTTP
    ("Wed, 26 Aug 2026 15:04:05 GMT"). El codigo anterior hacia `int(header)`
    a secas, asi que la variante de fecha lanzaba ValueError y reventaba el
    reintento -> se perdia el lote entero por un 429 que era recuperable.
    Tambien se acota: una cabecera absurda (Recraft devolviendo horas) dejaria
    el proceso dormido indefinidamente.
    """
    raw = (resp.headers.get("Retry-After") or "").strip()
    if not raw:
        return fallback
    try:
        wait = int(float(raw))
    except ValueError:
        try:
            when = parsedate_to_datetime(raw)
        except (TypeError, ValueError):
            return fallback
        if when is None:
            return fallback
        if when.tzinfo is None:
            when = when.replace(tzinfo=timezone.utc)
        wait = int((when - datetime.now(timezone.utc)).total_seconds())
    return max(1, min(wait, RATE_LIMIT_MAX_WAIT_S))


def _throttle() -> None:
    global _last_request_at
    with _throttle_lock:
        delta = time.monotonic() - _last_request_at
        if delta < _MIN_INTERVAL_S:
            time.sleep(_MIN_INTERVAL_S - delta)
        _last_request_at = time.monotonic()


def _log_event(event: dict) -> None:
    """Mismo patron que video_express_bot._log_generation_event - best
    effort, nunca interrumpe la generacion si falla el log."""
    try:
        LOG_DIR.mkdir(parents=True, exist_ok=True)
        day = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        log_path = LOG_DIR / f"generation_log_{day}.jsonl"
        event = {"timestamp": datetime.now(timezone.utc).isoformat(), **event}
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(event, ensure_ascii=False) + "\n")
    except Exception as exc:
        print(f"[log] no se pudo escribir el log: {exc}", flush=True)


def get_credits() -> dict:
    """GET /users/me - devuelve email, id, name y el balance de creditos."""
    resp = requests.get(f"{BASE_URL}/users/me", headers=_headers(), timeout=30)
    resp.raise_for_status()
    return resp.json()


def _credits_or_none():
    """Balance de creditos, o None si la consulta falla. El contador es
    telemetria, no parte del trabajo: antes un 429 o un corte de red en
    /users/me abortaba la generacion entera (o la dejaba sin registrar
    despues de haber gastado el credito)."""
    try:
        return get_credits().get("credits")
    except Exception as exc:
        print(f"[creditos] no se pudo leer el balance: {exc}", flush=True)
        return None


@dataclass
class GeneratedImage:
    url: str
    local_path: Path


# Firmas de archivo de los formatos que Recraft puede devolver. Sin este
# chequeo, si el CDN respondia con un HTML de error (403/expirado), se
# guardaba ese HTML con extension .png: un archivo que "existe", pesa poco y
# solo revienta mucho despues, al intentar subirlo a VideoExpress o al
# medirlo con ffprobe. Mejor detectarlo en el momento, con la URL todavia
# viva y el credito recien gastado.
_IMAGE_MAGIC = (b"\x89PNG\r\n\x1a\n", b"\xff\xd8\xff", b"RIFF", b"GIF8", b"<svg", b"<?xml")


def _looks_like_image(data: bytes) -> bool:
    return any(data.startswith(sig) for sig in _IMAGE_MAGIC)


def _download_image(url: str, dest: Path, attempts: int = 3) -> None:
    """Descarga con timeout, reintento y escritura atomica.

    - timeout: sin el, una conexion colgada bloquea el proceso para siempre
      (es exactamente el modo de fallo que ya costo 10 minutos de agente
      atascado en otra parte del proyecto).
    - reintento: la URL de Recraft es temporal y el credito YA esta gastado;
      rendirse al primer hipo de red equivale a tirar el dinero.
    - escritura atomica (.part -> replace): si el proceso muere a mitad de
      descarga, no queda un PNG truncado que aparente estar bien.
    """
    last_exc = None
    for attempt in range(1, attempts + 1):
        try:
            resp = requests.get(url, timeout=(10, 120))
            resp.raise_for_status()
            if not _looks_like_image(resp.content):
                raise RecraftError(
                    f"lo descargado no parece una imagen ({len(resp.content)} bytes, "
                    f"empieza por {resp.content[:16]!r})"
                )
            dest.parent.mkdir(parents=True, exist_ok=True)
            tmp = dest.with_suffix(dest.suffix + ".part")
            tmp.write_bytes(resp.content)
            tmp.replace(dest)
            return
        except Exception as exc:
            last_exc = exc
            if attempt < attempts:
                print(f"[descarga] intento {attempt}/{attempts} fallo ({exc}); reintentando", flush=True)
                time.sleep(2 * attempt)
    raise RecraftError(f"no se pudo descargar la imagen tras {attempts} intentos: {last_exc}")


def _crop_to_16_9(path: Path) -> tuple[int, int]:
    """Recorta el alto para dejar la imagen en 16:9 EXACTO (centrado).

    Necesario porque los modelos V4.x no ofrecen ningun tamano 16:9 exacto:
    el mas cercano es 1344x768 (1.750), y video_express_bot._check_aspect_
    ratio -y la propia VideoExpress- rechazan cualquier cosa que se desvie
    mas de 0.02 de 1.7778. 1344x768 -> 1344x756 si pasa.
    """
    try:
        from PIL import Image
    except ImportError as exc:  # pragma: no cover
        raise RecraftError(
            "crop_to_16_9 necesita Pillow (pip install -r recraft_ai/requirements.txt)"
        ) from exc

    with Image.open(path) as img:
        img = img.convert("RGB") if img.mode not in ("RGB", "RGBA") else img.copy()
        w, h = img.size
        target_h = round(w * 9 / 16)
        if target_h > h:  # imagen demasiado alta: se recorta el ancho
            target_w = round(h * 16 / 9)
            left = (w - target_w) // 2
            img = img.crop((left, 0, left + target_w, h))
        elif target_h < h:
            top = (h - target_h) // 2
            img = img.crop((0, top, w, top + target_h))
        img.save(path)
        return img.size


def generate_image(
    prompt: str,
    size: str = SIZE_16_9_V4_SOURCE,
    model: str = "recraftv4_1",
    style: str | None = None,
    style_id: str | None = None,
    negative_prompt: str | None = None,
    filename: str | None = None,
    label: str = "unnamed",
    crop_to_16_9: bool = True,
) -> GeneratedImage:
    """POST /images/generations.

    Defaults elegidos para el pipeline de Mindset Mechanics: V4.1 a 1344x768
    + recorte local a 1344x756 = 16:9 EXACTO, que es la unica condicion bajo
    la cual VideoExpress acepta animar la imagen despues.

    OJO (decision pendiente de Kimi/David, ver reporte 2026-08-25): 1344x756
    esta por debajo de 1080p. Las 12 escenas ya generadas por la app web
    salieron en 1376x768, tambien por debajo, asi que esto NO es una
    regresion - pero si se quiere 1080p nativo hay que pasar por
    /images/crispUpscale, que cuesta creditos aparte.

    style / style_id son mutuamente excluyentes (documentado). style_id es el
    mecanismo oficial de "estilo propio" (POST /styles con imagenes de
    referencia) y es la via correcta para fijar la identidad visual del
    personaje entre escenas; hoy solo es compatible con V3.

    NOTA: el parametro `image_url` que tenia esta funcion NO existe en
    /images/generations - image-to-image es otro endpoint. Se movio a
    image_to_image() para no seguir enviando un campo inexistente.
    """
    if style and style_id:
        raise RecraftError("style y style_id son mutuamente excluyentes: usa uno u otro.")
    _validate_request(model, size, negative_prompt, n=1)

    credits_before = _credits_or_none()

    body = {"prompt": prompt, "model": model, "size": size, "n": 1, "response_format": "url"}
    if style:
        body["style"] = style
    if style_id:
        body["style_id"] = style_id
    if negative_prompt:
        body["negative_prompt"] = negative_prompt

    for attempt in range(RATE_LIMIT_RETRIES + 1):
        _throttle()
        resp = requests.post(
            f"{BASE_URL}/images/generations", headers=_headers(), json=body, timeout=(10, 180)
        )
        if resp.status_code != 429 or attempt == RATE_LIMIT_RETRIES:
            break
        # Retry-After manda si Recraft lo envia; si no, backoff exponencial.
        wait = _retry_after_seconds(resp, RATE_LIMIT_BACKOFF_S[attempt])
        _log_event({"kind": "rate_limited", "label": label, "attempt": attempt + 1, "wait_s": wait})
        print(f"[rate-limit] 429 de Recraft, reintento {attempt + 1}/{RATE_LIMIT_RETRIES} en {wait}s", flush=True)
        time.sleep(wait)

    if resp.status_code != 200:
        _log_event({"kind": "image_error", "label": label, "status": resp.status_code, "body": resp.text[:2000]})
        raise RecraftError(f"Recraft API error {resp.status_code}: {resp.text[:500]}")

    try:
        image_url_result = resp.json()["data"][0]["url"]
    except (ValueError, KeyError, IndexError) as exc:
        # El credito ya se gasto: registrar el cuerpo crudo o se pierde toda
        # pista de que paso.
        _log_event({"kind": "image_bad_response", "label": label, "body": resp.text[:2000]})
        raise RecraftError(f"Respuesta inesperada de Recraft: {resp.text[:300]}") from exc

    # A partir de aqui el credito YA esta gastado. Se registra la URL ANTES
    # de intentar descargar: si la descarga falla, al menos queda en el log
    # la URL temporal para rescatarla a mano.
    _log_event({
        "kind": "image_generated",
        "label": label,
        "url": image_url_result,
        "size": size,
        "model": model,
        "credits_before": credits_before,
    })

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    filename = filename or f"{label}.png"
    local_path = OUTPUT_DIR / filename
    try:
        _download_image(image_url_result, local_path)
    except Exception as exc:
        _log_event({
            "kind": "download_error",
            "label": label,
            "url": image_url_result,
            "error": str(exc)[:500],
            "credits_before": credits_before,
        })
        raise RecraftError(
            f"La imagen se genero (credito gastado) pero no se pudo descargar: {exc}. "
            f"URL temporal: {image_url_result}"
        ) from exc

    final_size = size
    if crop_to_16_9:
        w, h = _crop_to_16_9(local_path)
        final_size = f"{w}x{h}"

    credits_after = _credits_or_none()
    _log_event({
        "kind": "image",
        "label": label,
        "prompt": prompt,
        "size": size,
        "final_size": final_size,
        "model": model,
        "style": style,
        "style_id": style_id,
        "status": "completed",
        "url": image_url_result,
        "local_path": str(local_path),
        "credits_before": credits_before,
        "credits_after": credits_after,
        "credits_spent": (credits_before - credits_after) if isinstance(credits_before, (int, float)) and isinstance(credits_after, (int, float)) else None,
    })
    print(f"Imagen generada ({label}): {local_path} [{final_size}] - creditos {credits_before} -> {credits_after}", flush=True)
    return GeneratedImage(url=image_url_result, local_path=local_path)


def image_to_image(
    prompt: str,
    image_path: Path,
    strength: float = 0.3,
    model: str = "recraftv3",
    style: str | None = None,
    style_id: str | None = None,
    negative_prompt: str | None = None,
    filename: str | None = None,
    label: str = "unnamed_i2i",
    crop_to_16_9: bool = True,
) -> GeneratedImage:
    """POST /images/imageToImage - genera una variante de una imagen local.

    Existe para reemplazar el parametro `image_url` que antes tenia
    generate_image(): ese campo NO forma parte de /images/generations (ver
    referencia oficial de endpoints), asi que se enviaba un campo inexistente
    creyendo estar haciendo image-to-image. El resultado era una imagen
    generada solo desde texto - es decir, el personaje NO heredaba nada de la
    referencia, pero el credito se gastaba igual.

    strength: 0 = casi identica a la original, 1 = ignora la original.
    Este endpoint es multipart/form-data (sube el archivo), no JSON.

    SIN PROBAR CONTRA LA API REAL (2026-08-25: no hay saldo/API key todavia y
    hay un gate explicito de Kimi que prohibe gastar creditos). Antes de
    usarlo en lote, correr UNA sola llamada y verificar el resultado.
    """
    if style and style_id:
        raise RecraftError("style y style_id son mutuamente excluyentes: usa uno u otro.")
    if not 0.0 <= strength <= 1.0:
        raise RecraftError(f"strength={strength} fuera de rango (0.0 - 1.0).")
    image_path = Path(image_path)
    if not image_path.exists():
        raise RecraftError(f"No existe la imagen de referencia: {image_path}")

    credits_before = _credits_or_none()

    data = {
        "prompt": prompt,
        "strength": str(strength),
        "model": model,
        "n": "1",
        "response_format": "url",
    }
    if style:
        data["style"] = style
    if style_id:
        data["style_id"] = style_id
    if negative_prompt and model.lower().startswith(_MODELS_WITH_NEGATIVE_PROMPT):
        data["negative_prompt"] = negative_prompt

    _throttle()
    with open(image_path, "rb") as fh:
        resp = requests.post(
            f"{BASE_URL}/images/imageToImage",
            headers=_headers(),
            data=data,
            files={"image": (image_path.name, fh)},
            timeout=(10, 180),
        )

    if resp.status_code != 200:
        _log_event({"kind": "i2i_error", "label": label, "status": resp.status_code, "body": resp.text[:2000]})
        raise RecraftError(f"Recraft imageToImage error {resp.status_code}: {resp.text[:500]}")

    try:
        image_url_result = resp.json()["data"][0]["url"]
    except (ValueError, KeyError, IndexError) as exc:
        _log_event({"kind": "i2i_bad_response", "label": label, "body": resp.text[:2000]})
        raise RecraftError(f"Respuesta inesperada de Recraft: {resp.text[:300]}") from exc

    _log_event({"kind": "i2i_generated", "label": label, "url": image_url_result, "credits_before": credits_before})

    filename = filename or f"{label}.png"
    local_path = OUTPUT_DIR / filename
    try:
        _download_image(image_url_result, local_path)
    except Exception as exc:
        _log_event({"kind": "download_error", "label": label, "url": image_url_result, "error": str(exc)[:500]})
        raise RecraftError(
            f"La imagen se genero (credito gastado) pero no se pudo descargar: {exc}. "
            f"URL temporal: {image_url_result}"
        ) from exc

    final_size = None
    if crop_to_16_9:
        w, h = _crop_to_16_9(local_path)
        final_size = f"{w}x{h}"

    credits_after = _credits_or_none()
    _log_event({
        "kind": "image_to_image",
        "label": label,
        "prompt": prompt,
        "reference": str(image_path),
        "strength": strength,
        "model": model,
        "final_size": final_size,
        "status": "completed",
        "url": image_url_result,
        "local_path": str(local_path),
        "credits_before": credits_before,
        "credits_after": credits_after,
    })
    print(f"Variante generada ({label}): {local_path} - creditos {credits_before} -> {credits_after}", flush=True)
    return GeneratedImage(url=image_url_result, local_path=local_path)


def create_style(reference_images: list[Path], base_style: str = "digital_illustration") -> str:
    """POST /styles - crea un estilo propio a partir de imagenes de
    referencia y devuelve su style_id, reutilizable en generate_image().

    Por que importa: es el mecanismo OFICIAL de consistencia visual de
    Recraft. Hoy la consistencia del personaje de Mindset Mechanics se
    sostiene copiando el mismo bloque de texto descriptivo en cada prompt,
    que es justo lo que produce derivas ("la oreja de la escena 8"). Un
    style_id fija la identidad del lado del modelo.

    LIMITACION documentada: los estilos creados por API solo son compatibles
    con Recraft V3 y V3 Vector - NO con V4.x. Usarlo implica decidir bajar a
    V3, que es una decision de direccion visual (Kimi/David), no tecnica.

    SIN PROBAR CONTRA LA API REAL - crear un estilo puede consumir creditos.
    No llamar sin autorizacion explicita.
    """
    files = []
    try:
        for i, ref in enumerate(reference_images):
            ref = Path(ref)
            if not ref.exists():
                raise RecraftError(f"No existe la imagen de referencia: {ref}")
            files.append((f"file{i + 1}", (ref.name, open(ref, "rb"))))
        _throttle()
        resp = requests.post(
            f"{BASE_URL}/styles",
            headers=_headers(),
            data={"style": base_style},
            files=files,
            timeout=(10, 180),
        )
    finally:
        for _, (_, fh) in files:
            fh.close()

    if resp.status_code not in (200, 201):
        _log_event({"kind": "style_error", "status": resp.status_code, "body": resp.text[:2000]})
        raise RecraftError(f"Recraft /styles error {resp.status_code}: {resp.text[:500]}")

    style_id = resp.json().get("id")
    _log_event({"kind": "style_created", "style_id": style_id, "base_style": base_style,
                "references": [str(p) for p in reference_images]})
    print(f"Estilo creado: {style_id}", flush=True)
    return style_id
