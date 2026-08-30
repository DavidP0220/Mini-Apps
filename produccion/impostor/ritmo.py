# -*- coding: utf-8 -*-
"""Corta el guion siguiendo una CURVA DE RITMO pensada para retencion.

La duracion de cada plano no sale del texto: sale de donde esta el espectador
en la curva de abandono. El texto se corta para caber en la duracion, no al
reves.

Cuatro mecanismos:
  1 HOOK RAPIDO      los primeros 30 s van a 2-3 s por plano. La mitad de la
                     audiencia se va ahi; el corte rapido compra atencion.
  2 RAMPA            los 4 planos antes de cada beat se van acortando. La
                     aceleracion avisa al cuerpo que viene algo.
  3 SOSTENIDO        la linea del beat se queda 6-7 s. El contraste con la
                     rampa es lo que hace que la frase pese.
  4 INTERRUPTOR      cada 25-35 s entra un plano corto de 2 s que rompe.
"""
import re, json

WPM = 158
PAUSA = re.compile(r'[.!?,;:—]$')

# ---- beats: se sostienen. La frase que los abre no se corta rapido. ----
BEATS = ["nobody has ever explained why",
         "Comment one if you have felt",
         "Tuesday in 40,000 BC",
         "I want to be honest",
         "And here's where it flips",
         "It is a fear of being seen as good enough",
         "Comment eight if you",
         "peace treaty with a tribe"]

def guion():
    s = open('GUION_impostor.md', encoding='utf-8').read()
    s = s.split('## Verificacion de beats')[0].split('\n---\n', 1)[1]
    l = [x for x in s.split('\n')
         if x.strip() and not x.lstrip().startswith(('#', '|', '---', '>'))]
    return re.sub(r'\*+', '', ' '.join(l)).strip()

def objetivo(pos, dur_total, desde_beat, hasta_beat, i):
    """Segundos que deberia durar este plano segun donde va el video."""
    t = pos * dur_total
    if t < 30:      base = 2.4          # hook: corte rapido
    elif t < 60:    base = 3.2
    elif pos > .92: base = 5.8          # cierre: se abre, respira
    elif .52 <= pos <= .58: base = 5.2  # giro oscuro: lento y pesado
    else:           base = 4.2          # cuerpo

    if desde_beat is not None and desde_beat <= 1:
        base = max(base, 6.2)           # 3 SOSTENIDO
    elif hasta_beat is not None and hasta_beat <= 4:
        base = 2.4 + .45 * hasta_beat   # 2 RAMPA: 2.8 · 3.2 · 3.7 · 4.2

    if i % 8 == 7 and t > 45:           # 4 INTERRUPTOR
        base = 2.1
    return base + (0.35 if i % 2 else -0.35)   # nunca dos iguales seguidos

texto = guion()
pal = texto.split()
dur_total = len(pal) / WPM * 60

# posiciones de palabra donde arranca cada beat
pos_beats = sorted(len(texto[:texto.find(b)].split()) for b in BEATS if texto.find(b) > 0)

bloques, buf, i = [], [], 0
while True:
    idx = len(' '.join(bloques).split()) if bloques else 0
    if idx >= len(pal): break
    prox = next((p for p in pos_beats if p > idx), None)
    prev = max((p for p in pos_beats if p <= idx), default=None)
    hasta = None if prox is None else max(0, prox - idx) / 10.5
    desde = None if prev is None else (idx - prev) / 10.5
    obj = objetivo(idx / len(pal), dur_total, desde, hasta, i)
    meta_pal = obj / 60 * WPM

    buf = []
    j = idx
    while j < len(pal):
        buf.append(pal[j]); j += 1
        if len(buf) >= meta_pal * .8 and PAUSA.search(buf[-1]): break
        if len(buf) >= meta_pal * 1.5:
            for _ in range(6):                       # estira buscando pausa
                if j < len(pal) and not PAUSA.search(buf[-1]):
                    buf.append(pal[j]); j += 1
                else: break
            break
    bloques.append(' '.join(buf)); i += 1

# ---- ajuste al numero exacto de planos ----
OBJ = 225
def partir(b):
    w = b.split()
    c = [k + 1 for k, x in enumerate(w[:-1]) if PAUSA.search(x)] or [len(w) // 2]
    m = min(c, key=lambda k: abs(k - len(w) / 2))
    return ' '.join(w[:m]), ' '.join(w[m:])
while len(bloques) < OBJ:
    k = max(range(len(bloques)), key=lambda x: len(bloques[x].split()))
    a, b = partir(bloques[k]); bloques[k:k+1] = [a, b]
while len(bloques) > OBJ:
    k = min(range(len(bloques)-1), key=lambda x: len(bloques[x].split())+len(bloques[x+1].split()))
    bloques[k:k+2] = [bloques[k] + ' ' + bloques[k+1]]

# ---- piso de 2.0 s: nada mas corto se alcanza a leer ----
PISO_PAL = int(2.0 / 60 * WPM)          # 5 palabras
def seg(b): return len(b.split()) / WPM * 60

cambio = True
while cambio:
    cambio = False
    for k, b in enumerate(bloques):
        if seg(b) >= 1.85 or len(bloques) == 1:
            continue
        # se funde con el vecino mas corto, para no crear un plano enorme
        izq = seg(bloques[k-1]) if k > 0 else 1e9
        der = seg(bloques[k+1]) if k < len(bloques)-1 else 1e9
        if izq <= der: bloques[k-1:k+1] = [bloques[k-1] + ' ' + b]
        else:          bloques[k:k+2]   = [b + ' ' + bloques[k+1]]
        cambio = True
        break

# ---- desempate: dos planos seguidos con la misma duracion pasan una palabra ----
for _ in range(4):
    for k in range(len(bloques) - 1):
        a, b = bloques[k], bloques[k+1]
        w = a.split()
        if (abs(seg(a) - seg(b)) < .15 and len(w) > PISO_PAL + 1
                and PAUSA.search(w[-2])):          # solo si el corte queda en pausa
            bloques[k], bloques[k+1] = ' '.join(w[:-1]), w[-1] + ' ' + b

# ---- piso y numero exacto a la vez: se parte solo lo que aguanta partirse ----
for _ in range(30):
    while len(bloques) < OBJ:
        # el mas largo cuyas dos mitades sigan por encima del piso
        cand = [x for x in range(len(bloques))
                if min(len(p.split()) for p in partir(bloques[x])) >= PISO_PAL]
        if not cand: break
        k = max(cand, key=lambda x: len(bloques[x].split()))
        a, b = partir(bloques[k]); bloques[k:k+1] = [a, b]
    while len(bloques) > OBJ:
        k = min(range(len(bloques)-1),
                key=lambda x: len(bloques[x].split()) + len(bloques[x+1].split()))
        bloques[k:k+2] = [bloques[k] + ' ' + bloques[k+1]]
    cortos = [x for x, b in enumerate(bloques) if seg(b) < 1.85]
    if not cortos and len(bloques) == OBJ:
        break
    for x in reversed(cortos):
        if len(bloques) == 1: break
        izq = seg(bloques[x-1]) if x > 0 else 1e9
        der = seg(bloques[x+1]) if x < len(bloques)-1 else 1e9
        if izq <= der and x > 0: bloques[x-1:x+1] = [bloques[x-1] + ' ' + bloques[x]]
        elif x < len(bloques)-1: bloques[x:x+2] = [bloques[x] + ' ' + bloques[x+1]]

# ---- movimiento de camara para VideoExpress ----
# Dos planos de la misma duracion se sienten iguales. El movimiento es lo que
# los separa: si duran lo mismo, tienen que moverse en familias distintas.
MOV = {
 "zoom":   ["zoom in lento", "zoom out lento", "zoom in fuerte"],
 "paneo":  ["paneo a la izquierda", "paneo a la derecha"],
 "tilt":   ["tilt hacia arriba", "tilt hacia abajo"],
 "quieto": ["plano fijo"],
}
FAMILIAS = list(MOV)

def familia_de(m):
    return next(f for f, v in MOV.items() if m in v)

filas, t = [], 0.0
ult_mov, ult_fam, ult_seg = None, None, None
usos = {m: 0 for v in MOV.values() for m in v}

for n, b in enumerate(bloques, 1):
    d = round(len(b.split()) / WPM * 60, 1)
    sostenido = d >= 5.5                       # la linea larga se queda quieta
    if sostenido and ult_mov != "plano fijo":
        mov = "plano fijo"
    else:
        # familias permitidas: nunca la anterior; si dura igual que el previo,
        # ademas se exige cambiar de familia
        prohib = {ult_fam} if (ult_seg is not None and abs(d - ult_seg) < .15) else set()
        cand = [m for f in FAMILIAS if f not in prohib and f != "quieto"
                  for m in MOV[f] if m != ult_mov]
        mov = min(cand, key=lambda m: usos[m])   # reparte, no repite siempre el mismo
    usos[mov] += 1
    filas.append({"shot": f"SH{n:03d}", "entrada": f"{int(t//60)}:{t%60:04.1f}",
                  "seg": d, "palabras": len(b.split()), "mov": mov, "vo": b})
    ult_mov, ult_fam, ult_seg = mov, familia_de(mov), d
    t += d

json.dump(filas, open('PLANOS_VO.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)
with open('PLANOS_VO.md','w',encoding='utf-8') as f:
    f.write(f"# Voz y ritmo por plano — {len(filas)} planos\n\n")
    f.write(f"Duracion {int(t//60)}:{int(t%60):02d} · cortado por curva de ritmo, no por palabras.\n\n")
    f.write("| # | entrada | seg | camara | linea de voz |\n|---|---|---|---|---|\n")
    for r in filas:
        f.write(f"| {r['shot']} | {r['entrada']} | {r['seg']} | {r['mov']} | {r['vo']} |\n")

segs = [r['seg'] for r in filas]
iguales = sum(1 for a,b in zip(segs, segs[1:]) if abs(a-b) < .15)
print(f"{len(filas)} planos · {int(t//60)}:{int(t%60):02d}")
print(f"hook (primeros 30 s): {sum(1 for r in filas if float(r['entrada'].split(':')[0])*60+float(r['entrada'].split(':')[1]) < 30)} planos")
print(f"duracion  min {min(segs)}s  max {max(segs)}s  media {sum(segs)/len(segs):.1f}s")
print(f"planos seguidos con la misma duracion: {iguales}")
mov_ig = sum(1 for a,b in zip(filas, filas[1:]) if a['mov'] == b['mov'])
ambos = sum(1 for a,b in zip(filas, filas[1:])
            if abs(a['seg']-b['seg']) < .15 and a['mov'] == b['mov'])
print(f"planos seguidos con el mismo movimiento: {mov_ig}")
print(f"planos seguidos iguales en duracion Y movimiento: {ambos}")
print("\nprimeros 10:")
for r in filas[:10]:
    print(f"   {r['shot']} {r['entrada']:>6s} {r['seg']:>4}s {r['mov']:<22s} {r['vo'][:48]}")
