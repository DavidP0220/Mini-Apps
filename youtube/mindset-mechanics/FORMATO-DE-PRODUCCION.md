# Formato de producción — Factory Settings

**Decidido el 2026-08-26.**

---

## 1. Formato: documental animado 2D con host consistente

Es el formato probado del nicho. `PLAYBOOK_MONETIZACION.md`:

| Canal | Formato | Resultado |
|---|---|---|
| **Zenn** | Documental animado 2D faceless, 8:00-8:40 | 32 videos → **179.000 subs**, **550.000 vistas de media** |
| ONLI | Personaje 2D, cabeza ovalada | 785.000 el video top |
| PsychToons | Cartoon 2D | — |
| Professor Stickman | Pictogramas | 200-540k por video con 24.400 subs |

Ningún ganador del nicho usa fotorrealismo. **Zenn es la tesis de este canal ejecutada a escala**, y lo
hace en 2D animado.

### Corrección registrada

Una versión anterior de este documento recomendaba imágenes fijas cinematográficas, argumentando que la
consistencia de personaje era un riesgo de producción. **Ese argumento era falso.**
`MANUAL_PRODUCCION.md` §5 dice textualmente:

> *"No bloquea producción — Técnica B (repetición textual, §2) ya está validada en vivo con resultado de
> alta fidelidad. Técnica A es una mejora a perseguir cuando haya tiempo, no un requisito para producir
> el canal hoy."*

La consistencia está resuelta y probada. El formato es 2D animado.

## 2. El host

`marca/personaje.png` — generado con IA, es la referencia visual canónica.

Cabeza grande ovalada, sin nariz, sin pelo, ojos óvalos negros planos sin iris, cejas finas oscuras
flotando por encima con hueco visible, boca pequeña y simple, piel crema plana, chaqueta de trabajo
gris oscuro. **Su firma: una pequeña luz ámbar encendida en la sien derecha**, que proyecta luz cálida
sobre ese lado de la cara — la máquina corriendo dentro del cráneo. Es lo que enlaza al personaje con
el nombre del canal.

### Ficha canónica — Técnica B (obligatoria)

Se pega **palabra por palabra, sin abreviar nunca**, al inicio de CADA Image Prompt de CADA escena.
Nunca escribir "same character" o "same host" — eso es exactamente lo que rompió el video de Resiliencia.

```
Flat 2D animated documentary character, large rounded oversized head, no nose,
no hair, plain black oval eyes with no iris and no highlight, thin dark eyebrows
floating high above the eyes with a visible gap, very small simple mouth low on
the face, flat cream skin, dark charcoal work jacket over a plain shirt, a small
soft amber indicator light glowing at his right temple casting warm orange light
across that side of his face, bold clean dark outlines, cel-shaded flat 2D
animated documentary style, consistent appearance across all scenes.
```

### Cláusula negativa (al final de cada Image Prompt)

```
Only the main character described — absolutely NO small side characters, NO
children, NO spectators, NO extra people in the corners or background. No text,
no letters, no signs or words anywhere in the image. No photorealism, no 3D
render, no comic panels, no halftone.
```

### Técnica A — mejora opcional

Subir `personaje.png` con `generate_video.py import-image` y activar "Consistent Character" +
"Prompt Enhancement". Según `MANUAL_PRODUCCION.md` §5, `mark_consistent_character()` todavía falla al
marcar una imagen subida a mano; el siguiente paso diagnosticado es generar una imagen con "Create
Image" teniendo la Reference Photo seleccionada, y revisar si el botón se habilita sobre ese resultado.
**No bloquea producción.**

## 3. Biblia visual

| Elemento | Regla |
|---|---|
| **Estilo** | Cel-shading 2D plano con iluminación cinematográfica. Contornos oscuros marcados. |
| **Paleta** | Fondo `#050A14` azul casi negro · acento `#FF9A2E` ámbar · luz fría azul de contrapunto |
| **Luz** | **Un solo foco cálido por plano.** El ámbar viene siempre de la sien del host o de una fuente de la escena. |
| **Los dos colores no se mezclan** | Ámbar = mecánica antigua. Azul frío = mundo moderno. Esa separación **es** la tesis. |
| **Personajes de fondo** | Aleatorios, nunca consistentes. Regla dura de VideoExpress: el toggle de Consistent Character se activa **solo** para el host. |
| **Texto en imagen** | **Prohibido.** Los subtítulos van quemados en post, nunca generados dentro de la imagen. |
| **Prohibido** | `comic`, `comic panel`, `halftone`, `vector`, `flat` como palabras de prompt · fotorrealismo · render 3D · fondos blancos |
| **Salida** | 1920×1080 mínimo, siempre. Shorts 1080×1920. |

## 4. Flujo por video

1. **Guion** — 1.500-2.000 palabras para 10-13 min, a 150-172 palabras/minuto.
2. **Desglose en ~50 escenas**, una cada ~15 segundos.
3. **Por escena:** ficha canónica del host + descripción de la escena + cláusula negativa → Image Prompt.
4. **Video Action Prompt** con el vocabulario de cámara de `MANUAL_PRODUCCION.md` §3.
5. **Subtítulos quemados** — obligatorios, de ellos dependen los recortes de Shorts.
6. **QA contra el checklist** de `ESTILO_MINDSET_MECHANICS.md` §7 antes de ensamblar.
7. **3-4 Shorts** recortados del largo con `make_ultrashorts.sh`: 12-18s, un hecho concreto, cero jerga
   clínica en la apertura, badge de suscripción, enlazados como Related Video.
8. **Miniatura**: frame del propio video + 2-3 palabras compuestas aparte, nunca generadas en la imagen.
