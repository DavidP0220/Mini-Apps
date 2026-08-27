# Reporte — El "techo de 8s" no era un techo: el bot nunca pedía duración

**De:** sesión Claude (auditoría técnica, en respuesta al pedido explícito de David de solucionar y no solo reportar) · **Fecha:** 2026-08-25 · Commit: `dae5829`

## Qué se pensaba y qué era en realidad

El reporte anterior (`REPORTE_2026-08-25_auditoria_paralela_y_riesgo_duracion.md`) dejó como riesgo sin verificar que VideoExpress pudiera tener un techo duro de ~8s, porque ningún clip del lote anterior superó 8,04s pese a pedir duraciones distintas por prompt.

**Causa raíz real:** el bot nunca fijaba la duración como parámetro — VideoExpress la elegía sola. Confirmado con ffprobe sobre los 22 .mp4 en disco: las duraciones estaban **cuantizadas en 3 valores exactos** (5,04 / 6,04 / 8,04s), sin nada intermedio — huella de un selector discreto, no de un recorte por límite de plataforma.

**Verificación sin gastar el crédito autorizado:** se volcó el DOM del modal de creación sin pulsar "Create Video". Detrás del checkbox "Advanced Mode" hay un control oculto: `input type="range" name="video_duration" min="3" max="10" value="5"`. **Rango real de la plataforma: 3–10 segundos.** La intuición de David (10s) era correcta, y además es el máximo posible — 12s nunca fue alcanzable, lo confirma también el roadmap público de VideoExpress ("Increase maximum AI video clip length to 10 seconds or more" sigue como petición abierta sin resolver).

## Qué quedó aplicado (no solo propuesto)

- `_set_video_duration()` + parámetro `duration_seconds` añadido a `animate_library_image()` y `create_silent_video()` en `video_express_ai/video_express_bot.py`.
- Guardarraíl: pedir algo fuera de 3–10s aborta ANTES de tocar el navegador (antes de gastar crédito).
- Telemetría D6 ampliada: cada evento registra `requested_duration_s` vs `actual_duration_s` (medido con ffprobe), así un descuadre futuro se detecta solo, sin depender de que alguien lo note a ojo.
- Regla dura nº10 añadida a `video_express_ai/CLAUDE.md`.
- **Storyboard piloto reescrito y ejecutable ya mismo:** los 8 paneles de 12s (imposibles) pasaron a **15 paneles** (14×6s + 1×10s), suman los 94s exactos del piloto, **sin tocar los timecodes de la voz en off**. Efecto colateral positivo: 15 cortes en vez de 8 — más dinamismo, que era justo la queja de QA de David sobre el video anterior.

## Lo que falta para cerrar del todo (no es responsabilidad técnica, son decisiones)

1. **No se pudo ejecutar la prueba real de generación:** la sesión de VideoExpress expiró (redirige a login) y el proyecto no guarda contraseñas por diseño. Hace falta que David corra `python setup_auth.py` una vez para renovar la sesión. El crédito de prueba autorizado por Kimi sigue sin gastar — la primera animación real del piloto servirá como verificación.
2. **Presupuesto:** las animaciones del piloto pasan de 8 a 15 (las imágenes de Recraft siguen siendo 8, cada par de paneles reutiliza la misma imagen base). Kimi/David deciden si aprueban el nuevo conteo antes de animar.
3. **Diseño:** los paneles "b" de cada par continúan el movimiento del panel "a" sobre la misma imagen — funciona tal cual. Si se quiere variedad de plano real en cada uno de los 15, haría falta una imagen distinta por panel, lo que subiría Recraft de 8 a 15 imágenes también — decisión creativa de `storyboard-director`, no técnica.

## Lección para no repetir

El error no fue de código sino de método: se infirió un límite de plataforma mirando solo las *salidas* (duraciones resultantes) sin revisar los *controles de entrada* (el modal tiene un slider oculto). Revisar el DOM/formulario real costó 0 créditos y dio el rango completo de una vez, en vez de un dato suelto que llevó a una hipótesis equivocada.
