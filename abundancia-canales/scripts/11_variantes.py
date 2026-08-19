# -*- coding: utf-8 -*-
"""Genera el paquete de la variante PANTALLA NEGRA de un video ya producido.

La misma produccion rinde dos videos: el de imagen y el de pantalla negra.
Son videos distintos para YouTube (titulo, miniatura y publico distintos), no
contenido duplicado: el de imagen compite en "abundance music" y el negro en
"black screen sleep music", que es una busqueda enorme y con menos competencia.

Solo tiene sentido para videos de 3 horas o mas, que es donde vive el publico
que duerme con el video puesto.

Uso:
  python3 scripts/11_variantes.py --id lakshmi-04
  python3 scripts/11_variantes.py --todos      (todos los que califican)
"""
import argparse, json, pathlib, sys

BASE = pathlib.Path(__file__).resolve().parent.parent
CAT = json.loads((BASE / "datos" / "catalogo.json").read_text(encoding="utf-8"))

GANCHOS_NEGRO = [
    "Black Screen Sleep Music, Fall Asleep Instantly",
    "BLACK SCREEN Sleep Music, Fall Asleep In Minutes",
    "Black Screen, Deep Sleep In Under 10 Minutes",
]
DOLENCIAS = ["Insomnia, Anxiety & Overthinking",
             "Insomnia, Stress & Racing Thoughts",
             "Insomnia, ADHD & Night Anxiety"]

TAGS = ["black screen sleep music","sleep music black screen","deep sleep music",
 "fall asleep fast","insomnia relief","anxiety relief","stress relief",
 "sleep meditation","sleep aid","healing frequency","meditation music",
 "binaural beats","rain sounds","dark screen sleep"]


def titulo(v, n):
    """Maximo 100 caracteres, con la frecuencia y la duracion al final."""
    g = GANCHOS_NEGRO[n % len(GANCHOS_NEGRO)]
    d = DOLENCIAS[n % len(DOLENCIAS)]
    for cand in (f"{g} | {d} • {v['hz']} Hz • {v['horas']} Hours",
                 f"{g} | {d} • {v['horas']} Hours",
                 f"{g} • {v['hz']} Hz • {v['horas']} Hours"):
        if len(cand) <= 100:
            return cand
    return cand[:100]


def paquete(canal, v, n):
    t = titulo(v, n)
    desc = f"""{t}

A completely black screen so nothing lights up your room and your battery lasts the night. Underneath it, {v['hz']}Hz tuned music with a soft layer of rain, looped seamlessly for {v['horas']} hours — no jumps, no sudden volume changes, nothing that pulls you out of sleep.

WHY A BLACK SCREEN
• Your room stays dark, so your melatonin is not disrupted
• Your phone or TV uses far less battery through the night
• Nothing moves on screen to catch your eye if you wake up

HOW TO USE IT
1. Start it at a low volume, just loud enough to notice.
2. Lie down and let your breathing slow for the first few minutes.
3. Leave it playing all night. It fades out gently at the end.

⚠️ Do not listen while driving. This music is for relaxation and sleep. It is not a substitute for medical treatment for insomnia or anxiety.

🔔 Subscribe to {canal['nombre']} for a new sleep frequency every 36 hours.

© {canal['nombre']}. Original music and visuals. All rights reserved."""

    return f"""# {v['id']}-negro — variante PANTALLA NEGRA

Producida a partir de **{v['id']}**, sin volver a generar musica ni imagenes.

## 1) Renderizarla
```bash
python3 scripts/03_audio.py --id {v['id']} --base bases/{v['id']}.wav --lluvia -19
python3 scripts/04_video.py --id {v['id']} --negro
```
Sale `salida/{v['id']}/{v['id']}-negro.mp4`. Pesa una fraccion del original.

## 2) TÍTULO — pégalo en YouTube Studio
```
{t}
```

## 3) DESCRIPCIÓN
```
{desc}
```

## 4) ETIQUETAS
```
{", ".join(TAGS + [f"{v['hz']}hz", f"{v['horas']} hour sleep music"])}
```

## 5) MINIATURA
Usa una imagen **muy oscura** con el texto en blanco: tiene que prometer oscuridad.
No reutilices la miniatura dorada del video original — confundiria a la audiencia.
Texto sugerido: **BLACK SCREEN** arriba y **{v['hz']} Hz · {v['horas']}H** abajo.

## 6) CUÁNDO PUBLICARLA
Entre las 20:00 y las 23:00 hora de Estados Unidos, y **nunca el mismo dia** que
el video original: separalas al menos 48 horas para que no compitan entre si.
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--id")
    ap.add_argument("--todos", action="store_true")
    a = ap.parse_args()
    if not (a.id or a.todos):
        sys.exit("Indica --id <video> o --todos")

    n = 0
    for c in CAT["canales"]:
        for v in c["videos"]:
            if a.id and v["id"] != a.id:
                continue
            if v["horas"] < 3:
                if a.id:
                    sys.exit(f"{v['id']} dura {v['horas']} h. La variante negra solo "
                             f"tiene sentido desde 3 h.")
                continue
            d = BASE / "salida" / c["slug"]
            d.mkdir(parents=True, exist_ok=True)
            (d / f"{v['id']}-negro.md").write_text(paquete(c, v, n), encoding="utf-8")
            n += 1
    print(f"OK -> {n} paquetes de variante negra generados")


if __name__ == "__main__":
    main()
