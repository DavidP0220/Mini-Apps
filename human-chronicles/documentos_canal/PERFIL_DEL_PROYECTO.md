# Human Chronicles — Perfil completo del proyecto

**Escrito: 2026-08-26.** Documento central del canal: qué es, por qué existe, para qué existe,
qué habilidades ya se dominan aquí, y cuáles faltan por aprender.

Está escrito para dos lectores a la vez:
1. Cualquier sesión o agente que entre a trabajar en Human Chronicles y necesite el cuadro completo.
2. **Otro proyecto de Claude, en otro canal/nicho**, que quiera replicar este método desde cero.

Por eso cada sección marca explícitamente qué es **específico de Human Chronicles** y qué es
**método general reutilizable**.

> Regla previa a todo: los datos operativos de este archivo son un resumen. La **fuente única de
> verdad** del estado del canal es `ESTADO_CANAL.md`, y la del historial de decisiones es
> `TABLERO_MONETIZACION.md`. Si algo no coincide, mandan ellos. Ver `ERRORES_A_EVITAR.md` #4 y #20.

---

## 1. Nombre e identidad

| Campo | Valor |
|---|---|
| **Nombre del canal** | Human Chronicles |
| **Handle** | `@humanchronicles11` (único válido; `HumanChronicles18` y `@HumanChroniclesHQ` son datos viejos y **erróneos**) |
| **Cuenta Google** | `humanchronicleshq@gmail.com` — cuenta **nueva y aislada** |
| **Nicho** | Historia y civilizaciones |
| **Subnicho concreto** | 🔴 **SIN DECIDIR** — bloqueo activo, decisión creativa de David |
| **Idioma del contenido** | Inglés (audiencia EE.UU./UK/CA/AU) |
| **Idioma de la documentación interna** | Español (ver `../POLITICA_IDIOMAS.md`) |
| **Formato** | **Faceless**: narración + ilustración + mapas + archivo. **Sin personaje ni host** |
| **Estado real** | **0 videos publicados, 0 avances de producción.** Canal creado, avatar y banner sin subir |
| **Repositorio** | Git **local propio** dentro de `PROYECTO HUMAN CHRONICLES/`. **Sin remoto** |

**Específico de HC:** el nicho, el idioma, el formato faceless.
**Método general:** tener un `ESTADO_CANAL.md` con una tabla de "campo / valor / estado" donde
cada dato dice si está *confirmado*, *decidido* o *pendiente*. Elimina el 90% de las alucinaciones
de sesión.

---

## 2. El porqué — por qué existe este canal

### 2.1 Motivo primero: aislar el riesgo de cuenta

Human Chronicles no nació como "una idea de contenido más". Nació de un **riesgo real de negocio**:
varios canales convivían bajo cuentas de Google compartidas (`walterdpscpfcm@gmail.com`), y en
YouTube **un strike o una desmonetización en un canal puede arrastrar a los demás canales alojados
en la misma cuenta**. Todo el trabajo acumulado en Mindset Mechanics estaba expuesto a un fallo
que ni siquiera sería suyo.

La respuesta fue estructural, no cosmética: **cuenta de Google nueva, exclusiva y aislada**
(`humanchronicleshq@gmail.com`), con reglas duras derivadas (`ESTADO_CANAL.md` §1):
1. Verificar siempre el channel ID / cuenta activa antes de tocar YouTube Studio.
2. Nunca reutilizar tokens, sesiones ni `auth_state.json` entre canales.
3. Nunca abrir las dos cuentas en la misma sesión de navegador (ya hubo conflictos reales de
   pestaña de Chrome entre sesiones concurrentes — `ERRORES_A_EVITAR.md` #12).

Y una consecuencia documental: los canales **no se mezclan** (commit `4a54f45`). Lo único que cruza
entre proyectos son **habilidades y aprendizajes técnicos**, nunca contenido ni documentos.

### 2.2 Motivo segundo: diversificar el ingreso

Un solo canal es un solo punto de fallo económico. Un segundo canal en un **nicho distinto**
(historia vs. desarrollo personal), con **audiencia distinta** y **cuenta distinta**, reparte el
riesgo: un cambio de algoritmo o de política que golpee a uno no tiene por qué golpear al otro.

### 2.3 Motivo tercero: el formato faceless no depende de una cara

Mindset Mechanics depende de mantener un personaje animado idéntico escena tras escena — el punto
técnico más caro y más frágil de ese canal. Human Chronicles se diseñó a propósito **sin esa
dependencia**: menos regeneraciones, menos créditos por video, menos modos de fallo.

**Método general:** antes de abrir un canal nuevo, pregúntate qué riesgo del canal existente estás
eliminando. Si no elimina ninguno, es solo más trabajo.

---

## 3. El para qué — objetivos

### 3.1 Objetivo de negocio: monetizar

Misma cadena que Mindset Mechanics — **vistas → audiencia → infoproductos → AdSense** — pero con
palancas propias (`PLAYBOOK_MONETIZACION_HC.md`):

| Palanca | Umbral | Estado hoy |
|---|---|---|
| **Infoproductos** (PDF cronologías, mapas imprimibles, packs de lectura) | **Ninguno** — se puede hoy | 🔴 no existe |
| **YouTube Shopping** (merch temático: mapas, láminas) | 500 subs | pendiente |
| **YPP / AdSense** (RPM historia: **$5-$12**) | 1.000 subs + 4.000 h | pendiente |
| **Patrocinios** (educación, apps de idiomas, streaming documental) | tracción | pendiente |

Decisión estratégica derivada del dato de RPM: en este nicho **no se optimiza por volumen de
videos**, se optimiza por **duración retenida** — largos de 8-12 min que habilitan varios mid-rolls,
más Shorts de 30-50s como puerta de entrada de suscriptores. Mezcla: 2 largos + 3-4 Shorts por
semana, **jueves y domingo, nunca lunes**.

### 3.2 Objetivo de aprendizaje: validar que el método es replicable

Human Chronicles es el **segundo caso de prueba** de un método que se quiere usar en un tercer canal
y en un cuarto. La hipótesis a validar es concreta:

> Un canal de YouTube se puede llevar a monetización con un **equipo permanente de agentes
> especializados + un tablero de solo-append + un archivo de errores con fuente**, sin que el
> conocimiento se pierda entre sesiones ni se reinvente cada semana.

Si funciona aquí — en un canal sin historial, sin videos y en un nicho distinto — el método es
del método, no de la suerte de Mindset Mechanics. **Esta es la parte que le sirve a "otro proyecto
de Claude que se complementa".**

---

## 4. Habilidades ya aprendidas y aplicadas

### 4.A — Técnicas heredadas de Mindset Mechanics que SÍ aplican aquí

Todas con fuente en `ERRORES_A_EVITAR.md` (documento de solo append, 20 entradas fechadas).

| # | Habilidad | Qué significa en la práctica |
|---|---|---|
| #4 | **Verificar todo dato operativo contra la fuente real** | IDs de video, handle, subs, estado de monetización: nunca desde memoria ni desde un resumen de sesión. Precedente propio: el handle documentado estaba mal |
| #6 | **`git check-ignore -v <ruta>` al crear cualquier carpeta nueva** | Un `.gitignore` de lista blanca (`/*` + excepciones) ignora carpetas nuevas **sin error ni aviso**. Si el comando devuelve una línea, ese archivo NO se está respaldando |
| #7 | **Commit inmediato al cerrar un bloque; comprobar que no estás en `HEAD detached`** | Un commit en detached HEAD se pierde al cambiar de rama |
| #8 | **Decidir el destino de respaldo ANTES de generar el archivo pesado** | Recraft y VideoExpress borran los originales a los ~60 días. Git para lo ligero, destino externo para video/audio |
| #9 | **Verificar que el resultado de un paso automático es el que se pidió** (hash, duración, contenido), no solo que no hubo error | Los fallos silenciosos son los caros: un bot descargaba el clip anterior y lo guardaba con el nombre correcto |
| #10 | **Verificar el aspecto ANTES de mandar a animar** | Recraft V4.1 no tiene ningún 16:9 exacto: se genera 1344x768 y se recorta a 1344x756. VideoExpress solo anima 16:9 y 9:16 |
| #11 | **Los negativos van en `negative_prompt` real de la API, nunca como texto en el prompt positivo** | Un modelo de difusión no interpreta la negación: repetir "NO ears" refuerza el concepto |
| #12 | **API antes que automatización de navegador; nunca dos sesiones sobre la misma cuenta** | La Media Library es global de la cuenta: dos corridas simultáneas se roban renders en silencio |
| #14 | **Prohibido sostener un frame congelado más de 4 segundos** | Un video con 85,6% de imagen fija (474 de 554s) fue rechazado entero. Bloques de 45-60s se cubren con **3-5 sub-planos reales de 12-20s**, ángulos y transiciones distintas (banco de movimientos de `MANUAL_PRODUCCION.md` §3) |
| #15 | **Medir con `ffprobe` un caso real antes de planificar duraciones** | Se planificaron planos de 12s; 20 clips reales medidos no pasaron de **8,04s**. Planificar sobre el dato medido, no sobre lo que promete la herramienta |
| #2 | **Un QA automático NO es una aprobación final** | Un video pasó todo el checklist técnico y David lo rechazó completo. El checklist mide lo medible; no mide si se ve bien. Y se le enseña el render, no una descripción del render |
| #1 | **Un gate de presupuesto es un límite, no una sugerencia de eficiencia** | Se generaron 12 escenas donde estaban autorizadas 2: 204 créditos fuera de techo y todo el pipeline congelado |
| #3 | **Anunciar en el tablero antes de empezar una tarea larga** | Dos sesiones auditaron lo mismo en paralelo; una rama entera se descartó |
| #5 | **Toda escalación bloqueante se le dice a David directo y en corto** | Una decisión estuvo 2 días parada esperando en un archivo que nadie leía. Nada más de 24h sin recordárselo |
| #16 | **Al resubir o cambiar un video, revisar todo lo que apunte a él** | 3 Shorts con enlaces muertos en la descripción. Texto público solo se edita con confirmación de David |
| #17 | **La biblia de estilo se valida contra el material publicado real** | Se validó contra una imagen de prueba y todo lo generado con esa plantilla salió mal. **Corolario para HC: con 0 videos, el primer video DEFINE el canon** — hay que revisarlo con más cuidado que ningún otro |
| #20 | **Se ejecuta primero y se documenta después** | Una sesión escribió que ya existían el repo git y una carpeta de agentes; se cortó antes de crearlos. Documentación perfecta, ejecución inexistente. Al revés, una interrupción deja un hueco visible, nunca una mentira consistente |

**Todo el bloque 4.A es método general reutilizable.** Es, con diferencia, la parte más valiosa
para un canal nuevo: son errores ya pagados con créditos, tiempo y videos reprobados.

### 4.B — Decisiones y método propios de Human Chronicles

1. **Aislamiento de cuenta de Google como decisión de arquitectura** (§2.1). No es higiene: es
   contención de riesgo entre canales. *Método general.*
2. **Formato faceless sin personaje.** El ancla de marca no es una cara, son **tres capas fijas**:
   voz narrativa + paleta + estructura del video (`ESTILO_HUMAN_CHRONICLES.md` §2-§3).
   *Específico de HC en el detalle, general en el principio: todo canal necesita un ancla
   reconocible en 10 segundos; elige cuál es la tuya conscientemente.*
3. **Recraft con referencia de ESTILO, no de PERSONAJE.** Es el cambio conceptual más importante
   frente a Mindset Mechanics. Se crea **una imagen de referencia de estilo** (escena histórica
   tipo con paleta y tratamiento definitivos) que cumple el rol que `true_character_ref.jpg`
   cumple en el otro canal. Cada prompt describe el estilo explícitamente, **nunca** "same style
   as before". Ventaja operativa medible: sin exigencia de consistencia facial → menos
   regeneraciones → **menos créditos por video**. *Método general para cualquier canal faceless.*
4. **Nunca rostros IA fotorrealistas de personas históricas reales.** Si hay retrato de dominio
   público, se usa el real; si no, ilustración claramente estilizada. Evita a la vez el problema de
   semejanza sintética y las quejas de rigor histórico. *Específico del nicho, generalizable a
   cualquier canal que retrate personas reales.*
5. **Arquitectura de equipo: 4 agentes + 1 director + 1 director visual.**
   - `human-chronicles-research-analyst` — investigación de nicho, competencia y política.
   - `human-chronicles-production-lead` — guion, storyboard, criterios de aprobación.
   - `human-chronicles-growth-monetization` — infoproducto, lead magnet, crecimiento.
   - `human-chronicles-program-director` — audita a los otros tres y **es el único que escribe en el tablero**.
   - `history-visual-director` — banco de planos, ritmo, regla de los 4 segundos.
   *Método general: separar quien ejecuta de quien audita. El director no produce, verifica en disco.*
6. **Tablero de monetización de solo-append** (`TABLERO_MONETIZACION.md`): entradas nuevas
   **arriba**, nada se reescribe jamás, cada entrada obliga a *fecha · qué se hizo con entregable
   real · qué falta · qué bloquea · próxima acción con responsable y fecha*. Prohibido "estoy
   investigando" sin entregable. *Método general.*
7. **Archivo de errores de solo-append con campo `Estado:`.** Una entrada equivocada no se edita:
   se añade una nueva y la vieja pasa a `SUPERADA POR #N`. Resuelve el problema clásico de la
   memoria append-only pura (dos versiones del mismo hecho conviviendo y el agente adivinando cuál
   vale). *Método general — probablemente la mejor pieza de diseño de todo el sistema.*
8. **Tarea programada diaria** (`.claude/scheduled-tasks/human-chronicles-daily-push/SKILL.md`):
   cada día invoca al director, que audita, convoca al especialista que toque y escribe entrada
   nueva en el tablero. El canal avanza sin depender de que David se acuerde. *Método general.*
9. **Copia de respaldo de los agentes dentro del repo del canal** (`agentes_equipo_hc/`), porque
   `.claude/agents/` vive fuera de todo repositorio y está explícitamente ignorado. La fuente de
   verdad sigue siendo `.claude/agents/`. *Método general — hueco real que casi nadie ve.*
10. **Registro de procedencia obligatorio** (`sources_<video>.md` por video: clip, URL, licencia,
    fecha de descarga). Sirve para responder un reclamo de Content ID con evidencia **y** como
    señal de esfuerzo humano ante la política de contenido no auténtico. *Método general para
    cualquier canal que use material de terceros.*

### 4.C — Hallazgos de investigación de mercado propios

1. **Política de contenido no auténtico de YouTube** (vigente desde julio 2025, oleadas de
   desmonetización en 2026, renombrada desde "contenido repetitivo"). **No prohíbe los canales
   faceless ni la IA** — castiga el contenido de bajo esfuerzo y producido en masa: plantillas
   idénticas, stock reciclado, guiones leídos literalmente de una fuente. Frase operativa del
   proyecto: **"la consistencia importa; la clonación mata."**
2. **Declaración de contenido sintético** obligatoria desde enero de 2026 cuando el material IA
   pueda confundirse con real, y **la etiqueta no penaliza el alcance** (confirmado por YouTube).
   Ante la duda, declararlo.
3. **Las voces sintéticas de alta calidad SÍ son monetizables.** Las robóticas y monótonas son
   justo el marcador que dispara la revisión por contenido no auténtico.
4. **RPM del nicho historia/documental: $5-$12**, por debajo de Educación/Ciencia (~$10,22 mediano)
   y muy por debajo de finanzas — pero se compensa con watch time alto (varios mid-rolls por video).
5. **Geografía del ingreso:** tráfico de EE.UU./UK/CA/AU paga **3-5x** más que mercados en
   desarrollo. Es la razón por la que el canal es en inglés. Decisión tomada, no revertir.
6. **Umbrales:** YPP en 1.000 subs + 4.000 h; **YouTube Shopping desde 500 subs**. Aviso pendiente
   de verificar en Studio: las 4.000 h pasarían a 8.000 h el 1-feb-2027 para canales fuera del YPP.
7. **Fórmulas de título del nicho de historia** (distintas de las 6 de Mindset Mechanics): "la
   decisión que lo cambió todo", "lo que no te contaron", "comparación imposible", "cifra concreta
   e improbable", "reconstrucción", "el error catastrófico". Nombres propios concretos ganan a
   conceptos abstractos; un año o una cifra sube el CTR.
8. **Fuentes de archivo de dominio público verificadas:** Library of Congress, Internet Archive
   Moving Image Archive, AP Archive, Periscope Films, PublicDomainFootage, gobierno de EE.UU.
   (NASA/NARA/CDC). **Advertencia:** dominio público del video ≠ dominio público de todo su
   contenido (música, obra de arte, personas identificables). Verificar ítem por ítem.

---

## 5. Habilidades que faltan por aprender — huecos reales

Sección deliberadamente honesta. Nada de esto está resuelto; marcar "sin probar" es más útil que
fingir cobertura.

| # | Hueco | Estado | Por qué importa |
|---|---|---|---|
| 1 | **Voz narrativa sintética de calidad** | 🔴 **SIN PROBAR** — no se ha evaluado ni una sola herramienta de voz para este canal | Es *el ancla de marca* del canal (§4.B.2) y a la vez el marcador que dispara la revisión por contenido no auténtico. Es el hueco más grave: el activo más importante del canal es lo único que no se ha tocado. Falta: comparar 2-3 motores, definir el criterio de "alta calidad con variación real", y un método para verificar el resultado (¿se puede medir la monotonía, o solo escuchar?) |
| 2 | **Evaluar y filtrar archivo histórico de dominio público en volumen** | 🔴 **SIN PROCESO PROBADO** — solo existe una lista inicial de 6 fuentes | Verificar licencia ítem por ítem es viable para 5 clips y no escala a 2 videos/semana. Falta un proceso repetible de búsqueda → verificación de licencia → registro en `sources_<video>.md`, y saber cuánto tarda de verdad |
| 3 | **Detectar señales tempranas de riesgo de desmonetización** | 🔴 **SIN MÉTODO** | Hoy el único plan es el checklist previo de `ESTILO_HUMAN_CHRONICLES.md` §6. No hay forma de saber si YouTube ya está tratando al canal como "bajo esfuerzo" **antes** de que llegue el aviso. Falta investigar qué señales anticipan la revisión (caída de impresiones, alcance limitado sin explicación) y montar un chequeo periódico |
| 4 | **Producir el infoproducto v0 sin gastar créditos** | 🔴 **SIN HACER** | Es el **único** flujo de ingreso que no depende de ningún umbral y podría estar vivo antes del primer video. Falta: elegir formato (PDF cronología / mapa imprimible), producirlo con herramientas de coste cero, y montar la plataforma de entrega (Gumroad/Sellfy) + lead magnet + lista de correo |
| 5 | **Repositorio remoto de respaldo** | 🟡 **PARCIAL** — git local propio existe; **sin remoto** | Sobrevive a un borrado accidental, **no** a una pérdida de disco. Debe ir bajo la cuenta de Human Chronicles, nunca bajo la de Mindset Mechanics (regla de aislamiento). Falta acción de David (`ERRORES_A_EVITAR.md` #18) |
| 6 | **Test & Compare (A/B nativo de miniaturas de YouTube)** | 🔴 **SIN EXPERIENCIA** | No se ha usado nunca en ningún canal del proyecto. Sin tráfico no sirve de nada todavía, pero conviene tener el método listo para el momento en que haya volumen |
| 7 | **Métricas reales del canal** | 🔴 **SIN DATOS — cero** | El canal no tiene videos. Todo lo estratégico de §3 y §4.C es investigación externa, no medición propia. La primera revisión con datos propios es **a las 6-8 semanas del primer video**, no antes. Hasta entonces, ninguna decisión de este proyecto está validada empíricamente |
| 8 | **Mapa animado como formato** | 🔴 **SIN PROBAR** | `ESTILO_HUMAN_CHRONICLES.md` §3.3 lo lista como el plano estrella del nicho, pero no se ha producido ninguno ni se sabe con qué herramienta se hace ni cuánto cuesta |
| 9 | **Verificación factual a escala** | 🟡 **REGLA SIN PROCESO** | La regla (2 fuentes independientes por dato duro) está escrita; no hay proceso ni plantilla ni medición de cuánto tiempo añade por guion. En un canal de historia, un error visible en comentarios destruye la autoridad más rápido que nada |
| 10 | **Subnicho concreto** | 🔴 **SIN DECIDIR** | Bloqueo raíz: sin subnicho no hay guion, sin guion no hay video, sin video no hay nada de lo demás |

**Método general:** mantener esta tabla de huecos con estados honestos (🔴 sin probar / 🟡 parcial)
es tan importante como la lista de habilidades. Un equipo de agentes que no sabe lo que no sabe
inventa avances — es exactamente el fallo #20.

---

## 6. Qué es específico de Human Chronicles vs. qué es reutilizable

### Específico de este canal (NO copiar tal cual a otro nicho)
- Nicho de historia y civilizaciones; idioma inglés; audiencia EE.UU./UK/CA/AU.
- Paleta pergamino/sepia + tinta oscura + un color de acento; cartelas de nombre + año.
- Estructura de video: cold open / tesis / contexto / 3 actos / cierre, 8-12 min.
- Las 6 fórmulas de título del nicho de historia.
- El RPM de $5-$12 y las fuentes de archivo histórico de dominio público.
- La regla de no generar rostros IA de personas históricas reales.
- La decisión de optimizar por duración retenida en vez de por volumen.

### Método general reutilizable en cualquier canal nuevo
1. **`ESTADO_CANAL.md`** con estado explícito por dato (confirmado / decidido / pendiente) y la
   regla "si no está confirmado aquí, no está confirmado".
2. **`ERRORES_A_EVITAR.md` de solo append con campo `Estado:`** y fuente documental por entrada.
   Se lee entero antes de empezar cualquier trabajo.
3. **`TABLERO_MONETIZACION.md` de solo append**, entradas nuevas arriba, con entregable real,
   bloqueo con nombre de responsable y próxima acción fechada.
4. **Equipo de agentes con separación ejecutor / auditor**, donde solo el director escribe el tablero.
5. **Tarea programada diaria** que hace avanzar el canal sin depender de la memoria del humano.
6. **Aislamiento de cuenta por canal** (cuenta Google propia, tokens propios, sesión de navegador propia).
7. **Repositorio propio por canal**, más copia de respaldo de los agentes dentro de él.
8. **`git check-ignore -v` al crear cualquier carpeta nueva** que deba respaldarse.
9. **Ejecutar primero, documentar después.**
10. **Ancla de marca elegida conscientemente** (personaje, voz, paleta o estructura) y una imagen
    de referencia que la fije.
11. **QA técnico como necesario pero no suficiente**: la aprobación final es siempre del humano,
    viendo el render.
12. **Gates de presupuesto literales**: ni un crédito fuera del lote autorizado; ante la duda, parar
    y preguntar.
13. **Registro de procedencia por video** de todo el material de terceros.
14. **Medir con `ffprobe` antes de planificar** cualquier duración sobre una herramienta.
15. **Cumplimiento de la política de contenido no auténtico**: tesis original por video, sin
    plantilla repetida, fuentes citadas, voz de calidad, ritmo sostenible.

---

## 7. Mapa de documentos del canal

| Archivo | Para qué sirve | Se lee cuándo |
|---|---|---|
| `PERFIL_DEL_PROYECTO.md` (este) | Cuadro completo: porqué, para qué, habilidades y huecos | Al entrar por primera vez |
| `ESTADO_CANAL.md` | **Fuente única de verdad** de los datos del canal y los pendientes | Antes de usar cualquier dato |
| `ERRORES_A_EVITAR.md` | 20 lecciones fechadas con fuente | **Entero, antes de cualquier trabajo** |
| `TABLERO_MONETIZACION.md` | Marcador hacia YPP e historial de decisiones | Antes de empezar y al terminar |
| `ESTILO_HUMAN_CHRONICLES.md` | Biblia de voz, visual, fuentes de archivo y checklist de publicación | Al guionizar, producir o revisar |
| `PLAYBOOK_MONETIZACION_HC.md` | Estrategia de ingreso, títulos, métricas | Al planificar contenido o monetización |
| `agentes_equipo_hc/` | Copia de respaldo de los 5 agentes del canal | Si `.claude/agents/` se pierde |

---

*Última actualización: 2026-08-26. Este documento se actualiza; no es de solo append (para eso
están `ERRORES_A_EVITAR.md` y `TABLERO_MONETIZACION.md`).*
