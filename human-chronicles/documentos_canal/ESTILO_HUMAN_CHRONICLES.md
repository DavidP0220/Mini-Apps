# Human Chronicles — Manual de estilo y formato faceless

**Escrito 2026-08-25.** Es el equivalente de `ESTILO_MINDSET_MECHANICS.md` para el canal
hermano, pero parte de una premisa opuesta: **aquí NO hay personaje**. La consistencia de
marca no se sostiene en una cara recurrente, sino en tres cosas: **voz narrativa, paleta
visual y estructura del video**. Todo lo que sigue es la biblia de esas tres.

> Idioma: todo el material del canal (guion, prompts, títulos, descripciones, subtítulos)
> va en **inglés**. Esta documentación interna, en español. Ver `../POLITICA_IDIOMAS.md`.

---

## 1. El problema central de un canal faceless de historia

Un canal con host tiene un ancla visual gratis: el personaje. Un canal faceless sin ancla
se siente genérico, y desde julio de 2025 YouTube penaliza explícitamente eso bajo la
política de **"contenido no auténtico"** (renombrada desde "contenido repetitivo"). No
prohíbe la IA — prohíbe lo **producido en masa, repetitivo y sin criterio humano**:
plantillas idénticas, clips de stock reciclados, presentaciones sin narrativa, guiones
leídos literalmente de una fuente externa. A principios de 2026 miles de canales faceless
de IA perdieron la monetización bajo esa política.

**Conclusión de diseño para Human Chronicles:** el ancla de este canal es **el ángulo
narrativo original**, no la producción. Cada video tiene que aportar algo que no esté ya
en el artículo de Wikipedia del tema: una tesis, una comparación, un enfoque. Eso es
literalmente lo que separa "monetizable" de "demonetizado" hoy.

### Regla dura de autenticidad (no negociable)
1. **Nunca** leer un texto ajeno palabra por palabra. El guion se escribe original, con tesis propia.
2. **Nunca** publicar dos videos con la misma plantilla visual exacta (mismo orden de planos, mismas transiciones, mismo ritmo).
3. **Nunca** subir en lote 5-10 videos clonados. Mejor 2 videos/semana bien diferenciados.
4. **Declarar el contenido sintético** en YouTube (casilla "Altered or synthetic content")
   cuando haya imágenes generadas por IA que puedan confundirse con material real —
   obligatorio desde enero de 2026, y **la etiqueta no penaliza el alcance** (confirmado por YouTube).
   Para ilustración claramente estilizada normalmente no aplica; ante la duda, declararlo.

---

## 2. Voz narrativa (el verdadero "personaje" del canal)

Este es el ancla de marca. Debe ser reconocible en 10 segundos sin ver la pantalla.

**SÍ:**
- Tono de **documental sobrio y curioso**, no de "dato curioso" ni de sensacionalismo de clickbait hablado.
- Narrador en tercera persona, presente histórico para las escenas (`In 1204, the fleet turns north…`) y pasado para el análisis.
- Frases cortas. Una idea por frase. Ritmo de lectura ~150-160 palabras/minuto.
- Estructura de **tesis explícita en los primeros 30 segundos**: qué vas a demostrar en este video.
- Cerrar con una consecuencia contemporánea ("por eso hoy…") — es lo que genera comentarios.

**NO:**
- "Hey guys, welcome back to the channel" — arranque muerto, mata la retención inicial.
- CTA hablado de suscripción (misma regla ya validada en Mindset Mechanics).
- Voz TTS plana sin pausas ni variación. Las voces sintéticas de alta calidad **sí** son
  monetizables hoy; las robóticas y monótonas son justo el marcador que dispara la
  revisión por contenido no auténtico.
- Afirmar fechas, cifras o citas sin verificarlas. Un error histórico visible en los
  comentarios destruye la autoridad de un canal de historia más rápido que nada.

### Verificación factual (obligatoria antes de grabar VO)
Todo guion pasa por una lista de datos duros (fechas, nombres, cifras, lugares) con al
menos **dos fuentes independientes** por dato. Si un dato es disputado entre historiadores,
el guion lo dice ("los cronistas no coinciden en…") — eso suma credibilidad, no la resta.

---

## 3. Sistema visual (reemplaza a la ficha de personaje)

Sin host, la identidad visual se construye con **cuatro capas fijas**:

### 3.1 Paleta (bloqueada, se define una vez y no se toca)
Propuesta base para nicho histórico: pergamino/sepia cálido (#D8C3A5 aprox.), tinta oscura
(#2E2A26), y **un solo color de acento** para mapas y resaltados (rojo óxido o azul índigo).
Un único acento en todo el canal es lo que hace que una miniatura se reconozca al vuelo.
> Pendiente de aprobación de David/Kimi: es una decisión creativa, no técnica.

### 3.2 Tipografía y grafismos
- Una sola familia serif para títulos en pantalla y miniaturas, una sans para datos/etiquetas de mapa.
- Cartelas fijas recurrentes: nombre + año en la esquina al presentar cada lugar o persona.
  Esa cartela repetida ES marca — es el equivalente faceless del personaje recurrente.

### 3.3 Tipos de plano (el "banco" del canal)
| Tipo | Uso | Fuente |
|---|---|---|
| **Mapa animado** | Movimiento de ejércitos, rutas comerciales, expansión de imperios | Generado propio (base geográfica + animación) |
| **Ilustración de escena** | Momentos concretos sin registro fotográfico | **Recraft AI** |
| **Documento/artefacto** | Manuscritos, monedas, mapas antiguos reales | Dominio público (ver §4) |
| **Archivo real** | Solo eventos posteriores a ~1890 | Dominio público (ver §4) |
| **Texto en pantalla** | Cita textual de un cronista | Grafismo propio |

Regla de ritmo (heredada de `MANUAL_PRODUCCION.md` §3, sigue siendo válida): **nunca un
solo plano fijo sosteniendo un bloque narrativo de 45-60s**. 3-5 planos de 12-20s por bloque,
y **nunca la misma transición repetida en todo el video**.

### 3.4 Uso de Recraft en un canal SIN personaje consistente
Este es el cambio conceptual más importante frente a Mindset Mechanics.

- En Mindset Mechanics, Recraft se usa con `true_character_ref` para forzar que **la misma
  persona** aparezca idéntica en cada escena. **Aquí eso no aplica** — no hay personaje que preservar.
- Lo que sí hay que preservar es el **estilo de ilustración**. Por tanto:
  - Se crea **una imagen de referencia de ESTILO** (no de personaje): una escena histórica
    tipo, con la paleta y el tratamiento definitivos. Ese archivo cumple el rol que
    `true_character_ref.jpg` cumple en el otro canal.
  - Todo prompt de escena incluye descripción de estilo explícita, nunca "same style as before".
  - **Ventaja operativa:** al no depender de consistencia facial, el nivel de exigencia por
    imagen baja mucho → menos regeneraciones → **menos créditos por video que Mindset Mechanics**.
- **Nunca** generar rostros de personas históricas reales con IA como si fueran retratos
  fidedignos. Si hay retrato de dominio público, se usa el real. Si no lo hay, la ilustración
  debe ser claramente estilizada, nunca fotorrealista. Esto evita a la vez el problema de
  "semejanza sintética" y las quejas de rigor histórico.
- Formato de salida: PNG, 16:9 exacto para video largo, 9:16 para Shorts. **Verificar el
  aspecto ANTES de mandar a animar** — un aspecto equivocado ya rompió un paso del pipeline antes.

---

## 4. Fuentes de B-roll y material de archivo (verificadas)

Prioridad de uso: material real de dominio público primero, ilustración IA solo donde no
existe registro. Eso mejora tanto la credibilidad como el perfil de riesgo ante la política
de contenido no auténtico.

| Fuente | Qué tiene | Nota |
|---|---|---|
| **Library of Congress** | Millones de films, audio y fotografía | Mayormente material de EE.UU. |
| **Internet Archive — Moving Image Archive** | +2.5M de videos, incluye largometrajes y noticieros de dominio público | Verificar licencia ítem por ítem |
| **AP Archive (YouTube)** | Archivo fílmico de Associated Press | Licenciable; revisar términos |
| **Periscope Films (YouTube)** | Films preservados, usado por BBC/History/Smithsonian | Stock, no siempre libre |
| **PublicDomainFootage** | Archivo de dominio público de bajo costo | Usado por History Channel, NatGeo |
| **Gobierno de EE.UU. (CDC, NASA, NARA)** | Obra del gobierno federal = dominio público | Sin permiso requerido |

**Advertencia obligatoria:** que un video esté en dominio público **no** significa que todo
su contenido lo esté — puede llevar música con derechos, obra de arte protegida o imagen de
personas identificables. Verificar cada clip por separado y anotar la procedencia.

### Registro de procedencia (obligatorio)
Cada video mantiene un archivo `sources_<video>.md` con: cada clip/imagen usada, su URL de
origen, su licencia y la fecha de descarga. Sirve para dos cosas reales: responder un
reclamo de Content ID con evidencia, y sostener la sección de fuentes en la descripción
(que además es señal de esfuerzo humano frente a la política de contenido no auténtico).

---

## 5. Estructura estándar de un video largo

| Bloque | Duración | Función |
|---|---|---|
| Cold open | 0:00-0:20 | La imagen/pregunta más fuerte del video. Sin intro, sin saludo. |
| Tesis | 0:20-0:45 | Qué se va a demostrar y por qué importa. |
| Contexto | 0:45-2:00 | Mapa + situación. Primer mapa animado aquí. |
| Desarrollo (3 actos) | 2:00-8:00 | Cada acto cierra con un giro o una consecuencia. |
| Cierre | 8:00-9:00 | Consecuencia contemporánea + pregunta abierta para comentarios. |

Duración objetivo: **8-12 min** para el largo (permite mid-rolls y aprovecha el punto
fuerte del nicho, que es el watch time alto). Shorts de 30-50s como puerta de entrada.

Calidad mínima: **1080p siempre**, largos y Shorts. Regla global del proyecto.

---

## 6. Checklist antes de dar por terminado un video

- [ ] Guion original con tesis propia (no resumen de una sola fuente).
- [ ] Todos los datos duros verificados con 2 fuentes; disputas señaladas en el guion.
- [ ] `sources_<video>.md` completo, con licencia por ítem.
- [ ] Ningún plano fijo sosteniendo un bloque largo; transiciones variadas.
- [ ] Paleta y cartelas coherentes con el resto del canal.
- [ ] Sin rostros IA fotorrealistas de personas reales.
- [ ] 1080p mínimo, 16:9 (o 9:16 en Shorts), aspecto verificado.
- [ ] Todo el texto visible y hablado, en inglés.
- [ ] Casilla de contenido sintético declarada si corresponde.
- [ ] Material generado respaldado en git (no dejarlo solo en Recraft/VideoExpress: borran a ~60 días).

---

## Fuentes

- [YouTube clarifies policies around AI slop and upsetting videos — TechCrunch, 2026-07-20](https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/)
- [YouTube AI Policy 2026: Faceless Creator Compliance Guide — Eliro](https://eliro.pro/blog/youtube-ai-content-policy-faceless-creators-2026)
- [YouTube Monetization with AI Content: What's Allowed and What Gets You Demonetized in 2026 — Miraflow](https://miraflow.ai/blog/youtube-monetization-ai-content-2026-allowed-demonetized)
- [YouTube AI Generated Content Disclosure Policy 2026](https://ytzolo.com/blog/youtube-policy-on-ai-generated-content-disclosure-2026/)
- [How to Find Archival Footage: Historical Video Clips — Coverr](https://coverr.co/blog/where-to-find-archival-footage)
- [Public Domain Content — Documentary Workshop, Ithaca College LibGuides](https://libguides.ithaca.edu/docworkshop/publicdomain)
- [A/V Materials in the Public Domain — NYU Libraries](https://guides.nyu.edu/video/PD-CC)
