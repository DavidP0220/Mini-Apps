# Producción de imágenes en masa — análisis

**2026-08-27.** Estilo objetivo: cartoon plano tipo *Rick and Morty* — línea negra gruesa e irregular,
color plano sin degradados, ojos ovalados enormes con pupila diminuta, formas simples.

---

## 0. Advertencia legal, primero

**Rick and Morty es propiedad de Adult Swim / Cartoon Network.** Reproducir a Rick o a Morty, o a
personajes derivados reconocibles, expone el canal a reclamo de copyright, retirada de videos y
pérdida de monetización.

**El estilo artístico no es registrable.** Línea gruesa, color plano, ojos ovalados grandes y formas
simples son recursos gráficos de uso libre. Docenas de canales los usan sin problema.

**Regla operativa:** personajes **originales** en un estilo *similar*. Nunca el pelo azul en pico, la
bata de laboratorio, ni la camiseta amarilla de Morty. Y **nunca escribir "Rick and Morty" en el
prompt de producción** — usar la descripción del estilo, no la marca.

---

## 1. Cuánto se necesita de verdad

Antes de comparar precios hay que dimensionar el volumen real. La suposición inicial —cientos de
imágenes al mes— es falsa:

| Necesidad | Volumen mensual | Quién lo cubre |
|---|---|---|
| Escenas de los videos largos | ~400 (8 videos × 50 escenas) | **VideoExpress 3.0**, que ya está pagado y en el pipeline |
| Miniaturas de largos | 8, más iteraciones ≈ **30** | Falta resolver |
| Miniaturas de Shorts | 0 — salen de frames del propio video | — |
| Avatar y banner | Una vez | Falta resolver |

**El volumen real que falta cubrir son ~30-40 imágenes al mes.** No es producción en masa.

Consecuencia: a los precios de 2026, ese volumen cuesta **entre $0,04 y $0,12 al mes**. El costo no es
la variable a optimizar — la **consistencia de estilo** sí lo es.

---

## 2. Comparativa de vías

### A) API de FLUX.1 schnell — recomendada para empezar

| Proveedor | Precio | Nota |
|---|---|---|
| **Pixazo** | **$0,0012 / imagen** | El más barato confirmado |
| **fal.ai** | $0,003 / megapíxel | El más rápido; **soporta LoRA**, que importa para el paso 2 |
| **Together AI** | ~$0,003 / imagen | Sencillo |
| Replicate | Variable | Cómodo, algo más caro |

A 40 imágenes/mes: **$0,05 a $0,12 mensuales**. Con $5 de saldo tienes para años.

- ✅ Sin instalación, sin GPU, funciona desde aquí — **yo genero e itero directamente**
- ✅ FLUX schnell es nítido y hace muy bien el cartoon plano
- ❌ Requiere una API key

### B) HuggingFace Inference — gratis con token

FLUX.1-schnell vía `router.huggingface.co`. Token de tipo *Read*, gratuito.

- ✅ **$0**, y suficiente para 40 imágenes/mes
- ✅ Yo genero directamente desde aquí
- ❌ Cuota gratuita limitada y colas en horas pico
- **Es la vía de arranque: cero costo y cero riesgo**

### C) ComfyUI local en tu PC — la vía definitiva

| Modelo | VRAM mínima | Nota |
|---|---|---|
| SD 1.5 | 4 GB | Insuficiente para calidad |
| **SDXL** | **8-12 GB** | *"El mejor todoterreno de 2026 por su ecosistema de LoRA y ControlNet"* |
| FLUX.1 Dev | 16-24 GB (o 6 GB en GGUF Q4) | Máxima calidad |

- ✅ **$0 por imagen, ilimitado y para siempre**
- ✅ Permite **entrenar un LoRA de estilo** — la única forma de garantizar que las 400 escenas se vean idénticas
- ✅ Control total, sin colas ni cuotas
- ❌ Exige GPU dedicada y una tarde de instalación
- ❌ **Yo no puedo operarlo desde aquí** — corre en tu máquina

### D) Suscripciones (Midjourney, Leonardo, Ideogram)

$10-30 al mes por un volumen que cuesta centavos vía API, y operación manual imagen por imagen.
**Descartadas** para este caso.

---

## 3. El problema real: consistencia, no precio

Con 40 imágenes al mes el costo es irrelevante. Lo que decide si el canal se ve profesional es que
**las 400 escenas del mes se vean del mismo universo**.

Tres niveles, de menor a mayor fiabilidad:

1. **Ficha de estilo repetida verbatim en cada prompt** — es la Técnica B de `MANUAL_PRODUCCION.md`,
   ya validada en vivo en este proyecto. Coste cero. Suficiente para arrancar.
2. **Imagen de referencia** (Consistent Character de VideoExpress, o IPAdapter en ComfyUI).
3. **LoRA de estilo entrenado** — se entrena una vez con 20-40 imágenes coherentes y a partir de ahí
   todo sale idéntico. Requiere la vía C, o fal.ai que sí admite LoRA.

---

## 4. Ficha de estilo — pegar en cada prompt

```
Flat 2D cartoon illustration, adult animation style. Thick uneven hand-drawn
black outlines. Completely flat cel colors, no gradients, no shading, no
texture. Large white oval eyes with tiny black dot pupils. Thin simple
eyebrows. Small simple line mouth. Simple rounded shapes, minimal detail.
Clean crisp vector line art, sharp edges, no blur.
```

Cláusula negativa:

```
No photorealism, no 3D render, no gradients, no soft shading, no blur,
no text, no letters, no words, no watermark, no signature.
```

**Nunca** escribir "Rick and Morty" en un prompt de producción.

---

## 5. Recomendación en tres pasos

1. **Hoy — token gratuito de HuggingFace.** Cero costo, cero riesgo. Con eso genero el personaje
   original, el avatar, el banner y las miniaturas del mes, e itero hasta que quede bien.
2. **Si HuggingFace se queda corto — $5 en fal.ai.** Cubre más de un año a este volumen, y deja la
   puerta abierta al LoRA.
3. **Cuando el canal facture — ComfyUI local con LoRA de estilo.** Es la única vía que garantiza que
   400 escenas mensuales se vean idénticas, a costo cero por imagen.

Las escenas de los videos siguen saliendo de **VideoExpress**, que ya está pagado. Lo único que hay
que cambiar ahí es la ficha de estilo del prompt.
