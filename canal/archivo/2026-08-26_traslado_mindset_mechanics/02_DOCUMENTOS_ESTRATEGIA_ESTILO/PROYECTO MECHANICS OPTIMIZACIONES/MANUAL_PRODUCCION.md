# Manual de producción — VideoExpress.ai para Mindset Mechanics
**Escrito 2026-08-22.** Síntesis operativa de `INVESTIGACION_tutoriales_videoexpress.md` (9 de 10 documentos oficiales de VideoExpress leídos completos; falló `Customer Training #10` por límite semanal de cuenta, no reintentado aquí). Se complementa con `ESTILO_MINDSET_MECHANICS.md` (biblia de estilo visual, ya validada contra el canal real) — este manual no repite esa parte, se centra en el FLUJO de producción.

**ACTUALIZACIÓN 2026-08-23 — la imagen base del personaje ya NO se genera aquí.** Todo lo que sigue en §1-§2 sobre "Consistent Character" (Técnica A) y repetición textual (Técnica B) para generar la IMAGEN del personaje en VideoExpress quedó superado: se confirmó que VideoExpress no reproduce el estilo del canal de forma fiel (sale fotorrealista o anime según el `Image Type`). **La imagen de cada escena se genera ahora en Recraft AI**, subiendo `true_character_ref.jpg` como referencia — ver la sección "SOLUCIÓN DEFINITIVA DE CONSISTENCIA" al inicio de `ESTILO_MINDSET_MECHANICS.md`. VideoExpress se sigue usando para TODO lo demás de este manual: animar esas imágenes ya generadas (`First Frame, Last Frame`, Image to Video), el vocabulario de cámara (§3, §3.1) y el ensamblaje — nada de eso cambió, solo el origen de la imagen fija de cada escena.

**Corrección sobre la sesión anterior, ya verificada en vivo (2026-08-22):** `ESTILO_MINDSET_MECHANICS.md` §5 presenta `First Frame, Last Frame` como "la función más importante" para movimiento de cámara real. Los 9 documentos oficiales de VideoExpress **no la mencionan ni una sola vez** — pero SÍ existe en la app real, en el panel "Create with AI", listada junto a "Create Video From Prompt" y "Text To Video", marcada con una etiqueta **"Beta"** (captura tomada en vivo el 2026-08-22). Conclusión: es real pero tan nueva que ningún tutorial la cubre todavía — trátala como beta al usarla (validar cada resultado, tener plan B) y sigue usando el flujo de "Video Action Prompt" en lenguaje natural (§3) como vía principal, probada y estable. Vale la pena un experimento A/B pequeño comparando ambas antes de comprometer el pipeline completo a una u otra.

---

## 1. El patrón nuclear, confirmado en 6 de 9 documentos

Cada escena se genera con **dos prompts separados y nunca fusionados**:

1. **Image Prompt / Image Scene Prompt** — descripción ESTÁTICA del fotograma: sujeto + pose + entorno + iluminación + composición + etiqueta de estilo. Esto genera la imagen fija (el "primer frame" real de la escena).
2. **Video Action Prompt** — SOLO el movimiento: qué hace la cámara + qué se mueve dentro del plano (pelo, polvo, ropa, luz) + a veces el audio ambiental al final. 1-2 frases, casi siempre empezando por el tipo de movimiento de cámara.

Mecanismo implícito de continuidad: se genera la imagen primero, se aprueba, y LUEGO se anima esa imagen concreta con el Video Action Prompt — no se generan imagen y video a ciegas por separado. Esto reduce deriva dentro de cada escena individual (aunque no resuelve la consistencia ENTRE escenas — eso es la sección 2).

Algunos docs añaden un tercer y cuarto campo separados:
- **Audio Prompt** — ambiente + SFX + música, en lista separada por comas, SIN narración ("no dialogue, no narration, no voices").
- **Speech** — una sola frase corta de diálogo entre comillas, cuando el formato sí lleva voz por escena (formato Talking Photo / historias cortas).

Para un documental narrado como Mindset Mechanics, el modelo correcto (confirmado explícitamente en Customer Training #14, el único doc que lo dice así) es: **generar todo el material visual sin narración ni diálogo, con audio limitado a ambiente/SFX, y montar la narración documental encima en el ensamblaje** — que es exactamente cómo ya funciona vuestro `youtube_pipeline` (TTS + subtítulos quemados en post). No hace falta cambiar esa arquitectura.

---

## 2. Consistencia de personaje — el problema #1 del handoff, resuelto con evidencia real

Hay **dos técnicas documentadas**, y se pueden (y deben) combinar. Ninguna de las 9 fuentes menciona seeds, LoRA, ni character-lock automático — todo el ecosistema de VideoExpress resuelve consistencia con dos mecanismos textuales/de referencia:

### Técnica A — "Consistent Character" con 4 vistas de referencia (la más fuerte, Customer Training #14)
1. Generar el personaje **antes que cualquier escena**, aislado, cuerpo entero, fondo blanco de estudio, mirando a cámara.
2. Para máxima consistencia, generar **4 vistas**: Front View, Back View, Left Side View, Right Side View.
3. Subir las 4 como referencias de **"Consistent Character"**.
4. En CADA generación de escena, activar dos casillas: **"Consistent Character"** + **"Prompt Enhancement"**.
5. Regla dura explícita del documento: *"Only your influencer should remain consistent. Everyone else should be random characters generated naturally for each scene. Do NOT use Consistent Character for background people."* — el toggle se activa solo para el host, nunca para personajes de fondo.

Una variante más simple (Customer Training #15 / #19) usa solo 2 vistas: primero el **"front shot"** sobre fondo blanco, y a continuación, en el mismo hilo/chat, pedir literalmente **"now create the backshot"**. Si 4 vistas resultan pesadas de producir al inicio, empezar con front+back es suficiente para activar Consistent Character.

### Técnica B — repetición textual verbatim (fallback universal, funciona en TODOS los docs incluso sin subir referencia)
Se fija una ficha de personaje densa, en una sola frase, y se **repite palabra por palabra** al inicio de cada Image Prompt de cada escena — nunca se abrevia a "same character" o "same outfit". El ejemplo más limpio (Customer Training #6, gatitos con impermeable): *"Two orange tabby kittens wearing yellow raincoats and rain boots"* aparece idéntico en las 6 escenas de la historia.

**Ficha canónica para el host de Mindset Mechanics (combinar ambas técnicas — subir como referencia Y repetir en cada prompt):**
```
Cartoon 2D documentary host character, large rounded oversized head, no nose, no hair, plain black oval eyes with no iris, thin dark eyebrows floating above the eyes, tiny mouth, flat cream skin, navy blue baseball cap covering the whole top of the head, grey hoodie over white t-shirt, rounded mitten-style hands, flat 2D animated documentary style, consistent appearance across all scenes.
```
(Esta frase deriva directamente del personaje ya bloqueado en `ESTILO_MINDSET_MECHANICS.md` §1 — no inventa nada nuevo, solo la empaqueta en el formato que las dos técnicas de VideoExpress esperan.)

**Acción concreta pendiente (handoff §5.3, ítem #4):** implementar `import_local_image()` en `video_express_bot.py`, copiando el patrón de `import_local_audio()` cambiando la carpeta destino de "Audio" a "Images" en la librería "My AI Images" de la app. Con eso se puede subir `REFERENCIA_personaje.png` (y las 2-4 vistas que se generen a partir de ella) y usarlas como referencia de Consistent Character en vez de depender solo de texto. Ver §5 de este documento para el plan de implementación.

### Clausula negativa estándar (pegar al final de cada Image Prompt)
Confirmada en 2 documentos, reduce contaminación de la escena con personajes/objetos no deseados:
```
Only the main character described — absolutely NO small side characters, NO children,
NO spectators, NO extra people in the corners or background. No text, no caption,
no watermark, no logo.
```
Para Mindset Mechanics, adaptar el final a vuestra regla ya existente: **"no text, letters, signs or words anywhere in the image"** (los subtítulos van solo en post).

---

## 3. Vocabulario de cámara — banco de frases listas para pegar en el Video Action Prompt

No hay sliders ni presets: todo es lenguaje natural. Vocabulario confirmado y agrupado por función narrativa (extraído literal de 3 documentos distintos):

| Función | Frases listas |
|---|---|
| **Apertura / revelación de lugar** | "Epic drone-style aerial shot begins high above [lugar]. Camera slowly descends..." / "Aerial drone shot slowly descends from above... before transitioning into a slow cinematic push-in." |
| **Acercamiento a un objeto/detalle** | "Extreme close-up of [objeto]. Camera tracks across... before revealing [rostro]." / "Slow dolly-in on [objeto]." |
| **Seguir al personaje** | "Tracking shot behind [host] as he walks toward [destino]." / "Ground-level tracking shot runs inches above the ground alongside [host]." |
| **Tensión / tono íntimo** | "Handheld camera trembles slightly, mirroring [emoción]." / "The camera lingers on [detalle emocional]." |
| **Revelación de escala** | "The camera performs a dramatic low-angle orbit around [host] before craning upwards into a bird's-eye view." / "Wide cinematic crane shot pulls upward, revealing [entorno]." |
| **Cierre de escena/acto** | "The camera slowly pulls back and rises higher, revealing [entorno] while [host] disappears into the horizon." / "Slow zoom toward [objeto] before cutting to black." |
| **Host hablando directo a cámara (narrador)** | "Still camera. [Host] looks directly toward the camera as if speaking to humanity." — útil para los planos de narración directa. |
| **Transición diegética entre escenas** | "Lights flicker back to life in his wake." / "Fade to black as his voice whispers: [línea]." |

**Patrón de montaje deducido (Customer Training #15):** apertura casi siempre aérea/dron descendente → escenas medias con tracking o push-in o primer plano extremo → clímax con órbita de 360° → cierre con grúa/pull-back ascendente. Aplica esto como arco por CADA acto del documental, no solo al video entero — coincide con la regla ya fijada en `ESTILO_MINDSET_MECHANICS.md` §3 de alternar distancia focal cada 3-4 escenas.

## 3.1 Nivel Netflix — reglas externas (2026-08-22, investigación web, no de VideoExpress)

Los documentos oficiales de VideoExpress dan vocabulario pero no reglas de calidad. Esto sí las da — síntesis de guías especializadas en prompting de cámara para IA de video (Atlabs AI, LzyPrompt) y de cinematografía documental profesional:

**Los 8 movimientos que de verdad importan** (todo lo demás es combinación de estos): estático, pan (giro horizontal), tilt (giro vertical), dolly in/out (acercar/alejar físicamente), tracking/lateral (seguir al lado), crane/boom (subir o bajar revelando escala), push-in/pull-out (zoom emocional hacia el rostro), orbit/arc (giro alrededor del sujeto). El banco de la tabla de arriba ya cubre los 8 — esto es la confirmación de que no falta ninguno.

**Fórmula de 4 partes para escribir cualquier Video Action Prompt de golpe:**
`[Movimiento + Velocidad] + [Sujeto/Acción] + [Qué revela el movimiento] + [Tono/ritmo]`
Ejemplo aplicado al host: *"Slow dolly in on him as the desk lamp flickers, shadows deepening behind him, tense and intimate."*

**Vocabulario de velocidad, de más lento a más rápido — úsalo siempre explícito, nunca lo dejes implícito:** imperceptible → slow → steady/measured → smooth/fluid → quick → whip/fast. **Regla dura medida:** los modelos de IA de video pierden calidad a velocidades rápidas — para Mindset Mechanics (tono cinematográfico, no acción) quedarse casi siempre en slow/smooth/steady, reservar whip/fast solo para un giro de shock puntual (como mucho 1 vez por video).

**Regla de encadenado de movimientos — la más importante para subir de nivel:** un solo movimiento por plano es la norma seria; el error de principiante es meter 3-4 movimientos distintos en un mismo Video Action Prompt y que la IA "no entienda" cuál priorizar. Si se necesita encadenar (p.ej. "empieza estático y luego hace push-in"), usar lenguaje de tiempo explícito — *"starts static on [detalle], then slowly tilts up to [rostro], then dollies in"* — y **nunca encadenar más de 2-3 movimientos**: más que eso y el resultado se vuelve inestable/incoherente en la mayoría de generadores (confirmado, no es intuición).

**Orden de las piezas dentro del prompt (los modelos priorizan los tokens tempranos):** 1) sujeto, 2) acción, 3) movimiento de cámara, 4) encuadre/lente, 5) estilo/iluminación. Aplicado: primero quién y qué hace, luego cómo se mueve la cámara, al final el look. Esto es un ajuste de ORDEN sobre las plantillas que ya usa el canal, no un cambio de contenido.

**Ancla el sujeto para evitar deriva:** nombrar explícitamente el sujeto dentro de la instrucción de movimiento (no solo "the character" sino "[host], with his navy cap and grey hoodie,") reduce que la IA pierda el encuadre o cambie identidad a mitad de plano — es la misma lógica de la Técnica B de consistencia (§2), aplicada ahora al Video Action Prompt y no solo al Image Prompt.

**De la cinematografía documental real (no de IA):** el pan y el tilt son la base — reserva el pan para seguir acción dentro de una escena y el tilt para revelar altura/escala (una estantería completa, la ventana de un rascacielos). El hand-held (cámara en mano, con temblor sutil) se usa deliberadamente para tensión/intimidad — no es un error, es una elección; reservarlo para los momentos de mayor carga emocional del guion (el giro oscuro al 55%, la escena de segunda persona), y usar cámara estabilizada/fluida para el resto — ese contraste deliberado es lo que hace que el momento hand-held se sienta especial en vez de descuidado.

**Encaje directo con la regla ya fijada en `ESTILO_MINDSET_MECHANICS.md` §3** (alternar distancia focal cada 3-4 escenas, nunca repetir el mismo plano dos veces seguidas): ahora esa regla tiene, además, el arco de acto completo de §3 arriba (apertura aérea → medio con tracking/push-in → clímax con orbit → cierre con crane/pull-back) para aplicar UNA vez por cada acto del guion (ver `PLAYBOOK_MONETIZACION.md` §3 para dónde caen los actos), no solo una vez por video entero — con eso, un documental de 10-13 min con 4 actos tiene 4 micro-arcos cinematográficos completos en vez de uno solo diluido.

**Ritmo de corte — cuánto debe durar cada plano visible, no cada "escena narrativa":** el dato de referencia de edición profesional es que el largometraje promedio corta cada 4-6s, pero el documental premiado sostiene tomas más largas, ~15s de media — equilibrando ritmo con profundidad narrativa. Traducción práctica para Mindset Mechanics: el bloque de 60-80s por escena de guion (§4) NO debe ser un solo plano fijo de 60-80s — hay que partirlo en **3-5 planos de 12-20s cada uno** dentro de ese mismo bloque, cada uno con su propio Video Action Prompt (un movimiento distinto del banco de arriba), igual que ya recomienda cortar más corto para subir tensión y dejar tomas más largas en momentos de alivio/calma. Esto es lo que separa un video que "se ve como fotos que se mueven" de uno que se siente montado como documental real.

**Composición — regla de tercios, aplicada plano a plano:** divide el encuadre en una rejilla de 3x3; coloca el punto de interés (los ojos del host, el objeto clave de la escena) sobre una de las 4 intersecciones, nunca centrado por defecto. Para planos de "narrador mirando a cámara" (Escena 7 del `RESILIENCE_SCENE_PLAN.md`, por ejemplo): coloca la línea de sus ojos en el tercio superior, con "espacio de mirada" (looking room) hacia donde mira — se ve profesional en vez de forzado. Es la técnica de composición más usada en cine, foto y animación combinadas; romperla a propósito (centrar al sujeto) es válido solo cuando el guion pide simetría/confrontación directa (el giro meta al 70%, por ejemplo). Se puede pedir directo en el Image Prompt: *"framed using the rule of thirds, subject's eyes on the upper-left intersection point"*.

**Gradación de color — nombrarla explícita, no dejarla implícita:** los generadores de 2026 responden fuerte a lenguaje de color grading nombrado, igual que responden a movimiento de cámara nombrado. En vez de solo "warm lighting", ser tan específico como ya se es con la cámara: *"warm golden-hour color grade"*, *"desaturated cinematic tones"*, *"lifted shadows, rolled-off highlights, warm skin tones"*. Esto encaja exacto con la paleta ya bloqueada del canal (`ESTILO_MINDSET_MECHANICS.md` §2: "naranjas/ámbar cálidos en interiores, azules/verdeazulados fríos en noche") — solo hay que nombrarla con más precisión técnica en el prompt en vez de dejarla en adjetivos genéricos.

**Nota sobre otros generadores (Sora/Veo/Kling), por si el canal migra de motor más adelante:** los tres responden al mismo lenguaje de "8 capas de control" — sujeto, emoción, óptica (lente/profundidad de campo), movimiento, iluminación, estilo, audio, continuidad — coherente con todo lo de arriba. Diferencias a tener en cuenta si se prueba otro motor: Sora responde fuerte a dirección de cámara detallada y lenguaje de lente (anamorphic, depth of field, 24fps); Veo sigue mejor indicaciones de audio/diálogo dentro del prompt; Kling es más económico para volumen alto y es fuerte en movimiento humano fluido — el más parecido en objetivo a lo que necesita este canal si algún día hay que generar en volumen.

Fuentes de esta sección: [Atlabs AI — Ultimate Prompt Guide: Best Camera Movement Prompts for AI Videos 2026](https://www.atlabs.ai/blog/ultimate-prompt-guide-best-camera-movement-prompts-for-ai-videos-2026), [LzyPrompt — AI Video Camera Movement Prompts: The 2026 Director's Cheatsheet](https://lzyprompt.com/blog/ai-video-camera-movement-prompts/), [StudioBinder — A Beginner's Guide to Cinematography Techniques](https://www.studiobinder.com/blog/cinematography-techniques-no-film-school/), [DocFilmAcademy — Camera Movement in Documentaries: 5 Techniques That Work](https://www.docfilmacademy.com/blog/5-basic-camera-movements), [StudioBinder — How Editors Control Rhythm and Pacing](https://www.studiobinder.com/blog/how-does-an-editor-control-the-rhythm-of-a-film/), [StudioBinder — Rules of Shot Composition in Film](https://www.studiobinder.com/blog/rules-of-shot-composition-in-film/), [Veo3AI — How to Get a Cinematic Film Look with Veo 3: Color Grading & LUT-Style Prompts](https://www.veo3ai.io/blog/veo-3-cinematic-film-look-color-grading-2026), [VO3 AI — How to Prompt Sora 2 Pro, Kling & Veo 3 for Cinematic AI Video](https://www.vo3ai.com/blog/how-to-use-sora-2-pro-kling-25-and-veo-3-to-create-cinematic-ai-videos-step-by-s-2026-03-22).

## 3.2 Addendum 2026-08-26 — ritmo respirado, rendimiento por generación y anclaje espacial

Investigación web de hoy (agosto 2026), contrastando fuentes distintas por cada punto. Esto **no repite** §3 ni §3.1: corrige tres cosas que aquellas secciones dejan mal resueltas (el ritmo plano, el presupuesto por panel, y la ambigüedad espacial del Image Prompt) y añade un cuarto anclaje que hoy no existe en el canal (referencia de escenario).

### 3.2.1 El ritmo NO es una cadencia fija — es un arco que respira [corrige §3.1 "ritmo de corte"]

§3.1 fija "3-5 planos de 12-20s" y `SISTEMA_STORYBOARD` §5.1 fija "cambio visual cada 10-14s, ASL 8-12s". Ambas describen una cadencia **uniforme**, y la evidencia de 2026 dice que la uniformidad es justo lo que no funciona: *"pace serves the story, not the other way around; cutting faster than your story can carry will hurt retention, not help it"*. El dato más fuerte no es teórico: **MrBeast, que popularizó el corte cada segundo, revirtió públicamente esa doctrina en 2024, ralentizó sus videos, metió respiros y las vistas subieron.** La conclusión convergente de las fuentes es que **la variación intencional de ritmo importa más que la velocidad de corte**.

Tres patrones concretos, medidos, para sustituir la cadencia plana:

| Patrón | Cómo se ejecuta | Dónde aplica en un documental de 10-13 min |
|---|---|---|
| **Progresivo** | Cortes cortos y resets visuales cada 10-20s en la entrada; una vez enganchado, se ensancha a 25-40s por corte | Los primeros 30-45s del video (hook) van más apretados que el resto — luego se abre |
| **Respiración** | Bloque rápido (3-4 planos cortos) seguido de UN plano largo. Inhalar (energía) / exhalar (procesar) | Es el patrón por defecto de todo el cuerpo del video, escena a escena |
| **Ráfaga (burst)** | Cadencia normal 15-25s por corte, y **cada 2-3 minutos** una ráfaga de 5-10 cortes rápidos, y vuelta a la calma | Sustituye al "pattern interrupt cada 2-3 min" genérico de `SISTEMA_STORYBOARD` §5.3 por algo ejecutable |

**Referencia de densidad para documental (no para vlog):** interview/documental ronda **5-10 cortes por minuto**; *"si tu documental tiene 40 cortes por minuto, probablemente vas demasiado rápido"*. Nuestro piloto iba a 15 cortes en 94s ≈ 9,6 cortes/min: dentro del rango correcto **pero repartidos de forma perfectamente plana** (14 paneles de 6s exactos). El arreglo no era cortar más ni menos, era **repartir distinto los mismos cortes**.

**Traducción obligatoria a nuestra plataforma (esto es nuestro, no de las fuentes):** VideoExpress topa el clip en **10s** (`SISTEMA_STORYBOARD` / storyboard piloto §0) y la deriva de estilo 2D se acumula con la duración (ola 2: ventana segura 5-8s). Así que **no podemos ejecutar literalmente los 25-40s de "exhalación" de las fuentes**: nuestra escala está comprimida por el motor. La regla del canal queda:

> **Regla de respiración Mindset Mechanics:** dentro de cada bloque narrativo, ningún par de planos consecutivos dura lo mismo. Rango operativo **4-8s** para planos normales; **9-10s reservado** para la exhalación de cierre de acto (y marcado como riesgo de deriva, porque supera la ventana segura de 2D). El plano más corto del video cae **sobre el pattern interrupt**, no en cualquier sitio.

Si algún día se quiere una ráfaga real (5-10 cortes rápidos seguidos), eso **cuesta generaciones extra** — es decisión de presupuesto, no de dirección.

Fuentes: [AIR Media-Tech — Advanced retention editing: cutting patterns that keep viewers past minute 8](https://air.io/en/youtube-hacks/advanced-retention-editing-cutting-patterns-that-keep-viewers-past-minute-8), [VidPros — Video Clip Length: Ultimate Guide for Every Editing Style](https://vidpros.com/video-clip-length/), [Shortzly — Short-Form Video Pacing: The Editing Rhythm Guide (2026)](https://shortzly.com/blog/short-form-video-pacing-editing-guide), [Mark Studios — Complete Video Editing & YouTube Growth Guide 2026](https://www.markstudios.com/guide), [Pixflow — YouTube Video Retention Editing](https://pixflow.net/blog/youtube-video-retention-editing/).

### 3.2.2 Rendimiento real por generación — el presupuesto de §4 está calculado 3× por debajo

§4 presupuesta "12 escenas = 12 generaciones". Eso asume que cada generación sale usable a la primera, y los datos de producciones documentadas con IA en 2026 dicen lo contrario:

- **~3 generaciones por plano usable** y **~25% de tasa de selección de clip** — *"credits go furthest when you plan around that yield instead of chasing perfect single takes"*.
- **68% de los usuarios agotan sus créditos a mitad de proyecto** por subestimar regeneraciones y refinamientos.

**Regla dura nueva del canal:** todo presupuesto de un video se calcula como **paneles × 3**, no paneles × 1. Un piloto de 8 imágenes + 15 animaciones se presupuesta como **~24 generaciones de imagen y ~45 de video en el peor caso**, y se lanza por lotes con gate humano entre lotes (que es lo que ya hace el proyecto). Este número explica retroactivamente por qué el canal ya pagó dos rondas de regeneración completas: no fue mala suerte, es el rendimiento normal del medio, y hay que presupuestarlo.

Corolario, coincidente en las 3 fuentes: **bloquear las referencias ANTES de generar escenas** — *"consistency re-rolls burn more credits than anything else"*, y *"a common mistake that slows beginners down is generating scenes before locking characters and shot structure"*. El orden correcto es imagen aprobada primero, movimiento después: *"consistency problems are cheap to fix in an image and expensive to fix across generated footage"*. El canal ya hace esto con el personaje; ver 3.2.3 para lo que aún NO bloquea.

Fuentes: [Data Science Collective — The 2026 AI Video Production Playbook](https://medium.com/data-science-collective/the-2026-ai-video-production-playbook-bc683d5b85da), [invideo — How do you reduce AI video generation waste and get more](https://invideo.io/faq/how-do-you-reduce-ai-video-generation-waste-and-get-more/), [Digen — Why AI Video Generation Fails and How to Fix It (2026)](https://resource.digen.ai/common-mistakes-ai-video-generation-fix-2026/), [invideo — AI Storyboarding: The Complete Guide](https://invideo.io/blog/ai-storyboarding/).

### 3.2.3 Falta un anclaje: la referencia de ESCENARIO (hoy solo está bloqueado el personaje)

`DICCIONARIO_VISUAL_MINDSET_MECHANICS.md` canoniza escenarios recurrentes (Sala de Control, Sabana, Ciudad-Neón) **como texto**, pero el canal no tiene una imagen de referencia bloqueada por escenario — solo la tiene del personaje (`true_character_ref.jpg`). Las fuentes de 2026 son explícitas en que el bloqueo se hace por lotes temáticos separados: *"separate references into thematic batches — spatial logic in one, color theory in another, a specific concept in a third"*, y que *"when the setting or lighting changes, give the model stronger anchors so it does not rebuild the character from scratch"*.

**Acción concreta:** la primera vez que un escenario del diccionario aparezca en producción, su still aprobado se guarda como `refs/escenario_<nombre>.png` y se usa como referencia en toda aparición posterior de ese escenario, en este y en futuros videos. Coste: 0 generaciones extra (es un still que igualmente se iba a generar; solo se archiva y se reutiliza). Beneficio: elimina la clase de re-roll más cara después de la del personaje.

Fuentes: [invideo — Reference Images for Consistent AI Video Characters](https://invideo.io/faq/how-do-you-use-reference-images-in-ai-video-generation/), [character.app — How to Make an AI Series with Consistent Characters (2026)](https://www.character.app/blog/how-to-make-an-ai-series), [Kittl — AI video character consistency workflow 2026](https://www.kittl.com/blogs/ai-video-character-consistency-workflow/).

### 3.2.4 Anclaje espacial explícito en el Image Prompt — la ambigüedad que aún queda

§3.1 ya obliga a la regla de tercios, pero eso solo coloca **un** punto de interés. Lo que las guías de prompting de 2026 añaden es la **descomposición en capas**: declarar explícitamente qué hay en primer plano, plano medio y fondo. *"Subject in midground, blurred crowd in background, railing in foreground"* — cada capa nombrada por separado crea profundidad y, sobre todo, **quita al generador la decisión de dónde poner cada cosa**. El mismo principio está detrás de que Ideogram 4.0 se entrenara con captions JSON estructurados con un campo `compositional_deconstruction`: *"JSON prompting removes guesswork by giving every element its own named key"*.

**Ampliación de la plantilla de `SISTEMA_STORYBOARD` §4** (orden de tokens, sin cambiar nada de lo que ya hay):

```
[FICHA_PERSONAJE_VERBATIM] + [shot_size + angle] + [action] + [CAPAS: foreground / midground / background]
+ [environment + grade nombrado] + [BLOQUE_ESTILO_FIJO] + [negativos según §6.bis de ESTILO]
```

Regla: la capa del sujeto se nombra siempre, aunque sea obvia ("host in midground"), porque es la que ancla la escala del plano. Los inserts declaran foreground y background aunque el midground quede vacío.

Fuentes: [Let's Enhance — How to write AI image prompts like a pro (2026)](https://letsenhance.io/blog/article/ai-text-prompt-guide/), [SurePrompts — How to Write AI Image Prompts: The 6-Part Formula (2026)](https://sureprompts.com/blog/how-to-write-ai-image-prompts), [DualView — JSON Prompts for AI Image Generation: Complete Guide 2025-2026](https://www.dualview.ai/blog/guides/json-prompts-ai-image.html), [Earngenix — Ideogram 4.0 JSON Prompt Format: Field-by-Field Guide (2026)](https://www.earngenix.com/tutorials/ideogram-4-prompt-guide-comfyui).

### 3.2.5 Nota de confianza y limitación de esta investigación

El proxy de red de la sesión bloqueó la descarga directa de todos los dominios consultados (`air.io`, `invideo.io`, `studiobinder.com`, `vidpros.com`, `myup.ai` — todos `EGRESS_BLOCKED`). Lo de arriba está construido sobre los **extractos devueltos por la búsqueda web**, no sobre el texto completo de cada artículo. Las cifras concretas (3 generaciones/plano usable, 25% de selección, 68% agotan créditos, 5-10 cortes/min en documental, 15-25s por corte en talking-head) aparecen citadas textualmente en esos extractos y **convergen entre fuentes distintas**, pero **no han sido verificadas contra el artículo completo**. Tratar como orientación fuerte, no como dato auditado. La regla derivada de 3.2.1 (repartir el ritmo en vez de aplanarlo) no depende de esas cifras: se sostiene sola.

---

## 4. Flujo extrapolado para 8-13 minutos (ningún doc lo cubre directo — esto es la síntesis)

Ningún documento oficial demuestra un video de más de 60 segundos / 8 escenas. Todos los ejemplos completos son historias cortas (5-10 escenas). El flujo de 8-13 minutos hay que construirlo escalando el mismo patrón:

1. **Bloque de estilo global** (una sola vez, se repite igual en cada prompt): tu párrafo ya validado de `ESTILO_MINDSET_MECHANICS.md` §6.
2. **Ficha de personaje canónica** (§2 de este doc), generada primero como referencia de 2-4 vistas.
3. **Guion dividido en actos** siguiendo el arco ya usado en el canal (planteamiento → evidencia → escena en 2ª persona → giro meta → cierre — ver `PLAYBOOK_MONETIZACION.md` §3), y cada acto dividido en escenas de 60-80s narrados (a diferencia de los ejemplos de VideoExpress que son clips de 5-8s sin narración, el vuestro va con narración continua en post, así que la escena visual puede ser más larga: 1 imagen/clip por cada 60-80s de guion, no por cada frase).
4. Para 10-13 minutos a razón de 1 escena nueva cada ~60-80s (igual que la cadencia medida en The Primal Glitch y Decode The Brain, que SÍ está confirmada en `PLAYBOOK_MONETIZACION.md`), eso da **9-13 escenas/imágenes por video** — mucho más manejable que la extrapolación ingenua a 60-80 micro-clips que sugeriría el patrón de Shorts. Genera 1 imagen fuerte por escena y anímala con un Video Action Prompt de cámara (dolly/push/pan/orbit) para llenar los 60-80s, en vez de trocear en decenas de clips de pocos segundos.
5. Cada Image Prompt de cada escena: `[bloque de estilo] + [ficha de personaje verbatim] + [descripción de la escena concreta] + [cláusula negativa]`.
6. Cada Video Action Prompt sigue la fórmula de 4 partes de §3.1: `[Movimiento + Velocidad, del banco de §3] + [qué hace/qué se mueve en el plano: polvo, ropa, luz] + [qué revela el movimiento] + [tono/ritmo] + [ambiente/SFX, sin narración]`. Máximo 2-3 movimientos encadenados por escena (§3.1).
7. Ensamblar en `youtube_pipeline` con la narración TTS y los subtítulos quemados ya existentes — esa parte del pipeline no cambia.

**VALIDADO EN VIVO 2026-08-22:** se generó una escena de prueba completa (`generate_video.py scene`) con la plantilla de personaje + un dolly-in lento hacia el rostro. Resultado: 1920x1080, movimiento de cámara real (no Ken Burns simulado), estilo consistente con `ESTILO_MINDSET_MECHANICS.md` en las 3 capturas del clip (inicio/medio/fin). El pipeline de imagen+cámara funciona de punta a punta tal como está descrito en este documento.

---

## 5. Estado de `import_local_image()` — IMPLEMENTADO Y PROBADO EN VIVO (2026-08-22)

`import_local_image()` ya existe en `video_express_ai/video_express_bot.py` (copiado del patrón de `import_local_audio()`, carpeta destino "Images" en vez de "Audio") y su comando CLI `generate_video.py import-image <ruta>`. **Subida de `REFERENCIA_personaje.png` confirmada en vivo, funciona.**

Lo que falta cerrar: `mark_consistent_character()` (comando `mark-character`) todavía falla al intentar marcar una imagen SUBIDA A MANO como Consistent Character. Diagnosticado en 4 rondas en vivo, cada una acotando más el problema:
1. El botón "Consistent Character" queda `disabled` sin una imagen activa en el modal — confirmado.
2. El botón "Use from Library"/"Reference Photo" sí es clickeable una vez se resuelve el disclaimer "I Agree" (que aparece INMEDIATAMENTE al marcar el checkbox "Use Consistent Character" y bloquea todo lo demás hasta aceptarlo — bug de orden ya corregido en el código).
3. Con el disclaimer aceptado Y una Reference Photo elegida de la carpeta "Images", el botón sigue `disabled`.
4. Con Reference Photo elegida Y texto en el Image Prompt, el botón SIGUE `disabled`.

Conclusión más probable tras las 4 rondas: el ícono del botón es "+" (`bi-plus-lg`) y su clase es `button-consistent-character-auto` — probablemente no sirve para registrar una foto subida directamente, sino para convertir en personaje reutilizable una imagen recién GENERADA por la app (flujo: click "Create Image" primero, usando la Reference Photo como base de generación si el modal lo permite, y solo sobre ESE resultado el botón se habilitaría). Próximo paso concreto para cerrar esto: generar una imagen con "Create Image" teniendo la Reference Photo ya seleccionada, y recién ahí revisar si el botón se habilita sobre el resultado.

**No bloquea producción** — Técnica B (repetición textual, §2) ya está validada en vivo con resultado de alta fidelidad (nota en §4). Técnica A es una mejora a perseguir cuando haya tiempo, no un requisito para producir el canal hoy.

**No bloquea producción hoy:** la Técnica B (repetición textual verbatim, §2) ya está validada en vivo con resultado de alta fidelidad (ver nota en §4). La Técnica A con imagen de referencia real es una mejora a perseguir, no un requisito.

**ACTUALIZACIÓN 2026-08-25 — Técnica B llegó a su techo, pivot a imagen real:** tras dos regeneraciones (§6.1 y plantilla §8) David siguió viendo orejas/nariz y rechazó el resultado por falta de dinamismo. Kimi decidió (`handoffs/HANDOFF_2026-08-25_decision_tercera_via_resiliencia.md`) cerrar la Técnica A tal como estaba descrita arriba y pasar a un pipeline nuevo: **Recraft AI genera la imagen de cada escena (ya validado que produce el personaje correcto) → se sube con `import_local_image()` → se anima DIRECTAMENTE con `animate_library_image()`** (función nueva, no la de arriba con "Consistent Character" — esa queda obsoleta para este flujo).

**Regla dura confirmada en vivo (2026-08-25): la imagen debe ser 16:9 o 9:16 exacto.** VideoExpress deja el botón "Create Video" deshabilitado sin ningún error visible hasta que ya elegiste la imagen — ahí aparece "Aspect ratio needs to be 16:9 or 9:16." Se probó con `true_character_ref.jpg` (650×900, retrato aislado de ficha de personaje) y falló por esto, no por otra cosa. **Consecuencia práctica: cada imagen de Recraft para animar debe exportarse como la ESCENA COMPLETA en 1920×1080 (personaje + composición + fondo), nunca como el retrato aislado del personaje.** `import_local_image()` ahora valida esto y falla rápido con mensaje claro si el aspecto no calza, en vez de descubrirse a mitad de una corrida real.

---

## 6. Checklist de producción por video (combina esto con el checklist de estilo ya existente en `ESTILO_MINDSET_MECHANICS.md` §7)

- [x] Pipeline imagen + cámara validado en vivo end-to-end (§4) — 1080p, movimiento real, estilo correcto
- [ ] Ficha de personaje repetida verbatim en cada Image Prompt (§2 Técnica B) — YA FUNCIONA. Referencia de Consistent Character (§2 Técnica A) — pendiente de cerrar el flujo del botón (§5)
- [ ] Cláusula negativa al final de cada Image Prompt
- [ ] Image Prompt y Video Action Prompt siempre en campos separados, nunca fusionados
- [ ] Video Action Prompt sigue la fórmula de 4 partes y el límite de 2-3 movimientos encadenados (§3.1), variando el tipo de plano acto a acto
- [ ] Sin narración/diálogo horneado en la generación visual — la voz se monta en post como ya hace el pipeline
- [x] "Automatically enhance my image prompt" — bug de desmarcado corregido y verificado en vivo 2026-08-22 (ver §7)
- [ ] `--type 2D` explícito, nunca dejar `Image Type: Human` por defecto
- [x] `First Frame, Last Frame` confirmada en vivo el 2026-08-22 (panel "Create with AI", etiqueta "Beta") — sin tutorial oficial todavía, tratar como experimental

---

## 7. Bugs reales encontrados y corregidos en `video_express_ai/` (2026-08-22)

Los tres primeros se encontraron reproduciendo el pipeline en vivo, no por inspección de código — cada uno bloqueaba `generate_video.py scene` por completo antes del fix:

1. **`scene` no estaba en el despachador de comandos de `generate_video.py`** — el subparser existía pero faltaba en el diccionario final, así que el comando lanzaba `KeyError` instantáneo. Corregido.
2. **El checkbox "Automatically enhance my image prompt" nunca se lograba desmarcar** — vivía dentro de un `<label class="custom-checkbox">` que lo oculta visualmente; el intento anterior (xpath + fallback de click por coordenadas) fallaba en silencio y la IA reescribía el prompt entero sin que nadie se enterara. Fix: apuntar al `name="auto_enhance_prompt"` real y clickear el `<label>` visible. Verificado en vivo: `checked=False` tras el fix.
3. **Si el panel "Create with AI" ya estaba abierto de una sesión anterior** (el tab activo persiste por cuenta, no por sesión de navegador), el nav item dejaba de resolver como `role="link"` y el bot se quedaba 60s esperando un clic que no hacía falta. Fix: comprobar primero si el marcador del panel ya es visible antes de intentar clickear.
4. **`cmd_mark_character` nunca abría el modal "Create Video From Prompt"** antes de buscar el checkbox "Use Consistent Character", que solo existe dentro de ese modal. Corregido (falta cerrar el punto 5 de arriba, el botón disabled).
5. **La sesión guardada de VideoExpress puede expirar** sin aviso — cuando pase, `setup_auth_auto.py` (variante sin bloqueo por `input()`, detecta el login solo) abre una ventana visible para que la persona real inicie sesión a mano; el bot nunca toca los campos de contraseña.
