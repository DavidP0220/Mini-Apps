# Paquete de conocimiento — Proyecto "Alternativa a Higgsfield.ai"

**Empaquetado:** 2026-08-26. **Estado del proyecto en este momento:** fase de investigación
completa, decisiones D-001 a D-006 tomadas, roadmap del Nivel 1 (MVP) escrito paso a paso.
**Dinero real gastado hasta hoy: $0.00.** Ningún código escrito todavía.

Este archivo existe para que **cualquier otra sesión de Claude, en cualquier otro proyecto o
cuenta, pueda entender este sistema completo sin haber estado en la conversación original.**
No omite nada a propósito — si algo existe y es relevante, está aquí o referenciado explícitamente.

---

## 1. Nombre del proyecto

**"Alternativa a Higgsfield.ai"** (nombre de producto todavía sin definir — es una de las
decisiones pendientes; internamente se identifica como `PROYECTO HIGGSFIELD ALTERNATIVA` en el
repo de Mindset Mechanics).

## 2. Por qué existe (el origen)

David (dueño del canal de YouTube **Mindset Mechanics**, contenido de psicología evolutiva /
desarrollo personal) recibió un informe de investigación (`fuente_original/informe_higgsfield.pdf`,
agosto 2026) sobre cómo construir y monetizar una alternativa propia a Higgsfield.ai — la empresa
dominante de IA generativa de video/imagen para creadores de contenido ($5,400M de valoración,
$700M de ingresos anuales, cerrada Serie B de $400M en agosto 2026).

El informe concluye que competir de frente es inviable, pero que existe un hueco real: construir
una herramienta de nicho (mindset/motivación/desarrollo personal) usando plataformas no-code +
APIs de terceros, apalancando la audiencia ya existente del canal como primer mercado de prueba.

David pidió explícitamente: no dejar esa información solo en un PDF de Downloads, sino un sistema
que **investigue, analice, guarde permanentemente y siga alimentándose**, para no perder contexto
ni repetir errores ya cometidos en el pipeline de producción existente del canal.

## 3. Para qué sirve (el objetivo concreto)

Construir y monetizar un **producto de software propio** (no contenido de un canal, no un video)
— una herramienta de IA generativa de video/imagen para creadores del nicho mindset/motivación,
vendida por suscripción o créditos, empezando con la propia audiencia del canal como primeros
usuarios de pago. Es un proyecto de negocio nuevo, separado del pipeline de producción de videos
de Mindset Mechanics, aunque nace de la misma cuenta y comparte lecciones técnicas con él.

## 4. Cómo está organizado — en qué orden leer

1. **`investigacion/INDEX.md`** — el mapa de los 7 documentos de investigación, quién los mantiene
   y con qué regla de actualización.
2. **`investigacion/01` a `04`** — qué se investigó: competencia (Higgsfield y su mercado),
   proveedores de IA vía API, plataformas no-code para construir sin programar, y riesgos legales.
   Todos verificados con búsquedas web frescas el 2026-08-25/26, no solo copiados del PDF original.
3. **`investigacion/05_PRESUPUESTO_Y_CRONOGRAMA.md`** — **el documento más importante para
   ejecutar**: contiene el roadmap paso a paso del MVP, escrito para alguien sin experiencia
   técnica (qué web abrir, qué botón apretar, qué prompt copiar y pegar en Lovable.dev), con cada
   paso que cuesta dinero marcado `[GASTO — requiere OK de David]`.
4. **`investigacion/06_DECISIONES_PRODUCTO.md`** — registro histórico de cada decisión real
   (nicho, plataforma, proveedor, precios), con fecha, razón, y qué alternativas se descartaron y
   por qué. Nunca se borra una entrada vieja.
5. **`investigacion/07_ERRORES_Y_LECCIONES.md`** — errores cometidos (propios de este proyecto y
   heredados del pipeline de producción existente), en formato síntoma → causa → fix → cómo
   evitarlo. Incluye un hallazgo importante: la propia carpeta de este proyecto estuvo sin respaldo
   en git durante 24 horas por un bug de `.gitignore` de lista blanca — ver el detalle ahí.
6. **`agentes/`** — los 3 agentes especializados que mantienen vivo este sistema (ver sección 5).
7. **`fuente_original/informe_higgsfield.pdf`** — el PDF original que dio origen a todo, sin editar.
8. **`dossier_html/dossier_higgsfield.html`** — el resumen visual (HTML autocontenido, abrir en
   cualquier navegador) que se le presentó a David para revisar antes de aprobar el roadmap.
9. **`HABILIDADES_APRENDIDAS.md`** — el método/sistema reutilizable que se construyó aquí, para que
   otro proyecto de Claude lo replique sin tener que redescubrirlo.
10. **`HABILIDADES_FALTANTES.md`** — lo que este sistema todavía NO sabe hacer y necesitaría
    aprender para retroalimentarse mejor.

## 5. Los 3 agentes especializados (en `agentes/`)

| Agente | Dueño de | Regla dura |
|---|---|---|
| `higgsfield-market-intel` | Competencia (doc 01) | Nunca decide estrategia de producto |
| `higgsfield-tech-scout` | Proveedores IA, no-code, legal (docs 02-04) | Nunca decide estrategia de producto |
| `higgsfield-product-architect` | Presupuesto, decisiones, errores (docs 05-07) | **Nunca ejecuta gasto real ni activa nada sin aprobación explícita de David en el chat** |

Ninguno tiene memoria propia entre sesiones — **los 7 documentos de `investigacion/` SON la
memoria.** Cada agente lee su documento antes de empezar y lo actualiza antes de terminar, nunca
lo reescribe desde cero.

## 6. Qué es específico de este proyecto vs. qué es el método reutilizable

- **Específico de "alternativa a Higgsfield" (no aplica igual a otro proyecto):** el nicho elegido
  (mindset/motivación), la plataforma elegida (Lovable.dev), el proveedor de IA elegido (fal.ai),
  los precios propuestos, todo el contenido factual de los documentos 01-04.
- **Método reutilizable (esto es lo que vale la pena copiar a otro proyecto):** ver
  `HABILIDADES_APRENDIDAS.md` — la arquitectura de "documentos vivos + agentes dueños de una
  porción cada uno + regla de nunca gastar sin aprobación + roadmap con gasto marcado
  explícitamente" es aplicable a cualquier proyecto nuevo que combine investigación con ejecución
  real de dinero.

## 7. Relación con el resto de proyectos de esta cuenta

Esta cuenta (`mechanicsmindset02@gmail.com`) tiene tres iniciativas separadas y deliberadamente no
mezcladas: el canal **Mindset Mechanics** (producción de video), el canal **Human Chronicles**
(faceless, historia), y este producto de software nuevo. Existe además una carpeta
`virtual_influencer_platform/` con un enfoque completamente distinto (contenido +18, self-hosted)
que **no tiene ninguna relación con este proyecto** y no fue tocada al construir este paquete.
