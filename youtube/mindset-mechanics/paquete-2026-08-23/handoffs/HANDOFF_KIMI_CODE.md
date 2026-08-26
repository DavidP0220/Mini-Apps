# Bloque de Resumen de Handoff — Mindset Mechanics
**De: Claude Code (ejecución técnica local) → Para: Kimi Code (estrategia)**
**Fecha: 2026-08-23**

---

## 1. Estado técnico actual

**Documentos de investigación sintetizados (nuevos, en `Documents\CLAUDE AUTOMATIC\PROYECTO MECHANICS OPTIMIZACIONES\`):**
- `PLAYBOOK_MONETIZACION.md` — síntesis accionable de 12 canales del nicho ya monetizados (fórmulas de título, hooks, retención, CTA, miniaturas, cadencia, matemática exacta de la meta de 1.000 subs).
- `MANUAL_PRODUCCION.md` — síntesis de 9 documentos oficiales de VideoExpress.ai (método de Consistent Character, patrón Image Prompt + Video Action Prompt, vocabulario de cámara, corrección sobre `First Frame/Last Frame` que no está documentado en ningún tutorial oficial).
- `RESILIENCE_SCENE_PLAN.md` (v2) — plan de 12 escenas para regenerar el video de Resiliencia, con timestamps reales medidos por `ffprobe` (audio ya grabado = 553.4s exactos), no estimados.

**Código depurado en `video_express_ai\video_express_bot.py`** (bot Playwright que automatiza VideoExpress.ai), 3 bugs reales encontrados y corregidos hoy en producción real, no en teoría:
1. Selector ambiguo `get_by_text("My AI Videos", exact=True)` resolvía a 2 elementos DOM (nav + título de panel) → causaba `strict mode violation`. Corregido con selector por clase CSS específica (`.library-panel-category-title`).
2. El bucle de polling de renderizado podía agotar sus reintentos y caer en un `.click()` a ciegas sobre un elemento no visible, comiéndose un timeout de 60s sin diagnóstico. Corregido: ahora hace `continue` a la siguiente vuelta del polling en vez de forzar el click.
3. Se agregó logging de `status`/`mediaPath`/`id` en cada vuelta del polling — antes el fallo por timeout de 900s no daba ninguna pista de si el render seguía "pending" o si el problema era de lectura de la API.

**Estado de la prueba en curso:** generación real de la escena 1 de Resiliencia (imagen + clip con movimiento de cámara) corriendo contra el sitio real. Ya pasó generación de imagen y arranque de video sin error; se está verificando si el paso de polling final (esperar a que el render aparezca "completed" en la Media Library) ahora sí reporta bien el estado o si el render legítimamente tarda más de 15 minutos.

---

## 2. Puntos críticos pendientes (nivel código, ya acotados)

- **`mark_consistent_character()` / comando `mark-character`:** técnica A de consistencia de personaje (subir foto de referencia + botón "Consistent Character") sigue fallando — el botón queda `disabled` incluso con foto de referencia + prompt de imagen llenos. Hipótesis más probable, documentada en `MANUAL_PRODUCCION.md` §2: el botón (ícono "+", clase `button-consistent-character-auto`) puede requerir que la imagen ya haya sido GENERADA por la app (no subida a mano) antes de habilitarse. **No bloquea producción** — la Técnica B (repetir la ficha de personaje textual en cada prompt) ya está validada y es la que se está usando en el lote actual.
- **`import_local_image()`:** aún no implementada (pendiente copiar el patrón de `import_local_audio()` cambiando la carpeta destino de "Audio" a "Images").
- **Polling de render:** posible que 900s (15 min) sea insuficiente para clips con movimiento de cámara complejo — a confirmar con el log nuevo antes de decidir si subir el timeout o si hay un bug de lectura de la API `get_media`.
- **Un short del canal ya estaba mal etiquetado** (`06_predator_douglas_mawson.mp4` cubría el tramo equivocado del video fuente) — corregido en sesión anterior, mencionado aquí solo como antecedente de calidad de QA necesaria en este pipeline.

---

## 3. Propuesta para la siguiente fase (decisiones para Kimi)

1. **Con el playbook y el manual ya escritos, la decisión estratégica pendiente es de secuenciación**, no de investigación: ¿se prioriza (a) terminar de regenerar el video de Resiliencia con el estilo correcto, (b) lanzar ya el primer guion nuevo con la fórmula de título validada (`Why Didn't Evolution Remove Social Anxiety?`), o (c) subir primero los 5 Shorts ya listos para no dejarlos parados? El dato duro del playbook dice que los Shorts no convierten en este nicho — Kimi debería decidir si eso justifica bajarlos de prioridad frente a (a)/(b).
2. **Definir el presupuesto de iteración del pipeline de VideoExpress**: cada escena de Resiliencia es una generación real con costo en créditos y tiempo (~5-15 min por escena). Kimi debería fijar cuántas escenas se lanzan en el próximo bloque antes de una revisión de calidad intermedia (el plan actual recomienda 1 a 1 para la primera tanda).
3. **Con la matemática de la meta ya resuelta** (playbook §7: el cuello de botella son los 1.000 subs, no las 4.000 horas; ~36-37k vistas adicionales de largos cierran la meta a la tasa de conversión actual), la decisión de fondo para Kimi es de **cadencia de publicación**: el dataset dice que ningún canal que rompió publicó menos de 1 video cada 4-5 días. Definir si el pipeline actual (con generación escena por escena vía Playwright) puede sostener esa cadencia o si hace falta paralelizar/acelerar antes de comprometerse a esa frecuencia públicamente.
