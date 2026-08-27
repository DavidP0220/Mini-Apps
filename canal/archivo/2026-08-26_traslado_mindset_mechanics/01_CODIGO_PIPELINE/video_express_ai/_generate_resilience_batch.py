"""Genera las escenas 2-12 de Resiliencia en una sola sesión de navegador,
reutilizando el prefijo/sufijo de personaje ya corregido (sin nariz, sin
blush) validado en la escena 1. Ver RESILIENCE_SCENE_PLAN.md."""
import sys
from pathlib import Path

# La carpeta de este propio script - antes clavada a la ruta de una maquina.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from playwright.sync_api import sync_playwright
from auth_manager import load_session_kwargs
import video_express_bot as bot

# v4 (2026-08-23): reescrita desde observacion directa de frames reales de
# los 4 videos ya publicados, no desde la descripcion escrita original (que
# estaba equivocada - ver ESTILO_MINDSET_MECHANICS.md addendum "CORRECCION
# MAYOR"). Diferencia clave: el canal real tiene contorno negro grueso y
# cel-shading plano, NO el sombreado pictorico atmosferico que se uso antes.
CHAR_PREFIX = (
    "Flat 2D vector cartoon illustration, cel-shaded animation style with bold thick "
    "clean black outlines around the character and every object in the scene, like a "
    "modern animated web series. {plano} of a young man with deliberately simplified "
    "cartoon proportions: a large round smooth bald head with absolutely no hair and no "
    "ears visible at all, a dark navy blue baseball cap sitting directly on the smooth "
    "head. His face is extremely minimal and flat: two simple solid black oval eyes with "
    "no iris detail and no highlight, two thick short dark eyebrows, absolutely no nose "
    "of any kind — completely flat and smooth between the eyes and mouth, no nose shape, "
    "no nostrils — and a small simple black line mouth. Flat solid cream skin tone with "
    "minimal flat shading, no gradients, no blush, no pink cheeks, no rosy tint anywhere "
    "on the face. Simple flat-colored grey hoodie, dark jeans, sneakers."
)

LIGHT_SUFFIX = (
    "Flat cel-shaded coloring throughout, bold clean black outlines on every shape, "
    "moderate warm lighting rendered as flat color blocks rather than soft gradients, "
    "simple flat background with clear detail, graphic-novel / flat-vector illustration "
    "quality, crisp and clean linework."
)

NEGATIVE = (
    "Absolutely NO soft painterly shading, NO atmospheric glow, NO volumetric light "
    "shafts, NO floating dust particles, NO photorealism, NO anime face, NO detailed "
    "irises, NO visible hair, NO visible ears, NO blush, NO pink cheeks, NO rosy cheeks, "
    "NO flushed skin, NO sharp jawline, NO nose, NO nostrils, NO nose bridge, NO nose "
    "shadow, NO nose shape of any kind, NO halftone dots, NO ben-day dots, NO starburst "
    "or speed lines, NO comic panels, NO white gutters, NO speech bubbles, and NO text, "
    "letters, signs or words anywhere in the image."
)

# (numero, plano, escena, motion)
SCENES = [
    (2, "Extreme close-up",
     "extreme close-up on his eye, a faint reflection of the blurred conference room visible in the pupil, sweat beading at his temple.",
     "Static for a beat, then slow tilt down from his eye to his trembling hand still holding the notes, subtle handheld tremor, anxious and claustrophobic."),
    (3, "Low-angle shot",
     "he stands frozen at an office doorway at night, the doorway's shadow subtly elongating into the silhouette of a cave mouth, faint glowing eyes of an unseen predator barely visible in the darkness beyond.",
     "Camera slowly cranes upward from a low angle, making the shadowed doorway loom larger, dust particles drifting through a shaft of cold light, dramatic and unsettling."),
    (4, "Overhead shot",
     "overhead view of his cluttered desk at night: a phone buzzing with notifications, stacks of paper piling up, a cold cup of coffee, the window behind showing a city skyline going dark.",
     "Slow zoom in on the buzzing phone, then gentle pan across the cluttered desk, cold blue city light flickering through the window, tense and exhausted mood."),
    (5, "Wide shot",
     "he sits slumped alone in a dim, sparse room, a door slightly ajar on the far wall with warm light spilling through the gap, but he isn't looking toward it.",
     "Static wide shot held for a long beat, only the light through the door gently flickering, quiet and heavy stillness."),
    (6, "Medium shot from behind",
     "he rises from the chair and walks steadily toward the half-open door, warm golden light growing brighter across the floor as he approaches it.",
     "Tracking shot behind him as he walks toward the light, camera slowly rising with him, hopeful and building, warm rim light increasing."),
    (7, "Medium close-up, direct address",
     "he stands in a plain softly-lit space, turned to look directly forward, calm and open expression, as if about to ask the viewer something.",
     "Still camera. He looks directly toward the camera as if speaking to the viewer, a faint, thoughtful pause before a small nod, quiet and direct."),
    (8, "Close-up, side profile",
     "close side-profile of him standing by a window at dawn, eyes closed, taking a deep breath, chest visibly rising, soft blue morning light.",
     "Slow dolly in on his profile as he exhales slowly, his shoulders visibly relaxing, calm and deliberate, his breath faintly visible in the cool morning light."),
    (9, "Close-up over the shoulder",
     "close-up over his shoulder as he stands at a bathroom sink, splashing cold water on his face, water droplets catching the light, soft blue morning light through a window above the sink.",
     "Slow dolly in toward his reflection rippling in the water droplets on the sink's surface, steam of his breath faintly visible, calm and reset."),
    (10, "Medium shot",
     "he sits at the same conference table as the opening scene, but now composed, taking one slow breath before speaking, a faint, steady focus in his eyes.",
     "Slow push-in mirroring the very first scene's camera move exactly, but steadier and calmer this time, quiet confidence."),
    (11, "Medium shot, low-stakes presentation",
     "he stands at the front of a small meeting room, gesturing calmly while speaking to three colleagues seated around a table, a simple whiteboard behind him, relaxed and steady posture.",
     "Smooth slow orbit around him as he speaks, colleagues nodding attentively, warm confident lighting, steady and assured."),
    (12, "Wide shot, low angle",
     "wide shot of him walking out of an office building entrance into full daylight, shoulders relaxed, the city open and bright ahead of him.",
     "Camera slowly pulls back and cranes upward, revealing the wide bright street as he walks confidently into it, uplifting and open."),
]


def build_prompt(plano: str, scene: str) -> str:
    return f"{CHAR_PREFIX.format(plano=plano)}\n\nScene: {scene}\n\n{LIGHT_SUFFIX}\n\n{NEGATIVE}"


def main():
    only = sys.argv[1:] and [int(x) for x in sys.argv[1:]] or None
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(**load_session_kwargs())
        page = context.new_page()
        bot.open_editor(page)

        for num, plano, scene, motion in SCENES:
            if only and num not in only:
                continue
            print(f"\n=== Escena {num} ===", flush=True)
            image_prompt = build_prompt(plano, scene)
            out_name = f"resilience_scene_{num:02d}.mp4"
            try:
                bot.open_create_video_from_prompt(page, landscape=True)
                asset = bot.create_silent_video(
                    page, image_prompt=image_prompt, video_prompt=motion,
                    image_type="2D", filename=out_name,
                )
                print(f"OK escena {num}: {asset.local_path}", flush=True)
            except Exception as e:
                print(f"FALLO escena {num}: {e}", flush=True)

        browser.close()


if __name__ == "__main__":
    main()
