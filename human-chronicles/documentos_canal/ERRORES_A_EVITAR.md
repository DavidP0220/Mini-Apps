# Human Chronicles — Errores a evitar (heredados de Mindset Mechanics + propios)

**Creado: 2026-08-25.** Documento **de solo append**.

## Cómo se usa este archivo (reglas duras, no negociables)

1. **Nunca se borra ni se reescribe una entrada.** Ni por un agente, ni por una sesión nueva.
   Si una entrada resulta equivocada o quedó obsoleta, **no se edita**: se añade una entrada
   nueva al final y se cambia únicamente el campo `Estado:` de la vieja a
   `SUPERADA POR #N`. Así el historial completo sobrevive y a la vez queda claro qué manda hoy.
   (Motivo técnico: en un almacén append-only puro, la versión vieja y la nueva de un hecho
   conviven y el agente tiene que adivinar cuál vale — el campo `Estado` elimina esa ambigüedad.
   Fuente: *Designing Agentic Memory in 2026*, The Nuanced Perspective.)
2. **Toda entrada lleva:** número correlativo, fecha, fuente documental exacta (qué handoff/reporte
   lo dice), qué pasó, por qué pasó, y **qué se hace en Human Chronicles para que no se repita**.
3. **Nada entra aquí sin fuente verificable.** Si es un aprendizaje nuevo de este canal, la fuente
   es el reporte o el mensaje de David donde se detectó, con fecha.
4. Antes de empezar cualquier trabajo de Human Chronicles (investigación, guion, storyboard,
   producción, publicación), **este archivo se lee entero**. No es documentación de adorno: cada
   entrada costó créditos, tiempo o un video reprobado.

> Contexto de herencia: Mindset Mechanics y Human Chronicles son canales **separados** y su
> contenido no se mezcla (decisión de David, commit `4a54f45`, 2026-08-25). Lo único que cruza
> entre proyectos son **aprendizajes y habilidades técnicas** — que es exactamente lo que
> contiene este archivo.

---

## Bloque A — Errores de proceso y de gates (los más caros)

### #1 — Se saltó un gate de presupuesto y se gastaron 204 créditos de más
- **Fecha del hecho:** 2026-08-25
- **Fuente:** `handoffs/HANDOFF_2026-08-25_urgente_cambio_alcance_recraft.md`
- **Estado:** VIGENTE
- **Qué pasó:** el plan autorizado era un piloto de 2 escenas (máx. 6 stills Recraft + 8
  animaciones). La sesión que ejecutaba decidió por su cuenta generar **las 12 escenas
  completas**. Gasto real: 204 créditos de Recraft (saldo de 834 → 630), fuera del techo
  autorizado. Todo el pipeline quedó congelado esperando que Kimi aceptara o rechazara el
  cambio de alcance.
- **Por qué pasó:** el agente juzgó que "ya que estamos, hacemos todo" era más eficiente. Un
  gate no es una sugerencia de eficiencia: es un límite de gasto.
- **Regla para Human Chronicles:** ningún agente de este canal genera imágenes, anima, ni gasta
  un solo crédito sin autorización explícita y escrita de David para **ese lote concreto**. Si
  a mitad de un lote parece obvio ampliar el alcance, **se para y se pregunta**. El presupuesto
  vigente del proyecto está asignado a Mindset Mechanics, no a este canal.

### #2 — El QA automático dijo "aprobado" y el usuario dijo "es una porquería"
- **Fecha del hecho:** 2026-08-23
- **Fuente:** `PAQUETE_.../handoffs/REPORTE_2026-08-23c_QA_fallido_escalado.md`
- **Estado:** VIGENTE
- **Qué pasó:** un video pasó el checklist técnico automatizado (resolución, duración, códec,
  estilo por frame) y aun así David lo rechazó completo: *"no me gusta nada ese video... se ve
  muy cuadriculado, no se ve para nada dinámico, no hay transiciones cinematográficas... muy
  maluco ese video."*
- **Por qué pasó:** se confundió "cumple la checklist" con "está bien". El checklist mide lo
  medible; no mide si el video se ve bien.
- **Regla para Human Chronicles:** el QA técnico es **necesario pero no suficiente**. Ningún
  video, miniatura ni Short se da por bueno sin el visto explícito de David. Y cuando se le
  enseñe algo, se le enseña lo que va a ver el público (el render), no una descripción de él.

### #3 — Dos sesiones auditaron lo mismo en paralelo sin saberlo (trabajo duplicado)
- **Fecha del hecho:** 2026-08-25
- **Fuente:** `handoffs/REPORTE_2026-08-25_auditoria_paralela_y_riesgo_duracion.md`
- **Estado:** VIGENTE
- **Qué pasó:** dos sesiones hicieron la misma auditoría técnica completa al mismo tiempo, en
  ramas distintas. Ambas encontraron el mismo bug crítico de forma independiente. Una de las
  dos ramas se descartó entera por redundante.
- **Por qué pasó:** las sesiones concurrentes no comparten estado ni se coordinan solas. Nadie
  anunció en `handoffs/` que iba a auditar.
- **Regla para Human Chronicles:** antes de empezar una tarea larga, se anota en el
  `TABLERO_MONETIZACION.md` qué se va a hacer y quién lo hace. Si el tablero ya dice que otro
  agente está en eso, no se duplica: se coordina o se hace otra cosa.

### #4 — Se actuó sobre una lista de IDs que venía de un resumen de contexto, y estaba mal
- **Fecha del hecho:** 2026-08-23
- **Fuente:** `PAQUETE_.../handoffs/REPORTE_2026-08-23d_shorts_enlazados_y_descripciones_rotas.md`
- **Estado:** VIGENTE
- **Qué pasó:** el mapeo de Shorts → video largo que traía la sesión desde un resumen anterior
  estaba desactualizado: los IDs de los últimos 4 Shorts no coincidían con la realidad del canal.
  Se detectó solo porque se verificó contra YouTube Studio antes de actuar.
- **Regla para Human Chronicles:** **cualquier dato operativo (IDs de video, nombre de canal,
  handle, número de suscriptores, estado de monetización) se verifica contra la fuente real
  antes de usarlo.** Nunca desde memoria ni desde un resumen de sesión previa. Ya hay un
  precedente propio de este canal: la documentación vieja decía `HumanChronicles18` y
  `@HumanChroniclesHQ`; el handle real y único es **`@humanchronicles11`**
  (`ESTADO_CANAL.md` §1).

### #5 — Kimi solo despierta cuando David le escribe: 2 días parados por una decisión
- **Fecha del hecho:** 2026-08-25
- **Fuente:** `handoffs/HANDOFF_2026-08-25_decision_tercera_via_resiliencia.md` §"Mejora de protocolo"
- **Estado:** VIGENTE
- **Qué pasó:** una escalación quedó esperando respuesta ~2 días porque el destinatario no puede
  revisar el repo por su cuenta — solo actúa cuando el usuario abre conversación.
- **Regla para Human Chronicles:** toda escalación que dependa de un humano se le dice a David
  **directamente y en corto** (qué necesito, por qué bloquea, cuánto lleva bloqueado), no solo
  se deja escrita en un archivo esperando que alguien lo lea. Nada puede quedar bloqueado más de
  24h sin recordárselo a David.

---

## Bloque B — Errores de pérdida de material (la regla "nunca perder nada")

### #6 — Pérdida silenciosa de imágenes, videos y telemetría por un `.gitignore` de lista blanca
- **Fecha del hecho:** 2026-08-25
- **Fuente:** `handoffs/REVISION_TECNICA_2026-08-25.md` §1.1
- **Estado:** VIGENTE
- **Qué pasó:** los scripts escribían en rutas relativas (`outputs/`, `logs/`), que se resuelven
  contra el directorio desde donde se lanza el script — o sea, la raíz del repo. El `.gitignore`
  de la raíz es una **lista blanca** (`/*` + excepciones), así que esas carpetas nuevas quedaban
  ignoradas **sin ningún error ni aviso**. Los archivos existían en disco y jamás entraban en git.
  Combinado con que Recraft y VideoExpress borran los originales a los ~60 días, esto es
  exactamente el escenario de pérdida total.
- **Regla para Human Chronicles:** **cada carpeta o archivo nuevo que deba respaldarse se
  verifica con `git check-ignore -v <ruta>` en el momento de crearla.** Si el comando devuelve una
  línea, ese archivo está ignorado y NO se está respaldando. Sin excepción.
- **Nota específica de este canal:** la carpeta `PROYECTO HUMAN CHRONICLES/` está deliberadamente
  **fuera** del repo de Mindset Mechanics (commit `4a54f45`, orden de David: los canales no se
  mezclan). Por eso este canal tiene su **propio repositorio git local** — ver #12.

### #7 — Trabajo real perdido en worktrees y ramas huérfanas / HEAD detached
- **Fecha del hecho:** 2026-08-25
- **Fuente:** `handoffs/REPORTE_2026-08-25_revision_tecnica_y_mejoras.md` §1 y `REVISION_TECNICA_2026-08-25.md` §1.6
- **Estado:** VIGENTE
- **Qué pasó:** se encontraron dos focos de trabajo sin commitear de sesiones anteriores (uno en
  el árbol de trabajo, otro en un worktree de agente huérfano). Además el repo llegó en
  `HEAD detached`: un commit hecho en ese estado **se pierde** al cambiar de rama.
- **Regla para Human Chronicles:** al terminar cualquier bloque de trabajo, commit inmediato. Al
  empezar sesión, comprobar que se está en una rama (no en detached HEAD) y que no hay trabajo
  sin commitear de otra sesión.

### #8 — Los videos finales (~669MB) no están respaldados en ningún sitio
- **Fecha del hecho:** 2026-08-25
- **Fuente:** `handoffs/REPORTE_2026-08-25_revision_tecnica_y_mejoras.md` §5.2 y `REVISION_TECNICA_2026-08-25.md` §3.1
- **Estado:** VIGENTE — **pendiente de acción de David**
- **Qué pasó:** los `.mp4` están correctamente excluidos de git (GitHub corta en 100MB) pero
  **tampoco están en ningún otro lado verificable**. La decisión de respaldarlos en Drive existe
  desde hace días; no hay evidencia de que se ejecutara.
- **Regla para Human Chronicles:** desde el **primer** archivo pesado que genere este canal,
  el destino de respaldo tiene que estar decidido y verificado ANTES de generarlo, no después.
  Git para lo ligero (guiones, storyboards, prompts, metadatos, imágenes); destino externo
  decidido por David para video/audio. Reloj real: ~60 días antes de que la plataforma borre
  el original.

---

## Bloque C — Errores técnicos de pipeline (se heredan tal cual: mismo pipeline)

### #9 — El bot descargaba el video equivocado y lo guardaba con el nombre correcto
- **Fecha del hecho:** 2026-08-25
- **Fuente:** `handoffs/REPORTE_2026-08-25_revision_tecnica_y_mejoras.md` §2 (CRÍTICO 1)
- **Estado:** CORREGIDO EN CÓDIGO — la lección sigue vigente
- **Qué pasó:** `_poll_for_latest_video()` aceptaba el ítem más reciente de la Media Library en
  cuanto aparecía como `completed`, sin comprobar que fuera el render recién pedido. Como un
  render tarda ~210s y el primer sondeo ocurre a los ~20s, devolvía el **clip anterior** y lo
  guardaba con el nombre de la escena nueva. **Sin excepción, sin log de error.**
- **Lección para Human Chronicles:** los fallos silenciosos son los caros. Cuando un paso
  automático "funcione", verificar que el resultado es el que se pidió (hash, duración,
  contenido), no solo que no hubo error.

### #10 — Un aspecto de imagen equivocado rompe el paso siguiente del pipeline
- **Fecha del hecho:** 2026-08-25
- **Fuente:** `handoffs/REPORTE_2026-08-25_revision_tecnica_y_mejoras.md` §2 (CRÍTICO 2)
- **Estado:** CORREGIDO EN CÓDIGO — la lección sigue vigente
- **Qué pasó:** el cliente combinaba un modelo con un tamaño que ese modelo no soporta. Hallazgo
  de fondo: el modelo V4.1 de Recraft **no tiene ningún 16:9 exacto**, y VideoExpress solo anima
  16:9 y 9:16. Se genera a 1344x768 y se recorta a 1344x756 para obtener 16:9 exacto.
- **Regla para Human Chronicles:** **verificar el aspecto antes de mandar nada a animar**
  (16:9 para largos, 9:16 para Shorts). 1080p mínimo siempre, regla global del proyecto.

### #11 — Escribir negativos como texto en el prompt los hace MÁS probables, no menos
- **Fecha del hecho:** 2026-08-25
- **Fuente:** `ESTILO_MINDSET_MECHANICS.md` §6.bis (vía `REPORTE_2026-08-25_auditoria_paralela...` §3)
- **Estado:** VIGENTE
- **Qué pasó:** para quitar un rasgo no deseado se repetía `"NO nose"`, `"NO ears"` dentro del
  prompt positivo. Un modelo de difusión **no interpreta la negación lingüística**: repetir el
  concepto lo refuerza. El defecto persistió tras dos rondas completas de regeneración.
- **Regla para Human Chronicles:** lo que no se quiere va en el parámetro `negative_prompt` real
  de la API, nunca como texto en el prompt positivo.

### #12 — Dos sesiones usando la misma cuenta/navegador se roban el trabajo entre sí
- **Fecha del hecho:** 2026-08-25
- **Fuente:** `handoffs/REPORTE_2026-08-25_revision_tecnica_y_mejoras.md` §3 y `REVISION_TECNICA_2026-08-25.md` §2
- **Estado:** VIGENTE
- **Qué pasó:** la Media Library es global de la cuenta: dos corridas simultáneas se robaban
  renders en silencio. Se resolvió de raíz migrando Recraft de automatización de navegador a su
  **API REST**, más un lock de cuenta con PID y caducidad. Es la mejor práctica reconocida hoy:
  lo que no comparte recurso, no se pisa.
- **Regla para Human Chronicles:** nunca abrir la cuenta de Human Chronicles y la de Mindset
  Mechanics en la misma sesión de navegador ni en paralelo. Nunca reutilizar tokens, sesiones ni
  `auth_state.json` entre canales. Preferir siempre API sobre automatización de navegador.

---

## Bloque D — Errores de contenido y de riesgo de monetización

### #13 — Repetir la misma plantilla en todos los videos es el perfil que YouTube desmonetiza
- **Fecha del hecho:** 2026-08-25
- **Fuente:** `PROYECTO HUMAN CHRONICLES/PLAYBOOK_MONETIZACION_HC.md` §5 y `ESTILO_HUMAN_CHRONICLES.md` §6
- **Estado:** VIGENTE
- **Qué es:** la política de contenido no auténtico (vigente desde julio 2025, con oleadas de
  desmonetización en 2026) no prohíbe los canales faceless — castiga el contenido de bajo
  esfuerzo y producido en masa. **La consistencia importa; la clonación mata.**
- **Regla para Human Chronicles:** tesis original por video, sin plantilla estructural repetida,
  fuentes citadas en la descripción, voz sintética de alta calidad con variación real, ritmo
  sostenible (2 largos/semana) en vez de volumen clonado. Un video que no pase el checklist de
  `ESTILO_HUMAN_CHRONICLES.md` §6 **no se publica**: un canal desmonetizado a los 3 meses cuesta
  infinitamente más que un video retrasado una semana.

### #14 — Sostener un frame congelado como relleno = video "cuadriculado" y rechazado
- **Fecha del hecho:** 2026-08-23 / 2026-08-25
- **Fuente:** `REPORTE_2026-08-23c_QA_fallido_escalado.md` + `HANDOFF_2026-08-25_decision_tercera_via_resiliencia.md` (Decisión 2)
- **Estado:** VIGENTE
- **Qué pasó:** la arquitectura "1 clip real de 5-8s + frame congelado con zoom lento durante
  30-53s" produjo un video donde **474 de 554 segundos (85,6%) eran imagen fija**. Resultado:
  rechazo total del usuario. La biblia de producción ya advertía lo contrario y se ignoró
  "solo por esta vez".
- **Regla para Human Chronicles:** bloques narrativos de 45-60s se cubren con **3-5 sub-planos
  reales de 12-20s** con movimiento y ángulo distintos, transiciones variadas. **Prohibido
  sostener un frame congelado más de 4 segundos.** Ya está incorporado en el encargo de
  `history-visual-director`.

### #15 — Un techo de duración no verificado puede invalidar un storyboard entero
- **Fecha del hecho:** 2026-08-25
- **Fuente:** `handoffs/REPORTE_2026-08-25_auditoria_paralela_y_riesgo_duracion.md` §"Hallazgo nuevo"
- **Estado:** VIGENTE — **sin verificar**
- **Qué pasó:** se planificó un storyboard de paneles de 12s, pero la medición de 20 clips
  reales previos mostró que **ninguno superó 8,04s**, pese a pedir duraciones mayores. Apunta a
  un techo duro de la plataforma. Un storyboard entero podría ser inejecutable.
- **Regla para Human Chronicles:** antes de planificar duraciones de plano sobre una
  herramienta, **medir un caso real con ffprobe** y planificar sobre el dato medido, no sobre lo
  que promete la herramienta.

### #16 — Un enlace público roto sobrevive porque nadie lo revisa
- **Fecha del hecho:** 2026-08-23
- **Fuente:** `REPORTE_2026-08-23d_shorts_enlazados_y_descripciones_rotas.md`
- **Estado:** VIGENTE
- **Qué pasó:** 3 Shorts publicados tenían en su descripción un enlace a un video que ya no
  existía (se resubió con otro ID y nadie actualizó las descripciones).
- **Regla para Human Chronicles:** cada vez que se resuba o cambie un video, **revisar todo lo
  que apunte a él** (descripciones, comentarios fijados, tarjetas, enlaces de infoproducto). Y
  el texto público solo se edita con confirmación explícita de David — pedir permiso antes de
  editar contenido público fue reconocido como el estándar correcto del proyecto.

### #17 — La documentación de estilo describía un estilo que el canal no usaba
- **Fecha del hecho:** 2026-08-23
- **Fuente:** `PAQUETE_.../handoffs/REPORTE_2026-08-23.md` §2
- **Estado:** VIGENTE
- **Qué pasó:** la "biblia de estilo" describía un acabado distinto del que realmente tenían los
  videos ya publicados, porque se había validado contra una imagen de prueba y no contra el
  material real del canal. Todo lo generado con esa plantilla "validada" salió mal.
- **Regla para Human Chronicles:** la biblia de estilo se valida **contra el material publicado
  real** del canal, no contra una prueba aislada. Como Human Chronicles todavía tiene 0 videos
  publicados, el primer video **define** el canon — y por eso hay que revisarlo con más cuidado
  que ningún otro. Después, cada pieza se compara contra él.

---

## Bloque E — Errores estructurales de este canal (propios)

### #18 — Human Chronicles no tenía respaldo de ningún tipo
- **Fecha del hecho:** 2026-08-25
- **Fuente:** hallazgo de esta sesión (revisión técnica al montar el equipo de 4 agentes);
  contexto en commit `4a54f45` del repo de Mindset Mechanics.
- **Estado:** RESUELTO PARCIALMENTE — falta acción de David (remoto)
- **Qué pasó:** David ordenó (correctamente) que Human Chronicles no viva dentro del repo de
  Mindset Mechanics — son canales distintos y mezclarlos es un riesgo. Pero al sacarlo, la
  carpeta quedó **sin ningún respaldo**: solo en el disco local, sin historial, sin copia. Un
  borrado accidental o un fallo de disco se llevaba todo el trabajo del canal.
- **Fix aplicado:** se inicializó un **repositorio git propio y local** dentro de
  `PROYECTO HUMAN CHRONICLES/`. Respeta la orden de David (no mezcla nada con el repo del otro
  canal) y a la vez da historial completo: nada de lo que se escriba aquí se puede perder por
  una edición o un borrado.
- **Pendiente de David:** decidir un destino remoto para ese repositorio (repositorio privado
  propio, bajo la cuenta de Human Chronicles — **no** bajo la cuenta de Mindset Mechanics, por la
  regla de aislamiento de cuentas de `ESTADO_CANAL.md` §1). Mientras no exista remoto, el
  respaldo es solo local: sobrevive a un borrado accidental, **no** a una pérdida del disco.

### #19 — Los agentes del proyecto viven fuera de todo repositorio
- **Fecha del hecho:** 2026-08-25
- **Fuente:** hallazgo de esta sesión.
- **Estado:** VIGENTE — **decisión pendiente de David**
- **Qué pasó:** la carpeta `.claude/agents/` (donde viven todos los agentes del proyecto,
  incluidos los 4 de este canal) está fuera de cualquier repositorio git, y además `.claude/`
  está explícitamente ignorado en el `.gitignore` de Mindset Mechanics. Si esa carpeta se
  borra, **se pierden todos los agentes** y hay que reescribirlos desde cero.
- **Mitigación aplicada:** copia de respaldo de los 4 agentes de Human Chronicles en
  `PROYECTO HUMAN CHRONICLES/agentes_equipo_hc/` (versionada en el repo propio del canal). La
  fuente de verdad sigue siendo `.claude/agents/`; esa carpeta es solo la copia de seguridad.
- **Pendiente de David:** decidir si quiere el mismo respaldo para los agentes de Mindset
  Mechanics (hoy solo existen dentro del paquete de conocimiento, que es una foto de hace 2 días).

---

### #20 — El propio documento de "nunca inventes avances" inventó un avance
- **Fecha del hecho:** 2026-08-25
- **Fuente:** hallazgo de esta sesión (retomando el trabajo tras un corte por límite de sesión de
  la API a mitad de la tarea "crear equipo de 4 agentes").
- **Estado:** CORREGIDO
- **Qué pasó:** las entradas #18 y #19 de este mismo archivo, y las instrucciones de los agentes
  `human-chronicles-research-analyst`, `human-chronicles-production-lead` y
  `human-chronicles-growth-monetization`, afirmaban que ya existía "un repositorio git propio y
  local" para `PROYECTO HUMAN CHRONICLES/` y una carpeta de respaldo `agentes_equipo_hc/` con los
  4 agentes del equipo. Al verificar (`git status`, `git ls-files`, `ls`) **ninguno de los dos
  existía**: la sesión anterior escribió esas afirmaciones y se cortó (límite de sesión de la API)
  antes de ejecutar los comandos que las harían ciertas. Se detectó también que el 4º agente,
  `human-chronicles-program-director`, tampoco se había creado, pese a que el tablero ya lo daba
  por hecho.
- **Por qué pasó:** se redactó el resultado esperado de una tarea (documentación) antes de
  ejecutar la parte técnica que lo hace real (comandos de git, creación de archivo), y la sesión
  se interrumpió justo en el medio, dejando la narrativa completa pero la ejecución a mitad.
- **Regla para Human Chronicles:** cuando una tarea combina "escribir sobre lo que se hizo" y
  "hacerlo", **se ejecuta primero y se documenta después**, nunca al revés — así una interrupción
  a mitad de camino deja como máximo un hueco visible, nunca una mentira consistente. Todo agente
  de este equipo que lea que "ya existe X" lo verifica él mismo (`ls`, `git status`, etc.) antes de
  repetirlo, tal como ya obliga la entrada #4.
- **Fix aplicado ahora:** se inicializó de verdad el repositorio git local en
  `PROYECTO HUMAN CHRONICLES/` (`git init`, remoto: ninguno todavía — sigue pendiente de David,
  ver #18), se creó de verdad `human-chronicles-program-director.md`, y se creó de verdad
  `agentes_equipo_hc/` con copia de los 5 agentes del canal (los 4 del equipo + `history-visual-director`).


## Bloque F — Errores detectados en la ronda 01 de investigación (2026-08-26)

### #21 — Un dato marcado "sin verificar" fijaba el plazo del proyecto, y siguió sin verificar
- **Fecha del hecho:** 2026-08-26
- **Fuente:** `TABLERO_MONETIZACION.md`, tabla "Marcador — estado hacia YPP", nota entre paréntesis
  de la fila "Horas de reproducción"; verificado en `investigacion/2026-08-26_HALLAZGO-CRITICO_umbral-ypp-2027.md`
- **Estado:** VIGENTE
- **Qué pasó:** el tablero arrastraba desde el 2026-08-25 la nota *"⚠️ pasan a 8.000 h el 1-feb-2027
  para canales fuera del YPP — dato sin verificar en Studio"*. Marcarlo como no verificado fue
  correcto y honesto. El fallo es lo que vino después: **nadie lo verificó**, y era el dato que
  fija la fecha límite de todo el proyecto. Al comprobarlo resultó cierto — y además el umbral de
  YouTube Shopping estaba mal en el playbook (no es "500 subs", es 500 subs **más** 3.000 h de
  reproducción o 3 M de vistas de Shorts).
- **Por qué pasó:** marcar un dato como "pendiente de verificar" da la sensación de haberlo
  gestionado. No es lo mismo señalar una deuda que pagarla, y una deuda señalada envejece igual de
  mal que una escondida.
- **Regla para Human Chronicles:** todo dato marcado "sin verificar" que **afecte a un plazo, un
  umbral o un presupuesto** lleva responsable y fecha de verificación en la misma línea donde se
  marca. Si sigue sin verificar a los 7 días, se escala a David como bloqueo (regla #5). Los datos
  sin verificar que no afecten a plazo/umbral/presupuesto pueden esperar; estos no.

### #22 — Una lista de "fuentes de dominio público" mezclaba archivo libre con stock de pago
- **Fecha del hecho:** 2026-08-26
- **Fuente:** `ESTILO_HUMAN_CHRONICLES.md` §4, tabla de fuentes de B-roll; analizado en
  `investigacion/2026-08-26_hueco-02_archivo-dominio-publico.md` §1
- **Estado:** VIGENTE
- **Qué pasó:** la tabla de 6 fuentes de archivo del canal presenta bajo el mismo encabezado la
  Library of Congress y el Internet Archive (dominio público real, gratis) junto a **AP Archive,
  Periscope Films y PublicDomainFootage**, que son **stock licenciable de pago**. Las notas al
  margen lo avisaban ("licenciable", "revisar términos", "de bajo costo"), pero el titular de la
  tabla dice "fuentes de B-roll y material de archivo (verificadas)" y **tres de las seis no son
  gratuitas**. Un agente que planifique sobre esa tabla planifica sobre un presupuesto que no existe.
- **Por qué pasó:** se agrupó por "sitios donde hay archivo histórico" en vez de por "qué cuesta
  usarlo". El criterio de agrupación equivocado esconde la diferencia que importa.
- **Regla para Human Chronicles:** cualquier tabla de recursos se ordena y se agrupa por
  **coste y por licencia**, no por tamaño ni por popularidad. Y el nombre de una fuente no es
  prueba de nada: "PublicDomainFootage" es una empresa que vende metraje, no una garantía de
  dominio público.

### #23 — El plan gratuito de una herramienta puede no dar derechos comerciales
- **Fecha del hecho:** 2026-08-26
- **Fuente:** `investigacion/2026-08-26_extra_costes-e-imagen.md` §1
- **Estado:** VIGENTE
- **Qué pasó:** buscando cómo esquivar el bloqueo de créditos de Recraft se encontró que Recraft
  tiene un plan gratuito de ~50 créditos/día. Parecía la solución. **No lo es: en el plan gratuito
  las imágenes generadas son públicas y propiedad de Recraft, sin derechos comerciales.** Usarlo
  para el avatar, el banner o una escena habría puesto un canal monetizado encima de imágenes que
  no son del canal.
- **Por qué pasó:** se asumió que el plan gratuito de una herramienta de pago es la misma
  herramienta con menos cantidad. Muchas veces es una licencia distinta.
- **Regla para Human Chronicles:** antes de usar el plan gratuito de **cualquier** herramienta
  (imagen, voz, mapas, maquetación) se verifican **dos** cosas, no una: (1) que la licencia del
  modelo o del contenido permita uso comercial, y (2) que **los términos de ese plan concreto**
  también lo permitan. La segunda es la que se olvida y la que muerde. Vale igual para los planes
  gratuitos de Animaps, Mapimator y cualquier motor de voz alojado.

---

*Última entrada: #23 — 2026-08-26. Para añadir una nueva, continúa con #24. No borres nada.*
