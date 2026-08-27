# PROGRAMA DE MEJORA CONTINUA — Kimi Code (permanente)
**Fecha de creación: 2026-08-25 · Directriz del usuario: "tu trabajo aquí nunca acaba — investiga, analiza y actúa diariamente para tener las mejores estrategias."**
**NOTA: este documento NO es un plan activo (no empieza por HANDOFF_) — es el programa permanente de Kimi. El plan activo sigue siendo el último HANDOFF_*.**

---

## 1. Ronda diaria de Kimi (ciclo fijo)

Cada día, Kimi ejecuta este ciclo y deja resultado en el repo:

1. **Leer el estado del proyecto:** `handoffs/` (reportes nuevos de Claude), últimos commits, bloqueantes abiertos.
2. **Investigar** (1-2 frentes por día, rotando la agenda de §2): fuentes externas actualizadas, datos del nicho, técnicas de producción.
3. **Actuar:** commitear al repo lo que corresponda:
   - Decisión/bloqueo resuelto → `handoffs/HANDOFF_YYYY-MM-DD_<tema>.md`
   - Hallazgo de investigación accionable → `handoffs/NOTA_INVESTIGACION_YYYY-MM-DD_<tema>.md` (no es plan activo, es insumo)
   - Nada nuevo que reportar → no commitear ruido; el silencio también es disciplina.
4. **Regla de oro del programa:** investigación sin acción es ruido. Cada nota de investigación termina en una recomendación concreta: adoptar / probar con presupuesto X / descartar con motivo.

## 2. Agenda de investigación rotativa

| Día | Frente | Qué busco |
|---|---|---|
| Lunes | **Nicho y competencia** | Videos nuevos de los 12 canales benchmark (Human Condition, Zenn, ONLI, Decode The Brain...): qué títulos/formatos están rompiendo AHORA, no hace 3 meses |
| Martes | **Técnica de producción IA** | Novedades de VideoExpress, Recraft y generadores de video (Veo/Kling/Sora): features nuevas, cambios de precio, técnicas de consistencia de personaje que hayan madurado |
| Miércoles | **Algoritmo y métricas YouTube** | Cambios en recomendación/Shorts/monetización; lectura de las métricas del propio canal cuando haya datos nuevos (cada video publicado genera datos a los 10 días — regla del playbook) |
| Jueves | **Guiones y retención** | Análisis de guiones top del nicho (cuando video_understand.py esté validado, transcribir competencia); patrones de hook/retención nuevos |
| Viernes | **Estrategia y monetización** | Hoja de ruta a 1.000 subs: revisión de la matemática del playbook §7 con datos reales actualizados; preparación del siguiente handoff de contenidos |
| Fin de semana | **QA y deuda** | Revisión de reportes acumulados, priorización de deuda técnica, limpieza de decisiones obsoletas en handoffs |

## 3. Restricciones permanentes del programa

- **Coste cero por defecto:** la investigación es web/datos — nunca gasta créditos de VideoExpress ni Recraft. Cualquier recomendación que implique gasto va como propuesta con presupuesto, nunca ejecutada directamente.
- **No contradecir el plan activo:** si una investigación sugiere cambiar algo del plan activo, se propone en un HANDOFF nuevo que explícitamente diga qué reemplaza.
- **Reportar consumo:** toda nota que derive en gasto debe cerrar el ciclo midiendo el resultado (regla 8 del principio rector).
- **Renovación de token:** el token de GitHub expira 2026-09-22 — avisar a David el 2026-09-18 como muy tarde.

## 4. Cómo se activa

- Vía automática: recordatorio diario programado en el chat de Kimi (cron).
- Vía manual: David escribe "ronda diaria" o "urgente en repo" en cualquier momento y se ejecuta el ciclo fuera de horario.
