# Mindset Mechanics — Biblia de estilo visual (LOCK)

## SOLUCIÓN DEFINITIVA DE CONSISTENCIA — 2026-08-23: cambio de herramienta para generar imágenes

**Problema cerrado.** Tras repetidos intentos de forzar consistencia con prompts de texto en VideoExpress (Técnica B) y probar en vivo la función "Consistent Character" de VideoExpress (Técnica A, con imagen de referencia real `true_character_ref`), se confirmó que **VideoExpress no es capaz de reproducir el estilo del personaje de forma fiel** en ninguno de los dos modos probados:
- `Image Type: Human` → sale fotorrealista.
- `Image Type: 2D` → sale estilo anime (pelo visible, ojos con iris/brillo, orejas marcadas).

**Solución adoptada:** generar las imágenes de cada escena en **Recraft AI** (recraft.ai), no en VideoExpress. Recraft está especializado en ilustración vectorial plana y su función de referencia de imagen sí mantiene la identidad del personaje sin reinterpretar el estilo. Probado en vivo: subiendo `true_character_ref` como referencia y pidiendo una escena nueva ("standing at a window at night looking out over a city"), el resultado fue prácticamente idéntico al personaje real del canal — contorno grueso, sin orejas, sin nariz, cel-shading plano. Confirmado visualmente por David.

**Límite real del plan gratuito (corrección del dato anterior — no son 50 créditos genéricos):** el plan gratuito de Recraft solo permite **2 generaciones/día usando referencia de personaje**, con el modelo **"Nano Banana"** (el que sí respeta `true_character_ref`). Es un límite estrecho para producción en volumen — con 9-13 escenas por video (`MANUAL_PRODUCCION.md` §4), un solo video tarda varios días en generarse a este ritmo. David está en proceso de pasar al **plan Basic (12 USD/mes con facturación mensual)** para quitar ese límite — ojo: Recraft anuncia "10 USD/mes" en su página de precios, pero ese número solo aplica si se paga facturación **anual**; facturación mensual son 12 USD/mes. No confundir los dos precios al presupuestar.

**Flujo de producción vigente de aquí en adelante:**
1. **Recraft AI** — generar cada imagen de escena, subiendo `true_character_ref` (o el mejor frame de referencia disponible) como imagen de referencia en el chat, describiendo la escena nueva en el prompt (nunca solo "mismo personaje", siempre describir también el estilo: "flat 2D cel-shaded vector cartoon style, bold black outlines, no visible ears, no nose").
2. Exportar cada imagen en PNG, 300 DPI, tamaño completo.
3. **VideoExpress** — usar esas imágenes ya correctas SOLO para animar (Image to Video / First Frame-Last Frame), nunca para generar la imagen base del personaje desde cero.

Esto reemplaza el flujo anterior (Técnica B, generación de imagen directamente en VideoExpress con prompt de texto repetido). La Técnica B queda documentada abajo (§2, §6, §8) como referencia histórica de lo que no funcionó de forma confiable.


> Escrita el 2026-08-22 tras detectar que el 5º video ("Resiliencia", `youtube_pipeline/channels/mindset_mechanics/output/video.mp4`) **rompe por completo** el estilo del canal y no es publicable. Todo lo que se genere de aquí en adelante se valida contra este documento antes de ensamblar.

---

## CORRECCIÓN MAYOR — 2026-08-23, validada contra frames reales de los 4 videos ya publicados

**Todo lo escrito en §1-§6 de este documento (versión original) describía el estilo INCORRECTO**, y no se detectó hasta comparar generaciones nuevas lado a lado con frames extraídos directamente de los videos ya publicados en el canal — no contra esta descripción escrita. La sesión que escribió este documento validó la plantilla contra un retrato estático de prueba, nunca contra el canal real, y confundió "evitar los tropos de cómic americano" (semitono, viñetas, globos de diálogo — eso sí era el error real del 5º video) con "evitar el contorno grueso y el cel-shading plano" — que en realidad SÍ es el estilo real del canal.

**Lo que el canal real tiene (confirmado visualmente, frame por frame, contra 4 videos publicados):**
- **Contorno negro grueso y limpio** alrededor de todo el personaje y los objetos — estilo vector plano, no entintado de cómic con semitono, pero SÍ una línea de contorno marcada.
- **Cel-shading plano**, sin gradientes suaves ni iluminación atmosférica pictórica.
- **Sin orejas visibles** — la cabeza es una forma lisa continua, esto nunca estaba escrito explícitamente en la plantilla original y era la fuente #1 de deriva.
- Sin nariz (esto sí estaba bien identificado).
- Sombreado por bloques de color plano, no degradados.

**Lo que SÍ seguía siendo cierto del documento original:** nada de semitono/puntos Ben-Day, nada de viñetas múltiples con márgenes blancos, nada de globos de diálogo, nada de anime, nada de texto dentro de la imagen, nada de fotorrealismo.

**La plantilla de prompt correcta y validada está en §8** (reemplaza a la de §6, que queda como referencia histórica de lo que NO hay que repetir).

---

## 0. El error que originó este documento

El video de Resiliencia se generó con prompts del tipo `"Flat 2D vector comic panel of..."` + `Image Type: 2D`. Eso produce **cómic americano plano**, que NO es el estilo del canal. Defectos concretos que salieron:

| Defecto | Qué pasó |
|---|---|
| Estilo equivocado | Tramas de semitono, fondos de estallido, viñetas con márgenes blancos, globos de diálogo |
| Personaje inconsistente | Cara distinta en casi cada escena (anime detallado, mandíbula marcada) |
| Sin subtítulos | Cero texto quemado; los otros 4 videos sí lo tienen |
| Resolución | 720p contra 1080p del resto del canal |
| Texto basura de IA | Letreros generados dentro de la imagen con errores ("SIENAL JAMMED") |

**Regla dura:** nunca usar las palabras `comic`, `comic panel`, `halftone`, `vector`, `flat` en un prompt de este canal.

---

## 1. Personaje (bloqueado)

- Cabeza **redonda/ovalada y ligeramente grande** respecto al cuerpo. Proporción semi-chibi, NO realista, NO anime.
- Ojos: **óvalos negros simples**, sin iris detallado, sin brillos anime, sin pestañas.
- Cejas finas y oscuras. Nariz mínima (un trazo o punto). Boca pequeña y simple.
- Piel: tono crema plano con sombreado suave.
- Vestuario fijo: **gorra de béisbol azul marino/oscura** (a veces al revés), **hoodie gris** (a veces verde oliva), jeans oscuros, tenis.
- Sin mandíbula marcada, sin músculos, sin rasgos afilados.

## 2. Estilo de arte (bloqueado)

**SÍ:**
- Ilustración digital **pictórica y suave**, tipo animación indie moderna / explainer cinematográfico.
- Línea limpia pero **no entintado grueso de cómic**.
- **Iluminación atmosférica rica**: luz cálida de lámpara, sol de atardecer por ventanas, luz de borde (rim light), haces volumétricos, partículas de polvo flotando.
- Paletas apagadas y armónicas: naranjas/ámbar cálidos en interiores, azules/verdeazulados fríos en noche.
- **Escena única a sangre completa** con profundidad real y fondo detallado (estanterías, escritorios, calles, laboratorios).

**NO (lista de exclusión, va literal en el prompt negativo):**
- tramas de semitono / puntos Ben-Day
- fondos de estallido, líneas de velocidad, rayos decorativos
- viñetas múltiples, márgenes/gutters blancos
- globos de diálogo, onomatopeyas
- caras anime u ojos detallados
- estética foto-realista
- **cualquier texto dentro de la imagen** (la IA lo escribe mal — el texto va solo en los subtítulos quemados en post)

## 3. Cámara y encuadre

Lo que ya se usa en los videos publicados (mantener la variedad, nunca repetir el mismo plano dos escenas seguidas):

| Plano | Uso |
|---|---|
| Primerísimo plano | Ojo con reflejo (fuego, pantalla) — para momentos de tensión |
| Sobre el hombro | Cuando el personaje lee/mira algo (papel, teléfono) |
| Picado (desde arriba) | Escritorio, objetos, sensación de agobio |
| Plano general | Establecer lugar (calle nocturna, laboratorio, mercado) |
| Plano medio | Diálogo/narración normal |
| Contrapicado | Poder, amenaza, revelación |

**Mejora a aplicar de aquí en adelante** (esto es lo que pidió el usuario):
- Alternar **distancia focal aparente**: intercalar un primerísimo plano cada 3-4 escenas para romper el ritmo.
- Añadir **movimiento de cámara real** con `First Frame, Last Frame` de VideoExpress v3.0 (ver §5) en vez de Ken Burns simulado: dolly-in lento, retroceso revelador, paneo lateral con paralaje.
- Regla de continuidad: si la escena N termina en primer plano, la N+1 abre en plano abierto (y viceversa).

## 4. Subtítulos quemados (obligatorio)

- Mayúsculas, tipografía **negrita condensada**.
- Color **amarillo** con **contorno negro grueso**.
- Centrados, tercio inferior.
- **3-4 palabras por bloque** (así están los 4 videos publicados; además de esto dependen los recortes de Shorts).

## 5. Funciones de VideoExpress v3.0 a explotar

Del catálogo oficial (https://videoexpress.ai/tutorials/, sección "Video Express v3.0"):

- **`First Frame, Last Frame`** — la más importante para lo que se pidió. Se define la composición inicial y la final y la app interpola: da dolly/push/paneo **reales**, no el zoom falso de Ken Burns.
- **`Transition Between Effects`** — transiciones entre escenas; hoy el pipeline solo hace crossfade.
- **`Stylize Character`** — img2img sobre una imagen real del personaje. **Mejor que prompt de texto libre** para mantener la identidad, porque no regenera desde cero.
- **`Text to Video`** — clips animados de hasta ~10s, sin límite de cantidad.
- **`Fix Subtitles`** / **`Separate Audio and Video`** / **`Voice Changer`** — post-producción.
- **`Smart Edit v2`** (inpainting / object removal) — arreglar un artefacto suelto en vez de regenerar el plano entero.

Flujos largos documentados que aplican al canal: **Masterclass #2** (video largo end-to-end con personaje consistente) y **Customer Training #16** (documental). El flujo "Idea → Documental 3D" usa un GPT propio que genera arco narrativo + prompts de imagen + prompts de imagen-a-video + narración por escena.

## 6. Plantilla de prompt — VALIDADA 2026-08-22

Probada de verdad contra VideoExpress (`video_express_ai/outputs/style_lock_v2.jpg`) y comparada frame a frame contra los videos publicados: **coincide**. Usar tal cual, sustituyendo solo `{PLANO}` y `{ESCENA}`.

Hicieron falta dos pasadas. La v1 salió buena en luz/paleta/profundidad pero el personaje se fue hacia anime: cabeza de proporción normal, flequillo negro visible bajo la gorra y rubor rosado en las mejillas. Las tres frases que lo arreglaron son las que van en MAYÚSCULAS abajo — **no quitarlas**.

```
Soft painterly digital illustration in the style of a modern animated explainer
short, 2D stylised animation, not anime. {PLANO} of a young man drawn with
deliberately simplified cartoon proportions: a VERY LARGE round smooth head
about one third of his total height, a completely smooth bald head shape with
NO visible hair at all, a dark navy baseball cap sitting directly on that
smooth head. His face is extremely minimal: two small plain solid black oval
eyes with no iris, no highlight and no eyelashes, two thin short dark eyebrows,
a tiny dot nose and a small simple line mouth. Flat pale cream skin with soft
even shading and NO blush, NO pink cheeks. Small simple body in a grey hoodie,
dark jeans and sneakers.

Scene: {ESCENA}

Rich atmospheric cinematic lighting, warm rim light, volumetric light shafts,
floating dust particles. Muted harmonious colour palette. Full-bleed single
scene with real environmental depth and a detailed background. Clean soft
linework, gentle painterly shading.

Absolutely NO halftone dots, NO ben-day dots, NO starburst or speed lines, NO
comic panels, NO white gutters, NO speech bubbles, NO anime face, NO detailed
irises, NO visible hair, NO blush, NO sharp jawline, NO photorealism, and NO
text, letters, signs or words anywhere in the image.
```

Ajustes en la app: `--type 2D`, **desmarcar "Automatically enhance my image prompt"** (se re-marca solo en cada apertura del modal) y **no** dejar `Image Type: Human` por defecto.

### 6.1 Addendum 2026-08-23 — deriva de nariz en escenas narrativas con movimiento de cámara

Detectado al regenerar Resiliencia: la plantilla de arriba (que sí quedó bien en un retrato estático de prueba) produce una **nariz claramente visible y rasgos más anime** cuando el prompt describe una escena narrativa completa (varios personajes, entorno, cámara en movimiento) en vez de un plano de personaje aislado. La cláusula "a tiny dot nose" no bastaba — no había ninguna prohibición explícita de nariz en la cláusula negativa original, así que el modelo tenía margen para dibujar una.

**Fix aplicado (usar de aquí en adelante en todo prompt de escena, no solo en retratos):**
- En la ficha de personaje, reemplazar `"a tiny dot nose and a small simple line mouth"` por: `"absolutely no nose of any kind — the space between the eyes and mouth is completely flat and smooth with no nose shape, no nostrils, no nose bridge, and no nose shadow — and a small simple line mouth"`.
- En la cláusula negativa, añadir explícitamente: `NO nose, NO nostrils, NO nose bridge, NO nose shadow, NO nose shape of any kind` (antes no estaba, solo se confiaba en la descripción positiva).

No se sobreescribe la plantilla original de arriba porque sigue siendo válida para retratos estáticos — este addendum aplica específicamente a escenas narrativas con contexto/cámara, que es el caso real de producción.

**Segunda ronda (mismo día):** al reforzar solo la nariz, la siguiente generación corrigió la nariz pero introdujo **mejillas rosadas visibles** — pese a que "NO blush, NO pink cheeks" ya estaba en la descripción positiva original. La cláusula negativa original NUNCA repetía la prohibición de blush, solo confiaba en la descripción positiva (mismo patrón de fallo que la nariz). Fix: reemplazar `"Flat pale cream skin with soft even shading and NO blush, NO pink cheeks"` por `"Completely flat pale cream skin colour with soft even shading, absolutely no rosy tint and no red or pink coloring anywhere on the face or cheeks — the cheeks are the exact same flat cream colour as the rest of the face, with no blush, no flush, and no warm coloring of any kind"`, y añadir a la cláusula negativa `NO blush, NO pink cheeks, NO rosy cheeks, NO flushed skin` (antes solo decía "NO blush" sin variantes).

**Lección operativa:** cualquier rasgo prohibido solo en la descripción POSITIVA (nunca repetido en la cláusula NEGATIVA) es un punto de fuga conocido en escenas narrativas complejas. Antes de escribir un prompt nuevo, verificar que cada "NO X" del personaje también aparece, con sinónimos, en la cláusula negativa final.

**Techo detectado de la Técnica B (solo texto) en este canal:** se probó también generar con la Reference Photo (`REFERENCIA_personaje.png`) seleccionada como base de imagen (sin depender del botón roto de Consistent Character) — la generación no dejó rastro localizable en la librería para verificar si mejoraba la fidelidad. No investigar más esta ruta por ahora (ver `MANUAL_PRODUCCION.md` §2, Técnica A queda diferida). Vía de producción vigente: Técnica B con las dos correcciones de arriba, aceptando que puede requerir 1-2 rondas de ajuste por lote de escenas.

Comando:
```bash
python generate_video.py image "$(cat prompt.txt)" --type 2D --out escena_01.jpg
```

## 7. Checklist antes de ensamblar cualquier video

- [ ] Todas las escenas comparten la misma cara del personaje
- [ ] Cero texto dentro de las imágenes
- [ ] Cero tramas de semitono / viñetas / globos
- [ ] Variedad de planos, sin repetir dos iguales seguidos
- [ ] Salida a **1920x1080**, nunca 720p
- [ ] Subtítulos quemados en amarillo con contorno negro, 3-4 palabras
- [ ] Badge de suscripción insertado (solo videos largos)
- [ ] Validado con `ffmpeg -f null` sin errores
- [ ] Comparado visualmente lado a lado contra un frame real de un video YA PUBLICADO (no solo contra este documento) — es el único chequeo que detecta deriva de estilo que la descripción escrita no captura

## 8. Plantilla de prompt v4 — VALIDADA 2026-08-23 contra frames reales publicados (reemplaza a §6)

Probada en vivo, comparada lado a lado contra un frame extraído directamente de `The-Psychological-Secret-to-Solving-EVERYTHING-Unlock-Your-Master-Mind.mp4` (uno de los 4 videos ya publicados) — coincide en contorno, ausencia de orejas, ausencia de nariz y cel-shading plano. Usar tal cual, sustituyendo `{PLANO}` y `{ESCENA}`.

**Ficha de personaje:**
```
Flat 2D vector cartoon illustration, cel-shaded animation style with bold thick
clean black outlines around the character and every object in the scene, like
a modern animated web series. {PLANO} of a young man with deliberately
simplified cartoon proportions: a large round smooth bald head with absolutely
no hair and no ears visible at all, a dark navy blue baseball cap sitting
directly on the smooth head. His face is extremely minimal and flat: two
simple solid black oval eyes with no iris detail and no highlight, two thick
short dark eyebrows, absolutely no nose of any kind — completely flat and
smooth between the eyes and mouth, no nose shape, no nostrils — and a small
simple black line mouth. Flat solid cream skin tone with minimal flat shading,
no gradients, no blush, no pink cheeks, no rosy tint anywhere on the face.
Simple flat-colored grey hoodie, dark jeans, sneakers.
```

**Sufijo de estilo/luz:**
```
Flat cel-shaded coloring throughout, bold clean black outlines on every shape,
moderate warm lighting rendered as flat color blocks rather than soft
gradients, simple flat background with clear detail, graphic-novel /
flat-vector illustration quality, crisp and clean linework.
```

**Cláusula negativa:**
```
Absolutely NO soft painterly shading, NO atmospheric glow, NO volumetric light
shafts, NO floating dust particles, NO photorealism, NO anime face, NO
detailed irises, NO visible hair, NO visible ears, NO blush, NO pink cheeks,
NO rosy cheeks, NO flushed skin, NO sharp jawline, NO nose, NO nostrils, NO
nose bridge, NO nose shadow, NO nose shape of any kind, NO halftone dots, NO
ben-day dots, NO starburst or speed lines, NO comic panels, NO white gutters,
NO speech bubbles, and NO text, letters, signs or words anywhere in the image.
```

**Diferencia clave contra §6 (la plantilla vieja, ya no usar):** se eliminó "soft painterly", "gentle painterly shading", "rich atmospheric cinematic lighting, volumetric light shafts, floating dust particles" — ese lenguaje es exactamente lo que empujaba el resultado hacia un estilo pintado/atmosférico que el canal real no tiene. Se añadió "no visible ears" a la cláusula negativa, ausente en todas las versiones anteriores.

## 9. Pendientes abiertos (verificar antes de dar por cerrado el estilo)

- [ ] **Miniatura de "The Psychology of Discipline How to Trick Your Brain into Loving Hard Work" rompe la consistencia visual.** Muestra un personaje musculoso/estilo anime de acción, distinto al host bloqueado en §1/§8 (cabeza lisa sin orejas, sin nariz, cel-shading plano). Es el único de los videos publicados que no pasaría el checklist de `thumbnail-consistency-guardian`. **Pendiente de rehacer con el flujo vigente de Recraft AI + `true_character_ref`** (ver sección al inicio de este documento) — no usar VideoExpress para regenerarla. No marcar como resuelto hasta que se confirme visualmente contra un frame real, igual que se hizo con Resiliencia.

## 10. Opción de respaldo gratuita a futuro — Stable Diffusion / ComfyUI local

Investigado el 2026-08-23 como alternativa gratuita a Recraft, por si el límite de generaciones diarias (§ arriba) o el costo del plan Basic se vuelven un problema. **Decisión: NO usar ahora**, prioridad es velocidad de producción y Recraft ya funciona en vivo. Queda documentado como plan B.

- Ya está instalado en `C:\Users\David Peñuela\Documents\CLAUDE AUTOMATIC\ComfyUI`.
- Hardware disponible: GPU RTX 3050 con 4GB VRAM — suficiente para generación básica, pero ajustado para flujos con varios modelos cargados a la vez.
- Para igualar lo que Recraft da "gratis" (consistencia de personaje contra una imagen de referencia) haría falta montar un flujo con **IPAdapter + ControlNet + un LoRA entrenado del personaje** — viable en teoría con 4GB VRAM pero requiere configuración no trivial (instalar los tres componentes, entrenar o conseguir el LoRA, ajustar pesos) y no es un simple "subir imagen y listo" como Recraft.
- **Cuándo reconsiderar esto:** si el plan Basic de Recraft deja de ser suficiente (más volumen, más canales hermanos como Human Chronicles generando en paralelo) o si el costo mensual deja de justificarse, retomar esta vía como la alternativa gratuita de respaldo — no antes.
