# Revisión técnica diaria — 2026-08-25

**Autor: Claude Code (rutina técnica automática) · Alcance: 100% técnico (código, errores, arquitectura). Marketing/crecimiento lo cubre otra rutina.**

---

## 0. Qué se revisó

- `git log -20`, `git status`, estado de ramas.
- Todos los handoffs y reportes de `handoffs/` (el plan activo es `HANDOFF_2026-08-25_decision_tercera_via_resiliencia.md`).
- Código de `video_express_ai/`, `recraft_ai/`, `youtube_pipeline/`, `shorts_final/`.
- Los cuatro `.gitignore` (raíz + por módulo) y los tres `requirements.txt`.
- Búsqueda de eventos de error (`image_error`, `poll_timeout`, `download_error`) en logs JSONL.
- Búsqueda de secretos hardcodeados en `.py`, `.md`, `.sh`, `.json`, `.yaml`.
- Investigación web con fecha actual (agosto 2026) sobre arquitectura de pipelines con agentes, rate limits, secretos y respaldo de assets generados por IA.

**Estado general: sano en lo importante, con un fallo silencioso serio ya corregido (ver 1.1) y varias decisiones pendientes que no me corresponden ejecutar.**

---

## 1. Arreglado en esta sesión (código + commit + push)

### 1.1 Pérdida silenciosa de imágenes, videos y telemetría D6 — CRÍTICO

**Síntoma:** no existe ni un solo `logs/generation_log_*.jsonl` en el repo, pese a que el handoff de Kimi declara la telemetría D6 **obligatoria en cada generación**.

**Causa raíz:** `video_express_bot.py` y `recraft_client.py` definían sus destinos así:

```python
OUTPUT_DIR = Path(os.getenv("OUTPUT_DIR", "outputs"))
LOG_DIR    = Path(os.getenv("LOG_DIR", "logs"))
```

Una ruta relativa se resuelve contra el **directorio de trabajo**, no contra el módulo. Lanzando cualquier script desde la raíz del repo (que es exactamente donde arranca una sesión de Claude Code), todo caía en `<raíz>/outputs` y `<raíz>/logs`. Y el `.gitignore` raíz es una **lista blanca** (`/*` seguido de excepciones): esas dos carpetas no están en la lista, así que git las ignora **en silencio**.

Resultado: los archivos se escribían a disco y nunca entraban en git. Combinado con que Recraft y VideoExpress borran el original a los 60 días, esto es exactamente el escenario que la política "nunca perder nada" quiere evitar. No hay error, no hay aviso: simplemente el `git add` no ve nada.

**Fix:** anclar las rutas por defecto a la carpeta del módulo (`Path(__file__).resolve().parent`), manteniendo la prioridad de las variables de entorno (si son absolutas, mandan ellas).

**Verificación:** ejecutado con `cwd` = raíz del repo →

```
OUTPUT_DIR: /home/user/mindset-mechanics/video_express_ai/outputs   (antes: <raíz>/outputs, ignorado)
LOG_DIR   : /home/user/mindset-mechanics/video_express_ai/logs      (antes: <raíz>/logs, ignorado)
```

y un evento de prueba escrito con `_log_generation_event()` cae ya en ruta trackeada por git. Con `RECRAFT_OUTPUT_DIR=/tmp/absoluto`, la env var sigue ganando.

> **Ojo, David/Kimi:** si en la máquina de David hay `outputs/`/`logs/` sueltos en la raíz de la carpeta del proyecto con material generado, **eso es material real que nunca se subió**. Vale la pena mirar antes de que pase de 60 días.

### 1.2 `_check_aspect_ratio()` roto fuera de la máquina de David

**Síntoma:** la validación de proporción 16:9 revienta en cualquier equipo que no sea el portátil de David.

**Causa raíz:** `FFPROBE` estaba clavado a la ruta absoluta de la instalación WinGet de un equipo concreto (`C:\Users\David Peñuela\AppData\...\ffprobe.exe`). En cualquier otro sitio, `subprocess.run()` lanza `FileNotFoundError` sin capturar. Y aun encontrándolo, si ffprobe fallaba (archivo corrupto, formato raro) el `returncode` no se miraba: `stdout` vacío reventaba abajo con un `not enough values to unpack` que no dice nada de la causa real.

**Fix:** `FFPROBE = os.getenv("FFPROBE") or shutil.which("ffprobe") or "ffprobe"`, más chequeo de `returncode`/salida vacía y mensajes de error que dicen qué pasó.

**Verificación:** en un entorno sin ffmpeg instalado devuelve ahora
`VideoExpressError: No se encontro ffprobe ('ffprobe'). Instala ffmpeg o apunta la variable de entorno FFPROBE al ejecutable.` — antes, un traceback opaco.

### 1.3 `RECRAFT_API_KEY no esta configurada` engañoso

**Causa raíz:** `generate_scene.py` llamaba a `load_dotenv()` sin argumentos; python-dotenv busca el `.env` desde el cwd hacia arriba, así que lanzando el CLI desde la raíz del repo **no encontraba `recraft_ai/.env`** y el error decía que faltaba la clave cuando la clave sí existía.

**Fix:** `load_dotenv(Path(__file__).resolve().parent / ".env")`.

### 1.4 Dependencias faltantes en `requirements.txt`

- `video_express_ai/requirements.txt` no listaba **Pillow**, que importan `_render_subtitle_pngs.py` y `_make_long_badge.py`. Instalación limpia → `ModuleNotFoundError`.
- `youtube_pipeline/requirements.txt` no listaba **replicate**, que importa `generar_animacion.py`. Añadido como `replicate>=1.0` (sin pin fijo: no hay versión validada en el proyecto todavía; el resto del archivo sí está pinneado y conviene fijarlo cuando se pruebe).

### 1.5 Recraft: rate limits y telemetría a prueba de fallos

Tres problemas en `recraft_client.generate_image()`, los tres con el mismo patrón: **la telemetría iba acoplada a llamadas de red opcionales, así que un fallo de red borraba el rastro de un crédito ya gastado.**

- Un 429 (rate limit) abortaba la generación sin más. Ahora hay reintento con backoff (`Retry-After` si Recraft lo manda, si no 5/15/45s). **Solo se reintentan los 429**, nunca los 5xx: un 429 es rechazo puro sin consumo, pero un 5xx pudo haberse ejecutado del lado de Recraft y reintentarlo cobraría la imagen dos veces.
- `get_credits()` fallando (429, corte de red) tumbaba la generación entera antes de empezar, o la dejaba **sin registrar después de haber gastado el crédito**. El balance es telemetría, no trabajo: ahora degrada a `None` y sigue.
- Si la descarga de la imagen fallaba, se perdía la línea de log **y** la URL de Recraft, que es temporal. Ahora se registra un evento `download_error` con la URL antes de propagar el error.

**Verificación:** simulado con mocks — dos 429 seguidos + `/users/me` caído → 3 intentos de POST, imagen descargada, y el JSONL con dos eventos `rate_limited` y el evento `image` completo (`credits_*` a `null` en vez de perderse todo).

### 1.6 Repo en HEAD detached

El repo llegó en `HEAD detached` sobre `origin/main` y con `main` local dos commits atrás. Reposicionado en `main` siguiendo a `origin/main`. Sin pérdida de trabajo (árbol limpio). Si esto se repite en las sesiones remotas, avisad: un commit hecho en detached HEAD **se pierde** al cambiar de rama.

---

## 2. Contraste con lo que funciona mejor hoy (investigación, agosto 2026)

| Tema | Estado del proyecto | Qué se recomienda hoy | Veredicto |
|---|---|---|---|
| **Choques entre sesiones/agentes** | Ya resuelto de la mejor manera posible: el commit `3c7b38b` cambió Recraft de automatización de navegador a **API real**. Eso elimina la pestaña de Chrome compartida y con ella la condición de carrera. | El consenso de 2026 es exactamente ese: las sesiones concurrentes no comparten estado ni se coordinan solas; lo que no se pisa es lo que no comparte recurso. El límite práctico son 2-3 sesiones concurrentes por proyecto. | ✅ **El proyecto va por delante aquí.** Queda VideoExpress, que sigue por Playwright — pero con perfil de navegador propio, no el Chrome del usuario, así que no choca. |
| **Rate limits** | No había ningún manejo de 429 en Recraft. | Backoff exponencial honrando `Retry-After`; nunca reintentar operaciones que puedan cobrar dos veces. | ⚠️ **Arreglado hoy** (1.5). |
| **Secretos / API keys** | `.env` por módulo, en `.gitignore`, `.env.example` sin valores, y el cliente documenta que la clave nunca se commitea. Escaneo de secretos hardcodeados: **limpio, cero hallazgos**. | La higiene básica está bien para local. La recomendación 2026 va más allá: claves de vida corta con permisos mínimos, rotación y auditoría, porque una clave de larga vida en `.env` es exactamente lo que un agente puede leer y usar fuera de contexto (caso Railway, abril 2026: un agente borró una BD de producción con un token de larga vida que encontró en un archivo no relacionado). | ✅ Correcto para el tamaño actual. Ver propuesta 3.3. |
| **Respaldo antes de los 60 días** | Decisión ya tomada (Drive, commit `2e5b332`) y política de trackear `outputs/` en git (`dd51e02`). **Pero el bug 1.1 hacía que la política no se cumpliera en la práctica**, y los `.mp4` siguen bloqueados globalmente. | Git para assets ligeros; objetos grandes a almacenamiento externo (S3/Drive) o Git LFS. Recraft permite exportar los assets desde la cuenta; borra cuentas inactivas 12+ meses avisando 7 días antes por email. | ⚠️ Política correcta, ejecución rota hasta hoy. Ver propuesta 3.1. |
| **Arquitectura de pipeline** | Etapas separadas, telemetría JSONL por generación, gates de presupuesto explícitos, QA humano obligatorio antes de escalar. | Es el patrón recomendado: pipeline por defecto, barrera solo cuando una etapa necesita todos los resultados previos; presupuesto acotado; revisión humana proporcional a la capacidad real de revisar. | ✅ **Bien diseñado.** El gate de piloto de la 3ª vía es literalmente la buena práctica. |

---

## 3. Para decidir David o Kimi — NO ejecutado

### 3.1 Los `.mp4` siguen sin respaldo (implica dinero / proceso)

El `.gitignore` raíz bloquea `*.mp4` globalmente. Es correcto (GitHub corta en 100MB), pero significa que **los videos finales no están respaldados en ningún sitio versionado**. La decisión de Drive existe desde el commit `2e5b332` pero no veo evidencia en el repo de que se haya ejecutado.

Opciones, de menor a mayor coste:
1. **Drive manual/rclone** — coste cero o casi, ya decidido, solo falta hacerlo y dejar constancia en un reporte.
2. **Git LFS** — versionado real junto al código, pero la cuota gratuita de GitHub son 1GB de storage y 1GB/mes de ancho de banda; con video se agota rápido y pasa a ser de pago.
3. **S3/R2** — lo más barato a escala, pero es infraestructura nueva que mantener.

**Recomiendo la 1.** Es la ya decidida y no añade nada que mantener. Lo que hace falta es ejecutarla y verificar que los archivos están arriba, no volver a discutirla.

### 3.2 `anthropic==0.40.0` está muy desactualizado (cambio de dependencia con breaking changes)

`youtube_pipeline/requirements.txt` pinnea el SDK de Anthropic en 0.40.0, mientras `pipeline/stages/script_writer.py` llama a `model="claude-sonnet-5"`. El ID del modelo es una cadena que se pasa tal cual a la API, así que **probablemente sigue funcionando** — no es un fallo activo. Pero el SDK ya va por la serie 1.x, con cambios que rompen (`httpx2`, Python ≥3.10, parámetros deprecados eliminados), y quedarse en 0.40.0 deja fuera todo lo posterior: `output_config.effort`, thinking adaptativo, structured outputs, compaction.

**No lo toco yo**: subir un major de una dependencia sin poder ejecutar el pipeline completo (requiere claves reales y gasta créditos de Gemini/ElevenLabs) es exactamente lo que no debe hacer una rutina desatendida. Además, `max_tokens=8192` en `script_writer.py` es conservador para lo que da hoy Sonnet 5 — subirlo es decisión de coste, no técnica.

**Propuesta:** hacerlo en una sesión con David presente, con una corrida de guion de prueba antes y después.

### 3.3 Higiene de secretos: suficiente hoy, revisar si crece

No hay nada que arreglar ahora mismo (escaneo limpio). Dos cosas a tener en el radar, ninguna urgente:

- La `RECRAFT_API_KEY` es de larga vida y sin ámbito reducido. Si algún día el proyecto añade credenciales con poder destructivo (borrar en Drive, publicar en YouTube con permisos amplios), conviene separarlas por entorno antes, no después.
- El `.gitignore` raíz tiene reglas muy amplias: `*token*`, `*secret*`, `*credentials*`, `*api_key*`. Son buenas como red de seguridad, pero **se tragan en silencio cualquier archivo legítimo cuyo nombre las contenga** — p.ej. un futuro `tokens_usage.json` de telemetría desaparecería sin aviso, igual que pasó con los logs en 1.1. No las cambio unilateralmente porque son reglas de seguridad; solo dejo constancia del filo.

### 3.4 Deuda técnica: los scripts `_*.py` no son reproducibles

`_assemble_visual_track.py`, `_final_assembly.py`, `_transcribe_voiceover.py` y `_render_subtitle_pngs.py` tienen rutas absolutas de la máquina de David clavadas en el código (`C:\Users\David Peñuela\Documents\CLAUDE AUTOMATIC\...`). Como scripts de un solo uso es defendible, pero **el ensamblaje final del video depende de ellos** y hoy solo corren en un equipo.

No los toco: parametrizarlos sin poder ejecutar el ensamblaje real es cambiar código de producción a ciegas. **Propuesta:** cuando toque el ensamblaje del piloto de la 3ª vía, promover `_final_assembly.py` a script parametrizado (argumentos en vez de constantes) y dejar el resto como está.

### 3.5 Verificar si la telemetría D6 llegó a correr alguna vez

Cero `generation_log_*.jsonl` en el repo. Con el bug 1.1 arreglado, la próxima generación ya debería dejar rastro. Pero conviene saber cuál de los dos casos es:

- **(a)** se generó material y los logs quedaron en la carpeta ignorada de la raíz → recuperables, y probablemente haya imágenes ahí también;
- **(b)** no se ha corrido nada desde que se implementó D6 → nada que recuperar.

Solo David puede mirar su disco. Si es (a), **hay material generado sin respaldar** y es lo más urgente de esta lista.

---

## 4. Resumen ejecutivo

- **Arreglado y pusheado:** pérdida silenciosa de assets y telemetría por rutas relativas contra un `.gitignore` de lista blanca (lo más serio); `ffprobe` clavado a una máquina; `.env` no encontrado según desde dónde se lance; dos dependencias faltantes; manejo de 429 y telemetría a prueba de fallos en Recraft.
- **Sano:** arquitectura del pipeline, gates de presupuesto, política de QA humano, higiene de secretos, y el pivot de Recraft a API real (que es la mejor práctica de 2026 para evitar choques entre agentes concurrentes, adoptada antes de esta revisión).
- **Decide otro:** ejecutar el respaldo de `.mp4` en Drive (3.1) y comprobar si hay material huérfano en carpetas ignoradas (3.5) — esas dos son las que corren contra el reloj de los 60 días. El resto puede esperar.

---

### Fuentes de la investigación

- [Parallel Agentic Development: Running Multiple Claude Code Sessions](https://www.mindstudio.ai/blog/parallel-agentic-development-claude-code-worktrees)
- [How to Run Multiple Claude Code Agents in Parallel (2026)](https://www.superbuilder.sh/blog/run-multiple-claude-code-agents-parallel)
- [Claude Code Workflows: Deterministic Multi-Agent Orchestration](https://alexop.dev/posts/claude-code-workflows-deterministic-orchestration/)
- [Secrets Management for Agent-Driven Pipelines — Augment Code](https://www.augmentcode.com/guides/secrets-management-agent-pipelines)
- [How to manage API keys, tokens, and secrets for AI agents — WorkOS](https://workos.com/blog/ai-agent-secrets-management)
- [Your coding agent can read your .env file — Bitwarden](https://bitwarden.com/blog/secure-ai-agent-access-with-secrets-manager/)
- [Recraft — Terms of Service (retención y exportación de assets)](https://www.recraft.ai/legal/terms)
- [Recraft API](https://www.recraft.ai/api)
- [Git LFS for Large Files: Setup, Migration & Best Practices 2026](https://khimananda.com/blog/git-lfs-for-large-files)
- [Cloud Storage for Development Teams: Git LFS, S3, and Artifacts](https://sesamedisk.com/cloud-storage-development-teams-git-lfs-s3-artifacts/)
