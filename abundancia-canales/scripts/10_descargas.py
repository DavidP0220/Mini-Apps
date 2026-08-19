# -*- coding: utf-8 -*-
"""Construye la pagina de descargas a partir de los FUENTES.md de cada video.

Se genera desde los archivos reales para que nunca se desincronice:
si produces un video nuevo, vuelves a correr esto y la pagina se actualiza.

Uso: python3 scripts/10_descargas.py
"""
import json, pathlib, re, html

BASE = pathlib.Path(__file__).resolve().parent.parent
CAT = json.loads((BASE / "datos" / "catalogo.json").read_text(encoding="utf-8"))


def leer_fuentes():
    """Extrae de cada FUENTES.md la musica y las imagenes."""
    items = []
    for f in sorted(BASE.glob("salida/*/FUENTES.md")):
        vid = f.parent.name
        txt = f.read_text(encoding="utf-8")
        musica = re.search(r"(https://ai-music-tracks\.s3[^\s]+\.wav)", txt)
        imgs = re.findall(r"(https://ai-thumbnails\.s3[^\s]+\.png)", txt)
        datos = None
        for c in CAT["canales"]:
            for v in c["videos"]:
                if v["id"] == vid:
                    datos = (c, v)
        if datos:
            items.append({"id": vid, "canal": datos[0], "v": datos[1],
                          "musica": musica.group(1) if musica else None,
                          "imgs": imgs})
    return items


def fila(i, it):
    v, canal = it["v"], it["canal"]
    enlaces = []
    if it["musica"]:
        enlaces.append(("Música base", it["musica"], "wav"))
    for n, u in enumerate(it["imgs"], 1):
        enlaces.append((f"Imagen {n}", u, "png"))
    li = "\n".join(
        f'''<li class="asset">
              <a class="asset-link" href="{html.escape(u)}" target="_blank" rel="noopener">
                <span class="asset-name">{html.escape(nombre)}</span>
                <span class="asset-kind">{kind}</span>
              </a>
              <button class="copy" type="button" data-url="{html.escape(u)}"
                      aria-label="Copiar enlace de {html.escape(nombre)}">Copiar</button>
            </li>''' for nombre, u, kind in enlaces)
    return f'''<article class="video" id="{it['id']}">
  <div class="video-head">
    <span class="idx">{i:02d}</span>
    <div class="video-meta">
      <h3>{html.escape(v['titulo_corto'])}</h3>
      <p class="titulo-yt">{html.escape(v['titulo_yt'])}</p>
      <p class="chips">
        <span class="chip chip-hz">{v['hz']} Hz</span>
        <span class="chip">{v['horas']} h</span>
        <span class="chip chip-quiet">{html.escape(v['bloque'])}</span>
      </p>
    </div>
  </div>
  <ul class="assets">{li}</ul>
</article>'''


def main():
    items = leer_fuentes()
    filas = "\n".join(fila(i, it) for i, it in enumerate(items, 1))
    total_img = sum(len(i["imgs"]) for i in items)
    pagina = PLANTILLA.format(filas=filas, n=len(items), n_img=total_img,
                              n_arch=total_img + sum(1 for i in items if i["musica"]))
    out = BASE / "descargas" / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(pagina, encoding="utf-8")
    print(f"OK -> {out}  ({len(items)} videos, {total_img} imagenes)")


PLANTILLA = r"""<title>Bóveda Maha Lakshmi</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=Karla:wght@400;500;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
:root {{
  --ground: #EFEDF2;
  --surface: #FFFFFF;
  --surface-2: #F6F4F9;
  --ink: #171526;
  --ink-soft: #4E4A63;
  --ink-faint: #7C7791;
  --gold: #8A6510;
  --gold-soft: #C9A94E;
  --line: #DCD8E4;
  --focus: #3B2E7E;
  --shadow: 0 1px 2px rgba(23,21,38,.06), 0 8px 24px -12px rgba(23,21,38,.18);
}}
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
    --ground: #12101C;
    --surface: #1B1830;
    --surface-2: #221E3A;
    --ink: #EDEAF6;
    --ink-soft: #B6B0CD;
    --ink-faint: #857FA0;
    --gold: #E8B84B;
    --gold-soft: #8A6510;
    --line: #2E2950;
    --focus: #A99BFF;
    --shadow: 0 1px 2px rgba(0,0,0,.4), 0 10px 30px -14px rgba(0,0,0,.7);
  }}
}}
:root[data-theme="dark"] {{
  --ground: #12101C;
  --surface: #1B1830;
  --surface-2: #221E3A;
  --ink: #EDEAF6;
  --ink-soft: #B6B0CD;
  --ink-faint: #857FA0;
  --gold: #E8B84B;
  --gold-soft: #8A6510;
  --line: #2E2950;
  --focus: #A99BFF;
  --shadow: 0 1px 2px rgba(0,0,0,.4), 0 10px 30px -14px rgba(0,0,0,.7);
}}

* {{ box-sizing: border-box; }}
body {{
  margin: 0;
  background: var(--ground);
  color: var(--ink);
  font: 400 17px/1.6 Karla, system-ui, sans-serif;
  -webkit-font-smoothing: antialiased;
}}
.wrap {{ max-width: 60rem; margin: 0 auto; padding: clamp(1.5rem, 4vw, 4rem) clamp(1rem, 4vw, 2rem) 6rem; }}

header.top {{ display: flex; flex-direction: column; gap: .9rem; margin-bottom: 2.5rem; }}
.eyebrow {{
  font: 500 .78rem/1 "IBM Plex Mono", ui-monospace, monospace;
  letter-spacing: .14em; text-transform: uppercase; color: var(--gold); margin: 0;
}}
h1 {{
  font: 600 clamp(2.1rem, 6vw, 3.4rem)/1.05 Fraunces, Georgia, serif;
  margin: 0; text-wrap: balance; letter-spacing: -.015em;
}}
.lede {{ margin: 0; max-width: 46ch; color: var(--ink-soft); font-size: 1.05rem; }}

.alert {{
  display: flex; gap: .85rem; align-items: flex-start;
  border: 1px solid var(--line); border-left: 3px solid var(--gold);
  background: var(--surface); border-radius: 4px; padding: 1rem 1.15rem;
  box-shadow: var(--shadow); margin: 2rem 0 2.5rem;
}}
.alert p {{ margin: 0; font-size: .96rem; color: var(--ink-soft); }}
.alert strong {{ color: var(--ink); }}

.stats {{ display: flex; flex-wrap: wrap; gap: 2rem; padding: 1.25rem 0; border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); margin-bottom: 3rem; }}
.stat b {{ display: block; font: 500 1.7rem/1 "IBM Plex Mono", monospace; font-variant-numeric: tabular-nums; color: var(--ink); }}
.stat span {{ font-size: .82rem; color: var(--ink-faint); letter-spacing: .04em; }}

h2 {{
  font: 600 1.45rem/1.2 Fraunces, Georgia, serif; margin: 3rem 0 .4rem;
  letter-spacing: -.01em;
}}
.section-note {{ margin: 0 0 1.5rem; color: var(--ink-faint); font-size: .95rem; max-width: 52ch; }}

.video {{
  background: var(--surface); border: 1px solid var(--line); border-radius: 6px;
  padding: 1.25rem 1.35rem; margin-bottom: 1rem; box-shadow: var(--shadow);
}}
.video-head {{ display: flex; gap: 1.1rem; align-items: flex-start; }}
.idx {{
  font: 500 .95rem/1 "IBM Plex Mono", monospace; color: var(--gold);
  padding-top: .35rem; font-variant-numeric: tabular-nums;
}}
.video-meta {{ min-width: 0; display: flex; flex-direction: column; gap: .35rem; }}
.video h3 {{ font: 600 1.22rem/1.25 Fraunces, Georgia, serif; margin: 0; letter-spacing: -.01em; }}
.titulo-yt {{
  margin: 0; font: 400 .84rem/1.45 "IBM Plex Mono", monospace;
  color: var(--ink-faint); word-break: break-word;
}}
.chips {{ display: flex; flex-wrap: wrap; gap: .4rem; margin: .3rem 0 0; }}
.chip {{
  font: 500 .74rem/1 "IBM Plex Mono", monospace; letter-spacing: .05em;
  padding: .38rem .6rem; border-radius: 3px; background: var(--surface-2);
  color: var(--ink-soft); border: 1px solid var(--line);
}}
.chip-hz {{ color: var(--gold); border-color: var(--gold-soft); }}
.chip-quiet {{ text-transform: none; letter-spacing: .02em; }}

.assets {{ list-style: none; margin: 1.1rem 0 0; padding: 0; display: grid; gap: .4rem; }}
.asset {{ display: flex; gap: .5rem; align-items: stretch; }}
.asset-link {{
  flex: 1; display: flex; justify-content: space-between; align-items: center; gap: 1rem;
  padding: .6rem .8rem; border: 1px solid var(--line); border-radius: 4px;
  background: var(--surface-2); color: var(--ink); text-decoration: none;
  transition: border-color .15s, transform .15s;
}}
.asset-link:hover {{ border-color: var(--gold); transform: translateX(2px); }}
.asset-name {{ font-size: .93rem; font-weight: 500; }}
.asset-kind {{ font: 400 .72rem/1 "IBM Plex Mono", monospace; color: var(--ink-faint); text-transform: uppercase; letter-spacing: .1em; }}
.copy {{
  font: 500 .78rem/1 Karla, sans-serif; padding: 0 .8rem; cursor: pointer;
  border: 1px solid var(--line); border-radius: 4px; background: var(--surface);
  color: var(--ink-soft); transition: border-color .15s, color .15s;
}}
.copy:hover {{ border-color: var(--gold); color: var(--gold); }}
.copy[data-done="1"] {{ color: var(--gold); border-color: var(--gold); }}
a:focus-visible, button:focus-visible {{ outline: 2px solid var(--focus); outline-offset: 2px; }}

.steps {{ counter-reset: s; list-style: none; padding: 0; margin: 0; display: grid; gap: .9rem; }}
.steps li {{ display: flex; gap: .9rem; }}
.steps li::before {{
  counter-increment: s; content: counter(s);
  font: 500 .8rem/1 "IBM Plex Mono", monospace; color: var(--gold);
  border: 1px solid var(--gold-soft); border-radius: 50%;
  width: 1.8rem; height: 1.8rem; display: grid; place-items: center; flex: none;
}}
pre {{
  background: var(--surface); border: 1px solid var(--line); border-radius: 4px;
  padding: 1rem; overflow-x: auto; font: 400 .84rem/1.7 "IBM Plex Mono", monospace;
  color: var(--ink-soft); margin: 1rem 0 0;
}}
footer {{ margin-top: 4rem; padding-top: 1.5rem; border-top: 1px solid var(--line); color: var(--ink-faint); font-size: .86rem; }}
@media (prefers-reduced-motion: reduce) {{ * {{ transition: none !important; }} }}
</style>

<div class="wrap">
  <header class="top">
    <p class="eyebrow">Maha Lakshmi Sanctuary</p>
    <h1>Bóveda de producción</h1>
    <p class="lede">La materia prima de los {n} videos ya producidos: música original y arte de fondo, listos para descargar y reconstruir en tu equipo.</p>
  </header>

  <div class="alert">
    <p><strong>Descarga esto pronto.</strong> Los archivos están alojados temporalmente y los enlaces pueden caducar. Los videos armados —de 500&nbsp;MB a 3,3&nbsp;GB— no se guardan en ningún lado: se reconstruyen desde aquí en unos minutos.</p>
  </div>

  <div class="stats">
    <div class="stat"><b>{n}</b><span>VIDEOS PRODUCIDOS</span></div>
    <div class="stat"><b>{n_arch}</b><span>ARCHIVOS DE ORIGEN</span></div>
    <div class="stat"><b>{n_img}</b><span>IMÁGENES</span></div>
  </div>

  <h2>Archivos por video</h2>
  <p class="section-note">Cada enlace abre en una pestaña nueva; desde ahí guarda el archivo. En el celular es más cómodo usar «Copiar» y pegar el enlace en tu gestor de descargas.</p>
  {filas}

  <h2>Cómo reconstruir un video</h2>
  <p class="section-note">Necesitas ffmpeg y Python con Pillow. Todo el proceso es automático.</p>
  <ol class="steps">
    <li>Guarda la música como <code>bases/&lt;id&gt;.wav</code> y las imágenes en <code>salida/&lt;id&gt;/img/</code>.</li>
    <li>Amplía las imágenes a 2560&nbsp;px de ancho antes de renderizar.</li>
    <li>Corre los cuatro comandos en orden.</li>
  </ol>
  <pre>python3 scripts/03_audio.py --id lakshmi-01 --base bases/lakshmi-01.wav
python3 scripts/04_video.py --id lakshmi-01
python3 scripts/06_miniatura.py --id lakshmi-01 --img salida/lakshmi-01/img/1.png
python3 scripts/08_short.py --id lakshmi-01 --seg 45</pre>

  <footer>
    Toda la música es original y libre de regalías. El arte fue generado para este proyecto.
    Página generada desde los archivos <code>FUENTES.md</code> del repositorio.
  </footer>
</div>

<script>
document.querySelectorAll('.copy').forEach(function (b) {{
  b.addEventListener('click', function () {{
    navigator.clipboard.writeText(b.dataset.url).then(function () {{
      b.textContent = 'Copiado';
      b.dataset.done = '1';
      setTimeout(function () {{ b.textContent = 'Copiar'; b.dataset.done = ''; }}, 1800);
    }});
  }});
}});
</script>
"""

if __name__ == "__main__":
    main()
