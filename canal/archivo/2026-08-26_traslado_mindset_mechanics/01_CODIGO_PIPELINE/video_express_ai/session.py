"""Sesión de navegador y bloqueo de concurrencia para VideoExpress.ai.

Dos problemas que este módulo resuelve de raíz:

1. **Procesos de Chromium zombis.** Cada comando de generate_video.py hacía
   `browser = p.chromium.launch(...)` ... `browser.close()` como última línea,
   SIN try/finally. Cualquier excepción a mitad del flujo (un selector que
   cambió, un timeout, Ctrl+C) saltaba el `close()` y dejaba un Chromium
   headless vivo consumiendo RAM. Repetido en 7 comandos idénticos. Aquí el
   cierre está garantizado por el context manager.

2. **Dos sesiones/agentes usando la misma cuenta a la vez.** Es el mismo tipo
   de choque que ya se documentó con las pestañas de Chrome compartidas, pero
   peor: `_poll_for_latest_video()` identifica el render nuevo mirando
   Media Library > My AI Videos, que es GLOBAL de la cuenta. Si dos procesos
   generan a la vez, cada uno puede descargar el clip del otro y ambos
   quedar registrados como correctos. El bloqueo de abajo hace imposible esa
   carrera: el segundo proceso falla en seco con un mensaje claro en vez de
   corromper el resultado en silencio.

Patrón de lock tomado de la práctica estándar para flotas de agentes
concurrentes (claim por creación exclusiva de archivo + PID + timestamp,
con caducidad para no quedarse bloqueado por un proceso muerto).
"""
import json
import os
import time
from contextlib import contextmanager
from pathlib import Path

_MODULE_DIR = Path(__file__).resolve().parent
LOCK_PATH = _MODULE_DIR / ".videoexpress.lock"

# Un lote largo (animar 12 escenas) puede pasar de una hora. Pasado este
# tiempo se asume que el proceso dueño murió sin limpiar y el lock caduca.
LOCK_STALE_SECONDS = 2 * 60 * 60


class SessionBusyError(RuntimeError):
    pass


def _pid_alive(pid: int) -> bool:
    if pid <= 0:
        return False
    try:
        os.kill(pid, 0)  # señal 0: no hace nada, solo comprueba existencia
    except OSError:
        return False
    except Exception:
        return True  # ante la duda, tratarlo como vivo (fail-safe)
    return True


def _claim(purpose: str) -> bool:
    """Crea el lock de forma ATÓMICA. Devuelve False si ya existía.

    O_CREAT|O_EXCL es una sola syscall que crea el archivo *o* falla si ya
    está: es imposible que dos procesos la ganen a la vez. Es lo que hace la
    diferencia con `Path.write_text()`, que primero trunca/crea y siempre
    tiene éxito (ver la nota de arriba sobre el bug que esto corrige).
    """
    payload = json.dumps({"pid": os.getpid(), "purpose": purpose, "started_at": time.time()})
    try:
        fd = os.open(LOCK_PATH, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o644)
    except FileExistsError:
        return False
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(payload)
    return True


def _read_lock() -> dict:
    try:
        return json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    except Exception:
        # Lock a medio escribir o corrupto: se trata como "de alguien vivo"
        # (started_at=0 lo haría caducar al instante, justo al revés de lo
        # que conviene ante la duda).
        return {"pid": 0, "purpose": "desconocida", "started_at": time.time()}


@contextmanager
def account_lock(purpose: str = "generacion"):
    """Impide que dos procesos operen la cuenta de VideoExpress a la vez."""
    if not _claim(purpose):
        info = _read_lock()
        age = time.time() - info.get("started_at", 0)
        owner_pid = int(info.get("pid", 0))
        if age < LOCK_STALE_SECONDS and _pid_alive(owner_pid):
            raise SessionBusyError(
                f"Otra sesión ya está usando la cuenta de VideoExpress "
                f"(pid={owner_pid}, tarea='{info.get('purpose')}', "
                f"desde hace {int(age)}s).\n"
                "Dos procesos a la vez se roban los renders entre sí (Media Library "
                "es global de la cuenta). Espera a que termine, o si estás seguro de "
                f"que ese proceso ya murió, borra {LOCK_PATH.name}."
            )
        print(f"[lock] lock huérfano encontrado (pid={owner_pid}, {int(age)}s) - se reclama", flush=True)
        LOCK_PATH.unlink(missing_ok=True)
        # El reclamo también es atómico: si dos procesos detectan el mismo
        # lock huérfano a la vez, solo uno consigue recrearlo y el otro se
        # va con el error de ocupado en vez de colarse.
        if not _claim(purpose):
            info = _read_lock()
            raise SessionBusyError(
                f"Otra sesión reclamó el lock huérfano primero "
                f"(pid={info.get('pid')}, tarea='{info.get('purpose')}'). Reintenta luego."
            )

    try:
        yield
    finally:
        LOCK_PATH.unlink(missing_ok=True)


@contextmanager
def browser_page(purpose: str = "generacion"):
    """Abre VideoExpress con la sesión guardada y garantiza el cierre.

    Uso:
        with browser_page("animar escena 3") as page:
            bot.open_create_video_from_prompt(page)
            ...
    """
    import sys

    from playwright.sync_api import sync_playwright

    from auth_manager import has_saved_session, load_session_kwargs
    import video_express_bot as bot

    if not has_saved_session():
        print("No hay sesión guardada. Corre primero: python setup_auth.py")
        sys.exit(1)

    headful = os.getenv("HEADFUL", "false").lower() == "true"
    with account_lock(purpose):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=not headful)
            try:
                context = browser.new_context(**load_session_kwargs())
                page = context.new_page()
                bot.open_editor(page)
                yield page
            finally:
                # Garantizado incluso si el bloque de arriba lanza: es lo que
                # faltaba y dejaba Chromium colgado en cada fallo.
                browser.close()
