# Generador de Mini-Apps (motor)

Plantilla reutilizable: HTML/CSS/JS puro, sin dependencias, sin costo, instalable como app (PWA).

## Estructura

```
mini_apps_hotmart/
  template/          <- el motor (no tocar directamente)
    index.html
    styles.css
    app.js
    manifest.json
    sw.js
    content.json      <- contenido de EJEMPLO (ayuno intermitente)
    icons/
  apps/               <- aquí vive cada app final generada
```

## Flujo de trabajo (cada vez que tengas un documento nuevo)

1. Pásame el PDF/Word/TXT en el chat.
2. Yo extraigo y reestructuro el contenido en capítulos/secciones.
3. Copio `template/` a `apps/nombre-del-producto/` y genero un `content.json` nuevo con tu contenido (textos, checklists, quizzes).
4. Te muestro la app funcionando en el navegador para que la revises.
5. Cuando esté aprobada, la subimos a GitHub Pages (gratis) para tener un link público que puedes entregar a tus compradores de Hotmart.

## Publicar gratis en GitHub Pages (lo haces tú una sola vez)

1. Crea una cuenta gratuita en https://github.com (tú la creas, yo no puedo).
2. Crea un repositorio nuevo, por ejemplo `mis-mini-apps`.
3. Yo te ayudo a subir cada carpeta de `apps/` a ese repositorio (con tu autorización en cada push).
4. Activas GitHub Pages en la configuración del repo (Settings → Pages).
5. Cada app queda accesible en un link tipo:
   `https://tu-usuario.github.io/mis-mini-apps/nombre-del-producto/`
6. Ese link es el que entregas como acceso al comprar en Hotmart.

## Herramientas (ahorro de tokens)

```bash
# Crear una app nueva sin que la IA reescriba el motor (~10.000 tokens ahorrados por app)
node tools/new-app.mjs mi-producto --titulo "Mi Producto" --color "#E67E22"

# Ver cuántos tokens y cuánto dinero se está gastando realmente
node tools/token-report.mjs

# Ver qué modelos gratuitos ofrece OpenRouter hoy
node tools/router/listar-modelos-gratis.mjs
```

## Documentación

- `CLAUDE.md` — contexto del proyecto para la IA (evita que explore el repo en cada sesión).
- `docs/OPTIMIZACION-TOKENS.md` — diagnóstico del gasto y las 6 acciones que más ahorran.
- `docs/OPENROUTER-MODELOS-GRATIS.md` — cómo trabajar gratis con modelos de OpenRouter.

## Personalización rápida por producto

En `content.json` puedes ajustar sin tocar código:
- `meta.title`, `meta.subtitle`, `meta.themeColor`, `meta.accentColor`
- Capítulos y secciones (`text`, `callout`, `checklist`, `quiz`)

El progreso, el tema oscuro/claro y las respuestas del usuario se guardan automáticamente en su dispositivo (localStorage) — sin necesidad de servidor ni base de datos.
