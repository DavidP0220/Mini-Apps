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

---

## 7. Análisis del canal de referencia (datos reales, vidIQ · 18/08/2026)

Video de referencia: *"MÚSICA para ATRAER MUCHO DINERO | AMOR Y ATRAER BUENA SUERTE"* — canal
**Paco Jarab** (México). El análisis cambió tres decisiones del proyecto.

**El canal:** 268.000 suscriptores · 1.121 videos · 34,9 M de vistas totales ·
~852.000 vistas en los últimos 30 días · 24 videos publicados al mes.

**El video:** 2 h 59 min · 6.545.598 vistas · publicado en 2020 y todavía sumando 44 vistas/hora.
Ingreso estimado del video: **$1.767 – $4.712 USD** en toda su vida.

### Lo que confirma nuestro plan
- Su ritmo es de ~24 videos/mes. El nuestro es de 20 por canal: sostenible y comparable.
- El catálogo es el activo: un video de 2020 sigue generando vistas seis años después.
- Los códigos sagrados (71588, 897) y las frecuencias son temas validados — ya están en
  nuestro catálogo del canal Uriel.

### Lo que corregimos con estos datos
1. **La duración de 1 hora manda hoy, no las de 3–8 h.** Sus videos con más velocidad de
   vistas son todos de exactamente 1 hora (35 a 63 vistas/hora), mientras que los de 3 h
   son de 2020. Reajustamos el catálogo: **23 videos de 1 h, 18 de 3 h y 19 de 8 h**
   (los de 8 h se conservan para la búsqueda de sueño, que es otro nicho distinto).
2. **"Pantalla oscura" es su formato campeón.** Su video de pantalla oscura tiene
   **77 vistas/hora**, el más alto del canal. Por eso `04_video.py` ahora tiene la
   opción `--oscuro`: misma producción, versión atenuada para dormir. Son dos videos
   con un solo trabajo.
3. **El idioma vale dinero.** Su RPM real es de ~$0,45 por cada 1.000 vistas porque su
   audiencia es de México. Nuestro contenido en inglés apunta a **$1,50–$4,00**: el mismo
   esfuerzo, entre 3 y 8 veces más ingreso por vista.

### Volumen de búsqueda real (vidIQ, mercado US) — ya aplicado a las etiquetas
| Palabra clave | Búsquedas/mes | Competencia |
|---|---|---|
| meditation music | 2.404.964 | 43,5 |
| binaural beats | 1.094.796 | 53,4 |
| law of attraction | 689.877 | 57,5 |
| 432 hz | 586.178 | 62,2 |
| 888 hz frequency | 133.004 | 41,5 |
| abundance frequency | 92.940 | **43,0** |

`abundance frequency` es la mejor oportunidad: alto volumen, competencia media y la mayor
proporción de búsquedas en Estados Unidos (28%), que es el país que mejor paga.

### Formato de título que le funciona a él (y que ya replicamos)
`GANCHO EN MAYÚSCULAS + emoji + beneficio concreto + duración`
Ejemplo suyo: *"ONDAS THETA 🧬 para DINERO | SALDO MILLONARIO DISPONIBLE 💲 (1 Hora)"*
Nuestro equivalente: *"Lakshmi's Infinite Wealth Current 💸 Non-Stop Money Flow • 888 Hz • 1 Hour"*

> Una advertencia honesta: su canal tardó de 2014 a hoy en llegar ahí, con 1.121 videos.
> No es dinero rápido. Es un catálogo que se acumula.

---

## 8. Decisiones tomadas tras el análisis de la competencia en inglés

Ver el detalle completo en `datos/competencia.md`. Estas tres decisiones ya están
aplicadas al catálogo y a los 60 paquetes:

**1. Los títulos empiezan por la frecuencia.** Es la fórmula de los canales que están
ganando en inglés hoy: la frecuencia es lo que la gente busca, la deidad es la identidad
del canal. Los 60 títulos son únicos y ninguno pasa de 96 caracteres.

Antes: `The Golden River of Lakshmi 💰 Activate Miracles & Heart-Centered Wealth • 528 Hz • 1 Hour`
Ahora: `528 Hz The Golden River of Lakshmi 💰 Unlock Miracles & Heart-Centered Wealth • 1 Hour`

Cada frecuencia tiene **tres promesas** que rotan, para que veinte videos seguidos no
parezcan la misma plantilla (YouTube penaliza el contenido repetitivo).

**2. Reparto de frecuencias cargado hacia el dinero.** 888 Hz es la frecuencia dominante
del nicho en inglés, seguida de 777 y 963. 432 Hz se reservó para los videos de 8 horas,
que es donde de verdad rinde (sueño).

| Frecuencia | Videos | Para qué |
|---|---|---|
| 888 Hz | 14 | Flujo de dinero — la reina del nicho |
| 528 Hz | 11 | Milagros y transformación |
| 432 Hz | 9 | Solo videos de 8 h (sueño) |
| 777 Hz | 9 | Suerte divina y puertas |
| 963 Hz | 6 | Sabiduría y guía |
| 396 Hz | 5 | Soltar el miedo a la escasez |
| 741 / 417 / 1111 Hz | 6 | Protección, reinicio y portal |

**3. Ritmo: 20 videos al mes por canal.** Es el modelo de *Zen Harmony Sounds*
(+313% de suscriptores en un año) y *Soul Healing Journey* (+89% de vistas en 30 días).
Publicar seguido acelera el arranque; una vez que el canal despegue podemos bajar el
ritmo y subir la calidad, que es el modelo de *Soothing Harmony*.

---

## 9. Cambios técnicos importantes (revisión del 19/08)

**El bucle de audio ya no tiene saltos.** El script calculaba un crossfade pero no lo
aplicaba: pegaba la pista consigo misma con un corte seco, así que cada 2-3 minutos
habría habido un salto audible. En un video de 8 horas son más de 150 saltos y eso
arruina la retención. Ahora se funde la cola de la pista con su propia cabeza, y esa
"unidad" empalma consigo misma de forma inaudible.

**El audio intermedio ahora es FLAC**, no WAV. Sin pérdida de calidad y menos peso.
Aun así, ten en cuenta el espacio en disco:

| Duración | audio.flac | video final .mp4 |
|---|---|---|
| 1 hora | ~600 MB | ~500 MB |
| 3 horas | ~1,8 GB | ~1,5 GB |
| 8 horas | ~4,5 GB | ~4 GB |

Borra el `audio.flac` después de renderizar el mp4: ya no lo necesitas.

**Nuevo: Shorts.** `scripts/08_short.py` genera un Short vertical (1080x1920, hasta
60 s) con los mismos insumos del video largo:

```bash
python3 scripts/08_short.py --id lakshmi-01
```

Lleva el texto de la miniatura, la frecuencia, una afirmación y, en los últimos 12
segundos, un llamado al video completo. **Publica 2 o 3 Shorts por cada video largo**:
son el motor de descubrimiento y lo que acelera los primeros 1.000 suscriptores.

**Nuevo: marca de canal.** `scripts/07_marca.py` convierte cualquier imagen en avatar
de 800x800 y banner de 2560x1440 respetando el área segura de YouTube. Los seis
archivos de los tres canales ya están hechos en `assets/marca/`.

### Orden de trabajo por video (actualizado)
```bash
python3 scripts/03_audio.py --id lakshmi-01 --base bases/lakshmi-01.wav
python3 scripts/04_video.py --id lakshmi-01
python3 scripts/06_miniatura.py --id lakshmi-01 --img salida/lakshmi-01/img/1.png
python3 scripts/08_short.py --id lakshmi-01
rm salida/lakshmi-01/audio.flac
```

---

## 10. El camino real a la monetización

YouTube pide dos cosas en 12 meses: **1.000 suscriptores** y **4.000 horas de
reproducción**. Al hacer la cuenta aparece algo que cambia toda la estrategia.

| Requisito | Cálculo | Vistas necesarias |
|---|---|---|
| 4.000 horas de reproducción | 240.000 min ÷ 25 min de retención media | **9.600** |
| 1.000 suscriptores | conversión típica del nicho, ~1,5% | **66.667** |

**Se necesitan siete veces más vistas para los suscriptores que para las horas.**

Esto es específico de nuestro formato: con videos de 3 a 8 horas, una sola persona
que se duerme con el video puesto aporta 8 horas de reproducción. Las horas llegan
solas. Los suscriptores no: alguien que duerme con tu video no se suscribe.

### Qué se hace con esa información

**1. Los Shorts no son un extra, son el motor.** Son lo único que convierte
espectadores en suscriptores a ritmo alto. Por eso el calendario pone un Short
por cada video largo, el mismo día.

**2. Las listas de reproducción son la palanca más barata para las horas.**
Al terminar un video arranca el siguiente sin que nadie haga nada. Crea estas
cuatro antes de publicar:

| Lista | Contenido |
|---|---|
| Sleep Frequencies (Black Screen) | Los gemelos en pantalla negra |
| 8 Hour Deep Sleep | Los videos de 8 horas |
| 888 Hz Money Frequency | Todos los de 888 Hz |
| Morning Abundance Ritual | Los de 1 hora |

Ponlas en la **pantalla final** de cada video y como **primer enlace de la descripción**.

**3. El comentario fijado tiene que pedir la suscripción**, no solo interacción.
Los paquetes ya lo traen escrito.

**4. Publica a la hora del público que paga.** El calendario usa hora del este de
EE.UU.: los videos de sueño a las 21:00, los de una hora a las 07:00 y los Shorts
a las 12:00.

### El calendario ya está hecho

```bash
python3 scripts/12_calendario.py --canal lakshmi --desde 2026-09-01
```

Genera `salida/_calendario/calendario-<canal>.md` con **fecha y hora exactas de cada
publicación**: 52 para Lakshmi, 55 para Ganesha y 56 para Uriel. Respeta la regla de
que un video y su gemelo negro nunca compitan el mismo día.

Ajusta la retención estimada con `--retencion 22` cuando tengas datos reales de tu
canal; el cálculo se rehace solo.

> Una advertencia honesta sobre el 1,5% de conversión: es una cifra típica del nicho,
> no una promesa. Puede ser 0,8% o 3% según lo bien que funcionen tus Shorts y tu
> marca. Por eso el plan es medir a los 30 días y ajustar, no asumir.
