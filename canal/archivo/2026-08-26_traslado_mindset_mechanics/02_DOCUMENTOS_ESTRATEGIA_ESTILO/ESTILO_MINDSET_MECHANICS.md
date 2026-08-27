# Mindset Mechanics — Biblia de estilo visual (LOCK)

> Escrita el 2026-08-22 tras detectar que el 5º video ("Resiliencia", `youtube_pipeline/channels/mindset_mechanics/output/video.mp4`) **rompe por completo** el estilo del canal y no es publicable. Todo lo que se genere de aquí en adelante se valida contra este documento antes de ensamblar.

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

Comando:
```bash
python generate_video.py image "$(cat prompt.txt)" --type 2D --out escena_01.jpg
```

## 6.bis Los negativos NO van en el prompt positivo (hallazgo 2026-08-25)

**Regla dura, permanente.** Las orejas y la nariz siguieron apareciendo tras
DOS pasadas de plantilla (§6.1 y §8) por un motivo técnico, no creativo: los
negativos se escribían como texto dentro del prompt positivo
(`"Absolutely NO visible ears, NO nose, NO nostrils..."`).

Los modelos de difusión **no entienden la negación lingüística**. El
codificador de texto ve los tokens `ears`, `nose`, `nostrils` y los usa como
condicionamiento **positivo**. Escribir "NO nose" cinco veces —como hacía
`video_express_ai/_scene01_prompt_v4.txt`— hace la nariz **más** probable, no
menos. Es el efecto "no pienses en un elefante rosa".

La vía correcta es el parámetro `negative_prompt` de la API, que se aplica
como guía negativa real en el espacio latente (classifier-free guidance) y no
como texto a interpretar. Recraft lo soporta en `/images/generations`.

- Los negativos canónicos del canal viven en `recraft_ai/recraft_client.py`
  → constante `NEGATIVE_PROMPT`, y se aplican **por defecto** en cada
  generación. No hay que copiarlos a mano en ningún prompt.
- El prompt positivo describe **solo lo que sí debe verse**. Si un prompt
  nuevo contiene la palabra "NO", está mal escrito.
- La telemetría D6 registra el `negative_prompt` usado en cada generación,
  así que se puede auditar después.

> Esto **no está verificado todavía contra una generación real** (requiere
> saldo de la API de Recraft, pendiente de autorización de David). Está
> verificado que el parámetro se envía correctamente y queda registrado.

## 7. Checklist antes de ensamblar cualquier video

- [ ] Todas las escenas comparten la misma cara del personaje
- [ ] Cero texto dentro de las imágenes
- [ ] Cero tramas de semitono / viñetas / globos
- [ ] Variedad de planos, sin repetir dos iguales seguidos
- [ ] Salida a **1920x1080**, nunca 720p
- [ ] Subtítulos quemados en amarillo con contorno negro, 3-4 palabras
- [ ] Badge de suscripción insertado (solo videos largos)
- [ ] Validado con `ffmpeg -f null` sin errores
