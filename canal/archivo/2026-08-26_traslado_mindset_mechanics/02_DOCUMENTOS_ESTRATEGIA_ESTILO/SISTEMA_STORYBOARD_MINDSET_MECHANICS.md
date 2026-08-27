# SISTEMA DE STORYBOARD — Mindset Mechanics (BIBLIA OPERATIVA)
**Versión 1.2 · 2026-08-26 · Base: Kimi Code (v1.0/v1.1, 3 frentes de investigación + taiarts.com). v1.2 por storyboard-director: ritmo repartido (§5.1), capas espaciales y aviso de negativos (§4), banderas de riesgo obligatorias (§8) — todo derivado de `MANUAL_PRODUCCION.md` §3.2.**
**ESTATUS: OBLIGATORIO. Ningún video entra a generación sin su storyboard aprobado. Es el paso entre guion y producción — cero excepciones.**

> El storyboard no es una obra de arte: es un documento de planificación. Se juzga por si el pipeline puede producir a partir de él sin improvisar nada. Detectar un error aquí cuesta 0 créditos; detectarlo tras generar cuesta 12 (ya lo pagamos dos veces).

---

## 1. Dónde vive en el pipeline (nuevo flujo oficial)

```
Guion (playbook) → Voiceover TTS → medición ffprobe → ★ STORYBOARD (este sistema) ★
→ Gate: David aprueba storyboard → Stills en Recraft (1 por panel, validados contra
frames publicados) → import_local_image() → animación VideoExpress (image-to-video)
→ ensamblaje (voz + subtítulos + badge) → QA → publicación (fecha fijada por Kimi)
```

Regla de posición: **ni sobre guion inestable ni tan tarde que no haya tiempo de corregir lo que revele.** El storyboard va inmediatamente después de tener audio medido.

## 2. Anatomía del panel — los 12 campos obligatorios

Cada panel/sub-clip es un registro con EXACTAMENTE estos campos (ni más ni menos):

| # | Campo | Contenido |
|---|---|---|
| 1 | `shot_id` | Formato `SC{escena}_SH{plano}` — idéntico en storyboard, archivos y logs (SC03_SH012 → SC03_SH012.png / .mp4) |
| 2 | `scene` | Escena narrativa (bloque de 40-60s del guion) |
| 3 | `duration_s` | 8-14s por panel. Marcado ESTIMADO si no hay audio medido |
| 4 | `shot_size` | wide / medium / medium_close / close_up / extreme_close_up / insert |
| 5 | `angle` | eye_level / low / high / overhead / dutch |
| 6 | `camera_move` | `{type, speed}` — UN movimiento dominante (static/pan/tilt/dolly/tracking/crane/push_in/orbit), velocidad explícita (slow/smooth/steady; whip máx 1 por video) |
| 7 | `subject` | `HOST` (ficha verbatim) u objeto/escena sin host |
| 8 | `action` | UNA acción visible, 1-2 frases. Comportamiento visible, nunca emoción abstracta |
| 9 | `environment` | Lugar + iluminación + paleta (nombrada, no genérica: "warm golden-hour grade") |
| 10 | `emotion_beat` | Función narrativa: hook / tensión / vulnerabilidad / amenaza / revelación / alivio / cierre |
| 11 | `image_prompt` | Prompt Recraft completo construido por plantilla (§4) |
| 12 | `video_action_prompt` | Prompt de movimiento para VideoExpress (§4) + `transition_out` + `vo_text` con timecode |

## 3. Esquema canónico JSON (consumible por scripts)

Un archivo por video: `storyboard_{video}.json`. Ensamblaje determinista: ffmpeg concat por `shot_id`.

```json
{
  "video": "resilience_v3",
  "audio_total_s": 553.4,
  "shots": [
    {
      "shot_id": "SC01_SH001",
      "scene": 1,
      "duration_s": 12,
      "shot_size": "medium",
      "angle": "eye_level",
      "camera_move": {"type": "push_in", "speed": "slow"},
      "subject": "HOST",
      "action": "sits at conference table, opens mouth to speak, freezes",
      "environment": "office meeting room, evening, warm lamp light",
      "emotion_beat": "hook",
      "image_prompt": "<construido por plantilla §4>",
      "video_action_prompt": "<construido por plantilla §4>",
      "transition_out": "hard_cut",
      "vo_text": "Picture this: you're in a high-stakes meeting...",
      "vo_tc": "0:00-0:12",
      "status": "pending"
    }
  ]
}
```

## 4. Plantillas de construcción de prompts (derivación mecánica, sin ambigüedad)

**Image Prompt (Recraft) — orden fijo de tokens (v1.2):**
```
[FICHA_PERSONAJE_VERBATIM si subject=HOST] + [shot_size + angle] + [action]
+ [CAPAS: foreground / midground / background]        ← nuevo v1.2
+ [environment + grade nombrado] + [BLOQUE_ESTILO_FIJO] + [NEGATIVOS — ver aviso abajo]
```
**Capas (nuevo v1.2, `MANUAL_PRODUCCION.md` §3.2.4):** declarar explícitamente qué hay en primer plano, plano medio y fondo (*"host in midground, blurred colleague silhouettes in background, edge of the table in foreground"*). La regla de tercios coloca **un** punto de interés; las capas le quitan al generador la decisión de dónde va **todo lo demás**. La capa del sujeto se nombra siempre aunque sea obvia. Los inserts declaran foreground y background aunque el midground quede vacío.

**⚠️ AVISO v1.2 sobre los negativos — conflicto abierto con `ESTILO_MINDSET_MECHANICS.md` §6.bis.**
§6.bis (regla dura, 2026-08-25) prohíbe escribir los negativos dentro del prompt positivo: los modelos de difusión no entienden la negación y los tokens `ears`/`nose` acaban condicionando **en positivo** — es la causa raíz diagnosticada de las orejas/narices que forzaron dos rondas rechazadas. §6.bis remite al parámetro `negative_prompt` de la API, **pero esa vía no está disponible en el camino por defecto:** `recraft_ai/generate_scene.py` usa `recraftv4_1` y `recraft_client.py` (líneas 87 y 136) sólo admite `negative_prompt` en V2/V3; tampoco existe hoy la constante `NEGATIVE_PROMPT` que §6.bis da por hecha. Hasta que Kimi decida entre **(a)** redactar los negativos en positivo o **(b)** mover la generación a `recraftv3 @1820x1024`, ningún storyboard nuevo debe darse por cerrado en este punto: se marca como bandera de riesgo del storyboard (ver el piloto, §6, bandera R2).

**Video Action Prompt (VideoExpress) — fórmula v1.1 (con blindaje anti-deriva 2D):**
```
"Flat 2D vector illustration style, solid colors, no 3D rendering, not photorealistic, 2D only." + [camera_move.type + speed + dirección] + [micro-movimiento del sujeto: 1 acción visible] + [1-2 movimientos ambientales: polvo/luz/ropa] + "Keep character identity, face and proportions unchanged. No cuts, no warping, no flicker. Stable camera, smooth motion."
```
**Reglas anti-deriva 2D (v1.1, investigación ola 2):**
- La identidad vive en la IMAGEN, no en el prompt — el prompt de video solo describe movimiento
- **PROHIBIDO orbit/rotación alrededor del personaje con cara visible** y giros de cabeza amplios: fuerzan volumen 3D y la IA inventa rasgos (orejas/nariz — nuestro defecto exacto). Movimientos seguros: push-in, pull-back, pan/tilt lentos, static con movimiento interno
- Micro-vida facial: solo `blinks once, natural breathing` — nunca varias expresiones por clip
- **Hard cut entre clips del mismo personaje, NUNCA crossfade** (el crossfade superpone dos "versiones" y exhibe la deriva). Crossfade solo para cambio de escenario/tiempo

Reglas duras de prompts:
- Ficha de personaje VERBATIM siempre (cero sinónimos: si dice "grey hoodie" nunca "gray sweatshirt")
- Cambiar UNA sola variable entre paneles (acción O ángulo — nunca vestuario+estilo)
- Prompt de imagen: 5-7 detalles distintivos, nunca >150 palabras
- La composición del frame debe pensar en el movimiento: dejar espacio en el encuadre hacia donde viaja la cámara
- Composición por regla de tercios (ojos en intersección superior); centrar SOLO para confrontación directa (giro meta)
- Cero texto en imagen — subtítulos solo en post

## 5. Reglas de ritmo y retención (investigación aplicada)

1. **Densidad de corte:** 4 sub-clips por escena de 40-60s → un video de 10-13 min = ~50-60 paneles. Densidad de referencia para documental: **5-10 cortes/min** (40/min ya es demasiado rápido).
   **⚠️ CORREGIDO v1.2 (2026-08-26) — la cadencia NO es fija.** La versión anterior de este punto pedía "cambio visual cada 10-14s, ASL 8-12s", es decir una cadencia **uniforme**; la investigación de retención de 2026 dice que la variación intencional de ritmo importa más que la velocidad de corte, y que la uniformidad es lo que agota. Regla vigente (`MANUAL_PRODUCCION.md` §3.2.1): **ningún par de paneles consecutivos dura lo mismo**; rango operativo **4-8s**, con 9-10s reservado a la exhalación de cierre de acto (y marcado como riesgo de deriva 2D, que se acumula con la duración del clip); **el plano más corto de cada segmento cae sobre el pattern interrupt**. Los tres patrones ejecutables (progresivo / respiración / ráfaga) están descritos en el manual. Ejemplo aplicado y reversible: `storyboards/STORYBOARD_resilience_v3_piloto_SC01-SC02.md` §5.
2. **Un panel = una idea = 1-2 frases de VO.** Si un plano sobrevive a su frase, es diapositiva; si corta más rápido que la VO, agota.
3. **Pattern interrupt obligatorio a los 25-35s** (donde el espectador nuevo decide irse) y cada 2-3 min: cambio brusco de escala, silencio, o insert de detalle.
4. **Anti-cuadrícula:** nunca 2 planos del mismo tamaño seguidos; alternar dirección de movimiento de cámara entre planos consecutivos; insertar un `insert` (detalle) tras 2-3 planos de personaje.
5. **Micro-movimiento en todo frame:** ningún plano nace estático del todo; mínimo deriva lenta o partículas/luz en movimiento.
6. **Hook visual 0-30s:** abrir a mitad de acción (el host ya atrapado en el problema), 3-4 escalas de plano en los primeros 30s, cero intro/logo/saludo.
7. **Sostén el plano fuerte 1-2s más de lo cómodo tras la frase clave** (la quietud leída como confianza amplifica el impacto — úsalo 1-2 veces por video, no más).

## 6. Mapa beat emocional → plano (obligatorio)

| Beat | Plano/ángulo/cámara |
|---|---|
| Hook / peligro inmediato | medium → push_in slow, eye_level |
| Tensión psicológica | extreme_close_up + dutch + handheld tremor sutil |
| Vulnerabilidad ("tu cerebro te sabotea") | high/overhead, host pequeño en el entorno |
| Amenaza (el mecanismo antiguo) | low angle, el estímulo domina el frame desde abajo |
| Revelación / insight | orbit o crane-out de close a wide — abrir espacio = abrir comprensión |
| Alivio / técnica | close_up perfil, dolly slow, luz cálida amanecer |
| Direct address (CTA) | medium_close, cámara quieta, mirada a cámara, tercio superior |
| Cierre | pull_back + crane up, wide, horizonte abierto |

Arco por acto (manual §3.1): apertura aérea/establecedora → medios con tracking/push → clímax con orbit → cierre con pull-back. UNA vez por acto.

## 7. Continuidad (reglas de oro entre paneles)

- **Eje de 180°:** la cámara no cruza la línea de acción salvo movimiento visible intencional
- **Screen direction:** si el host avanza izquierda→derecha, mantiene esa dirección entre paneles
- **Raccord de movimiento:** cortar en mitad del gesto; la acción continúa en el siguiente plano
- **Raccord de mirada:** si mira arriba-derecha, el siguiente plano muestra lo que ve desde ese eje
- Si el panel N cierra en primer plano, el N+1 abre en plano abierto (y viceversa)

## 8. Checklist de auto-verificación (15 puntos, ANTES de entregar)

1. ☐ Cada panel tiene los 12 campos completos
2. ☐ Ficha de personaje verbatim en TODOS los image_prompt con HOST
3. ☐ Cero paneles con mismo shot_size consecutivo
4. ☐ Ningún frame congelado previsto >4s
5. ☐ Un solo movimiento de cámara dominante por panel, velocidad explícita
6. ☐ Pattern interrupt colocado a 25-35s y cada 2-3 min
7. ☐ Beats emocionales mapeados según §6
8. ☐ Acciones descritas como comportamiento visible (no emociones)
9. ☐ Eje de 180° y screen direction verificados en toda la secuencia
10. ☐ Cero texto dentro de las imágenes en todos los prompts
11. ☐ Negativos resueltos según §4 (⚠️ NO darlo por hecho copiando la cláusula al final del prompt positivo: eso choca con `ESTILO` §6.bis — ver aviso en §4 y anotarlo como bandera de riesgo)
12. ☐ vo_text de cada panel cuadra con el timecode del audio real
13. ☐ Duraciones suman el total del audio (±3s)
14. ☐ Transiciones variadas (no el mismo fundido en todos los cortes)
15. ☐ Prueba de rejilla mental: ¿mismo personaje reconocible en todos los paneles?
16. ☐ **(v1.2)** Ritmo repartido, no plano: ningún par de paneles consecutivos con la misma duración; plano más corto sobre el pattern interrupt (§5.1)
17. ☐ **(v1.2)** Capas foreground/midground/background declaradas en cada image_prompt (§4)
18. ☐ **(v1.2)** Sección de **banderas de riesgo** presente, aunque esté vacía: cada storyboard declara qué puede salir mal y qué decisión ajena está pendiente (créditos, negativos, assets de audio, paneles fuera de la ventana segura de 5-8s)

## 8.5 Capa de sonido (v1.1 — obligatoria en storyboards completos)

Cada panel lleva además un bloque `AUDIO` ejecutable por editor/ffmpeg:

```
AUDIO:
  musica:    <track_id|continua|cut|fadeout:2s|none>   # cut = music drop
  ambiente:  <asset_id|none>  amb_db: <-35>
  sfx:       [{id: "whoosh_04", t: "in", db: -12}, {id: "riser_02", t: "out-2.5s", db: -15}]
  ducking:   <on|off>          # sidechain de música bajo la voz, obligatorio con TTS
  silencio:  <none|pre:0.5s|post:0.8s>
  nota:      "..."
```

Reglas de sonido del canal:
- **Niveles:** voz -16 LUFS (master final -14 LUFS, limitador -1dB), música -18 a -24 dB bajo voz, SFX -10 a -20 dB, ambiente -30 a -40 dB continuo (sin ambiente el video "suena a lata")
- **Music drop:** 0,5-1,5s de corte musical antes de cada dato clave/reveal — es el pattern interrupt sonoro más barato
- **Cambio de música cada 60-120s** o por beat narrativo; BPM/mood por sección (hook 100-130 BPM percusivo; tensión: drones 60-80; revelación: hit + swell; cierre: acústico fade 2-4s)
- **Silencio total:** 1-2 por video máximo, 0,3-0,8s antes de la frase más importante
- **Whoosh** en transiciones entre escenas (no dentro de la misma escena); **riser** 2-4s antes de giros; **hit grave** en datos duros (máx 2-3/min)
- **Fuentes con licencia segura para YPP:** YouTube Audio Library + Pixabay (gratis, empezar) → Epidemic Sound al monetizar. Guardar certificado de licencia de cada pista
- La notación de sonido del storyboard piloto de Resiliencia se aplica en post sobre el ensamblaje (no requiere regenerar)

## 8.6 Diccionario visual del canal (v1.1)

Existe `DICCIONARIO_VISUAL_MINDSET_MECHANICS.md` (raíz del repo): el catálogo canonizado de metáforas visuales por concepto (Guardia roja = amígdala, Ingeniero azul = corteza prefrontal, el Desfase sabana/ciudad, etc.). **Todo storyboard se valida contra el diccionario: un concepto = un símbolo = un color, siempre.** Si un storyboard necesita un concepto no catalogado, se propone la metáfora nueva y Kimi la canoniza antes de producción.

## 9. Gobierno del sistema

- **Storyboard Director** (rol registrado): produce los storyboards, aplica esta biblia, auto-verifica
- **Kimi Code:** aprueba el storyboard a nivel estratégico, fija fechas, investiga mejoras diarias (frente de storyboard en agenda)
- **David:** gate final de storyboard antes de gastar 1 crédito (igual que el piloto de escenas)
- **Claude Code:** ejecuta el storyboard tal cual; si un panel es técnicamente inviable, NO improvisa — devuelve el panel marcado `status: blocked` con el motivo
- Errores descubiertos en producción se retroalimentan a esta biblia (versión++) — el sistema aprende
