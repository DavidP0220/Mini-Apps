# -*- coding: utf-8 -*-
"""Barrido de punta a punta de la produccion de Impostor.

Revisa que el guion, los tiempos, los movimientos y las hojas de prompts
digan lo mismo. Sale con codigo 1 si algo no cuadra, para que nunca se genere
una imagen sobre una base rota.
"""
import re, json, sys, importlib

OBJ_PLANOS = 225
WPM = 158
fallos, avisos = [], []

def ok(c, msg, dato=""):
    (print if c else fallos.append)(f"  {'OK  ' if c else 'FALLA'} {msg} {dato}" if c else f"{msg} {dato}")
    if c: return True
    return False

print("=" * 68); print("BARRIDO DE PRODUCCION — Impostor"); print("=" * 68)

# ---------- 1. guion ----------
print("\n[1] GUION")
g = open('GUION_impostor.md', encoding='utf-8').read()
txt = re.sub(r'\*+', '', ' '.join(
    l for l in g.split('## Verificacion de beats')[0].split('\n---\n',1)[1].split('\n')
    if l.strip() and not l.lstrip().startswith(('#','|','---','>')))).strip()
n_pal = len(txt.split()); dur = n_pal / WPM * 60
ok(True, f"palabras habladas: {n_pal} -> {int(dur//60)}:{int(dur%60):02d}")

BEATS = [("palabra del tema","Impostor syndrome",None),
         ("pregunta del titulo","nobody has ever explained why",None),
         ("comment one / zero","Comment one if you have felt",(.36,.44)),
         ("2a persona con ano","Tuesday in 40,000 BC",(.40,.49)),
         ("giro oscuro","I want to be honest",(.52,.58)),
         ("giro meta","And here's where it flips",(.65,.72)),
         ("comment eight","Comment eight if you",(.85,.90)),
         ("cierre citable","peace treaty with a tribe",(.90,1.0))]
for nom, frag, v in BEATS:
    i = txt.find(frag)
    if i < 0: fallos.append(f"beat ausente: {nom}"); continue
    w = len(txt[:i].split()); seg = w/WPM*60; pct = w/n_pal
    bien = (seg >= 22) if nom=="palabra del tema" else \
           (19 <= seg <= 45) if nom=="pregunta del titulo" else (v[0] <= pct <= v[1])
    ok(bien, f"beat {nom:22s}", f"{int(seg//60)}:{int(seg%60):02d} ({pct*100:.0f}%)")
ok("subscribe" not in txt.lower(), "cero CTA de suscripcion")

# ---------- 2. planos y ritmo ----------
print("\n[2] PLANOS, DURACION Y CAMARA")
P = json.load(open('PLANOS_VO.json', encoding='utf-8'))
ok(len(P) == OBJ_PLANOS, f"numero de planos = {OBJ_PLANOS}", f"({len(P)})")
segs = [r['seg'] for r in P]
total = sum(segs)
ok(abs(total - dur) < 2, "la suma de los planos cuadra con el guion",
   f"{int(total//60)}:{int(total%60):02d}")
ok(min(segs) >= 1.85, "ningun plano por debajo del piso", f"min {min(segs)}s")
ok(max(segs) <= 7.0, "ningun plano por encima del techo", f"max {max(segs)}s")
mov_ig = [(a['shot'],b['shot']) for a,b in zip(P,P[1:]) if a['mov']==b['mov']]
ok(not mov_ig, "nunca dos movimientos de camara seguidos iguales", f"({len(mov_ig)})")
ambos = [(a['shot'],b['shot']) for a,b in zip(P,P[1:])
         if abs(a['seg']-b['seg'])<.15 and a['mov']==b['mov']]
ok(not ambos, "nunca dos planos seguidos iguales en duracion Y camara", f"({len(ambos)})")
hook = [r for r in P if float(r['entrada'].split(':')[0])*60+float(r['entrada'].split(':')[1]) < 30]
ok(len(hook) >= 8, "hook rapido: 8 planos o mas en los primeros 30 s", f"({len(hook)})")
ok(sum(r['seg'] for r in hook)/len(hook) < 3.6, "duracion media del hook por debajo de 3.6 s",
   f"({sum(r['seg'] for r in hook)/len(hook):.1f}s)")
# el texto de los planos tiene que reconstruir el guion exacto
recon = ' '.join(r['vo'] for r in P).split()
ok(recon == txt.split(), "los planos reconstruyen el guion palabra por palabra")

# ---------- 3. hojas de prompts ----------
print("\n[3] HOJAS DE PROMPTS")
sys.path.insert(0, '.')
esc = importlib.import_module('escenas')
# Faltar escenas por escribir NO es un fallo: es trabajo pendiente del
# servidor. Lo que si es fallo es que una escena ya escrita este mal.
disenados = sum(len(v) for v in esc.BLOQUES.values())
print(f"  INFO  escenas escritas: {disenados}/{OBJ_PLANOS}")
if disenados < OBJ_PLANOS:
    avisos.append(f"faltan {OBJ_PLANOS - disenados} escenas por escribir "
                  f"(SH{disenados+1:03d} a SH{OBJ_PLANOS:03d}) — las escribe el servidor")
ids = [p[0] for v in esc.BLOQUES.values() for p in v]
ok(len(ids) == len(set(ids)), "sin shot_id repetidos")
ok(ids == sorted(ids), "los shot_id van en orden")
tam = [p[1] for v in esc.BLOQUES.values() for p in v]
rep = [(ids[i], ids[i+1]) for i in range(len(tam)-1) if tam[i] == tam[i+1]]
ok(not rep, "nunca dos planos seguidos del mismo tamano", f"({len(rep)}) {rep[:3]}")
# El host es el hilo del canal. Muchos planos seguidos sin el y el video deja
# de parecer de Mindset Mechanics.
MAX_SIN_HOST = 12
racha, peor, donde = 0, 0, ""
for p in [q for v in esc.BLOQUES.values() for q in v]:
    if p[3]: racha = 0
    else:
        racha += 1
        if racha > peor: peor, donde = racha, p[0]
ok(peor <= MAX_SIN_HOST, f"nunca mas de {MAX_SIN_HOST} planos seguidos sin host",
   f"(racha de {peor}, termina en {donde})")

PROH = ["nose","ears","hair","blush","nostril",r"\bno\b","without","never","avoid","remove"]
malos = [(p[0], w) for v in esc.BLOQUES.values() for p in v
         for w in PROH if re.search(w if w.startswith('\\') else r'\b'+w, p[2], re.I)]
ok(not malos, "cero negaciones en las escenas", f"{malos[:3]}")
ARR = ("with ","seen ","standing","framed ","alone ","half ")
mal_red = [p[0] for v in esc.BLOQUES.values() for p in v
           if p[3] and not (p[2].split()[0].endswith('ing') or p[2].startswith(ARR))]
ok(not mal_red, "redaccion valida en las escenas con host", f"{mal_red[:3]}")

# --- repeticion visual: lo que hace que un video "se vea repetido" ---
import collections
MOTIVOS = ["fire","ring","hand","wall","door","stone","crowd","stage","desk","map",
           "column","pyramid","bell","screen","phone","tablet","ash","snow","hut",
           "bed","tile","machine","mask","trophy","stack","drawer","suit","cloth"]
escs = [(p[0], p[2]) for v in esc.BLOQUES.values() for p in v]
rachas = []
for m in MOTIVOS:
    idx = [i for i,(s_,e_) in enumerate(escs) if re.search(r'\b'+m+r's?\b', e_, re.I)]
    run = []
    for i in idx + [10**9]:
        if run and i == run[-1] + 1:
            run.append(i); continue
        if len(run) >= 4:
            rachas.append(f"{m} en {escs[run[0]][0]}-{escs[run[-1]][0]} ({len(run)} seguidos)")
        run = [i]
ok(not rachas, "ningun motivo visual en 4 o mas planos seguidos", f"{rachas[:3]}")

# ---------- 4. correspondencia imagen <-> voz ----------
print("\n[4] IMAGEN CONTRA VOZ")
vo = {r['shot']: r for r in P}
sin_vo = [i for i in ids if i not in vo]
ok(not sin_vo, "toda escena disenada tiene su linea de voz", f"{sin_vo[:3]}")
if not sin_vo:
    print(f"  INFO  cubierto {len(ids)}/{OBJ_PLANOS} planos "
          f"({vo[ids[0]]['entrada']} a {vo[ids[-1]]['entrada']})")
    # los bloques 1 y 2 ya se reescribieron contra PLANOS_VO el 2026-08-30

# ---------- resultado ----------
print("\n" + "=" * 68)
if not fallos:
    print(f"VERDE — se puede generar hasta SH{disenados:03d}")
if fallos:
    print(f"{len(fallos)} FALLOS\n"); [print("  -", f) for f in fallos]
else:
    print("SIN FALLOS")
if avisos:
    print(f"\n{len(avisos)} avisos:"); [print("  ·", a) for a in avisos]
print("=" * 68)
sys.exit(1 if fallos else 0)
