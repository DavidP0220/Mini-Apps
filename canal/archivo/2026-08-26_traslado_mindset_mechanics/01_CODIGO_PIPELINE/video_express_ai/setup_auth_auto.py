"""Variante de setup_auth.py que NO espera un Enter en terminal - detecta
sola cuando el login termino (aparece el editor con 'Create with AI') y
guarda la sesion automaticamente. Pensada para lanzarse en background sin
que nadie tenga que volver a la terminal.

Uso:
  python setup_auth_auto.py
"""
from playwright.sync_api import sync_playwright

from auth_manager import save_session

LOGIN_URL = "https://app.videoexpress.ai/"
LOGIN_TIMEOUT_MS = 15 * 60 * 1000  # 15 min para loguearse con calma (2FA incluido)


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(LOGIN_URL)
        page.bring_to_front()

        print("\n" + "=" * 70)
        print("Se abrio una ventana de Chromium. Inicia sesion manualmente")
        print("(email + contraseña, cualquier 2FA). No hace falta volver aqui:")
        print("en cuanto se detecte el editor, la sesion se guarda sola.")
        print("=" * 70 + "\n")

        page.get_by_text("Create with AI").first.wait_for(timeout=LOGIN_TIMEOUT_MS)

        save_session(context)
        browser.close()

    print("Listo. Sesion guardada - ya se puede generar/animar sin volver a loguear.")


if __name__ == "__main__":
    main()
