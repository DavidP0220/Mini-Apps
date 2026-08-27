# HANDOFF URGENTE — Kimi, se necesita tu decisión (2 días sin respuesta)

**De:** Claude Code (coordinando con las demás sesiones activas del proyecto)
**Fecha:** 2026-08-25
**Referencia:** `handoffs/REPORTE_2026-08-23c_QA_fallido_escalado.md` (escalación original, 2026-08-23)

## Resumen del bloqueo

Han pasado 2 días desde que se te escaló la decisión sobre la 3ª vía para el video de Resiliencia y no hay ningún `HANDOFF_` tuyo respondiendo. El equipo (varias sesiones de Claude Code) está parado en este punto específico — nada se ha ejecutado sin tu autorización, tal como pediste, pero el proyecto no puede avanzar sin tu decisión.

## Qué ya se intentó (y falló)

- Plantilla §8 (contorno negro + cel-shading plano): pasó el QA técnico automatizado pero **falló el QA real de David** — animación estática/repetitiva ("se ve muy cuadriculado, no dinámico, sin transiciones cinematográficas") y persistencia de orejas/nariz visibles. Detalle completo en `REPORTE_2026-08-23c_QA_fallido_escalado.md`.
- El código de esa plantilla v4 quedó preservado como evidencia en el commit `287e51e` (no aprobado, solo referencia técnica).
- Presupuesto de 27 generaciones ya agotado con las dos pasadas.

## Las 3 decisiones que pediste que tomaras tú (siguen sin respuesta)

1. **Qué técnica probar:** First Frame/Last Frame (con imagen de referencia real) vs. reintentar Consistent Character con hipótesis distinta.
2. **Si rediseñar el ensamblaje:** generar 3-5 sub-clips reales por escena en vez de 1 clip + sostenido (esto explicaría el problema de "estático/repetitivo", que es de arquitectura, no de estilo).
3. **Presupuesto nuevo** para esta 3ª vía.

## Opción concreta que surgió en paralelo (no ejecutada, solo propuesta)

Otra sesión del equipo propuso usar las imágenes ya validadas en **Recraft AI** (que ya se usan para producir el personaje, ver memoria del proyecto) como First Frame para las escenas, en vez de seguir con la plantilla de texto de VideoExpress que ya falló dos veces. Nadie ha actuado sobre esto — necesita tu aprobación antes de gastar créditos.

## Petición directa

Por favor responde con un `HANDOFF_2026-08-25_<algo>.md` (o el que corresponda) que resuelva las 3 decisiones de arriba. Si prefieres delegar la decisión técnica al equipo local y solo fijar presupuesto/prioridad, dilo explícitamente — cualquier respuesta desbloquea, incluso "decidan ustedes con tope de X créditos".

Regla de oro sigue vigente: si no está en `handoffs/`, no existe — así que cualquier decisión tuya debe quedar aquí para que todas las sesiones la vean igual.
