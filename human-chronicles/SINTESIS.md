# Human Chronicles — Síntesis operativa

**Escrita: 2026-08-26.** Condensa los 30 documentos del paquete de conocimiento + la ronda 01 de
investigación. **Si solo vas a leer un archivo de este directorio, que sea este.**

Los documentos originales están íntegros en `documentos_canal/`, `agentes/`, `herencia_mindset_mechanics/`,
`memoria/` y `tarea_programada/`. Esto no los reemplaza: los indexa y les añade lo que faltaba.

> Leer los 39 documentos enteros cuesta **~71.000 tokens**. Este archivo cuesta ~3.000 y te deja
> saber qué sección concreta pedir después con `node human-chronicles/tools/hc.mjs ver <doc> <n>`.

---

## 1. Qué es esto en tres frases

Human Chronicles (`@humanchronicles11`) es un canal de YouTube de **historia y civilizaciones**, en
**inglés**, formato **faceless** (sin personaje ni host), operado por un equipo de agentes de Claude
con un único objetivo: **llegar a monetización**.

Existe por tres razones, en orden de peso: **aislar el riesgo de cuenta** (un strike en un canal
puede arrastrar a los demás canales de la misma cuenta de Google), **diversificar el ingreso**, y
**validar que el método es replicable** en un tercer y cuarto canal.

**Estado honesto: 0 videos publicados, 0 avances de producción.** Lo que existe es infraestructura
de método y memoria, no contenido.

## 2. El estado real, sin adornos

| Dato | Valor | Estado |
|---|---|---|
| Handle | `@humanchronicles11` | Confirmado (`HumanChronicles18` y `@HumanChroniclesHQ` son **erróneos**) |
| Cuenta Google | `humanchronicleshq@gmail.com` | Confirmada, **aislada** de las otras cuentas |
| Nicho / subnicho | Historia / **sin decidir** | 🔴 **Bloqueo raíz, ahora con fecha límite** |
| Videos publicados | 0 | — |
| Suscriptores | Sin dato medido | ⛔ Nunca verificado en Studio |
| Avatar y banner | No subidos | 🔴 Pendiente |
| Infoproducto | No existe | 🟢 Ejecutable hoy, coste 0 (§5) |
| Repositorio | Git local propio, **sin remoto** | 🟡 Parcialmente resuelto (§7) |
| Voz del canal | Ninguna herramienta probada | 🟡 Candidatas elegidas (§5) |

La **fuente única de verdad** sigue siendo `documentos_canal/ESTADO_CANAL.md`. Si un dato no está
confirmado ahí, no está confirmado.

## 3. 🔴 Lo que cambió con la ronda 01: el reloj

**El umbral de entrada al YPP se duplica el 1-feb-2027.**

| | Hasta el 31-ene-2027 | Desde el 1-feb-2027 |
|---|---|---|
| Suscriptores | 1.000 | 1.000 (igual) |
| Horas de reproducción | **4.000 h** | **8.000 h** |
| Vía Shorts (90 días) | 10 M vistas | **20 M vistas** |

**Los canales ya dentro del YPP quedan protegidos.** Hoy es 2026-08-26: quedan **~5 meses**.

Esto reordena todo. El subnicho sin decidir deja de ser "un bloqueo más" y pasa a ser **un bloqueo
que consume una ventana que no se repite**. Cada semana de retraso ahora vale el doble después.

**Corrección adicional:** YouTube Shopping no es "500 subs" a secas — es **500 subs Y** 3.000 h de
reproducción en el último año **o** 3 M de vistas de Shorts en 90 días. El
`PLAYBOOK_MONETIZACION_HC.md` §4 queda corregido en este punto.

Detalle y verificación: `investigacion/2026-08-26_HALLAZGO-CRITICO_umbral-ypp-2027.md`.

## 4. Las 6 decisiones ya tomadas que NO se revierten

1. **Inglés y audiencia EE.UU./UK/CA/AU.** Ese tráfico paga 3-5x más. Decidido y correcto.
2. **Optimizar por duración retenida, no por volumen.** RPM del nicho 5-12 $, compensado con watch
   time alto y varios mid-rolls. El reloj del §3 refuerza esto: los Shorts pasan a exigir 20 M de
   vistas, inalcanzable para un canal nuevo. **Las horas salen de los largos.**
3. **Mezcla:** 2 largos de 8-12 min + 3-4 Shorts/semana derivados de esos largos. **Jueves y
   domingo, nunca lunes.**
4. **Faceless sin personaje.** El ancla son tres capas: **voz narrativa + paleta + estructura**.
5. **Recraft con referencia de ESTILO, no de personaje.** Sin exigencia de consistencia facial →
   menos regeneraciones → menos créditos que el canal hermano.
6. **Nunca rostros IA fotorrealistas de personas históricas reales.** Si hay retrato de dominio
   público se usa el real; si no, ilustración claramente estilizada.

## 5. Qué se puede hacer HOY sin desbloquear nada

Los 5 bloqueos 🔴 del tablero dependen todos de David (login de Recraft, autorización de créditos,
acceso a Studio, subnicho, remoto). **Estas tres cosas no dependen de ninguno:**

| Acción | Coste | Cierra |
|---|---|---|
| **Probar la voz del canal** — Chatterbox (MIT) y Kokoro (Apache 2.0), locales y gratis, contra ElevenLabs como vara de medir. Escucha ciega de David sobre los primeros 90 s del guion real | 0 € | Hueco #1, el más grave |
| **Montar el infoproducto v0** — Lemon Squeezy (5% + 0,50 $, procesamiento incluido, **email gratis hasta 500 suscriptores**). Cronología PDF como lead magnet | 0 € | Hueco #4, el único ingreso sin umbral |
| **Producir un mapa animado de prueba** — Animaps (12 créditos/mes gratis) o Mapimator. Medirlo con `ffprobe` antes de planificar nada | 0 € | Hueco #8 |

**Gumroad queda descartado** (10% base, 30% vía Discover, sin email). Corrige el playbook §4.

## 6. Las reglas duras (las que cuestan dinero si se saltan)

Condensadas de las 20 entradas de `documentos_canal/ERRORES_A_EVITAR.md`. **Ese archivo se lee
entero antes de cualquier trabajo** — esto es un recordatorio, no un sustituto.

**De proceso:**
- **Ejecutar primero, documentar después.** Nunca al revés (#20).
- **Ni un crédito fuera del lote autorizado.** Un gate es un límite, no una sugerencia (#1).
- **El QA técnico no aprueba nada.** La aprobación es de David, **viendo el render**, no una
  descripción del render (#2).
- **Todo dato operativo se verifica contra la fuente real**, nunca desde memoria ni desde un
  resumen de sesión (#4).
- **Toda escalación bloqueante se le dice a David directo y en corto.** Nada más de 24 h (#5).
- Anunciar en el tablero antes de empezar una tarea larga (#3).

**De material:**
- `git check-ignore -v <ruta>` **al crear cualquier carpeta nueva** que deba respaldarse. Un
  `.gitignore` de lista blanca ignora carpetas nuevas sin avisar (#6).
- Commit al cerrar cada bloque; comprobar que no estás en `HEAD detached` (#7).
- Decidir el destino de respaldo **antes** de generar el archivo pesado. Recraft y VideoExpress
  borran los originales a los ~60 días (#8).

**De pipeline:**
- Verificar que un paso automático devolvió **lo que se pidió** (hash, duración), no solo que no
  falló. Los fallos silenciosos son los caros (#9).
- Verificar el **aspecto** antes de mandar a animar. 1080p mínimo siempre (#10).
- Los negativos van en `negative_prompt` real de la API, **nunca** como texto en el prompt positivo:
  un modelo de difusión no interpreta la negación, la refuerza (#11).
- API antes que automatización de navegador. Nunca dos sesiones sobre la misma cuenta (#12).
- **Medir con `ffprobe` un caso real** antes de planificar duraciones (#15).

**De contenido y monetización:**
- **Prohibido sostener un frame congelado más de 4 segundos.** Bloques de 45-60 s se cubren con
  3-5 sub-planos reales de 12-20 s (#14).
- Sin plantilla repetida entre videos. **"La consistencia importa; la clonación mata"** (#13).
- El primer video **define el canon** del canal. Revisarlo con más cuidado que ninguno (#17).
- Al resubir o cambiar un video, revisar todo lo que apunte a él (#16).

## 7. Lo que sigue faltando (honesto)

| # | Hueco | Antes | Ahora | Qué falta exactamente |
|---|---|---|---|---|
| 1 | Voz narrativa | 🔴 | 🟡 | La escucha ciega de David. Candidatas y protocolo listos |
| 2 | Archivo de dominio público a escala | 🔴 | 🟡 | Herramienta escrita, **nunca ejecutada** (el entorno remoto bloquea las 3 APIs). Falta la primera corrida local |
| 3 | Señales de desmonetización | 🔴 | 🟢 | Método listo. Inaplicable hasta tener videos |
| 4 | Infoproducto v0 | 🔴 | 🟢 | Plataforma elegida, ruta completa. Falta ejecutarla |
| 5 | Repositorio remoto | 🟡 | 🟡 | Este repo da respaldo remoto **de la documentación**. Ver aviso abajo |
| 6 | Test & Compare | 🔴 | 🟢 | Método listo. Se activa a las 1.000 impresiones/72 h |
| 7 | Métricas reales | 🔴 | 🔴 | **Sin cambio y sin arreglo posible: el canal no tiene videos.** Primera revisión con datos propios, 6-8 semanas tras el video 1 |
| 8 | Mapa animado | 🔴 | 🟢 | Herramientas con plan gratis identificadas. Falta producir uno |
| 9 | Verificación factual a escala | 🟡 | 🟡 | Proceso y plantilla escritos. **El coste en tiempo sigue sin medir** |
| 10 | Subnicho | 🔴 | 🔴 | **Sigue siendo de David.** Ya hay datos para decidir en 10 minutos (§8) |

> **⚠️ Aviso sobre el hueco #5 y el aislamiento de cuentas.** Este directorio vive en el repo
> `Mini-Apps`, que **no** está bajo la cuenta de Human Chronicles. La regla de aislamiento
> (`ESTADO_CANAL.md` §1, `ERRORES_A_EVITAR.md` #18) es sobre **cuentas de Google/YouTube**, no sobre
> GitHub, así que no hay riesgo de strike cruzado. Pero la regla de David de **no mezclar canales**
> sigue viva. Este directorio está construido para ser **portable**: es autocontenido y se puede
> mover entero a un repo propio de Human Chronicles el día que exista. **Recomendación: hazlo.**
> Mientras tanto, la documentación tiene respaldo remoto, que es más de lo que tenía.

## 8. La única pregunta que desbloquea todo

> **¿Sobre qué civilización o periodo concreto estarías dispuesto a leer y hablar durante 100 videos?**

Los datos dicen **civilizaciones antiguas** (Roma, Egipto, Mesopotamia): volumen de búsqueda **+40%
interanual**, encaja con la paleta sepia y las cartelas ya decididas, y —clave— para la Antigüedad
**no hay archivo fílmico que reclamar**, así que el problema de licencias casi desaparece. Además
los videos de historia siguen posicionando **3-5+ años**, así que el watch time se acumula en vez
de evaporarse: es lo que hace alcanzable la ventana de 5 meses del §3.

Pero el dato dice dónde hay demanda, no qué te interesa. **Si tu respuesta choca con el dato, manda
tu respuesta:** un canal de historia delata el desinterés en la voz y en el guion.

Argumento completo: `investigacion/2026-08-26_hueco-10_subnicho.md`.

## 9. Mapa de este directorio

| Ruta | Qué es | Cuándo se lee |
|---|---|---|
| `SINTESIS.md` (este) | El cuadro completo condensado | Al entrar |
| `documentos_canal/ESTADO_CANAL.md` | **Fuente única de verdad** | Antes de usar cualquier dato |
| `documentos_canal/ERRORES_A_EVITAR.md` | 20+ lecciones fechadas con fuente | **Entero, antes de cualquier trabajo** |
| `documentos_canal/TABLERO_MONETIZACION.md` | Marcador e historial de decisiones (solo append) | Al empezar y al terminar |
| `documentos_canal/ESTILO_HUMAN_CHRONICLES.md` | Biblia de voz, visual y checklist de publicación | Al guionizar o producir |
| `documentos_canal/PLAYBOOK_MONETIZACION_HC.md` | Estrategia de ingreso, títulos, métricas | Al planificar |
| `documentos_canal/PERFIL_DEL_PROYECTO.md` | El porqué, el para qué, habilidades y huecos | Primera vez |
| `investigacion/` | Rondas de investigación fechadas, con fuentes | Al retomar un hueco |
| `agentes/` | Los 9 agentes (5 exclusivos + 4 multicanal) | Al invocar al equipo |
| `herencia_mindset_mechanics/` | Pipeline heredado (§3 = banco de movimientos de cámara) | Al producir |
| `tools/hc.mjs` | Lector selectivo (ahorro de tokens) | Siempre |
| `tools/buscar-archivo.mjs` | Búsqueda de dominio público + `sources_<video>.md` | Al reunir material |

## 10. Qué de esto sirve para OTRO canal

El 80% del valor es método, no nicho. Reutilizable tal cual:

1. **`ESTADO_CANAL.md`** con estado explícito por dato (confirmado / decidido / pendiente).
2. **`ERRORES_A_EVITAR.md` de solo append con campo `Estado:`** — una entrada equivocada no se
   edita, se añade otra y la vieja pasa a `SUPERADA POR #N`. Es la mejor pieza de diseño del sistema.
3. **Tablero de solo append**, entradas nuevas arriba, con entregable real y próxima acción fechada.
   Prohibido "estoy investigando" sin entregable.
4. **Equipo de agentes con separación ejecutor / auditor.** Solo el director escribe el tablero, y
   verifica en disco antes de dar algo por hecho.
5. **Tarea programada diaria** para que el canal avance sin depender de la memoria del humano.
6. **Aislamiento de cuenta por canal** y repositorio propio por canal.
7. **Ejecutar primero, documentar después.**
8. **Ancla de marca elegida conscientemente** y fijada con una referencia.
9. **Gates de presupuesto literales.**
10. **Registro de procedencia por video** de todo el material de terceros.

**No copiar tal cual:** el nicho de historia, el inglés, la paleta sepia, la estructura de 8-12 min,
las 6 fórmulas de título, el RPM de 5-12 $, la regla de no generar rostros históricos.

---

*Se actualiza (no es de solo append — para eso están `ERRORES_A_EVITAR.md` y el tablero).*
