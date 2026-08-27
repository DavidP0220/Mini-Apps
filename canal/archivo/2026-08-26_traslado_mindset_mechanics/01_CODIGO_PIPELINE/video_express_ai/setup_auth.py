"""Script interactivo de inicio de sesión (corre UNA sola vez, o cuando la
sesión guardada expire).

Abre una ventana de Chromium VISIBLE en videoexpress.ai y espera a que TÚ
inicies sesión manualmente (email + contraseña, cualquier 2FA, etc.) — el
bot nunca escribe tu contraseña por ti. Una vez que detecta que ya estás
adentro (llegaste al editor), guarda la sesión en auth_state.json para que
generate_video.py pueda reusarla sin pedirte login cada vez.

Uso:
  python setup_auth.py
"""
from playwright.sync_api import sync_playwright

from auth_manager import save_session

LOGIN_URL = "https://app.videoexpress.ai/"


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(LOGIN_URL)

        print("\n" + "=" * 70)
        print("Se abrió una ventana de Chromium.")
        print("Inicia sesión manualmente en VideoExpress.ai (email + contraseña).")
        print("Cuando veas el editor (la pantalla con 'Create with AI' a la")
        print("derecha), vuelve aquí y presiona Enter para guardar la sesión.")
        print("=" * 70 + "\n")
        input("Presiona Enter cuando hayas iniciado sesión... ")

        save_session(context)
        browser.close()

    print("Listo. Ya puedes usar generate_video.py sin volver a iniciar sesión")
    print("(hasta que la sesión expire, en cuyo caso vuelve a correr este script).")


if __name__ == "__main__":
    main()
