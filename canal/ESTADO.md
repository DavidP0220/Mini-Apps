# ESTADO — tablero vivo del proyecto

> Lo mantiene `jefe-monetizacion`. Se actualiza al cerrar **cada** ronda. Append-only: cada
> ronda añade su bloque arriba; los bloques anteriores se quedan.

## Objetivo único
**Monetizar el canal.** Traducido a números:
- 1.000 suscriptores **y** 4.000 horas de visualización pública en 12 meses (vía formato largo).
- En paralelo, ingresos que no dependen de AdSense: infoproductos por enlace, tienda, comunidad.

---

## Ronda 2026-08-27 (b) — reconexión con Kimi y hallazgo del proyecto real

**Lo que se descubrió (cambia el plan):**
- El proyecto **ya existe** y está más avanzado de lo que sabíamos. En `DavidP0220/mindset-mechanics`
  (privado, acceso de escritura confirmado) vive el **Plan Maestro de portafolio**: 10 nichos
  investigados con evidencia real y **el canal #1 ya con nombre confirmado, `Vantage Case`**
  (true crime / misterio), con los handles libres en las cuatro plataformas desde el 23-ago.
- **Kimi lleva 4 días esperando respuesta.** Dejó dos handoffs el 23-ago con tres decisiones de
  producto abiertas (agregador vs. integración directa, agente de voz, VideoExpress) que nadie
  contestó porque el trabajo siguió en otra línea paralela.
- **El puente con Kimi nunca fue automático.** Kimi no tiene cuenta de Google, ni disco, ni git:
  la dirección Claude → Kimi siempre dependió de que David arrastrara el archivo a su chat.
  El protocolo que escribí esta mañana estaba equivocado y ya está corregido.
- **Riesgo de primer orden fichado (E-15):** en enero de 2026 YouTube terminó 16 canales con
  35 millones de suscriptores por "contenido no auténtico". El atajo de plantilla + IA + volumen
  es exactamente ese perfil. Afecta directamente al plan de monetizar rápido.

**Qué se entregó**
- `puente-kimi/HANDOFF_KIMI_2026-08-27_reconexion.md` — handoff de reconexión para Kimi, con las
  tres decisiones reabiertas y una recomendación por cada una.
- `puente-kimi/README.md` — protocolo corregido con el funcionamiento real del puente.
- Fichas **E-15** y **E-16** en el catálogo de errores.

**Bloqueante más caro:** ya no es P-01 (el canal probablemente es `Vantage Case`). Ahora es
**la fragmentación**: tres sitios con trabajo del mismo proyecto que no se ven entre sí (E-16).
Hasta consolidarlos, cualquier cosa que produzcamos corre el riesgo de duplicar lo ya hecho.

**Las 3 acciones siguientes**
| # | Acción | Responsable | Depende de |
|---|---|---|---|
| 1 | Entregar el handoff de reconexión a Kimi y traer sus tres respuestas | David (es el cartero) | Nada |
| 2 | Consolidar los tres sitios en una fuente única de verdad | `arqueologo-memoria` | Visto bueno de David |
| 3 | Análisis de nicho sobre `Vantage Case` (true crime) en vez de partir de cero | `investigador-nicho` | Confirmación del canal |

---

## Ronda 2026-08-27 — montaje del sistema

**Números de hoy:** el canal nuevo todavía no existe. Suscriptores 0 · horas 0 · videos 0.
Línea base heredada del canal anterior en `base-conocimiento/04-metricas/METRICAS.md`.

**Qué se movió**
- Sistema multiagente creado: 1 orquestador + 4 especialistas, en `.claude/agents/`.
- Archivo histórico completo depositado e inmutable en `archivo/` (18 MB, 142 archivos).
- Base de conocimiento sembrada con datos reales, no con plantillas vacías:
  **14 errores** fichados con causa raíz y antídoto, **6 fórmulas de título** con evidencia
  medida, **10 decisiones** vigentes, línea base de métricas y umbrales de decisión.
- Protocolos escritos: investigación, antiborrado, definición de "hecho", puente con Kimi.
- Pipeline de producción y plantilla de storyboard, heredando el sistema de 12 campos ya probado.

**Qué NO se movió**
- Ningún número del objetivo. Es esperable: hoy se construyó la máquina, no se publicó nada.
  A partir de la ronda siguiente, cada ronda debe mover un número o justificar por escrito por qué no.

**Deuda:** ninguna todavía.

**Bloqueante más caro:** `P-01` — no hay nombre, nicho exacto ni ángulo del canal nuevo. Bloquea
absolutamente todo lo demás: guiones, storyboards, miniaturas, calendario. Se destraba con una
ronda de `investigador-nicho` sobre la mesa y una decisión de David (y Kimi).

**Las 3 acciones de la próxima ronda**
| # | Acción | Responsable | Mueve |
|---|---|---|---|
| 1 | Ronda de nicho: qué está rompiendo **ahora** en el nicho y qué hueco hay libre → 3 propuestas de canal (nombre, ángulo, formato) con evidencia | `investigador-nicho` | Destraba P-01 |
| 2 | Matemática del objetivo: cuántos videos, a qué ritmo y con qué vistas medias hacen falta para llegar a 1.000 subs y 4.000 horas; y qué pasa si el ritmo real es la mitad | `analista-datos` | Fija la cadencia real |
| 3 | Barrido del archivo en busca de decisiones y activos rescatables que ahorren trabajo al canal nuevo | `arqueologo-memoria` | Evita repetir trabajo ya pagado |

---

## Semáforo permanente

| Frente | Estado | Nota |
|---|---|---|
| Investigación | 🟢 sistema listo | Falta la primera ronda |
| Datos y métricas | 🟡 sin canal | Línea base heredada disponible |
| Memoria y archivo | 🟢 completo | 18 MB archivados, 14 errores fichados |
| Producción | 🟠 bloqueada por consolidación | El canal probablemente ya tiene nombre: `Vantage Case` |
| Puente con Kimi | 🟠 handoff escrito, sin entregar | Depende de David: hay que arrastrarlo al chat de Kimi |
| Monetización | 🔴 0 de 1.000 subs | El objetivo |
