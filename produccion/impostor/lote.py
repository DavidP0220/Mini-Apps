# -*- coding: utf-8 -*-
"""Generador de hojas de lote para Artistly — Mindset Mechanics.

Convierte una tabla de planos en prompts listos para copiar y pegar,
con la ficha del personaje y el sufijo de estilo ya incrustados,
en positivo puro y con auditoria de negaciones.

Uso:  python3 lote.py            -> escribe LOTE_LISTO.txt
"""
import re, sys

# ---------------- bloques fijos (verbatim del lote aprobado) ----------------

APERTURA = ("Flat 2D vector cartoon illustration in a cel-shaded animation style, drawn with bold thick "
 "clean black outlines around the character and around every object in the scene, like a modern "
 "animated web series. ")

FICHA = (
 "a young man drawn with deliberately simplified cartoon proportions. His head is a large, "
 "perfectly round, completely smooth bare scalp, and a dark navy blue baseball cap rests directly "
 "on that bare scalp. The sides of his head are smooth and unbroken curves from cap to jaw. "
 "His face is minimal and flat: two solid black oval eyes, two thick short dark eyebrows, a small "
 "black line for a mouth, and between the eyes and the mouth the face is one continuous smooth "
 "unbroken plane of flat cream skin. The skin is a single even cream tone across the whole face. "
 "He wears a plain grey hoodie, dark jeans and sneakers.")

SILUETA = ("The head is drawn as one single unbroken oval outline, one continuous closed silhouette. ")

CIERRE = ("Every surface is filled with flat solid blocks of colour and hard-edged cel shading. All "
 "outlines are thick, black and clean. Lighting is rendered as flat blocks of tone with hard edges. "
 "The background is simple, flat and graphic. Crisp clean vector linework throughout, "
 "graphic-novel / flat-vector illustration quality. The image is entirely wordless.")

CERRADOS = ("Close-up", "Medium close-up", "Extreme close-up")

# ---------------- tabla de planos ----------------
# (id, tamano de plano, escena en ingles positivo, lleva host)

PLANOS = [
("SH001","Wide shot",
 "standing alone in the exact centre of a wide empty stage, one hard-edged circle of white light "
 "around his feet, the rest of the frame deep flat black, his arms straight down at his sides",True),

("SH002","Medium shot",
 "seen from behind, shoulders raised toward his cap, facing a dark auditorium filled with long rows "
 "of pale cream head shapes, each head carrying two small flat black oval marks, every row turned "
 "toward him",True),

("SH003","Close-up",
 "gripping the front edge of a plain wooden podium with both hands, his fingers pressed flat and "
 "pale against the dark wood, the rest of the frame in flat shadow",True),

("SH004","Medium close-up",
 "with the grey hood pulled up and forward over the navy cap, the flat cream face resting deep "
 "inside the dark opening of the hood, held very still",True),

("SH005","Wide shot",
 "an empty stage with one hard circle of white light on the floor, and a single grey hoodie lying "
 "flat and abandoned inside that circle, deep flat black all around it",False),

("SH006","Wide shot",
 "an open savannah at dusk under a deep orange and purple flat sky, one small round pool of flat "
 "orange firelight on the ground, eight simplified seated human shapes arranged evenly around the "
 "fire, all of them the same size and the same grey tone",False),

("SH007","Medium shot",
 "one of the seated shapes around that fire now standing upright, taller than every other shape and "
 "lit brighter orange by the flames, alone above the ring",False),

("SH008","Medium shot",
 "the seated shapes around the fire all rotated toward the standing figure, every head aligned on "
 "the same point, the standing figure small and bright at the centre of their attention",False),

("SH009","Close-up",
 "tall dark grass at ground level in the blue night beyond the fire, and low inside that grass two "
 "small flat black oval shapes, each one 100% solid black from edge to edge like a paper cut-out, "
 "the orange firelight glowing far behind them",False),

("SH010","Wide shot",
 "the same fire circle with every figure seated again at the same height, the ring even and closed, "
 "the flat orange light spread equally across all of them",False),

("SH011","Medium shot",
 "standing beside a long conference table in a flat modern office, six simplified seated colleagues "
 "around the table, his right hand lifted halfway toward the ceiling and stopped there",True),

("SH012","Close-up",
 "lowering his raised hand back down onto the pale surface of the conference table, his fingers "
 "spread flat and still",True),

("SH013","Medium close-up",
 "sitting in a dim room in front of an open laptop, the screen throwing one flat block of cold blue "
 "light across his cap and hoodie, one bright blue rectangular button glowing on that screen",True),

("SH014","Close-up",
 "an open laptop screen in a dim room, its surface entirely dark and empty, one uniform black "
 "rectangle, the room around it flat and grey",False),

("SH015","Wide shot",
 "walking down a long grey corridor pressed close against the left wall, his shoulder brushing the "
 "surface, the corridor stretching far away to a small pale rectangle of light",True),

("SH016","Medium shot",
 "stepping sideways around a bright hard-edged pool of light on the corridor floor, both feet "
 "staying inside the grey shadow beside it",True),

("SH017","Wide shot",
 "a crowded city street seen from above, filled with dozens of identical simplified grey human "
 "shapes all walking the same direction, evenly spaced and interchangeable",False),

("SH018","Medium shot",
 "the same grey crowd with one single figure in bright red standing still among them, and every "
 "surrounding grey head turned toward that red figure",False),

("SH019","Close-up",
 "framed so that his face fills the frame, flat and unreadable, one hard-edged diagonal shadow "
 "cutting across it so that one half is bright cream and the other half is deep grey",True),

("SH020","Wide shot",
 "alone again on the wide empty stage inside the hard circle of white light, taking one single step "
 "forward so that the toe of one sneaker crosses the bright edge of the circle into the black",True),
]

# ---------------- construccion ----------------

PROHIBIDAS = ["nose","ears","hair","blush","nostril","painterly",
              r"\bno\b","without","never","avoid","remove","empty of"]

def construir(tam, escena, host):
    partes = [APERTURA]
    if host:
        partes.append(f"{tam} of {FICHA} He is {escena}. ")
    else:
        partes.append(f"{tam} of {escena}. ")
    if tam in CERRADOS and host:
        partes.append(SILUETA)
    partes.append(CIERRE)
    return "".join(partes)

ARRANQUES = ("with ", "seen ", "standing", "framed ", "alone ", "half ")

def gramatica(escena, host):
    """Con host el prompt dice 'He is <escena>', asi que la escena debe empezar
    en gerundio (-ing) o por un arranque valido."""
    if not host:
        return True
    primera = escena.split()[0]
    return primera.endswith("ing") or escena.startswith(ARRANQUES)

def auditar(p):
    mal = []
    for w in PROHIBIDAS:
        pat = w if w.startswith("\\") else r"\b" + re.escape(w)
        if re.search(pat, p, re.I):
            mal.append(w.strip("\\b"))
    return mal

lineas = []
lineas.append("HOJA DE LOTE — 20 imagenes · Impostor / DONT BE SEEN")
lineas.append("=" * 72)
lineas.append("")
lineas.append("ANTES DE CADA UNA (5 clics, sin saltarse ninguno):")
lineas.append("  1. Consistent Characters -> 3d & 2d Style Images")
lineas.append("  2. RESELECCIONAR HOST_CORRECTO.png como referencia")
lineas.append("  3. Poner 16:9")
lineas.append("  4. Pegar el prompt completo")
lineas.append("  5. Generar. UNA sola. Luego volver al paso 2.")
lineas.append("")
lineas.append("=" * 72)

fallos = 0
for i, (sid, tam, esc, host) in enumerate(PLANOS, 1):
    p = construir(tam, esc, host)
    if not gramatica(esc, host):
        fallos += 1
        print(f"  !! {sid} redaccion invalida: 'He is {esc[:45]}...'", file=sys.stderr)
    mal = auditar(p)
    if mal:
        fallos += 1
        print(f"  !! {sid} contiene {mal}", file=sys.stderr)
    marca = "HOST" if host else "SIN HOST"
    lineas.append("")
    lineas.append(f"--- {i:02d} · {sid} · {tam} · {marca} " + "-" * 20)
    lineas.append("")
    lineas.append(p)
    lineas.append("")

open("LOTE_LISTO.txt", "w", encoding="utf-8").write("\n".join(lineas))

print(f"{len(PLANOS)} prompts escritos en LOTE_LISTO.txt")
print(f"con host: {sum(1 for x in PLANOS if x[3])}   sin host: {sum(1 for x in PLANOS if not x[3])}")
print("auditoria de negaciones:", "LIMPIA" if fallos == 0 else f"{fallos} FALLOS")
