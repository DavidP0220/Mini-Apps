# Decisiones de producto — registro vivo

> Mantenido por el agente `higgsfield-product-architect`. **Nunca se borra una decisión vieja.**
> Si una decisión cambia, se añade una entrada nueva que referencia y explica el cambio — el
> historial completo queda como evidencia de por qué se llegó a donde se llegó.

## Formato de cada entrada

```
### AAAA-MM-DD — <título corto de la decisión>
**Decisión:** qué se decidió, en una frase.
**Razón:** por qué, con datos/fuente de los documentos 01-05.
**Alternativas consideradas y descartadas:** cuáles y por qué no.
**Reversible:** sí/no — y qué costaría revertirla si hace falta.
```

---

### 2026-08-25 — Arranque del proyecto de investigación

**Decisión:** crear esta base de conocimiento persistente y el equipo de 3 agentes especializados
(`higgsfield-market-intel`, `higgsfield-tech-scout`, `higgsfield-product-architect`) antes de tomar
ninguna decisión de producto real.

**Razón:** el usuario pidió revisar toda la información disponible (informe `informe_higgsfield.pdf`)
y montar un sistema que investigue, analice y documente de forma permanente para no perder contexto
ni repetir errores, antes de comprometer tiempo o dinero en construir nada.

**Alternativas consideradas y descartadas:** dejar la investigación solo en el PDF de Downloads (se
pierde, no se actualiza, nadie más que David puede leerlo) — descartado porque el objetivo explícito
era "que no se borre nunca" y que los agentes puedan seguir alimentándolo.

**Reversible:** sí, sin costo — son solo documentos de markdown en git.

---

### 2026-08-26 — D-001: Nicho definitivo — mindset/motivación, con Mindset Mechanics como grupo de prueba

**Decisión:** el producto se llama y se posiciona como herramienta de video IA **para creadores de
contenido de mindset / motivación / desarrollo personal** (faceless). El primer grupo de prueba son
seguidores del canal Mindset Mechanics, no público frío.

**Razón:** `01_COMPETENCIA_HIGGSFIELD.md` (verificado 2026-08-25) confirma tres cosas: (a) Higgsfield
vale $5,400M con $700M ARR y 30M usuarios — competirle de frente es inviable; (b) Higgsfield se está
moviendo **hacia arriba** (equipos, agencias, Cinema Studio, Higgsfield Assist), dejando el hueco del
creador individual de bajo presupuesto más abierto, no menos; (c) **no existe hoy ningún competidor
que combine calidad multi-modelo con posicionamiento de marca en mindset** — solo herramientas
genéricas de entrada (InVideo, Reelsta, Mootion, Bigmotion). Además el nicho tiene RPM $4–$12 y
monetiza fuerte por afiliados, o sea que sus creadores ya tienen dinero y motivo para pagar herramientas.

**Alternativas consideradas y descartadas:**
- Herramienta generalista tipo "Higgsfield más barato" — descartada: sin nicho no hay razón para que
  nadie nos elija sobre un producto con $400M de financiamiento.
- Nicho historia/documental (canal Human Chronicles) — descartado por ahora: la audiencia cautiva
  disponible y madura es la de Mindset Mechanics; abrir dos nichos a la vez diluye el MVP. Se
  reevalúa si el Nivel 1 valida.
- Público frío pagado desde el día uno — descartado: `05` marca el Nivel 1 como validación barata;
  meter marketing pagado antes de validar quema presupuesto sin señal.

**Reversible:** sí, barato. El nicho vive en copy, landing y presets, no en la arquitectura. Cambiarlo
cuesta días de contenido, no reconstruir el producto.

---

### 2026-08-26 — D-002: Ruta técnica — Lovable.dev (Ruta B), con Bubble descartado para el MVP

**Decisión:** el MVP se construye en **Lovable.dev** (frontend + backend Supabase generado por prompt),
con el patrón obligatorio **Edge Function + webhook/callback** para las generaciones largas. Bubble
(Ruta A) queda explícitamente fuera del Nivel 1 y solo se reconsidera si Lovable falla la prueba de
colas (ver D-006).

**Razón:** `03_PLATAFORMAS_NOCODE.md` (2026-08-25): Lovable es la ruta de menor dificultad para alguien
no técnico, cuesta ~$25/mes, tiene Stripe nativo y — el punto decisivo — **genera código React/TypeScript
real sincronizado a GitHub sobre Supabase, sin lock-in**, mientras Bubble no permite exportar código
y encierra el producto en su plataforma. Si esto falla, con Lovable nos llevamos el código; con Bubble
nos quedamos sin nada.

**Alternativas consideradas y descartadas:**
- **Bubble (Ruta A):** más probado para SaaS, pero curva de 3-6 semanas, más caro, y su API Connector
  tiene el **mismo** problema de timeout de 30-60 seg — o sea que no evita el trabajo de webhooks,
  solo lo hace más caro y con lock-in. Se reconsidera en Nivel 2 si hay tracción.
- **Base44 (Wix):** confirmado que sí soporta suscripciones recurrentes nativas y tiene tracción real
  (ARR $100M → $150M entre marzo y mayo 2026), pero quedan sin verificar tasas exactas, multi-moneda y
  límites de payout, y es lock-in de Wix. Se queda como **plan B de plataforma**, no como elección.
- **White-label (Ruta C):** ~$500/mes de retainer y el rebranding completo casi siempre exige contrato
  Enterprise — caro y "no es tuyo". Descartada.
- **Softr / Glide / Adalo:** descartadas por el documento 03 como la herramienta equivocada — no manejan
  colas de varios minutos, y Softr Business cuesta $269/mes.

**Reversible:** sí, con costo medio. Como Lovable exporta código a GitHub, migrar a hosting propio es
viable; migrar a Bubble sería empezar de cero (2-4 semanas).

---

### 2026-08-26 — D-003: Motor de IA — fal.ai como agregador único, con abstracción anti-lock-in obligatoria

**Decisión:** **fal.ai** es el proveedor único de generación del MVP (video: Kling y MiniMax; imagen:
Flux). Todas las llamadas pasan por **una sola capa/función interna del backend** (`generarVideo()`),
nunca dispersas por la app, para poder cambiar de proveedor sin rehacer el producto.

**Razón:** `02_PROVEEDORES_IA_APIS.md` (2026-08-25): fal.ai cobra por segundo de GPU sin margen añadido,
es 30-50% más barato que Replicate, y cubre Kling, MiniMax, Flux, Wan, Veo y Seedream con **una sola
API key** — una integración en vez de cinco. La cláusula de "no exponer la API directamente a end users"
(sección 4(b)(ii) de sus ToS) **coincide exactamente** con la arquitectura que ya íbamos a construir,
así que no es un obstáculo. La obligación de abstraer viene del precedente Sora 2: su API cierra el
24-sep-2026 sin sucesor oficial, y quien la tenía cableada directo se quedó roto.

**Alternativas consideradas y descartadas:**
- **Runway directo:** legalmente viable con plan API estándar (corrección del doc 04), pero obliga a
  mostrar "Powered by Runway" con link a runway.com — regalar la marca al competidor desde el logo del
  producto. Descartado para el MVP; disponible como motor premium en Nivel 2.
- **Replicate:** catálogo enorme pero cobra con margen sobre fal.ai. Descartado por costo.
- **Sora 2 / OpenAI:** **prohibido usarlo** — API cierra el 24-sep-2026. Es un requisito, no una opción.
- **Midjourney:** sin API oficial en 2026, riesgo de baneo vía terceros. Descartado.
- **Suno / Udio (música):** sin API pública self-serve; Suno solo abrió intake curado de partners el
  1-jul-2026. **El MVP se lanza sin generación de música**; se usa librería de audio licenciado.
- **ElevenLabs (voz) en el MVP:** aplazado a Nivel 2 — añade $299/mes de plan Scale y todo el problema
  de consentimiento de voz clonada antes de haber validado que alguien paga.

**Reversible:** sí, barato **si y solo si** se respeta la capa de abstracción. Sin ella, es caro.

---

### 2026-08-26 — D-004: Pagos — Stripe, y ningún cobro real antes de la prueba cerrada

**Decisión:** **Stripe** vía la integración nativa de Lovable, configurado en **modo Test** durante
toda la construcción. El modo Live no se activa hasta que David lo apruebe explícitamente en el chat.

**Razón:** `03` confirma Stripe nativo en Lovable (suscripciones, portal de cliente, pagos únicos), y
`05` ya presupuesta su comisión (~2.9% + $0.30). Es el estándar del sector y el camino de menor fricción.

**Alternativas consideradas y descartadas:**
- **Base44 Payments (Wix):** viable pero con dudas operativas abiertas (tasas exactas, multi-moneda,
  payouts) según doc 03, y atado a la plataforma que ya descartamos en D-002.
- **Cobro manual (PayPal/transferencia) en la prueba cerrada:** descartado — no mide de verdad si la
  gente paga con fricción real de tarjeta, que es justo lo que el Nivel 1 debe validar.

**Reversible:** sí, sin costo mientras esté en modo Test.

---

### 2026-08-26 — D-005: Modelo de precios — créditos prepagados, no suscripción, en el MVP

**Decisión:** el MVP vende **paquetes de créditos prepagados** con margen mínimo **3x sobre el costo
real de generación**. Los créditos **no expiran**. Precio de lanzamiento propuesto (a confirmar con
el costo real medido en la Fase 2): paquete de prueba ~$9 y paquete estándar ~$29. No hay suscripción
mensual todavía.

**Razón:** con costo fal.ai de $0.02-$0.40 por output (doc 02), el riesgo del modelo suscripción es
que un usuario intensivo consuma más de lo que paga y cada venta genere pérdida. Con prepago, el
ingreso entra antes del costo y nunca se puede perder dinero por usuario. Sobre "no expiran": el doc 01
documenta que a Higgsfield **los créditos no usados le expiran al fin del ciclo**, lo que "efectivamente
duplica el costo real" — es una queja concreta del mercado y es nuestra diferenciación más barata de
implementar.

**Alternativas consideradas y descartadas:**
- **Suscripción mensual estilo Higgsfield ($19-$129):** descartada en el MVP por riesgo de margen
  negativo y porque exige demostrar valor recurrente que aún no tenemos. Se reevalúa en Nivel 2.
- **Gratis con límite (freemium):** descartado — regala créditos de GPU reales y no valida lo único
  que el Nivel 1 debe validar: que alguien saque la tarjeta.

**Reversible:** sí. Cambiar precios es trivial; lo caro sería quitar el "los créditos no expiran"
después de haberlo prometido — por eso queda registrado como promesa de marca, no como parámetro suelto.

---

### 2026-08-26 — D-006: Prueba de humo de colas largas ANTES de comprometer la Ruta B (decisión de secuencia)

**Decisión:** antes de construir nada del producto ni de conectar Stripe, el primer entregable es un
**prototipo mínimo desechable** en Lovable que genere un solo video vía fal.ai con patrón
webhook/callback y sobreviva a una espera de 3+ minutos. Si falla y no se resuelve en **5 días
hábiles**, se reabre D-002 y se evalúa Bubble o Base44.

**Razón:** es el único riesgo que la investigación dejó **explícitamente sin resolver**: el doc 03 dice
literal que auditar cómo maneja Lovable/Supabase colas de IA de varios minutos "es información que solo
se obtiene construyendo un prototipo real" y lo llama "el punto más débil sin verificar de toda la
investigación no-code". Si ese punto falla, toda la Ruta B se cae — así que se prueba primero, cuando
cuesta $25, no en la semana 4 cuando ya hay usuarios esperando.

**Alternativas consideradas y descartadas:**
- Construir el producto completo y probar las colas al final — descartado: es exactamente cómo se
  desperdicia un mes de trabajo sobre un supuesto no verificado.
- Seguir investigando en la web antes de construir — descartado: `higgsfield-tech-scout` ya lo intentó
  el 2026-08-25 y no existe documentación pública. Esto solo se responde construyendo.

**Reversible:** sí — el prototipo es desechable por diseño.

---

*(Próximas decisiones pendientes de datos: precio final exacto de los paquetes de créditos, que depende
del costo real medido en la Fase 2; y proveedor de voz, que se decide en Nivel 2.)*
