---
description: Lanza una ronda completa del sistema multiagente del canal (jefe + especialistas)
argument-hint: [foco opcional, p.ej. "nicho" o "métricas"]
---

Abre una ronda de trabajo del proyecto del canal. Foco pedido: $ARGUMENTS
(si está vacío, el jefe decide el foco según `canal/ESTADO.md`).

Actúa como orquestador siguiendo `.claude/agents/jefe-monetizacion.md`:

1. Lee `canal/ESTADO.md`, las últimas entradas de `canal/bitacora/` y el `HANDOFF_*.md` más
   reciente de `canal/puente-kimi/`.
2. Reparte encargos a los especialistas que correspondan (`investigador-nicho`,
   `analista-datos`, `arqueologo-memoria`, `director-storyboard`), lanzándolos **en paralelo**
   cuando sean independientes. Cada encargo dice qué traer y contra qué número del objetivo se
   juzga.
3. Revisa cada entrega contra `canal/base-conocimiento/02-errores/ERRORES-HISTORICOS.md` y
   `canal/protocolos/DEFINICION_DE_HECHO.md`. Rechaza lo que no cumpla, diciendo exactamente
   qué falta, y relanza al agente.
4. Cierra la ronda actualizando `canal/ESTADO.md`: números de hoy contra la ronda anterior, qué
   se movió, la deuda con nombre del agente, el bloqueante más caro, y las 3 acciones de mañana
   con responsable.
5. Commitea y pushea todo a la rama de trabajo.

Todo en español. No gastes créditos ni publiques nada sin autorización explícita de David.
