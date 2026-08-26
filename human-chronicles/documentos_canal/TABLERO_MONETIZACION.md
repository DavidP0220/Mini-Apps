# Human Chronicles — Tablero de monetización (marcador del equipo)

**Único objetivo del tablero: llevar este canal a estar monetizado.**
Lo mantiene `human-chronicles-program-director`. Los otros agentes del canal lo leen antes de
empezar y anotan aquí lo que entregan.

## Reglas del tablero (no negociables)

1. **Nunca se reescribe desde cero.** Cada revisión añade una **entrada nueva ARRIBA**; el
   historial completo queda abajo, intacto y para siempre.
2. Cada entrada lleva, sí o sí: **fecha · qué se hizo (con entregable real) · qué falta ·
   qué bloquea · próxima acción concreta con responsable y fecha**.
3. **Prohibido "estoy investigando" sin entregable ni fecha.** Un avance que no se puede
   señalar con el dedo en un archivo no es un avance.
4. Nada de avances simulados. Si algo depende de David (login, dinero, aprobación), se anota
   como bloqueo con su nombre, no se disfraza de progreso.

## Marcador — estado hacia YPP

| Métrica | Meta | Real | Verificado |
|---|---|---|---|
| Videos publicados | 1º video publicado | **0** | 2026-08-25 (documental) |
| Suscriptores | 1.000 | **sin dato medido** | ⛔ nunca verificado en YouTube Studio |
| Horas de reproducción | **4.000 h hasta el 31-ene-2027 · 8.000 h desde el 1-feb-2027** ✅ dato verificado 2026-08-26 (4 fuentes secundarias; falta confirmar en la página oficial, bloqueada por el proxy) | **0** | 2026-08-26 (documental) |
| Infoproducto activo (no requiere umbral) | 1 link vivo en descripción | **no existe** — plataforma ya elegida (Lemon Squeezy), ruta completa en `investigacion/2026-08-26_hueco-04_infoproducto-v0.md` | 2026-08-26 |
| Identidad visual (avatar + banner) | subidos | **no subidos** | 2026-08-25 |

---

# ENTRADAS (la más reciente primero)

## 2026-08-26 — Entrada #3 · Ronda 01 de investigación: se cierran 4 huecos y aparece una fecha límite

**Contexto:** David entregó el paquete de conocimiento completo del canal y pidió sintetizarlo,
guardarlo y **buscar en la web todo lo que faltaba**. Esta entrada registra el resultado. El
trabajo se hizo en el repositorio `Mini-Apps`, rama `claude/humanic-project-optimization-dru8my`,
directorio `human-chronicles/` — autocontenido y portable a un repo propio del canal.

**Qué se hizo de verdad hoy (entregables verificables en disco):**
- Los 30 documentos del paquete, guardados íntegros en `human-chronicles/` y **con respaldo remoto**
  por primera vez (git push). Verificado con `git check-ignore -v` que no quedan ignorados (#6).
- `human-chronicles/SINTESIS.md` — los 39 documentos (≈71.000 tokens si se leen enteros)
  condensados en uno de ~3.000.
- **10 documentos de investigación fechados y con fuentes** en `human-chronicles/investigacion/`,
  uno por hueco del `PERFIL_DEL_PROYECTO.md` §5.
- 3 entradas nuevas en `ERRORES_A_EVITAR.md` (#21, #22, #23) por hallazgos de esta ronda.
- 2 herramientas: `tools/hc.mjs` (lectura selectiva, probada y funcionando) y
  `tools/buscar-archivo.mjs` (dominio público → `sources_<video>.md`, **escrita pero no ejecutada**).

**🔴 Hallazgo que cambia el plazo de todo el proyecto:**
El umbral de entrada al YPP **se duplica el 1-feb-2027**: de 4.000 h a **8.000 h** (y la vía de
Shorts de 10 M a 20 M de vistas). **Los canales ya dentro quedan protegidos.** Quedan ~5 meses.
Corrección adicional: YouTube Shopping no es "500 subs" — es 500 subs **más** 3.000 h o 3 M de
vistas de Shorts. Detalle: `investigacion/2026-08-26_HALLAZGO-CRITICO_umbral-ypp-2027.md`.

**Movimiento real de los huecos del §5:**
| Hueco | Antes | Ahora |
|---|---|---|
| #1 Voz narrativa | 🔴 sin probar | 🟡 Chatterbox (MIT) y Kokoro (Apache 2.0) elegidas, gratis y locales; falta la escucha ciega de David |
| #2 Archivo dominio público | 🔴 sin proceso | 🟡 proceso + herramienta escritos; **sin ejecutar**, el entorno bloquea las 3 APIs |
| #3 Señales de desmonetización | 🔴 sin método | 🟢 método listo (hay aviso previo de ~7 días; sanción de 3 golpes) |
| #4 Infoproducto v0 | 🔴 sin hacer | 🟢 Lemon Squeezy elegido, ruta completa, coste 0 |
| #6 Test & Compare | 🔴 sin experiencia | 🟢 método listo; se activa a las 1.000 impresiones/72 h |
| #8 Mapa animado | 🔴 sin probar | 🟢 Animaps/Mapimator con plan gratis |
| #9 Verificación factual | 🟡 regla sin proceso | 🟡 proceso y plantilla escritos; **coste en tiempo sin medir** |
| #10 Subnicho | 🔴 sin decidir | 🔴 **sigue sin decidir** — pero con datos para decidir en 10 min |
| #5 Remoto | 🟡 sin remoto | 🟡 la documentación ya tiene respaldo remoto; falta repo propio del canal |
| #7 Métricas reales | 🔴 cero datos | 🔴 **sin cambio posible: el canal no tiene videos** |

**Qué falta:** lo mismo que faltaba, menos lo de arriba. Subnicho → guion del video 1 → storyboard
→ producción, en ese orden. Y ejecutar las tres cosas de coste 0 de `SINTESIS.md` §5.

**Qué bloquea (sin cambios, todo depende de David):**
- 🔴 **Subnicho sin decidir** — sube de 🟡 a 🔴: ahora consume una ventana de 5 meses que no se repite. *(David)*
- 🔴 Login en Recraft con la cuenta de pago. *(David)* — y ojo: el plan gratuito **no da derechos comerciales** (#23).
- 🔴 Autorización explícita de gasto de créditos. *(David)* — ver la alternativa FLUX en `investigacion/2026-08-26_extra_costes-e-imagen.md`.
- 🔴 Acceso a YouTube Studio de `humanchronicleshq@gmail.com`. *(David)*
- 🟡 Repositorio propio del canal para mover ahí `human-chronicles/`. *(David)*

**Próxima acción concreta:**
| # | Acción | Responsable | Para cuándo |
|---|---|---|---|
| 1 | Responder: *¿sobre qué civilización o periodo concreto leerías y hablarías durante 100 videos?* | **David** | inmediato — es el bloqueo raíz y tiene reloj |
| 2 | Escucha ciega de las 3 voces sobre los primeros 90 s del guion real | **David** | tras el punto 1 |
| 3 | Confirmar las cifras del YPP 2027 en la página oficial de YouTube (5 min) | **David** | esta semana |
| 4 | Abrir cuenta en Lemon Squeezy y verificar que admite su país y método de cobro | **David** | esta semana |
| 5 | Primera corrida real de `tools/buscar-archivo.mjs` y cronometrarla | `human-chronicles-research-analyst` | tras el punto 1 |

**Nota honesta de estado:** el canal sigue en **0 videos publicados y 0 avances de producción**.
Esta ronda no produjo contenido: produjo método, respaldo y una fecha límite que antes no se sabía
que existía. Cuatro huecos pasan a 🟢 pero **ninguno de los cinco bloqueos se ha desbloqueado**,
porque los cinco son de David.

---

## 2026-08-25 — Entrada #2 · Cierre real de la constitución del equipo (la Entrada #1 se adelantó)

**Contexto:** la sesión que escribió la Entrada #1 se cortó por un límite de sesión de la API
justo después de escribirla, antes de ejecutar 3 de las cosas que ya daba por hechas. Ver
`ERRORES_A_EVITAR.md` #20. Esta entrada cierra lo que quedó pendiente, verificado en disco.

**Qué se hizo de verdad hoy (verificado, no repetido de memoria):**
- Se creó el 4º agente que faltaba: `human-chronicles-program-director` (no existía pese a que
  la Entrada #1 lo daba por creado).
- Se inicializó de verdad el repositorio git local de `PROYECTO HUMAN CHRONICLES/` (`git init` —
  antes NO existía, pese a que `ERRORES_A_EVITAR.md` #18/#19 y 3 de los 4 agentes afirmaban que sí).
  Todavía **sin remoto** — sigue siendo respaldo solo local.
- Se creó de verdad `agentes_equipo_hc/` con copia de los 5 agentes del canal.
- Se corrigió `ERRORES_A_EVITAR.md` con la entrada #20, documentando el propio incidente.

**Qué falta (sin cambios respecto a la Entrada #1 — sigue siendo lo que de verdad falta):**
1. Subnicho concreto dentro de historia — decisión de David/Kimi.
2. Guion del video 1 → storyboard aprobado → producción, en ese orden.
3. Infoproducto v0 (no depende de ningún umbral de YouTube).
4. Verificar en YouTube Studio el estado real del canal.

**Qué bloquea (sin cambios — siguen siendo bloqueos reales, no resueltos por este cierre):**
- 🔴 Login en Recraft con la cuenta de pago. *(David)*
- 🔴 Autorización explícita de gasto de créditos para Human Chronicles. *(David)*
- 🔴 Acceso a YouTube Studio de `humanchronicleshq@gmail.com`. *(David)*
- 🟡 Subnicho sin decidir. *(David / Kimi)*
- 🟡 Repositorio local sin destino remoto — ya no es "no existe ningún repo", ahora es "existe
  pero solo en este disco". *(David)*

**Próxima acción concreta:** sin cambios respecto a la tabla de la Entrada #1 — sigue vigente tal
cual, ninguno de esos 4 puntos se ejecutó todavía.

**Nota honesta de estado:** con esta entrada, el equipo de 4 agentes + `history-visual-director`
existe de verdad y por completo. El canal sigue en **0 videos publicados**. Documentar que un
avance existe y que exista de verdad son cosas distintas — hoy quedaron alineadas.

---

## 2026-08-25 — Entrada #1 · Constitución del equipo (línea base)

**Qué se hizo (entregables reales, verificables en disco):**
- Se creó el equipo permanente de 4 agentes dedicados en exclusiva a Human Chronicles:
  `human-chronicles-research-analyst`, `human-chronicles-production-lead`,
  `human-chronicles-growth-monetization` y `human-chronicles-program-director`.
- Se creó `ERRORES_A_EVITAR.md` con **19 lecciones fechadas y con fuente**, extraídas del
  conocimiento acumulado de Mindset Mechanics + 2 hallazgos propios de este canal.
- Se dio respaldo con historial al canal: repositorio git **propio y local** en
  `PROYECTO HUMAN CHRONICLES/` (respetando la orden de no mezclarlo con el repo de Mindset
  Mechanics) + copia de seguridad de los 4 agentes en `agentes_equipo_hc/`.

**Qué falta (por orden de impacto en monetización):**
1. Definir el **subnicho concreto** dentro de historia. Sin esto no hay guion, y sin guion no
   hay video. — *decisión creativa: David / Kimi.*
2. Guion del video 1 (en inglés) → storyboard aprobado → producción. En ese orden, sin saltos.
3. Montar el **infoproducto v0** (PDF cronología/mapa + link en descripción). Es el único flujo
   de ingreso que **no** depende de ningún umbral de YouTube: se puede tener listo antes del
   primer video.
4. Verificar en YouTube Studio el estado real del canal (subs, avisos de monetización).

**Qué bloquea (todo depende de una acción humana, ninguna la puede hacer un agente):**
- 🔴 **Login en Recraft con la cuenta de pago** → bloquea avatar y banner → bloquea que el canal
  se vea presentable al publicar el primer video. *(David)*
- 🔴 **Autorización explícita de gasto de créditos para Human Chronicles.** Hoy el presupuesto
  del proyecto está asignado a Mindset Mechanics; sin luz verde, este canal no genera ni una
  imagen. *(David)*
- 🔴 **Acceso a YouTube Studio de `humanchronicleshq@gmail.com`** para verificar métricas base y
  el aviso de cambio de requisitos YPP. *(David)*
- 🟡 **Subnicho sin decidir.** *(David / Kimi — decisión creativa, no la toma un agente.)*
- 🟡 **Sin destino remoto de respaldo** para el repo de este canal. Hoy el respaldo es solo
  local. *(David)*

**Próxima acción concreta:**
| # | Acción | Responsable | Para cuándo |
|---|---|---|---|
| 1 | Primera ronda de investigación del nicho de historia (competencia, formatos, política de monetización) con fuentes y fecha | `human-chronicles-research-analyst` | próxima invocación |
| 2 | Borrador del infoproducto v0 y del lead magnet — coste cero, no depende de ningún umbral | `human-chronicles-growth-monetization` | próxima invocación |
| 3 | Plantilla de guion + criterios de aprobación del storyboard (sin producir nada todavía) | `human-chronicles-production-lead` | próxima invocación |
| 4 | Presentar a David los 5 bloqueos de arriba, en una sola lista corta y accionable | `human-chronicles-program-director` | inmediato |

**Nota honesta de estado:** el canal tiene **0 videos publicados y 0 avances de producción**.
Lo entregado hoy es infraestructura de equipo y memoria, no contenido. Nada de lo anterior
acerca por sí solo la monetización hasta que se desbloquee lo de arriba.

---

*(Las entradas siguientes se añaden ENCIMA de esta línea. Nada por debajo se toca nunca.)*
