# Reporte — Las 12 escenas de Resiliencia ya están generadas en Recraft, en 16:9
**De:** sesión Claude (Chrome/Recraft) **Fecha:** 2026-08-25

## Qué se hizo
Las 12 escenas de `RESILIENCE_SCENE_PLAN.md` están generadas en el proyecto de Recraft
(`https://www.recraft.ai/project/59139eb8-9a2a-468e-b7cf-15abff459480`), todas confirmadas
en 1376×768 (16:9 real — VideoExpress solo anima 16:9/9:16, ver hallazgo del 2026-08-25 en
`MANUAL_PRODUCCION.md`).

Escenas 1 y 2 se generaron primero a mano (verificadas 16:9). Escenas 3-11 las generó un
subagente en background (~54 min, 1 reintento en la escena 8 por oreja visible — el
reintento salió bien). Escena 12 se generó a mano al final porque el subagente se detuvo
antes de llegar a ella. Escena 11 (los 3 colegas) cumple el requisito no negociable de
mismo estilo plano 2D para personajes secundarios.

**Créditos gastados en total en esta ronda:** de 834 a 630 (204 créditos), quedan 630.

## Defecto encontrado, sin corregir todavía
**Escena 11 tiene una burbuja de cómic vacía en el fondo** (viola la cláusula negativa de
`RESILIENCE_SCENE_PLAN.md`/`ESTILO_MINDSET_MECHANICS.md`: "no comic panels, no speech
bubbles"). Recraft ya ofrece un botón "Remove speech bubble" sobre esa imagen en el chat
del proyecto — no lo usé todavía porque no es bloqueante para seguir y quería dejarlo
para revisión en vivo. Antes de animar esa escena en VideoExpress, aplicar esa corrección
(o regenerar la escena si no se ve bien limpio).

## Pendiente de decisión de David (no lo hice sin autorización)
**API de Recraft:** existe una vía mucho más rápida y estable para generar imágenes (API
REST directa, sin navegador — ver commit `recraft_ai/`), pero requiere cargar saldo
separado: mínimo $5 USD por 5000 unidades. No lo compré, queda pendiente de que David
confirme el gasto. Mientras tanto, todo lo de hoy se hizo por la vía de navegador (más
lenta, ~200 créditos de la app web, pool aparte del de la API).

## Siguiente paso técnico
Con las 12 imágenes ya en Recraft, falta: (1) descargarlas a
`video_express_ai/outputs/` y subirlas a VideoExpress con `import_local_image()`, (2)
animar cada una con `animate_library_image()` (función nueva, ver commit `4208ccb`) usando
el Video Action Prompt de cada escena de `RESILIENCE_SCENE_PLAN.md`, (3) 1 experimento
First Frame/Last Frame en la escena 1 (autorizado por Kimi), (4) ensamblar solo el piloto
de escenas 1-2 (~90s) y parar para el veredicto de David — según el gate que fijó Kimi en
`HANDOFF_2026-08-25_decision_tercera_via_resiliencia.md`.

No se ha gastado nada del presupuesto de animación de VideoExpress todavía (el piloto de
Kimi: máx 8 animaciones VE + 6 stills Recraft) — los 630 créditos de Recraft gastados son
de generar las 12 imágenes completas, más de lo que cubría el piloto original de 2
escenas, porque se decidió generar el set completo de una vez en vez de solo el piloto.
Vale la pena que Kimi lo sepa para ajustar el presupuesto restante.
