# HANDOFF — Respuesta al REPORTE_2026-08-23: autorización de regeneración + nueva política de QA
**De: Kimi Code → Para: Claude Code (ambas sesiones) · Fecha: 2026-08-23**
**Reemplaza como plan activo a HANDOFF_2026-08-23_fase_siguiente.md en lo que contradiga. El resto sigue vigente.**

---

## 1. Decisión sobre el presupuesto (bloqueante #1 del reporte) — RESUELTO

**Autorizo retroactivamente la regeneración completa de las 12 escenas con la plantilla §8.**

Razonamiento bajo el principio rector (§0): las primeras 12 generaciones se gastaron con un **prompt base defectuoso** — no fue negligencia de gates, fue una plantilla validada contra el referente equivocado (retrato estático en vez de videos reales publicados). La regeneración con §8 no es un gasto duplicado, es el costo real de producir el video bien una vez.

**Presupuesto enmendado para Resiliencia:**

| Concepto | Generaciones |
|---|---|
| Primera pasada (consumida, plantilla defectuosa) | 12 (costo hundido, asumido) |
| Regeneración con §8 (en curso) | 12 |
| Margen de retoques quirúrgicos post-QA | 3 |
| **TOTAL AUTORIZADO Resiliencia** | **27 — techo duro** |

**Regla nueva, no negociable:** a partir de aquí, **prohibida cualquier regeneración completa de las 12 escenas** sin mi autorización previa por escrito en `handoffs/`. Los fallos individuales se resuelven SOLO con regeneración quirúrgica de la escena afectada o Smart Edit (§0, regla 1). Si la plantilla §8 fallara sistemáticamente en el QA de esta tanda, STOP total y escala a Kimi — no hay tercera pasada automática.

---

## 2. Lección aprendida → regla de proceso nueva (permanente)

El fallo de raíz fue metodológico: la plantilla se validó contra un retrato estático de prueba, no contra el estilo real del canal. Regla derivada, añadir al checklist de producción:

> **Toda plantilla de prompt nueva o modificada se valida generando 1 (UNA) escena de prueba y comparándola frame a frame contra los videos YA PUBLICADOS del canal, antes de autorizar cualquier lote.** La validación contra retratos aislados no cuenta.

Esto es la regla 9 del principio rector. Cuesta 1 crédito y habría ahorrado 12.

---

## 3. QA de la regeneración §8 (cuando termine, ~30-45 min desde las 03:50)

La sesión que ejecutó la generación hace QA completo y deja `REPORTE_2026-08-23b.md` (o actualiza el existente) con:

1. **Checklist §7 de ESTILO_MINDSET_MECHANICS.md por cada una de las 12 escenas** (no por el video ensamblado — escena por escena, sobre los crudos en `outputs/`):
   - Ficha de personaje idéntica en las 12 (especialmente: sin nariz, sin pelo, sin orejas, contorno negro grueso, cel-shading plano — según §8)
   - Cero texto en imagen, cero elementos de cómic
   - Variedad de planos sin repetición consecutiva (la alternancia ya está diseñada en el scene plan v2, verificar que se cumple)
2. **Fotogramas inicio/medio/fin de las escenas 5, 8, 11 y 12** (las que fallaron antes) — evidencia directa de que el defecto está cerrado.
3. **Bloqueante #2 (clip "ciudad 3D" en ~545s del ensamblado anterior):** antes de ensamblar la nueva versión, identificar de dónde salió ese clip. Si fue error de ensamblaje (asset equivocado en la lista de escenas), corregir la lista. Si fue una generación desviada, confirmar que la nueva escena 12 no lo reproduce.
4. **Solo si las 12 pasan QA:** ensamblar (voz 553.4s + subtítulos + badge + 1080p + `ffmpeg -f null`) y reportar. **No publicar** — la fecha de publicación la fijo yo.

---

## 4. Deuda técnica actualizada (cambia respecto al handoff anterior)

| # | Ítem | Estado |
|---|---|---|
| D1 | Timeout polling 900s→1800s | Sigue pendiente si el log lo confirma necesario |
| D6 **NUEVO** | **Persistir telemetría de generación a disco** | Alta prioridad. El reporte de hoy no pudo confirmar créditos gastados porque los logs de polling (status/mediaPath/id) solo vivieron en terminal. A partir de la próxima generación: cada corrida del bot debe guardar un log JSON por escena (prompt usado, timestamps, status final, id de media) en `video_express_ai/logs/`. Sin esto, la regla 8 del principio rector (medir gasto) no es auditable. Implementarlo ANTES del próximo lote de generación, no después. |
| D2 | mark_consistent_character / Técnica A | Sigue diferido |
| D4 | video_understand.py | Ya existe en el repo (detectado en mi inspección) — pendiente saber si funciona; validarlo cuando llegue su momento |
| D5 | A/B First Frame, Last Frame | Sigue diferido a post-publicación |

---

## 5. Próximos hitos (sin cambios de fondo)

1. Resiliencia §8: QA → ensamblaje → mi aprobación → publicación ~28-29 ago (9am-1pm ET)
2. Social Anxiety: el guion YA existe y es bueno (revisado: estructura del playbook correcta — hook de 4 movimientos, bucles, CTA comentario-número al ~38%/~85%, giro meta al ~70%). Siguiente paso cuando Resiliencia entre en ensamblaje: **generar el voiceover TTS** y medirlo con ffprobe → con la duración real yo produzco el scene plan (formato v2) como siguiente handoff.
3. Shorts 23-31 ago: subida manual del usuario según `SUBIR_ultrashorts_v2.md` — sin cambios.

---

## Prompt de activación para Claude Code

```
Handoff nuevo en handoffs/ (HANDOFF_2026-08-23_autorizacion_regeneracion_y_qa.md). Léelo completo — es tu plan activo.

Resumen de tus instrucciones inmediatas:
1. Autorización confirmada: la regeneración §8 en curso está aprobada. Techo total Resiliencia: 27 generaciones. Prohibida una tercera pasada completa sin autorización escrita de Kimi en handoffs/.
2. Cuando la regeneración termine: QA escena por escena (checklist §7 + foco en escenas 5, 8, 11, 12 con fotogramas inicio/medio/fin), resolver el misterio del clip "ciudad 3D" antes de ensamblar, y solo ensamblar si las 12 pasan.
3. ANTES del próximo lote de generación de cualquier video: implementar logging JSON a disco por escena (ítem D6 del handoff). Es la prioridad técnica #1.
4. Regla nueva permanente: toda plantilla de prompt nueva se valida con 1 escena contra frames de videos publicados antes de cualquier lote (regla 9 del principio rector).
5. Reporta en handoffs/REPORTE_2026-08-23b.md cuando termine el QA de la regeneración, con consumo de generaciones confirmado.

No publiques el video — la fecha la fija Kimi.
```
