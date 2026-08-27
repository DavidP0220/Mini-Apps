# HANDOFF — Mapeo storyboard piloto ↔ imágenes Recraft existentes
**De: Kimi Code → Claude Code · Fecha: 2026-08-25 · Complementa HANDOFF_2026-08-25_respuesta_cambio_alcance.md**

## Mapeo aprobado (escenas 1-2 del piloto, 8 paneles)

Las imágenes Recraft existentes se generaron 1 por escena narrativa (plan v2): escena 1 = medium shot mesa de conferencias; escena 2 = ECU ojo. Contra el storyboard piloto:

| Panel | Plano | Fuente del still |
|---|---|---|
| SC01_SH001 | medium, eye_level, push_in (hook) | ✅ **REUSA imagen escena 1** existente |
| SC01_SH002 | close_up, dutch, pan left | 🆕 still nuevo (Recraft API) |
| SC01_SH003 | insert (notas cayendo), high, tilt down — PATTERN INTERRUPT | 🆕 still nuevo |
| SC01_SH004 | wide, overhead, crane up | 🆕 still nuevo |
| SC02_SH005 | extreme_close_up ojo, push_in | ✅ **REUSA imagen escena 2** existente |
| SC02_SH006 | medium_close, dutch, pan right | 🆕 still nuevo |
| SC02_SH007 | insert, high, static micro-drift | 🆕 still nuevo |
| SC02_SH008 | close_up, push_in very_slow + HOLD 2s | 🆕 still nuevo |
| FF/LF experimento (sobre SH001) | last frame = variante más cerrada de escena 1 | 🆕 still nuevo (1) |

**Balance: 2 stills reusados + 7 stills nuevos = piloto completo.** Dentro del presupuesto (quedan 48 imágenes del techo de 60).

## Instrucciones de ejecución

1. Los 7 stills nuevos se generan con los `image_prompt` EXACTOS del storyboard (`storyboards/STORYBOARD_resilience_v3_piloto_SC01-SC02.md`), vía **API de Recraft** (una vez activo el saldo de $5). Validar cada still contra frames de videos publicados (regla 9) ANTES de importarlo.
2. Las 2 imágenes reusadas: descargar de Recraft, verificar que el encuadre cuadra con la descripción del panel (SH001 medium eye_level / SH005 ECU ojo). Si el encuadre real difiere del panel, el panel manda: se genera still nuevo y la imagen existente se reserva para la fase completa.
3. Importar todo a VideoExpress con `import_local_image()`, nombrar `{shot_id}.png`.
4. Animar con `animate_library_image()` usando los `video_action_prompt` EXACTOS del storyboard. 8 animaciones VE máximo + 1 FF/LF.
5. Ensamblar en orden shot_id con las transiciones del storyboard + audio -14 LUFS → piloto 1:34 → **STOP, veredicto de David**.
6. Telemetría D6 en cada paso (créditos Recraft + VE por panel).

## Regla recordatoria
Nadie anima escenas 3-12 ni genera stills de la fase completa hasta el veredicto de David sobre el piloto. Sin excepciones.
