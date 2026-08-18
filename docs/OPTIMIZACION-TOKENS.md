# Optimización de tokens — diagnóstico y plan

Medido el 2026-08-18 sobre este mismo repositorio con `node tools/token-report.mjs`.

## 1. Cómo se están gastando hoy

Datos reales de una sesión de trabajo normal en este proyecto:

| Concepto | Tokens | Comentario |
|---|---:|---|
| Contexto base al abrir la sesión | **69.005** | antes de escribir una sola línea de código |
| Escritura de caché (contexto nuevo) | 165.029 | |
| Lectura de caché (contexto reusado) | 530.617 | 10x más barato que el nuevo |
| Salida (respuestas + razonamiento) | 10.178 | |
| **Costo aproximado (Opus)** | | **~$4,65 en 11 turnos** |

El detalle importante: **el proyecto entero pesa 100 KB (~25.000 tokens)**. O sea que
más de dos tercios de lo que se paga en cada turno **no es tu código**, es equipaje.

### De dónde salen esos 69.005 tokens de arranque

En la sesión se cargaron **547 herramientas**, de las cuales 509 vienen de conectores MCP:

| Conector | Herramientas |
|---|---:|
| Vani by Zoho | 149 |
| Adobe for creativity | 75 |
| github | 55 |
| vidIQ | 49 |
| TubeAlfred | 34 |
| Cloudinary | 30 |
| Notion | 28 |
| Gmail | 27 |
| Slack | 19 |
| Descript | 14 |
| Google Drive / Calendar | 20 |
| Zight, Vivideo, AC | 9 |
| (nativas de Claude Code) | 38 |

Para hacer una PWA en HTML/CSS/JS puro no se necesita ninguno de esos conectores.
Cada uno mete su nombre, su descripción y sus instrucciones de servidor en **cada turno**.

## 2. Las 6 acciones que más ahorran (en orden de impacto)

### 1) Desconectar los conectores MCP que no uses — ahorro estimado 40-70%
Es, de lejos, lo más rentable. En claude.ai → Configuración → Conectores, deja
activos solo los que uses en el proyecto actual. Para este repo basta con **github**
(y ni siquiera siempre).
Regla práctica: un conector que no vas a llamar en esta sesión, apágalo.

### 2) Usar modelos gratuitos para el trabajo mecánico — ahorro 100% en esos turnos
Copiar plantillas, renombrar, reformatear JSON, escribir CSS repetitivo: eso no
necesita Opus. Ver `docs/OPENROUTER-MODELOS-GRATIS.md`. Deja Claude para lo que
de verdad requiere criterio (arquitectura, depuración difícil, redacción del contenido).

### 3) Sesiones largas en vez de muchas cortas — ahorro ~30%
Cada sesión nueva vuelve a pagar los ~69.000 tokens de arranque a precio de
"escritura de caché" (1,25x). Reusar la misma sesión los cobra a precio de
"lectura de caché" (0,10x): **12 veces más barato**. No uses `/clear` por costumbre;
úsalo solo cuando cambies realmente de tema.

### 4) `CLAUDE.md` en el repo — ahorro ~10.000 tokens por sesión
Ya está creado en la raíz. Evita que Claude tenga que explorar la estructura del
proyecto con `ls`, `find` y lecturas de archivos cada vez que empieza.

### 5) No regenerar el motor en cada app — ahorro ~10.000 tokens por app
Antes, crear una app nueva significaba reescribir `index.html`, `app.js`,
`styles.css`, `sw.js` y `manifest.json` (~40 KB). Ahora:

```bash
node tools/new-app.mjs mi-producto --titulo "Mi Producto" --color "#E67E22"
```

El script copia el motor y deja solo `content.json` por redactar, que es lo único
que de verdad cambia entre una app y otra.

### 6) Permisos preaprobados — ahorro en turnos perdidos
`.claude/settings.json` ya trae una lista de comandos seguros permitidos
(`ls`, `cat`, `git status`, `node tools/*`…). Cada permiso que no se pregunta es
un turno completo que no se paga.

## 3. Reglas de trabajo (para ti y para Claude)

- Pide cambios concretos: "cambia el color del capítulo 3" cuesta mucho menos que
  "revisa la app y mejórala".
- Si un archivo es enorme (`content.json` de 21 KB), pide editar **una sección**,
  no el archivo entero.
- No pidas "lee todo el proyecto"; ya está resumido en `CLAUDE.md`.
- Cuando el contenido venga de un PDF, pega solo el capítulo que se va a convertir,
  no el documento completo.
- Antes de una tarea larga, pregúntate: ¿esto lo puede hacer un modelo gratis?

## 4. Medir el gasto tú mismo

```bash
node tools/token-report.mjs           # sesiones de este proyecto
node tools/token-report.mjs --all     # todos los proyectos
node tools/token-report.mjs --top 20  # top 20 turnos más caros
```

Lee las transcripciones locales de Claude Code (`~/.claude/projects/**/*.jsonl`);
no envía nada a ningún servidor. Fíjate sobre todo en **"Reuso de caché"**:
por debajo del 70% significa que estás reiniciando el contexto demasiado seguido.
