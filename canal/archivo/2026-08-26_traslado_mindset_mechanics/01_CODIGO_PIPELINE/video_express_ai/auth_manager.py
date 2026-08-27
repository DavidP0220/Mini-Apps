"""Gestor de sesión persistente para VideoExpress.ai.

Guarda/carga el `storage_state` de Playwright (cookies + localStorage) en
auth_state.json, para no tener que iniciar sesión en cada ejecución.
"""
from pathlib import Path

AUTH_STATE_PATH = Path(__file__).parent / "auth_state.json"


def has_saved_session() -> bool:
    return AUTH_STATE_PATH.exists()


def save_session(context) -> None:
    context.storage_state(path=str(AUTH_STATE_PATH))
    print(f"Sesión guardada en {AUTH_STATE_PATH}")


def load_session_kwargs() -> dict:
    """Devuelve los kwargs para pasarle a browser.new_context() si hay
    una sesión guardada; dict vacío si no hay ninguna (login limpio)."""
    if has_saved_session():
        return {"storage_state": str(AUTH_STATE_PATH)}
    return {}
