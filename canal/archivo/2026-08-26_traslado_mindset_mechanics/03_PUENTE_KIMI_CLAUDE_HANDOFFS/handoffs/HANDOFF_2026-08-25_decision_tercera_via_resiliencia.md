# HANDOFF — Decisión sobre la 3ª vía de Resiliencia (respuesta a la escalación urgente)
**De: Kimi Code → Para: todas las sesiones de Claude Code · Fecha: 2026-08-25**
**Responde a: HANDOFF_2026-08-25_urgente_kimi_decision_pendiente.md y REPORTE_2026-08-23c_QA_fallido_escalado.md. Plan activo inmediato.**

---

## 0. Contexto de la decisión

La evidencia es clara y la acepto completa:
- **La Técnica B (texto verbatim) tiene techo real de fiabilidad** — orejas/nariz persisten tras DOS pasadas (§6.1 y §8). No se insiste más por esa vía como método principal.
- **El problema de dinamismo es de ARQUITECTURA de ensamblaje, no de estilo** — "1 clip real de 5-8s + frame congelado con zoom 30-53s" produce exactamente el resultado "cuadriculado y estático" que David describió. La biblia ya lo advertía (`MANUAL_PRODUCCION.md` §3.1: bloques de 45-60s deben ser 3-5 planos de 12-20s). Se aplicó la vía simple "para esta primera regeneración" y el mercado (David) ha dicho que no.
- **David manda en el QA visual.** El checklist automatizado es necesario pero no suficiente: ningún lote se da por bueno sin su visto.

---

## DECISIÓN 1 — Técnica: pivot a pipeline basado en IMAGEN DE REFERENCIA REAL

**La vía principal pasa a ser: Recraft AI (personaje ya validado ahí) → importar imagen a VideoExpress → animar con Video Action Prompt (image-to-video).**

Razonamiento: si Recraft ya produce el personaje correcto de forma fiable (memoria del proyecto), el problema de consistencia NO hay que resolverlo en VideoExpress — hay que **evitar que VideoExpress genere al personaje desde texto**. VideoExpress pasa a hacer lo que sí hace bien: animar una imagen dada con movimiento de cámara real.

Instrucciones:
1. Generar en Recraft las imágenes base de cada escena (personaje + composición de la escena), validando cada una contra frames de los videos publicados ANTES de importarla (regla 9 del principio rector).
2. Importar a VideoExpress con `import_local_image()` (ya implementada y probada).
3. Animar cada imagen con su Video Action Prompt (banco de §3 del manual + reglas §3.1: velocidad explícita, máx 2-3 movimientos encadenados, sujeto anclado por nombre).
4. **First Frame/Last Frame: AUTORIZADO ahora, como experimento acotado DENTRO del piloto** — 1 escena, comparativa A/B contra Video Action Prompt sobre la misma imagen base. La razón original para diferirlo ("la vía validada funciona") dejó de existir: la vía validada falló dos veces. Si FF/LF da mejor movimiento de cámara, se adopta para el resto del lote.
5. **Consistent Character (Técnica A): queda cerrada.** Con pipeline basado en imagen real, ya no aporta — no gastar más rondas en ella salvo que el pivot a imagen también falle.

## DECISIÓN 2 — Ensamblaje rediseñado: SÍ, 3 sub-clips reales por escena

Nueva arquitectura por escena narrativa (bloque de 40-60s):
- **3 sub-clips reales de 12-18s cada uno** (rango 2-4 según la duración del bloque), cada uno con plano/movimiento de cámara DISTINTO del banco (el scene plan v2 ya trae el plano principal de cada escena; los sub-clips varían ese plano: p.ej. escena 1 = push-in medio → primer plano ojo → sobre el hombro).
- **PROHIBIDO sostener un frame congelado más de 4 segundos.** El relleno con zoom lento sobre frame congelado queda eliminado de la arquitectura.
- **Transiciones cinematográficas entre sub-clips** — crossfade mínimo 8-12 frames o transición diegética; nada de cortes duros repetitivos ni el mismo fundido en todos los cortes (eso es parte de lo "cuadriculado").
- Arco cinematográfico por acto (manual §3.1): apertura aérea/establecedora → medio con tracking/push → clímax con orbit → cierre con pull-back, UNA vez por acto.
- El audio ya normalizado a -14 LUFS se conserva — eso estuvo bien hecho.

Coste estimado: 12 escenas × 3 sub-clips ≈ 36 animaciones en VideoExpress + stills en Recraft. Es el precio real de "que se vea como documental y no como fotos que se mueven". Lo autorizo, con gate de piloto (Decisión 3).

## DECISIÓN 3 — Presupuesto de la 3ª vía: GATE DE PILOTO, no cheque en blanco

| Fase | Contenido | Techo |
|---|---|---|
| **Piloto** | Escenas 1 y 2 completas con la nueva arquitectura (stills Recraft + ~6-8 animaciones VE incluido el experimento FF/LF) + ensamblaje de esos ~90s | **8 animaciones VE + 6 stills Recraft** |
| **Gate** | David ve el piloto de ~90 segundos y da veredicto: dinamismo + personaje. Sin su OK explícito NO se pasa a la fase completa. | — |
| **Completa** | Escenas 3-12 con la arquitectura validada | **34 animaciones VE + 22 stills Recraft** |
| **Margen quirúrgico** | Fallos individuales post-QA | **6 animaciones + 4 stills** |
| **TECHO TOTAL 3ª vía** | | **48 animaciones VE + 32 stills Recraft** |

Reglas del principio rector que aplican con fuerza aquí:
- Cada still de Recraft se valida contra frames publicados ANTES de gastar una animación encima (regla 9). Una imagen mala animada = crédito doble desperdiciado.
- Fallo individual = regeneración quirúrgica del sub-clip, nunca de la escena entera.
- La telemetría D6 (logs JSON a disco) es **obligatoria en cada generación de esta vía** — quiero consumo exacto por escena en el próximo reporte.
- Si el piloto falla el QA de David, STOP total y escala a mí con fotogramas + el diagnóstico. No hay cuarta vía sin mi autorización escrita.

---

## Autorización adicional (pendiente del REPORTE_2026-08-23d)

**SÍ, autorizado: corregir las 3 descripciones de Shorts con el link roto** (`nV4Yr03ov8E` → `p5ABwo18i2M` en x402GO_EYhM, qGzFLS-lP8E, Yb15pWj330Y). Es un link roto público — arreglarlo es estrictamente mejor que dejarlo, riesgo cero. Buen criterio el de pedir permiso antes de editar contenido público; mantened esa regla.

Y el trabajo de enlazado de los 14 Shorts (Related Video) queda registrado como **excelente** — verificación contra fuente real en vez de confiar en contexto resumido es exactamente el estándar que quiero.

---

## Mejora de protocolo (para que no vuelva el silencio de 2 días)

Kimi solo actúa cuando el usuario abre conversación — no puedo revisar el repo autónomamente. Por tanto:
- Cuando dejéis un archivo con `urgente` en el nombre, **avisad a David de que me escriba "urgente en repo"**. Es la única vía de despertarme.
- Escalaciones normales: reporte en `handoffs/` y David me avisa cuando pueda.
- Nunca más de 24h parados por una decisión mía sin recordatorio a David.

---

## Prompt de activación para Claude Code

```
Handoff nuevo de Kimi en handoffs/ (HANDOFF_2026-08-25_decision_tercera_via_resiliencia.md). Léelo completo — es el plan activo.

Instrucciones inmediatas:
1. Tarea de coste cero primero: corregir las 3 descripciones de Shorts con link roto (autorizado, ver handoff).
2. Piloto de la 3ª vía: escenas 1-2 de Resiliencia con pipeline Recraft (stills validados contra frames publicados) → import_local_image() → animación VE con Video Action Prompt + 1 experimento FF/LF en la escena 1. Arquitectura: 3 sub-clips reales de 12-18s por escena, PROHIBIDO frame congelado >4s, transiciones cinematográficas variadas.
3. Ensambla solo el piloto (~90s con el audio normalizado) y enséñaselo a David. STOP hasta su veredicto.
4. Telemetría D6 obligatoria en cada generación; reporta consumo exacto en REPORTE_2026-08-25.md.
5. Presupuesto del piloto: máx 8 animaciones VE + 6 stills Recraft. Sin OK de David no se pasa a la fase completa.
6. Si David aprueba: fase completa (escenas 3-12) dentro del techo total de 48 animaciones + 32 stills.

Recuérdale a David que me escriba "urgente en repo" si hay otro bloqueo — es la única forma de despertar a Kimi.
```
