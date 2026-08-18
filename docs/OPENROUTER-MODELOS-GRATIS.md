# Usar modelos gratuitos con Claude Code (OpenRouter)

> Nota: interpreté "ahmniroute" como **OpenRouter** (https://openrouter.ai), que es
> la pasarela que da acceso a decenas de modelos —varios gratuitos— con una sola API key.
> Si te referías a otro servicio, dímelo y adapto la configuración.

## Qué se logra

Claude Code sigue siendo el mismo programa (mismas herramientas, mismos comandos),
pero las peticiones se envían a un modelo gratuito en vez de a Claude. Se cambia de
uno a otro con un solo comando, así que puedes usar el modelo gratis para lo mecánico
y volver a Claude cuando necesites criterio.

| Comando | Qué usa | Costo |
|---|---|---|
| `claude` | Claude (Opus/Sonnet) | consume tus créditos |
| `ccr code` | modelo gratuito vía OpenRouter | $0 |

## Instalación (una sola vez)

**Requisito:** Node.js 18 o superior (https://nodejs.org).

1. Crea tu cuenta gratis en https://openrouter.ai y genera una API key en
   https://openrouter.ai/keys (empieza por `sk-or-v1-`).
2. Ejecuta el instalador desde la raíz del repo:

   **Windows (PowerShell):**
   ```powershell
   .\tools\router\setup-openrouter.ps1 -ApiKey "sk-or-v1-tu-key-aqui"
   ```

   **Mac / Linux:**
   ```bash
   bash tools/router/setup-openrouter.sh sk-or-v1-tu-key-aqui
   ```

Esto instala `claude-code-router` y escribe tu configuración en
`~/.claude-code-router/config.json` (fuera del repo, para que la key nunca se suba a GitHub).

## Uso diario

```bash
ccr code            # abre Claude Code con modelos gratuitos
```

Dentro de la sesión puedes cambiar de modelo cuando quieras:

```
/model openrouter,deepseek/deepseek-chat-v3-0324:free
/model openrouter,qwen/qwen3-coder:free
```

Para volver a Claude, sal y ejecuta `claude` normalmente.

## Qué modelo usar para qué

La configuración de `tools/router/config.ejemplo.json` ya enruta automáticamente:

| Situación | Modelo asignado |
|---|---|
| Trabajo general (`default`) | `deepseek/deepseek-chat-v3-0324:free` |
| Tareas de fondo, resúmenes (`background`) | `mistralai/mistral-small-3.2-24b-instruct:free` |
| Razonamiento profundo (`think`) | `deepseek/deepseek-r1-0528:free` |
| Contexto largo, +60k tokens (`longContext`) | `meta-llama/llama-3.3-70b-instruct:free` |

**Los IDs de los modelos gratuitos cambian seguido.** Antes de editar la configuración,
consulta la lista viva:

```bash
node tools/router/listar-modelos-gratis.mjs
```

Después edita `~/.claude-code-router/config.json` con los IDs que te devuelva.

## Límites honestos de los modelos gratuitos

- Tienen **cupo diario** (típicamente unas decenas de peticiones) y pueden saturarse
  en horas pico; si falla, reintenta o cambia de modelo.
- Son **claramente menos capaces** que Opus en tareas largas o de arquitectura. Se
  equivocan más con ediciones de archivos grandes y con instrucciones ambiguas.
- OpenRouter **usa las conversaciones de los modelos gratuitos para entrenamiento**.
  No metas ahí datos sensibles ni contenido de clientes que no puedas compartir.
- No hay soporte ni garantía: un modelo gratuito puede desaparecer sin aviso.

## Reparto recomendado para este proyecto

| Tarea | Con qué |
|---|---|
| Crear la carpeta de una app nueva | `node tools/new-app.mjs` (ni siquiera necesita IA) |
| Reformatear / traducir / limpiar JSON | modelo gratuito (`ccr code`) |
| Convertir un PDF en `content.json` | modelo gratuito para el primer borrador, Claude para pulir |
| Cambios en el motor (`template/app.js`) | Claude |
| Depurar algo que no funciona | Claude |
