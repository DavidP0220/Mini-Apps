"""CLI para generar imágenes/videos en VideoExpress.ai vía Playwright.

Requiere haber corrido `python setup_auth.py` al menos una vez (guarda la
sesión en auth_state.json).

Ejemplos:
  # Solo imagen (b-roll estático, estilo cómic)
  python generate_video.py image "Flat 2D comic panel of..." --type 2D --out panel1.jpg

  # Imagen + marcarla como personaje consistente
  python generate_video.py image "..." --type 2D --consistent-character

  # Clip con lipsync (requiere personaje consistente ya marcado en la sesión)
  python generate_video.py lipsync \
      --video-prompt "Actor 1 is a bald man in a black cap and grey hoodie, talking to camera" \
      --script "It's your ancient survival wiring misfiring in a modern world." \
      --out clip1.mp4
"""
import argparse
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

from playwright.sync_api import sync_playwright

from auth_manager import has_saved_session, load_session_kwargs
import video_express_bot as bot


def _require_session():
    if not has_saved_session():
        print("No hay sesión guardada. Corre primero: python setup_auth.py")
        sys.exit(1)


def cmd_image(args):
    _require_session()
    headful = os.getenv("HEADFUL", "false").lower() == "true"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not headful)
        context = browser.new_context(**load_session_kwargs())
        page = context.new_page()
        bot.open_editor(page)
        bot.open_create_video_from_prompt(page, landscape=not args.vertical)
        asset = bot.create_image(page, args.prompt, image_type=args.type, filename=args.out)
        if args.consistent_character:
            bot.mark_consistent_character(page)
        browser.close()
    print(f"Listo: {asset.local_path}")


def cmd_stylize(args):
    _require_session()
    headful = os.getenv("HEADFUL", "false").lower() == "true"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not headful)
        context = browser.new_context(**load_session_kwargs())
        page = context.new_page()
        bot.open_editor(page)
        asset = bot.stylize_character(page, style=args.style, filename=args.out)
        browser.close()
    print(f"Listo: {asset.local_path}")


def cmd_lipsync(args):
    _require_session()
    headful = os.getenv("HEADFUL", "false").lower() == "true"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not headful)
        context = browser.new_context(**load_session_kwargs())
        page = context.new_page()
        bot.open_editor(page)
        bot.open_create_video_from_prompt(page, landscape=not args.vertical)
        asset = bot.create_lipsync_video(page, args.video_prompt, args.script, filename=args.out)
        browser.close()
    print(f"Listo: {asset.local_path}")


def cmd_scene(args):
    """Escena animada sin diálogo: imagen + movimiento real de cámara.

    Es la vía correcta para el b-roll de Mindset Mechanics — da dolly/paneo
    de verdad en vez del Ken Burns simulado del pipeline viejo, y no tiene el
    límite de 100 caracteres del lipsync.
    """
    _require_session()
    headful = os.getenv("HEADFUL", "false").lower() == "true"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not headful)
        context = browser.new_context(**load_session_kwargs())
        page = context.new_page()
        bot.open_editor(page)
        bot.open_create_video_from_prompt(page, landscape=not args.vertical)
        asset = bot.create_silent_video(
            page,
            image_prompt=args.image_prompt,
            video_prompt=args.motion,
            image_type=args.type,
            filename=args.out,
        )
        browser.close()
    print(f"Listo: {asset.local_path}")


def cmd_import_image(args):
    _require_session()
    headful = os.getenv("HEADFUL", "false").lower() == "true"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not headful)
        context = browser.new_context(**load_session_kwargs())
        page = context.new_page()
        bot.open_editor(page)
        bot.import_local_image(page, Path(args.path))
        browser.close()
    print(f"Subido a My AI Images: {args.path}")


def cmd_mark_character(args):
    """Marca como 'Consistent Character' una imagen ya subida a la carpeta
    'Images' (vía import-image) en vez de la última generada en la app.
    Cierra el ciclo: import-image sube REFERENCIA_personaje.png -> mark-character
    la fija como referencia -> las siguientes escenas heredan la identidad."""
    _require_session()
    headful = os.getenv("HEADFUL", "false").lower() == "true"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not headful)
        context = browser.new_context(**load_session_kwargs())
        page = context.new_page()
        bot.open_editor(page)
        bot.open_create_video_from_prompt(page, landscape=True)
        bot.mark_consistent_character(page, folder=args.folder)
        browser.close()
    print(f"Marcada como Consistent Character (carpeta: {args.folder})")


def main():
    parser = argparse.ArgumentParser(description="Generador de video/imagen para VideoExpress.ai")
    sub = parser.add_subparsers(dest="command", required=True)

    p_scene = sub.add_parser("scene", help="Escena animada sin dialogo (imagen + movimiento de camara)")
    p_scene.add_argument("--image-prompt", required=True, help="Descripcion de la imagen (usar plantilla de ESTILO_MINDSET_MECHANICS.md)")
    p_scene.add_argument("--motion", required=True, help="Direccion de camara/movimiento, ej: 'slow dolly in toward his face'")
    p_scene.add_argument("--type", default="2D", choices=["Human", "2D", "3D", "Photorealistic (Cinematic)", "Other"])
    p_scene.add_argument("--out", default=None, help="Nombre de archivo de salida")
    p_scene.add_argument("--vertical", action="store_true", help="9:16 en vez de 16:9")

    p_image = sub.add_parser("image", help="Genera una imagen (b-roll estático)")
    p_image.add_argument("prompt", help="Descripcion de la imagen")
    p_image.add_argument("--type", default="2D", choices=["Human", "2D", "3D", "Photorealistic (Cinematic)", "Other"])
    p_image.add_argument("--out", default=None, help="Nombre de archivo de salida")
    p_image.add_argument("--vertical", action="store_true", help="9:16 en vez de 16:9")
    p_image.add_argument("--consistent-character", action="store_true", help="Marcar como personaje reutilizable")

    p_style = sub.add_parser("stylize", help="Reestiliza la última imagen en My AI Images con un preset")
    p_style.add_argument(
        "--style", default="Comic Book",
        choices=["Realistic", "3D Pixar", "Anime", "Comic Book", "Line Art", "Watercolor"],
    )
    p_style.add_argument("--out", default=None, help="Nombre de archivo de salida")

    p_lip = sub.add_parser("lipsync", help="Genera un clip con personaje hablando (lipsync)")
    p_lip.add_argument("--video-prompt", required=True, help="Descripcion visual/de movimiento de la escena")
    p_lip.add_argument("--script", required=True, help="Linea hablada, maximo 100 caracteres")
    p_lip.add_argument("--out", default=None, help="Nombre de archivo de salida")
    p_lip.add_argument("--vertical", action="store_true", help="9:16 en vez de 16:9")

    p_import_img = sub.add_parser("import-image", help="Sube una imagen local a Media Library (carpeta Images)")
    p_import_img.add_argument("path", help="Ruta al archivo de imagen local")

    p_mark_char = sub.add_parser("mark-character", help="Marca una imagen ya subida como Consistent Character")
    p_mark_char.add_argument("--folder", default="Images", help="Carpeta del picker: 'Images' (subida a mano) o 'My AI Images' (generada en la app)")

    args = parser.parse_args()
    {
        "image": cmd_image,
        "stylize": cmd_stylize,
        "lipsync": cmd_lipsync,
        "scene": cmd_scene,
        "import-image": cmd_import_image,
        "mark-character": cmd_mark_character,
    }[args.command](args)


if __name__ == "__main__":
    main()
