# Plan de escenas — regeneración del video de Resiliencia
**v2, revisado 2026-08-22.** Reemplaza la v1 (que tenía 9 escenas a ojo y se saltaba la Técnica 3 completa). Esta versión mapea `script_resilience_video.md` a la duración REAL del audio ya grabado (`voiceover.mp3` = **553.4s exactos**, medidos con `ffprobe`, no estimados), usando la misma técnica de fracción-de-caracteres que ya está documentada como precisa (±3s) en el handoff original. El guion y la narración **no se tocan** — esto es solo el plan de las imágenes/clips que hacían falta.

Resultado: **12 escenas** (subo de las 9 originales porque la v1 directamente omitía la Técnica 3 completa — 60.6s de guion sin escena asignada — y comprimía el bloque de Técnica 1 en una sola escena cuando cubre dos acciones físicas distintas). 12 escenas a ~46s de media es coherente con la cadencia de 45-98s que el propio guion ya tiene por bloque narrativo — no es un número inventado, sale de medir el guion real.

**Costo de lanzar esto:** 12 generaciones reales (imagen + video con movimiento cada una). En la prueba de esta sesión, una escena tomó unos minutos de principio a fin con el servicio respondiendo normal. Contar con 45-70 minutos de punta a punta y los créditos de 12 generaciones. **No lanzar hasta confirmar.**

---

## Timestamps reales (fracción de caracteres del guion × 553.4s)

| # | Bloque del guion | Rango | Duración |
|---|---|---|---|
| 1 | Intro | 0:00 – 0:48 | 48s |
| 2 | Sección 1: Anatomía del bloqueo | 0:48 – 1:34 | 46s |
| 3 | Sección 2a: Amígdala / detector de amenazas | 1:34 – 2:23 | 49s |
| 4 | Sección 2b: Carga alostática / estrés crónico | 2:23 – 3:13 | 50s |
| 5 | Sección 3a: Indefensión aprendida | 3:13 – 3:56 | 43s |
| 6 | Sección 3b: El giro hacia los recursos internos | 3:56 – 4:40 | 44s |
| 7 | CTA (pregunta directa a cámara) + intro a soluciones | 4:40 – 5:14 | 34s |
| 8 | Técnica 1a: el suspiro fisiológico | 5:14 – 5:53 | 39s |
| 9 | Técnica 1b: el reflejo de inmersión (agua fría) | 5:53 – 6:33 | 40s |
| 10 | Técnica 2: el reencuadre — bucle con escena 1 | 6:33 – 7:19 | 46s |
| 11 | Técnica 3: micro-exposiciones / inoculación al estrés | 7:19 – 8:20 | 61s |
| 12 | Conclusión | 8:20 – 9:13 | 54s |

---

## Bloque de estilo + cláusula negativa (fijos, van completos en CADA Image Prompt — Técnica B de `MANUAL_PRODUCCION.md` §2)

**Prefijo de personaje (pegar textual al inicio de cada Image Prompt, solo cambia {PLANO}):**
```
Soft painterly digital illustration in the style of a modern animated explainer short, 2D stylised animation, not anime. {PLANO} of a young man drawn with deliberately simplified cartoon proportions: a VERY LARGE round smooth head about one third of his total height, a completely smooth bald head shape with NO visible hair at all, a dark navy baseball cap sitting directly on that smooth head. His face is extremely minimal: two small plain solid black oval eyes with no iris, no highlight and no eyelashes, two thin short dark eyebrows, absolutely no nose of any kind — the space between the eyes and mouth is completely flat and smooth with no nose shape, no nostrils, no nose bridge, and no nose shadow — and a small simple line mouth. Completely flat pale cream skin colour with soft even shading, absolutely no rosy tint and no red or pink coloring anywhere on the face or cheeks — the cheeks are the exact same flat cream colour as the rest of the face, with no blush, no flush, and no warm coloring of any kind. Small simple body in a grey hoodie, dark jeans and sneakers.
```

**Sufijo de luz/estilo (pegar al final de cada Image Prompt, antes de la cláusula negativa):**
```
Rich atmospheric cinematic lighting, warm rim light, volumetric light shafts, floating dust particles. Muted harmonious colour palette. Full-bleed single scene with real environmental depth and a detailed background. Clean soft linework, gentle painterly shading.
```

**Cláusula negativa (pegar siempre al final, cierra el Image Prompt):**
```
Absolutely NO halftone dots, NO ben-day dots, NO starburst or speed lines, NO comic panels, NO white gutters, NO speech bubbles, NO anime face, NO detailed irises, NO visible hair, NO blush, NO pink cheeks, NO rosy cheeks, NO flushed skin, NO sharp jawline, NO photorealism, NO nose, NO nostrils, NO nose bridge, NO nose shadow, NO nose shape of any kind, and NO text, letters, signs or words anywhere in the image.
```

Cada fila de abajo solo da el `{PLANO}` + la parte de `Scene:` que cambia, y el Video Action Prompt completo — el resto se pega igual las 12 veces.

---

## Las 12 escenas

### 1 · Intro (0:00-0:48) — el bloqueo mental en la reunión
**{PLANO}:** Medium shot
**Scene:** he sits at a long conference table, several colleagues' silhouettes blurred around him, all eyes turned toward him. He has just opened his mouth to speak but his expression has gone blank, papers with notes forgotten in his hand.
**Video Action Prompt:** Slow push-in toward his face as the room around him gently blurs out of focus, his eyes widening slightly, tense and intimate.

### 2 · Sección 1 (0:48-1:34) — anatomía del bloqueo
**{PLANO}:** Extreme close-up
**Scene:** extreme close-up on his eye, a faint reflection of the blurred conference room visible in the pupil, sweat beading at his temple.
**Video Action Prompt:** Static for a beat, then slow tilt down from his eye to his trembling hand still holding the notes, subtle handheld tremor, anxious and claustrophobic.

### 3 · Sección 2a (1:34-2:23) — el detector de amenazas ancestral
**{PLANO}:** Low-angle shot
**Scene:** he stands frozen at an office doorway at night, the doorway's shadow subtly elongating into the silhouette of a cave mouth, faint glowing eyes of an unseen predator barely visible in the darkness beyond.
**Video Action Prompt:** Camera slowly cranes upward from a low angle, making the shadowed doorway loom larger, dust particles drifting through a shaft of cold light, dramatic and unsettling.

### 4 · Sección 2b (2:23-3:13) — carga alostática, estrés crónico
**{PLANO}:** Overhead shot
**Scene:** overhead view of his cluttered desk at night: a phone buzzing with notifications, stacks of paper piling up, a cold cup of coffee, the window behind showing a city skyline going dark.
**Video Action Prompt:** Slow zoom in on the buzzing phone, then gentle pan across the cluttered desk, cold blue city light flickering through the window, tense and exhausted mood.

### 5 · Sección 3a (3:13-3:56) — indefensión aprendida
**{PLANO}:** Wide shot
**Scene:** he sits slumped alone in a dim, sparse room, a door slightly ajar on the far wall with warm light spilling through the gap, but he isn't looking toward it.
**Video Action Prompt:** Static wide shot held for a long beat, only the light through the door gently flickering, quiet and heavy stillness.

### 6 · Sección 3b (3:56-4:40) — el giro hacia los recursos internos
**{PLANO}:** Medium shot from behind
**Scene:** he rises from the chair and walks steadily toward the half-open door, warm golden light growing brighter across the floor as he approaches it.
**Video Action Prompt:** Tracking shot behind him as he walks toward the light, camera slowly rising with him, hopeful and building, warm rim light increasing.

### 7 · CTA + intro a soluciones (4:40-5:14) — dirigiéndose al espectador
**{PLANO}:** Medium close-up, direct address
**Scene:** he stands in a plain softly-lit space, turned to look directly forward, calm and open expression, as if about to ask the viewer something.
**Video Action Prompt:** Still camera. He looks directly toward the camera as if speaking to the viewer, a faint, thoughtful pause before a small nod, quiet and direct.

### 8 · Técnica 1a (5:14-5:53) — el suspiro fisiológico
**{PLANO}:** Close-up, side profile
**Scene:** close side-profile of him standing by a window at dawn, eyes closed, taking a deep breath, chest visibly rising, soft blue morning light.
**Video Action Prompt:** Slow dolly in on his profile as he exhales slowly, his shoulders visibly relaxing, calm and deliberate, his breath faintly visible in the cool morning light.

### 9 · Técnica 1b (5:53-6:33) — el reflejo de inmersión
**{PLANO}:** Close-up over the shoulder
**Scene:** close-up over his shoulder as he stands at a bathroom sink, splashing cold water on his face, water droplets catching the light, soft blue morning light through a window above the sink.
**Video Action Prompt:** Slow dolly in toward his reflection rippling in the water droplets on the sink's surface, steam of his breath faintly visible, calm and reset.

### 10 · Técnica 2 (6:33-7:19) — el reencuadre, bucle con la escena 1
**{PLANO}:** Medium shot
**Scene:** he sits at the same conference table as the opening scene, but now composed, taking one slow breath before speaking, a faint, steady focus in his eyes.
**Video Action Prompt:** Slow push-in mirroring the very first scene's camera move exactly, but steadier and calmer this time, quiet confidence.

### 11 · Técnica 3 (7:19-8:20) — micro-exposiciones, inoculación al estrés
**{PLANO}:** Medium shot, low-stakes presentation
**Scene:** he stands at the front of a small meeting room, gesturing calmly while speaking to three colleagues seated around a table, a simple whiteboard behind him, relaxed and steady posture.
**Video Action Prompt:** Smooth slow orbit around him as he speaks, colleagues nodding attentively, warm confident lighting, steady and assured.

### 12 · Conclusión (8:20-9:13) — la resiliencia es entrenable
**{PLANO}:** Wide shot, low angle
**Scene:** wide shot of him walking out of an office building entrance into full daylight, shoulders relaxed, the city open and bright ahead of him.
**Video Action Prompt:** Camera slowly pulls back and cranes upward, revealing the wide bright street as he walks confidently into it, uplifting and open.

---

## Notas de continuidad y ritmo
- Escena 10 repite deliberadamente el encuadre exacto de Escena 1 (mismo push-in, misma mesa) — dispositivo de "cierre en bucle" de `PLAYBOOK_MONETIZACION.md` §3, aplicado visualmente al bloqueo mental resuelto.
- Alternancia de plano revisada, sin dos planos iguales seguidos: medio → primerísimo plano → picado bajo → picado alto → general → medio-tras → medio-frontal → primer plano perfil → primer plano hombro → medio (bucle) → medio-orbit → general/contrapicado.
- Escena 7 (CTA) es la única con el host mirando directo a cámara — coherente con que en el guion es el único momento de segunda persona directa ("I have a question for you").
- Siguiendo `MANUAL_PRODUCCION.md` §3.1 (ritmo de corte tipo documental premiado, ~15s por plano visible dentro de cada bloque narrativo de 45-60s): esta v2 todavía genera **1 clip por escena narrativa**, no 3-5 sub-planos por escena. Es la vía correcta para esta primera regeneración (más simple, más barata, ya validada). Subdividir cada escena en 3-5 sub-planos más cortos es la mejora natural para la SIGUIENTE iteración, una vez el canal tenga volumen — anotado, no bloquea lanzar esto ahora.
- Ficha de personaje y cláusula negativa van COMPLETAS en las 12 — nunca abreviar entre escenas (Técnica B).

---

## v3 — Arquitectura de sub-planos (2026-08-25, Decisión 2 de Kimi)

**Reemplaza la nota de la línea anterior ("1 clip por escena, subdividir es la mejora de la siguiente iteración") — Kimi decidió que la subdivisión SÍ va desde ya**, en `HANDOFF_2026-08-25_decision_tercera_via_resiliencia.md` Decisión 2, tras el rechazo real de David al resultado de 1-clip-y-frame-congelado ("se ve muy cuadriculado... no hay transiciones cinematográficas"). Reglas que aplican a las 12 escenas de abajo:
- **3 sub-planos reales por escena**, sumando la duración total del bloque (columna "Duración" de la tabla de timestamps).
- **Ningún sub-plano puede sostenerse como frame congelado más de 4s** — si un tramo necesita más quietud narrativa, se cubre con movimiento de cámara lento (push/pan/tilt), nunca con un still puro.
- **Transición distinta entre cada par de sub-planos** dentro del video completo — nunca repetir el mismo tipo de corte/fundido en las 12 escenas seguidas.
- El **sub-plano A de cada escena reutiliza el still ya generado en Recraft** (el "plano principal", ver `handoffs/REPORTE_2026-08-25_12_escenas_recraft_listas.md`) — es la única imagen ya pagada. **Los sub-planos B y C son stills NUEVOS, todavía NO generados** — quedan aquí solo como especificación, a la espera de que Kimi confirme el presupuesto ajustado (ver handoff urgente activo) antes de gastar más créditos de Recraft.
- Fórmula de Video Action Prompt (4 partes, `MANUAL_PRODUCCION.md` §3.1): [Movimiento+Velocidad] + [Acción/qué se mueve] + [Qué revela] + [Tono].

### Escena 1 · Intro (48s total)
| Sub-plano | Duración | Plano | Composición (delta sobre el still principal) | Video Action Prompt | Transición al siguiente |
|---|---|---|---|---|---|
| A (still ya generado) | 18s | Medium shot | El ya existente: mesa de juntas, colegas desenfocados | Slow push-in toward his face as the room blurs, eyes widening slightly, tense and intimate | Crossfade suave (12 frames) |
| B (still nuevo) | 15s | Extreme close-up, manos | Sus manos sobre los papeles olvidados, temblor sutil | Static for a beat, then slow tilt up from his trembling hands to his blank stare, anxious and claustrophobic | Corte duro (silencio incómodo, coherente con el bloqueo) |
| C (still nuevo) | 15s | Picado alto (high angle) | Vista alta de toda la mesa, todos mirándolo a él, silla vacía en primer plano sugiriendo su punto de vista | Slow crane down from high angle toward his frozen face, dust motes in the light, unsettling and exposed | — (cierra el bloque) |

### Escena 2 · Anatomía del bloqueo (46s total)
| Sub-plano | Duración | Plano | Composición | Video Action Prompt | Transición |
|---|---|---|---|---|---|
| A (existente) | 16s | Extreme close-up, ojo | El ya generado: reflejo de la sala en la pupila | Static for a beat, then slow tilt down from his eye to his trembling hand, subtle handheld tremor, anxious | Corte duro |
| B (nuevo) | 15s | Primer plano, garganta/pecho | Su respiración entrecortada, cuello tenso | Slow dolly in on his tense throat as he swallows hard, shallow breathing visible, claustrophobic | Fundido a negro breve (0.3s, marca el quiebre emocional) |
| C (nuevo) | 15s | Plano medio, perfil | Perfil completo, papeles cayendo de su mano | Handheld camera trembles slightly as papers slip from his fingers, mirroring his panic, tense and intimate | Crossfade suave |

### Escena 3 · El detector de amenazas ancestral (49s total)
| Sub-plano | Duración | Plano | Composición | Video Action Prompt | Transición |
|---|---|---|---|---|---|
| A (existente) | 17s | Low-angle shot | El ya generado: puerta de oficina de noche, sombra tipo cueva | Camera slowly cranes upward from low angle, the shadowed doorway looming larger, dust in a cold light shaft, dramatic | Corte duro |
| B (nuevo) | 16s | Primerísimo primer plano, ojos | Sus ojos muy abiertos reflejando la sombra | Slow push-in on his wide eyes as the shadow reflection grows, breath held, unsettling | Whip pan rápido (único uso permitido de velocidad rápida, giro de shock puntual) |
| C (nuevo) | 16s | Picado bajo extremo | Silueta completa contra la puerta, ahora diminuto en el encuadre | Wide low-angle static hold with slow zoom in, emphasizing how small he looks against the door, dramatic and unsettling | — (cierra el bloque) |

### Escena 4 · Carga alostática, estrés crónico (50s total)
| Sub-plano | Duración | Plano | Composición | Video Action Prompt | Transición |
|---|---|---|---|---|---|
| A (existente) | 17s | Overhead shot | El ya generado: escritorio desordenado, teléfono vibrando | Slow zoom in on the buzzing phone, then gentle pan across the desk, cold blue city light, tense and exhausted | Crossfade suave |
| B (nuevo) | 17s | Primer plano, taza de café fría | Vapor que ya no sale, mancha de café seca | Slow dolly in on the cold coffee cup, condensation gone, steady and heavy, exhausted mood | Corte duro |
| C (nuevo) | 16s | Plano medio desde la ventana | Su silueta contra el skyline oscureciéndose, encorvado sobre el escritorio | Static wide hold from outside the window looking in, city lights flickering on around his silhouette, isolating and tense | — (cierra el bloque) |

### Escena 5 · Indefensión aprendida (43s total)
| Sub-plano | Duración | Plano | Composición | Video Action Prompt | Transición |
|---|---|---|---|---|---|
| A (existente) | 15s | Wide shot | El ya generado: sentado solo, puerta entreabierta con luz cálida | Static wide shot held for a long beat, only the light through the door flickering, quiet and heavy stillness | Fundido a negro breve |
| B (nuevo) | 14s | Primer plano, rostro | Su mirada perdida, sin mirar hacia la puerta/luz | Slow push-in on his blank stare, unmoving, the warm light reflected faintly in his unfocused eyes, heavy | Corte duro |
| C (nuevo) | 14s | Plano medio, manos sobre las rodillas | Manos inertes, postura derrotada | Static hold on his slack hands resting on his knees, only his shallow breathing moving the frame, quiet and heavy | — (cierra el bloque, el más lento/quieto del video a propósito) |

### Escena 6 · El giro hacia los recursos internos (44s total)
| Sub-plano | Duración | Plano | Composición | Video Action Prompt | Transición |
|---|---|---|---|---|---|
| A (existente) | 15s | Medium shot from behind | El ya generado: se levanta, camina hacia la puerta | Tracking shot behind him as he walks toward the light, camera slowly rising with him, hopeful, warm rim light increasing | Crossfade suave |
| B (nuevo) | 15s | Primer plano, pies/pasos | Sus pasos decididos cruzando el suelo iluminándose | Ground-level tracking shot runs inches above the floor alongside his steps, light spreading with each step, building | Corte duro |
| C (nuevo) | 14s | Plano medio frontal, en el umbral | Su rostro iluminado de lleno al cruzar el umbral | Slow dolly in on his face as warm golden light washes over it fully, determined and building | — (cierra el bloque) |

### Escena 7 · CTA, dirigiéndose al espectador (34s total)
| Sub-plano | Duración | Plano | Composición | Video Action Prompt | Transición |
|---|---|---|---|---|---|
| A (existente) | 17s | Medium close-up, direct address | El ya generado: mirando directo a cámara | Still camera. He looks directly toward the camera as if speaking to the viewer, a thoughtful pause, quiet and direct | Corte duro (único bloque de 2 sub-planos, es el más corto e íntimo — no fuerza un 3º plano innecesario) |
| B (nuevo) | 17s | Primer plano, mismo encuadre, más cerca | Push-in sobre el mismo plano A, sin cambiar posición — refuerza la intimidad del CTA | Slow push-in tightening on his face, a small nod, still speaking directly to the viewer, quiet and direct | — (cierra el bloque) |

### Escena 8 · El suspiro fisiológico (39s total)
| Sub-plano | Duración | Plano | Composición | Video Action Prompt | Transición |
|---|---|---|---|---|---|
| A (existente) | 13s | Close-up, side profile | El ya generado (regenerado tras QA, sin oreja): ventana al amanecer | Slow dolly in on his profile as he exhales slowly, shoulders relaxing, calm and deliberate | Crossfade suave |
| B (nuevo) | 13s | Primerísimo primer plano, nariz/boca | El aire visible al exhalar en el frío | Static macro hold on his exhale, breath faintly visible in the cool morning light, calm and deliberate | Corte duro |
| C (nuevo) | 13s | Plano medio, espalda/hombros | Hombros que se relajan visiblemente | Slow tilt down from his relaxing shoulders to his open hands, released tension, calm and reset | — (cierra el bloque) |

### Escena 9 · El reflejo de inmersión (40s total)
| Sub-plano | Duración | Plano | Composición | Video Action Prompt | Transición |
|---|---|---|---|---|---|
| A (existente) | 14s | Close-up over the shoulder | El ya generado: lavabo, agua fría | Slow dolly in toward his reflection rippling in the water droplets, steam of his breath, calm and reset | Fundido a negro breve |
| B (nuevo) | 13s | Primerísimo primer plano, gotas de agua | Gotas cayendo del rostro | Static macro hold on water droplets falling from his jaw, catching the light, calm and deliberate | Corte duro |
| C (nuevo) | 13s | Plano medio frontal, mirándose al espejo | Su rostro reseteado, mirada más clara | Slow push-in on his reflection in the mirror, calmer eyes now, steady and reset | — (cierra el bloque) |

### Escena 10 · El reencuadre, bucle con la escena 1 (46s total)
| Sub-plano | Duración | Plano | Composición | Video Action Prompt | Transición |
|---|---|---|---|---|---|
| A (existente) | 16s | Medium shot | El ya generado: misma mesa, ahora compuesto | Slow push-in mirroring the very first scene's camera move exactly, steadier and calmer, quiet confidence | Crossfade suave (deliberadamente igual a la transición de apertura de la escena 1, refuerza el bucle) |
| B (nuevo) | 15s | Primer plano, manos quietas sobre la mesa | Sin temblor esta vez — contraste directo con escena 1B | Static hold on his steady hands resting on the table, no tremor, calm confidence | Corte duro |
| C (nuevo) | 15s | Plano medio-alto, la sala completa | Todos lo miran, él ya no se ve pequeño | Slow crane down mirroring scene 1's high angle, but he now holds the room's attention with steady posture, assured | — (cierra el bloque) |

### Escena 11 · Micro-exposiciones, inoculación al estrés (61s total — el bloque más largo, justifica 3 sub-planos completos)
**Nota de estilo obligatoria:** los 3 colegas deben mantener el mismo estilo plano 2D del personaje principal en los 3 sub-planos (sin orejas, sin nariz, mismos ojos ovalados) — ya validado en el still A, replicar exacto en B y C. **Además: la escena 11 ya generada tiene un defecto (burbuja de cómic vacía de fondo) pendiente de corregir con "Remove speech bubble" antes de animar el sub-plano A.**
| Sub-plano | Duración | Plano | Composición | Video Action Prompt | Transición |
|---|---|---|---|---|---|
| A (existente, con defecto a corregir) | 21s | Medium shot | El ya generado: presentando a 3 colegas | Smooth slow orbit around him as he speaks, colleagues nodding attentively, warm confident lighting, steady | Crossfade suave |
| B (nuevo) | 20s | Plano medio, reacción de los colegas | Los 3 colegas asintiendo, mismo estilo visual | Slow pan across the three colleagues nodding attentively, warm lighting, steady and assured | Corte duro |
| C (nuevo) | 20s | Primer plano, él señalando el whiteboard | Gesto calmado hacia el whiteboard | Static hold with a slow push-in as he gestures calmly toward the whiteboard, confident and measured | — (cierra el bloque) |

### Escena 12 · Conclusión (54s total)
| Sub-plano | Duración | Plano | Composición | Video Action Prompt | Transición |
|---|---|---|---|---|---|
| A (existente) | 18s | Wide shot, low angle | El ya generado: saliendo del edificio a la luz del día | Camera slowly pulls back and cranes upward, revealing the wide bright street as he walks into it, uplifting and open | Crossfade suave |
| B (nuevo) | 18s | Plano medio, caminando hacia cámara | Avanza con hombros relajados, ciudad de fondo desenfocada | Slow tracking shot moving backward in front of him as he walks steadily forward, city softly blurred behind, open and confident | Corte duro |
| C (nuevo) | 18s | Plano general, grúa ascendente final | Toma final elevándose, la ciudad entera abierta ante él | Wide cinematic crane shot pulls upward and back, revealing the full bright city as he walks confidently into the horizon, uplifting | — (fin del video, fundido final) |

---

## Cómo lanzar (cuando se confirme)
Por cada fila de la tabla, un comando:
```bash
python generate_video.py scene \
  --image-prompt "<prefijo de personaje> {PLANO} of... Scene: <texto de la escena>. <sufijo de luz> <cláusula negativa>" \
  --motion "<Video Action Prompt de la fila>" \
  --out resilience_scene_01.mp4
```
Recomendado: lanzar de a una, revisar el resultado visualmente (estilo + consistencia del personaje) antes de seguir con la siguiente — más lento pero evita gastar las 12 sin detectar un problema temprano.
