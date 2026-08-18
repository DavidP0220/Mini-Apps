---
description: Crea una mini-app nueva a partir del motor (sin gastar tokens en copiar archivos)
argument-hint: <carpeta> "<Título>" [#color]
allowed-tools: Bash(node tools/new-app.mjs:*)
---

Crea una mini-app nueva con estos datos: $ARGUMENTS

Ejecuta `node tools/new-app.mjs` con la carpeta, `--titulo` y, si se indicó un
color, `--color`. No escribas a mano ningún archivo del motor: el script los copia.

Después, pregunta por el contenido (PDF, texto o capítulos) para redactar
`content.json`, y usa `node tools/content.mjs` para escribirlo por capítulos en
vez de generar el archivo completo de una sola vez.
