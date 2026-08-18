# Mini-Apps — contexto del proyecto

Motor de mini-apps educativas en HTML/CSS/JS puro (sin dependencias, sin build,
PWA instalable). Cada app final se publica en GitHub Pages y el link se entrega
a compradores de Hotmart.

## Estructura (no hace falta explorarla, está toda aquí)

```
template/           motor base — index.html, app.js, styles.css, sw.js, manifest.json, icons/
apps/<producto>/    copia del motor + content.json propio  <- lo único que cambia por app
tools/              scripts de apoyo (ver abajo)
docs/               guías de costos y de modelos gratuitos
serve.ps1           servidor local para previsualizar (Windows)
```

- `template/app.js` (10 KB) es el motor de render. **Solo se toca para cambiar el
  comportamiento de TODAS las apps.**
- `apps/*/content.json` es el contenido: capítulos, textos, checklists, quizzes.
  Es lo único que se redacta por producto.

## Formato de `content.json`

```json
{
  "meta": { "id": "slug", "title": "", "subtitle": "", "author": "",
            "themeColor": "#2D6CDF", "accentColor": "#00D9A5" },
  "chapters": [
    { "id": "intro", "title": "", "icon": "📘",
      "sections": [ { "type": "text", "heading": "", "body": "" } ] }
  ]
}
```

Tipos de sección soportados por el motor: `text`, `callout`, `checklist`, `quiz`.

## Comandos

```bash
node tools/new-app.mjs <carpeta> --titulo "Título" --color "#RRGGBB"   # crear app nueva
node tools/token-report.mjs                                            # ver gasto de tokens
node tools/router/listar-modelos-gratis.mjs                            # modelos gratis de OpenRouter
pwsh serve.ps1                                                         # previsualizar (Windows)
```

## Reglas de trabajo (ahorro de tokens)

1. **Nunca escribas a mano los archivos del motor al crear una app.** Usa
   `node tools/new-app.mjs`; copia todo y deja solo `content.json` pendiente.
2. `apps/*/content.json` puede pesar 20 KB: edita **secciones puntuales**, no el
   archivo completo.
3. No leas `template/app.js` ni `styles.css` salvo que el cambio sea al motor.
4. Si cambias `template/sw.js`, sube la versión del caché (`CACHE = '...-vN'`) o
   los usuarios seguirán viendo la versión vieja.
5. Idioma del proyecto y de las apps: **español**.

Detalles de costos y de modelos gratuitos: `docs/OPTIMIZACION-TOKENS.md` y
`docs/OPENROUTER-MODELOS-GRATIS.md`.
