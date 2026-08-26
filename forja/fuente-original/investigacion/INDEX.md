# Proyecto: Alternativa propia a Higgsfield.ai

**Qué es esto:** un producto nuevo y separado de la producción de videos de Mindset Mechanics —
una herramienta de IA generativa (video, imagen, música) para creadores, inspirada en Higgsfield.ai
pero enfocada en un nicho propio, no en competir de frente con un jugador de $5,400M de valoración.

**Origen:** `informe_higgsfield.pdf` (agosto 2026), producido con 3 agentes de investigación +
3 validadores independientes. Su contenido fue volcado a los documentos de esta carpeta el
2026-08-25 para que deje de vivir solo en un PDF de Downloads y pase a ser conocimiento vivo,
versionado en git, que nunca se pierde y que los agentes especializados pueden seguir alimentando.

## Cómo está organizado (leer en este orden)

1. [`01_COMPETENCIA_HIGGSFIELD.md`](01_COMPETENCIA_HIGGSFIELD.md) — quién es Higgsfield.ai hoy: producto,
   precios, financiamiento, por qué no competirle de frente.
2. [`02_PROVEEDORES_IA_APIS.md`](02_PROVEEDORES_IA_APIS.md) — motores de video/imagen/voz/música
   disponibles vía API, precios, y agregadores (fal.ai, Replicate, etc.).
3. [`03_PLATAFORMAS_NOCODE.md`](03_PLATAFORMAS_NOCODE.md) — las 3 rutas para construir sin programar
   (Bubble, Lovable/Base44, white-label) y sus riesgos reales.
4. [`04_LEGAL_RIESGOS.md`](04_LEGAL_RIESGOS.md) — lo que puede frenar el proyecto si no se resuelve a
   tiempo: reventa de APIs, ToS, indemnización, dependencia de un solo proveedor.
5. [`05_PRESUPUESTO_Y_CRONOGRAMA.md`](05_PRESUPUESTO_Y_CRONOGRAMA.md) — los 3 niveles de inversión y
   el cronograma semana a semana de la ruta recomendada.
6. [`06_DECISIONES_PRODUCTO.md`](06_DECISIONES_PRODUCTO.md) — **documento vivo.** Cada decisión real
   que tomemos (nicho elegido, plataforma elegida, proveedor elegido, precios propios) se registra
   aquí con fecha y razón. Nunca se borra una decisión vieja — si cambia, se anota el cambio y por qué.
7. [`07_ERRORES_Y_LECCIONES.md`](07_ERRORES_Y_LECCIONES.md) — **documento vivo.** Todo error cometido
   (en este proyecto o aprendido del pipeline de producción existente) con formato
   síntoma → causa → fix → cómo evitarlo la próxima vez. El objetivo es no pagar dos veces el mismo error.

## Quién mantiene esto vivo

Tres agentes especializados (`.claude/agents/`), cada uno dueño de una porción, más el
`knowledge-archivist` general que empaqueta todo el proyecto cuando se pida:

| Agente | Dueño de | Cuándo usarlo |
|---|---|---|
| `higgsfield-market-intel` | Doc 1 | Investigar a Higgsfield y su competencia directa (movimientos, precios, features nuevas) |
| `higgsfield-tech-scout` | Docs 2, 3, 4 | Investigar proveedores de IA, plataformas no-code, y vigilar riesgos legales/ToS |
| `higgsfield-product-architect` | Docs 5, 6, 7 | Convertir investigación en decisiones concretas de producto, presupuesto y roadmap |

**Regla de oro (la misma que ya usa el resto del proyecto en `handoffs/`): si no está escrito aquí,
no existe.** Ningún agente asume que "ya se investigó eso" de memoria — si no está en estos
documentos, se investiga de nuevo y se documenta. Los agentes no tienen memoria propia entre
sesiones: **estos archivos SON la memoria.** Cada uno debe leer su documento antes de empezar y
actualizarlo antes de terminar, nunca reescribir desde cero lo que ya hay — solo añadir, corregir
fechas/precios que cambiaron, y marcar qué quedó obsoleto (tachado o con nota, nunca borrado sin dejar rastro).

## Relación con el resto del proyecto Mindset Mechanics

Este es un producto nuevo, no el pipeline de producción de videos (`video_express_ai/`, `recraft_ai/`,
`youtube_pipeline/`). Sin embargo, comparte lecciones operativas útiles — ver
`handoffs/REVISION_TECNICA_2026-08-25.md` para errores reales ya encontrados en ese pipeline
(rutas relativas silenciosamente ignoradas por git, manejo de rate-limits 429, telemetría a prueba
de fallos) que aplican igual de bien a la arquitectura de este producto nuevo.
