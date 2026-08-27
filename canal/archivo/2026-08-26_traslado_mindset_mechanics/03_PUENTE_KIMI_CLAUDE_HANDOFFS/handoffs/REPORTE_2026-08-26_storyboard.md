# REPORTE — Storyboard Director · 2026-08-26

**Rol:** dirección de storyboard (investigación diaria + auditoría del storyboard en producción).
**Créditos consumidos: 0.** No se generó ninguna imagen ni ningún video. No se tocó el navegador.
**Producto de hoy: documentos.**

---

## 1. Qué se investigó (web, agosto 2026)

Tres frentes, contrastando fuentes distintas en cada uno:

1. **Cómo evitan otros creadores las regeneraciones caras por mala planificación visual.**
   Convergen en dos cosas: bloquear TODAS las referencias antes de generar escenas
   (*"consistency re-rolls burn more credits than anything else"*) y el orden imagen-aprobada→
   movimiento (*"consistency problems are cheap to fix in an image and expensive to fix across
   generated footage"*). Dato de economía: **~3 generaciones por plano usable, ~25% de tasa de
   selección**, y **68% de los usuarios agotan créditos a mitad de proyecto**.
2. **Ritmo de corte en documental.** El hallazgo relevante NO es una cifra de ASL: es que
   **la variación intencional de ritmo importa más que la velocidad de corte**. Patrones
   ejecutables: progresivo, respiración, ráfaga. Densidad de referencia documental 5-10
   cortes/min. Caso citado: MrBeast revirtiendo el corte-cada-segundo en 2024 y subiendo vistas.
3. **Storyboard que un generador de imágenes pueda seguir sin ambigüedad.** Descomposición
   por capas (foreground/midground/background) declarada explícitamente; es el mismo principio
   detrás de los captions JSON estructurados con los que se entrenó Ideogram 4.0
   (*"JSON prompting removes guesswork by giving every element its own named key"*).

**Limitación honesta:** el proxy de red bloqueó la descarga directa de todos los dominios
(`air.io`, `invideo.io`, `studiobinder.com`, `vidpros.com`, `myup.ai` → `EGRESS_BLOCKED`). Todo
está construido sobre los extractos devueltos por la búsqueda, no sobre el artículo completo.
Las cifras concretas convergen entre fuentes distintas pero **no están verificadas contra el
texto íntegro**. Queda anotado también en `MANUAL_PRODUCCION.md` §3.2.5.

---

## 2. Qué se mejoró

### `PROYECTO MECHANICS OPTIMIZACIONES/MANUAL_PRODUCCION.md` — nueva §3.2 (addendum)
No repite §3 ni §3.1; corrige tres cosas que aquellas dejaban mal resueltas y añade una cuarta:

- **§3.2.1 — el ritmo no es una cadencia fija, es un arco que respira.** Corrige §3.1
  ("3-5 planos de 12-20s") y `SISTEMA_STORYBOARD` §5.1 ("cada 10-14s"), que describían cadencia
  **uniforme**. Incluye la traducción obligatoria a nuestra plataforma: VideoExpress topa en 10s
  y la deriva 2D se acumula con la duración, así que los 25-40s de "exhalación" de las fuentes
  **no se pueden ejecutar literalmente** — nuestra escala está comprimida por el motor.
- **§3.2.2 — el presupuesto de §4 está calculado 3× por debajo.** Regla nueva: presupuestar
  **paneles × 3**, no × 1. Explica retroactivamente por qué el canal ya pagó dos rondas
  completas de regeneración: es el rendimiento normal del medio, no mala suerte.
- **§3.2.3 — falta bloquear la referencia de ESCENARIO.** Hoy sólo está bloqueado el personaje.
  Acción propuesta: archivar el primer still aprobado de cada escenario del diccionario como
  `refs/escenario_<nombre>.png` y reusarlo. Coste 0 generaciones.
- **§3.2.4 — capas espaciales explícitas** en el Image Prompt (la regla de tercios coloca UN
  punto de interés; las capas quitan al generador la decisión sobre todo lo demás).
- **§3.2.5 — nota de confianza** (la limitación del proxy, arriba).

### `SISTEMA_STORYBOARD_MINDSET_MECHANICS.md` → v1.2
- §5.1: cadencia uniforme **corregida** por la regla de ritmo repartido.
- §4: nueva ranura de capas en la plantilla + **aviso del conflicto de negativos** (abajo).
- §8: tres puntos nuevos de checklist (16, 17, 18), incluida la obligación de que **todo
  storyboard declare sus banderas de riesgo aunque estén vacías**.

### `storyboards/` (piloto de Resiliencia) → v1.1, en `.md` y en `.json`
Auditoría contra la estructura completa. Lo que **ya cumplía**: duración medida real (94,0s de
553,4s medidos con ffprobe, no estimados), 4 sub-planos por bloque narrativo, tipo de plano +
Video Action Prompt de 4 partes en los 15 paneles, transiciones variadas (4 tipos), eje de 180°
y raccords verificados. Lo que **le faltaba y se completó**:

1. **Ritmo plano → ritmo repartido (§5).** Tenía 14 paneles de 6,00s exactos + 1 de 10s. La
   densidad era correcta (9,6 cortes/min) pero perfectamente uniforme. Nueva secuencia
   `5-7-8-4-4-8-7-5-4-8-6-6-5-7-10` (94s exactos). El par `4+4` es el momento más rápido y cae
   **encima** de la ventana de pattern interrupt de 25-35s, con el `smash_cut` en 0:24.
   **No cambian: las 8 imágenes, los 15 clips, los beats, los timecodes de voz en off, los
   prompts, las transiciones. Coste: 0 créditos.** Sólo cambia el `duration_seconds` que se
   pasa a `animate_library_image()`. Tabla de reversión incluida.
2. **Banderas de riesgo (§6).** No existían. Ahora hay 5 (R1-R5), también en el JSON.
3. **Capa de audio (§7).** `SISTEMA_STORYBOARD` §8.5 la exige y faltaba entera. Andamiaje por
   beat con niveles del canal; los `asset_id` van marcados `<POR ELEGIR>` a propósito.

---

## 3. Bug encontrado (síntoma → causa → fix → verificación)

**Síntoma.** Los 15 `image_prompt` del piloto cierran con los negativos escritos dentro del
prompt positivo (`"...NO visible hair, NO visible ears, NO blush..."`), y el checklist del
propio storyboard lo marcaba ☑ como si fuera un acierto.

**Causa.** `ESTILO_MINDSET_MECHANICS.md` §6.bis (regla dura, 2026-08-25) dice justo lo
contrario: los modelos de difusión no entienden la negación lingüística y los tokens `ears` /
`nose` acaban condicionando **en positivo** — es la causa raíz ya diagnosticada de las orejas y
narices que forzaron dos rondas rechazadas. §6.bis remite al parámetro `negative_prompt` de la
API y afirma que los negativos canónicos "viven en `recraft_ai/recraft_client.py` → constante
`NEGATIVE_PROMPT` y se aplican por defecto". **Ninguna de las dos cosas es cierta hoy en el
código:** no existe tal constante, `generate_scene.py` usa `recraftv4_1` por defecto y
`recraft_client.py` (líneas 87 y 136) sólo acepta `negative_prompt` en V2/V3. Es decir: la vía
que la regla manda usar no está disponible en el camino por defecto, y nadie lo había notado
porque el piloto se detuvo antes de generar.

**Fix aplicado hoy:** no lo cierro yo — es decisión de Kimi (ver §4). Lo que sí hice es dejar
de esconderlo: bandera **R2** en el storyboard, punto 11 del checklist del piloto degradado de
☑ a ⚠️, y aviso en `SISTEMA_STORYBOARD` §4 para que ningún storyboard futuro dé este punto por
cerrado copiando la cláusula al final del prompt.

**Verificación:** `grep -n NEGATIVE_PROMPT recraft_ai/recraft_client.py` → sólo aparece
`_MODELS_WITH_NEGATIVE_PROMPT` (línea 87), no hay constante de negativos del canal.
`recraft_ai/generate_scene.py:41` → `--model default="recraftv4_1"`; `:44` →
`--negative-prompt default=None`.

---

## 4. Lo que NO me toca a mí — para David / Kimi

1. **R2 — negativos (decisión bloqueante, antes de gastar el primer crédito).** Dos opciones:
   **(a)** redactar los negativos en positivo dentro del prompt (describir la silueta lisa
   deseada en vez de nombrar lo prohibido), o **(b)** mover la generación a
   `recraftv3 @1820x1024` y pasar el negativo por el parámetro real de la API. Es una decisión
   creativa y de coste, no técnica: la (b) cambia el modelo con el que se validó el look.
2. **R4 — saldo de la API de Recraft sin pagar** (commit `7c425d0`). Bloqueante externo: nada
   de esto se puede generar hasta resolverlo.
3. **R3 — librería de audio.** El andamiaje de sonido está escrito, pero **nadie ha curado
   todavía música/ambiente/SFX con licencia apta para YPP**. Sin eso, §7 son huecos.
4. **R1 — el panel de 10s (SC02_SH008).** Supera la ventana segura de 5-8s de la ola 2. Lo dejo
   como estaba porque ya estaba aprobado, pero es el panel con más probabilidad de deriva del
   piloto. Si sale mal, partirlo en 6s+4s **antes** de re-rollear la imagen (más barato).
5. **Ráfaga real en el pattern interrupt.** El patrón de "ráfaga" (5-10 cortes rápidos) no se
   puede ejecutar con la arquitectura a/b actual: haría falta un tercer clip en ese beat, o sea
   generaciones extra. Es decisión de presupuesto.
6. **Audio real medido más allá de 1:34.** El piloto sólo cubre 0:00-1:34 de los 553,4s. Los
   otros ~7:39 siguen sin storyboard.

---

## 5. Archivos tocados

- `PROYECTO MECHANICS OPTIMIZACIONES/MANUAL_PRODUCCION.md` — nueva §3.2 (5 sub-secciones)
- `SISTEMA_STORYBOARD_MINDSET_MECHANICS.md` — v1.0 → v1.2
- `storyboards/STORYBOARD_resilience_v3_piloto_SC01-SC02.md` — v1.1 (§5, §6, §7 + tabla,
  cabeceras y JSON embebido regenerados)
- `storyboards/storyboard_resilience_v3_piloto.json` — duraciones, `tc`, `rhythm_role`,
  `rhythm_note`, `risk`, `rhythm_rule`, `risk_flags`
- `handoffs/REPORTE_2026-08-26_storyboard.md` — este reporte
