# Reporte — Auditoría técnica en paralelo: la mayoría ya estaba resuelta por otra sesión; 1 riesgo nuevo sin verificar

**De:** sesión Claude (coordinación) · **Fecha:** 2026-08-25

## Qué pasó

Lancé una auditoría técnica completa del pipeline en un worktree aislado, sin saber que otra sesión estaba haciendo lo mismo en `main` al mismo tiempo. Al terminar, `main` ya tenía el commit `2bd5b47` ("revision tecnica completa - 14 bugs") que cubre el mismo terreno con más profundidad — incluido el bug más grave que mi auditoría había encontrado por su cuenta:

**Coincidencia exacta:** `_poll_for_latest_video()` devolvía `results[0]` sin comprobar que fuera el render recién pedido. Como una generación tarda ~210s, en la primera vuelta del polling `results[0]` casi siempre era el video ANTERIOR ya completado — se descargaba el clip equivocado y se guardaba con el nombre de la escena nueva, sin ningún error visible. Las dos auditorías llegaron al mismo diagnóstico de forma independiente; `2bd5b47` ya trae el fix (snapshot de IDs + abortar en `failed`) y es más completo que el mío (14 bugs vs 5), así que **no fusioné mi rama** — habría sido redundante y con más riesgo de conflicto que valor.

## Qué sí rescaté de mi auditoría (no tocado por la otra sesión)

Solo 3 archivos que `2bd5b47` no tocó:

1. **`video_express_ai/_assemble_visual_track.py`** — marcado como OBSOLETO con guardarraíl: aborta si algún día se reintenta la arquitectura de "1 clip corto + frame congelado" que Kimi prohibió (Decisión 2 del handoff de la 3ª vía). Documenta con números la causa raíz del QA fallido: del video Resiliencia anterior, **474 de 554s (85,6%) eran imagen fija**, no movimiento.
2. **`video_understand.py`** — rutas de ffmpeg/ffprobe clavadas a una sola máquina, cambiadas a PATH/variable de entorno (mismo patrón de fix que ya se aplicó en el resto del pipeline).
3. **`ESTILO_MINDSET_MECHANICS.md` §6.bis** — nota permanente explicando por qué escribir negativos como texto en el prompt positivo (`"NO nose"` repetido) los vuelve MÁS probables, no menos (los modelos de difusión no interpretan la negación lingüística). Documentación, no cambia comportamiento — el fix real ya está en `recraft_client.py` vía `2bd5b47`.

Todo lo demás de mi rama (fixes a `video_express_bot.py`, `recraft_client.py`, `generate_scene.py`) quedó descartado por ser una versión menos completa de lo que ya hizo `2bd5b47`. La rama sigue disponible en `worktree-agent-a7e98089cf0c98088` por si algo se necesita revisar, pero no es el plan activo.

## 🔴 Hallazgo nuevo, sin verificar — riesgo para el piloto de la 3ª vía

El storyboard del piloto (`storyboards/STORYBOARD_resilience_v3_piloto_SC01-SC02.md`) planea **8 paneles de 12s** (94s totales). Mi auditoría midió los 20 clips del lote anterior de VideoExpress (texto-a-video) y **ninguno superó 8,04s**, pese a que el prompt pedía duraciones distintas — sugiere un techo duro de la plataforma, no una elección de prompt.

**Ojo:** esa medición es de generación texto-a-video (arquitectura vieja). El piloto usa `animate_library_image()` (imagen-a-video con Video Action Prompt), que puede comportarse distinto — **no está confirmado que el mismo techo aplique aquí.**

**Antes de gastar las 8 animaciones del presupuesto del piloto:** lanzar 1 sola animación de prueba con `animate_library_image()` pidiendo 12s explícitos y medir la duración real del .mp4 con ffprobe. Si el techo de ~8s también aplica ahí, el storyboard de 12s/panel no es ejecutable tal cual y hay que decidir (Kimi/David) entre: recortar a paneles de ~8s (más paneles, mismo total), o aceptar el hueco y rellenarlo con un método distinto al frame congelado prohibido (p.ej. sub-clip repetido con corte, no sostenido estático).

## Estado de mi rama de auditoría

`worktree-agent-a7e98089cf0c98088` — commit `05c5fbb`, no fusionada a `main` salvo los 3 archivos rescatados arriba (ya commiteados en `main` directamente). Se puede borrar la rama cuando se confirme que no hace falta revisar nada más de ahí.
