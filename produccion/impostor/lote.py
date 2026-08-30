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

from escenas import BLOQUES

N_BLOQUE = int(sys.argv[1]) if len(sys.argv) > 1 else 1
PLANOS = BLOQUES[N_BLOQUE]

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

# --- ritmo: nunca dos planos seguidos del mismo tamano, ni en la costura ---
def ritmo(planos, n_bloque):
    fallos = []
    previo = BLOQUES.get(n_bloque - 1)
    serie = ([previo[-1]] if previo else []) + list(planos)
    for a, b in zip(serie, serie[1:]):
        if a[1] == b[1]:
            fallos.append(f"{a[0]} y {b[0]} son ambos {a[1]}")
    return fallos

lineas = []
lineas.append(f"HOJA DE LOTE {N_BLOQUE:02d} — {len(PLANOS)} imagenes · Impostor / DONT BE SEEN")
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
for f in ritmo(PLANOS, N_BLOQUE):
    fallos += 1
    print("  !! ritmo:", f, file=sys.stderr)

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

open(f"LOTE_{N_BLOQUE:02d}.txt", "w", encoding="utf-8").write("\n".join(lineas))

print(f"{len(PLANOS)} prompts escritos en LOTE_{N_BLOQUE:02d}.txt")
print(f"con host: {sum(1 for x in PLANOS if x[3])}   sin host: {sum(1 for x in PLANOS if not x[3])}")
print("auditoria (negaciones + redaccion + ritmo):", "LIMPIA" if fallos == 0 else f"{fallos} FALLOS")
