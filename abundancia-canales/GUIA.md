# GUÍA MAESTRA — Red de Canales de Abundancia

Todo en español. Los textos que van en YouTube están en inglés (mercado global = mayor RPM)
y están listos para copiar en `salida/<canal>/<id>.md`.

---

## 1. Qué construimos y por qué así

Tres canales **hiperenfocados** en vez de uno genérico. YouTube premia la especialización:
cada canal entrena su propio algoritmo, su propia audiencia y su propio nicho de búsqueda.

| Canal | Deidad | Promesa | Momento de consumo |
|---|---|---|---|
| Maha Lakshmi Sanctuary | Goddess Maha Lakshmi | Riqueza, fortuna, prosperidad | Mañana / trabajo |
| Lord Ganesha 432Hz | Lord Ganesha | Abrir caminos, negocios, quitar bloqueos | Mañana / antes de trabajar |
| Archangel Uriel Divine Light | Archangel Uriel | Provisión divina, paz, dormir | Noche / sueño (8 h) |

Ritmo: **1 video cada 36 horas por canal → 20 videos/mes por canal → 60 al mes.**

---

## 2. Las herramientas (mínimo costo, máxima capacidad)

| Función | Herramienta | Costo | Por qué |
|---|---|---|---|
| Música base | **Suno Pro** | ~$10/mes | 500 canciones/mes en modo instrumental, licencia comercial |
| Alternativa | Soundful | ~$59/año | Loops limpios sin voz, licencia comercial |
| Frecuencia pura | **ffmpeg** (nuestro script) | Gratis | Capa senoidal exacta 432/528/888 Hz, sin pagar nada |
| Bucle a 3–8 h | **ffmpeg** (nuestro script) | Gratis | Crossfade de 12 s, sin cortes audibles |
| Imágenes | **Leonardo.ai** (gratis 150/día) o Midjourney ($10) | $0–10 | 5 imágenes por video = 300/mes |
| Escalado 4K | Upscayl | Gratis | Opcional |
| Render de video | **ffmpeg** (nuestro script) | Gratis | Ken Burns + afirmaciones + bucle |
| Miniatura | **Pillow** (nuestro script) | Gratis | 1280x720 con texto dorado automático |
| Control | `panel/index.html` | Gratis | Estado de los 60 videos |

**Presupuesto real: entre $10 y $20 al mes.** Todo lo demás es nuestro código.

> Sobre TopMedia.ai: no sirve para este proyecto. Genera pistas de 1–3 min con sistema de
> créditos caro para 60 videos/mes. Suno + nuestro script hace lo mismo por menos.

---

## 3. Flujo de trabajo real (lo que haces tú y lo que hace el sistema)

### Paso 0 — Una sola vez
1. Instala ffmpeg: Windows `winget install Gyan.FFmpeg` · Mac `brew install ffmpeg`.
2. Instala Pillow: `pip install Pillow`.
3. Crea los 3 canales de YouTube (Google no permite que yo lo haga por ti).
4. Genera avatar y banner con los prompts de `datos/branding.md`.

### Paso 1 — Música base (tú, ~15 min por canal)
En Suno, modo **Instrumental**, genera una pista de 2–5 min por video y guárdala como
`bases/<id>.wav` (ejemplo: `bases/lakshmi-01.wav`). Prompt sugerido en `datos/branding.md`.

**Truco de escala:** una misma base sirve para 2–3 videos si cambias la frecuencia
superpuesta y las imágenes. Con 8 bases por canal cubres los 20 videos del mes.

### Paso 2 — Imágenes (tú, ~10 min por video)
Abre `salida/<canal>/<id>.md`, copia los 5 prompts, genera las imágenes y guárdalas en
`salida/<id>/img/`. Deben ser 5 o más para que el ciclo visual no se sienta repetido
(YouTube penaliza el contenido repetitivo: por eso variamos imágenes, textos y duración).

### Paso 3 — Render (automático)
```bash
python3 scripts/03_audio.py --id lakshmi-01 --base bases/lakshmi-01.wav --prueba 60   # vista previa
python3 scripts/03_audio.py --id lakshmi-01 --base bases/lakshmi-01.wav               # final
python3 scripts/04_video.py --id lakshmi-01
python3 scripts/06_miniatura.py --id lakshmi-01 --img salida/lakshmi-01/img/1.png
```
O todo el canal de una vez: `python3 scripts/05_lote.py --canal lakshmi`

### Paso 4 — Subida (tú, ~6 min por video)
Sigue el checklist al final de cada `.md`. Programa el video (no lo publiques manual):
así trabajas un día y publicas dos semanas.

---

## 4. Cómo hacerlo BRUTAL (lo que separa un canal de $50/mes de uno de $5.000/mes)

1. **Multiplica por formato, no por trabajo.** Cada pista larga te da además:
   - 3 Shorts verticales de 45 s (mismo audio + una imagen animada) → los Shorts alimentan al canal largo.
   - 1 versión "1 hora" y 1 versión "8 horas" del mismo tema → dos videos, un solo render.
2. **Domina la búsqueda de sueño.** Los videos de 8 h en el canal Uriel capturan
   "sleep music" — la categoría con más horas vistas de YouTube. La retención por sesión es
   lo que dispara el RPM.
3. **Publica a la hora correcta.** Uriel: 20:00–22:00 hora de EE.UU. (sueño).
   Lakshmi/Ganesha: 6:00–8:00 (rutina de la mañana). Programa en esas franjas.
4. **Ingresos que no dependen de AdSense** (esto es lo que multiplica de verdad):
   - **Venta del audio en Bandcamp/Gumroad**: pack de 20 pistas por $9. Ya lo tienes producido.
   - **Distribución a Spotify/Apple** vía DistroKid (~$20/año, ilimitado): la misma música
     genera regalías en streaming 24/7 sin volver a trabajar. Este es el mayor error que
     comete el 95% de estos canales: dejan el dinero solo en YouTube.
   - **Mini-app de rituales de abundancia** (¡ya tienes el motor en este repo!): un
     acompañamiento de 21 días para vender en Hotmart con enlace en la descripción.
   - **Membresías de canal** y videos exclusivos para miembros.
   - **Afiliados**: audífonos, cuencos tibetanos, velas — enlace en la descripción.
5. **La marca, no solo el video.** Mismo avatar, mismo color, misma tipografía en las 60
   miniaturas. Una red reconocible se suscribe 3× más que canales sueltos.
6. **Idioma:** todo en inglés. El mismo video en inglés paga entre 3 y 5 veces más
   que en español. Por eso los paquetes vienen en inglés con instrucciones en español.

### Proyección realista (no promesas)
Un canal de música de este tipo suele tardar **3 a 6 meses** en monetizar (1.000 subs +
4.000 h de reproducción; con música larga las horas llegan rápido). RPM típico del nicho:
$1,5–$4 por cada 1.000 vistas, más alto en el contenido de sueño en EE.UU.
Con 3 canales y 60 videos/mes, el catálogo acumulado es el activo: el mes 12 sigue
generando ingresos por el mes 1. Es un negocio de **acumulación**, no de viralidad.

---

## 5. Reglas para no morir en el intento

- **Nunca uses música de otros.** Todo lo que produces con Suno/Soundful en plan de pago
  tiene licencia comercial. Guarda los comprobantes.
- **Evita "contenido repetitivo"** (motivo #1 de rechazo de monetización): varía imágenes,
  afirmaciones, duración y frecuencia entre videos. Nuestro catálogo ya lo hace por diseño.
- **No prometas curas ni resultados económicos garantizados.** La descripción ya incluye
  el descargo de responsabilidad; no lo quites.
- **Sube en 1080p mínimo.** Usa `--4k` solo si tu PC lo aguanta; no cambia el ingreso.
- **Respaldo:** guarda `bases/` y `salida/*/img/` en Drive. Es tu materia prima.

---

## 6. Reparto del trabajo

| Yo (asistente) | Tú |
|---|---|
| Catálogo, títulos, descripciones, tags, prompts, afirmaciones | Crear las cuentas de YouTube y de Suno |
| Scripts de audio, video y miniaturas | Generar las bases musicales y las imágenes |
| Panel de control y checklists | Pegar los textos y subir/programar los videos |
| Ajustar títulos y estrategia según los datos que me pases | Pasarme las métricas cada semana |

Cuando tengas la primera base musical y las primeras 5 imágenes, dímelo y renderizamos
juntos el primer video completo.
