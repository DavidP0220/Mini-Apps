# -*- coding: utf-8 -*-
"""Calendario de publicacion y calculo del camino a la monetizacion.

YouTube exige 1.000 suscriptores Y 4.000 horas de reproduccion en 12 meses.
En este nicho las horas NO son el problema: un video de 3 h con 25 minutos de
retencion media aporta muchisimo. El cuello de botella son los suscriptores,
y eso lo mueven los Shorts y la constancia.

Este script arma el calendario real: que se publica cada dia, a que hora y
en que orden, respetando que un video y su gemelo negro nunca compitan.

Uso:
  python3 scripts/12_calendario.py --canal lakshmi --desde 2026-09-01
  python3 scripts/12_calendario.py --canal lakshmi --desde 2026-09-01 --retencion 22
"""
import argparse, datetime as dt, json, pathlib, sys

BASE = pathlib.Path(__file__).resolve().parent.parent
CAT = json.loads((BASE / "datos" / "catalogo.json").read_text(encoding="utf-8"))

# Horas en punto (hora del este de EE.UU.) segun el momento de consumo.
# Sueno: la gente se acuesta. Dinero/manifestacion: rutina de la manana.
HORA = {"sueno": "21:00", "dia": "07:00", "short": "12:00"}


def clasifica(v):
    return "sueno" if v["horas"] >= 3 else "dia"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--canal", required=True)
    ap.add_argument("--desde", required=True, help="AAAA-MM-DD")
    ap.add_argument("--retencion", type=float, default=25.0,
                    help="minutos de retencion media estimada (por defecto 25)")
    a = ap.parse_args()

    canal = next((c for c in CAT["canales"] if c["slug"] == a.canal), None)
    if not canal:
        sys.exit("canal invalido: lakshmi, ganesha o uriel")
    d0 = dt.date.fromisoformat(a.desde)

    # Se alternan: video largo, Short, gemelo negro, Short...
    # Un video y su gemelo quedan separados minimo 48 h.
    agenda, dia = [], 0
    for v in canal["videos"]:
        agenda.append((d0 + dt.timedelta(days=dia), HORA[clasifica(v)],
                       "VIDEO", v["id"], v["titulo_corto"], f"{v['horas']}h {v['hz']}Hz"))
        agenda.append((d0 + dt.timedelta(days=dia), HORA["short"],
                       "SHORT", v["id"] + "-short", v["miniatura_texto"], "45 s vertical"))
        if v["horas"] >= 3:
            agenda.append((d0 + dt.timedelta(days=dia + 3), HORA["sueno"],
                           "NEGRO", v["id"] + "-negro", "BLACK SCREEN " + v["miniatura_texto"],
                           f"{v['horas']}h pantalla negra"))
        dia += 2                                   # un video largo cada 36-48 h

    agenda.sort(key=lambda x: (x[0], x[1]))

    # --- camino a la monetizacion
    horas_video = sum(v["horas"] for v in canal["videos"])
    n_negros = sum(1 for v in canal["videos"] if v["horas"] >= 3)
    minutos_meta = 4000 * 60
    vistas_necesarias = minutos_meta / a.retencion

    out = [f"# Calendario de publicación — {canal['nombre']}",
           "",
           f"Inicio: **{d0.isoformat()}** · {len(canal['videos'])} videos largos, "
           f"{len(canal['videos'])} Shorts y {n_negros} gemelos en pantalla negra.",
           f"Total: **{len(agenda)} publicaciones** en {agenda[-1][0].isoformat()}.",
           "",
           "## Camino a la monetización",
           "",
           "YouTube pide **1.000 suscriptores** y **4.000 horas de reproducción** en 12 meses.",
           "",
           "| Requisito | Cálculo | Resultado |",
           "|---|---|---|",
           f"| Horas de reproducción | 4.000 h = 240.000 min ÷ {a.retencion:.0f} min de retención media | "
           f"**{vistas_necesarias:,.0f} vistas** |",
           f"| Suscriptores | 1.000 subs con ~1,5% de conversión | "
           f"**{1000/0.015:,.0f} vistas** |",
           "",
           "**El cuello de botella son los suscriptores, no las horas.** Con videos de 3 a 8 horas",
           "las horas de reproducción llegan solas: quien deja el video toda la noche aporta",
           "8 horas de una sentada. Por eso el plan carga tanto en Shorts, que es lo que",
           "convierte espectadores en suscriptores.",
           "",
           f"Catálogo de este canal: **{horas_video} horas** de contenido. Si cada video",
           f"acumulara solo 300 vistas al mes, serían {300*len(canal['videos'])*a.retencion/60:,.0f} horas",
           "de reproducción mensuales.",
           "",
           "## Reglas que sigue este calendario",
           "",
           "1. Un video largo cada **48 horas**: constante sin saturar.",
           "2. Cada video largo lleva **su Short el mismo día al mediodía** — el Short",
           "   trae gente nueva y el video largo retiene.",
           "3. El **gemelo en pantalla negra sale 3 días después**, nunca el mismo día:",
           "   así no compiten entre sí por la misma búsqueda.",
           "4. Horarios en **hora del este de EE.UU.**, que es el mercado que mejor paga:",
           "   - Videos de sueño (3 h o más): **21:00**, cuando la gente se acuesta",
           "   - Videos de día (1 h): **07:00**, rutina de la mañana",
           "   - Shorts: **12:00**, hora del almuerzo",
           "",
           "## Calendario",
           "",
           "| Fecha | Hora (ET) | Tipo | Qué se publica | Detalle |",
           "|---|---|---|---|---|"]

    for fecha, hora, tipo, vid, titulo, det in agenda:
        dias = ["lunes","martes","miércoles","jueves","viernes","sábado","domingo"]
        out.append(f"| {fecha.isoformat()} ({dias[fecha.weekday()][:3]}) | {hora} | "
                   f"{tipo} | {titulo} | {det} |")

    out += ["",
            "## Listas de reproducción (créalas antes de publicar)",
            "",
            "Las listas suben mucho el tiempo por sesión: al terminar un video arranca el",
            "siguiente solo. Es la palanca más barata para las 4.000 horas.",
            "",
            "| Lista | Qué incluye |",
            "|---|---|",
            "| Sleep Frequencies (Black Screen) | Todos los gemelos negros |",
            "| 8 Hour Deep Sleep | Los videos de 8 horas |",
            "| 888 Hz Money Frequency | Todos los de 888 Hz |",
            "| Morning Abundance Ritual | Los de 1 hora |",
            "",
            "Pon la lista correspondiente en la **pantalla final** de cada video y en el",
            "**primer enlace de la descripción**."]

    d = BASE / "salida" / "_calendario"
    d.mkdir(parents=True, exist_ok=True)
    f = d / f"calendario-{a.canal}.md"
    f.write_text("\n".join(out), encoding="utf-8")
    print(f"OK -> {f}  ({len(agenda)} publicaciones)")
    print(f"Vistas necesarias para las 4.000 h: {vistas_necesarias:,.0f}")


if __name__ == "__main__":
    main()
