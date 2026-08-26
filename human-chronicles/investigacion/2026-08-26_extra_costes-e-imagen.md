# EXTRA — Coste real del pipeline y una trampa de licencia en Recraft

**Ronda 01 · 2026-08-26 · no estaba en la lista de 10 huecos, salió buscando y es material**

El objetivo declarado del proyecto incluye **máxima economía**. Dos hallazgos que afectan
directamente al bloqueo 🔴 de "autorización de gasto de créditos".

---

## 1. ⚠️ Trampa: el plan gratuito de Recraft no da derechos comerciales

Recraft tiene un plan gratuito de ~50 créditos/día (≈50 imágenes ráster diarias). Suena a solución
al bloqueo de presupuesto. **No lo es:**

> **En el plan gratuito, las imágenes generadas son públicas y propiedad de Recraft, sin derechos
> comerciales.**

Usar el plan gratuito para el avatar, el banner o cualquier escena del canal significaría publicar
un canal de YouTube monetizado sobre imágenes que no son del canal. **No se hace.** Si se generan
imágenes en Recraft para Human Chronicles, es con la cuenta de pago — que es justo el bloqueo 🔴
del tablero, y ahora se entiende por qué ese bloqueo no tiene atajo.

**Coste de referencia de Recraft de pago:** ~0,010-0,012 $ por imagen ráster (1 crédito);
vectorial/SVG 2 créditos, ~0,02-0,024 $.

## 2. Alternativas con derechos comerciales limpios

| Opción | Coste | Licencia | Nota |
|---|---|---|---|
| **FLUX.1 [schnell] autoalojado** | **0 €** (hardware propio) | Comercial permitido, pesos abiertos | Señalado como el mejor punto de partida abierto para autoalojar |
| FLUX.1 [schnell] vía Replicate | **~0,003 $/imagen** | Comercial | **3-4x más barato que Recraft** |
| Stable Diffusion / FLUX local | 0 € | Pesos abiertos, comercial | Sin cuota por imagen, sin dependencia de proveedor |
| Cloudflare Workers AI | Cuota diaria gratis | Según modelo | Señalada como la mejor API gratuita para desarrolladores |
| Hugging Face ZeroGPU | Gratis con tope | Según modelo | Minutos de GPU al día, cola impredecible. Para pruebas, no para producción |

**Regla de licencia que vale para todo (imagen, voz, mapas):** hay que verificar **dos** cosas, no
una — que la licencia de los pesos del modelo permita uso comercial, **y** que los términos del
proveedor alojado y **de ese plan concreto** también lo permitan. La trampa de Recraft es
exactamente el segundo caso: modelo de pago legítimo, plan gratuito sin derechos.

## 3. Qué significa esto para el canal

El pipeline heredado (Recraft → VideoExpress) es el que está probado y funciona
(`MANUAL_PRODUCCION.md`), y `ERRORES_A_EVITAR.md` avisa de no cambiar cosas probadas a la ligera.
Pero el presupuesto vigente está asignado a Mindset Mechanics y este canal no tiene ni un crédito
autorizado. Las opciones reales son dos, y son de David:

- **A — autorizar un lote pequeño de créditos de Recraft** para el video 1 (gate literal, lote
  cerrado, por `ERRORES_A_EVITAR.md` #1: ni un crédito fuera del lote).
- **B — evaluar FLUX schnell** como motor de imagen de Human Chronicles. 3-4x más barato por
  imagen, o gratis autoalojado, con licencia comercial limpia. Coste de la evaluación: una tarde.

**Argumento a favor de B específicamente para este canal:** Human Chronicles es faceless. La razón
por la que Mindset Mechanics necesita Recraft es la **consistencia de personaje**
(`true_character_ref.jpg`). Aquí eso no aplica — solo hay que mantener un **estilo**
(`ESTILO_HUMAN_CHRONICLES.md` §3.4), que es mucho menos exigente. El canal que menos necesita la
herramienta cara es justo este.

**No es una decisión que tome un agente.** Se le presenta a David con las dos opciones y el número.

## Fuentes

- [Recraft Pricing 2026 — Plans, Cost per Image & Free Tier — Price Per Token](https://pricepertoken.com/recraft-pricing)
- [Recraft's Pricing Update: Credit-Based Subscriptions — Recraft](https://www.recraft.ai/blog/pricing-update)
- [Best Free AI Image Generation APIs & Open-Source Models (2026) — Eden AI](https://www.edenai.co/post/top-free-image-generation-tools-apis-and-open-source-models)
- [Free AI Image Generation API: What's Actually Free in 2026 — APIFrame](https://apiframe.ai/blog/free-ai-image-generation-api-2026)
- [Local AI Image Generation in 2026: Flux, SD & ComfyUI — Digital Applied](https://www.digitalapplied.com/blog/local-image-generation-flux-stable-diffusion-comfyui-2026)
- [Free AI Models for Commercial Use (2026) — AY Automate](https://www.ayautomate.com/blog/free-ai-models-commercial-use)
