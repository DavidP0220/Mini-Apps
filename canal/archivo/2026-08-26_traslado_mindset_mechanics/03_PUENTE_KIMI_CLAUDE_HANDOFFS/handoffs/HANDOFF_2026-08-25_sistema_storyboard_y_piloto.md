# HANDOFF — Sistema de Storyboard instalado + piloto Resiliencia actualizado
**De: Kimi Code → Para: Claude Code · Fecha: 2026-08-25**
**Plan activo. Actualiza (no reemplaza) el handoff de 3ª vía: el piloto de escenas 1-2 ahora se ejecuta CON storyboard.**

---

## 1. Qué cambia desde hoy (permanente)

**Ningún video entra a generación sin storyboard aprobado.** El pipeline oficial pasa a ser:

```
Guion → TTS + ffprobe → STORYBOARD → gate David → stills Recraft (1 por panel)
→ VideoExpress image-to-video → ensamblaje → QA → publicación
```

Documentos nuevos en el repo:
- `SISTEMA_STORYBOARD_MINDSET_MECHANICS.md` (raíz) — biblia operativa: anatomía de panel (12 campos), esquema JSON canónico, plantillas de prompts, reglas de ritmo/retención, mapa beat→plano, continuidad, checklist de 15 puntos.
- `storyboards/STORYBOARD_resilience_v3_piloto_SC01-SC02.md` + `storyboard_resilience_v3_piloto.json` — el primer storyboard real, producido por el nuevo rol Storyboard Director: 8 paneles para las escenas 1-2, validado 15/15.

## 2. El piloto de la 3ª vía AHORA se ejecuta con este storyboard

Actualización de la arquitectura respecto al handoff anterior: en vez de 3 sub-clips de 12-18s, son **4 sub-clips de ~10-14s por escena** (ajuste fino tras la investigación de ritmo: cambio visual cada 10-14s, cero metrónomo). El piloto sigue siendo escenas 1-2 = **8 animaciones VE** — mismo presupuesto autorizado, mejor granularidad.

Instrucciones de ejecución:
1. **Antes de generar nada:** enséñale a David el storyboard (la tabla resumen basta — es la previsualización de coste cero). Gate: su OK.
2. Con OK de David: genera los 8 stills en Recraft siguiendo los `image_prompt` del storyboard EXACTAMENTE (ficha verbatim + fixes `NO visible ears` + `thick black outline, flat cel-shading`). Valida cada still contra frames de los videos publicados ANTES de animarlo (regla 9).
3. Importa cada still con `import_local_image()` y anímalo con su `video_action_prompt` EXACTO. Un movimiento dominante por panel. En SH001 ejecuta además el experimento FF/LF ya autorizado (comparativa sobre la misma imagen base).
4. Ensambla los 8 clips en orden de `shot_id` con las transiciones indicadas + audio normalizado (-14 LUFS) → piloto de 1:34 → gate de David.
5. Telemetría D6 obligatoria: log JSON por generación. Nombres de archivo = `{shot_id}.png` / `{shot_id}.mp4`.
6. Si un panel es técnicamente inviable: NO improvises — márcalo `status: blocked` con el motivo en el reporte.

## 3. Nota técnica aceptada (revisión de biblia)

El Storyboard Director señaló que los image_prompt pesan ~280-300 palabras (ficha verbatim + sufijo + negativa), por encima de la guía de ≤150 palabras. **Decisión: prevalece la ficha verbatim** (jerarquía de fuentes 1-2). La guía de brevedad aplica a los detalles de escena (5-7 distintivos), no al bloque fijo. Queda anotado para la v1.1 de la biblia.

## 4. Roles actualizados del proyecto

| Rol | Quién | Función |
|---|---|---|
| Estratega | Kimi Code | Decisiones, investigación diaria, aprobación estratégica |
| **Storyboard Director** | Subagente especializado (rol registrado) | Produce storyboards bajo la biblia; rango creativo más alto del pipeline |
| Ejecutor técnico | Claude Code | Genera, ensambla, reporta — ejecuta storyboards sin improvisar |
| Gate de calidad | David | Aprueba storyboard y piloto antes de gasto masivo |

## Prompt de activación para Claude Code

```
git pull. Hay handoff nuevo: handoffs/HANDOFF_2026-08-25_sistema_storyboard_y_piloto.md — léelo junto a SISTEMA_STORYBOARD_MINDSET_MECHANICS.md y storyboards/STORYBOARD_resilience_v3_piloto_SC01-SC02.md.

El piloto de Resiliencia ahora se ejecuta con storyboard: 8 paneles, 8 stills Recraft, 8 animaciones VE, prompts EXACTOS del documento. Primer paso: muestra la tabla resumen del storyboard a David y espera su OK antes de generar. Telemetría D6 en cada generación. Reporta en handoffs/REPORTE_2026-08-25_storyboard_piloto.md.
```
