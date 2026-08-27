# ESTADO — tablero vivo del proyecto

> Lo mantiene `jefe-monetizacion`. Se actualiza al cerrar **cada** ronda. Append-only: cada
> ronda añade su bloque arriba; los bloques anteriores se quedan.

## Objetivo único
**Monetizar el canal.** Traducido a números:
- 1.000 suscriptores **y** 4.000 horas de visualización pública en 12 meses (vía formato largo).
- En paralelo, ingresos que no dependen de AdSense: infoproductos por enlace, tienda, comunidad.

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
| Producción | 🔴 bloqueada por P-01 | Sin nicho no hay guion |
| Puente con Kimi | 🟡 protocolo listo | Sin handoff activo todavía |
| Monetización | 🔴 0 de 1.000 subs | El objetivo |
