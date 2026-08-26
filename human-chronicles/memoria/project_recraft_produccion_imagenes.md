---
name: project-recraft-produccion-imagenes
description: Recraft AI reemplaza a VideoExpress para generar las imágenes del personaje — VideoExpress queda solo para animar
metadata: 
  node_type: memory
  type: project
  originSessionId: 7c314928-c713-440b-b468-8bb93948d97b
  modified: 2026-08-23T20:20:51.240Z
---

Tras varios intentos fallidos de lograr consistencia del personaje de Mindset Mechanics con VideoExpress (tanto con Técnica B de solo texto como con la función "Consistent Character" e imagen de referencia real), se probó Recraft AI (recraft.ai, plan gratuito) el 2026-08-23 y **funcionó**: subiendo la imagen de referencia `true_character_ref` y pidiendo una escena nueva describiendo también el estilo (flat 2D cel-shaded vector, bold black outlines, no visible ears, no nose), el resultado fue casi idéntico al personaje real ya publicado. Confirmado visualmente por David ("ahora sí se parece").

**Nuevo flujo de producción de imágenes (reemplaza al anterior):**
1. Recraft AI genera cada imagen de escena a partir de la referencia del personaje.
2. Se exporta en PNG 300 DPI.
3. VideoExpress se usa solo para animar esas imágenes ya correctas (Image to Video / First Frame-Last Frame) — nunca para generar la imagen base del personaje.

**Why:** VideoExpress reinterpreta el estilo sin importar la técnica usada (fotorrealista con "Image Type: Human", anime con "Image Type: 2D"). Recraft está especializado en vector plano y sí respeta la referencia.

**How to apply:** Cualquier trabajo futuro de generación de escenas para Mindset Mechanics (incluida la pendiente regeneración de "Resiliencia" y de la miniatura de "Discipline") debe usar este flujo, no el anterior basado solo en VideoExpress. Detalle técnico completo y plantilla de prompt en `PROYECTO MECHANICS OPTIMIZACIONES/ESTILO_MINDSET_MECHANICS.md` (sección añadida el 2026-08-23, al inicio del documento, más §9 pendientes y §10 respaldo). Ver también [[project-mindset-mechanics-scope]].

**Límite real del plan gratuito (corrección, 2026-08-23):** no son "50 créditos diarios" genéricos — el plan gratuito solo da **2 generaciones/día con referencia de personaje**, usando el modelo **"Nano Banana"** (el único que respeta bien `true_character_ref`). David está pasando al **plan Basic (12 USD/mes facturación mensual)** para no depender de ese límite — cuidado con el precio de "10 USD/mes" que Recraft anuncia, ese solo aplica pagando anual.

**Alternativa gratuita de respaldo investigada (no adoptada aún):** Stable Diffusion / ComfyUI, ya instalado localmente en `C:\Users\David Peñuela\Documents\CLAUDE AUTOMATIC\ComfyUI` (GPU RTX 3050, 4GB VRAM). Requeriría IPAdapter + ControlNet + LoRA de personaje para igualar la consistencia que Recraft da de fábrica — configuración no trivial. Se decidió no usarla ahora por prioridad de velocidad; queda como plan B si el límite/costo de Recraft se vuelve un problema.
