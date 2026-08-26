# HANDOFF ESTRATÉGICO — Kimi Code → Claude Code

**Fecha: 2026-08-23 · Proyecto: Mindset Mechanics**
Naturaleza: decisiones tomadas + plan de ejecución por lotes. Kimi decide el QUÉ y el ORDEN; Claude Code ejecuta el CÓMO en terminal.

---

## 0. PRINCIPIO RECTOR PERMANENTE — máxima calidad al menor costo de producción

Directriz del usuario (2026-08-23), aplica a TODO el proyecto de aquí en adelante: **el resultado debe ser el mejor posible, pero cada crédito de VideoExpress y cada hora de pipeline debe justificarse. Calidad sin techo, gasto con lupa.** Reglas operativas que se derivan:

1. **Nunca regenerar en bloque lo que falla en parte.** Si una escena sale mal, se regenera SOLO esa escena (o se repara con Smart Edit v2 / inpainting si el defecto es un artefacto localizado — más barato que una regeneración completa).
2. **Los gates de tanda existen precisamente por esto:** detectar un prompt defectuoso en la escena 2 cuesta 2 créditos; detectarlo en la escena 12 cuesta 12. Los gates no se saltan nunca aunque "parezca que todo va bien".
3. **Técnica B (texto verbatim) es la vía de producción; Técnica A (Consistent Character) solo se persigue si se demuestra que mejora el resultado** — no gastar créditos de diagnóstico en una mejora que la evidencia aún no justifica.
4. **Cero experimentos con funciones Beta** (First Frame, Last Frame) mientras el Video Action Prompt validado hace el trabajo. Un experimento A/B cuesta créditos reales: se hace UNA vez, pequeño, con hipótesis clara, y solo si promete subir calidad o bajar costo por escena.
5. **Reutilización antes que generación nueva:** el fondo/entorno de una escena aprobada puede reciclarse (misma ubicación narrativa = reutilizar imagen base con distinto Video Action Prompt cuando el guion lo permita, p.ej. las escenas 1 y 10 de Resiliencia que comparten mesa de conferencias — evaluar si la 10 puede partir de una variante barata de la 1 en vez de generación desde cero, SOLO si el QA visual lo aprueba).
6. **Contenido derivado de coste cero tiene prioridad estructural:** Shorts solo se recortan de largos ya producidos (nunca producción dedicada); la recopilación/maratón de 45-70 min para las 4.000 horas se cose de material ya publicado (playbook §6).
7. **Duración 10-13 min es también una decisión de costo:** más minutos por video con el mismo número de escenas (60-80s por escena) = más watch-time por crédito gastado. Subir duración NO implica subir escenas proporcionalmente.
8. **Métrica de control:** cada handoff de Claude Code debe reportar créditos/generaciones consumidas vs. presupuesto, igual que reporta bugs. Lo que no se mide se desperdicia.

---

## 1. Las 3 decisiones pendientes — RESUELTAS

### Decisión 1 — Secuenciación: (a) Resiliencia → (b) guion nuevo → (c) Shorts en paralelo manual

Orden fijado:

| Prioridad | Tarea | Por qué |
|---|---|---|
| **P0** | Regenerar el video de Resiliencia con `RESILIENCE_SCENE_PLAN.md` v2 | Es el único 🔴 abierto: un video completo no publicable. Además es la prueba de fuego del pipeline de 12 escenas — si el pipeline no sostiene 12 generaciones consistentes, hay que saberlo ANTES de escribir guiones nuevos a 10-13 min (que exigirán 12-16 escenas). |
| **P1** | Guion nuevo #1: "Why Didn't Evolution Remove Social Anxiety?" | Empieza en cuanto Resiliencia pase QA visual de la tanda 1, no antes. Kimi produce guion + scene plan siguiendo el playbook; Claude Code no lo necesita todavía. |
| **P2** | Subir los 5 ultra-shorts según `SUBIR_ultrashorts_v2.md` (fechas 23, 25, 27, 29, 31 ago) | Es tarea manual de 10 minutos por short en YouTube Studio, no consume pipeline ni créditos. El playbook dice "no producir más Shorts", pero estos ya están pagados: subirlos no compite con nada. El usuario los sube a mano; no es tarea de Claude Code salvo el paso de "Vídeo relacionado" si requiere revisión. |

**Lo que NO se hace:** priorizar Shorts sobre largos (el dato del playbook §0.1 y las métricas propias lo prohíben), ni escribir más guiones hasta validar la tanda 1 de Resiliencia.

### Decisión 2 — Presupuesto de iteración del pipeline

Esquema escalonado con gates de calidad (no 1 a 1 todo el camino — demasiado lento; no 12 de golpe — demasiado riesgo):

- **Tanda 0 (ya en curso):** Escena 1. Verificar resultado visual + comportamiento del polling con el nuevo logging.
- **Tanda 1:** Escenas 2-3 (2 generaciones). Gate: revisión visual de consistencia de personaje + estilo contra `ESTILO_MINDSET_MECHANICS.md` §7.
- **Tanda 2:** Escenas 4-7 (4 generaciones). Gate intermedio: revisar escena 7 (direct address) — es la de mayor riesgo de deriva facial.
- **Tanda 3:** Escenas 8-12 (5 generaciones). Gate final + ensamblaje.
- **Regla de abortado:** si en cualquier tanda 1 escena rompe estilo o personaje, se para, se ajusta el prompt global (prefijo/sufijo/cláusula negativa) y se regenera SOLO lo defectuoso. No seguir gastando créditos con un prompt defectuoso.
- **Presupuesto total autorizado:** 12 generaciones + margen de 3 regeneraciones = **15 máximo**. Si se agotan sin QA aprobado, se escala a Kimi antes de seguir.

### Decisión 3 — Cadencia de publicación: SÍ se puede sostener 1 largo cada 4-5 días

Cálculo: 12-16 escenas × ~5-15 min/escena = 2-4h de generación por video, más ensamblaje existente. El pipeline escena-por-escena **sostiene la cadencia sin paralelizar todavía**.

- **Compromiso:** 1 video largo cada 4-5 días, franja 9am-1pm ET, sin importar el día de la semana (playbook §6).
- **No paralelizar generación ahora** (riesgo de sesión Playwright/rate-limits). Re-evaluar solo si aparece cuello de botella real medido, no anticipado.
- **No anunciar la cadencia públicamente todavía** — primero 2 videos consecutivos cumplidos, luego ya es hábito demostrado.

---

## 2. Cola de trabajo para Claude Code (orden de ejecución)

### LOTE A — Cierre de la prueba en curso (hoy)

1. Verificar resultado de la escena 1 de Resiliencia: ¿el polling reportó `completed` con el nuevo logging, o el render tardó >900s legítimamente?
2. Si el render completó: revisar visualmente contra checklist §7 de `ESTILO_MINDSET_MECHANICS.md` (personaje, estilo, cero texto en imagen, 1080p). Si pasa → LOTE B.
3. Si hubo timeout de polling: subir el timeout de render de 900s a **1800s (30 min)** como medida defensiva y registrar el status real que devolvió `get_media` al expirar. Decisión sobre bug de API vs. render lento se toma CON ese dato, no antes.

### LOTE B — Regeneración de Resiliencia (tandas 1-3)

Ejecutar las tandas definidas en Decisión 2, con estos detalles operativos:

- Cada comando sigue el patrón de `RESILIENCE_SCENE_PLAN.md` §"Cómo lanzar": prefijo de personaje + {PLANO} + Scene: + sufijo de luz + cláusula negativa, **completos las 12 veces, nunca abreviados**.
- `--type 2D` explícito siempre; verificar "Automatically enhance" desmarcado en cada apertura de modal (se re-marca solo — bug conocido ya mitigado, pero confirmar).
- Nombrar salidas `resilience_scene_01.mp4` … `resilience_scene_12.mp4`.
- Tras cada tanda: **STOP y reporte a Kimi** con capturas inicio/medio/fin de cada clip antes de lanzar la siguiente tanda.

### LOTE C — Ensamblaje del video de Resiliencia (cuando las 12 pasen QA)

1. Concatenar los 12 clips en orden.
2. Montar `voiceover.mp3` (553.4s) encima — el plan de timestamps de la tabla v2 es la referencia de sincronía.
3. Subtítulos quemados según §4 del estilo (amarillo, contorno negro, 3-4 palabras, tercio inferior).
4. Badge de suscripción (largo).
5. Salida 1920x1080, validación `ffmpeg -f null` sin errores, checklist §7 completo.
6. **NO publicar todavía** — queda en cola de publicación con fecha asignada por Kimi (ver §3).

### LOTE D — Deuda técnica (SOLO cuando LOTE B/C estén en gate de revisión, nunca interrumpiendo generaciones)

Orden de prioridad de la deuda:

| # | Ítem | Prioridad | Nota estratégica |
|---|---|---|---|
| D1 | Timeout de polling 900s → 1800s | Alta si LOTE A confirma timeout; si no, bajar a media | Es 1 línea; no tocar la lógica de lectura de `get_media` hasta tener el log del status real |
| D2 | `mark_consistent_character()` / Técnica A | Baja — diferida | No bloquea producción (Técnica B validada). Hipótesis documentada: el botón + solo se habilita sobre imágenes GENERADAS por la app. Próximo paso cuando se retome: generar con "Create Image" teniendo la Reference Photo seleccionada y revisar el botón sobre ese resultado. No gastar más rondas de diagnóstico esta semana. |
| D3 | `import_local_image()` | ✅ Ya implementada según MANUAL §5 — confirmar que así es y tachar de la lista de pendientes del handoff anterior | |
| D4 | `video_understand.py` (yt-dlp + faster-whisper ya instalados) | Media — para la fase de guion nuevo | Lo necesitaré para analizar competencia antes del guion #2. Especificación la da Kimi en el siguiente handoff; no improvisar alcance. |
| D5 | Experimento A/B First Frame, Last Frame vs Video Action Prompt | Baja — diferida | Es función Beta sin documentación. Un solo experimento pequeño DESPUÉS de publicar Resiliencia regenerado. No comprometer el pipeline a ella. |

---

## 3. Calendario objetivo (sujeto a QA, no es una promesa rígida)

| Fecha | Hito |
|---|---|
| 23 ago | LOTE A cerrado + Tanda 1 lanzada. Short `18_predator_mawson_livers` subido a las 19:00 (manual, usuario) |
| 24 ago | Tandas 2-3 + inicio de LOTE C |
| 25 ago | Resiliencia ensamblado y en QA final. Kimi entrega guion #1 (Social Anxiety) + scene plan |
| 26-27 ago | Generación del video de Social Anxiety por tandas (mismo esquema de gates) |
| 28-29 ago | **Publicación de Resiliencia regenerado** (9am-1pm ET) |
| ~1-2 sept | **Publicación de Social Anxiety** → cadencia de 4-5 días inaugurada con 2 videos consecutivos |

**Regla de publicación:** un video no se juzga antes del día 10 (playbook §6). Nada de cortar presupuesto o pivotar por un arranque flojo.

---

## 4. Reglas de colaboración (recordatorio para Claude Code)

1. Verificar channel ID `UCKL6AQzdYM0-s3yFe3HrjYA` antes de tocar YouTube Studio (gotcha de cuentas múltiples documentado).
2. Nunca usar `drawtext` de ffmpeg en esa máquina — segfault confirmado. Badges con `make_shorts_badge.py` + `add_badge.sh`.
3. No borrar `SMSd8a9Im_c` (brazo negativo del experimento A/B de hooks).
4. Ante cualquier desviación de este plan que implique gastar créditos fuera del presupuesto de 15 generaciones, o cambiar el orden de los lotes: **STOP y consultar a Kimi, no improvisar**.
5. Todo bug nuevo encontrado en producción se documenta al estilo del handoff anterior (síntoma → causa → fix → verificación en vivo), no solo se arregla.

---

## 5. Lo que Kimi hace en paralelo (no es trabajo de Claude Code)

- Guion completo de "Why Didn't Evolution Remove Social Anxiety?" (hook de 4 movimientos, 3-4 bucles abiertos, giro meta al ~70%, CTA comentario-número al 40% y 85%, cero CTA hablado de suscripción, 10-13 min).
- Scene plan del guion #1 en el formato de `RESILIENCE_SCENE_PLAN.md` v2.
- Revisión de QA de cada tanda (Kimi define criterio de pase/fallo; Claude Code aporta capturas).
- Siguiente handoff con la especificación de `video_understand.py` cuando llegue su turno (D4).
