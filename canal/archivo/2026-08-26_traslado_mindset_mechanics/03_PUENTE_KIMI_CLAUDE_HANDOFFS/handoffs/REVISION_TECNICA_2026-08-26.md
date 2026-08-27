# Revisión técnica diaria — 2026-08-26

**De:** rutina técnica automática (Claude Code, sesión remota programada)
**Para:** David y Kimi
**Alcance:** solo técnico (código, errores, arquitectura, buenas prácticas). Crecimiento y
monetización los cubre la otra rutina — aquí no se tocan.
**Créditos gastados: 0 Recraft / 0 VideoExpress.** No se generó ninguna imagen ni video.

---

## 0. Contexto de dónde corrió esto (importante para interpretar el alcance)

Esta rutina corre en un **contenedor remoto efímero con un clon limpio del repo**, no en la
máquina de David. Consecuencias directas:

- Solo se puede auditar **lo que está en git**. Nada de `outputs/` pesados, ni `.env`, ni la
  sesión de VideoExpress, ni los ~669MB de videos existen aquí.
- Por eso los puntos pendientes que dependen de la máquina de David (respaldo del material,
  saldo de la API de Recraft, YouTube Studio) siguen abiertos: **no se pueden ejecutar desde
  aquí, por diseño.** No es que se hayan ignorado.
- Ventaja del clon limpio: es el mejor detector de rutas clavadas a una máquina. De hecho así
  salió el hallazgo nº2 de abajo.

---

## 1. Estado del repo

- `origin/main` en `68070f1`, árbol de trabajo limpio, sin conflictos ni ramas colgando.
- Sin PRs abiertos.
- Los 20 commits recientes son coherentes: la auditoría del 25-ago (`2bd5b47`, `e31bd44`) cerró
  14 bugs, y encima de eso van docs de storyboard, investigación y la corrección de duración de
  VideoExpress (`dae5829`: el techo de 8s no existía, el rango real es 3-10s).
- Todos los `.py` compilan (Python 3.11).
- **Sin secretos en el código.** Barrido de `sk-`, `api_key=`, tokens: cero resultados. Las claves
  se leen de `.env` vía `os.getenv`, y los cuatro `.env` reales están correctamente ignorados
  (verificado con `git check-ignore`, no de vista).
- `video_express_ai/logs/generation_log_2026-08-25.jsonl`: **un solo evento, y es sano** —
  `kind: duration_investigation`, `credits_spent: 0`. Ningún `image_error`, ningún `poll_timeout`,
  ningún `rate_limited`, ningún `image_bad_response`. El pipeline no ha fallado; sencillamente
  lleva sin ejecutarse desde el 25 porque está bloqueado esperando el saldo de Recraft.

---

## 2. Lo que se arregló en esta sesión (commit `f4600a8`, ya en `origin/main`)

Cuatro hallazgos, todos técnicos y de bajo riesgo, todos verificados con una prueba que falla
antes del arreglo y pasa después.

### 2.1 CRÍTICO — el lock de cuenta no excluía nada (condición de carrera)

**Síntoma:** ninguno visible. Ese es el problema.

**Causa raíz:** `session.account_lock()` hacía `if LOCK_PATH.exists():` y después
`LOCK_PATH.write_text(...)`. Son **dos syscalls con una ventana en medio** (TOCTOU): N procesos
que arrancan a la vez ven todos "no existe", los N escriben el archivo, y los N entran. El
docstring del propio módulo dice *"claim por creación exclusiva de archivo"* — pero
`write_text()` no es exclusivo, siempre tiene éxito.

Ese lock se escribió el 25-ago justo para impedir que dos corridas simultáneas se robaran
renders entre sí, porque Media Library es **global de la cuenta**. O sea: **fallaba en silencio
exactamente en el caso para el que se creó.** Y el síntoma sería un clip mal etiquetado
descubierto semanas después en el montaje, no un error.

**Fix:** `os.open(LOCK_PATH, O_CREAT|O_EXCL|O_WRONLY)` — una sola syscall atómica que crea el
archivo *o* falla. El reclamo del lock huérfano también pasa por ahí, para que dos procesos que
detecten el mismo huérfano no se cuelen los dos.

**Verificación:** 12 procesos sincronizados con `multiprocessing.Barrier` (para forzar la ventana,
que con arranques escalonados casi nunca se abre), 15 rondas:

| | procesos dentro del lock a la vez |
|---|---|
| código viejo | **hasta 8 de 12** — el bug se reprodujo en 12 de 15 rondas |
| código nuevo | **1**, en las 15 rondas |

> Nota de riesgo real: hoy esto casi no se dispara, porque el pipeline lo corre una persona a la
> vez. Importa hacia adelante — en el momento en que haya dos sesiones/agentes en paralelo (que es
> justo la dirección en que va el proyecto), este bug corrompe resultados sin avisar.

### 2.2 Cinco scripts seguían clavados a la máquina de David

**Síntoma:** `FileNotFoundError` al correr cualquiera de ellos fuera del PC de David.

**Causa raíz:** la auditoría del 25-ago quitó ese patrón de `video_express_bot.py`,
`video_understand.py` y `_assemble_visual_track.py`, pero **se saltó cinco**:
`_transcribe_voiceover.py`, `_render_subtitle_pngs.py`, `_make_long_badge.py`,
`_final_assembly.py`, `_generate_resilience_batch.py`. Traían rutas
`C:\Users\David Peñuela\Documents\CLAUDE AUTOMATIC\...`, el `ffmpeg.exe` de una instalación
WinGet **con el número de versión dentro de la ruta**, y
`ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf")` sin alternativa.

Lo del ffmpeg merece subrayarse: esa ruta contiene `ffmpeg-9.0-full_build`. **Se habría roto en
la propia máquina de David con solo actualizar ffmpeg**, no hacía falta otro equipo.

**Fix:** nuevo `video_express_ai/_paths.py`, con el mismo patrón que ya usa el resto del repo
(anclado al repo + variable de entorno que manda + `shutil.which()` para binarios + lista de
fuentes con respaldo, igual que ya hacía `pipeline/stages/visuals.py`).

**La equivalencia se mantiene:** `_paths.py` vive en `<repo>/video_express_ai/`, así que
`REPO_ROOT` **es** `CLAUDE AUTOMATIC` en la máquina de David. Las rutas resueltas allí son
idénticas a las viejas. No cambia nada para él; solo deja de estar clavado.

**Verificación:** `_make_long_badge.py` corre de punta a punta en Linux (antes crasheaba en la
fuente). El PNG trackeado se restauró byte a byte — se comprobó por MD5 que el badge del canal
quedó intacto.

### 2.3 El `.gitignore` se tragaba en silencio las plantillas `.env.example`

**Causa raíz:** la regla `.env.*` (pensada para `.env.local`, `.env.produccion`) también captura
`.env.example`, que es **la única documentación de qué variables hay que configurar**.
`recraft_ai/.env.example` sobrevive de milagro: se trackeó antes de que existiera esa regla. Pero
cualquier plantilla nueva (`video_express_ai/.env.example`, `youtube_pipeline/.env.example`) se
habría ignorado sin aviso — el **mismo fallo silencioso que ya pasó con `storyboards/`** y que
está documentado en el propio `.gitignore`.

**Fix:** excepciones `!.env.example`, `!.env.template`, `!.env.sample`.

**Verificación:** las tres plantillas quedan visibles; los cuatro `.env` reales siguen ignorados.

### 2.4 `recraft_client` reventaba con un `Retry-After` en formato fecha

**Causa raíz:** `int(resp.headers.get("Retry-After"))` asume segundos, pero **RFC 9110 permite dos
formatos**: segundos, o fecha HTTP (`"Wed, 26 Aug 2026 15:04:05 GMT"`). Con la variante de fecha
saltaba `ValueError` **dentro del manejo del 429** — o sea, un rate limit que era perfectamente
recuperable tumbaba el lote entero.

**Fix:** `_retry_after_seconds()` parsea ambos formatos, cae al backoff exponencial si la cabecera
es basura, y acota a 5 min para que una cabecera absurda no deje el proceso dormido.

**Verificación:** 7 casos (segundos, fecha futura, fecha pasada, basura, ausente, absurda,
decimal). Los dos primeros reventaban antes.

---

## 3. Contraste con lo que se usa hoy (investigación, agosto 2026)

Se contrastó el estado del proyecto contra la práctica actual. Resumen honesto: **el proyecto está
razonablemente alineado**, y en un punto va por delante.

| Tema | Práctica actual (ago-2026) | Este proyecto |
|---|---|---|
| Aislamiento entre agentes concurrentes | git worktrees para agentes que escriben; los de solo lectura no lo necesitan | ✅ ya se usa (hubo un worktree huérfano rescatado el 25-ago) |
| Choque de navegador entre sesiones | Chrome bloquea el `user-data-dir` a nivel de proceso: dos instancias de Playwright **no pueden** compartir perfil. Playwright 1.59 añadió `browser.bind()` para sesiones aisladas sobre un navegador ya corriendo | ✅ el proyecto usa `storage_state` (`auth_state.json`), no `user-data-dir` — evita el choque de raíz. **Mejor decisión que la que se recomienda por defecto** |
| Colisión sobre `storageState` compartido | El fallo típico: dos flujos sobrescriben el mismo `.auth/user.json` en carrera | ⚠️ el proyecto tiene un solo rol y un solo `auth_state.json` — hoy no aplica, pero es la misma familia que el bug 2.1. El lock ya arreglado lo cubre |
| Rate limits | Auto-limitarse antes que comerse 429s y depender del backoff | ✅ throttle a 4 req/s (límite documentado 5/s), backoff con `Retry-After` — **ahora sí correcto** tras 2.4 |
| Reintentos | No reintentar operaciones que ya pudieron cobrar | ✅ ya hecho a conciencia: reintenta 429 (rechazo puro, no cobra) pero **no** 5xx (pudo ejecutarse del lado del proveedor). Está bien razonado |
| Secretos | Nunca hardcodear; `.env` + `.gitignore`; rotar si se filtra | ✅ correcto. Y ahora las plantillas se documentan sin filtrar valores (2.3) |
| Escalado de subagentes | Claude Code: hasta 20 concurrentes, 3 niveles de anidamiento | ℹ️ el proyecto no lo usa todavía; cuando lo haga, **2.1 era el bloqueante real** |

**Único desalineamiento de fondo:** todo el aislamiento de este proyecto vive en **un solo lock de
archivo local**. Es suficiente para una máquina. Si algún día se corre desde dos máquinas contra
la misma cuenta de VideoExpress, el lock no ve nada — y el modo de fallo vuelve a ser el
silencioso de 2.1. No hace falta hacer nada hoy; queda anotado.

---

## 4. Lo que NO se tocó, y por qué (decisiones de otros)

### 4.1 ⚠️ La premisa de los "60 días" no se pudo confirmar en fuentes públicas

Esto importa porque **es la justificación escrita de una decisión de arquitectura**: el
`.gitignore` y varios reportes dicen *"Recraft y VideoExpress borran el original a los 60 días"*, y
sobre esa frase se decidió trackear `outputs/` y `logs/` dentro de git.

Buscando hoy (ago-2026):

- Los **Términos de Recraft** no mencionan 60 días. Lo que dicen apunta en otra dirección:
  borran **cuentas inactivas 12+ meses**, con aviso por email 7 días antes, y los assets se pueden
  descargar en cualquier momento. Las imágenes creadas con suscripción de pago siguen siendo tuyas
  aunque canceles.
- De **VideoExpress.ai** no hay política de retención pública localizable.
- No se pudo abrir `recraft.ai` directamente desde este contenedor (bloqueado por el proxy de red),
  así que esto se basa en resultados de búsqueda, no en lectura de la fuente.

**No estoy diciendo que la política de respaldo esté mal** — respaldar material generado es
correcto pase lo que pase. Lo que digo es que **la urgencia declarada (60 días) no tiene fuente**,
y una decisión de arquitectura apoyada en un número inventado o mal recordado envejece mal.

→ **Para David:** cuando entres a Recraft, confirma la política real y la anotamos con fuente. Si
resulta ser 12 meses y no 60 días, la política de respaldo no cambia, pero sí cambia la prisa.

### 4.2 🔴 Riesgo confirmado: las 12 imágenes de Recraft ya pagadas no están en ningún lado del repo

Esto sí se pudo verificar desde aquí, y confirma lo que decía el reporte del 25-ago:

- `recraft_ai/outputs/` **no existe** en el repo. Las 12 imágenes de Resiliencia (**204 créditos
  ya gastados**) viven solo en el proyecto web de Recraft.
- 0 archivos `.mp4` en el repo (correcto: los bloquea el `.gitignore` por el límite de 100MB de
  GitHub) — pero eso significa que los ~669MB de video generado **no tienen respaldo verificable**.

Sea la retención de 60 días o de 12 meses, esto es material pagado que existe en un solo lugar y
ese lugar no lo controlamos.

→ **Para David:** decidir el destino de respaldo (¿OneDrive? ¿Drive?) y descargar las 12 imágenes
de Recraft. **No se puede hacer desde esta rutina**: no hay sesión de Recraft ni acceso a tus
discos desde el contenedor remoto. Es una tarea de tu máquina.

### 4.3 Decisiones que siguen abiertas de días anteriores (sin cambios, solo para que no se pierdan)

Ninguna es técnica, así que ninguna se ejecutó:

1. **Saldo de $5 de la API de Recraft, sin pagar.** Bloquea el piloto entero (7 stills nuevos).
   Es dinero real → decisión de David.
2. **V4.1 + recorte a 1344x756, o V3 @ 1820x1024 nativo** para los stills nuevos. V3 es el único
   que soporta `style_id` (el mecanismo oficial de consistencia de personaje), pero podría cambiar
   el look frente a las 12 escenas ya generadas con V4.1 → decisión creativa de Kimi.
3. **Verificar en YouTube Studio** si aparece el aviso del cambio de requisitos YPP → tarea de
   David (requiere su login).
4. **La burbuja de cómic de la escena 11** sigue sin resolver (fuera del piloto) → Kimi.
5. **`negative_prompt` sin verificar contra una generación real.** El cambio del 25-ago (sacar los
   negativos del prompt positivo y mandarlos por el parámetro real de la API) es correcto en
   teoría, pero **nadie lo ha visto funcionar** — depende del punto 1. Ojo con un detalle que sí
   está verificado en el código: `negative_prompt` **solo lo soportan V2/V3**. Si se elige V4.1 en
   el punto 2, ese arreglo no aplica y los negativos hay que redactarlos dentro del prompt.
   **Los puntos 2 y 5 están acoplados** — conviene decidirlos juntos.

---

## 5. Veredicto

**El pipeline está sano.** Cero errores en la telemetría, cero secretos filtrados, todo compila,
la auditoría del 25-ago se sostiene bien. Lo que había era **deuda silenciosa**: un lock que no
bloqueaba, cinco scripts que solo corrían en un PC, una regla de `.gitignore` que se comía las
plantillas y un parser de cabecera que reventaba en un caso legal del RFC. Los cuatro quedaron
arreglados y verificados con pruebas reproducibles.

**El proyecto no está bloqueado por nada técnico.** Está bloqueado por los $5 de saldo de Recraft
(punto 4.3.1) y por la decisión V3-vs-V4.1 (punto 4.3.2). Hasta que eso se resuelva, no hay piloto.

**Lo más urgente que no puedo hacer yo:** bajar a disco las 12 imágenes de Recraft ya pagadas
(4.2). Es lo único de esta lista donde esperar tiene un costo que no se recupera.
