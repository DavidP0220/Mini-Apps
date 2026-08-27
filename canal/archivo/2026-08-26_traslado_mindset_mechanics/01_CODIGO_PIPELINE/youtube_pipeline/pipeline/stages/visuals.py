"""Etapa 4a: Miniatura (thumbnail).

Esta etapa SÍ funciona hoy sin ninguna API key: compone una miniatura
1280x720 con un fondo de degradado, texto grande y un acento de color,
siguiendo el patrón "simple gana" (poco texto, alto contraste, sin
animaciones ni saturación de elementos).

Si más adelante quieres miniaturas con imágenes generadas por IA en vez de
un fondo de degradado, esta es la función a extender (recibe una imagen de
fondo opcional con `background_image_path`).
"""
import os
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from ..models import VisualAsset

# Miniatura: 1280x720 es el tamaño correcto y recomendado por YouTube para
# thumbnails, no se toca.
THUMB_WIDTH, THUMB_HEIGHT = 1280, 720

# Imágenes de ESCENA: 1080p. Antes compartían el 1280x720 de la miniatura, lo
# que topaba el video final a 720p aunque la etapa de ensamblado renderizara
# más alto (regla dura del proyecto: mínimo 1080p siempre).
WIDTH = int(os.getenv("PIPELINE_WIDTH", "1920"))
HEIGHT = int(os.getenv("PIPELINE_HEIGHT", "1080"))

_FONT_CANDIDATES = [
    r"C:\Windows\Fonts\arialbd.ttf",
    r"C:\Windows\Fonts\segoeuib.ttf",
    r"C:\Windows\Fonts\calibrib.ttf",
]


def _load_font(size: int) -> ImageFont.FreeTypeFont:
    for path in _FONT_CANDIDATES:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default(size=size)


def _gradient_background(top_color: tuple, bottom_color: tuple, width: int, height: int) -> Image.Image:
    base = Image.new("RGB", (width, height), top_color)
    draw = ImageDraw.Draw(base)
    for y in range(height):
        t = y / height
        r = int(top_color[0] + (bottom_color[0] - top_color[0]) * t)
        g = int(top_color[1] + (bottom_color[1] - top_color[1]) * t)
        b = int(top_color[2] + (bottom_color[2] - top_color[2]) * t)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    return base


def _save_image(img: Image.Image, output_path: Path) -> None:
    """Guarda respetando el formato real del archivo.

    Antes se llamaba siempre `img.save(path, quality=95)`. Con un .png ese
    `quality` se ignora en silencio (PNG no tiene compresión con pérdida),
    así que la opción no hacía nada; y con .jpg sobre una imagen RGBA
    revienta. Se decide por extensión."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    if output_path.suffix.lower() in (".jpg", ".jpeg"):
        img.convert("RGB").save(output_path, quality=95, subsampling=0)
    else:
        img.save(output_path)


def make_thumbnail(
    title: str,
    output_path: Path,
    top_color: tuple = (15, 17, 26),
    bottom_color: tuple = (35, 20, 60),
    accent_color: tuple = (255, 199, 44),
) -> VisualAsset:
    w, h = THUMB_WIDTH, THUMB_HEIGHT
    img = _gradient_background(top_color, bottom_color, w, h)
    draw = ImageDraw.Draw(img)

    # Acento simple: una franja diagonal, nada de animaciones ni efectos costosos.
    draw.polygon([(w - 260, 0), (w, 0), (w, h), (w - 60, h)], fill=accent_color)

    font = _load_font(96)
    wrapped = textwrap.fill(title.upper(), width=14)
    text_bbox = draw.multiline_textbbox((0, 0), wrapped, font=font, spacing=10)
    x = 60
    # Se centra usando el bbox COMPLETO (incluye el offset superior del
    # tipo), no solo su alto: usar solo la altura dejaba el texto ligeramente
    # descentrado hacia abajo en fuentes con ascendente alto.
    y = (h - (text_bbox[3] + text_bbox[1])) // 2

    # Sombra simple para legibilidad, luego el texto blanco encima.
    draw.multiline_text((x + 4, y + 4), wrapped, font=font, fill=(0, 0, 0), spacing=10)
    draw.multiline_text((x, y), wrapped, font=font, fill=(255, 255, 255), spacing=10)

    _save_image(img, output_path)
    return VisualAsset(image_path=output_path, duration_seconds=0.0)


def make_scene_image(
    text: str,
    output_path: Path,
    top_color: tuple,
    bottom_color: tuple,
    duration_seconds: float = 4.0,
) -> VisualAsset:
    """Genera una imagen de escena simple (fondo + texto corto) para usar
    como placeholder animable en la etapa de ensamblado, mientras no haya
    generación de imágenes por IA conectada.
    """
    img = _gradient_background(top_color, bottom_color, WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)

    # Tamaño de fuente proporcional: 64px estaba calibrado para 720p y al
    # subir a 1080p se veía diminuto.
    font = _load_font(max(32, round(HEIGHT * 0.089)))
    wrapped = textwrap.fill(text, width=28)
    text_bbox = draw.multiline_textbbox((0, 0), wrapped, font=font, spacing=8, align="center")
    text_w = text_bbox[2] - text_bbox[0]
    text_h = text_bbox[3] - text_bbox[1]
    x = (WIDTH - text_w) // 2
    y = (HEIGHT - text_h) // 2

    draw.multiline_text(
        (x, y), wrapped, font=font, fill=(255, 255, 255), spacing=8, align="center"
    )

    _save_image(img, output_path)
    return VisualAsset(image_path=output_path, duration_seconds=duration_seconds)


def generate_ai_scene_image(
    scene_title: str,
    scene_text: str,
    niche: str,
    output_path: Path,
    duration_seconds: float = 4.0,
) -> VisualAsset:
    """Genera el fondo de una escena con IA (Gemini/Imagen) en vez del
    degradado simple, para usar como b-roll animado en el ensamblado
    (Ken Burns). El prompt se arma a partir del texto REAL que se narra en
    esa escena (no solo el título corto), para que la imagen ilustre
    específicamente lo que se está diciendo en ese momento del video.

    Requiere: GEMINI_API_KEY en el archivo .env
    Se crea en console.cloud.google.com/apis/credentials, vinculada a una
    cuenta de servicio con el rol "Usuario de Agent Platform".
    """
    # Se lee en el momento de usarla, NO al importar el módulo. Antes era una
    # constante de nivel de módulo: si load_dotenv() corría después del
    # import (orden habitual en Python), la clave quedaba en None para
    # siempre y el error decía "falta GEMINI_API_KEY" aunque sí estuviera
    # en el .env.
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Falta GEMINI_API_KEY en .env. Sin esta clave no se pueden generar "
            "b-rolls con IA."
        )

    from google import genai

    client = genai.Client(api_key=api_key)
    narration_excerpt = " ".join(scene_text.split())[:500]
    prompt = (
        f"Fotografía profesional editorial hiperrealista y muy detallada, estilo "
        f"documental cinematográfico (nivel serie documental de streaming), "
        f"iluminación dramática y cuidada, enfoque nítido, profundidad de campo, "
        f"colores apagados y elegantes, sin texto ni letras en la imagen. "
        f"La imagen debe ilustrar de forma concreta y específica lo que se narra "
        f"en este momento del video (objetos, personas, situaciones reales que "
        f"representen la idea) — evita una escena genérica de stock.\n\n"
        f"Escena: {scene_title}\n"
        f'Lo que se está narrando en este momento: "{narration_excerpt}"\n'
        f"Contexto general del video: {niche}."
    )
    response = client.models.generate_content(
        model="gemini-3-pro-image",
        contents=[prompt],
    )
    # `next()` sin default lanzaba StopIteration si el modelo devolvía solo
    # texto (pasa cuando el prompt se bloquea por filtros de seguridad):
    # una excepción sin ningún mensaje útil, imposible de diagnosticar.
    image_bytes = next(
        (part.inline_data.data
         for part in response.candidates[0].content.parts
         if part.inline_data),
        None,
    )
    if image_bytes is None:
        raise RuntimeError(
            f"Gemini no devolvió imagen para la escena '{scene_title}' "
            "(normalmente = el prompt se bloqueó por filtros de contenido). "
            "Reformula el texto de la escena o usa make_scene_image() como respaldo."
        )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    raw_path = output_path.with_suffix(".raw.png")
    raw_path.write_bytes(image_bytes)
    try:
        with Image.open(raw_path) as raw:
            img = _crop_to_aspect(raw.convert("RGB"), WIDTH, HEIGHT)
        _save_image(img, output_path)
    finally:
        # try/finally: si el recorte fallaba, el .raw.png quedaba huérfano en
        # el directorio de salida y se colaba en el siguiente ensamblado.
        raw_path.unlink(missing_ok=True)

    return VisualAsset(image_path=output_path, duration_seconds=duration_seconds)


def _crop_to_aspect(img: Image.Image, target_w: int, target_h: int) -> Image.Image:
    target_ratio = target_w / target_h
    w, h = img.size
    ratio = w / h
    if ratio > target_ratio:
        new_w = int(h * target_ratio)
        left = (w - new_w) // 2
        img = img.crop((left, 0, left + new_w, h))
    else:
        new_h = int(w / target_ratio)
        top = (h - new_h) // 2
        img = img.crop((0, top, w, top + new_h))
    return img.resize((target_w, target_h), Image.LANCZOS)
