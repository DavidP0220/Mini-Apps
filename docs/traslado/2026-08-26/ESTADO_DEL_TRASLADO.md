# ESTADO DEL TRASLADO — Mindset Mechanics · corte 2026-08-26

Dos cosas en un mismo documento: **(A)** en qué punto está el proyecto y **(B)** qué entró en
este paquete y qué no.

> El documento de referencia lo escribió David: `LEEME_PRIMERO_TRASLADO.md`, en el zip
> `00_RAIZ_INDICES_DEL_AUTOR`. Si algo aquí y allí se contradice, **manda el suyo**.

---

## A. Dónde está parado el proyecto (último día registrado: 2026-08-26)

### Lo que se desbloqueó
**El saldo de la API de Recraft ya está pagado y activo** (confirmado por David el 26-ago).
Era el bloqueante principal: las 7 imágenes base nuevas del piloto dependían de él. En el PC
nuevo hay que **recrear `recraft_ai/.env` con `RECRAFT_API_KEY`** — la clave no viaja aquí.

### Dónde quedó la producción
- **Video "Resiliencia"** — en producción del **piloto (0:00-1:34, 15 paneles / 94 s)**,
  **parado a medias por orden expresa de David**. El video del piloto **no se ha generado**.
  Nada se ejecuta sin autorización.
- La **voz en off ya existe** y cuadra con el tramo del piloto (553,4 s totales).
- La **sesión de VideoExpress hay que volver a autenticarla** en el PC nuevo
  (`setup_auth.py` / `setup_auth_auto.py`; Playwright guarda la sesión tras un login manual).

### El pipeline oficial vigente

```
Guion → TTS + ffprobe (duración real) → STORYBOARD → [GATE humano]
   → stills en Recraft AI (1 por panel, validados contra material publicado)
   → import_local_image() a VideoExpress
   → animate_library_image() con Video Action Prompt (image-to-video)
   → ensamblaje ffmpeg (sub-clips reales, transiciones variadas, audio -14 LUFS)
   → QA técnico + [GATE humano] → publicación
```

### Pendientes abiertos, por urgencia

1. **Las 12 imágenes ya pagadas (204 créditos) siguen solo en el servidor web de Recraft.**
   Nunca se descargaron a disco. **Riesgo real de pérdida y descargarlas cuesta 0 créditos** —
   es la primera tarea, antes que cualquier generación nueva.
2. **Referencia de escenario sin bloquear.** Solo el personaje está bloqueado
   (`MANUAL_PRODUCCION.md` §3.2.3). Generar escenas sin eso repite el problema de consistencia
   que ya costó una ronda entera.
3. **Burbuja de cómic de la escena 11** sin resolver (queda fuera del piloto, pero está abierta).
4. **Decisiones escaladas a Kimi** que siguen sin cerrar: 3ª vía de animación y presupuesto —
   `HANDOFF_2026-08-25_urgente_kimi_decision_pendiente.md` y
   `HANDOFF_2026-08-25_decision_tercera_via_resiliencia.md`.
5. **Regla nueva del 26-ago:** presupuestar **paneles × 3 generaciones**, no × 1. La tasa de
   selección real ronda 1 de cada 3.
6. **Guiones:** solo hay **2 guiones reales** (Resiliencia y Social Anxiety), no 4. Attention
   Span y Jealousy están en fase de idea. Es el cuello de botella de la cadencia.
7. **Tareas que necesitan navegador** y nadie ha ejecutado: el post de Comunidad (encuesta ya
   redactada) y verificar el CTA "mira el video completo" en los 14 Shorts y 4 largos.

### Contexto de monetización que cambió y no hay que ignorar
- YouTube **duplicó la barra del YPP**: 8.000 horas (antes 4.000) o 20 M vistas de Shorts;
  1.000 subs se mantiene. **Entra en vigor el 1-feb-2027** y solo afecta a quien no esté ya
  *aceptado* dentro del programa para esa fecha. El objetivo no es "estar cerca": es **estar
  dentro**.
- Cambió el conteo de vistas públicas (desde el fotograma 1). **No cambia la elegibilidad**: el
  progreso real se mide en *Engaged Watch Hours* (Studio → Analytics → Advanced Mode).
- **Test & Compare** elige la variante con más *watch time por impresión*, no la de más CTR:
  las variantes deben ser ángulos genuinamente distintos, no retoques del mismo texto.
- **Función Collab** (hasta 10 creadores etiquetados, con botón de suscripción propio sobre el
  video): palanca de crecimiento detectada y **todavía sin usar**.

---

## B. Qué entró en este paquete

**1377 archivos** (160M) del árbol de traslado, más **246** extraídos de
los 6 `.zip` que venían anidados dentro.

- **Todo el trabajo con Kimi-Claude**: los 27 archivos de `handoffs/` sin excepción
  (HANDOFF_*, REPORTE_*, INVESTIGACION_*, REVISION_TECNICA_*, PROGRAMA_MEJORA_CONTINUA_KIMI),
  más `HANDOFF_KIMI_CODE.md`, el volcado de 522 KB, el `.zip` y `HANDOFF_KIMI_PACKAGE/`.
- **Todo el código**: `recraft_ai/`, `video_express_ai/`, `youtube_pipeline/`, `shorts_final/`,
  con configs, requirements, logs de generación y manifiestos de subtítulos.
- **Toda la documentación**: `PROY_MECH_OPT/`, `docs_raiz_repo/`, los paquetes de conocimiento
  v1, v2 y v3 (sueltos **y** en `.zip`), investigaciones de canales monetizados y de
  VideoExpress.
- **Los storyboards**, las **8 memorias persistentes**, los **8 agentes de Claude Code** +
  `settings.local.json`, y todas las **referencias visuales** (personaje, style-locks, badges,
  stills de Recraft, paneles de cómic, last-frames de las 12 escenas).

### Verificación de que nada quedó atrapado dentro de un zip
Se compararon por huella SHA-256 los archivos sueltos contra los que venían dentro de los
`.zip` anidados: **0 archivos existen solo dentro de un zip**. Es decir, el árbol ya
trae suelto todo lo que había ahí dentro; los zips desempaquetados van igualmente por comodidad.
El detalle está en `UNICOS_EN_ZIPS_INTERNOS.md`.

### Lo que NO entró — y por qué (decisiones explícitas, ninguna omisión accidental)

1. **Los videos `.mp4/.mov/.mkv/.webm`.** Excluidos a propósito: habrían llevado el paquete por
   encima de 1 GB. **Ya están respaldados en OneDrive** y los publicados están en YouTube. Sí
   viaja todo lo necesario para continuidad: el código que los produce, los scripts de
   ensamblaje, los `concat_*.txt`, `filter_complex.txt`, los manifiestos de subtítulos, el
   audio de voz en off y los **frames extraídos** (`last_frame_*.png`).
2. **Otros proyectos de David** que conviven en la misma carpeta de trabajo (GRASS, HUMAN
   CHRONICLES, HIGGSFIELD ALTERNATIVA, mini_apps_hotmart, rfq, etc.). Regla dura del proyecto:
   **nunca se mezclan canales ni proyectos**. Cada uno tiene su propio paquete.
3. **`ComfyUI/` (~13 GB)**: herramienta de terceros, se reinstala desde su fuente oficial.
4. **`__pycache__/` y `.pyc`**: basura de compilación, se regenera sola.
5. **Los secretos**: `.env` reales, `auth_state.json`, `kimi_token.txt` y cualquier archivo con
   `token`/`secret`/`api_key`/`credentials` en el nombre. Sí viajan los `.env.example`.

### Credenciales que hay que rehacer en el PC nuevo
1. `recraft_ai/.env` → `RECRAFT_API_KEY` (el saldo ya está pagado en la cuenta de David).
2. `video_express_ai/.env` + `auth_state.json` → ejecutar `setup_auth.py` y hacer login manual
   una vez.
3. `youtube_pipeline/.env` → credenciales OAuth de la YouTube Data API
   (cuenta `mechanicsmindset02@gmail.com`).
4. `kimi_token.txt` → token de coordinación con Kimi Code; pedírselo a David.

---

## C. Cómo verificar la copia

```bash
# en la carpeta donde extrajiste TODOS los zips de paquetes/
sha256sum -c MANIFIESTO_SHA256.txt
```

Si algo aparece como `FAILED` o no existe, se vuelve a sacar del zip que lo contiene, según
`INVENTARIO_COMPLETO.md`.
