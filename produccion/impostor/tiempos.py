# -*- coding: utf-8 -*-
"""Parte el guion en bloques de 4 segundos y les pone tiempo de entrada.

A 158 wpm, 4 segundos = 10.53 palabras. El corte se busca en el limite de
frase mas cercano para que ninguna imagen empiece a media palabra.
"""
import re, json, sys

WPM   = 158
SEG   = 4.0
PAL   = WPM / 60 * SEG          # palabras por bloque

def guion():
    """Solo el texto hablado: desde el primer separador --- del encabezado
    hasta antes de la tabla de verificacion, sin titulos ni tablas."""
    s = open('GUION_impostor.md', encoding='utf-8').read()
    s = s.split('## Verificacion de beats')[0]
    s = s.split('\n---\n', 1)[1]                      # salta el encabezado
    lineas = [l for l in s.split('\n')
              if l.strip() and not l.lstrip().startswith(('#', '|', '---', '>'))]
    return re.sub(r'\*+', '', ' '.join(lineas)).strip()

def frases(t):
    """Corta en frases, conservando el signo final."""
    return [f.strip() for f in re.split(r'(?<=[.!?])\s+', t) if f.strip()]

PAUSA = re.compile(r'[.!?,;:—]$')

def bloques(texto, objetivo, r_pausa=.85, r_max=1.45):
    """Camina el texto palabra por palabra llenando bloques de ~PAL palabras.
    Cierra el bloque en la pausa mas cercana al objetivo, para que ninguna
    imagen empiece a media frase. Nunca pasa de MAXP palabras."""
    pal = texto.split()
    ideal = len(pal) / objetivo          # palabras por bloque para dar el total
    MINP, MAXP = max(4, int(ideal * .5)), max(6, int(ideal * r_max))
    out, buf = [], []
    i = 0
    while i < len(pal):
        w = pal[i]; buf.append(w); i += 1
        n = len(buf)
        if n >= MINP and PAUSA.search(w) and n >= ideal * r_pausa:
            out.append(' '.join(buf)); buf = []
        elif n >= MAXP:
            # antes de cortar a la fuerza, estira hasta 3 palabras buscando pausa
            for _ in range(8):
                if i < len(pal) and not PAUSA.search(buf[-1]):
                    buf.append(pal[i]); i += 1
                else:
                    break
            out.append(' '.join(buf)); buf = []
    if buf:
        if out and len(buf) < MINP: out[-1] += ' ' + ' '.join(buf)
        else: out.append(' '.join(buf))
    return out

texto = guion()
# busca los parametros de corte que dan exactamente el numero de bloques
# pedido con la menor cantidad de bloques fuera del rango 2.5-5.5 s
OBJETIVO = 226
mejor = None
for rp in [x / 100 for x in range(45, 101, 5)]:
    for rm in [x / 100 for x in range(105, 156, 5)]:
        c = bloques(texto, OBJETIVO, rp, rm)
        segs = [len(b.split()) / WPM * 60 for b in c]
        fuera = sum(1 for x in segs if x > 5.5 or x < 2.5)
        feos = sum(1 for b in c if not PAUSA.search(b.split()[-1]))
        clave = (abs(len(c) - OBJETIVO), feos, fuera)
        if mejor is None or clave < mejor[0]:
            mejor = (clave, rp, rm, c)
_, RP, RM, bl = mejor
print(f"corte elegido: pausa={RP} max={RM} -> {len(bl)} bloques")

def partir(b):
    """Parte un bloque en dos por la pausa interna mas cercana al centro."""
    w = b.split()
    cortes = [i + 1 for i, x in enumerate(w[:-1]) if PAUSA.search(x)]
    if not cortes:
        cortes = [len(w) // 2]
    c = min(cortes, key=lambda i: abs(i - len(w) / 2))
    return ' '.join(w[:c]), ' '.join(w[c:])

# ajusta al objetivo exacto: parte los bloques mas largos, une los mas cortos
while len(bl) < OBJETIVO:
    i = max(range(len(bl)), key=lambda k: len(bl[k].split()))
    a, b = partir(bl[i]); bl[i:i + 1] = [a, b]
while len(bl) > OBJETIVO:
    i = min(range(len(bl) - 1), key=lambda k: len(bl[k].split()) + len(bl[k + 1].split()))
    bl[i:i + 2] = [bl[i] + ' ' + bl[i + 1]]
print(f"ajustado a {len(bl)} bloques")
n = len(bl)

filas, t = [], 0.0
for i, b in enumerate(bl, 1):
    dur = len(b.split()) / WPM * 60
    filas.append({"shot": f"SH{i:03d}",
                  "entrada": f"{int(t//60)}:{t%60:04.1f}",
                  "seg": round(dur, 1),
                  "palabras": len(b.split()),
                  "vo": b})
    t += dur

json.dump(filas, open('PLANOS_VO.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

with open('PLANOS_VO.md', 'w', encoding='utf-8') as f:
    f.write(f"# Voz en off por plano — {n} bloques de 4 s\n\n")
    f.write(f"Total {len(texto.split())} palabras · {int(t//60)}:{int(t%60):02d}\n\n")
    f.write("| # | entrada | seg reales | linea de voz |\n|---|---|---|---|\n")
    for r in filas:
        f.write(f"| {r['shot']} | {r['entrada']} | {r['seg']} | {r['vo']} |\n")

largos = [r for r in filas if r['seg'] > 5.5]
cortos = [r for r in filas if r['seg'] < 2.5]
print(f"{n} bloques · objetivo 226 · {len(texto.split())} palabras habladas")
print(f"duracion total {int(t//60)}:{int(t%60):02d}")
print(f"fuera de rango -> largos (>5.5s): {len(largos)}   cortos (<2.5s): {len(cortos)}")
for r in largos[:4]: print("   largo ", r['shot'], r['seg'], "s ->", r['vo'][:55])
for r in cortos[:4]: print("   corto ", r['shot'], r['seg'], "s ->", r['vo'][:55])
print("\nprimeros bloques:")
feos = [r for r in filas if not PAUSA.search(r['vo'].split()[-1])]
print(f"cortes a media frase: {len(feos)}")
for r in filas[:5]: print(f"   {r['shot']} {r['entrada']:>6s} {r['seg']}s  {r['vo']}")
