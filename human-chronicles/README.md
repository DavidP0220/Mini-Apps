# Human Chronicles — conocimiento y método del canal

Todo el conocimiento del canal de YouTube **Human Chronicles** (`@humanchronicles11`): historia y
civilizaciones, en inglés, formato faceless, operado por un equipo de agentes con un único objetivo
— **llegar a monetización**.

## Por dónde empezar

1. **`SINTESIS.md`** ← empieza aquí, siempre. Los 39 documentos condensados en uno.
2. `documentos_canal/ERRORES_A_EVITAR.md` — 23 lecciones fechadas y con fuente.
   **Se lee entero antes de tocar nada.** Cada entrada costó créditos, tiempo o un video reprobado.
3. `documentos_canal/ESTADO_CANAL.md` — fuente única de verdad. Si un dato no está confirmado ahí,
   no está confirmado.
4. `documentos_canal/TABLERO_MONETIZACION.md` — marcador e historial. Entrada #3 = ronda 01.

## No leas los documentos enteros

Leer los 39 cuesta **~71.000 tokens**, y se pagan en cada turno posterior de la sesión.

```bash
node human-chronicles/tools/hc.mjs listar               # índice + coste en tokens de cada uno
node human-chronicles/tools/hc.mjs ver <doc>            # secciones de un documento
node human-chronicles/tools/hc.mjs ver <doc> <n>        # SOLO esa sección
node human-chronicles/tools/hc.mjs buscar "texto"       # grep sobre todo el conocimiento
node human-chronicles/tools/hc.mjs estado               # ficha del canal
node human-chronicles/tools/hc.mjs huecos               # lo que falta por aprender
```

Hay un hook (`tools/hooks/aviso-content.mjs`) que **bloquea** leer de golpe cualquier `.md` de más
de 6 KB de este directorio y remite a `hc.mjs`. No es un recordatorio, es una barrera. `SINTESIS.md`
y este README están exentos.

## Buscar material de dominio público

```bash
node human-chronicles/tools/buscar-archivo.mjs "Constantinople 1453" --video video-01
```

Consulta Wikimedia Commons, Library of Congress e Internet Archive, descarta lo que no tenga
licencia comercial legible y genera el `sources_<video>.md` obligatorio del canal.

> ⚠️ **Escrita pero nunca ejecutada** (2026-08-26): el entorno remoto donde se escribió bloquea las
> tres APIs en el proxy de red. **La primera corrida en tu máquina es el paso de validación.**

## Estructura

| Carpeta | Qué hay |
|---|---|
| `documentos_canal/` | Los 6 documentos del canal (perfil, estado, errores, tablero, estilo, playbook) |
| `investigacion/` | Rondas de investigación fechadas y con fuentes. Ronda 01: 2026-08-26 |
| `agentes/` | Los 9 agentes: 5 exclusivos de HC + 4 multicanal (**al invocar los multicanal hay que decirles en qué canal trabajan**) |
| `herencia_mindset_mechanics/` | Pipeline heredado del canal hermano. Su `MANUAL_PRODUCCION.md` §3 es el banco de movimientos de cámara |
| `memoria/` | Reglas permanentes del usuario |
| `tarea_programada/` | La tarea diaria que invoca al director del programa |
| `tools/` | `hc.mjs` (lectura selectiva) y `buscar-archivo.mjs` (dominio público) |

Los 9 agentes están **además** instalados en `.claude/agents/` de este repo, así que son invocables
y quedan respaldados en git — lo que cierra el problema de `ERRORES_A_EVITAR.md` #19 (los agentes
vivían fuera de todo repositorio y se perdían si se borraba la carpeta).

## Aviso sobre el aislamiento de canales

Este directorio vive en el repo `Mini-Apps`, que **no** es la cuenta de Human Chronicles. La regla
de aislamiento (`ESTADO_CANAL.md` §1) es sobre **cuentas de Google/YouTube**, no sobre GitHub, así
que no hay riesgo de strike cruzado. Pero la regla de David de no mezclar canales sigue viva.

**Este directorio es autocontenido y portable a propósito:** el día que exista un repositorio propio
de Human Chronicles, se mueve entero y no se rompe nada. Recomendado hacerlo. Mientras tanto, la
documentación tiene respaldo remoto — que es más de lo que tenía.

## Idioma

Todo el material **del canal** (guion, prompts, títulos, descripciones, subtítulos) va en **inglés**.
Toda la documentación interna y toda la comunicación con David, en **español**. Sin excepción.
