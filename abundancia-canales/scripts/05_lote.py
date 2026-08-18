# -*- coding: utf-8 -*-
"""Procesa en lote todos los videos de un canal que ya tengan
audio base + imagenes listos. Uso: python3 scripts/05_lote.py --canal lakshmi"""
import argparse, json, pathlib, subprocess, sys
BASE = pathlib.Path(__file__).resolve().parent.parent
CAT = json.loads((BASE/"datos"/"catalogo.json").read_text(encoding="utf-8"))
ap = argparse.ArgumentParser(); ap.add_argument("--canal", required=True)
ap.add_argument("--bases", default="bases", help="carpeta con melodias base <id>.wav")
a = ap.parse_args()
canal = next((c for c in CAT["canales"] if c["slug"]==a.canal), None) or sys.exit("canal invalido")
hechos, faltan = [], []
for v in canal["videos"]:
    d = BASE/"salida"/v["id"]; base = BASE/a.bases/f"{v['id']}.wav"
    if not base.exists() or not (d/"img").exists():
        faltan.append(v["id"]); continue
    if not (d/"audio.wav").exists():
        subprocess.run([sys.executable, str(BASE/"scripts"/"03_audio.py"),"--id",v["id"],"--base",str(base)],check=True)
    subprocess.run([sys.executable, str(BASE/"scripts"/"04_video.py"),"--id",v["id"]],check=True)
    hechos.append(v["id"])
print(f"\nRenderizados: {len(hechos)}  |  Sin insumos: {len(faltan)}")
if faltan: print("Faltan base o imagenes:", ", ".join(faltan))
