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

---

## Proyecto paralelo: `canal/` — sistema multiagente de monetización

En `canal/` vive un **segundo proyecto, autocontenido y sin relación con el motor de
mini-apps**: el sistema de agentes que investiga, documenta y produce el canal de YouTube.
No comparten código ni contenido; están en el mismo repositorio solo mientras el canal no
tenga uno propio (`canal/base-conocimiento/05-decisiones/DECISIONES.md`, D-10).

- Puerta de entrada: `canal/README.md`. Tablero vivo: `canal/ESTADO.md`.
- Agentes: `.claude/agents/` — `jefe-monetizacion` (orquestador) y cuatro especialistas.
- Comandos: `/ronda-diaria` (lanza una ronda completa) y `/estado-canal` (foto rápida).
- **Si trabajas en `canal/`, usa Opus** (`/model opus`): es investigación y estrategia, no
  HTML plano. La regla de Sonnet por defecto aplica al motor de mini-apps, no a esto.
- No mezcles nunca contenido del canal dentro de `apps/` o `template/`, ni al revés.
