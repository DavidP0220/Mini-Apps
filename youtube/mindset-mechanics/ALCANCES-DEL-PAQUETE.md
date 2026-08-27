# Alcances totales del paquete de conocimiento — Mindset Mechanics

**Auditoría hecha el 2026-08-26** sobre `PAQUETE_CONOCIMIENTO_MINDSET_MECHANICS_2026-08-23.zip`
(27 archivos, 1,2 MB, corte de datos 2026-08-22/23).

Este documento responde a dos cosas: **qué contiene el paquete** y **qué contradice de las
decisiones tomadas el 2026-08-26**.

---

## 1. Estado real del canal, medido hoy (vidIQ, no estimado)

| Métrica | Paquete (22-ago) | Hoy (26-ago) | Delta |
|---|---|---|---|
| Suscriptores | 7 | **11** | +4 |
| Vistas totales | 246 | **411** | +165 |
| Videos publicados | 9 | **12** | +3 |

Canal: `UCKL6AQzdYM0-s3yFe3HrjYA` · `@MindsetMechanicsCo` · creado 2026-07-20 · US / inglés.
Nicho: psicología evolutiva — *"tu cerebro corre mecánica de hace 300.000 años"*.

Distancia a monetización completa (YPP): faltan **989 suscriptores** y **≈3.993 horas**.

---

## 2. Inventario por función

### 2.1 Estrategia y monetización (el núcleo)

| Archivo | Qué contiene |
|---|---|
| `PLAYBOOK_MONETIZACION.md` | **El activo más valioso.** 9 secciones destiladas de 12 canales del nicho ya monetizados: 5 decisiones críticas, 6 fórmulas de título con métricas A/B reales, plantilla de hook de 4-5 movimientos, estructura de bucles abiertos, 3 mecanismos de CTA, 3 plantillas de miniatura, cadencia/horario, matemática exacta de la meta, 4 filones sin explotar, plan de 4 videos. |
| `PLAYBOOK_MARCA_INTERACCION_VENTAS.md` | Capa de marca personal y venta fuera de AdSense: relación parasocial en canales faceless, rutina diaria de interacción, protocolo de comentarios, YouTube Shopping (requisitos 2026), infoproductos por link. 14 fuentes externas citadas. |
| `INVESTIGACION_canales_monetizados.md` (187 KB) | **Datos crudos.** 8 bloques JSON con 29 channelIds verificados. Canales analizados a fondo: Zenn, Decode The Brain, ONLI, Human Condition, The Primal Glitch, PsychToons, Psychology Simplified, Professor Stickman, ThinkMan, Beyond the Obvious, Apex, Ask Nigel, Big Brain Explains, Smart StickLogic, Cave Circuit. |

### 2.2 Identidad visual

| Archivo | Qué contiene |
|---|---|
| `ESTILO_MINDSET_MECHANICS.md` | Biblia de estilo **bloqueada (LOCK)**, corregida contra frames reales de los 4 videos publicados. Personaje, arte, cámara, subtítulos quemados, plantilla de prompt v4 validada, checklist de 7 puntos. Lista de palabras **prohibidas** en prompts: `comic`, `comic panel`, `halftone`, `vector`, `flat`. |
| `REFERENCIA_personaje.png` (635 KB) | Referencia real del personaje, extraída de frames publicados. Es el insumo para "Use Consistent Character". |

### 2.3 Pipeline de producción (código funcional)

| Archivo | Qué contiene |
|---|---|
| `video_express_bot.py` (26 KB) | Bot Playwright contra VideoExpress.ai. **23 funciones**: `create_image`, `create_silent_video`, `create_lipsync_video`, `stylize_character`, `mark_consistent_character`, `import_local_image`, `import_local_audio`, `add_media_to_timeline`, `enable_automatic_captions`, `export_video`, más helpers. |
| `generate_video.py` (8 KB) | CLI del bot: subcomandos `image`, `stylize`, `lipsync`, `scene`, `import-image`, `mark-character`. |
| `MANUAL_PRODUCCION.md` | Manual destilado de 9 tutoriales oficiales de VideoExpress: patrón nuclear Image Prompt → Video Action Prompt, dos técnicas de consistencia de personaje, cláusula negativa estándar, banco de frases de cámara, reglas "nivel Netflix", flujo para 8-13 min, checklist. |
| `INVESTIGACION_tutoriales_videoexpress.md` (195 KB) | Datos crudos: 7 documentos Customer Training extraídos (#6, #7, #8, #13, #14, #15, #19). |
| `make_shorts_badge.py` + `add_badge.sh` | Badge de SUBSCRIBE quemado en los últimos 3,5s de cada Short (Pillow, porque `ffmpeg drawtext` segfalla en esa máquina). |
| `make_ultrashorts.sh` | Recorte reproducible de Shorts verticales 1080x1920 desde los largos. |

### 2.4 Contenido en cola

| Archivo | Qué contiene |
|---|---|
| `script_resilience_video.md` | Guion completo del 5º video largo (*Why Your Brain Breaks Under Pressure*). |
| `RESILIENCE_SCENE_PLAN.md` | Desglose en 12 escenas con timestamps calculados, prompts de imagen y bloque de estilo fijo. |
| `SUBIR_ultrashorts_v2.md` | 5 Shorts listos con título, descripción, tags y fecha de publicación. Puntuación vidIQ 86-94. |

### 2.5 Memoria y trazabilidad

`memoria_claude/` — 4 reglas duras del usuario: comunicación **solo en español**, calidad **mínima 1080p** (y principio general de "siempre subir el nivel, nunca bajarlo"), investigar en la web antes de parchar, y el alcance completo del proyecto en 5 capas.

`handoffs/` — 6 documentos de traspaso entre sesiones (Kimi Code ↔ Claude Code): decisiones de presupuesto, QA fallido escalado, bug de descripciones rotas en 3 Shorts, enlazado de los 14 Shorts a su video largo.

---

## 3. Técnicas reutilizables en CUALQUIER canal

Esto es lo que el paquete aporta más allá de Mindset Mechanics:

1. **Leer un video sin verlo** — rejilla de frames con ffmpeg recortando solo la banda de subtítulos: 20 momentos del video de una mirada.
   ```
   ffmpeg -ss 140 -t 60 -i v.mp4 -vf "fps=1/3,crop=1920:330:0:700,scale=760:-2,tile=4x5:margin=6:padding=6:color=black" -frames:v 1 out.png
   ```
2. **Cortes limpios en fronteras de silencio** — `silencedetect=noise=-30dB:d=0.25`.
3. **Ubicar una frase en el timeline** — fracción de caracteres del transcript × duración. Precisión ±3s.
4. **Filtro de Short vertical con fondo difuminado** — un solo `filter_complex`, salida CRF 18.
5. **Las 6 fórmulas de título con evidencia A/B** — transferibles a cualquier nicho de conocimiento.
6. **La plantilla de hook de 4-5 movimientos** — regla verificada: la palabra del título NUNCA aparece en los primeros 15-22 segundos.
7. **El CTA de "comenta un número"** — multiplica la tasa de comentarios x4-x30.

---

## 4. Deuda técnica y errores abiertos

| # | Estado | Asunto |
|---|---|---|
| 1 | 🔴 | El 5º video (Resiliencia) **no es publicable**: estilo cómic equivocado, personaje inconsistente, sin subtítulos, 720p, texto basura generado por IA. Hay que regenerarlo. |
| 2 | 🟡 | `06_predator_douglas_mawson.mp4` está mal nombrado — cubre el tramo de biomagnificación, no el de Mawson. |
| 3 | 🟡 | 3 descripciones de Shorts apuntan a un video que ya no existe. |
| 4 | 🟡 | `video_understand.py` (yt-dlp + faster-whisper) nunca se escribió. |
| 5 | 🟡 | `generate_video.py scene` quedó sin probar. |
| 6 | 🟢 | **Discrepancia detectada en el propio paquete:** `LEEME-PRIMERO-HANDOFF.md` §6 dice que falta escribir `import_local_image()`. Es falso — está implementada en `video_express_bot.py:471` y `MANUAL_PRODUCCION.md` §5 la da por probada en vivo. El handoff tiene corte 22-ago y quedó desactualizado. |

---

## 5. Contradicciones con las decisiones del 2026-08-26

Tres de las cuatro decisiones tomadas hoy chocan de frente con la evidencia medida que el propio
paquete contiene.

### 5.1 🔴 "2-3 Shorts diarios" vs. la decisión #1 del playbook: *matar los Shorts al 100%*

Datos medidos en el canal (19-jul a 22-ago):

| Formato | Vistas | Minutos vistos | Subs ganados |
|---|---|---|---|
| Largos | 146 | **398** | **4** |
| Shorts | 95 | **8** | **0** |

Y en el dataset externo: **11 de 12** canales monetizados del nicho crecieron con cero o casi cero
Shorts. El único con Shorts pesados (Cave Circuit) es la prueba negativa.

Los Shorts de este canal han producido 95 vistas, 8 minutos y **cero suscriptores** — incluido uno con
83,8 % de retención. El cuello de botella del YPP son los 1.000 suscriptores, y los Shorts no aportan
ninguno.

### 5.2 🔴 "Canal nuevo desde cero" vs. lo que ya está construido y midiendo bien

Empezar de cero descarta: biblia de estilo bloqueada y validada contra frames reales, referencia de
personaje, pipeline Playwright de 23 funciones, 12 videos publicados, 14 Shorts enlazados, y —lo más
importante— una **tasa de conversión medida de 2,74 %** (146 vistas → 4 subs).

Ese 2,74 % es mejor que **todos** los benchmarks del dataset:

| Canal | Conversión |
|---|---|
| **Mindset Mechanics** | **2,74 %** |
| ONLI | 1,27 % |
| Human Condition | 0,81 % |
| The Primal Glitch | 0,60 % |
| Professor Stickman | 0,58 % |
| Decode The Brain | 0,30-0,39 % |

Cita textual del playbook §7: *"El problema nunca fue tu conversión ni tu formato — es puramente
volumen de vistas acumuladas."* Y §6: *"El pivote de formato funciona sin borrar el canal (ThinkMan:
3 meses muerto → cambia de fórmula → +12.300 subs en 8 semanas). No hace falta reiniciar Mindset
Mechanics, solo cambiar la plantilla de título/duración desde el próximo video."*

### 5.3 🟡 "Monetizar en menos de un mes" vs. la matemática del propio paquete

A la conversión actual del canal:

- **1.000 subs** exigen ≈ **36.000-37.000 vistas** adicionales de video largo.
- **4.000 horas** exigen ≈ 88.000 vistas a la retención actual, o ≈ 55.000 si los videos suben a 11-13 min.

El horizonte que el paquete documenta para el nicho es de **6-9 meses**: Decode The Brain tuvo su
primer breakout a los 8 meses y ~40 videos; ThinkMan estuvo 3 meses muerto antes de pivotar. La ley
de potencia del nicho es que 3-10 % de los videos generan 75-90 % de las vistas.

**AdSense en 30 días no va a pasar.** Lo que sí puede pasar en 30 días es la vía §4.2 del playbook de
marca: **infoproducto con link en la descripción**, que no depende de ningún umbral de suscriptores y
se puede montar desde el primer video.

---

## 6. Lo que sí encaja: el puente Mini-Apps ↔ canal

El playbook de marca (§4.2) propone como producto candidato *"un mini-ebook o PDF tipo 'Guía de
bolsillo: por qué tu cerebro hace esto' que empaquete 8-10 de los mecanismos evolutivos ya cubiertos
en los videos — contenido que YA existe en los guiones, solo hay que compilarlo."*

Este repositorio ya es exactamente ese motor, y mejor que un PDF: una mini-app PWA instalable con
capítulos, checklists y quizzes, donde el contenido es un solo `content.json`. Producir la versión en
inglés no requiere una app nueva — requiere un `content.json` nuevo.

Ruta concreta: guiones ya escritos → `content.json` en inglés → `node tools/new-app.mjs` → GitHub
Pages → link en la descripción de cada video y en la sección "Acerca de" del canal. Sin umbral de
suscriptores, sin logística, sin esperar al YPP.

---

## 7. Recomendación

1. **No abrir canal nuevo.** Pivotar Mindset Mechanics cambiando plantilla de título y duración desde
   el próximo video, como hizo ThinkMan.
2. **Parar la producción de Shorts nuevos.** Subir los 5 que ya están hechos (ya están pagados en
   tiempo) y no producir más.
3. **Todo el esfuerzo al video largo de 10-13 min**, con las fórmulas A/C del playbook, cadencia de 1
   cada 4-5 días.
4. ~~**Montar el infoproducto en inglés esta semana** con el motor de Mini-Apps.~~ **Hecho el
   2026-08-27:** `apps/factory-settings-manual/`, 10 capítulos. Queda decidir precio y captura de
   correos, y activar GitHub Pages. Ver `INFOPRODUCTO.md`.
5. Regenerar el video de Resiliencia con el estilo correcto antes de publicarlo.
