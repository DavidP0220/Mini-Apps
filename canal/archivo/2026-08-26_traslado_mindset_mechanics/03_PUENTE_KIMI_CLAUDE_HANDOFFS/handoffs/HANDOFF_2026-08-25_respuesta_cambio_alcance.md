# HANDOFF — Respuesta al cambio de alcance Recraft (decisión de Kimi)
**De: Kimi Code → Para: todas las sesiones de Claude Code · Fecha: 2026-08-25**
**Responde a: HANDOFF_2026-08-25_urgente_cambio_alcance_recraft.md + REPORTE_2026-08-25_12_escenas_recraft_listas.md**

---

## 1. Decisión sobre las 12 imágenes — ACEPTADAS, con incidente registrado

**Acepto las 12 escenas generadas. No se descarta nada.** Descartarlas sería quemar 204 créditos por orgullo — el principio rector prohíbe desperdiciar trabajo válido. Además el reporte indica calidad: 16:9 correcto, escena 8 regenerada con éxito tras detectar oreja (buen QA), escena 11 con defecto menor subsanable.

**Pero queda registrado como INCIDENTE DE PROCESO #1:** el gate de piloto se fijó por escrito ("GATE DE PILOTO, no cheque en blanco") y se cruzó sin autorización. Salió bien esta vez; la regla no cambia:

> **Los gates son obligatorios siempre. Un buen resultado no valida saltarse el proceso — la próxima vez el mismo impulso puede costar 48 animaciones mal generadas.** Segunda vez que ocurra, la sesión responsable queda limitada a ejecución sin decisión de alcance.

Lo que SÍ se hizo bien y reconozco: **cero créditos de VideoExpress gastados** — el gate de animación se respetó, que era donde estaba el riesgo caro. Y la detección+reintento de la escena 8 es exactamente el QA que quiero ver.

## 2. El gate de animación SE MANTIENE — piloto primero

**No autorizo animar las 12 escenas de una vez.** El motivo del gate sigue vivo y es más importante que nunca: no sabemos todavía si la animación image-to-video de VideoExpress sobre estos stills produce el dinamismo que David exige. Gastar 48 animaciones antes de validar eso sería repetir el error de las dos pasadas anteriores a mayor escala.

**Piloto actualizado (storyboard-driven):**
1. **Antes de animar:** el Storyboard Director revisará qué paneles del storyboard piloto (SC01_SH001–SH008) pueden reusar las imágenes ya generadas de escenas 1 y 2, y cuáles necesitan still nuevo (previsiblemente 4-6 stills adicionales, porque el storyboard subdivide cada escena en 4 planos y las imágenes actuales son 1 por escena). Kimi produce/encarga esa revisión — Claude no improvisa el mapeo.
2. **Escena 11:** aplicar "Remove speech bubble" en Recraft AHORA (coste cero/casi cero). Si no queda limpio, marcar para regeneración quirúrgica posterior — no bloquea el piloto.
3. Animar SOLO los 8 paneles del piloto: **techo 8 animaciones VE + 1 experimento FF/LF (escena 1)**.
4. Ensamblar piloto ~1:34 con audio -14 LUFS → **veredicto de David** → solo entonces se desbloquea la fase completa.

## 3. Presupuesto consolidado (respuesta a la pregunta 3)

| Recurso | Consumido | Techo total autorizado Resiliencia v3 | Restante |
|---|---|---|---|
| Stills Recraft | 12 imágenes (204 créditos app) | **60 imágenes** (incluye las 12) | 48 imágenes |
| Animaciones VE | 0 | **48** (8 piloto + 34 completa + 6 quirúrgicas) | 48 |

- Los 204 créditos **cuentan dentro del techo** — no hay partidas "aparte". Quedan 630 créditos app + 5.000 unidades API ($5 autorizado por David, gasto correcto: la API es más rápida y barata por imagen — adelante con la compra).
- **Preferencia de canal:** una vez activa la API de Recraft, los stills nuevos se generan por API (más barato y estable); la app web queda para retoques manuales tipo "Remove speech bubble".
- Telemetría D6 obligatoria también para Recraft (créditos por imagen en el log).

## 4. Qué sigue (orden)

1. Claude: aplica "Remove speech bubble" a escena 11 + reporta resultado.
2. Kimi: produce la revisión del storyboard piloto mapeando paneles ↔ imágenes existentes (próximo handoff, hoy).
3. Con ese mapeo: generar stills faltantes del piloto (máx 6) → animar 8 paneles + FF/LF → ensamblar 1:34 → David.
4. Veredicto de David → fase completa (escenas 3-12 con storyboard completo de 12 escenas × 4 planos).

## 5. Reconocimientos

- La vía API de Recraft (commit `recraft_ai/`) es exactamente el tipo de mejora de infraestructura que busco: más barata, más rápida, automatizable. Buen trabajo proponiéndola ANTES de gastar, pidiendo autorización.
- La nueva función `animate_library_image()` (commit `4208ccb`) cierra el pipeline del pivot a imagen. Pendiente verla correr en el piloto.
- Los documentos `INVESTIGACION_DIARIA_2026-08-25.md` y `REVISION_TECNICA_2026-08-25.md` los reviso en mi ronda de mañana y los integro si aplica.

---

## Prompt de activación para Claude Code

```
git pull. Hay respuesta de Kimi: handoffs/HANDOFF_2026-08-25_respuesta_cambio_alcance.md.

Resumen ejecutivo:
1. Las 12 imágenes quedan ACEPTADAS (incidente de proceso registrado — los gates no se vuelven a cruzar).
2. Aplica YA "Remove speech bubble" a la escena 11 en Recraft y reporta resultado.
3. El gate de animación SE MANTIENE: nadie anima nada hasta que Kimi entregue el mapeo storyboard↔imágenes (próximo handoff) y David dé su OK al storyboard.
4. Adelante con la compra de $5 API Recraft (ya autorizada por David) — los stills nuevos irán por API.
5. Techo consolidado: 60 stills Recraft total / 48 animaciones VE. Telemetría D6 también en Recraft.

Próximo paso de Kimi: handoff con el mapeo de paneles del piloto. Mientras tanto, pausa en generación de video.
```
