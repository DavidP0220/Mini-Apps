# -*- coding: utf-8 -*-
"""Genera un paquete listo para copiar/pegar por cada video:
titulo, descripcion en ingles, tags, hashtags, comentario fijado,
prompts de imagen (Midjourney/Flux), afirmaciones y checklist de subida.
Cada bloque en ingles va precedido de una instruccion en espanol."""
import json, pathlib, textwrap

BASE = pathlib.Path(__file__).resolve().parent.parent
CAT = json.loads((BASE / "datos" / "catalogo.json").read_text(encoding="utf-8"))

BENEFICIO = {
 396: "release fear, guilt and the deep roots of scarcity",
 417: "clear stagnant energy and undo old money patterns",
 432: "align with the natural harmony of the earth and rest deeply",
 528: "activate transformation, miracles and heart-centered abundance",
 741: "cleanse your field and protect you from envy and negativity",
 777: "open divine luck, synchronicity and unexpected doors",
 888: "amplify the vibration of money, wealth and infinite flow",
 963: "connect you with divine wisdom and higher guidance",
 1111: "open the manifestation portal and seal your intention",
}

AFIRMACIONES = [
 "Money flows to me easily and constantly.",
 "I am a magnet for wealth and opportunity.",
 "Everything I need is already on its way to me.",
 "I receive with gratitude and I give with joy.",
 "My income grows while I rest.",
 "Doors open for me in the perfect timing.",
 "I am safe, supported and abundantly provided for.",
 "Prosperity is my natural state.",
 "I release every fear of not having enough.",
 "Divine abundance surrounds me right now.",
 "I deserve to live in comfort and freedom.",
 "New sources of income find me.",
]

# Etiquetas ordenadas por volumen de busqueda REAL (vidIQ, mercado US):
# meditation music 2.4M/mes - binaural beats 1.09M - 432 hz 586k - law of attraction 690k
# abundance frequency 93k (26k solo en US, la de mayor proporcion estadounidense)
TAGS_BASE = ["meditation music","binaural beats","law of attraction","abundance frequency",
 "money frequency","attract money","abundance meditation","wealth meditation","sleep music",
 "manifestation music","healing frequency","relaxing music","attract abundance","prosperity"]

def descripcion(canal, v):
    hz, hrs = v["hz"], v["horas"]
    return f"""{v['titulo_corto']} — {hz}Hz music to {BENEFICIO[hz]}.

Let this {hrs}-hour journey play while you sleep, work, meditate or pray. Every tone is tuned to {hz}Hz and layered with a soft ambient pad, so your mind can relax while your intention keeps working in the background.

HOW TO USE THIS TRACK
1. Find a quiet place and set one clear intention about your abundance.
2. Play at a low, comfortable volume — headphones recommended, not required.
3. Breathe slowly for the first 3 minutes and repeat the affirmations on screen.
4. Let it play for at least 30 minutes, or all night while you sleep.

WHAT IS {hz}Hz?
{hz}Hz is used in sound therapy to {BENEFICIO[hz]}. Combined with the energy of {canal['deidad']}, it becomes a daily ritual of receptivity and gratitude.

AFFIRMATIONS IN THIS VIDEO
{chr(10).join('• ' + a for a in AFIRMACIONES[:6])}

⚠️ Do not listen while driving or operating machinery.
This music is for relaxation and meditation. It is not a substitute for medical or psychological treatment.

🔔 Subscribe to {canal['nombre']} and turn on the bell to receive a new abundance frequency every 36 hours.

© {canal['nombre']}. Original music and visuals. All rights reserved.
"""

def comentario_fijado(canal, v):
    return (f"🙏 Write \"I RECEIVE\" below and let this {v['hz']}Hz frequency work while you rest. "
            f"Tell us what you are manifesting — {canal['deidad']} hears every intention. ✨")

def prompts(canal, v):
    e, pal = canal["estetica"], ", ".join(canal["paleta"])
    return [
        f"{v['escena']}, {e}, cinematic volumetric light, ultra detailed, 8k, serene spiritual atmosphere, color palette {pal} --ar 16:9 --style raw",
        f"wide establishing shot of {v['escena']}, {e}, god rays, soft mist, painterly, no text, no people faces --ar 16:9",
        f"close macro detail inspired by {v['escena']}, {e}, shallow depth of field, glowing particles --ar 16:9",
        f"symmetrical mandala composition based on {v['escena']}, {e}, sacred geometry, centered --ar 16:9",
        f"night version of {v['escena']}, {e}, moonlight, deep blues with gold accents --ar 16:9",
    ]

def miniatura(canal, v):
    return (f"thumbnail art: {v['escena']}, {canal['estetica']}, extreme high contrast, dramatic rim light, "
            f"large empty space on the left third for text overlay, no text in image --ar 16:9")

def paquete(canal, v):
    tags = TAGS_BASE + [f"{v['hz']}hz", f"{v['hz']} hz music", canal["deidad"].lower(),
                        f"{v['horas']} hour music", v["titulo_corto"].lower()]
    P = []
    A = P.append
    A(f"# {v['id']} — {v['titulo_corto']}\n")
    A(f"Canal: **{canal['nombre']}** ({canal['handle']}) · Bloque: {v['bloque']} · {v['hz']}Hz · {v['horas']} horas\n")
    A("---\n")
    A("## 1) TÍTULO — pégalo en YouTube Studio → campo *Título*\n```")
    A(v["titulo_yt"]); A("```\n")
    A("## 2) DESCRIPCIÓN — pégala en el campo *Descripción* (todo el bloque)\n```")
    A(descripcion(canal, v)); A("```\n")
    A("## 3) ETIQUETAS — Studio → *Mostrar más* → campo *Etiquetas* (pega separado por comas)\n```")
    A(", ".join(tags)); A("```\n")
    A("## 4) COMENTARIO FIJADO — publícalo y luego clic en los 3 puntos → *Fijar*\n```")
    A(comentario_fijado(canal, v)); A("```\n")
    A("## 5) PROMPTS DE IMÁGENES — genera 5 imágenes (Midjourney / Flux / Leonardo)\n")
    for i, p in enumerate(prompts(canal, v), 1):
        A(f"Imagen {i}:\n```\n{p}\n```")
    A("\n## 6) PROMPT DE MINIATURA\n```")
    A(miniatura(canal, v)); A("```")
    A(f"\nTexto que va ENCIMA de la miniatura (grande, dorado, 2 líneas máx): **{v['miniatura_texto']}**\n")
    A("## 7) AFIRMACIONES EN PANTALLA — aparecen cada 4 minutos sobre las imágenes\n```")
    A("\n".join(AFIRMACIONES)); A("```\n")
    A("## 8) CHECKLIST DE SUBIDA\n")
    A("- [ ] Audio renderizado (`scripts/03_audio.py`)")
    A("- [ ] 5 imágenes generadas y guardadas en `salida/" + v["id"] + "/img/`")
    A("- [ ] Video renderizado (`scripts/04_video.py`)")
    A("- [ ] Miniatura 1280x720 subida")
    A("- [ ] Título, descripción, etiquetas pegados")
    A("- [ ] Público: *No, no es para niños*")
    A("- [ ] Categoría: *Música* · Idioma: *Inglés*")
    A("- [ ] Programado (un video cada 36 h)")
    A("- [ ] Comentario fijado publicado")
    return "\n".join(P)

def main():
    n = 0
    for canal in CAT["canales"]:
        d = BASE / "salida" / canal["slug"]
        d.mkdir(parents=True, exist_ok=True)
        for v in canal["videos"]:
            (d / f"{v['id']}.md").write_text(paquete(canal, v), encoding="utf-8")
            n += 1
    print(f"OK -> {n} paquetes en salida/<canal>/")

if __name__ == "__main__":
    main()
