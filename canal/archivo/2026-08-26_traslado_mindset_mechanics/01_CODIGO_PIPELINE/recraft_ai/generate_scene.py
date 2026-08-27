"""CLI para generar stills de escena via la API real de Recraft AI.

Ejemplo:
    python generate_scene.py "Same character, same exact flat 2D..." \
        --label resilience_scene_03

Por defecto: modelo recraftv4_1 a 1344x768 con recorte automatico a
1344x756 = 16:9 EXACTO (unica proporcion que VideoExpress acepta animar).
Ver recraft_client.generate_image para el detalle de por que.

Comprobar el saldo antes de un lote:
    python generate_scene.py --credits
"""
import argparse
import sys
from pathlib import Path

from dotenv import load_dotenv

# Ruta explicita: load_dotenv() a secas busca el .env desde el directorio de
# trabajo hacia arriba, asi que lanzar el CLI desde la raiz del repo no
# encontraba recraft_ai/.env y fallaba con un "RECRAFT_API_KEY no esta
# configurada" enganoso (la clave si existia).
load_dotenv(Path(__file__).resolve().parent / ".env")

# El modulo vive junto a este archivo; sin esto, "python recraft_ai/generate_
# scene.py" desde la raiz del repo fallaba con ModuleNotFoundError segun como
# lo invocara el shell.
sys.path.insert(0, str(Path(__file__).resolve().parent))

import recraft_client as rc


def main():
    parser = argparse.ArgumentParser(description="Genera un still de escena con la API de Recraft")
    parser.add_argument("prompt", nargs="?", help="Prompt completo (personaje + escena + negativos)")
    parser.add_argument("--label", help="Nombre corto para el archivo y el log, ej: resilience_scene_03")
    parser.add_argument("--size", default=rc.SIZE_16_9_V4_SOURCE,
                        help=f"WxH. Default {rc.SIZE_16_9_V4_SOURCE} (+ recorte a 16:9 exacto). "
                             f"Con --model recraftv3 usar {rc.SIZE_16_9_V3}.")
    parser.add_argument("--model", default="recraftv4_1")
    parser.add_argument("--style", default=None)
    parser.add_argument("--style-id", default=None, help="ID de estilo propio creado con POST /styles (solo V3)")
    parser.add_argument("--negative-prompt", default=None, help="Solo soportado por recraftv2/recraftv3")
    parser.add_argument("--no-crop", action="store_true",
                        help="No recortar a 16:9 exacto (la imagen NO servira para animar en VideoExpress)")
    parser.add_argument("--credits", action="store_true", help="Solo consultar el saldo y salir (no gasta nada)")
    args = parser.parse_args()

    # Consulta de saldo: util como paso previo de cualquier lote, y no gasta
    # creditos. Va antes de validar prompt/label a proposito.
    if args.credits:
        print(rc.get_credits())
        return

    if not args.prompt or not args.label:
        parser.error("se requieren 'prompt' y --label (o usa --credits)")

    asset = rc.generate_image(
        prompt=args.prompt,
        size=args.size,
        model=args.model,
        style=args.style,
        style_id=args.style_id,
        negative_prompt=args.negative_prompt,
        filename=f"{args.label}.png",
        label=args.label,
        crop_to_16_9=not args.no_crop,
    )
    print(f"Listo: {asset.local_path}")


if __name__ == "__main__":
    try:
        main()
    except rc.RecraftError as exc:
        # Un traceback de 30 lineas por un tamano invalido no ayuda a nadie:
        # el mensaje de RecraftError ya explica que hacer.
        print(f"\nERROR: {exc}\n", file=sys.stderr)
        sys.exit(1)
