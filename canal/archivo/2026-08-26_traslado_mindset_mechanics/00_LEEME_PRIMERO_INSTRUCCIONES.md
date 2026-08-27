# Paquete de traslado — Proyecto Mindset Mechanics
**Generado: 2026-08-26 · De: sesión Claude Code local (David) → Para: nueva cuenta Claude Max**

Este paquete contiene **toda la información** del proyecto para que puedas seguir trabajando en él
desde una cuenta/sesión de Claude distinta, sin perder nada de lo hecho hasta hoy. Léelo completo
antes de tocar nada.

---

## 0. Qué es este proyecto, en una frase

Automatizar la producción y el crecimiento del canal de YouTube **"Mindset Mechanics"** (nicho:
psicología evolutiva, host caricaturesco fijo) hasta monetizarlo — no es solo "hacer videos", el
objetivo incluye interacción de comunidad, marca personal y eventualmente venta de infoproductos.
**Todo el trabajo de contenido se comunica en español; el canal en sí se publica en inglés.**

## 0.bis Aviso: dentro del repo ya existe otro paquete de conocimiento previo

En `PROYECTO MECHANICS OPTIMIZACIONES/` hay carpetas `PAQUETE_CONOCIMIENTO_MINDSET_MECHANICS_2026-08-23`,
`_v2` y `_v3` — snapshots anteriores de este mismo tipo de paquete, hechos por sesiones previas.
**Ya están desactualizados** (el más reciente, v3, es del 2026-08-25 18:41; este paquete es del
2026-08-26 y el proyecto avanzó mucho ese día — ver §0.ter). Se dejaron **fuera de este zip a
propósito** (no por omisión: sus rutas anidadas superaban el límite de 260 caracteres de Windows y
rompían la compresión) porque siguen íntegros dentro del propio repo git — cualquier `git clone`
los trae. No hace falta copiarlos aparte.

## 0.ter Qué pasó el mismo día de este paquete (2026-08-26), para que no falte contexto

Mientras se armaba este paquete, otra sesión (probablemente Claude Code de David en paralelo, o
Kimi) siguió avanzando el proyecto en vivo: **el piloto de Resiliencia ya se animó**
(`handoffs/REPORTE_2026-08-25_piloto_animado.md`, `REPORTE_2026-08-25_duracion_resuelta.md`), hubo
investigación nueva de captación e interacción (`REPORTE_2026-08-26_captacion.md`,
`REPORTE_2026-08-26_interaccion.md`, `REPORTE_2026-08-26_storyboard.md`,
`INVESTIGACION_DIARIA_2026-08-26.md`) y una revisión técnica nueva
(`REVISION_TECNICA_2026-08-26.md`). Todo esto SÍ está incluido en este paquete (carpeta
`03_PUENTE_KIMI_CLAUDE_HANDOFFS/` y el bundle de `06_HISTORIAL_GIT_COMPLETO/`, que se generó
al final, en el commit más reciente al momento de entregar este zip). **Antes de seguir trabajando,
la nueva sesión debe leer estos handoffs de hoy — son más recientes que cualquier resumen que
David te dé de memoria.**

## 1. El dato más importante: esto es un repo git real con colaborador remoto

El proyecto vive en GitHub: `https://github.com/mechanicsmindset02-ai/mindset-mechanics` (repo
privado). Ahí colabora, además de Claude Code (ejecución técnica local), otra cuenta llamada
**"Kimi Code"** que hace de estratega/decisor de alto nivel, comunicándose exclusivamente **a
través de commits al repo**, en la carpeta `handoffs/`. Este es el "puente Kimi ↔ Claude Code".

**Protocolo del puente (ya definido y en uso, no lo reinventes):**
1. Al iniciar cualquier sesión de trabajo: `git pull`, y leer el archivo más reciente de
   `handoffs/` que empiece por `HANDOFF_` — ese es el plan activo. Si hay varios del mismo día,
   revisa `git log --reverse --name-status <rango> -- handoffs/` para ver el orden real (las
   fechas de archivo en disco NO son fiables tras un `git pull`, todas quedan con la fecha del
   pull).
2. Ejecutar ese plan por lotes. **Nunca contradecir un handoff de Kimi sin consultar** — las
   decisiones de alcance/estrategia/presupuesto son de Kimi, no del ejecutor técnico.
3. Al completar un lote o cerrar sesión: escribir `handoffs/REPORTE_YYYY-MM-DD_<tema>.md` (qué se
   hizo, bugs en formato síntoma→causa→fix→verificación, créditos/gasto consumido vs presupuesto,
   bloqueantes) y hacer `git add` + `git commit` + `git push`. Esto ya está pre-autorizado por
   David en el `CLAUDE.md` del repo — no hace falta pedirle permiso cada vez para ESTE tipo de
   commit/push (sí para gastar dinero real o tocar cuentas de terceros).
4. Nunca commitear archivos en `.gitignore` (ahí vive `kimi_token.txt` y similares).

**Gates activos que no se deben cruzar sin autorización de Kimi:** en este momento hay un
"gate de piloto" sobre el video de Resiliencia — nadie anima ni genera stills de la fase completa
del video hasta que Kimi/David den el veredicto sobre un piloto reducido. Lee
`03_PUENTE_KIMI_CLAUDE_HANDOFFS/` en orden cronológico (usa el bundle de `06_HISTORIAL_GIT_COMPLETO/`
para ver el orden exacto por commit) para saber el estado exacto de ese gate HOY.

## 2. Cómo restaurar el repo de trabajo en la máquina/cuenta nueva

El repo real y actualizado sigue viviendo en GitHub. Lo más simple:

```bash
git clone https://github.com/mechanicsmindset02-ai/mindset-mechanics.git
```

Este paquete además incluye, en `06_HISTORIAL_GIT_COMPLETO/`, un **bundle de git con el historial
completo** (`mindset-mechanics-historial-completo.bundle`, todos los commits y ramas, incluida una
rama de un worktree de agente que en su momento quedó sin fusionar) como respaldo por si el remoto
de GitHub no estuviera disponible o se perdiera el acceso a esa cuenta. Para restaurar desde el
bundle:

```bash
git clone mindset-mechanics-historial-completo.bundle mindset-mechanics
```

**Importante:** las carpetas `01_CODIGO_PIPELINE/`, `02_DOCUMENTOS_ESTRATEGIA_ESTILO/` y
`05_CONFIGURACION_REPO/` de este paquete son una **copia de solo lectura** del contenido ya
trackeado en git — están aquí para que puedas leer todo sin clonar nada primero. Para seguir
trabajando de verdad (commitear, pushear), usa el `git clone` de arriba, no estas copias sueltas.

## 3. Qué NO viene en este zip (y por qué, y dónde está)

**~1.3GB de video/audio/imágenes ya generados** (los videos largos y Shorts terminados, escenas de
Recraft, previews) se quedaron fuera del zip por tamaño — no son "información" que una sesión de
Claude necesite leer para poder seguir orquestando el proyecto, son activos de producción binarios.
**Nada se perdió ni se omitió silenciosamente**: el archivo `07_INVENTARIO_MEDIA_PESADA_NO_INCLUIDA.txt`
en la raíz de este paquete lista la ruta exacta y el tamaño de los 671 archivos. Siguen en el disco
de la máquina de David, en `C:\Users\David Peñuela\CLAUDE AUTOMATIC PC 3\CLAUDE AUTOMATIC\`. Si la
nueva cuenta/sesión corre en la MISMA máquina, todo sigue ahí sin hacer nada. Si corre en otra
máquina, hay que copiar esa carpeta física aparte (por tamaño, no cabe en un paquete de chat) —
David decide cómo (USB, red local, etc).

**Advertencia de riesgo ya reportada y sin resolver todavía:** varios de esos archivos (~669MB de
videos de Resiliencia + varios Shorts) no tienen respaldo en ningún otro lado (ni git, ni la nube) y
las plataformas que los generaron (Recraft, VideoExpress) borran los originales a los 60 días. Ver
`03_PUENTE_KIMI_CLAUDE_HANDOFFS/REPORTE_2026-08-25_revision_tecnica_y_mejoras.md`.

## 4. Estructura de este paquete

- `01_CODIGO_PIPELINE/` — todo el código: `video_express_ai/` (bot Playwright que automatiza
  VideoExpress.ai), `recraft_ai/` (cliente API de Recraft), `youtube_pipeline/`, `shorts_final/`,
  `storyboards/`.
- `02_DOCUMENTOS_ESTRATEGIA_ESTILO/` — playbooks de monetización/marca, biblia de estilo visual del
  canal, plan de escenas, diccionario visual, política de idiomas, guiones.
- `03_PUENTE_KIMI_CLAUDE_HANDOFFS/` — TODOS los handoffs y reportes intercambiados con Kimi hasta
  hoy. Esta es la memoria de las decisiones estratégicas tomadas — léela en orden cronológico real
  (usa el historial git, no la fecha de archivo).
- `04_MEMORIA_PERSISTENTE_CLAUDE/memoria_claude/` — la memoria persistente que esta sesión de Claude
  Code había acumulado sobre el usuario, sus preferencias y el proyecto (`MEMORY.md` + archivos
  individuales). Sirve como contexto de arranque para la nueva cuenta, pero **no se auto-carga**:
  si la nueva cuenta también es Claude Code con memoria persistente propia, hay que importar estos
  archivos a mano a su propio directorio de memoria (o usar la skill `import-memory` si está
  disponible). Incluye la regla explícita: "nunca mezclar contenido de Human Chronicles (canal
  aparte) dentro de este proyecto — solo se comparten habilidades técnicas y mejoras generales".
- `05_CONFIGURACION_REPO/` — `.gitignore` (es de lista blanca, revísalo antes de añadir carpetas
  nuevas o se ignoran en silencio), `.gitattributes`, los `CLAUDE.md` (instrucciones permanentes del
  repo y del módulo `video_express_ai`), `INDEX.md`.
- `06_HISTORIAL_GIT_COMPLETO/` — el bundle de git con el historial 100% completo (ver §2).
- `07_INVENTARIO_MEDIA_PESADA_NO_INCLUIDA.txt` — lista de los 671 archivos de media que se quedaron
  en la máquina local (ver §3).

## 5. Lo primero que debe hacer la nueva sesión de Claude

1. `git clone` del repo real (§2).
2. Leer, en orden, TODO `handoffs/` (o `03_PUENTE_KIMI_CLAUDE_HANDOFFS/` de este paquete) — es la
   fuente de verdad de qué se decidió y por qué.
3. Confirmar con David en qué estado sigue el gate de piloto de Resiliencia y si ya se cargó la API
   key de Recraft (`recraft_ai/.env`, con `RECRAFT_API_KEY` — a fecha de este paquete, NO estaba
   configurada, bloqueando el siguiente paso del pipeline).
4. Seguir el protocolo del puente (§1) desde ahí en adelante.

---
Este paquete fue generado a petición explícita de David para trasladar el proyecto completo a otra
cuenta Claude, sin omitir nada — incluido el trabajo del puente Kimi↔Claude.
