# PLANTILLA DE STORYBOARD — anatomía obligatoria del panel

Hereda el sistema ya probado en el proyecto anterior (biblia completa en
`../archivo/2026-08-26_traslado_mindset_mechanics/02_DOCUMENTOS_ESTRATEGIA_ESTILO/SISTEMA_STORYBOARD_MINDSET_MECHANICS.md`).
Se conservan **los mismos 12 campos y los mismos nombres** para que los scripts de ensamblaje
que ya existen sigan sirviendo.

Regla fundacional: **nada se genera sin storyboard aprobado** (decisión D-07).

## Los 12 campos — ni más, ni menos

| # | Campo | Contenido |
|---|---|---|
| 1 | `shot_id` | `SC{escena}_SH{plano}`. Idéntico en storyboard, archivos y registros (`SC03_SH012` → `SC03_SH012.png` / `.mp4`) |
| 2 | `scene` | Escena narrativa: un bloque de 40-60 s del guion |
| 3 | `duration_s` | **8-14 s por panel.** Se marca ESTIMADO si aún no hay audio medido |
| 4 | `shot_size` | `wide` / `medium` / `medium_close` / `close_up` / `extreme_close_up` / `insert` |
| 5 | `angle` | `eye_level` / `low` / `high` / `overhead` / `dutch` |
| 6 | `camera_move` | `{type, speed}` — **un** movimiento dominante (`static`/`pan`/`tilt`/`dolly`/`tracking`/`crane`/`push_in`/`orbit`) con velocidad explícita. Máximo un movimiento brusco por video |
| 7 | `subject` | El personaje (ficha literal) o el objeto/escena si no aparece |
| 8 | `action` | **Una** acción visible, 1-2 frases. Comportamiento observable, nunca una emoción abstracta |
| 9 | `environment` | Lugar + iluminación + paleta **nombrada**, no genérica |
| 10 | `emotion_beat` | Función narrativa: `hook` / `tension` / `vulnerability` / `threat` / `revelation` / `relief` / `close` |
| 11 | `image_prompt` | Prompt de imagen completo, construido por plantilla — nunca improvisado |
| 12 | `video_action_prompt` | Prompt de movimiento, más `transition_out` y `vo_text` con su marca de tiempo |

Un panel al que le falta un campo es un panel que se va a improvisar en la generación. No cuenta
como terminado.

## Reglas de ritmo (contra el "video cuadriculado" — error E-02)
- **Ningún plano sostenido más de 5 s** sin cambio real de ángulo, escala o movimiento.
- La **escala de plano varía** entre paneles consecutivos. Dos planos medios seguidos son un
  error de montaje, no una elección.
- Las **transiciones se deciden aquí**, no en el ensamblaje.
- **Un ancla dura cada 20-30 s** (dato exacto o nombre propio) y **un bucle abierto cada 60-90 s**.
  El ritmo narrativo se planifica en el panel; no se arregla después.
- **Giro meta al 65-72%** del video, marcado en el storyboard.

## Checklist de entrega (se rellena al final del documento, punto por punto)
- [ ] Los 12 campos, en **todos** los paneles
- [ ] Ningún `duration_s` mayor de 14 s
- [ ] Ningún plano sostenido >5 s sin cambio real
- [ ] `shot_size` varía entre paneles consecutivos
- [ ] Continuidad de personaje declarada contra la referencia publicada
- [ ] Rasgos prohibidos declarados en negativo en cada `image_prompt`
- [ ] Ancla dura cada 20-30 s, marcada
- [ ] Bucle abierto cada 60-90 s, marcado
- [ ] Giro meta situado entre el 65% y el 72%
- [ ] Cierre = inversión citable del título, no un resumen
- [ ] Llamada a comentar un número al 40% y al 85-90%, nunca antes del minuto 3
- [ ] Cero petición hablada de suscripción (decisión D-03)
- [ ] Capa de sonido declarada por panel
- [ ] Suma de `duration_s` cuadra con la duración objetivo (9-14 min)
- [ ] **Aprobado por David o Kimi** — un agente no aprueba su propio storyboard

## Archivos por video
- `STORYBOARD_<video>_v<N>.md` — legible, para revisión humana
- `storyboard_<video>_v<N>.json` — consumible por los scripts (esquema en `esquema-storyboard.json`)

Las versiones no se sobrescriben: `v1`, `v2`, `v3` conviven. La superada se marca OBSOLETA
arriba del archivo, apuntando a la que la reemplaza.
