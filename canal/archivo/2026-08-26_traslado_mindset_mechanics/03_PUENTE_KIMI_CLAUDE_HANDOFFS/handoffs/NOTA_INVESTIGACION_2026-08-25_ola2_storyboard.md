# NOTA DE INVESTIGACIÓN — Ola 2: storyboard/producción (4 frentes)
**Fecha: 2026-08-25 · Kimi Code · Pedida por David antes de aprobar el piloto. 4 subagentes explore en paralelo.**
**Estado: integrada. Cada hallazgo tiene su acción marcada: [ADOPTADO] / [PILOTO] / [FUTURO] / [DESCARTADO].**

---

## Hallazgo crítico #1 — Nuestros clips planeados eran DEMASIADO LARGOS para 2D [ADOPTADO → biblia §5 v1.1]

La investigación de animación 2D con IA es unánime: **la deriva de estilo se acumula con la duración del clip** (propagación de error). Clips crudos óptimos: **5-8s**. Además, los movimientos **orbit/rotación con cara visible son los que inventan orejas y narices** — el modelo fuerza volumen 3D sobre ilustración plana. Ese es el origen exacto de nuestro defecto histórico.

Acción: doctrina de duración reescrita (clip crudo 5-8s + extensión eased en post máx 4s), orbit prohibido con cara visible, hard cut (no crossfade) entre clips del mismo personaje.

## Hallazgo crítico #2 — El video_action_prompt llevaba el blindaje equivocado [ADOPTADO → biblia §4 v1.1]

Nueva plantilla con: declaración de estilo 2D como primera frase ("Flat 2D... no 3D rendering"), identidad delegada a la imagen (no al prompt), micro-vida facial limitada a parpadeo/respiración, y cierre "Keep character identity, face and proportions unchanged. No cuts, no warping, no flicker."

## Hallazgo #3 — El sonido era nuestra asignatura pendiente [ADOPTADO → biblia §8.5]

El pipeline solo tenía voz + subtítulos. Ahora: bloque AUDIO por panel (música/ambiente/SFX/ducking/silencio), niveles profesionales (-14 LUFS master, música -18/-24 bajo voz, ducking sidechain obligatorio con TTS), music drop antes de reveals, cambio de música cada 60-120s, silencio dramático 1-2 por video. Fuentes libres para YPP: YouTube Audio Library + Pixabay ahora, Epidemic Sound al monetizar.
**Para el piloto de Resiliencia: se aplica en post sobre el ensamblaje — no requiere regenerar nada.**

## Hallazgo #4 — El canal necesitaba un lenguaje visual propio [ADOPTADO → DICCIONARIO_VISUAL]

Canonizado: Guardia roja (amígdala), Ingeniero azul (corteza prefrontal), Jardinero verde (neuroplasticidad), metáfora madre "El Desfase" (sabana/ciudad espejo), escenarios recurrentes (Sala de Control, Sabana, Ciudad-Neón), morphing diegético como gramática (tigre→notificación). Esto es lo que hará el canal reconocible en <1s y "que la gente espere los videos" — universo visual consistente.

## Hallazgo #5 — Lecciones Kurzgesagt aplicables [PARCIALMENTE ADOPTADO]

- [ADOPTADO] El guion manda sobre lo visual; consistencia vía sistema (style guide + assets recurrentes) no talento; caso documentado: +126% AVD solo por eliminar inconsistencias entre escenas.
- [ADOPTADO] El host SUFRE el concepto en pantalla, nunca diagrama flotante.
- [FUTURO] Su densidad (~200 ilustraciones/10 min) es inalcanzable con nuestro presupuesto por ahora; nuestro objetivo 50-60 paneles es el compromiso correcto costo/calidad. Re-evaluar cuando el canal monetice.
- [DESCARTADO] Copiar su polish — competimos en nicho adyacente con estilo propio.

## Hallazgo #6 — Nicho psicología animada 2024-2026 [ADOPTADO como contexto]

Psych2Go (12M, "7 señales de..."), After Skool (whiteboard), Sprouts (metáforas de aula). El ganador siempre: UN estilo ultra-consistente identificable en 2s. La consistencia es exactamente lo que la IA hace bien si se fuerza con sistema — jugamos a nuestro favor.

## Impacto en el piloto (actualización de instrucciones)

1. Clips crudos de animación: 5-8s (no 10-14s de generación continua)
2. Video action prompts: usar plantilla v1.1 con blindaje anti-deriva
3. Transiciones del storyboard: verificar hard cut entre clips del host (el storyboard ya usa mayoría hard cuts ✅)
4. Post: extensión eased + grain 15-20% (unifica clips, oculta flicker) + capa de sonido según §8.5
5. El storyboard piloto NO necesita regenerarse: sus planos (push-in, pan, tilt, crane, static) son todos de la lista SEGURA para 2D ✅ — la ola 2 lo valida retrospectivamente

**Fuentes completas en los 4 reportes de investigación (archivados en esta sesión de Kimi). Confianza: alta en animación 2D y sonido (fuentes convergentes); media en benchmarks de nicho (agregadores).**
