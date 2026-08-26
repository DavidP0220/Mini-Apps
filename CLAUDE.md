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

Tipos de sección soportados por el motor: `text`, `callout`, `checklist`, `quiz`, `table`.

## Comandos

```bash
node tools/new-app.mjs <carpeta> --titulo "Título" --color "#RRGGBB"   # crear app nueva
node tools/content.mjs listar <app>                                    # índice de capítulos
node tools/content.mjs ver <app> <capituloId>                          # UN capítulo, no los 20 KB
node tools/content.mjs set <app> <capId> <n> --body "texto"            # editar una sección
node tools/sync-motor.mjs [--aplicar]                                  # propagar cambios del motor
node tools/token-report.mjs                                            # ver gasto de tokens
node tools/contar-herramientas.mjs                                     # herramientas cargadas
node tools/router/listar-modelos-gratis.mjs                            # modelos gratis de OpenRouter
pwsh serve.ps1                                                         # previsualizar (Windows)
```

## Modelo por defecto

Este proyecto usa **Sonnet** (`.claude/settings.json`). Es HTML/CSS/JS puro sin
dependencias: Sonnet basta y cuesta 5 veces menos. Cambia a Opus con `/model opus`
solo para arquitectura o depuración difícil, y vuelve con `/model sonnet`.

## Automatismos ya configurados

- **Hook**: leer `apps/*/content.json` entero queda bloqueado con un aviso que
  remite a `tools/content.mjs`. No es un recordatorio, es una barrera.
- **Línea de estado**: muestra modelo, contexto usado y costo de la sesión.
- **Comandos propios**: `/gasto` (reporte de consumo) y `/app-nueva` (crear app).
  Se editan en `.claude/commands/*.md`.

## Proyecto aparte: `forja/` (herramienta multimedia con IA)

`forja/` **no es una mini-app** y no usa el motor de `template/`. Es una herramienta propia de
generacion de video/imagen con IA (alternativa personal a Higgsfield.ai), tambien en HTML/CSS/JS
puro y sin dependencias, pero con su propia arquitectura.

- Antes de tocar nada ahi, lee **`forja/MEMORIA.md`** — es la memoria del proyecto: que se
  investigo, que se decidio (D-001 a D-011), y **que no esta verificado todavia**.
- Lo que falta esta en **`forja/PENDIENTES.md`**.
- Todo lo que sale a internet pasa por **`forja/app/js/proveedor.js`** y por nada mas. Esa capa
  unica es una decision explicita (D-003), no un detalle: es lo que permite cambiar de proveedor
  sin rehacer la herramienta. **No metas llamadas de red en otros archivos.**
- Los presets y los modelos son JSON editables (`forja/app/presets.json`, `modelos.json`). Anadir
  un preset o un modelo **no requiere tocar codigo**.
- Probar: `node forja/servir.mjs` y luego `node prueba-forja.mjs`.

## Reglas de trabajo (ahorro de tokens)

1. **Nunca escribas a mano los archivos del motor al crear una app.** Usa
   `node tools/new-app.mjs`; copia todo y deja solo `content.json` pendiente.
2. **Nunca leas `apps/*/content.json` entero** (20 KB ≈ 5.200 tokens). Usa
   `node tools/content.mjs listar/ver/set` para traer o cambiar solo un capítulo.
3. No leas `template/app.js` ni `styles.css` salvo que el cambio sea al motor.
4. Si cambias el motor en `template/`, propágalo con `node tools/sync-motor.mjs
   --aplicar` en vez de repetir la edición en cada app. Sube la versión del caché
   (`CACHE = '...-vN'`) o los usuarios seguirán viendo la versión vieja.
5. Idioma del proyecto y de las apps: **español**.

Detalles de costos y de modelos gratuitos: `docs/OPTIMIZACION-TOKENS.md` y
`docs/OPENROUTER-MODELOS-GRATIS.md`.
