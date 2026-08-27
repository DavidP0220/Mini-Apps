"""Genera clips de video animados vía Replicate (Kling/Luma/Minimax) a partir
de un prompt de texto, opcionalmente animando una imagen de referencia
(image-to-video) para mantener consistencia de personaje entre escenas.

Requiere: pip install replicate  (ya instalado)
           REPLICATE_API_TOKEN en el entorno o en .env (ver instrucciones abajo)

Uso:
  python generar_animacion.py "descripcion del video"
  python generar_animacion.py "descripcion del video" --image ruta/o/url/imagen.jpg
  python generar_animacion.py "descripcion del video" --output clip.mp4 --duration 5
"""
import argparse
import os
import sys
import urllib.request
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

import replicate

MODEL = "kwaivgi/kling-v1.6-standard"


def generar_video(
    prompt: str,
    output_path: str = "animacion.mp4",
    duration: int = 5,
    aspect_ratio: str = "16:9",
    image_path: str | None = None,
) -> Path:
    if not os.getenv("REPLICATE_API_TOKEN"):
        raise RuntimeError(
            "Falta REPLICATE_API_TOKEN. Crea una cuenta en https://replicate.com, "
            "genera un token en https://replicate.com/account/api-tokens, y agrégalo "
            "al archivo .env como REPLICATE_API_TOKEN=r8_..."
        )

    print(f"Generando animacion para: '{prompt}'...")

    input_payload = {
        "prompt": prompt,
        "duration": duration,
        "aspect_ratio": aspect_ratio,
    }
    if image_path:
        # Kling soporta image-to-video: si se pasa una imagen local, la sube;
        # si es una URL, la usa directo. Esto es lo que permite mantener el
        # mismo personaje del canal (ej. el host de Mindset Mechanics) entre
        # distintos clips generados, en vez de texto-a-video puro.
        if image_path.startswith("http"):
            input_payload["start_image"] = image_path
        else:
            input_payload["start_image"] = open(image_path, "rb")

    output = replicate.run(MODEL, input=input_payload)

    # replicate.run devuelve un FileOutput (o lista) según el modelo; normalizamos
    url = output.url if hasattr(output, "url") else (output[0] if isinstance(output, list) else output)

    out_path = Path(output_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(str(url), out_path)

    print(f"Video generado y descargado: {out_path}")
    return out_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Genera un clip de video animado vía Replicate")
    parser.add_argument("prompt", help="Descripcion del video a generar")
    parser.add_argument("--output", default="animacion.mp4", help="Ruta del archivo de salida")
    parser.add_argument("--duration", type=int, default=5, help="Duracion en segundos")
    parser.add_argument("--aspect-ratio", default="16:9", help="Relacion de aspecto")
    parser.add_argument("--image", default=None, help="Ruta o URL de imagen de referencia (image-to-video)")
    args = parser.parse_args()

    generar_video(
        args.prompt,
        output_path=args.output,
        duration=args.duration,
        aspect_ratio=args.aspect_ratio,
        image_path=args.image,
    )
