# Protocolo de ronda de investigación recurrente

Para que el canal siga cerrando huecos sin depender de que David se acuerde. Complementa a
`SKILL_human-chronicles-daily-push.md` (que audita al equipo); esto es lo que se investiga.

## Frecuencia recomendada

**Semanal, no diaria.** Razón honesta: las políticas de YouTube, los precios de las herramientas y
los umbrales del YPP **no cambian a diario**. Una ronda diaria sobre los mismos temas devuelve los
mismos resultados y gasta tokens sin entregable — que es justo lo que el tablero prohíbe
("prohibido *estoy investigando* sin entregable").

Pasa a **diaria** solo en dos situaciones concretas:
1. Hay un plazo activo a menos de 30 días (hoy lo hay: **1-feb-2027**, umbral del YPP).
2. Se está monitorizando un aviso de YouTube ya recibido (la ventana de corrección es de ~7 días).

## Qué se revisa en cada ronda

| Prioridad | Tema | Qué buscar | Se cierra cuando |
|---|---|---|---|
| 1 | **Cambios de política de YouTube** | Contenido no auténtico, declaración de contenido sintético, umbrales del YPP | Nunca — es vigilancia permanente |
| 2 | **Huecos aún abiertos** (`SINTESIS.md` §7) | Lo concreto que falta en cada uno | Cuando el hueco llega a 🟢 |
| 3 | **Precios y licencias de las herramientas del pipeline** | Voz, imagen, mapas, plataforma de venta | Cuando cambia un precio o una licencia |
| 4 | **Competencia del subnicho** | Formatos, duraciones, fórmulas de título que funcionan | Solo una vez decidido el subnicho |

## Reglas de la ronda (no negociables)

1. **Una ronda sin entregable no es una ronda.** Si no hay un archivo nuevo y fechado en
   `investigacion/`, no se anota nada y no se dice que se investigó.
2. **Cada afirmación con fuente y con fecha.** Un enlace, no un recuerdo.
3. **Si nada cambió, se dice que nada cambió** — una línea en `REGISTRO.md` y se acaba. Es un
   resultado perfectamente válido y mucho mejor que inventar movimiento.
4. **Verificar contra la fuente real** todo lo que afecte a un plazo, un umbral o un presupuesto
   (`ERRORES_A_EVITAR.md` #4 y #21). Si un dominio está bloqueado, se marca como no verificado —
   nunca se disfraza de confirmado.
5. **Ejecutar primero, documentar después** (#20).
6. Solo `human-chronicles-program-director` escribe en `TABLERO_MONETIZACION.md`.

## Salida de cada ronda

1. Un archivo `investigacion/AAAA-MM-DD_<tema>.md` con hallazgos y fuentes.
2. Una entrada nueva **arriba** en `investigacion/REGISTRO.md`.
3. Si hay un hallazgo que cambie una decisión o un plazo: entrada nueva en el tablero **y**
   aviso a David en corto (`ERRORES_A_EVITAR.md` #5). Nada bloqueante espera más de 24 h.
4. Si el hallazgo es una lección: entrada nueva en `ERRORES_A_EVITAR.md`, continuando desde #24.

## Cómo se lanza

Puede ir como Routine (tarea programada de Claude) con este prompt:

> Ronda de investigación de Human Chronicles. Lee `human-chronicles/SINTESIS.md` y
> `human-chronicles/investigacion/REGISTRO.md`, mira qué huecos siguen abiertos, y sigue el
> protocolo de `human-chronicles/tarea_programada/RONDA_INVESTIGACION.md`. Si nada ha cambiado,
> dilo en una línea y no inventes avances. Comunícate en español.
