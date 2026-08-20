# -*- coding: utf-8 -*-
"""Produce videos en lote, de principio a fin y sin supervision.

Por cada video hace todo: audio -> video -> miniatura -> Short -> gemelo en
pantalla negra (si dura 3 h o mas) -> limpieza del audio intermedio.

Pensado para dejarlo corriendo de noche en tu PC:
  * Retoma donde se quedo: si el video ya existe, lo salta.
  * Un fallo no detiene el lote: lo anota y sigue con el siguiente.
  * Vigila el disco y se detiene antes de llenarlo, no despues.
  * Toma la materia prima de assets/origen si no esta en bases/ y salida/.

Uso:
  python3 scripts/05_lote.py --canal lakshmi
  python3 scripts/05_lote.py --canal lakshmi --desde 11 --hasta 20
  python3 scripts/05_lote.py --canal lakshmi --solo-negros
  python3 scripts/05_lote.py --canal lakshmi --lluvia -19 --min-libre 30
"""
import argparse, json, pathlib, shutil, subprocess, sys, time

BASE = pathlib.Path(__file__).resolve().parent.parent
CAT = json.loads((BASE / "datos" / "catalogo.json").read_text(encoding="utf-8"))
PY_ = sys.executable


def gb_libres():
    return shutil.disk_usage(BASE).free / 1e9


def preparar_insumos(v):
    """Copia musica e imagenes desde assets/origen si hacen falta."""
    base = BASE / "bases" / f"{v['id']}.wav"
    if not base.exists():
        orig = BASE / "assets" / "origen" / "musica" / f"{v['id']}.wav"
        if orig.exists():
            base.parent.mkdir(exist_ok=True)
            shutil.copy(orig, base)
    img_dir = BASE / "salida" / v["id"] / "img"
    if not img_dir.exists() or not any(img_dir.iterdir()):
        origs = sorted((BASE / "assets" / "origen" / "img").glob(f"{v['id']}-*"))
        if origs:
            img_dir.mkdir(parents=True, exist_ok=True)
            for o in origs:
                shutil.copy(o, img_dir / o.name)
    return base, img_dir


def corre(args, etiqueta):
    r = subprocess.run([PY_] + args, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"{etiqueta}: {r.stderr.strip().splitlines()[-1] if r.stderr.strip() else 'fallo'}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--canal", required=True)
    ap.add_argument("--desde", type=int, default=1)
    ap.add_argument("--hasta", type=int, default=99)
    ap.add_argument("--lluvia", type=float, default=0,
                    help="capa de lluvia en dB, p.ej. -19 (recomendado en los de sueno)")
    ap.add_argument("--solo-negros", action="store_true",
                    help="solo los gemelos en pantalla negra de los videos de 3 h o mas")
    ap.add_argument("--min-libre", type=float, default=15,
                    help="GB libres minimos para empezar un video (por defecto 15)")
    ap.add_argument("--conservar-audio", action="store_true",
                    help="no borrar el audio.flac intermedio al terminar")
    a = ap.parse_args()

    canal = next((c for c in CAT["canales"] if c["slug"] == a.canal), None)
    if not canal:
        sys.exit("canal invalido: lakshmi, ganesha o uriel")

    hechos, saltados, fallidos = [], [], []
    t0 = time.time()

    for v in canal["videos"]:
        if not (a.desde <= v["n"] <= a.hasta):
            continue
        if a.solo_negros and v["horas"] < 3:
            continue

        d = BASE / "salida" / v["id"]
        final = d / (f"{v['id']}-negro.mp4" if a.solo_negros else f"{v['id']}.mp4")
        if final.exists():
            saltados.append(v["id"]); continue

        if gb_libres() < a.min_libre:
            print(f"\n[!] Quedan {gb_libres():.1f} GB libres, menos del minimo de "
                  f"{a.min_libre} GB. Se detiene aqui para no llenar el disco.")
            print("    Libera espacio o baja el limite con --min-libre.")
            break

        base, img_dir = preparar_insumos(v)
        if not base.exists():
            fallidos.append((v["id"], "falta la musica base")); continue
        if not img_dir.exists() or len(list(img_dir.glob("*"))) < 3:
            fallidos.append((v["id"], "hacen falta al menos 3 imagenes")); continue

        t1 = time.time()
        print(f"\n=== {v['id']}  ({v['horas']} h, {v['hz']} Hz)  ·  {gb_libres():.0f} GB libres")
        try:
            audio = next((d / f"audio{e}" for e in (".flac", ".wav") if (d / f"audio{e}").exists()), None)
            if not audio:
                cmd = ["scripts/03_audio.py", "--id", v["id"], "--base", str(base)]
                if a.lluvia:
                    cmd += ["--lluvia", str(a.lluvia)]
                print("  audio..."); corre(cmd, "audio")

            if a.solo_negros:
                print("  pantalla negra..."); corre(["scripts/04_video.py", "--id", v["id"], "--negro"], "video negro")
            else:
                print("  video...");     corre(["scripts/04_video.py", "--id", v["id"]], "video")
                primera = sorted(img_dir.glob("*"))[0]
                print("  miniatura..."); corre(["scripts/06_miniatura.py", "--id", v["id"],
                                                "--img", str(primera)], "miniatura")
                print("  short...");     corre(["scripts/08_short.py", "--id", v["id"], "--seg", "45"], "short")
                if v["horas"] >= 3:
                    print("  gemelo negro..."); corre(["scripts/04_video.py", "--id", v["id"], "--negro"], "video negro")

            if not a.conservar_audio:
                for e in (".flac", ".wav"):
                    (d / f"audio{e}").unlink(missing_ok=True)
            hechos.append(v["id"])
            print(f"  LISTO en {(time.time()-t1)/60:.1f} min")
        except Exception as e:
            fallidos.append((v["id"], str(e)))
            print(f"  FALLO -> {e}")

    print(f"\n{'='*52}")
    print(f"Terminados: {len(hechos)}   Ya existian: {len(saltados)}   Fallidos: {len(fallidos)}")
    print(f"Tiempo total: {(time.time()-t0)/60:.0f} min   ·   {gb_libres():.0f} GB libres")
    if hechos:
        print("  OK: " + ", ".join(hechos))
    if fallidos:
        print("  Revisar:")
        for vid, motivo in fallidos:
            print(f"    - {vid}: {motivo}")


if __name__ == "__main__":
    main()
