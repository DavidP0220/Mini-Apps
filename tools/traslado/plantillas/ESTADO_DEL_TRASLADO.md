# ESTADO DEL TRASLADO — Mindset Mechanics · corte {{FECHA}}

Dos cosas distintas en un mismo documento:
**(A)** en qué punto está el proyecto, y **(B)** qué entró en este paquete y qué no.

---

## A. Dónde está parado el proyecto (último día registrado: 2026-08-26)

### El bloqueo principal
La producción visual está **detenida a la espera de una decisión de David: los 5 USD de saldo
de la API de Recraft.** No es un problema técnico y no está esperando a nadie más.

Ese bloqueo **no es solo del video de Resiliencia** — es el pipeline visual válido para
*cualquier* video nuevo. Hay una salida parcial ya identificada: **630 créditos ya pagados en
la vía web de Recraft**, más lenta y frágil, utilizable si David la autoriza mientras se
resuelve el pago de la API.

### El pipeline oficial vigente

```
Guion → TTS + ffprobe (duración real) → STORYBOARD → [GATE humano]
   → stills en Recraft AI (1 por panel, validados contra material publicado)
   → import_local_image() a VideoExpress
   → animate_library_image() con Video Action Prompt (image-to-video)
   → ensamblaje ffmpeg (sub-clips reales, transiciones variadas, audio -14 LUFS)
   → QA técnico + [GATE humano] → publicación
```

### Estado real de los videos (verificado contra archivos, no asumido)

| Video | Guion | Storyboard | Producción visual |
|---|---|---|---|
| **Resiliencia** ("Why Your Brain Breaks Under Pressure") | Completo (19-ago) | v1.1 — 15 paneles, 94 s del piloto, escenas 1-2 de 12 | **Rehaciéndose desde cero.** La versión v2 ya renderizada la rechazó David por verse "cuadriculada y estática" → pivote a la 3ª vía (Recraft + storyboard) |
| **Social Anxiety** ("Why Didn't Evolution Remove Social Anxiety?") | Completo (22-ago, ~1.680 palabras, 10:30-11:00) | **No existe** | Cero. Es el mejor candidato: no arrastra el problema de calidad ya rechazado |
| **Attention Span** | **No existe** — solo la idea en el playbook | — | — |
| **Jealousy** | **No existe** — solo la idea en el playbook | — | — |

> Corrección importante que el plan anterior no reflejaba: hay **2 guiones reales, no 4**.
> Escribir los otros dos es el cuello de botella oculto de la cadencia de publicación.

### Siguiente paso concreto, en orden

1. **storyboard-director** → construir el storyboard técnico completo de **Social Anxiety**
   antes de generar ninguna imagen. Coste: **0 créditos**, es planeación.
2. **Decisión de David** (pendiente, ya escalada) → aprobar los 5 USD de la API de Recraft, o
   autorizar los 630 créditos web ya pagados.
3. Solo después: animación en VideoExpress con 3 sub-clips reales de 12-18 s por escena.

### Otros pendientes abiertos que dependen de la máquina de David
- **Respaldo de los ~669 MB de video existentes.** No caben en git y las plataformas borran
  los originales a los 60 días. Es un riesgo real de pérdida, sigue sin resolverse.
- **Acceso a navegador / YouTube Studio**: el post de Comunidad (encuesta ya redactada) y la
  verificación del CTA "mira el video completo" en los 14 Shorts y 4 largos están escritos y
  listos, pero **nadie los ha ejecutado** porque las sesiones remotas no tienen navegador.
- **Retitular** el archivo de Resiliencia al título de fórmula C del playbook.

### Contexto de monetización que cambió hace días (no ignorar)
- YouTube **duplicó la barra del YPP**: 8.000 horas (antes 4.000) o 20 M vistas de Shorts,
  1.000 subs se mantiene. **Entra en vigor el 1-feb-2027** y solo afecta a quien no esté ya
  *aceptado* dentro del programa para esa fecha. El objetivo no es "estar cerca": es **estar
  dentro** antes de esa fecha.
- YouTube cambió el conteo de vistas públicas (desde el fotograma 1). **No cambia la
  elegibilidad al YPP**: el progreso real se mide en *Engaged Watch Hours* (Studio → Analytics
  → Advanced Mode), no en el contador público.
- **Test & Compare** elige la variante con más *watch time por impresión*, no la de más CTR:
  las variantes deben ser ángulos genuinamente distintos, no retoques del mismo texto.
- **Función Collab** (hasta 10 creadores etiquetados, con botón de suscripción propio sobre el
  video): palanca de crecimiento detectada y **todavía sin usar** por el canal.

---

## B. Qué entró en este paquete y qué falta

### Entró — completo y verificado
- **{{N_ARBOL}} archivos** del árbol de traslado ({{PESO}}), más **{{N_DESEMP}}** rescatados
  del interior de los zips anidados.
- **Todo el trabajo con Kimi-Claude**: 27 handoffs/reportes/revisiones + el paquete
  `HANDOFF_KIMI_PACKAGE` + `HANDOFF_KIMI_CODE_COMPLETO.txt` (510 KB de historial).
- Los **3 paquetes de conocimiento** (v1 del 23-ago, v2 del 23-ago, v3 del 25-ago), tanto en
  `.zip` original como ya desempaquetados.
- **{{N_UNICOS}} archivos que solo existían dentro de esos zips** — entre ellos los 8 agentes
  de Claude Code, `ERRORES_QUE_NO_SE_DEBEN_REPETIR.md`, `MANIFIESTO.md`,
  `SISTEMA_STORYBOARD_MINDSET_MECHANICS.md`, `DICCIONARIO_VISUAL`, `POLITICA_IDIOMAS.md`, el
  storyboard v3 del piloto (JSON + MD), `script_social_anxiety_video.md`, `video_understand.py`
  y `check_video_specs.py`. Listado exacto en `UNICOS_EN_ZIPS_INTERNOS.md`.
- **Todo el código** de `youtube_pipeline/`, `video_express_ai/`, `recraft_ai/` y
  `shorts_final/`, con sus configs, requirements y logs de generación.
- Los assets generados (imágenes de escenas, referencias de personaje, voces en off, frames de
  prueba), en volúmenes numerados.

### NO entró — hay que pedirlo aparte

1. **Las partes 5, 6 y 7 de 7** del reparto original (`TRASLADO_MM_parte_5_de_7.zip` …
   `parte_7_de_7.zip`). Este paquete se armó con las partes **1 a 4**.
   Se sabe que falta contenido porque `COMO_UNIRLOS.txt` describe un
   `LEEME_PRIMERO_TRASLADO.md` en la raíz del paquete original **que no está en las partes
   1-4**, y porque la numeración de carpetas se corta en `03_`.
2. **Los ~669 MB de video renderizado** (`resilience_final_v2.mp4` y demás). No estaban en el
   origen: no caben en git y su respaldo sigue siendo un pendiente abierto.
3. **Los `.env` reales.** Nunca viajan, y está bien que sea así. La cuenta nueva necesitará sus
   propias claves: YouTube Data API, Anthropic, ElevenLabs, Gemini, Recraft y las credenciales
   de VideoExpress.

> **Cuando lleguen las partes 5-7:** se vuelve a ejecutar
> `bash tools/traslado/armar-traslado.sh <carpeta_fusionada> <salida>` sobre el árbol completo
> y se regenera el paquete entero — inventario, manifiesto y reporte de únicos incluidos. No
> hay que rehacer nada a mano.

---

## C. Cómo verificar que no se perdió nada al copiar

```bash
# dentro de la carpeta donde extrajiste TODOS los zips de paquetes/
sha256sum -c MANIFIESTO_SHA256.txt
```

Si algo aparece como `FAILED` o `No existe el archivo`, ese archivo se corrompió o no se
extrajo — se vuelve a sacar del zip que lo contiene, según `INVENTARIO_COMPLETO.md`.
