# HUECO #3 — Detectar señales tempranas de riesgo de desmonetización

**Ronda 01 · 2026-08-26 · estado previo: 🔴 SIN MÉTODO**
**Estado ahora: 🟢 MÉTODO DEFINIDO — aplicable desde el video 1 (no requiere datos históricos)**

El hueco decía: *"no hay forma de saber si YouTube ya está tratando al canal como bajo esfuerzo
antes de que llegue el aviso"*. La investigación encontró dos cosas: **sí hay un aviso previo**, y
sí hay un perfil de riesgo comprobable **antes de publicar**.

---

## 1. Hallazgo principal: existe un aviso previo de 7 días

YouTube opera un sistema de aviso previo: cuando considera que un canal podría perder la
monetización, **envía una notificación ~7 días antes**, dando margen a corregir. No es garantía
—no todos los casos lo reciben— pero significa que **la bandeja de notificaciones de YouTube
Studio es un canal de alerta real y hay que revisarla**, no solo las métricas.

Y el régimen sancionador completo, ya confirmado: **aviso → suspensión de monetización 90 días →
expulsión permanente del YPP.** Tres golpes.

## 2. El perfil de riesgo (lo que YouTube mira), convertido en checklist

La política de contenido no auténtico describe patrones concretos. Traducidos a algo que se puede
comprobar en el propio canal **antes de publicar**:

| # | Señal de riesgo que YouTube nombra | Autochequeo de Human Chronicles |
|---|---|---|
| 1 | Videos con plantilla y poca variación entre ellos | ¿El video N tiene el mismo orden de planos y las mismas transiciones que el N-1? Si sí, **no se publica** |
| 2 | Subidas repetitivas / contenido replicable a escala | ¿Podría otro canal producir este video cambiando solo el tema? Si sí, falta tesis |
| 3 | Narración sin aportación autoral propia | ¿Qué dice este video que no esté en la Wikipedia del tema? Si no hay respuesta en una frase, no hay tesis |
| 4 | Miniaturas y títulos repetitivos | Consistencia de paleta SÍ; misma composición y misma fórmula de título NO |
| 5 | Presentaciones de imágenes sin metraje original | Regla de los 4 s de `ERRORES_A_EVITAR.md` #14. Ya cubierto |
| 6 | Locución de IA de baja calidad | Checklist de escucha del `hueco-01`. Ya cubierto |
| 7 | Frecuencia de subida excesiva | 2 largos/semana. Ya decidido, no subir el ritmo "para acelerar" |

Las dos políticas que se citan en la inmensa mayoría de las suspensiones de 2026 son
**contenido reutilizado** (material ajeno sin valor original) y **contenido no auténtico**
(producción en masa con plantilla). Ambas están cubiertas por el checklist de arriba y por el
registro de procedencia (`sources_<video>.md`).

## 3. Chequeo periódico (el proceso que faltaba)

**Antes de publicar cada video** — lo hace `publish-readiness-coordinator`, sobre el checklist de
`ESTILO_HUMAN_CHRONICLES.md` §6 más la tabla de arriba. Un fallo en cualquiera de las 7 filas
bloquea la publicación.

**Mensual, desde que haya 3 videos** — lo hace `human-chronicles-program-director`:
1. Revisar la bandeja de notificaciones de YouTube Studio (el aviso de 7 días llega ahí).
2. Comparar los 3 últimos videos entre sí: orden de planos, transiciones, composición de miniatura,
   fórmula de título. Si dos se parecen demasiado, **es un hallazgo**, no una coincidencia.
3. Mirar impresiones. Una caída de impresiones **sin caída de CTR** es el patrón que sugiere alcance
   limitado por decisión de la plataforma, no por rendimiento del video.
4. Anotar el resultado en el tablero, aunque sea "sin señales". Un chequeo que no se anota no ocurrió.

> **Límite honesto de este método:** no existe ningún panel donde YouTube diga "te estoy tratando
> como bajo esfuerzo". El punto 3 es una **inferencia**, no una medición. Sirve para levantar una
> pregunta, no para concluir. Se marca así a propósito.

## 4. Qué NO se puede hacer todavía

Nada de la sección 3 es aplicable hoy: **0 videos publicados, 0 impresiones**. El único punto vivo
hoy es el chequeo previo a publicar (sección 2), y ese sí se aplica desde el minuto uno — es más,
como el primer video **define el canon** (`ERRORES_A_EVITAR.md` #17), se aplica sobre él con más
rigor que sobre ninguno.

## Fuentes

- [YouTube Demonetization in 2026: Still Possible, Yet Still Avoidable — Mediacube](https://mediacube.io/en-US/blog/youtube-demonetization)
- [YouTube AI demonetization: The new rule hitting entire channels — TubeBuddy](https://www.tubebuddy.com/blog/youtube-ai-demonetization-how-to-spot-risk/)
- [YouTube Inauthentic Content Policy 2026: What Threatens AI Creator Channels — ARWriter](https://arwriterai.com/en/blog/youtube-inauthentic-content-policy-ai-creators-2026/)
- [YouTube's AI content crackdown in 2026 — ScaleLab](https://scalelab.com/en/why-youtube-is-cracking-down-on-ai-generated-content-in-2026)
- [YouTube Demonetization 2026: Which Problem You Have & the Fix — YTGrowth](https://ytgrowth.io/blog/youtube-demonetization)
- [What channels have a high risk of demonetization in 2026 — MilX](https://milx.app/en/trends/what-channels-have-a-high-risk-of-demonetization-in-2026)
