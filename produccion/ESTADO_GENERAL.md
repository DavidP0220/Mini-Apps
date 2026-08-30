# Estado general del canal — dos videos en vuelo

Actualizado 2026-08-30 tras el reporte del Claude del PC.

## Video 5 — *The Psychology Of People Who Can't Stop Scrolling*

**Titulo cerrado por David. No se reabre.** 195 planos x 4 s = 13:00.
Tema: dopamina como sistema de busqueda ancestral, Skinner 1937 (razon
variable), el algoritmo como caja de Skinner, salida por diseno del entorno.

Hecho y verificado (vive en `CLAUDE AUTOMATIC/` del PC de David):

- 195 imagenes descargadas de Google Flow, 121 MB
- guion sincronizado plano a plano, 195 filas
- narracion en ingles, 1.887 palabras
- **voz en off ya generada: Edge TTS `en-US-AndrewNeural`, gratis, 10:46**
- 10 hojas indice · 0 duplicados reales

Pendiente:

| # | Que | Quien |
|---|---|---|
| 1 | animar los 195 clips en VideoExpress 3.0 | **David + Claude juntos, paso a paso** |
| 2 | resolver 2:14 de diferencia entre voz (10:46) y video (13:00) | los dos |
| 3 | escalar de 1376x768 a 1920x1080 | Claude |
| 4 | subtitulos | Claude |
| 5 | miniatura | Claude propone, David aprueba |
| 6 | respaldo en la nube de las 195 | Claude |
| 7 | publicar — **jueves o domingo, nunca lunes** | David |

## Video 7 — *Why Didn't Evolution Remove Your Fear of Being Seen?*

Miniatura `DONT BE SEEN`. 225 planos, 15:03. Guion completo y verificado,
40 de 225 escenas escritas, imagenes por generar en Artistly.

**Va detras del video 5.** El 5 esta a tres tareas de publicarse; el 7 esta a
185 escenas y 225 generaciones.

---

## Canon del canal (del documento del PC, no se negocia)

- **Solo Artistly** para imagenes y miniaturas. **Solo VideoExpress 3.0** para
  animar. Nunca al reves. **Dreamina prohibido.**
- Minimo **180 imagenes** por video.
- Minimo **1080p** siempre.
- **Subtitulos:** Arial Bold, MAYUSCULAS, amarillo, contorno negro, tercio
  inferior, **3-4 palabras** por bloque.
- **Doble respaldo:** local + nube. Sin las dos copias el trabajo no esta hecho.
- Nada se publica sin OK explicito de David.
- Todo en espanol con David.

---

## Dos choques detectados y como quedan

**1. Duracion del plano.** El documento del PC dice *"4 segundos por plano, sin
excepcion"*. El 2026-08-30 David dijo, sobre la duracion variable siguiendo la
voz: *"DEBEMOS USAR ESTO... ESA ES LA MANERA CORRECTA DE HACERLO"*.

Queda asi: **la instruccion nueva manda**, y no contradice el motivo de la
regla vieja. El motivo era *corte frecuente = retencion*. La curva de ritmo
conserva la media en 4,0 s y ademas **acelera el hook a 3,1 s de media**, que
es donde de verdad se pierde la audiencia. Se corta mas, no menos.
Aplica al video 7. **El video 5 ya esta cortado a 4 s fijos: no se rehace.**

**2. Subtitulos.** Yo habia adoptado palabra por palabra. El canon del canal
dice **3-4 palabras**. Manda el canon: Arial Bold, mayusculas, amarillo,
contorno negro, tercio inferior.

---

## Voz en off — hallazgo aprovechable

El video 5 uso **Edge TTS con `en-US-AndrewNeural`, gratis**. Sirve igual para
el video 7: permite medir la duracion real con ffprobe antes de montar, en vez
de estimar a 158 wpm.
