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
Soft painterly digital illustration in the style of a modern animated explainer short, 2D stylised animation, not anime. {PLANO} of a young man drawn with deliberately simplified cartoon proportions: a VERY LARGE round smooth head about one third of his total height, a completely smooth bald head shape with NO visible hair at all, a dark navy baseball cap sitting directly on that smooth head. His face is extremely minimal: two small plain solid black oval eyes with no iris, no highlight and no eyelashes, two thin short dark eyebrows, a tiny dot nose and a small simple line mouth. Flat pale cream skin with soft even shading and NO blush, NO pink cheeks. Small simple body in a grey hoodie, dark jeans and sneakers.
```

**Sufijo de luz/estilo (pegar al final de cada Image Prompt, antes de la cláusula negativa):**
```
Rich atmospheric cinematic lighting, warm rim light, volumetric light shafts, floating dust particles. Muted harmonious colour palette. Full-bleed single scene with real environmental depth and a detailed background. Clean soft linework, gentle painterly shading.
```

**Cláusula negativa (pegar siempre al final, cierra el Image Prompt):**
```
Absolutely NO halftone dots, NO ben-day dots, NO starburst or speed lines, NO comic panels, NO white gutters, NO speech bubbles, NO anime face, NO detailed irises, NO visible hair, NO blush, NO sharp jawline, NO photorealism, and NO text, letters, signs or words anywhere in the image.
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

## Cómo lanzar (cuando se confirme)
Por cada fila de la tabla, un comando:
```bash
python generate_video.py scene \
  --image-prompt "<prefijo de personaje> {PLANO} of... Scene: <texto de la escena>. <sufijo de luz> <cláusula negativa>" \
  --motion "<Video Action Prompt de la fila>" \
  --out resilience_scene_01.mp4
```
Recomendado: lanzar de a una, revisar el resultado visualmente (estilo + consistencia del personaje) antes de seguir con la siguiente — más lento pero evita gastar las 12 sin detectar un problema temprano.
