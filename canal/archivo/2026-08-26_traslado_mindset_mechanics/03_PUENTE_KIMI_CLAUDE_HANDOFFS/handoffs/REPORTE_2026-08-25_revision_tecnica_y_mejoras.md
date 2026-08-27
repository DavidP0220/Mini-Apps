# Reporte — Revisión técnica completa del pipeline + mejoras aplicadas
**De: Claude Code (ejecución técnica local) → Para: Kimi Code y David · Fecha: 2026-08-25**

---

## 1. Qué se hizo

A petición de David ("revisemos todo desde el inicio y corrijamos posibles errores"), se hizo
una auditoría técnica completa del pipeline (`video_express_ai/`, `recraft_ai/`,
`youtube_pipeline/`), **sin gastar un solo crédito** (gate de piloto de Kimi respetado —
`HANDOFF_2026-08-25_decision_tercera_via_resiliencia.md`). Todo verificado offline: lectura de
código, `ffprobe` sobre archivos ya en disco, mocks.

De paso se rescataron **dos focos de trabajo local que existían sin commitear** desde sesiones
anteriores (uno en el working tree, otro en un worktree de agente huérfano
`.claude/worktrees/agent-a7e98089cf0c98088`) — nada se perdió, todo quedó en `main` y pusheado.

Commits de esta sesión: `2bd5b47`, `e31bd44`, `de78f29`, `4db5b20`.

## 2. Bugs corregidos (síntoma → causa → fix → verificación)

**CRÍTICO 1 — el bot descargaba el video equivocado sin fallar.**
Síntoma: clips repetidos/mal etiquetados en algún render.
Causa: `_poll_for_latest_video` aceptaba el ítem más reciente de Media Library apenas apareciera
`completed`, sin comprobar que fuera el render recién pedido. Un render tarda ~210s pero el primer
tick de polling ocurre a los ~20s, así que devolvía el clip **anterior** y lo guardaba con el
nombre de la escena nueva. Fallo silencioso: no había excepción ni log de error.
Fix: `snapshot_video_ids()` antes de generar + `known_ids` en el polling; aborta si el render sale
`failed` en vez de esperar 30 min completos.
Verificación: por SHA-256 se confirmó que el lote actual de 12 escenas de Resiliencia **no** está
afectado; el bug seguía latente para el próximo lote.

**CRÍTICO 2 — el cliente nuevo de Recraft nunca habría funcionado.**
Causa: combinaba `model=recraftv4_1` con `size=1820x1024`, tamaño que solo existe en V2/V3
(Appendix oficial de la API de Recraft). Hallazgo de fondo: **V4.1 no tiene ningún 16:9 exacto**, y
VideoExpress solo anima 16:9/9:16.
Fix: tabla de tamaños por familia de modelo con validación antes del HTTP; V4.1 genera 1344x768 y
se recorta a 1344x756 (16:9 exacto, verificado: 1.77778).

**SEGURIDAD — riesgo de publicar el borrador en la galería pública sin querer.**
Causa: `animate_library_image` togleaba el checkbox "Share this in the public gallery" a ciegas,
asumiendo que venía marcado. Si viniera desmarcado, ese mismo click lo **activa**.
Fix: usa `_set_checkbox_by_label` (ya existía el patrón, no se aplicaba aquí) — lee el `<input>`
real antes de tocarlo y aborta si no puede leerlo.

**Otros 11 arreglos** (detalle completo en el commit `2bd5b47`): `image_url` apuntaba a un endpoint
que no existe (se habría pagado un image-to-image que nunca ocurría — movido a `image_to_image()`
con el endpoint correcto); `negative_prompt` no es compatible con modelos V4.x y no se validaba;
descargas sin timeout/reintento/atomicidad en ambos módulos (podían colgar el proceso o dejar
archivos truncados con el crédito ya gastado); Chromium quedaba zombi en los 7 comandos del CLI por
falta de `try/finally` (nuevo `video_express_ai/session.py` con cierre garantizado); `ffprobe` sin
timeout; `youtube_pipeline` renderizaba **a 720p**, contra la regla dura del canal de 1080p mínimo.

**Rescatado de un worktree huérfano** (commit `e31bd44`, trabajo de una sesión anterior que quedó
sin fusionar): rutas de `video_understand.py` clavadas a una instalación WinGet de una máquina
concreta (mismo patrón de bug que en `video_express_bot.py`, ya corregido ahí); y el guardarraíl de
la Decisión 2 de Kimi en `_assemble_visual_track.py` — ese script ahora se marca **OBSOLETO** y
aborta si un frame congelado supera 4s, en vez de producir en silencio el video que ya reprobó QA
(medido: 474 de 554s del lote anterior eran imagen fija — 85,6%. Ese es también el origen del
misterioso "clip de ciudad 3D" en ~545s: era el último frame de la escena 12, un pull-back que a
los ~4s deja al personaje fuera de cuadro, congelado 46 segundos).

## 3. Mejoras de infraestructura aplicadas

- Lock de cuenta con PID+caducidad en `session.py` (Media Library es global de la cuenta; dos
  corridas simultáneas se robaban renders en silencio entre sí).
- Throttle a 4 req/s en el cliente de Recraft (límite documentado de la API: 5/s, 100/min).
- `.gitattributes` (no existía): fuerza `eol=lf` en texto y `binary` en PNG/MP4/ZIP — un `.sh` con
  CRLF rompe los scripts de ffmpeg de `shorts_final/`.
- Telemetría D6 completa (antes `stylize`/`export`/`import` no dejaban rastro).
- `import_local_audio`/`import_local_image` unificados (estaban duplicados y ya divergidos).
- `generate_scene.py --credits`: consulta el saldo de Recraft sin gastar nada.
- Se registró en `ESTILO_MINDSET_MECHANICS.md` §6.bis: los negativos ("NO nose", "NO ears") nunca
  deben ir como texto en el prompt positivo — un modelo de difusión no entiende la negación
  lingüística y repetir "NO nose" lo hace *más* probable, no menos. Ahora van vía el parámetro
  `negative_prompt` real de la API. **Pendiente de verificar contra una generación real** (falta
  saldo de la API).
- `PLAYBOOK_MONETIZACION.md` §5.bis: Test & Compare (A/B nativo de YouTube) registrado como paso
  obligatorio del checklist de publicación, por instrucción de Kimi
  (`HANDOFF_2026-08-25_integracion_investigacion_ypp_y_backup.md`).
- Se rescataron 3 documentos de Human Chronicles (segundo canal) que existían en disco sin
  commitear: `ESTADO_CANAL.md`, `ESTILO_HUMAN_CHRONICLES.md`, `PLAYBOOK_MONETIZACION_HC.md`. Y se
  corrigió una referencia obsoleta en `LEEME-PRIMERO-HANDOFF.md` (el canal hermano es
  `@humanchronicles11`, cuenta de Google separada — no `HumanChronicles18`, que era un borrador
  viejo).

## 4. Decisión pendiente de Kimi (no técnica, no la tomo yo)

Para los 7 stills nuevos del piloto de Resiliencia: ¿generarlos con **V4.1 + recorte a 1344x756**,
o bajar a **V3 @ 1820x1024** (16:9 nativo, y el único que soporta `style_id`, el mecanismo oficial
de Recraft para consistencia de personaje)? V3 podría cambiar ligeramente el look frente a las 12
escenas ya generadas con V4.1.

## 5. Pendiente de David

1. **La API de Recraft sigue sin configurar** (`recraft_ai/.env` no existe, sin `RECRAFT_API_KEY`
   ni el saldo de $5 cargado) — bloquea el siguiente paso del piloto
   (`HANDOFF_2026-08-25_mapeo_piloto_stills.md`). Esto requiere que tú lo hagas — no puedo cargar
   saldo ni manejar la key por ti.
2. **Riesgo real de pérdida de material.** Hay ~669MB en videos largos generados
   (`youtube_pipeline/channels/mindset_mechanics/output/resilience_v2/*.mp4`, incluye
   `resilience_final_v2.mp4` y `RESILIENCIA_AUDIO_ARREGLADO.mp4`) más varios Shorts en
   `shorts_final/` que están **fuera de git** (correctamente, por `.gitignore`, son pesados) pero
   **tampoco están respaldados en ningún otro lado** que se haya podido verificar desde aquí (no
   hay carpeta de Google Drive sincronizada en esta máquina, solo OneDrive). Recraft y VideoExpress
   borran originales a los 60 días. Dime dónde quieres que se respalden (¿OneDrive local?) y lo
   dejo copiado.
3. **Verificación pedida por Kimi:** entrar a YouTube Studio → Monetización y confirmar si ya
   aparece el aviso del cambio de requisitos YPP (4.000h → 8.000h desde el 1-feb-2027 para canales
   fuera del programa). Es la fuente que falta para que Kimi confirme la fecha límite estratégica.

## 6. Qué NO se tocó (a propósito)

No se generó ningún still de Recraft, no se animó nada en VideoExpress, no se gastó ningún crédito.
El gate de piloto de Kimi sigue intacto — sigue esperando la API key de Recraft para poder ejecutar
`HANDOFF_2026-08-25_mapeo_piloto_stills.md`.
