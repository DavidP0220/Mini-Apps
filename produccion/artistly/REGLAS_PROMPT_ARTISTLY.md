# Reglas de prompt para Artistly — Mindset Mechanics

Escritas el 2026-08-28 después de tres fallos consecutivos. **No son consejos.
Son barreras.** Cada una salió de una generación que costó dinero y tiempo.

---

## 1. Cero negaciones. Nunca. Ni una.

Artistly **ignora las negaciones y a veces dibuja justo lo que se le prohíbe.**
Verificado tres veces: un prompt con `NO nose`, `NO ears`, `NO hair`, `NO blush`
produjo nariz, oreja, pelo y rubor.

**Prohibido en el prompt:** `no`, `NO`, `without`, `never`, `avoid`, `remove`.

| Nunca escribir | Escribir esto |
|---|---|
| `NO nose, NO nostrils` | `between the eyes and the mouth the face is one continuous smooth unbroken plane` |
| `NO ears` | `the sides of his head are smooth and unbroken curves from cap to jaw` |
| `NO hair` | `a large, perfectly round, completely smooth bare scalp` |
| `NO blush` | `a single even cream tone across the whole face` |
| `no notification, no light` | `its surface entirely dark and empty, one uniform black rectangle` |
| `with no notepad and no pen` | `with both hands empty` |
| `no second shape overlapping` | `one continuous closed silhouette` |
| `NO text` | `the image is entirely wordless` |

**Antes de mandar un lote, buscar `\bno\b` en todos los prompts.** Si aparece
una sola vez, el lote no sale.

---

## 2. Un ojo en primer plano NO se llama ojo

Si el prompt dice *eye* en un plano cerrado, el modelo dibuja un ojo
anatómico: esclerótica blanca, iris, pupila y brillo. Pasó en `SC01_SH002`.

**Se describe como forma gráfica:**

> `one solid black oval shape, 100% solid black from edge to edge, a single flat
> silhouette of one uniform black, like a paper cut-out`

Y no se carga la ficha de personaje completa en un plano donde solo se ve un
fragmento de cara.

---

## 3. Los planos cerrados llevan la regla de silueta

En `close`, `medium_close` y `extreme_close`, Artistly a veces dibuja **un
segundo plano de cara sobresaliendo** por un lado, como un bulto.

Se previene añadiendo:

> `The head is drawn as one single unbroken oval outline, one continuous closed
> silhouette.`

---

## 4. La identidad viene de la imagen, no del texto

**El texto no impone estilo en Artistly.** Se comprobó tres veces:

- `AI Image Designer v6` ignoró `bold thick clean black outlines`, `flat solid
  blocks of colour`, `hard-edged cel shading` y `2D style` — las cinco.
- `Script To Storybook V2` puso ojos con iris, nariz y el título quemado.
- Lo plano **solo apareció** cuando vino copiado de `HOST_CORRECTO.png`.

**Única vía válida:** Consistent Characters → 3d & 2d Style Images, con
`HOST_CORRECTO.png` como referencia, una imagen por vez.

---

## 5. Mecánica de la interfaz

- **Reseleccionar la referencia antes de CADA generación.** Artistly deja
  seleccionada la última imagen generada y la usa como referencia de la
  siguiente: se deriva del original sin darse cuenta.
- **16:9 en cada generación.** Sale en 1:1 por defecto y no se queda puesto.
- **El campo de prompt no tiene límite de caracteres** (verificado en el DOM).
  Va el prompt entero, sin recortar.
- **La gorra se pide explícitamente en cada prompt.** Si la gorra tapa media
  cabeza, el modelo reconstruye pelo debajo.
- **Su CDN sirve JPEG bajo URL `.png`.** Convertir a PNG real con ffmpeg.
- Si falla un solo detalle: **inpaint, no regenerar.**
