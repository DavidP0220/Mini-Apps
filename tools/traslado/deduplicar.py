#!/usr/bin/env python3
"""
deduplicar.py — quita del arbol de traslado todo lo que esta repetido.

Compara por huella SHA-256 del contenido, no por nombre: dos archivos con
nombres distintos pero contenido identico cuentan como duplicado, y dos
archivos con el mismo nombre pero contenido distinto NO se tocan.

Que hace, en orden:

1. Borra los .zip anidados cuyo contenido completo ya existe suelto en el
   arbol. Son copias comprimidas de lo mismo y obligan a descomprimir zips
   dentro de zips para nada. Si un zip tuviera aunque sea UN archivo que no
   esta suelto, se conserva entero.
2. De cada grupo de archivos identicos, deja UNA copia — la que esta en el
   sitio mas canonico — y borra las demas.
3. Escribe DUPLICADOS_ELIMINADOS.md: cada archivo borrado con la ruta de la
   copia que sobrevive. Nada desaparece sin dejar dicho donde esta.

Uso:
    python3 deduplicar.py <carpeta_del_arbol> <archivo_de_reporte.md>
"""
import hashlib
import os
import subprocess
import sys
import zipfile
from collections import defaultdict

# Orden de preferencia: gana el numero mas bajo. Dentro del mismo puntaje,
# gana la ruta menos profunda y, a igualdad, el orden alfabetico.
# Orden de preferencia: gana el numero mas bajo. Se recorre en orden, asi que
# los prefijos mas especificos van primero. La idea es que gane el documento
# VIVO (el del repo o el de la carpeta de trabajo), no un snapshot: los
# paquetes de conocimiento y el paquete que se le mando a Kimi son fotos de un
# dia concreto, utiles como historico pero no son donde se sigue trabajando.
PREFERENCIA = [
    # snapshots — siempre pierden
    ("01_HANDOFFS_KIMI_CLAUDE_COMPLETO/HANDOFF_KIMI_PACKAGE", 40),
    ("03_DOCUMENTACION_Y_MANUALES/PROY_MECH_OPT/PAQUETE_CONOCIMIENTO_v3", 41),
    ("03_DOCUMENTACION_Y_MANUALES/PAQUETE_CONOCIMIENTO_2026-08-23_v2", 42),
    ("03_DOCUMENTACION_Y_MANUALES/PAQUETE_CONOCIMIENTO_2026-08-23", 43),
    # material vivo
    ("01_HANDOFFS_KIMI_CLAUDE_COMPLETO/handoffs", 10),
    ("03_DOCUMENTACION_Y_MANUALES/docs_raiz_repo", 11),
    ("03_DOCUMENTACION_Y_MANUALES/PROY_MECH_OPT", 12),
    ("01_HANDOFFS_KIMI_CLAUDE_COMPLETO", 13),
    ("02_CODIGO_PIPELINE", 13),
    ("04_STORYBOARDS", 13),
    ("05_MEDIA_REFERENCIA", 13),
    ("06_MEMORIA_PERSISTENTE_CLAUDE", 13),
    ("07_AGENTES_CLAUDE_CODE", 13),
    ("03_DOCUMENTACION_Y_MANUALES", 20),
]


def puntaje(rel):
    for prefijo, valor in PREFERENCIA:
        if rel == prefijo or rel.startswith(prefijo + "/"):
            return (valor, rel.count("/"), rel)
    return (5, rel.count("/"), rel)  # archivos sueltos de la raiz: maxima prioridad


def lineas(ruta):
    """Lineas no vacias de un archivo de texto; vacio si es binario."""
    try:
        with open(ruta, encoding="utf-8") as fh:
            return {l.strip() for l in fh if l.strip()}
    except (UnicodeDecodeError, OSError):
        return set()


SNAPSHOTS = (
    "01_HANDOFFS_KIMI_CLAUDE_COMPLETO/HANDOFF_KIMI_PACKAGE",
    "03_DOCUMENTACION_Y_MANUALES/PROY_MECH_OPT/PAQUETE_CONOCIMIENTO_v3",
    "03_DOCUMENTACION_Y_MANUALES/PAQUETE_CONOCIMIENTO_2026-08-23_v2",
    "03_DOCUMENTACION_Y_MANUALES/PAQUETE_CONOCIMIENTO_2026-08-23",
)


def es_snapshot(rel):
    return any(rel.startswith(p + "/") for p in SNAPSHOTS)


def parecido(a, b):
    """Jaccard entre dos conjuntos de lineas: 1.0 identicos, 0.0 sin nada en comun."""
    union = a | b
    return len(a & b) / len(union) if union else 0.0


def sha256(ruta):
    h = hashlib.sha256()
    with open(ruta, "rb") as fh:
        for bloque in iter(lambda: fh.read(1 << 20), b""):
            h.update(bloque)
    return h.hexdigest()


def main():
    raiz, reporte = sys.argv[1], sys.argv[2]
    reporte_versiones = sys.argv[3] if len(sys.argv) > 3 else None
    raiz = os.path.abspath(raiz)

    archivos = []
    for dirpath, _, nombres in os.walk(raiz):
        for n in nombres:
            archivos.append(os.path.relpath(os.path.join(dirpath, n), raiz))
    archivos.sort()

    huella = {rel: sha256(os.path.join(raiz, rel)) for rel in archivos}
    sueltos = defaultdict(list)
    for rel, h in huella.items():
        sueltos[h].append(rel)

    borrados = []          # (ruta_borrada, motivo, ruta_que_sobrevive)
    zips_borrados = []

    # --- 1. zips anidados cuyo contenido ya existe suelto ---------------------
    for rel in [r for r in archivos if r.lower().endswith(".zip")]:
        ruta = os.path.join(raiz, rel)
        try:
            with zipfile.ZipFile(ruta) as z:
                miembros = [m for m in z.infolist() if not m.is_dir()]
                falta = None
                for m in miembros:
                    h = hashlib.sha256(z.read(m)).hexdigest()
                    fuera = [p for p in sueltos.get(h, []) if p != rel]
                    if not fuera:
                        falta = m.filename
                        break
        except (zipfile.BadZipFile, OSError) as e:
            print(f"  aviso: no se pudo leer {rel} ({e}); se conserva")
            continue
        if falta is None and miembros:
            zips_borrados.append((rel, len(miembros)))
        else:
            print(f"  se conserva {rel}: contiene algo que no esta suelto ({falta})")

    for rel, n in zips_borrados:
        os.remove(os.path.join(raiz, rel))
        borrados.append((rel, f"zip redundante: sus {n} archivos ya estan sueltos", "-"))
        archivos.remove(rel)
        huella.pop(rel, None)

    # --- 2. copias identicas: se deja la mas canonica -------------------------
    grupos = defaultdict(list)
    for rel in archivos:
        grupos[huella[rel]].append(rel)

    for h, rels in grupos.items():
        if len(rels) < 2:
            continue
        rels.sort(key=puntaje)
        se_queda, sobran = rels[0], rels[1:]
        for r in sobran:
            os.remove(os.path.join(raiz, r))
            borrados.append((r, "copia identica", se_queda))

    # --- 3. carpetas que quedaron vacias -------------------------------------
    for dirpath, _, _ in sorted(os.walk(raiz), reverse=True):
        if dirpath != raiz and not os.listdir(dirpath):
            os.rmdir(dirpath)

    # --- 4. reporte ----------------------------------------------------------
    quedan = sum(len(n) for _, _, n in os.walk(raiz))
    peso = subprocess.run(["du", "-sh", raiz], capture_output=True, text=True)
    peso = peso.stdout.split()[0] if peso.returncode == 0 else "?"

    with open(reporte, "w", encoding="utf-8") as fh:
        fh.write("# Duplicados eliminados\n\n")
        fh.write(
            "Se compararon todos los archivos por huella SHA-256 de su contenido.\n"
            "De cada grupo de archivos identicos se dejo UNA copia y se borraron las\n"
            "demas. **No se perdio informacion**: aqui esta cada archivo borrado y la\n"
            "ruta de la copia que se conservo.\n\n"
        )
        fh.write(f"- Archivos antes: **{len(borrados) + quedan}**\n")
        fh.write(f"- Archivos despues: **{quedan}** ({peso})\n")
        fh.write(f"- Copias eliminadas: **{len(borrados)}**\n\n")

        if zips_borrados:
            fh.write("## Zips anidados eliminados\n\n")
            fh.write(
                "Cada uno era una copia comprimida de archivos que ya estan sueltos en\n"
                "el arbol. Se comprobo miembro por miembro antes de borrar: si a alguno\n"
                "le hubiera faltado aunque fuera un archivo, se habria conservado entero.\n\n"
            )
            for rel, n in sorted(zips_borrados):
                fh.write(f"- `{rel}` ({n} archivos, todos presentes sueltos)\n")
            fh.write("\n")

        fh.write("## Copias identicas eliminadas\n\n")
        fh.write("| Se borro | Se conserva |\n|---|---|\n")
        for r, motivo, queda in sorted(borrados):
            if motivo == "copia identica":
                fh.write(f"| `{r}` | `{queda}` |\n")

    # --- 5. mismo nombre, contenido distinto = versiones, no duplicados ------
    # Estas NO se borran: son versiones reales del documento y borrar una
    # perderia informacion. Pero hay que decir cual es la vigente, o quien
    # reciba el paquete no sabra cual de los cuatro MANUAL_PRODUCCION.md leer.
    if reporte_versiones:
        vivos = []
        for dirpath, _, nombres in os.walk(raiz):
            for n in nombres:
                vivos.append(os.path.relpath(os.path.join(dirpath, n), raiz))
        por_nombre = defaultdict(list)
        for rel in vivos:
            por_nombre[os.path.basename(rel)].append(rel)

        # Agrupar por nombre no basta: el .gitignore de recraft_ai y el de
        # youtube_pipeline comparten nombre y no tienen nada que ver. Solo
        # cuentan como versiones del mismo documento si su TEXTO se parece.
        familias = {}
        for nombre, rels in por_nombre.items():
            if len(rels) < 2:
                continue
            rels = sorted(rels, key=puntaje)
            canonico = lineas(os.path.join(raiz, rels[0]))
            if len(canonico) < 5:
                continue   # binario, vacio o demasiado corto para comparar de fiar
            juntos = [rels[0]]
            for rel in rels[1:]:
                otras = lineas(os.path.join(raiz, rel))
                if otras and parecido(canonico, otras) >= 0.3:
                    juntos.append(rel)
            if len(juntos) <= 1:
                continue
            # Cual es la vigente: las fechas no sirven (el zip de traslado las
            # reescribio todas al mismo dia), asi que se elige por contenido —
            # gana la version que CONTIENE a las demas, que es como crecen
            # estos documentos: se les va anadiendo seccion encima. A igualdad,
            # decide la ubicacion (documento vivo antes que snapshot).
            texto = {rel: lineas(os.path.join(raiz, rel)) for rel in juntos}
            def cobertura(rel):
                otras = set().union(*(texto[o] for o in juntos if o != rel))
                return len(texto[rel] & otras) / len(otras) if otras else 0.0
            familias[nombre] = sorted(
                juntos,
                key=lambda r: (es_snapshot(r), -round(cobertura(r), 3), puntaje(r)),
            )

        with open(reporte_versiones, "w", encoding="utf-8") as fh:
            fh.write("# Versiones del mismo documento\n\n")
            fh.write(
                "Estos archivos comparten nombre pero **su contenido es distinto**: son\n"
                "versiones reales, no copias, y por eso NO se borro ninguna. Lo que si\n"
                "hace falta es saber cual leer.\n\n"
                "**La marcada como VIGENTE es la version que contiene a las demas.** Las\n"
                "fechas de archivo no sirven para decidir (el zip de traslado las reescribio\n"
                "todas al mismo dia), asi que se compara el texto: estos documentos crecen\n"
                "anadiendo secciones encima, de modo que la version que incluye lo de las\n"
                "otras es la ultima. A igualdad decide la ubicacion — el documento vivo del\n"
                "repo o de la carpeta de trabajo gana al snapshot de un paquete de\n"
                "conocimiento o del envio a Kimi.\n\n"
                "Las marcadas como historico sirven para ver como evoluciono una decision,\n"
                "no para trabajar sobre ellas. **Si vas a editar, edita la VIGENTE.**\n\n"
            )
            for nombre in sorted(familias):
                rels = familias[nombre]
                fh.write(f"### `{nombre}`\n\n")
                for i, rel in enumerate(rels):
                    ruta = os.path.join(raiz, rel)
                    kb = os.path.getsize(ruta) / 1024
                    marca = "**VIGENTE**" if i == 0 else "historico"
                    fh.write(f"- {marca} — `{rel}` ({kb:,.1f} KB)\n")
                fh.write("\n")
        print(f"versiones con el mismo nombre: {len(familias)} documentos")

    print(f"quedan {quedan} archivos ({peso}); eliminadas {len(borrados)} copias")


if __name__ == "__main__":
    main()
