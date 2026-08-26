# Presupuesto y cronograma

> Mantenido por el agente `higgsfield-product-architect`. Última actualización: 2026-08-26
> (roadmap ejecutable del Nivel 1 añadido en "Estado real de ejecución"). Base original: 2026-08-25
> (fuente: `informe_higgsfield.pdf`). Los tres niveles asumen que NO se programa y que se usan
> plataformas no-code + APIs de terceros. Los costos de "créditos de IA" son variables y dependen
> del volumen real de generación — las cifras son para un número moderado de usuarios activos.

## Nivel 1 — Validación / MVP interno

| Concepto | Costo estimado |
|---|---|
| Plataforma (Lovable o Base44) | $25-$50/mes |
| Motor de IA (fal.ai, uso moderado) | $50-$150/mes |
| Dominio + hosting básico | $15-$30/mes |
| Stripe (comisiones por transacción) | ~2.9% + $0.30 por cobro |
| **TOTAL MENSUAL ESTIMADO** | **$90-$230/mes** |
| Tiempo estimado de construcción | 2 a 4 semanas |

## Nivel 2 — Producto vendible a un grupo cerrado (tu audiencia)

| Concepto | Costo estimado |
|---|---|
| Plataforma (Bubble, plan pago) | $32-$134/mes |
| Motor de IA (fal.ai + ElevenLabs, uso medio-alto) | $300-$800/mes |
| Google Veo 3.1 (tier premium opcional) | $100-$400/mes según uso |
| Automatización (n8n, self-host o cloud) | $0-$50/mes |
| Marketing/lanzamiento inicial | $200-$500 (una vez) |
| **TOTAL MENSUAL ESTIMADO** | **$450-$1,400/mes** |
| Tiempo estimado de construcción | 6 a 10 semanas |

## Nivel 3 — Producto SaaS público, escalable, con equipo Enterprise

| Concepto | Costo estimado |
|---|---|
| Plataforma (Bubble Enterprise / infraestructura propia) | $500-$2,000/mes |
| Motor de IA (planes Enterprise con SLA e indemnización) | $2,000-$8,000+/mes según volumen |
| Soporte legal (revisión de contratos con proveedores) | $500-$2,000 (una vez o recurrente) |
| Equipo (freelancer dev de apoyo + soporte a clientes) | $1,500-$4,000/mes |
| **TOTAL MENSUAL ESTIMADO** | **$4,500-$16,000+/mes** |
| Tiempo estimado de construcción | 3 a 6 meses |

**Recomendación de secuencia:** empezar en Nivel 1 con la propia audiencia como grupo de prueba
(costo y riesgo mínimos), y solo escalar a Nivel 2 o 3 cuando el Nivel 1 muestre que la gente
realmente paga y usa el producto de forma recurrente.

## Cronograma sugerido (ruta recomendada: B, escalando a A)

| Semana | Actividad | Entregable |
|---|---|---|
| 1 | Definir nicho exacto, elegir plataforma (Lovable/Base44) y motor de IA (fal.ai) | Alcance y stack definidos |
| 2-3 | Configurar cuenta, diseñar interfaz básica, conectar API de IA, probar generación | Prototipo funcional |
| 4 | Integrar Stripe, definir precios propios, revisar términos de reventa con proveedores | Sistema de pagos activo |
| 5-6 | Prueba cerrada con 10-30 usuarios de la propia audiencia, recoger feedback | MVP validado |
| 7-8 | Ajustes según feedback, lanzamiento público limitado, primeras campañas en redes propias | Lanzamiento Nivel 1 |
| Mes 3+ | Si hay tracción: migrar/ampliar a Bubble (Nivel 2), sumar Veo 3.1 premium, automatizar con n8n | Escalamiento a Nivel 2 |

Tiempo total hasta tener un producto vendible funcionando: 6-10 semanas para el Nivel 1-2. El
Nivel 3 es un horizonte de 3-6 meses adicionales, y solo tiene sentido si el negocio ya genera
ingresos recurrentes estables.

## Estado real de ejecución (vive aquí, se actualiza en cada avance)

### Situación al 2026-08-26

- **Fase actual:** salida de investigación → entrada a Nivel 1 (MVP). Luz verde de David el 2026-08-26.
- **Decisiones tomadas:** D-001 a D-006 en [`06_DECISIONES_PRODUCTO.md`](06_DECISIONES_PRODUCTO.md)
  (nicho, Lovable, fal.ai, Stripe, créditos prepagados, prueba de colas primero).
- **Dinero real comprometido hasta hoy: $0.00.** Ninguna cuenta de pago activada.
- **Código escrito hasta hoy:** ninguno.
- **Bloqueante activo:** el riesgo de colas largas de la Fase 2 — hasta resolverlo, ninguna decisión
  posterior es firme.

### Regla de gasto de este proyecto (no negociable)

Ningún agente activa una suscripción, mete una tarjeta ni pasa Stripe a modo Live. Cada paso marcado
con **[GASTO — requiere OK de David]** se detiene hasta que David lo apruebe por escrito en el chat.
Todo gasto aprobado se anota abajo en el "Registro de gasto real" con fecha e importe.

---

## Roadmap Nivel 1 paso a paso (escrito para alguien no técnico)

> Cómo leerlo: cada paso dice **en qué web entrar, qué botón apretar y qué escribir**. Si un paso no
> sale como está descrito, no improvises: anótalo y se documenta en `07_ERRORES_Y_LECCIONES.md`.
> Las cajas de texto que empiezan con "Prompt para Lovable:" se copian y pegan **tal cual**.

### FASE 0 — Preparativos gratis (día 1, ~1 hora, $0)

**Paso 0.1 — Correo dedicado del proyecto.**
Entra a gmail.com → "Crear cuenta". Usa un correo **nuevo y exclusivo** de este producto (ejemplo:
`hola@…` o un gmail tipo `mindsetstudio.ai@gmail.com`). No uses el correo personal ni el del canal.
Motivo: si mañana el producto se vende o se le da acceso a alguien más, se entrega el correo y ya —
no hay que desenredar cuentas mezcladas.

**Paso 0.2 — Gestor de contraseñas.**
Entra a bitwarden.com → "Get started" → plan **Free**. Guarda ahí la contraseña del correo nuevo.
Todas las claves de API que aparezcan más adelante se guardan aquí, **nunca en un archivo de texto,
nunca en un chat, nunca en el escritorio**. Una API key filtrada = alguien gastando tu dinero de GPU.

**Paso 0.3 — Cuenta de GitHub (gratis).**
Entra a github.com → "Sign up" con el correo del Paso 0.1. No hay que saber usarlo; sirve para que
Lovable guarde ahí una copia del código (esa copia es lo que nos protege del lock-in, ver D-002).

**Paso 0.4 — Nombre y dominio: solo investigar, NO comprar todavía.**
Entra a namecheap.com y busca 3 nombres candidatos. El dominio se compra en la Fase 5, cuando ya
sepamos que el producto funciona. Comprar dominio antes de validar es el gasto más común y más inútil.

**Entregable Fase 0:** correo, Bitwarden y GitHub creados. 3 nombres candidatos anotados. **Costo: $0.**

---

### FASE 1 — Alta de cuentas de las herramientas (día 2, ~1 hora)

**Paso 1.1 — Cuenta de fal.ai. [GASTO — requiere OK de David]**
Entra a fal.ai → "Sign up" con el correo del Paso 0.1 → menú **Billing** → cargar saldo inicial de
**$20** (no una suscripción mensual; fal.ai es prepago por uso). Luego menú **API Keys** → "Add key"
→ nómbrala `mvp-test` → copia la clave y **guárdala en Bitwarden inmediatamente** (solo se muestra una vez).
- Por qué $20 y no más: según doc 02, cada generación cuesta $0.02-$0.40. Con $20 hay para
  ~50-100 pruebas, de sobra para la Fase 2. Si se acaba, se recarga; nunca al revés.

**Paso 1.2 — Cuenta de Lovable.dev.**
Entra a lovable.dev → "Sign up" **con el botón de GitHub** (así queda enlazado desde el inicio).
**Empieza en el plan gratuito.** No pagues el plan de $25/mes todavía: el plan free da créditos de
prompt suficientes para intentar la prueba de la Fase 2. Solo si se acaban se pasa al de pago, y eso
es **[GASTO — requiere OK de David]**.

**Paso 1.3 — Cuenta de Stripe (sin activar cobros).**
Entra a stripe.com → "Start now" → crea la cuenta con el correo del Paso 0.1. **NO completes la
verificación de identidad ni conectes cuenta bancaria todavía.** Quédate en **modo Test** (el
interruptor "Test mode" arriba a la derecha, que debe verse encendido). En modo Test, Stripe simula
pagos con tarjetas falsas y no mueve un centavo real. Esto es D-004.

**Entregable Fase 1:** 3 cuentas creadas, API key de fal.ai en Bitwarden.
**Costo real: $20 de saldo prepago en fal.ai (único gasto de esta fase).**

---

### FASE 2 — LA PRUEBA QUE DECIDE TODO: colas largas (días 3-7)

> Esta es la fase más importante del proyecto y ejecuta la decisión D-006. Estamos probando **una
> sola cosa**: si Lovable/Supabase aguanta que una generación de video tarde 3+ minutos sin romperse.
> El doc 03 dice que nadie lo ha documentado públicamente. Aquí lo averiguamos por $20.

**Paso 2.1 — Crear el proyecto en Lovable.**
En lovable.dev, en la caja grande de texto de la pantalla de inicio, pega **exactamente** esto:

> **Prompt para Lovable:** "Create a minimal web app with a single page. The page has one text input
> for a prompt and one button labeled 'Generate video'. When clicked, it calls a Supabase Edge
> Function that submits the prompt to the fal.ai queue API (model fal-ai/kling-video) using the
> webhook/callback pattern — do NOT wait synchronously for the result. Store each job in a Supabase
> table `jobs` with columns: id, prompt, status (queued/processing/done/failed), request_id,
> video_url, created_at, updated_at. Create a second Edge Function that receives the fal.ai webhook
> and updates the job row. The front page must subscribe to Supabase realtime and show the job status
> live, then display the finished video. Store the fal.ai API key as a Supabase secret, never in the
> frontend code."

**Paso 2.2 — Guardar la clave de fal.ai como secreto.**
Lovable te pedirá conectar Supabase (botón "Connect Supabase" arriba a la derecha) y luego te pedirá
la API key. Pégala **solo** cuando te la pida como "secret"/"environment variable". Si en algún
momento ves tu API key escrita dentro del código de la página visible, **detente** — eso significa
que quedó expuesta a cualquier visitante; hay que decirle a Lovable: "Move the fal.ai API key out of
the frontend into a Supabase secret."

**Paso 2.3 — La prueba en sí.**
Aprieta el botón "Generate video" con un prompt cualquiera (ej. "a man running at sunrise, cinematic")
y **cronometra**. Anota, literalmente, en un archivo de notas:
1. ¿Cuántos segundos/minutos tardó?
2. ¿La pantalla siguió mostrando el estado o se quedó colgada / dio error de timeout?
3. Si cierras la pestaña a la mitad y la vuelves a abrir, ¿el video aparece igual cuando termina?
   (Esta es **la pregunta clave**: si el trabajo sobrevive a cerrar la pestaña, la arquitectura es
   correcta. Si no, está esperando de forma síncrona y hay que corregirlo.)
4. ¿Cuánto saldo consumió en fal.ai? (menú Billing) → **este número alimenta D-005**, es el costo
   real sobre el que se calcula el margen 3x.

**Paso 2.4 — Manejo de errores desde el primer día (lección heredada #2 del doc 07).**
Pídele a Lovable, en un segundo prompt:

> **Prompt para Lovable:** "Add retry logic to the fal.ai Edge Function: on HTTP 429, retry with
> exponential backoff honoring the Retry-After header. On 5xx errors, do NOT retry — mark the job as
> failed instead, because the provider may have already executed and charged the generation. Log
> every job attempt to the jobs table even if the status check call fails."

Esto no es opcional ni "una mejora para después": el doc 07 documenta que reintentar un 5xx **cobra
la generación dos veces**. Con usuarios reales pagando, eso es un problema de facturación, no un bug.

**CRITERIO DE DECISIÓN (esto es un semáforo, no una opinión):**
- **VERDE** — el video llega, la pantalla no se cuelga y el trabajo sobrevive a cerrar la pestaña →
  la Ruta B queda confirmada, se sigue a Fase 3.
- **ROJO** — no se logra en **5 días hábiles** → se reabre D-002. Se prueba Base44 con el mismo
  experimento antes de considerar Bubble (Bubble tiene el mismo timeout de 30-60 seg y además
  lock-in, según doc 03). Se documenta el fallo completo en `07_ERRORES_Y_LECCIONES.md`.

**Entregable Fase 2:** un video generado de verdad, el costo real por generación medido, y semáforo
verde o rojo sobre la Ruta B. **Costo adicional: $0** (usa el saldo de la Fase 1).

---

### FASE 3 — El producto de verdad (semanas 2-3)

Solo se entra aquí con semáforo VERDE.

**Paso 3.1 — Tirar el prototipo y empezar limpio.** El de la Fase 2 era desechable por diseño; su
valor era la respuesta, no el código.

**Paso 3.2 — Construir la app con 3 pantallas.** Nuevo proyecto en Lovable:

> **Prompt para Lovable:** "Build a web app for creators of mindset/motivation faceless content.
> Three pages: (1) Sign up / log in with email, using Supabase Auth. (2) A generator page where the
> user picks one of 6 preset styles, writes a short motivational line, and clicks Generate; it uses
> the queue + webhook pattern with fal.ai and shows live status. (3) A library page listing all the
> user's past generations with download buttons. Each user row has a `credits` integer column;
> generating costs credits and the button is disabled at zero credits. All fal.ai calls must go
> through a single shared backend function called `generateVideo` so the provider can be swapped
> later without touching the rest of the app. Never expose the fal.ai API key to the browser."

La frase "a single shared backend function called `generateVideo`" ejecuta la capa de abstracción de
D-003 — es la póliza de seguro contra un cierre de API tipo Sora 2. Si Lovable dispersa las llamadas,
insiste hasta que estén centralizadas.

**Paso 3.3 — Los 6 presets del nicho (esto es el producto, no un detalle).**
Esta es la razón por la que alguien nos elegiría sobre InVideo. Los 6 presets de mindset se definen
con el equipo de contenido del canal (`storyboard-director` conoce qué funciona visualmente en este
nicho) y deben ser resultados de un clic, no una caja de prompt vacía. Sugerencia de partida:
"Amanecer / disciplina", "Gimnasio 4am", "Ciudad de noche / soledad", "Naturaleza / calma",
"Éxito / oficina", "Superación / lluvia".

**Paso 3.4 — Verificación de seguridad antes de dejar entrar a nadie.**

> **Prompt para Lovable:** "Audit this app for security: confirm Row Level Security is enabled on
> every Supabase table so a user can only read their own rows, confirm no API keys are present in the
> frontend bundle, and confirm credits can only be decremented server-side, never from the browser."

Sin esto, un usuario podría darse créditos infinitos desde el navegador y gastar tu saldo de fal.ai.

**Entregable Fase 3:** app funcionando con login, presets y créditos. **Costo posible: plan Lovable
$25/mes si se acaban los créditos gratis — [GASTO — requiere OK de David].**

---

### FASE 4 — Pagos y textos legales (semana 4)

**Paso 4.1 — Stripe en modo Test.** En Lovable: "Add Stripe checkout to buy credit packs: 100 credits
and 400 credits. Use Stripe test mode." Compra tú mismo con la tarjeta de prueba de Stripe
`4242 4242 4242 4242` (cualquier fecha futura, cualquier CVC) y verifica que los créditos aparecen
en la cuenta. **Ningún dinero real se mueve en este paso.**

**Paso 4.2 — Fijar los precios con el costo real.** Toma el costo medido en el Paso 2.3 y aplica el
margen 3x de D-005. Ejemplo: si un video cuesta $0.15, un paquete de 100 créditos (=20 videos, $3.00
de costo) se vende a ~$9. Este número se registra como decisión nueva en `06` antes de cobrar nada.

**Paso 4.3 — Términos de uso y aviso de privacidad. NO OPCIONAL.**
El doc 04 es tajante: **la indemnización frente a reclamos de usuarios finales recae en el proyecto,
no en fal.ai** (sección 17 de sus ToS). Los términos deben decir explícitamente: el usuario es
responsable de lo que genera; prohibido generar imagen o voz de personas reales sin consentimiento;
prohibido contenido ilegal; el servicio se ofrece "tal cual" sin garantía. Redáctalos con Lovable y
**antes de cobrar a un tercero real, pásalos por una consulta legal puntual** (no un retainer) — el
doc 04 lo marca como "ahora más urgente".

**Paso 4.4 — Confirmar que no hay nada de Sora 2 en el producto.** Checklist del doc 04. La API cierra
el 24-sep-2026, o sea **dentro de un mes**.

**Entregable Fase 4:** pagos probados en Test, precios fijados sobre costo real, textos legales listos.

---

### FASE 5 — Prueba cerrada con audiencia real (semanas 5-6)

**Paso 5.1 — Comprar el dominio. [GASTO — requiere OK de David]** Ahora sí, en Namecheap (~$12/año).
Conectarlo desde Lovable → "Settings" → "Domains".

**Paso 5.2 — Activar Stripe en modo Live. [GASTO/INGRESO — requiere OK explícito de David en el chat]**
Completar verificación de identidad y cuenta bancaria en Stripe. **Este es el punto de no retorno del
Nivel 1**: a partir de aquí entra dinero real de terceros y aplican los términos legales del Paso 4.3.

**Paso 5.3 — Reclutar 10-30 personas de Mindset Mechanics.** No abrirlo al público. Coordinar el
mensaje con `community-engagement-manager` (conoce el tono de la marca) y validar cualquier pieza
pública con `publish-readiness-coordinator` antes de publicarla — regla estándar del proyecto.
Ofrecer el paquete de prueba con descuento de fundador a cambio de feedback.

**Paso 5.4 — Vigilar el saldo de fal.ai a diario.** Con usuarios reales el consumo se dispara. Poner
alerta de saldo bajo en fal.ai. Un saldo agotado a mitad de la prueba cerrada mata la prueba.

**Paso 5.5 — Medir solo 3 números:** cuántos compraron (de los invitados), cuántos volvieron a generar
una segunda vez otro día (esto es lo único que predice si hay negocio), y el costo real por usuario
frente a lo que pagó.

**Entregable Fase 5:** MVP validado o refutado con datos reales. **Costo: dominio ~$12 + consumo real
de fal.ai.**

---

### FASE 6 — Decisión de escalar (semanas 7-8)

Con los 3 números de la Fase 5, `higgsfield-product-architect` registra en `06` la decisión de:
seguir en Nivel 1 puliendo, escalar a Nivel 2 ($450-$1,400/mes: Bubble, ElevenLabs, Veo 3.1 premium,
n8n), o parar. **Antes de aprobar Nivel 2 se refresca la investigación** con `higgsfield-market-intel`
y `higgsfield-tech-scout`: para entonces los datos de los docs 01-04 tendrán 6+ semanas y ese es
justo el umbral de re-verificación que exige este proyecto.

---

## Presupuesto real del Nivel 1, fase por fase

| Fase | Concepto | Costo | ¿Requiere OK de David? |
|---|---|---|---|
| 0 | Correo, Bitwarden, GitHub | $0 | No |
| 1 | Saldo prepago fal.ai | $20 (una vez) | **Sí** |
| 1 | Lovable plan free | $0 | No |
| 1 | Stripe modo Test | $0 | No |
| 2 | Prueba de colas | $0 (usa saldo Fase 1) | No |
| 3 | Lovable plan pago (solo si hace falta) | $25/mes | **Sí** |
| 4 | Consulta legal puntual (recomendada) | $100-$300 (una vez) | **Sí** |
| 5 | Dominio | ~$12/año | **Sí** |
| 5 | Stripe modo Live | 2.9% + $0.30 por cobro | **Sí, explícito** |
| 5 | Recarga fal.ai según uso real | $50-$150/mes | **Sí** |

**Compromiso para llegar hasta el semáforo de la Fase 2 (la decisión que más importa): $20.**
**Total Nivel 1 completo en régimen: $90-$230/mes**, coherente con la tabla de arriba.

---

## Registro de gasto real

| Fecha | Concepto | Importe | Aprobado por David |
|---|---|---|---|
| — | *(sin gastos todavía al 2026-08-26)* | $0.00 | — |

## Fuentes

`informe_higgsfield.pdf` (agosto 2026).
