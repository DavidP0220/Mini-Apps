# HALLAZGO CRÍTICO — El umbral de YPP se DUPLICA el 1-feb-2027

**Ronda de investigación 01 · 2026-08-26 · cierra el dato marcado "sin verificar" en `TABLERO_MONETIZACION.md`**

---

## Qué se buscaba

El `TABLERO_MONETIZACION.md` traía esta nota entre paréntesis:

> *"4.000 h (⚠️ pasan a 8.000 h el 1-feb-2027 para canales fuera del YPP — **dato sin verificar en Studio**)"*

Era un dato sin confirmar arrastrado de una sesión anterior. **Está confirmado, y es peor y mejor
de lo que decía la nota a la vez.**

## Qué dice el dato confirmado

| Concepto | Hoy (hasta 31-ene-2027) | Desde el 1-feb-2027 |
|---|---|---|
| Suscriptores para YPP | 1.000 | 1.000 (**no cambia**) |
| Horas de reproducción válidas (365 días) | **4.000 h** | **8.000 h** |
| Vía alternativa por Shorts (90 días) | 10 M de vistas válidas | **20 M de vistas válidas** |
| Canales **ya dentro** del YPP | — | **No les afecta. Quedan protegidos.** |

Y un dato que **corrige** el playbook actual:

| Concepto | Lo que decía `PLAYBOOK_MONETIZACION_HC.md` §4 | Lo confirmado |
|---|---|---|
| YouTube Shopping / fan funding | "accesible desde 500 suscriptores" | **500 subs Y ADEMÁS** 3.000 h de reproducción en el último año **o** 3 M de vistas de Shorts en 90 días |

El umbral de 500 subs no era el umbral completo. Shopping no está "a la vuelta de la esquina": pide
casi tanto watch time como el propio YPP viejo.

## Por qué esto cambia la estrategia entera

Hoy es **2026-08-26**. Quedan **~5 meses** (158 días) hasta el 1-feb-2027.

El canal tiene **0 videos publicados**. Las dos lecturas posibles:

**Lectura A — se llega antes del 1-feb-2027.** El canal entra al YPP con el umbral viejo (4.000 h)
y queda **protegido de por vida** del umbral nuevo. Requiere: primer video publicado ya, ritmo
sostenido, y 1.000 subs + 4.000 h en 5 meses desde cero. Es agresivo pero no imposible en un nicho
con watch time alto — y es exactamente la ventaja que tiene este nicho.

**Lectura B — no se llega.** El listón sube a 8.000 h. **El coste de no llegar es que el esfuerzo
necesario se duplica**, no que se retrase un poco. Cada semana de retraso ahora vale el doble
después.

### Consecuencia operativa inmediata

El bloqueo raíz (`ESTADO_CANAL.md` §4, pendiente #4: **subnicho sin decidir**) ya no es solo el
primer eslabón de la cadena: **tiene reloj**. Cada día que el subnicho siga sin decidir consume
parte de una ventana de 5 meses que no se repite.

Esto sube el subnicho de "🟡 bloqueo" a **🔴 bloqueo urgente con fecha límite**, y justifica
presentárselo a David de inmediato y en corto, tal como obliga `ERRORES_A_EVITAR.md` #5.

### Consecuencia sobre la mezcla de contenido

`PLAYBOOK_MONETIZACION_HC.md` §2 elige la **Vía A (horas de reproducción)** como principal y los
Shorts como puerta de entrada de suscriptores. Ese análisis **sigue siendo correcto y ahora lo es
más**: la vía de Shorts pasa de 10 M a 20 M de vistas en 90 días, que para un canal nuevo es
inalcanzable. Los Shorts sirven para los 1.000 suscriptores; las horas salen de los largos.
No revertir.

## Estado de verificación (honesto)

- **Confirmado por ≥4 fuentes secundarias independientes** que coinciden en las mismas cifras y la
  misma fecha (vidIQ, Business Standard, No Film School, Android Headlines, subsub, izoate).
- **NO verificado contra la página oficial de YouTube.** `blog.youtube` y `support.google.com`
  están **bloqueados por el proxy de red del entorno remoto** donde se hizo esta investigación
  (error `EGRESS_BLOCKED`, comprobado el 2026-08-26). No es que no se intentara: se intentó dos
  veces y el gateway devolvió 403.
- **Acción pendiente de verificación final (David, 5 min):** abrir
  `https://support.google.com/youtube/answer/12843009` y
  `https://blog.youtube/news-and-events/youtube-partner-program-updates-2027-new-opportunities-earn/`
  y confirmar las dos cifras (8.000 h / 20 M) y la fecha (1-feb-2027).

Se documenta así a propósito, por `ERRORES_A_EVITAR.md` #4: un dato operativo se verifica contra
la fuente real. Cuatro fuentes secundarias que coinciden es fuerte, pero no es la fuente real.

## Fuentes

- [YouTube Monetization Requirements Are Changing in 2027 — vidIQ](https://vidiq.com/blog/post/youtube-partner-program-changes-2027/)
- [YouTube updates channel monetisation rules after 8 years — Business Standard](https://www.business-standard.com/technology/tech-news/technology-tech-news-youtube-partner-program-monetisation-rules-2027-watch-hours-shorts-views-126081100708_1.html)
- [YouTube Announces Changes to Partner Program — No Film School](https://nofilmschool.com/youtube-partner-program-changes)
- [YouTube Is Doubling Partner Program Monetization Requirements — Android Headlines](https://www.androidheadlines.com/2026/08/youtube-doubles-partner-program-monetization-requirements-2027-update.html)
- [YouTube Monetization Requirements for 2026 Explained — SubSub](https://www.subsub.io/blog/youtube-monetization-requirements)
- [How Many Subscribers Do You Need to Make Money on YouTube (2026) — Izoate](https://www.izoate.com/blog/how-many-subscribers-do-you-need-to-make-money-on-youtube-2026-what-each-tier-actually-unlocks/)
- [Changes to the YouTube Partner Program — YouTube Help (oficial, no accesible desde este entorno)](https://support.google.com/youtube/answer/12843009)
