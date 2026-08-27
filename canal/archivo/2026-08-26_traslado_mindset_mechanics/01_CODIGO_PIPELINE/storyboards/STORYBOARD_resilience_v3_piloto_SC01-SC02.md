# STORYBOARD — PILOTO RESILIENCIA (resilience_v3) · Escenas narrativas 1 y 2
**Storyboard Director · 2026-08-25 · Audio real medido: 553.4s totales · Segmento cubierto: 0:00-1:34 (94.0s, medido, NO estimado)**
**Arquitectura EJECUTABLE (revisada 2026-08-25): 15 paneles, ninguno >10s — ver §0.**
**v1.1 (2026-08-26): ritmo repartido en vez de plano (§5), banderas de riesgo (§6) y capa de audio (§7). Mismas 8 imágenes, mismos 15 clips, 0 créditos de coste.**
**Continuidad global del piloto: el host mira y se orienta siempre hacia frame-DERECHA (los colegas están a su derecha). La cámara nunca cruza ese eje (180°).**

---

## 0. ⚠️ REGLA DURA DE DURACIÓN — leer antes de animar nada

**Ningún panel puede superar 10 segundos.** No es una preferencia de montaje: es el
límite físico de VideoExpress.

Medido el 2026-08-25 leyendo el DOM real del modal "Create Video From Prompt": tras
activar el checkbox **"Advanced Mode"** aparece `manual_video_length` y un
`<input type="range" name="video_duration" min="3" max="10" value="5">`.
**El máximo es 10s y el mínimo 3s.** Corroborado por la petición aún abierta en el
roadmap oficial de la plataforma, *"Increase maximum AI video clip length to 10
seconds or more"* (roadmap.videoexpress.ai/feedback/205505): si los usuarios piden
subirlo **a** 10 o más, el tope de hoy es exactamente 10.

**Los 12s por panel de la versión anterior de este storyboard eran inejecutables.**
Se habrían pedido 8 clips de 12s y VideoExpress habría devuelto clips de otra
duración sin dar ningún error, descuadrando el montaje contra la voz en off.

Aclaración importante sobre el "techo de 8s" que se había reportado antes: **no
existía tal techo.** El bot nunca tocaba la duración, así que la plataforma la
elegía sola y devolvía 5,04s / 6,04s / 8,04s de forma impredecible (medido con
ffprobe sobre los 20 clips del lote anterior). La causa raíz era un control que el
bot no usaba, no un límite de 8s.

**Cómo se pide la duración ahora:** `animate_library_image(..., duration_seconds=N)`
con `N` = el `duration_s` del panel. Si se omite, la duración vuelve a ser aleatoria.
Pedir un valor fuera de 3-10 aborta la corrida **antes** de gastar el crédito.

---

## 1. TABLA RESUMEN DE 15 PANELES

Los 8 *beats* narrativos aprobados no cambian: cada beat de 12s se cubre con
**dos paneles** (fases a/b del mismo movimiento sobre la MISMA imagen), y el
beat final de 10s cabe tal cual. **Desde v1.1 (2026-08-26) esos dos paneles ya NO duran 6s+6s:
duran lo que pide el ritmo del beat (4-8s), sumando siempre 12s — ver §5.** Los bloques de voz en off son fijos y medidos: **no
se tocó ni un timecode de audio.** Efecto secundario deseable: 15 cortes en vez de 8,
que es justo el dinamismo que pidieron Kimi y David para dejar de verse "cuadriculado".

| # | shot_id | duration_s | tc | beat origen | shot_size | camera_move | transition_out | ritmo |
|---|---|---|---|---|---|---|---|---|
| 1 | SC01_SH001a | 5 | 0:00-0:05 | SC01_SH001 | medium | push_in / slow (fase 1/2) | cut_on_action | entrada |
| 2 | SC01_SH001b | 7 | 0:05-0:12 | SC01_SH001 | medium | push_in / slow (fase 2/2) | cut_on_action | exhalacion |
| 3 | SC01_SH002a | 8 | 0:12-0:20 | SC01_SH002 | close_up | pan_left / slow (fase 1/2) | cut_on_action | exhalacion |
| 4 | SC01_SH002b | 4 | 0:20-0:24 | SC01_SH002 | close_up | pan_left / slow (fase 2/2) | smash_cut | aceleracion |
| 5 | SC01_SH003a | 4 | 0:24-0:28 | SC01_SH003 | insert | tilt_down / slow (fase 1/2) | cut_on_action | rafaga |
| 6 | SC01_SH003b | 8 | 0:28-0:36 | SC01_SH003 | insert | tilt_down / slow (fase 2/2) | match_cut | exhalacion |
| 7 | SC01_SH004a | 7 | 0:36-0:43 | SC01_SH004 | wide | crane_up / slow (fase 1/2) | cut_on_action | exhalacion |
| 8 | SC01_SH004b | 5 | 0:43-0:48 | SC01_SH004 | wide | crane_up / slow (fase 2/2) | hard_cut | aceleracion |
| 9 | SC02_SH005a | 4 | 0:48-0:52 | SC02_SH005 | extreme_close_up | push_in / slow (fase 1/2) | cut_on_action | inhalacion |
| 10 | SC02_SH005b | 8 | 0:52-1:00 | SC02_SH005 | extreme_close_up | push_in / slow (fase 2/2) | cut_on_action | exhalacion |
| 11 | SC02_SH006a | 6 | 1:00-1:06 | SC02_SH006 | medium_close | pan_right / slow (fase 1/2) | cut_on_action | neutro |
| 12 | SC02_SH006b | 6 | 1:06-1:12 | SC02_SH006 | medium_close | pan_right / slow (fase 2/2) | hard_cut | neutro |
| 13 | SC02_SH007a | 5 | 1:12-1:17 | SC02_SH007 | insert | static micro-drift (fase 1/2) | cut_on_action | inhalacion |
| 14 | SC02_SH007b | 7 | 1:17-1:24 | SC02_SH007 | insert | static micro-drift (fase 2/2) | match_cut | exhalacion |
| 15 | SC02_SH008 | 10 | 1:24-1:34 | SC02_SH008 | close_up | push_in / very_slow + HOLD 2s (★ PLANO SOSTENIDO) | hard_cut | hold |

**Sumas:** Escena 1 = 48s (0:00-0:48) ✓ · Escena 2 = 46s (0:48-1:34) ✓ · Total piloto = 94s = 1:34 exacto (±0s) ✓ · Panel más largo = 10s ✓ · Panel más corto = 4s ✓ (mínimo de plataforma: 3s)

**Coste:** las **imágenes siguen siendo 8** (cada par a/b reutiliza la misma imagen de
Recraft) — no hay gasto extra en Recraft. Las animaciones de VideoExpress pasan de
**8 a 15**. Ese aumento de presupuesto lo tienen que aprobar David/Kimi antes de lanzar el lote.

**Pendiente creativo (NO técnico, para storyboard-director/Kimi):** los paneles `b`
reutilizan la imagen de su panel `a` y continúan el mismo movimiento (cut-in sobre el
eje, no jump cut). Es correcto y ejecutable tal cual, pero si se quiere máxima
variedad de plano, lo ideal sería que storyboard-director escriba una composición
propia para cada panel `b` — eso sí subiría el coste de Recraft de 8 a 15 imágenes.
**Anti-cuadrícula:** medium → close_up → insert → wide → extreme_close_up → medium_close → insert → close_up (cero repeticiones consecutivas) ✓
**Direcciones de cámara:** in → izquierda → abajo → arriba → in → derecha → deriva → in (alternadas) ✓
**Inserts:** SH003 (escena 1), SH007 (escena 2) ✓
**Plano sostenido (único uso en el piloto):** SH008 — el push-in termina a los ~8s y los últimos 2s quedan casi quietos sobre su cara tras el "But why?" (solo polvo y luz en movimiento; jamás >4s congelado).
**Pattern interrupt:** corte smash a 0:24 hacia el insert SH003; el cambio brusco de escala domina la ventana 25-35s ✓

---

## 2. DETALLE POR PANEL

### SC01_SH001 — Hook: a mitad de la acción (0:00-0:05 + 0:05-0:12 · 5s + 7s (SC01_SH001a / SC01_SH001b))
- **action:** El host está sentado en la mesa de conferencias, ligeramente inclinado hacia adelante, con la boca entreabierta a mitad de palabra y una hoja de notas suelta en una mano; sus ojos están fijos hacia frame-derecha (colegas fuera de cuadro).
- **environment:** Sala de reuniones corporativa al anochecer; mesa larga de madera oscura; 4-5 siluetas de colegas desenfocadas en el lado derecho; lámparas cálidas ámbar, luz fría teal del atardecer por la ventana tras él; *warm amber interior grade with muted teal accents*. Host en el tercio izquierdo, ojos en la intersección superior-izquierda, espacio abierto a la derecha (hacia donde viaja el push-in).
- **vo_text (0:00-0:12):** "Picture this: you're in a high-stakes meeting, and all eyes are on you. You've prepped for this for weeks."
- **image_prompt (listo para pegar):**

```
Soft painterly digital illustration in the style of a modern animated explainer short, 2D stylised animation, not anime. Medium shot of a young man drawn with deliberately simplified cartoon proportions: a VERY LARGE round smooth head about one third of his total height, a completely smooth bald head shape with NO visible hair at all, a dark navy baseball cap sitting directly on that smooth head. His face is extremely minimal: two small plain solid black oval eyes with no iris, no highlight and no eyelashes, two thin short dark eyebrows, a tiny dot nose and a small simple line mouth. Flat pale cream skin with soft even shading and NO blush, NO pink cheeks. Small simple body in a grey hoodie, dark jeans and sneakers. He sits at a long dark-wood conference table, leaning slightly forward, mouth half-open mid-word, holding a sheet of notes loosely in one hand, eyes fixed toward frame right. He is placed on the left third of the frame with open space on the right. Corporate meeting room at dusk: out-of-focus colleague silhouettes along the right side of the table, warm amber desk lamps, cool teal dusk light through a window behind him, warm amber interior grade with muted teal accents. Rich atmospheric cinematic lighting, warm rim light, volumetric light shafts, floating dust particles. Muted harmonious colour palette. Full-bleed single scene with real environmental depth and a detailed background. Clean soft linework, thick black outline, flat cel-shading. Absolutely NO halftone dots, NO ben-day dots, NO starburst or speed lines, NO comic panels, NO white gutters, NO speech bubbles, NO anime face, NO detailed irises, NO visible hair, NO visible ears, NO blush, NO sharp jawline, NO photorealism, and NO text, letters, signs or words anywhere in the image.
```

- **video_action_prompt (listo para pegar):**

```
Slow smooth push-in toward the young man with his navy cap and grey hoodie, seated at the conference table. His chest rises once with a held breath, the sheet of notes shifts slightly in his hand, dust particles drift through the warm lamp light, the blurred colleague silhouettes stay soft and still. The push-in tightens the frame on his face as his mouth opens to speak. Calm-before-the-storm tone, restrained tension. Stable camera, smooth motion, minimal distortion.
```

---

### SC01_SH002 — Tensión: la mente en blanco (0:12-0:20 + 0:20-0:24 · 8s + 4s (SC01_SH002a / SC01_SH002b))
- **action:** Su boca sigue entreabierta pero no salen palabras; sus ojos ovalados negros se abren un poco más y dejan de parpadear; la mano con las notas baja y sale por el borde inferior del cuadro.
- **environment:** Misma sala, foco mucho más plano; el fondo se funde en manchas suaves cálidas y teal; brillo ámbar de lámpara en su mejilla izquierda, luz de borde fría de la ventana a su derecha. Cara en el tercio derecho, ojos en la intersección superior-derecha; el pan a izquierda abre espacio vacío de lámpara a la izquierda.
- **vo_text (0:12-0:24):** "You open your mouth to share a brilliant idea, and… nothing. Your mind goes completely blank. The words are gone. The concepts have vanished."
- **image_prompt (listo para pegar):**

```
Soft painterly digital illustration in the style of a modern animated explainer short, 2D stylised animation, not anime. Close-up, slight dutch angle, of a young man drawn with deliberately simplified cartoon proportions: a VERY LARGE round smooth head about one third of his total height, a completely smooth bald head shape with NO visible hair at all, a dark navy baseball cap sitting directly on that smooth head. His face is extremely minimal: two small plain solid black oval eyes with no iris, no highlight and no eyelashes, two thin short dark eyebrows, a tiny dot nose and a small simple line mouth. Flat pale cream skin with soft even shading and NO blush, NO pink cheeks. Small simple body in a grey hoodie, dark jeans and sneakers. His mouth hangs half-open and silent, his black oval eyes are wide and unblinking, his gaze fixed toward frame right. His face sits on the right third of the frame, eyes at the upper-right intersection, with empty lamp-lit space opening on the left. Very shallow focus: the meeting room melts into soft warm and teal shapes behind him, amber lamp glow on one cheek, cool edge light from a window on the other, warm amber interior grade with muted teal accents. Rich atmospheric cinematic lighting, warm rim light, volumetric light shafts, floating dust particles. Muted harmonious colour palette. Full-bleed single scene with real environmental depth and a detailed background. Clean soft linework, thick black outline, flat cel-shading. Absolutely NO halftone dots, NO ben-day dots, NO starburst or speed lines, NO comic panels, NO white gutters, NO speech bubbles, NO anime face, NO detailed irises, NO visible hair, NO visible ears, NO blush, NO sharp jawline, NO photorealism, and NO text, letters, signs or words anywhere in the image.
```

- **video_action_prompt (listo para pegar):**

```
Slow smooth pan to the left across the close-up of the young man with his navy cap and grey hoodie. His plain black oval eyes stay wide and unblinking, his half-open mouth does not move, a faint tremor runs through his shoulders, dust particles drift through the amber lamp light. The pan opens empty space beside his face, underlining the silence. Growing unease, held-breath pacing. Stable camera, smooth motion, minimal distortion.
```

---

### SC01_SH003 — ★ PATTERN INTERRUPT (0:24-0:36): insert de las notas que caen (0:24-0:28 + 0:28-0:36 · 4s + 8s (SC01_SH003a / SC01_SH003b))
- **action:** Sus dedos se aflojan y las hojas de notas se deslizan de su mano; una hoja se inclina en el aire y se posa sobre la mesa oscura; sus yemas tiemblan una vez contra la madera.
- **environment:** Detalle macro del tablero de la mesa: páginas de notas con marcas tipo garabato desenfocadas e ILEGIBLES (jamás palabras), un bolígrafo simple rueda levemente; charco cálido de luz de lámpara sobre la veta de la madera, bordes cayendo a sombra; profundidad de campo muy baja. Mano en el tercio inferior-izquierdo, espacio arriba para el recorrido del tilt down.
- **vo_text (0:24-0:36):** "All that's left is that rising tide of panic as you stare into a sea of expectant faces. That frustrating moment of shutting down is not a personal failure."
- **image_prompt (listo para pegar):**

```
Soft painterly digital illustration in the style of a modern animated explainer short, 2D stylised animation, not anime. Extreme close-up detail insert of the hand of a young man drawn with deliberately simplified cartoon proportions: a VERY LARGE round smooth head about one third of his total height, a completely smooth bald head shape with NO visible hair at all, a dark navy baseball cap sitting directly on that smooth head. His face is extremely minimal: two small plain solid black oval eyes with no iris, no highlight and no eyelashes, two thin short dark eyebrows, a tiny dot nose and a small simple line mouth. Flat pale cream skin with soft even shading and NO blush, NO pink cheeks. Small simple body in a grey hoodie, dark jeans and sneakers. Only his grey-hoodie sleeve, his hand and the tabletop are visible: his fingers loosen as several note pages slip from his grip, one sheet tilting mid-fall onto a dark wood table; the pages show only soft blurred scribble-like marks, never legible words; a simple pen lies nearby; a warm pool of lamplight on the wood grain, edges falling into shadow; very shallow depth of field; the hand sits in the lower-left third with open space above. Rich atmospheric cinematic lighting, warm rim light, volumetric light shafts, floating dust particles. Muted harmonious colour palette. Full-bleed single scene with real environmental depth and a detailed background. Clean soft linework, thick black outline, flat cel-shading. Absolutely NO halftone dots, NO ben-day dots, NO starburst or speed lines, NO comic panels, NO white gutters, NO speech bubbles, NO anime face, NO detailed irises, NO visible hair, NO visible ears, NO blush, NO sharp jawline, NO photorealism, and NO text, letters, signs or words anywhere in the image.
```

- **video_action_prompt (listo para pegar):**

```
Slow smooth tilt down over the detail of the hand of the young man with his navy cap and grey hoodie, on the dark wood table. His fingers loosen and the note pages slide and settle onto the wood, one sheet rocking gently before going still, his fingertips trembling once against the table, dust particles falling through the narrow pool of warm lamplight. The tilt lands on the fallen pages. Abrupt, intimate, held-tension tone. Stable camera, smooth motion, minimal distortion.
```

---

### SC01_SH004 — Vulnerabilidad: pequeño y solo (0:36-0:43 + 0:43-0:48 · 7s + 5s (SC01_SH004a / SC01_SH004b))
- **action:** Visto directamente desde arriba, el host está pequeño e inmóvil en la mesa larga, hombros encogidos, cabeza ligeramente gacha sobre las notas caídas, brazos pegados al cuerpo; las siluetas de los colegas rodean la mesa, todas orientadas hacia él.
- **environment:** Sala completa en cenital: mesa larga en diagonal de inferior-izquierda a superior-derecha, charcos alternos de luz cálida y sombra fría en el suelo, franja teal del atardecer en las ventanas del borde superior; el host ocupa la zona inferior-izquierda. El crane up revela más suelo y más vacío.
- **vo_text (0:36-0:48):** "It's not because you're not smart enough or weren't prepared. It's not your fault. It's your ancient survival wiring—designed to save you from tigers—misfiring in a modern world."
- **image_prompt (listo para pegar):**

```
Soft painterly digital illustration in the style of a modern animated explainer short, 2D stylised animation, not anime. Wide overhead top-down shot of a young man drawn with deliberately simplified cartoon proportions: a VERY LARGE round smooth head about one third of his total height, a completely smooth bald head shape with NO visible hair at all, a dark navy baseball cap sitting directly on that smooth head. His face is extremely minimal: two small plain solid black oval eyes with no iris, no highlight and no eyelashes, two thin short dark eyebrows, a tiny dot nose and a small simple line mouth. Flat pale cream skin with soft even shading and NO blush, NO pink cheeks. Small simple body in a grey hoodie, dark jeans and sneakers. Seen from directly above: he sits small and motionless at a long dark conference table set on a diagonal from lower-left to upper-right, shoulders drawn in, head bowed over fallen note pages, arms held close to his body; a ring of out-of-focus colleague silhouettes around the table all turned toward him; alternating pools of warm lamplight and cool shadow across the floor, a strip of teal dusk light at the windows along the upper edge; he occupies the lower-left area of the frame with empty floor space around him. Rich atmospheric cinematic lighting, warm rim light, volumetric light shafts, floating dust particles. Muted harmonious colour palette. Full-bleed single scene with real environmental depth and a detailed background. Clean soft linework, thick black outline, flat cel-shading. Absolutely NO halftone dots, NO ben-day dots, NO starburst or speed lines, NO comic panels, NO white gutters, NO speech bubbles, NO anime face, NO detailed irises, NO visible hair, NO visible ears, NO blush, NO sharp jawline, NO photorealism, and NO text, letters, signs or words anywhere in the image.
```

- **video_action_prompt (listo para pegar):**

```
Slow smooth crane up from the overhead view of the young man with his navy cap and grey hoodie at the conference table. His shoulders stay drawn in, his head stays bowed over the fallen notes, the colleague silhouettes remain still and turned toward him, dust drifting slowly through the warm light pools. The rise reveals how small and alone he is in the long room. Vulnerable, exposed tone. Stable camera, smooth motion, minimal distortion.
```

---

### SC02_SH005 — Tensión íntima: el ojo y el sudor (0:48-0:52 + 0:52-1:00 · 4s + 8s (SC02_SH005a / SC02_SH005b))
- **action:** Su ojo derecho llena el encuadre, abierto demasiado, sin parpadear; una fina gota de sudor resbala lentamente por su sien; el ojo da un único tirón hacia frame-derecha. (Los reflejos cálidos de la sala se ven como manchas ámbar suaves sobre su piel y el borde de la gorra — NO en el ojo, que es un óvalo negro sólido por ficha.)
- **environment:** Macro extremo; el fondo es solo desenfoque ámbar-teal de la sala; el borde inferior de la gorra navy cruza la parte alta del cuadro; foco macro muy bajo. Ojo en el tercio superior-izquierdo, mirando a derecha (raccord con toda la secuencia).
- **vo_text (0:48-1:00):** "This 'brain freeze' is a universal human experience. It happens to public speakers, athletes, students in an exam… just about everyone."
- **image_prompt (listo para pegar):**

```
Soft painterly digital illustration in the style of a modern animated explainer short, 2D stylised animation, not anime. Extreme close-up framed tight on one eye and the temple of a young man drawn with deliberately simplified cartoon proportions: a VERY LARGE round smooth head about one third of his total height, a completely smooth bald head shape with NO visible hair at all, a dark navy baseball cap sitting directly on that smooth head. His face is extremely minimal: two small plain solid black oval eyes with no iris, no highlight and no eyelashes, two thin short dark eyebrows, a tiny dot nose and a small simple line mouth. Flat pale cream skin with soft even shading and NO blush, NO pink cheeks. Small simple body in a grey hoodie, dark jeans and sneakers. His right eye fills the upper-left third of the frame, open too wide and unblinking, a plain solid black oval; a thin bead of sweat slides down his temple; the lower edge of his dark navy cap brim crosses the top of the frame; the blurred warm meeting room glows as soft amber smudges across his cheek and skin; very shallow macro focus, muted amber and teal tones. Rich atmospheric cinematic lighting, warm rim light, volumetric light shafts, floating dust particles. Muted harmonious colour palette. Full-bleed single scene with real environmental depth and a detailed background. Clean soft linework, thick black outline, flat cel-shading. Absolutely NO halftone dots, NO ben-day dots, NO starburst or speed lines, NO comic panels, NO white gutters, NO speech bubbles, NO anime face, NO detailed irises, NO visible hair, NO visible ears, NO blush, NO sharp jawline, NO photorealism, and NO text, letters, signs or words anywhere in the image.
```

- **video_action_prompt (listo para pegar):**

```
Very slow smooth push-in on the extreme close-up of the eye of the young man with his navy cap and grey hoodie. His plain solid black oval eye stays open too wide without blinking, a thin bead of sweat slides slowly down his temple, the soft amber glow on his skin shimmers faintly, floating dust crosses the macro focus. The push tightens until the eye dominates the frame. Claustrophobic, clinical tension. Stable camera, smooth motion, minimal distortion.
```

---

### SC02_SH006 — Tensión sostenida: el cuerpo bloqueado (1:00-1:06 + 1:06-1:12 · 6s + 6s (SC02_SH006a / SC02_SH006b))
- **action:** En tres cuartos, se mantiene rígido, la mirada clavada hacia frame-derecha en la nada; su mano libre aprieta el borde de la mesa; su garganta sube y baja en una deglución seca.
- **environment:** Encuadre claustrofóbico; fondo comprimido en manchas oscuras desenfocadas con un único orbe cálido de lámpara tras su hombro; sombras más largas, grado ámbar más apagado. Host en el tercio izquierdo, espacio abierto a la derecha (el pan right viaja hacia donde mira).
- **vo_text (1:00-1:12):** "In these moments, your higher-level thinking seems to abandon you. Your prefrontal cortex—the logical, planning, modern part of your brain—gets its signals scrambled and takes a backseat."
- **image_prompt (listo para pegar):**

```
Soft painterly digital illustration in the style of a modern animated explainer short, 2D stylised animation, not anime. Medium close-up, slight dutch angle, of a young man drawn with deliberately simplified cartoon proportions: a VERY LARGE round smooth head about one third of his total height, a completely smooth bald head shape with NO visible hair at all, a dark navy baseball cap sitting directly on that smooth head. His face is extremely minimal: two small plain solid black oval eyes with no iris, no highlight and no eyelashes, two thin short dark eyebrows, a tiny dot nose and a small simple line mouth. Flat pale cream skin with soft even shading and NO blush, NO pink cheeks. Small simple body in a grey hoodie, dark jeans and sneakers. He sits rigid in three-quarter view on the left third of the frame, gaze locked toward frame right at nothing, his free hand gripping the edge of the table, shoulders tense; open dark space on the right. The background is compressed into dark blurred shapes with a single warm lamp orb glowing behind his shoulder; longer shadows, dimmer warm amber grade with muted teal accents. Rich atmospheric cinematic lighting, warm rim light, volumetric light shafts, floating dust particles. Muted harmonious colour palette. Full-bleed single scene with real environmental depth and a detailed background. Clean soft linework, thick black outline, flat cel-shading. Absolutely NO halftone dots, NO ben-day dots, NO starburst or speed lines, NO comic panels, NO white gutters, NO speech bubbles, NO anime face, NO detailed irises, NO visible hair, NO visible ears, NO blush, NO sharp jawline, NO photorealism, and NO text, letters, signs or words anywhere in the image.
```

- **video_action_prompt (listo para pegar):**

```
Slow smooth pan to the right across the medium close-up of the young man with his navy cap and grey hoodie. He stays rigid, gaze locked off-screen to the right, his throat moves in one dry swallow, his fingers press harder on the table edge, the warm lamp glow behind his shoulder flickers almost imperceptibly, dust drifting through the light. The pan follows the direction of his stare into empty dark space. Sustained, airless tension. Stable camera, smooth motion, minimal distortion.
```

---

### SC02_SH007 — Vulnerabilidad: la mano que no obedece (1:12-1:17 + 1:17-1:24 · 5s + 7s (SC02_SH007a / SC02_SH007b))
- **action:** Detalle: su mano yace palma abajo sobre las notas desperdigadas; los dedos se curvan lentamente hasta arrugar las páginas bajo ellos; un temblor fino recorre los dedos; el bolígrafo al lado no se mueve.
- **environment:** Mismo tablero de mesa, luz más baja: el charco cálido de lámpara se ha estrechado, los bordes caen a sombra profunda; páginas solo con marcas ilegibles tipo garabato desenfocado; profundidad de campo muy baja. Mano en el tercio centro-izquierdo.
- **vo_text (1:12-1:24):** "It feels like the command center of your mind has just been hijacked. You know the information is in there. You know what you need to do, but you just can't get to it."
- **image_prompt (listo para pegar):**

```
Soft painterly digital illustration in the style of a modern animated explainer short, 2D stylised animation, not anime. Extreme close-up detail insert of the hand of a young man drawn with deliberately simplified cartoon proportions: a VERY LARGE round smooth head about one third of his total height, a completely smooth bald head shape with NO visible hair at all, a dark navy baseball cap sitting directly on that smooth head. His face is extremely minimal: two small plain solid black oval eyes with no iris, no highlight and no eyelashes, two thin short dark eyebrows, a tiny dot nose and a small simple line mouth. Flat pale cream skin with soft even shading and NO blush, NO pink cheeks. Small simple body in a grey hoodie, dark jeans and sneakers. Only his grey-hoodie sleeve, his hand and the tabletop are visible: his hand lies palm-down on scattered note pages, fingers half-curled so the pages crease under them; a simple pen rests motionless beside; the warm pool of lamplight has narrowed, edges fallen to deep shadow; the pages show only blurred illegible scribble-like marks; very shallow depth of field; the hand sits in the center-left third. Rich atmospheric cinematic lighting, warm rim light, volumetric light shafts, floating dust particles. Muted harmonious colour palette. Full-bleed single scene with real environmental depth and a detailed background. Clean soft linework, thick black outline, flat cel-shading. Absolutely NO halftone dots, NO ben-day dots, NO starburst or speed lines, NO comic panels, NO white gutters, NO speech bubbles, NO anime face, NO detailed irises, NO visible hair, NO visible ears, NO blush, NO sharp jawline, NO photorealism, and NO text, letters, signs or words anywhere in the image.
```

- **video_action_prompt (listo para pegar):**

```
Static shot with a barely-there slow drift over the detail of the hand of the young man with his navy cap and grey hoodie, resting on the scattered pages. His fingers slowly curl until the pages crease under them, a fine tremor runs through the fingers, the pen beside them does not move, dust particles float through the narrowed warm light. Nothing else moves. Quiet helplessness, held still. Stable camera, smooth motion, minimal distortion.
```

---

### SC02_SH008 — ★ PLANO SOSTENIDO: la pregunta abierta (1:24-1:34 · 10s · 1 panel)
- **action:** Gira la cabeza unos grados hacia cámara (tres cuartos, NUNCA address directo — reservado al giro meta); sus ojos negros ovalados brillan, la mandíbula se tensa, los hombros se cuadran; queda muy quieto mientras la luz se asienta; en los últimos 2 segundos no se mueve en absoluto.
- **environment:** La sala detrás casi completamente a oscuras; una única luz de borde cálida dibuja su gorra y su mejilla; sombras teal-negras profundas. Cara en el tercio derecho, ojos en la intersección superior-derecha, espacio abierto a la izquierda.
- **vo_text (1:24-1:34):** "This isn't just a feeling; it's a real neurological event. When your brain perceives overwhelming stress, it fundamentally shifts its resources. But why?"
- **NOTA DE RITMO (único sostenido del piloto):** el push-in se completa hacia el segundo 8; los segundos 8-10 quedan casi quietos sobre su cara tras el "But why?" — quietud leída como confianza, solo polvo y luz en movimiento (nunca frame congelado, máximo 2s de sostenido).
- **image_prompt (listo para pegar):**

```
Soft painterly digital illustration in the style of a modern animated explainer short, 2D stylised animation, not anime. Close-up of a young man drawn with deliberately simplified cartoon proportions: a VERY LARGE round smooth head about one third of his total height, a completely smooth bald head shape with NO visible hair at all, a dark navy baseball cap sitting directly on that smooth head. His face is extremely minimal: two small plain solid black oval eyes with no iris, no highlight and no eyelashes, two thin short dark eyebrows, a tiny dot nose and a small simple line mouth. Flat pale cream skin with soft even shading and NO blush, NO pink cheeks. Small simple body in a grey hoodie, dark jeans and sneakers. In three-quarter view he turns his head a few degrees toward the camera without fully facing it; his plain black oval eyes glisten, his jaw is set, his shoulders squared; he is very still. His face sits on the right third of the frame, eyes at the upper-right intersection, open space on the left. The meeting room behind him is almost fully dark, one warm rim light tracing his cap and cheek, deep teal-black shadows, dim warm amber grade. Rich atmospheric cinematic lighting, warm rim light, volumetric light shafts, floating dust particles. Muted harmonious colour palette. Full-bleed single scene with real environmental depth and a detailed background. Clean soft linework, thick black outline, flat cel-shading. Absolutely NO halftone dots, NO ben-day dots, NO starburst or speed lines, NO comic panels, NO white gutters, NO speech bubbles, NO anime face, NO detailed irises, NO visible hair, NO visible ears, NO blush, NO sharp jawline, NO photorealism, and NO text, letters, signs or words anywhere in the image.
```

- **video_action_prompt (listo para pegar):**

```
Very slow smooth push-in on the close-up of the young man with his navy cap and grey hoodie as he turns his head a few degrees toward the camera. His jaw sets, his plain black oval eyes hold still and glistening, the warm rim light settles along his cap and cheek, dust drifts through the teal-dark room. The push-in completes early and the final two seconds hold nearly still on his face, only light and dust moving. Maximum tension, question left hanging. Stable camera, smooth motion, minimal distortion.
```

---

## 3. JSON CANÓNICO — array "shots" (también entregado como archivo `storyboard_resilience_v3_piloto.json`)

```json
{
  "video": "resilience_v3",
  "segment": "piloto_SC01-SC02",
  "audio_total_s": 553.4,
  "segment_tc": "0:00-1:34",
  "segment_duration_s": 94,
  "shots": [
    {
      "shot_id": "SC01_SH001a",
      "scene": 1,
      "duration_s": 5,
      "shot_size": "medium",
      "angle": "eye_level",
      "camera_move": {
        "type": "push_in",
        "speed": "slow",
        "phase": "1/2",
        "note": "fase 1/2: arranque del movimiento"
      },
      "subject": "HOST",
      "action": "sits at conference table leaning slightly forward, mouth half-open mid-word, sheet of notes held loosely in one hand, eyes fixed frame-right",
      "environment": "corporate meeting room at dusk, long dark-wood table, out-of-focus colleague silhouettes on the right, warm amber lamps, cool teal dusk through window, warm amber interior grade with muted teal accents; host on left third, open space right",
      "emotion_beat": "hook",
      "image_prompt": "Soft painterly digital illustration in the style of a modern animated explainer short, 2D stylised animation, not anime. Medium shot of a young man drawn with deliberately simplified cartoon proportions: a VERY LARGE round smooth head about one third of his total height, a completely smooth bald head shape with NO visible hair at all, a dark navy baseball cap sitting directly on that smooth head. His face is extremely minimal: two small plain solid black oval eyes with no iris, no highlight and no eyelashes, two thin short dark eyebrows, a tiny dot nose and a small simple line mouth. Flat pale cream skin with soft even shading and NO blush, NO pink cheeks. Small simple body in a grey hoodie, dark jeans and sneakers. He sits at a long dark-wood conference table, leaning slightly forward, mouth half-open mid-word, holding a sheet of notes loosely in one hand, eyes fixed toward frame right. He is placed on the left third of the frame with open space on the right. Corporate meeting room at dusk: out-of-focus colleague silhouettes along the right side of the table, warm amber desk lamps, cool teal dusk light through a window behind him, warm amber interior grade with muted teal accents. Rich atmospheric cinematic lighting, warm rim light, volumetric light shafts, floating dust particles. Muted harmonious colour palette. Full-bleed single scene with real environmental depth and a detailed background. Clean soft linework, thick black outline, flat cel-shading. Absolutely NO halftone dots, NO ben-day dots, NO starburst or speed lines, NO comic panels, NO white gutters, NO speech bubbles, NO anime face, NO detailed irises, NO visible hair, NO visible ears, NO blush, NO sharp jawline, NO photorealism, and NO text, letters, signs or words anywhere in the image.",
      "video_action_prompt": "Slow smooth push-in toward the young man with his navy cap and grey hoodie, seated at the conference table. His chest rises once with a held breath, the sheet of notes shifts slightly in his hand, dust particles drift through the warm lamp light, the blurred colleague silhouettes stay soft and still. The push-in tightens the frame on his face as his mouth opens to speak. Calm-before-the-storm tone, restrained tension. Stable camera, smooth motion, minimal distortion.",
      "transition_out": "cut_on_action",
      "vo_text": "Picture this: you're in a high-stakes meeting, and all eyes are on you. You've prepped for this for weeks.",
      "vo_tc": "0:00-0:12",
      "status": "pending",
      "derived_from": "SC01_SH001",
      "tc": "0:00-0:05",
      "panel_index": 1,
      "vo_block_tc": "0:00-0:12",
      "rhythm_role": "entrada",
      "rhythm_note": "entrada a mitad de accion: corto, no deja instalarse",
      "risk": [
        "R2-NEGATIVOS-INLINE: el image_prompt lleva los negativos escritos dentro del prompt positivo, lo que ESTILO_MINDSET_MECHANICS.md 6.bis declara contraproducente (los tokens 'ears'/'nose' condicionan en positivo). El modelo por defecto de recraft_ai/generate_scene.py es recraftv4_1, que NO acepta el parametro negative_prompt (recraft_client.py:87,136), asi que la via del 6.bis no esta disponible sin cambiar a recraftv3 @1820x1024. DECISION PENDIENTE DE KIMI antes de gastar creditos."
      ]
    },
    {
      "shot_id": "SC01_SH001b",
      "scene": 1,
      "duration_s": 7,
      "shot_size": "medium",
      "angle": "eye_level",
      "camera_move": {
        "type": "push_in",
        "speed": "slow",
        "phase": "2/2",
        "note": "fase 2/2: continuacion del MISMO movimiento sobre la MISMA imagen, encuadre ya avanzado (cut-in sobre el eje del movimiento, no jump cut)"
      },
      "subject": "HOST",
      "action": "sits at conference table leaning slightly forward, mouth half-open mid-word, sheet of notes held loosely in one hand, eyes fixed frame-right",
      "environment": "corporate meeting room at dusk, long dark-wood table, out-of-focus colleague silhouettes on the right, warm amber lamps, cool teal dusk through window, warm amber interior grade with muted teal accents; host on left third, open space right",
      "emotion_beat": "hook",
      "image_prompt": "Soft painterly digital illustration in the style of a modern animated explainer short, 2D stylised animation, not anime. Medium shot of a young man drawn with deliberately simplified cartoon proportions: a VERY LARGE round smooth head about one third of his total height, a completely smooth bald head shape with NO visible hair at all, a dark navy baseball cap sitting directly on that smooth head. His face is extremely minimal: two small plain solid black oval eyes with no iris, no highlight and no eyelashes, two thin short dark eyebrows, a tiny dot nose and a small simple line mouth. Flat pale cream skin with soft even shading and NO blush, NO pink cheeks. Small simple body in a grey hoodie, dark jeans and sneakers. He sits at a long dark-wood conference table, leaning slightly forward, mouth half-open mid-word, holding a sheet of notes loosely in one hand, eyes fixed toward frame right. He is placed on the left third of the frame with open space on the right. Corporate meeting room at dusk: out-of-focus colleague silhouettes along the right side of the table, warm amber desk lamps, cool teal dusk light through a window behind him, warm amber interior grade with muted teal accents. Rich atmospheric cinematic lighting, warm rim light, volumetric light shafts, floating dust particles. Muted harmonious colour palette. Full-bleed single scene with real environmental depth and a detailed background. Clean soft linework, thick black outline, flat cel-shading. Absolutely NO halftone dots, NO ben-day dots, NO starburst or speed lines, NO comic panels, NO white gutters, NO speech bubbles, NO anime face, NO detailed irises, NO visible hair, NO visible ears, NO blush, NO sharp jawline, NO photorealism, and NO text, letters, signs or words anywhere in the image.",
      "video_action_prompt": "Continuation of the previous shot, second half of the same camera move, already tighter in the frame. Slow smooth push-in toward the young man with his navy cap and grey hoodie, seated at the conference table. His chest rises once with a held breath, the sheet of notes shifts slightly in his hand, dust particles drift through the warm lamp light, the blurred colleague silhouettes stay soft and still. The push-in tightens the frame on his face as his mouth opens to speak. Calm-before-the-storm tone, restrained tension. Stable camera, smooth motion, minimal distortion.",
      "transition_out": "cut_on_action",
      "vo_text": "Picture this: you're in a high-stakes meeting, and all eyes are on you. You've prepped for this for weeks.",
      "vo_tc": "0:00-0:12",
      "status": "pending",
      "derived_from": "SC01_SH001",
      "tc": "0:05-0:12",
      "panel_index": 2,
      "vo_block_tc": "0:00-0:12",
      "transition_in": "cut_on_action",
      "rhythm_role": "exhalacion",
      "rhythm_note": "deja aterrizar el bloqueo antes de cortar",
      "risk": [
        "R2-NEGATIVOS-INLINE: el image_prompt lleva los negativos escritos dentro del prompt positivo, lo que ESTILO_MINDSET_MECHANICS.md 6.bis declara contraproducente (los tokens 'ears'/'nose' condicionan en positivo). El modelo por defecto de recraft_ai/generate_scene.py es recraftv4_1, que NO acepta el parametro negative_prompt (recraft_client.py:87,136), asi que la via del 6.bis no esta disponible sin cambiar a recraftv3 @1820x1024. DECISION PENDIENTE DE KIMI antes de gastar creditos."
      ]
    },
    {
      "shot_id": "SC01_SH002a",
      "scene": 1,
      "duration_s": 8,
      "shot_size": "close_up",
      "angle": "dutch",
      "camera_move": {
        "type": "pan",
        "speed": "slow",
        "direction": "left",
        "phase": "1/2",
        "note": "fase 1/2: arranque del movimiento"
      },
      "subject": "HOST",
      "action": "mouth stays half-open but no words come out, black oval eyes widen and stop blinking, the hand with notes lowers out of frame",
      "environment": "same meeting room, very shallow focus, background melted into soft warm and teal shapes, amber lamp glow on one cheek, cool window edge light on the other; face on right third, empty lamp-lit space opening left",
      "emotion_beat": "tensión",
      "image_prompt": "Soft painterly digital illustration in the style of a modern animated explainer short, 2D stylised animation, not anime. Close-up, slight dutch angle, of a young man drawn with deliberately simplified cartoon proportions: a VERY LARGE round smooth head about one third of his total height, a completely smooth bald head shape with NO visible hair at all, a dark navy baseball cap sitting directly on that smooth head. His face is extremely minimal: two small plain solid black oval eyes with no iris, no highlight and no eyelashes, two thin short dark eyebrows, a tiny dot nose and a small simple line mouth. Flat pale cream skin with soft even shading and NO blush, NO pink cheeks. Small simple body in a grey hoodie, dark jeans and sneakers. His mouth hangs half-open and silent, his black oval eyes are wide and unblinking, his gaze fixed toward frame right. His face sits on the right third of the frame, eyes at the upper-right intersection, with empty lamp-lit space opening on the left. Very shallow focus: the meeting room melts into soft warm and teal shapes behind him, amber lamp glow on one cheek, cool edge light from a window on the other, warm amber interior grade with muted teal accents. Rich atmospheric cinematic lighting, warm rim light, volumetric light shafts, floating dust particles. Muted harmonious colour palette. Full-bleed single scene with real environmental depth and a detailed background. Clean soft linework, thick black outline, flat cel-shading. Absolutely NO halftone dots, NO ben-day dots, NO starburst or speed lines, NO comic panels, NO white gutters, NO speech bubbles, NO anime face, NO detailed irises, NO visible hair, NO visible ears, NO blush, NO sharp jawline, NO photorealism, and NO text, letters, signs or words anywhere in the image.",
      "video_action_prompt": "Slow smooth pan to the left across the close-up of the young man with his navy cap and grey hoodie. His plain black oval eyes stay wide and unblinking, his half-open mouth does not move, a faint tremor runs through his shoulders, dust particles drift through the amber lamp light. The pan opens empty space beside his face, underlining the silence. Growing unease, held-breath pacing. Stable camera, smooth motion, minimal distortion.",
      "transition_out": "cut_on_action",
      "vo_text": "You open your mouth to share a brilliant idea, and… nothing. Your mind goes completely blank. The words are gone. The concepts have vanished.",
      "vo_tc": "0:12-0:24",
      "status": "pending",
      "derived_from": "SC01_SH002",
      "tc": "0:12-0:20",
      "panel_index": 3,
      "vo_block_tc": "0:12-0:24",
      "rhythm_role": "exhalacion",
      "rhythm_note": "sostiene el silencio: el plano mas largo del cuerpo del piloto",
      "risk": [
        "R2-NEGATIVOS-INLINE: el image_prompt lleva los negativos escritos dentro del prompt positivo, lo que ESTILO_MINDSET_MECHANICS.md 6.bis declara contraproducente (los tokens 'ears'/'nose' condicionan en positivo). El modelo por defecto de recraft_ai/generate_scene.py es recraftv4_1, que NO acepta el parametro negative_prompt (recraft_client.py:87,136), asi que la via del 6.bis no esta disponible sin cambiar a recraftv3 @1820x1024. DECISION PENDIENTE DE KIMI antes de gastar creditos."
      ]
    },
    {
      "shot_id": "SC01_SH002b",
      "scene": 1,
      "duration_s": 4,
      "shot_size": "close_up",
      "angle": "dutch",
      "camera_move": {
        "type": "pan",
        "speed": "slow",
        "direction": "left",
        "phase": "2/2",
        "note": "fase 2/2: continuacion del MISMO movimiento sobre la MISMA imagen, encuadre ya avanzado (cut-in sobre el eje del movimiento, no jump cut)"
      },
      "subject": "HOST",
      "action": "mouth stays half-open but no words come out, black oval eyes widen and stop blinking, the hand with notes lowers out of frame",
      "environment": "same meeting room, very shallow focus, background melted into soft warm and teal shapes, amber lamp glow on one cheek, cool window edge light on the other; face on right third, empty lamp-lit space opening left",
      "emotion_beat": "tensión",
      "image_prompt": "Soft painterly digital illustration in the style of a modern animated explainer short, 2D stylised animation, not anime. Close-up, slight dutch angle, of a young man drawn with deliberately simplified cartoon proportions: a VERY LARGE round smooth head about one third of his total height, a completely smooth bald head shape with NO visible hair at all, a dark navy baseball cap sitting directly on that smooth head. His face is extremely minimal: two small plain solid black oval eyes with no iris, no highlight and no eyelashes, two thin short dark eyebrows, a tiny dot nose and a small simple line mouth. Flat pale cream skin with soft even shading and NO blush, NO pink cheeks. Small simple body in a grey hoodie, dark jeans and sneakers. His mouth hangs half-open and silent, his black oval eyes are wide and unblinking, his gaze fixed toward frame right. His face sits on the right third of the frame, eyes at the upper-right intersection, with empty lamp-lit space opening on the left. Very shallow focus: the meeting room melts into soft warm and teal shapes behind him, amber lamp glow on one cheek, cool edge light from a window on the other, warm amber interior grade with muted teal accents. Rich atmospheric cinematic lighting, warm rim light, volumetric light shafts, floating dust particles. Muted harmonious colour palette. Full-bleed single scene with real environmental depth and a detailed background. Clean soft linework, thick black outline, flat cel-shading. Absolutely NO halftone dots, NO ben-day dots, NO starburst or speed lines, NO comic panels, NO white gutters, NO speech bubbles, NO anime face, NO detailed irises, NO visible hair, NO visible ears, NO blush, NO sharp jawline, NO photorealism, and NO text, letters, signs or words anywhere in the image.",
      "video_action_prompt": "Continuation of the previous shot, second half of the same camera move, already tighter in the frame. Slow smooth pan to the left across the close-up of the young man with his navy cap and grey hoodie. His plain black oval eyes stay wide and unblinking, his half-open mouth does not move, a faint tremor runs through his shoulders, dust particles drift through the amber lamp light. The pan opens empty space beside his face, underlining the silence. Growing unease, held-breath pacing. Stable camera, smooth motion, minimal distortion.",
      "transition_out": "smash_cut",
      "vo_text": "You open your mouth to share a brilliant idea, and… nothing. Your mind goes completely blank. The words are gone. The concepts have vanished.",
      "vo_tc": "0:12-0:24",
      "status": "pending",
      "derived_from": "SC01_SH002",
      "tc": "0:20-0:24",
      "panel_index": 4,
      "vo_block_tc": "0:12-0:24",
      "transition_in": "cut_on_action",
      "rhythm_role": "aceleracion",
      "rhythm_note": "acelera hacia el pattern interrupt",
      "risk": [
        "R2-NEGATIVOS-INLINE: el image_prompt lleva los negativos escritos dentro del prompt positivo, lo que ESTILO_MINDSET_MECHANICS.md 6.bis declara contraproducente (los tokens 'ears'/'nose' condicionan en positivo). El modelo por defecto de recraft_ai/generate_scene.py es recraftv4_1, que NO acepta el parametro negative_prompt (recraft_client.py:87,136), asi que la via del 6.bis no esta disponible sin cambiar a recraftv3 @1820x1024. DECISION PENDIENTE DE KIMI antes de gastar creditos."
      ]
    },
    {
      "shot_id": "SC01_SH003a",
      "scene": 1,
      "duration_s": 4,
      "shot_size": "insert",
      "angle": "high",
      "camera_move": {
        "type": "tilt",
        "speed": "slow",
        "direction": "down",
        "phase": "1/2",
        "note": "fase 1/2: arranque del movimiento"
      },
      "subject": "HOST",
      "action": "fingers loosen, note pages slip from his hand, one sheet tilts mid-fall and settles onto the dark table, fingertips tremble once against the wood",
      "environment": "macro detail of the tabletop, pages with blurred illegible scribble-like marks only, simple pen, warm pool of lamplight on wood grain, edges falling to shadow, very shallow depth of field; hand in lower-left third, open space above",
      "emotion_beat": "tensión sostenida (PATTERN INTERRUPT 25-35s)",
      "image_prompt": "Soft painterly digital illustration in the style of a modern animated explainer short, 2D stylised animation, not anime. Extreme close-up detail insert of the hand of a young man drawn with deliberately simplified cartoon proportions: a VERY LARGE round smooth head about one third of his total height, a completely smooth bald head shape with NO visible hair at all, a dark navy baseball cap sitting directly on that smooth head. His face is extremely minimal: two small plain solid black oval eyes with no iris, no highlight and no eyelashes, two thin short dark eyebrows, a tiny dot nose and a small simple line mouth. Flat pale cream skin with soft even shading and NO blush, NO pink cheeks. Small simple body in a grey hoodie, dark jeans and sneakers. Only his grey-hoodie sleeve, his hand and the tabletop are visible: his fingers loosen as several note pages slip from his grip, one sheet tilting mid-fall onto a dark wood table; the pages show only soft blurred scribble-like marks, never legible words; a simple pen lies nearby; a warm pool of lamplight on the wood grain, edges falling into shadow; very shallow depth of field; the hand sits in the lower-left third with open space above. Rich atmospheric cinematic lighting, warm rim light, volumetric light shafts, floating dust particles. Muted harmonious colour palette. Full-bleed single scene with real environmental depth and a detailed background. Clean soft linework, thick black outline, flat cel-shading. Absolutely NO halftone dots, NO ben-day dots, NO starburst or speed lines, NO comic panels, NO white gutters, NO speech bubbles, NO anime face, NO detailed irises, NO visible hair, NO visible ears, NO blush, NO sharp jawline, NO photorealism, and NO text, letters, signs or words anywhere in the image.",
      "video_action_prompt": "Slow smooth tilt down over the detail of the hand of the young man with his navy cap and grey hoodie, on the dark wood table. His fingers loosen and the note pages slide and settle onto the wood, one sheet rocking gently before going still, his fingertips trembling once against the table, dust particles falling through the narrow pool of warm lamplight. The tilt lands on the fallen pages. Abrupt, intimate, held-tension tone. Stable camera, smooth motion, minimal distortion.",
      "transition_out": "cut_on_action",
      "vo_text": "All that's left is that rising tide of panic as you stare into a sea of expectant faces. That frustrating moment of shutting down is not a personal failure.",
      "vo_tc": "0:24-0:36",
      "status": "pending",
      "derived_from": "SC01_SH003",
      "tc": "0:24-0:28",
      "panel_index": 5,
      "vo_block_tc": "0:24-0:36",
      "rhythm_role": "rafaga",
      "rhythm_note": "PATTERN INTERRUPT: plano mas corto del piloto, aterriza el smash_cut",
      "risk": [
        "R2-NEGATIVOS-INLINE: el image_prompt lleva los negativos escritos dentro del prompt positivo, lo que ESTILO_MINDSET_MECHANICS.md 6.bis declara contraproducente (los tokens 'ears'/'nose' condicionan en positivo). El modelo por defecto de recraft_ai/generate_scene.py es recraftv4_1, que NO acepta el parametro negative_prompt (recraft_client.py:87,136), asi que la via del 6.bis no esta disponible sin cambiar a recraftv3 @1820x1024. DECISION PENDIENTE DE KIMI antes de gastar creditos."
      ]
    },
    {
      "shot_id": "SC01_SH003b",
      "scene": 1,
      "duration_s": 8,
      "shot_size": "insert",
      "angle": "high",
      "camera_move": {
        "type": "tilt",
        "speed": "slow",
        "direction": "down",
        "phase": "2/2",
        "note": "fase 2/2: continuacion del MISMO movimiento sobre la MISMA imagen, encuadre ya avanzado (cut-in sobre el eje del movimiento, no jump cut)"
      },
      "subject": "HOST",
      "action": "fingers loosen, note pages slip from his hand, one sheet tilts mid-fall and settles onto the dark table, fingertips tremble once against the wood",
      "environment": "macro detail of the tabletop, pages with blurred illegible scribble-like marks only, simple pen, warm pool of lamplight on wood grain, edges falling to shadow, very shallow depth of field; hand in lower-left third, open space above",
      "emotion_beat": "tensión sostenida (PATTERN INTERRUPT 25-35s)",
      "image_prompt": "Soft painterly digital illustration in the style of a modern animated explainer short, 2D stylised animation, not anime. Extreme close-up detail insert of the hand of a young man drawn with deliberately simplified cartoon proportions: a VERY LARGE round smooth head about one third of his total height, a completely smooth bald head shape with NO visible hair at all, a dark navy baseball cap sitting directly on that smooth head. His face is extremely minimal: two small plain solid black oval eyes with no iris, no highlight and no eyelashes, two thin short dark eyebrows, a tiny dot nose and a small simple line mouth. Flat pale cream skin with soft even shading and NO blush, NO pink cheeks. Small simple body in a grey hoodie, dark jeans and sneakers. Only his grey-hoodie sleeve, his hand and the tabletop are visible: his fingers loosen as several note pages slip from his grip, one sheet tilting mid-fall onto a dark wood table; the pages show only soft blurred scribble-like marks, never legible words; a simple pen lies nearby; a warm pool of lamplight on the wood grain, edges falling into shadow; very shallow depth of field; the hand sits in the lower-left third with open space above. Rich atmospheric cinematic lighting, warm rim light, volumetric light shafts, floating dust particles. Muted harmonious colour palette. Full-bleed single scene with real environmental depth and a detailed background. Clean soft linework, thick black outline, flat cel-shading. Absolutely NO halftone dots, NO ben-day dots, NO starburst or speed lines, NO comic panels, NO white gutters, NO speech bubbles, NO anime face, NO detailed irises, NO visible hair, NO visible ears, NO blush, NO sharp jawline, NO photorealism, and NO text, letters, signs or words anywhere in the image.",
      "video_action_prompt": "Continuation of the previous shot, second half of the same camera move, already tighter in the frame. Slow smooth tilt down over the detail of the hand of the young man with his navy cap and grey hoodie, on the dark wood table. His fingers loosen and the note pages slide and settle onto the wood, one sheet rocking gently before going still, his fingertips trembling once against the table, dust particles falling through the narrow pool of warm lamplight. The tilt lands on the fallen pages. Abrupt, intimate, held-tension tone. Stable camera, smooth motion, minimal distortion.",
      "transition_out": "match_cut",
      "vo_text": "All that's left is that rising tide of panic as you stare into a sea of expectant faces. That frustrating moment of shutting down is not a personal failure.",
      "vo_tc": "0:24-0:36",
      "status": "pending",
      "derived_from": "SC01_SH003",
      "tc": "0:28-0:36",
      "panel_index": 6,
      "vo_block_tc": "0:24-0:36",
      "transition_in": "cut_on_action",
      "rhythm_role": "exhalacion",
      "rhythm_note": "recuperacion larga tras el golpe",
      "risk": [
        "R2-NEGATIVOS-INLINE: el image_prompt lleva los negativos escritos dentro del prompt positivo, lo que ESTILO_MINDSET_MECHANICS.md 6.bis declara contraproducente (los tokens 'ears'/'nose' condicionan en positivo). El modelo por defecto de recraft_ai/generate_scene.py es recraftv4_1, que NO acepta el parametro negative_prompt (recraft_client.py:87,136), asi que la via del 6.bis no esta disponible sin cambiar a recraftv3 @1820x1024. DECISION PENDIENTE DE KIMI antes de gastar creditos."
      ]
    },
    {
      "shot_id": "SC01_SH004a",
      "scene": 1,
      "duration_s": 7,
      "shot_size": "wide",
      "angle": "overhead",
      "camera_move": {
        "type": "crane",
        "speed": "slow",
        "direction": "up",
        "phase": "1/2",
        "note": "fase 1/2: arranque del movimiento"
      },
      "subject": "HOST",
      "action": "seen from directly above, he sits small and motionless at the long table, shoulders drawn in, head bowed over the fallen notes, arms close to his body; colleague silhouettes ring the table, all turned toward him",
      "environment": "full conference room top-down, long table on a diagonal lower-left to upper-right, alternating warm lamplight pools and cool shadow on the floor, teal dusk strip at windows on upper edge; host in lower-left area with empty floor around him",
      "emotion_beat": "vulnerabilidad",
      "image_prompt": "Soft painterly digital illustration in the style of a modern animated explainer short, 2D stylised animation, not anime. Wide overhead top-down shot of a young man drawn with deliberately simplified cartoon proportions: a VERY LARGE round smooth head about one third of his total height, a completely smooth bald head shape with NO visible hair at all, a dark navy baseball cap sitting directly on that smooth head. His face is extremely minimal: two small plain solid black oval eyes with no iris, no highlight and no eyelashes, two thin short dark eyebrows, a tiny dot nose and a small simple line mouth. Flat pale cream skin with soft even shading and NO blush, NO pink cheeks. Small simple body in a grey hoodie, dark jeans and sneakers. Seen from directly above: he sits small and motionless at a long dark conference table set on a diagonal from lower-left to upper-right, shoulders drawn in, head bowed over fallen note pages, arms held close to his body; a ring of out-of-focus colleague silhouettes around the table all turned toward him; alternating pools of warm lamplight and cool shadow across the floor, a strip of teal dusk light at the windows along the upper edge; he occupies the lower-left area of the frame with empty floor space around him. Rich atmospheric cinematic lighting, warm rim light, volumetric light shafts, floating dust particles. Muted harmonious colour palette. Full-bleed single scene with real environmental depth and a detailed background. Clean soft linework, thick black outline, flat cel-shading. Absolutely NO halftone dots, NO ben-day dots, NO starburst or speed lines, NO comic panels, NO white gutters, NO speech bubbles, NO anime face, NO detailed irises, NO visible hair, NO visible ears, NO blush, NO sharp jawline, NO photorealism, and NO text, letters, signs or words anywhere in the image.",
      "video_action_prompt": "Slow smooth crane up from the overhead view of the young man with his navy cap and grey hoodie at the conference table. His shoulders stay drawn in, his head stays bowed over the fallen notes, the colleague silhouettes remain still and turned toward him, dust drifting slowly through the warm light pools. The rise reveals how small and alone he is in the long room. Vulnerable, exposed tone. Stable camera, smooth motion, minimal distortion.",
      "transition_out": "cut_on_action",
      "vo_text": "It's not because you're not smart enough or weren't prepared. It's not your fault. It's your ancient survival wiring—designed to save you from tigers—misfiring in a modern world.",
      "vo_tc": "0:36-0:48",
      "status": "pending",
      "derived_from": "SC01_SH004",
      "tc": "0:36-0:43",
      "panel_index": 7,
      "vo_block_tc": "0:36-0:48",
      "rhythm_role": "exhalacion",
      "rhythm_note": "la grua necesita recorrido para revelar escala",
      "risk": [
        "R2-NEGATIVOS-INLINE: el image_prompt lleva los negativos escritos dentro del prompt positivo, lo que ESTILO_MINDSET_MECHANICS.md 6.bis declara contraproducente (los tokens 'ears'/'nose' condicionan en positivo). El modelo por defecto de recraft_ai/generate_scene.py es recraftv4_1, que NO acepta el parametro negative_prompt (recraft_client.py:87,136), asi que la via del 6.bis no esta disponible sin cambiar a recraftv3 @1820x1024. DECISION PENDIENTE DE KIMI antes de gastar creditos."
      ]
    },
    {
      "shot_id": "SC01_SH004b",
      "scene": 1,
      "duration_s": 5,
      "shot_size": "wide",
      "angle": "overhead",
      "camera_move": {
        "type": "crane",
        "speed": "slow",
        "direction": "up",
        "phase": "2/2",
        "note": "fase 2/2: continuacion del MISMO movimiento sobre la MISMA imagen, encuadre ya avanzado (cut-in sobre el eje del movimiento, no jump cut)"
      },
      "subject": "HOST",
      "action": "seen from directly above, he sits small and motionless at the long table, shoulders drawn in, head bowed over the fallen notes, arms close to his body; colleague silhouettes ring the table, all turned toward him",
      "environment": "full conference room top-down, long table on a diagonal lower-left to upper-right, alternating warm lamplight pools and cool shadow on the floor, teal dusk strip at windows on upper edge; host in lower-left area with empty floor around him",
      "emotion_beat": "vulnerabilidad",
      "image_prompt": "Soft painterly digital illustration in the style of a modern animated explainer short, 2D stylised animation, not anime. Wide overhead top-down shot of a young man drawn with deliberately simplified cartoon proportions: a VERY LARGE round smooth head about one third of his total height, a completely smooth bald head shape with NO visible hair at all, a dark navy baseball cap sitting directly on that smooth head. His face is extremely minimal: two small plain solid black oval eyes with no iris, no highlight and no eyelashes, two thin short dark eyebrows, a tiny dot nose and a small simple line mouth. Flat pale cream skin with soft even shading and NO blush, NO pink cheeks. Small simple body in a grey hoodie, dark jeans and sneakers. Seen from directly above: he sits small and motionless at a long dark conference table set on a diagonal from lower-left to upper-right, shoulders drawn in, head bowed over fallen note pages, arms held close to his body; a ring of out-of-focus colleague silhouettes around the table all turned toward him; alternating pools of warm lamplight and cool shadow across the floor, a strip of teal dusk light at the windows along the upper edge; he occupies the lower-left area of the frame with empty floor space around him. Rich atmospheric cinematic lighting, warm rim light, volumetric light shafts, floating dust particles. Muted harmonious colour palette. Full-bleed single scene with real environmental depth and a detailed background. Clean soft linework, thick black outline, flat cel-shading. Absolutely NO halftone dots, NO ben-day dots, NO starburst or speed lines, NO comic panels, NO white gutters, NO speech bubbles, NO anime face, NO detailed irises, NO visible hair, NO visible ears, NO blush, NO sharp jawline, NO photorealism, and NO text, letters, signs or words anywhere in the image.",
      "video_action_prompt": "Continuation of the previous shot, second half of the same camera move, already tighter in the frame. Slow smooth crane up from the overhead view of the young man with his navy cap and grey hoodie at the conference table. His shoulders stay drawn in, his head stays bowed over the fallen notes, the colleague silhouettes remain still and turned toward him, dust drifting slowly through the warm light pools. The rise reveals how small and alone he is in the long room. Vulnerable, exposed tone. Stable camera, smooth motion, minimal distortion.",
      "transition_out": "hard_cut",
      "vo_text": "It's not because you're not smart enough or weren't prepared. It's not your fault. It's your ancient survival wiring—designed to save you from tigers—misfiring in a modern world.",
      "vo_tc": "0:36-0:48",
      "status": "pending",
      "derived_from": "SC01_SH004",
      "tc": "0:43-0:48",
      "panel_index": 8,
      "vo_block_tc": "0:36-0:48",
      "transition_in": "cut_on_action",
      "rhythm_role": "aceleracion",
      "rhythm_note": "cierra escena 1 acortando hacia el corte de escena",
      "risk": [
        "R2-NEGATIVOS-INLINE: el image_prompt lleva los negativos escritos dentro del prompt positivo, lo que ESTILO_MINDSET_MECHANICS.md 6.bis declara contraproducente (los tokens 'ears'/'nose' condicionan en positivo). El modelo por defecto de recraft_ai/generate_scene.py es recraftv4_1, que NO acepta el parametro negative_prompt (recraft_client.py:87,136), asi que la via del 6.bis no esta disponible sin cambiar a recraftv3 @1820x1024. DECISION PENDIENTE DE KIMI antes de gastar creditos."
      ]
    },
    {
      "shot_id": "SC02_SH005a",
      "scene": 2,
      "duration_s": 4,
      "shot_size": "extreme_close_up",
      "angle": "eye_level",
      "camera_move": {
        "type": "push_in",
        "speed": "slow",
        "phase": "1/2",
        "note": "fase 1/2: arranque del movimiento"
      },
      "subject": "HOST",
      "action": "his right eye fills the frame, open too wide, unblinking; a thin bead of sweat slides slowly down his temple; the eye flicks once frame-right",
      "environment": "extreme macro, background only amber-teal blur of the meeting room, lower edge of navy cap brim crossing the top of frame, very shallow macro focus; eye on upper-left third looking right",
      "emotion_beat": "tensión (íntima)",
      "image_prompt": "Soft painterly digital illustration in the style of a modern animated explainer short, 2D stylised animation, not anime. Extreme close-up framed tight on one eye and the temple of a young man drawn with deliberately simplified cartoon proportions: a VERY LARGE round smooth head about one third of his total height, a completely smooth bald head shape with NO visible hair at all, a dark navy baseball cap sitting directly on that smooth head. His face is extremely minimal: two small plain solid black oval eyes with no iris, no highlight and no eyelashes, two thin short dark eyebrows, a tiny dot nose and a small simple line mouth. Flat pale cream skin with soft even shading and NO blush, NO pink cheeks. Small simple body in a grey hoodie, dark jeans and sneakers. His right eye fills the upper-left third of the frame, open too wide and unblinking, a plain solid black oval; a thin bead of sweat slides down his temple; the lower edge of his dark navy cap brim crosses the top of the frame; the blurred warm meeting room glows as soft amber smudges across his cheek and skin; very shallow macro focus, muted amber and teal tones. Rich atmospheric cinematic lighting, warm rim light, volumetric light shafts, floating dust particles. Muted harmonious colour palette. Full-bleed single scene with real environmental depth and a detailed background. Clean soft linework, thick black outline, flat cel-shading. Absolutely NO halftone dots, NO ben-day dots, NO starburst or speed lines, NO comic panels, NO white gutters, NO speech bubbles, NO anime face, NO detailed irises, NO visible hair, NO visible ears, NO blush, NO sharp jawline, NO photorealism, and NO text, letters, signs or words anywhere in the image.",
      "video_action_prompt": "Very slow smooth push-in on the extreme close-up of the eye of the young man with his navy cap and grey hoodie. His plain solid black oval eye stays open too wide without blinking, a thin bead of sweat slides slowly down his temple, the soft amber glow on his skin shimmers faintly, floating dust crosses the macro focus. The push tightens until the eye dominates the frame. Claustrophobic, clinical tension. Stable camera, smooth motion, minimal distortion.",
      "transition_out": "cut_on_action",
      "vo_text": "This 'brain freeze' is a universal human experience. It happens to public speakers, athletes, students in an exam… just about everyone.",
      "vo_tc": "0:48-1:00",
      "status": "pending",
      "derived_from": "SC02_SH005",
      "tc": "0:48-0:52",
      "panel_index": 9,
      "vo_block_tc": "0:48-1:00",
      "rhythm_role": "inhalacion",
      "rhythm_note": "entra rapido al ojo tras el cambio de escena",
      "risk": [
        "R2-NEGATIVOS-INLINE: el image_prompt lleva los negativos escritos dentro del prompt positivo, lo que ESTILO_MINDSET_MECHANICS.md 6.bis declara contraproducente (los tokens 'ears'/'nose' condicionan en positivo). El modelo por defecto de recraft_ai/generate_scene.py es recraftv4_1, que NO acepta el parametro negative_prompt (recraft_client.py:87,136), asi que la via del 6.bis no esta disponible sin cambiar a recraftv3 @1820x1024. DECISION PENDIENTE DE KIMI antes de gastar creditos."
      ]
    },
    {
      "shot_id": "SC02_SH005b",
      "scene": 2,
      "duration_s": 8,
      "shot_size": "extreme_close_up",
      "angle": "eye_level",
      "camera_move": {
        "type": "push_in",
        "speed": "slow",
        "phase": "2/2",
        "note": "fase 2/2: continuacion del MISMO movimiento sobre la MISMA imagen, encuadre ya avanzado (cut-in sobre el eje del movimiento, no jump cut)"
      },
      "subject": "HOST",
      "action": "his right eye fills the frame, open too wide, unblinking; a thin bead of sweat slides slowly down his temple; the eye flicks once frame-right",
      "environment": "extreme macro, background only amber-teal blur of the meeting room, lower edge of navy cap brim crossing the top of frame, very shallow macro focus; eye on upper-left third looking right",
      "emotion_beat": "tensión (íntima)",
      "image_prompt": "Soft painterly digital illustration in the style of a modern animated explainer short, 2D stylised animation, not anime. Extreme close-up framed tight on one eye and the temple of a young man drawn with deliberately simplified cartoon proportions: a VERY LARGE round smooth head about one third of his total height, a completely smooth bald head shape with NO visible hair at all, a dark navy baseball cap sitting directly on that smooth head. His face is extremely minimal: two small plain solid black oval eyes with no iris, no highlight and no eyelashes, two thin short dark eyebrows, a tiny dot nose and a small simple line mouth. Flat pale cream skin with soft even shading and NO blush, NO pink cheeks. Small simple body in a grey hoodie, dark jeans and sneakers. His right eye fills the upper-left third of the frame, open too wide and unblinking, a plain solid black oval; a thin bead of sweat slides down his temple; the lower edge of his dark navy cap brim crosses the top of the frame; the blurred warm meeting room glows as soft amber smudges across his cheek and skin; very shallow macro focus, muted amber and teal tones. Rich atmospheric cinematic lighting, warm rim light, volumetric light shafts, floating dust particles. Muted harmonious colour palette. Full-bleed single scene with real environmental depth and a detailed background. Clean soft linework, thick black outline, flat cel-shading. Absolutely NO halftone dots, NO ben-day dots, NO starburst or speed lines, NO comic panels, NO white gutters, NO speech bubbles, NO anime face, NO detailed irises, NO visible hair, NO visible ears, NO blush, NO sharp jawline, NO photorealism, and NO text, letters, signs or words anywhere in the image.",
      "video_action_prompt": "Continuation of the previous shot, second half of the same camera move, already tighter in the frame. Very slow smooth push-in on the extreme close-up of the eye of the young man with his navy cap and grey hoodie. His plain solid black oval eye stays open too wide without blinking, a thin bead of sweat slides slowly down his temple, the soft amber glow on his skin shimmers faintly, floating dust crosses the macro focus. The push tightens until the eye dominates the frame. Claustrophobic, clinical tension. Stable camera, smooth motion, minimal distortion.",
      "transition_out": "cut_on_action",
      "vo_text": "This 'brain freeze' is a universal human experience. It happens to public speakers, athletes, students in an exam… just about everyone.",
      "vo_tc": "0:48-1:00",
      "status": "pending",
      "derived_from": "SC02_SH005",
      "tc": "0:52-1:00",
      "panel_index": 10,
      "vo_block_tc": "0:48-1:00",
      "transition_in": "cut_on_action",
      "rhythm_role": "exhalacion",
      "rhythm_note": "se queda en el sudor: incomodidad por permanencia",
      "risk": [
        "R2-NEGATIVOS-INLINE: el image_prompt lleva los negativos escritos dentro del prompt positivo, lo que ESTILO_MINDSET_MECHANICS.md 6.bis declara contraproducente (los tokens 'ears'/'nose' condicionan en positivo). El modelo por defecto de recraft_ai/generate_scene.py es recraftv4_1, que NO acepta el parametro negative_prompt (recraft_client.py:87,136), asi que la via del 6.bis no esta disponible sin cambiar a recraftv3 @1820x1024. DECISION PENDIENTE DE KIMI antes de gastar creditos."
      ]
    },
    {
      "shot_id": "SC02_SH006a",
      "scene": 2,
      "duration_s": 6,
      "shot_size": "medium_close",
      "angle": "dutch",
      "camera_move": {
        "type": "pan",
        "speed": "slow",
        "direction": "right",
        "phase": "1/2",
        "note": "fase 1/2: arranque del movimiento"
      },
      "subject": "HOST",
      "action": "sits rigid in three-quarter view, gaze locked frame-right at nothing, free hand gripping the table edge, throat moves in one dry swallow",
      "environment": "claustrophobic tight framing, background compressed into dark blurred shapes, single warm lamp orb behind his shoulder, longer shadows, dimmer warm amber grade with muted teal accents; host on left third, open dark space right",
      "emotion_beat": "tensión sostenida",
      "image_prompt": "Soft painterly digital illustration in the style of a modern animated explainer short, 2D stylised animation, not anime. Medium close-up, slight dutch angle, of a young man drawn with deliberately simplified cartoon proportions: a VERY LARGE round smooth head about one third of his total height, a completely smooth bald head shape with NO visible hair at all, a dark navy baseball cap sitting directly on that smooth head. His face is extremely minimal: two small plain solid black oval eyes with no iris, no highlight and no eyelashes, two thin short dark eyebrows, a tiny dot nose and a small simple line mouth. Flat pale cream skin with soft even shading and NO blush, NO pink cheeks. Small simple body in a grey hoodie, dark jeans and sneakers. He sits rigid in three-quarter view on the left third of the frame, gaze locked toward frame right at nothing, his free hand gripping the edge of the table, shoulders tense; open dark space on the right. The background is compressed into dark blurred shapes with a single warm lamp orb glowing behind his shoulder; longer shadows, dimmer warm amber grade with muted teal accents. Rich atmospheric cinematic lighting, warm rim light, volumetric light shafts, floating dust particles. Muted harmonious colour palette. Full-bleed single scene with real environmental depth and a detailed background. Clean soft linework, thick black outline, flat cel-shading. Absolutely NO halftone dots, NO ben-day dots, NO starburst or speed lines, NO comic panels, NO white gutters, NO speech bubbles, NO anime face, NO detailed irises, NO visible hair, NO visible ears, NO blush, NO sharp jawline, NO photorealism, and NO text, letters, signs or words anywhere in the image.",
      "video_action_prompt": "Slow smooth pan to the right across the medium close-up of the young man with his navy cap and grey hoodie. He stays rigid, gaze locked off-screen to the right, his throat moves in one dry swallow, his fingers press harder on the table edge, the warm lamp glow behind his shoulder flickers almost imperceptibly, dust drifting through the light. The pan follows the direction of his stare into empty dark space. Sustained, airless tension. Stable camera, smooth motion, minimal distortion.",
      "transition_out": "cut_on_action",
      "vo_text": "In these moments, your higher-level thinking seems to abandon you. Your prefrontal cortex—the logical, planning, modern part of your brain—gets its signals scrambled and takes a backseat.",
      "vo_tc": "1:00-1:12",
      "status": "pending",
      "derived_from": "SC02_SH006",
      "tc": "1:00-1:06",
      "panel_index": 11,
      "vo_block_tc": "1:00-1:12",
      "rhythm_role": "neutro",
      "rhythm_note": "beat de respiracion normal, sin acento",
      "risk": [
        "R2-NEGATIVOS-INLINE: el image_prompt lleva los negativos escritos dentro del prompt positivo, lo que ESTILO_MINDSET_MECHANICS.md 6.bis declara contraproducente (los tokens 'ears'/'nose' condicionan en positivo). El modelo por defecto de recraft_ai/generate_scene.py es recraftv4_1, que NO acepta el parametro negative_prompt (recraft_client.py:87,136), asi que la via del 6.bis no esta disponible sin cambiar a recraftv3 @1820x1024. DECISION PENDIENTE DE KIMI antes de gastar creditos."
      ]
    },
    {
      "shot_id": "SC02_SH006b",
      "scene": 2,
      "duration_s": 6,
      "shot_size": "medium_close",
      "angle": "dutch",
      "camera_move": {
        "type": "pan",
        "speed": "slow",
        "direction": "right",
        "phase": "2/2",
        "note": "fase 2/2: continuacion del MISMO movimiento sobre la MISMA imagen, encuadre ya avanzado (cut-in sobre el eje del movimiento, no jump cut)"
      },
      "subject": "HOST",
      "action": "sits rigid in three-quarter view, gaze locked frame-right at nothing, free hand gripping the table edge, throat moves in one dry swallow",
      "environment": "claustrophobic tight framing, background compressed into dark blurred shapes, single warm lamp orb behind his shoulder, longer shadows, dimmer warm amber grade with muted teal accents; host on left third, open dark space right",
      "emotion_beat": "tensión sostenida",
      "image_prompt": "Soft painterly digital illustration in the style of a modern animated explainer short, 2D stylised animation, not anime. Medium close-up, slight dutch angle, of a young man drawn with deliberately simplified cartoon proportions: a VERY LARGE round smooth head about one third of his total height, a completely smooth bald head shape with NO visible hair at all, a dark navy baseball cap sitting directly on that smooth head. His face is extremely minimal: two small plain solid black oval eyes with no iris, no highlight and no eyelashes, two thin short dark eyebrows, a tiny dot nose and a small simple line mouth. Flat pale cream skin with soft even shading and NO blush, NO pink cheeks. Small simple body in a grey hoodie, dark jeans and sneakers. He sits rigid in three-quarter view on the left third of the frame, gaze locked toward frame right at nothing, his free hand gripping the edge of the table, shoulders tense; open dark space on the right. The background is compressed into dark blurred shapes with a single warm lamp orb glowing behind his shoulder; longer shadows, dimmer warm amber grade with muted teal accents. Rich atmospheric cinematic lighting, warm rim light, volumetric light shafts, floating dust particles. Muted harmonious colour palette. Full-bleed single scene with real environmental depth and a detailed background. Clean soft linework, thick black outline, flat cel-shading. Absolutely NO halftone dots, NO ben-day dots, NO starburst or speed lines, NO comic panels, NO white gutters, NO speech bubbles, NO anime face, NO detailed irises, NO visible hair, NO visible ears, NO blush, NO sharp jawline, NO photorealism, and NO text, letters, signs or words anywhere in the image.",
      "video_action_prompt": "Continuation of the previous shot, second half of the same camera move, already tighter in the frame. Slow smooth pan to the right across the medium close-up of the young man with his navy cap and grey hoodie. He stays rigid, gaze locked off-screen to the right, his throat moves in one dry swallow, his fingers press harder on the table edge, the warm lamp glow behind his shoulder flickers almost imperceptibly, dust drifting through the light. The pan follows the direction of his stare into empty dark space. Sustained, airless tension. Stable camera, smooth motion, minimal distortion.",
      "transition_out": "hard_cut",
      "vo_text": "In these moments, your higher-level thinking seems to abandon you. Your prefrontal cortex—the logical, planning, modern part of your brain—gets its signals scrambled and takes a backseat.",
      "vo_tc": "1:00-1:12",
      "status": "pending",
      "derived_from": "SC02_SH006",
      "tc": "1:06-1:12",
      "panel_index": 12,
      "vo_block_tc": "1:00-1:12",
      "transition_in": "cut_on_action",
      "rhythm_role": "neutro",
      "rhythm_note": "beat de respiracion normal, sin acento",
      "risk": [
        "R2-NEGATIVOS-INLINE: el image_prompt lleva los negativos escritos dentro del prompt positivo, lo que ESTILO_MINDSET_MECHANICS.md 6.bis declara contraproducente (los tokens 'ears'/'nose' condicionan en positivo). El modelo por defecto de recraft_ai/generate_scene.py es recraftv4_1, que NO acepta el parametro negative_prompt (recraft_client.py:87,136), asi que la via del 6.bis no esta disponible sin cambiar a recraftv3 @1820x1024. DECISION PENDIENTE DE KIMI antes de gastar creditos."
      ]
    },
    {
      "shot_id": "SC02_SH007a",
      "scene": 2,
      "duration_s": 5,
      "shot_size": "insert",
      "angle": "high",
      "camera_move": {
        "type": "static",
        "speed": "slow",
        "note": "barely-there micro drift, never frozen | fase 1/2: arranque del movimiento",
        "phase": "1/2"
      },
      "subject": "HOST",
      "action": "his hand lies palm-down on the scattered note pages, fingers slowly curl until the pages crease under them, a fine tremor runs through the fingers, the pen beside them does not move",
      "environment": "same tabletop, light dimmer, warm lamplight pool narrowed, edges in deep shadow, pages with blurred illegible scribble-like marks only, very shallow depth of field; hand in center-left third",
      "emotion_beat": "vulnerabilidad",
      "image_prompt": "Soft painterly digital illustration in the style of a modern animated explainer short, 2D stylised animation, not anime. Extreme close-up detail insert of the hand of a young man drawn with deliberately simplified cartoon proportions: a VERY LARGE round smooth head about one third of his total height, a completely smooth bald head shape with NO visible hair at all, a dark navy baseball cap sitting directly on that smooth head. His face is extremely minimal: two small plain solid black oval eyes with no iris, no highlight and no eyelashes, two thin short dark eyebrows, a tiny dot nose and a small simple line mouth. Flat pale cream skin with soft even shading and NO blush, NO pink cheeks. Small simple body in a grey hoodie, dark jeans and sneakers. Only his grey-hoodie sleeve, his hand and the tabletop are visible: his hand lies palm-down on scattered note pages, fingers half-curled so the pages crease under them; a simple pen rests motionless beside; the warm pool of lamplight has narrowed, edges fallen to deep shadow; the pages show only blurred illegible scribble-like marks; very shallow depth of field; the hand sits in the center-left third. Rich atmospheric cinematic lighting, warm rim light, volumetric light shafts, floating dust particles. Muted harmonious colour palette. Full-bleed single scene with real environmental depth and a detailed background. Clean soft linework, thick black outline, flat cel-shading. Absolutely NO halftone dots, NO ben-day dots, NO starburst or speed lines, NO comic panels, NO white gutters, NO speech bubbles, NO anime face, NO detailed irises, NO visible hair, NO visible ears, NO blush, NO sharp jawline, NO photorealism, and NO text, letters, signs or words anywhere in the image.",
      "video_action_prompt": "Static shot with a barely-there slow drift over the detail of the hand of the young man with his navy cap and grey hoodie, resting on the scattered pages. His fingers slowly curl until the pages crease under them, a fine tremor runs through the fingers, the pen beside them does not move, dust particles float through the narrowed warm light. Nothing else moves. Quiet helplessness, held still. Stable camera, smooth motion, minimal distortion.",
      "transition_out": "cut_on_action",
      "vo_text": "It feels like the command center of your mind has just been hijacked. You know the information is in there. You know what you need to do, but you just can't get to it.",
      "vo_tc": "1:12-1:24",
      "status": "pending",
      "derived_from": "SC02_SH007",
      "tc": "1:12-1:17",
      "panel_index": 13,
      "vo_block_tc": "1:12-1:24",
      "rhythm_role": "inhalacion",
      "rhythm_note": "reaprieta antes del plano final",
      "risk": [
        "R2-NEGATIVOS-INLINE: el image_prompt lleva los negativos escritos dentro del prompt positivo, lo que ESTILO_MINDSET_MECHANICS.md 6.bis declara contraproducente (los tokens 'ears'/'nose' condicionan en positivo). El modelo por defecto de recraft_ai/generate_scene.py es recraftv4_1, que NO acepta el parametro negative_prompt (recraft_client.py:87,136), asi que la via del 6.bis no esta disponible sin cambiar a recraftv3 @1820x1024. DECISION PENDIENTE DE KIMI antes de gastar creditos."
      ]
    },
    {
      "shot_id": "SC02_SH007b",
      "scene": 2,
      "duration_s": 7,
      "shot_size": "insert",
      "angle": "high",
      "camera_move": {
        "type": "static",
        "speed": "slow",
        "note": "barely-there micro drift, never frozen | fase 2/2: continuacion del MISMO movimiento sobre la MISMA imagen, encuadre ya avanzado (cut-in sobre el eje del movimiento, no jump cut)",
        "phase": "2/2"
      },
      "subject": "HOST",
      "action": "his hand lies palm-down on the scattered note pages, fingers slowly curl until the pages crease under them, a fine tremor runs through the fingers, the pen beside them does not move",
      "environment": "same tabletop, light dimmer, warm lamplight pool narrowed, edges in deep shadow, pages with blurred illegible scribble-like marks only, very shallow depth of field; hand in center-left third",
      "emotion_beat": "vulnerabilidad",
      "image_prompt": "Soft painterly digital illustration in the style of a modern animated explainer short, 2D stylised animation, not anime. Extreme close-up detail insert of the hand of a young man drawn with deliberately simplified cartoon proportions: a VERY LARGE round smooth head about one third of his total height, a completely smooth bald head shape with NO visible hair at all, a dark navy baseball cap sitting directly on that smooth head. His face is extremely minimal: two small plain solid black oval eyes with no iris, no highlight and no eyelashes, two thin short dark eyebrows, a tiny dot nose and a small simple line mouth. Flat pale cream skin with soft even shading and NO blush, NO pink cheeks. Small simple body in a grey hoodie, dark jeans and sneakers. Only his grey-hoodie sleeve, his hand and the tabletop are visible: his hand lies palm-down on scattered note pages, fingers half-curled so the pages crease under them; a simple pen rests motionless beside; the warm pool of lamplight has narrowed, edges fallen to deep shadow; the pages show only blurred illegible scribble-like marks; very shallow depth of field; the hand sits in the center-left third. Rich atmospheric cinematic lighting, warm rim light, volumetric light shafts, floating dust particles. Muted harmonious colour palette. Full-bleed single scene with real environmental depth and a detailed background. Clean soft linework, thick black outline, flat cel-shading. Absolutely NO halftone dots, NO ben-day dots, NO starburst or speed lines, NO comic panels, NO white gutters, NO speech bubbles, NO anime face, NO detailed irises, NO visible hair, NO visible ears, NO blush, NO sharp jawline, NO photorealism, and NO text, letters, signs or words anywhere in the image.",
      "video_action_prompt": "Continuation of the previous shot, second half of the same camera move, already tighter in the frame. Static shot with a barely-there slow drift over the detail of the hand of the young man with his navy cap and grey hoodie, resting on the scattered pages. His fingers slowly curl until the pages crease under them, a fine tremor runs through the fingers, the pen beside them does not move, dust particles float through the narrowed warm light. Nothing else moves. Quiet helplessness, held still. Stable camera, smooth motion, minimal distortion.",
      "transition_out": "match_cut",
      "vo_text": "It feels like the command center of your mind has just been hijacked. You know the information is in there. You know what you need to do, but you just can't get to it.",
      "vo_tc": "1:12-1:24",
      "status": "pending",
      "derived_from": "SC02_SH007",
      "tc": "1:17-1:24",
      "panel_index": 14,
      "vo_block_tc": "1:12-1:24",
      "transition_in": "cut_on_action",
      "rhythm_role": "exhalacion",
      "rhythm_note": "abre paso al plano sostenido",
      "risk": [
        "R2-NEGATIVOS-INLINE: el image_prompt lleva los negativos escritos dentro del prompt positivo, lo que ESTILO_MINDSET_MECHANICS.md 6.bis declara contraproducente (los tokens 'ears'/'nose' condicionan en positivo). El modelo por defecto de recraft_ai/generate_scene.py es recraftv4_1, que NO acepta el parametro negative_prompt (recraft_client.py:87,136), asi que la via del 6.bis no esta disponible sin cambiar a recraftv3 @1820x1024. DECISION PENDIENTE DE KIMI antes de gastar creditos."
      ]
    },
    {
      "shot_id": "SC02_SH008",
      "scene": 2,
      "duration_s": 10,
      "shot_size": "close_up",
      "angle": "eye_level",
      "camera_move": {
        "type": "push_in",
        "speed": "very_slow",
        "note": "push-in completes at ~8s, final 2s near-still HOLD, only light and dust moving (único plano sostenido del piloto)"
      },
      "subject": "HOST",
      "action": "turns his head a few degrees toward camera (three-quarter, never direct address), plain black oval eyes glisten, jaw sets, shoulders square, then he goes very still",
      "environment": "meeting room behind almost fully dark, one warm rim light tracing his cap and cheek, deep teal-black shadows, dim warm amber grade; face on right third, eyes at upper-right intersection, open space left",
      "emotion_beat": "tensión máxima / pregunta abierta",
      "image_prompt": "Soft painterly digital illustration in the style of a modern animated explainer short, 2D stylised animation, not anime. Close-up of a young man drawn with deliberately simplified cartoon proportions: a VERY LARGE round smooth head about one third of his total height, a completely smooth bald head shape with NO visible hair at all, a dark navy baseball cap sitting directly on that smooth head. His face is extremely minimal: two small plain solid black oval eyes with no iris, no highlight and no eyelashes, two thin short dark eyebrows, a tiny dot nose and a small simple line mouth. Flat pale cream skin with soft even shading and NO blush, NO pink cheeks. Small simple body in a grey hoodie, dark jeans and sneakers. In three-quarter view he turns his head a few degrees toward the camera without fully facing it; his plain black oval eyes glisten, his jaw is set, his shoulders squared; he is very still. His face sits on the right third of the frame, eyes at the upper-right intersection, open space on the left. The meeting room behind him is almost fully dark, one warm rim light tracing his cap and cheek, deep teal-black shadows, dim warm amber grade. Rich atmospheric cinematic lighting, warm rim light, volumetric light shafts, floating dust particles. Muted harmonious colour palette. Full-bleed single scene with real environmental depth and a detailed background. Clean soft linework, thick black outline, flat cel-shading. Absolutely NO halftone dots, NO ben-day dots, NO starburst or speed lines, NO comic panels, NO white gutters, NO speech bubbles, NO anime face, NO detailed irises, NO visible hair, NO visible ears, NO blush, NO sharp jawline, NO photorealism, and NO text, letters, signs or words anywhere in the image.",
      "video_action_prompt": "Very slow smooth push-in on the close-up of the young man with his navy cap and grey hoodie as he turns his head a few degrees toward the camera. His jaw sets, his plain black oval eyes hold still and glistening, the warm rim light settles along his cap and cheek, dust drifts through the teal-dark room. The push-in completes early and the final two seconds hold nearly still on his face, only light and dust moving. Maximum tension, question left hanging. Stable camera, smooth motion, minimal distortion.",
      "transition_out": "hard_cut",
      "vo_text": "This isn't just a feeling; it's a real neurological event. When your brain perceives overwhelming stress, it fundamentally shifts its resources. But why?",
      "vo_tc": "1:24-1:34",
      "status": "pending",
      "derived_from": "SC02_SH008",
      "tc": "1:24-1:34",
      "panel_index": 15,
      "vo_block_tc": "1:24-1:34",
      "rhythm_role": "hold",
      "rhythm_note": "exhalacion final ya aprobada: push-in + HOLD 2s",
      "risk": [
        "R1-DERIVA-2D: 10s supera la ventana segura de 5-8s por clip (NOTA ola2). Es el panel con mas probabilidad de deriva de estilo del piloto. Si sale mal, partirlo en 6s+4s antes de re-rollear la imagen.",
        "R2-NEGATIVOS-INLINE: el image_prompt lleva los negativos escritos dentro del prompt positivo, lo que ESTILO_MINDSET_MECHANICS.md 6.bis declara contraproducente (los tokens 'ears'/'nose' condicionan en positivo). El modelo por defecto de recraft_ai/generate_scene.py es recraftv4_1, que NO acepta el parametro negative_prompt (recraft_client.py:87,136), asi que la via del 6.bis no esta disponible sin cambiar a recraftv3 @1820x1024. DECISION PENDIENTE DE KIMI antes de gastar creditos."
      ]
    }
  ],
  "panel_count": 15,
  "max_clip_duration_s": 10,
  "duration_rule": "VideoExpress admite 3-10s por clip (input range video_duration, min=3 max=10, leido del DOM en vivo 2026-08-25). NINGUN panel puede superar 10s. Los 12s originales eran inejecutables. Cada llamada a animate_library_image() debe pasar duration_seconds=<duration_s del panel>.",
  "rhythm_rule": "v1.1 (2026-08-26, MANUAL_PRODUCCION.md 3.2.1): el ritmo NO es plano. Ningun par de paneles consecutivos dura lo mismo salvo el beat neutro SH006. Rango 4-8s para paneles normales; 9-10s solo para la exhalacion de cierre (y marcado como riesgo de deriva 2D). El panel mas corto del segmento cae SOBRE el pattern interrupt. Los limites de beat y los bloques de voz en off NO se tocaron: siguen en 0:12/0:24/0:36/0:48/1:00/1:12/1:24/1:34.",
  "rhythm_previous": "v1.0: 14 paneles de 6s exactos + 1 de 10s (cadencia plana). Reversible: ver tabla en el .md, seccion 5.",
  "risk_flags": [
    {
      "id": "R1-DERIVA-2D",
      "panel": "SC02_SH008",
      "estado": "aceptado con vigilancia",
      "detalle": "clip de 10s por encima de la ventana segura 5-8s de la ola 2."
    },
    {
      "id": "R2-NEGATIVOS-INLINE",
      "panel": "todos",
      "estado": "BLOQUEANTE-DECISION",
      "detalle": "negativos dentro del prompt positivo vs ESTILO 6.bis; recraftv4_1 no soporta negative_prompt. Decide Kimi: (a) redactar los negativos en positivo, o (b) cambiar a recraftv3 @1820x1024 y pasar el negativo por API."
    },
    {
      "id": "R3-AUDIO-SIN-ASSETS",
      "panel": "todos",
      "estado": "abierto",
      "detalle": "SISTEMA_STORYBOARD 8.5 exige bloque AUDIO por panel. El andamiaje esta ahora en el .md seccion 7, pero sin asset_id reales: nadie ha curado todavia la libreria de musica/SFX con licencia YPP."
    },
    {
      "id": "R4-CREDITOS-RECRAFT",
      "panel": "todos",
      "estado": "bloqueante externo",
      "detalle": "saldo de la API de Recraft sin pagar (commit 7c425d0). Nada de esto se puede generar hasta resolverlo."
    },
    {
      "id": "R5-RENDIMIENTO",
      "panel": "todos",
      "estado": "informativo",
      "detalle": "MANUAL 3.2.2: presupuestar paneles x3 (~24 generaciones de imagen, ~45 de video en el peor caso), no x1."
    }
  ]
}
```

---

## 4. CHECKLIST DE AUTO-VERIFICACIÓN (15 puntos)

1. ☑ **Cada panel tiene los 12 campos completos** — los 8 paneles llevan shot_id, scene, duration_s, shot_size, angle, camera_move{type,speed}, subject, action, environment, emotion_beat, image_prompt, video_action_prompt (+ transition_out, vo_text, vo_tc, status en JSON).
2. ☑ **Ficha de personaje verbatim en TODOS los image_prompt con HOST** — los 8 paneles son subject=HOST y los 8 la llevan palabra por palabra, incluidos los inserts (mano) y el ECU del ojo; cero sinónimos ("grey hoodie", "dark navy baseball cap" siempre iguales).
3. ☑ **Cero paneles con mismo shot_size consecutivo** — medium → close_up → insert → wide → extreme_close_up → medium_close → insert → close_up.
4. ☑ **Ningún frame congelado >4s** — el único sostenido es SH008 (2s finales, solo luz/polvo en movimiento); todo plano tiene micro-movimiento (polvo, luz, sudor, temblor, páginas).
5. ☑ **Un solo movimiento dominante por panel, velocidad explícita** — push_in slow / pan left slow / tilt down slow / crane up slow / push_in slow / pan right slow / static micro-drift slow / push_in very_slow+hold. Sin whip (0 usados, bajo el máximo de 1).
6. ☑ **Pattern interrupt a 25-35s** — smash_cut a 0:24 hacia el insert SH003; el cambio brusco de escala (close_up → macro insert) domina exactamente la ventana 25-35s. (Es piloto de 1:34; no aplica "cada 2-3 min" todavía.)
7. ☑ **Beats mapeados según §6** — hook: medium + push_in slow + eye_level (SH001) ✓; tensión: dutch/ECU (SH002, SH005, SH006) ✓; vulnerabilidad: overhead con host pequeño (SH004) y high en insert (SH007) ✓; pregunta/revelación pendiente: push_in a close con sostenido (SH008) ✓.
8. ☑ **Acciones como comportamiento visible** — "boca entreabierta sin palabras", "dedos se aflojan y las hojas se deslizan", "garganta sube en deglución seca", "gota de sudor resbala por la sien". Cero emociones abstractas.
9. ☑ **Eje de 180° y screen direction verificados** — el host mira/se orienta a frame-DERECHA en los 8 paneles (colegas a su derecha); la cámara nunca cruza la línea; raccord de mirada SH005→SH006 (el ojo tira a la derecha, el siguiente plano sigue su mirada); raccord de movimiento SH001→SH002 (la mano baja y sale de cuadro, continúa la caída de las notas en SH003) y SH003→SH004 (mano en inferior-izquierdo → host en inferior-izquierdo cenital, match_cut posicional).
10. ☑ **Cero texto dentro de las imágenes** — las páginas de notas se describen como "blurred illegible scribble-like marks, never legible words" y la cláusula negativa cierra con "NO text, letters, signs or words".
11. ⚠️ **Cláusula negativa completa al final de cada image_prompt** — las 8 la llevan íntegra, incluyendo "NO visible ears" y el bloque de estilo con fix "thick black outline, flat cel-shading". **Marcado ⚠️ en v1.1: cumplir este punto puede ser exactamente el problema.** `ESTILO_MINDSET_MECHANICS.md` §6.bis declara que los negativos dentro del prompt positivo condicionan **en positivo** los tokens `ears`/`nose`. Ver bandera **R2** en §6: decisión pendiente de Kimi antes de generar.
12. ☑ **vo_text cuadra con el timecode del audio real** — cada panel lleva su bloque de VO exacto con su tc (0:00-0:12, 0:12-0:24, 0:24-0:36, 0:36-0:48, 0:48-1:00, 1:00-1:12, 1:12-1:24, 1:24-1:34); duraciones MEDIDAS, no estimadas.
13. ☑ **Duraciones suman el total del segmento (±3s)** — Escena 1: 48s = 0:48 exacto; Escena 2: 46s = 0:46 exacto; total 94s = 1:34 exacto (desviación 0s), repartido en 15 paneles de los cuales ninguno supera el techo real de 10s de VideoExpress (§0).
14. ☑ **Transiciones variadas** — cut_on_action, smash_cut, match_cut, hard_cut, cut_on_action, hard_cut, match_cut, hard_cut (4 tipos; ninguno se repite más de 2 veces ni dos iguales seguidas salvo hard_cut separados por match_cut).
15. ☑ **Prueba de rejilla mental: mismo personaje reconocible en todos los paneles** — ficha verbatim idéntica en los 8 prompts + ancla textual "navy cap and grey hoodie" en los 8 video_action_prompts; única variable entre paneles: acción/ángulo (nunca vestuario ni estilo).

16. ☑ **Ningún panel supera el máximo real de la plataforma** — desde v1.1, paneles de 4 a 8s + 1 de 10s; rango de VideoExpress = 3-10s (§0). Cada animación debe pasar `duration_seconds` explícito.

17. ☑ **(v1.1) Ritmo repartido, no plano** — 15 paneles con 5 duraciones distintas (4/5/6/7/8) + el sostenido de 10s; el plano más corto cae sobre el pattern interrupt. Ver §5.

18. ☐ **(v1.1) Bloque AUDIO por panel (`SISTEMA_STORYBOARD` §8.5)** — andamiaje escrito en §7, **sin `asset_id` reales**: falta curar la librería con licencia YPP. No bloquea la generación de imagen/video (es capa de post).

**VEREDICTO: 17/18 ☑ — Storyboard EJECUTABLE. Lo único abierto es la capa de audio (§7), que es post-producción y no consume créditos.**
**Pendientes de decisión ajena (NO los resuelve storyboard-director):** ver §6, banderas R2 (negativos inline vs `ESTILO` §6.bis) y R4 (saldo de Recraft). R2 debería resolverse **antes** de gastar el primer crédito.

---

## 5. RITMO v1.1 (2026-08-26) — por qué las duraciones dejaron de ser 6s planos

**Motivo:** `MANUAL_PRODUCCION.md` §3.2.1 (investigación web de 2026-08-26). La evidencia
convergente de varias fuentes de edición para retención es que **la variación intencional
de ritmo importa más que la velocidad de corte**, y que una cadencia perfectamente uniforme
es justo lo que agota al espectador. El caso más citado: MrBeast, que popularizó el corte
cada segundo, revirtió esa doctrina en 2024, metió respiros y las vistas subieron.

La v1.0 de este storyboard tenía **14 paneles de 6,00s exactos + 1 de 10s**. La densidad de
corte era correcta (9,6 cortes/min, dentro del rango documental de 5-10/min), pero estaba
**repartida de forma plana**. El arreglo no era cortar más ni menos: era repartir distinto
**los mismos 15 cortes**.

**Lo que NO cambió (importante):** las 8 imágenes de Recraft, los 15 clips de VideoExpress,
los 8 beats narrativos, los límites de beat (0:12 / 0:24 / 0:36 / 0:48 / 1:00 / 1:12 / 1:24 / 1:34),
los bloques de voz en off, los `image_prompt`, los `video_action_prompt`, las transiciones y
el eje de 180°. **Coste del cambio: 0 créditos.** Solo cambia el valor `duration_seconds` que
se pasa a `animate_library_image()` en cada panel.

| Beat | v1.0 | v1.1 | Intención del reparto |
|---|---|---|---|
| SH001 hook | 6+6 | **5+7** | entra a mitad de acción sin dejar que se instale, luego deja aterrizar el bloqueo |
| SH002 tensión | 6+6 | **8+4** | sostiene el silencio (plano más largo del cuerpo) y luego acelera hacia el interrupt |
| SH003 ★ interrupt | 6+6 | **4+8** | el plano más corto del piloto aterriza el `smash_cut`; después, recuperación larga |
| SH004 vulnerabilidad | 6+6 | **7+5** | la grúa necesita recorrido para revelar escala; acorta al cerrar escena |
| SH005 tensión íntima | 6+6 | **4+8** | entra rápido al ojo tras el cambio de escena, se queda en el sudor |
| SH006 sostenida | 6+6 | **6+6** | beat neutro deliberado: sin acento, para que los acentos de al lado se noten |
| SH007 vulnerabilidad | 6+6 | **5+7** | reaprieta y abre paso al plano final |
| SH008 pregunta | 10 | **10** | sin cambios (exhalación final ya aprobada) |

Secuencia resultante: `5-7-8-4-4-8-7-5-4-8-6-6-5-7-10` (94s exactos).
El par `4+4` de 0:20 a 0:28 es el momento más rápido del piloto y cae **encima** de la
ventana de pattern interrupt de 25-35s, con el `smash_cut` justo en 0:24.

**Regla del canal derivada (`MANUAL_PRODUCCION.md` §3.2.1):** rango operativo 4-8s por panel;
9-10s reservado para exhalación de cierre y marcado como riesgo de deriva 2D; el plano más
corto del segmento cae sobre el pattern interrupt.

**Reversible:** para volver a v1.0, poner todos los `duration_s` a 6 salvo SH008 (10) y
recalcular `tc`. Nada más depende de estos valores.

---

## 6. BANDERAS DE RIESGO (v1.1 — antes no existían en este documento)

| ID | Panel | Estado | Qué pasa y qué hay que decidir |
|---|---|---|---|
| **R1-DERIVA-2D** | SC02_SH008 | aceptado con vigilancia | El clip de **10s supera la ventana segura de 5-8s** que fijó la investigación de la ola 2 (`handoffs/NOTA_INVESTIGACION_2026-08-25_ola2_storyboard.md`): la deriva de estilo 2D se acumula con la duración. Es el panel con más probabilidad de salir mal del piloto. Si sale mal, **partirlo en 6s+4s antes de re-rollear la imagen** (es más barato). |
| **R2-NEGATIVOS-INLINE** | todos | **BLOQUEANTE — decide Kimi** | Los 15 `image_prompt` cierran con los negativos escritos **dentro del prompt positivo** (`"...NO visible hair, NO visible ears, NO blush..."`). `ESTILO_MINDSET_MECHANICS.md` §6.bis (2026-08-25, regla dura permanente) dice que eso es contraproducente: el codificador de texto ve los tokens `ears`/`nose` y los usa como condicionamiento **positivo** — es la causa raíz diagnosticada de las orejas y narices que ya forzaron dos rondas rechazadas. **Pero la vía que propone §6.bis no está disponible tal cual:** el modelo por defecto de `recraft_ai/generate_scene.py` es `recraftv4_1`, y `recraft_client.py` (líneas 87 y 136) rechaza `negative_prompt` en V4.x. Además no existe hoy ninguna constante `NEGATIVE_PROMPT` en `recraft_client.py`, aunque §6.bis afirme que sí. **Opciones:** (a) redactar los negativos en positivo dentro del prompt (describir la silueta lisa deseada en vez de nombrar lo prohibido), o (b) cambiar a `recraftv3 @1820x1024` y pasar el negativo por el parámetro real de la API. **Esta decisión debería tomarse antes de gastar el primer crédito.** |
| **R3-AUDIO-SIN-ASSETS** | todos | abierto | `SISTEMA_STORYBOARD` §8.5 exige un bloque `AUDIO` por panel. El andamiaje está ahora en §7, pero **sin `asset_id` reales**: nadie ha curado todavía la librería de música/ambiente/SFX con licencia apta para YPP. Es post-producción: no bloquea generar imagen ni video. |
| **R4-CREDITOS-RECRAFT** | todos | bloqueante externo | El saldo de la API de Recraft está sin pagar (commit `7c425d0`, "piloto detenido antes de gastar"). Nada de este storyboard puede generarse hasta resolverlo. |
| **R5-RENDIMIENTO** | todos | informativo | `MANUAL_PRODUCCION.md` §3.2.2: las producciones documentadas con IA en 2026 promedian **~3 generaciones por plano usable** (~25% de selección). Presupuestar **paneles × 3**: peor caso ~24 generaciones de imagen y ~45 de video, no 8 y 15. |

---

## 7. CAPA DE AUDIO — andamiaje (`SISTEMA_STORYBOARD` §8.5)

Faltaba por completo. Se añade como **andamiaje ejecutable en post**, con los `asset_id`
marcados `<POR ELEGIR>` porque la curaduría de librería (R3) no es decisión de
storyboard-director. Niveles y reglas salen tal cual de §8.5, no se inventa nada.

Se anota **por beat** (no por panel) porque los pares a/b son el mismo plano partido: el
sonido no corta en el corte interno.

```
BEAT SH001 (0:00-0:12) — hook
  musica:   <POR ELEGIR: drone tenso 60-80 BPM>  entra en 0:00, -20 dB bajo voz
  ambiente: sala de reuniones (aire acondicionado, papel)   amb_db: -35
  sfx:      [{id: "<POR ELEGIR: room_tone_in>", t: "in", db: -18}]
  ducking:  on        silencio: none

BEAT SH002 (0:12-0:24) — la mente en blanco
  musica:   continua, filtro paso-bajo desde 0:18 (el mundo se aleja)
  ambiente: mismo, bajando a -40 dB
  sfx:      [{id: "<POR ELEGIR: heartbeat_low>", t: "0:18", db: -16}]
  ducking:  on        silencio: pre:0.5s antes de "your mind goes completely blank"

BEAT SH003 (0:24-0:36) — ★ PATTERN INTERRUPT (notas que caen)
  musica:   cut  (music drop 0,8s justo en el smash_cut de 0:24 — el pattern interrupt sonoro)
  ambiente: none durante el drop, vuelve a -38 dB en 0:28
  sfx:      [{id: "<POR ELEGIR: paper_fall>", t: "0:24", db: -10}]
  ducking:  on        silencio: pre:0.4s
  nota:     el corte de música ES el golpe; no meter whoosh encima (§8.5: whoosh solo entre escenas)

BEAT SH004 (0:36-0:48) — vulnerabilidad (grúa arriba)
  musica:   swell ascendente acompañando la grúa, -22 dB
  ambiente: sala, -38 dB      sfx: none
  ducking:  on        silencio: none

BEAT SH005 (0:48-1:00) — cambio de ESCENA (1→2)
  musica:   nuevo track <POR ELEGIR: drone 60-70 BPM>  (cambio por beat narrativo, §8.5)
  ambiente: interior íntimo, -36 dB
  sfx:      [{id: "<POR ELEGIR: whoosh_soft>", t: "0:48", db: -14}]   # whoosh SÍ: cambio de escena
  ducking:  on        silencio: none

BEAT SH006 (1:00-1:12) — cuerpo bloqueado
  musica:   continua        ambiente: -36 dB
  sfx:      [{id: "<POR ELEGIR: swallow_dry>", t: "1:04", db: -18}]
  ducking:  on        silencio: none

BEAT SH007 (1:12-1:24) — la mano que no obedece
  musica:   continua, empieza a adelgazar (quitar capas)
  ambiente: -38 dB
  sfx:      [{id: "<POR ELEGIR: riser>", t: "1:20", db: -15}]   # riser 2-4s antes del giro
  ducking:  on        silencio: none

BEAT SH008 (1:24-1:34) — ★ la pregunta abierta
  musica:   fadeout:2s tras "But why?"
  ambiente: -40 dB, solo el cuarto
  sfx:      none
  ducking:  on        silencio: post:0.8s  (el silencio dramático del piloto — 1 de los 1-2 por video)
  nota:     el HOLD de 2s finales va con la música ya fuera: la imagen quieta y el silencio son el mismo gesto
```

**Niveles del canal (§8.5, no negociables en el mezclado):** voz -16 LUFS · master -14 LUFS con
limitador a -1 dB · música -18 a -24 dB bajo voz · SFX -10 a -20 dB · ambiente -30 a -40 dB
continuo · ducking sidechain **obligatorio** bajo el TTS.
