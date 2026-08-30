# Reporte de tanda — LOTE_01 — 2026-08-30

Escrito por el Claude del PC. Tanda **incompleta**: se detuvo en SH005 de 20.

---

## Generadas

| plano | estado | nota |
|---|---|---|
| SH001 | ok | wide, host en circulo de luz sobre negro. Limpia. |
| SH002 | rehacer | Artistly ignoro `seen from behind`: dibujo al host de frente. Ademas el publico salio con ojos anatomicos (esclerotica blanca, sonrisa) en vez de los `two small flat black oval marks` que pedia el prompt. |
| SH003 | ok | close-up en el podio, manos en el borde. La mejor del bloque. |
| SH004 | inpaint | la boca salio en curva de sonrisa; la marca del canal es boca recta y cara neutra. Corregir con ai-inpainter, no regenerar. |
| SH005 | rehacer | ya con el prompt corregido (Close-up). La sudadera no lee como sudadera: lee como un bulto/saco. El circulo de luz quedo separado del objeto, cuando el prompt pedia la luz cayendo **sobre** ella. |
| SH006 - SH020 | sin generar | tanda detenida, ver Bloqueos |

Formato de salida verificado en las 5: **PNG real 1344x768 (16:9)**.
Confirmado que el CDN de Artistly entrega **JPEG bajo nombre .png**; se
convierten con ffmpeg antes de guardar.

**Cero texto en las 5 imagenes.** La regla de "ninguna letra" se cumplio sin
una sola excepcion.

---

## Control de deriva

Comparacion de `SH001.png` contra `SH004.png` (la ultima con host):

- [x] alto y ancho de cabeza — igual
- [x] gorra apoyada en el craneo, mismo azul — igual
- [x] dos ovalos negros macizos, mismo tamano — igual
- [x] costado de la cabeza, curva limpia — igual, sin orejas
- [x] grosor del contorno negro — igual
- [ ] tono crema de la piel — **empieza a moverse**: SH001 es crema plano y
      parejo; SH003 y SH004 traen un bloque de sombra en pomulo y mandibula, y
      SH004 tira a un crema mas calido.

Veredicto: **se mantuvo**, con una senal temprana en el sombreado de la cara.
Con solo 5 planos no es concluyente. Hay que repetir el control con el bloque
de 20 completo antes de dar el bloque por bueno.

---

## Prompts que Artistly no obedecio

- **SH002** — pedia `seen from behind, shoulders raised toward his cap`.
  Dibujo al host de frente, centrado. Confirma la leccion 2 del reparto: las
  instrucciones de camara y de orientacion no significan nada para Artistly.
  Hay que describir la espalda **como objeto del cuadro**, no como punto de vista.
- **SH002** — pedia que el publico fuera `pale cream head shapes, each head
  carrying two small flat black oval marks`. Dibujo caras completas con ojos
  anatomicos y sonrisa. La regla del ojo como forma grafica (regla 2 de
  REGLAS_PROMPT_ARTISTLY) aplica tambien a las figuras de fondo, no solo al
  primer plano.
- **SH004** — pedia `a small black line for a mouth`. Dibujo una sonrisa.
  El prompt no ancla la expresion neutra; conviene decirlo como forma
  (`one short straight horizontal black line`).
- **SH005** — pedia `a single grey hoodie lying flat and abandoned`. Dibujo un
  bulto sin forma reconocible de prenda. Falta describir capucha, cordones y
  mangas como partes visibles del objeto.

No se corrigio ninguno desde el PC, conforme a la regla de oro.

---

## Creditos

Gastados en esta tanda: **6 generaciones** (SH001-SH005, mas la SH005 vieja con
el prompt anterior al `git pull`, que se descarto sin descargar).
Restantes: **sin verificar** — no encontre el contador en la interfaz. Si el
servidor sabe donde lo expone Artistly, que lo indique y lo reporto la proxima.

---

## Bloqueos

1. **`auditoria.py` sale en rojo (codigo 1).** Regla acatada: no se genera nada.
   Fallo unico: `escenas disenadas = 225 (40 - faltan 185)`.
   Todo lo demas paso: guion, los 8 beats, los 225 planos, duraciones, camara,
   sin negaciones, sin shot_id repetidos.

2. **Los bloques 1 y 2 no cuadran con su linea de voz.** Es el aviso 2 de la
   auditoria y se confirma al cruzar `LOTE_01.txt` con `PLANOS_VO.md`:

   | plano | linea de voz | lo que pide el prompt | cuadra |
   |---|---|---|---|
   | SH001 | Right before you speak in public, | host solo en el centro del escenario | si |
   | SH002 | your body does something you never asked it to do. | de espaldas ante el auditorio | flojo |
   | SH003 | Your chest tightens. Your hands go cold. | manos apretando el borde del podio | si |
   | SH004 | Something starts scanning the room — | capucha puesta, cara quieta dentro | **no** |
   | SH005 | not for danger, for faces. | sudadera tirada y abandonada | **no** |

   SH004 y SH005 ilustran lo contrario de lo que dice la voz: la linea habla de
   **buscar caras** y la imagen muestra **esconderse** y **ausencia**. Generar
   SH006-SH020 sobre esta base es gastar creditos en planos que hay que rehacer.

3. **Seleccion de la referencia, riesgo activo.** Artistly deja preseleccionada
   la ultima imagen generada. En un ciclo un clic desviado dejo puesta
   `prompt-to-image-b08b688f-...png` (SH004, 119 KB) como referencia en vez de
   HOST_CORRECTO. Se detecto con verificacion en el DOM antes de generar y se
   corrigio; **no se gasto credito**. Ya no se usan coordenadas fijas: se
   verifica el nombre del archivo de referencia antes de cada `Generate Image`
   y si no dice `3d-2d-style-images-d329cded-...` (1.2 MB) no se genera.

---

## Lo que necesita el PC para reanudar

- Las 185 escenas que faltan, o al menos el visto bueno de que se puede seguir
  con el bloque 1 mientras tanto.
- Los bloques 1 y 2 revisados plano por plano contra `PLANOS_VO.md`.
- SH002, SH004 y SH005 reescritos en `escenas.py` con las correcciones de arriba.
- Confirmacion de si `Quantity` desaparecio de la interfaz a proposito: en el
  build actual de Artistly **ese campo ya no existe**, y el README todavia pide
  ponerlo en 2.

## Nota de interfaz, para actualizar los documentos

`https://app.artistly.ai/consistent-character-3d` **esta muerta**: el build
actual responde `Page component not found: ConsistentCharacter3D` y deja la
pagina en blanco. La ruta viva es:

```
https://app.artistly.ai/ai/consistent-characters
```

Hay que corregirla en `README_PARA_CLAUDE_PC.md` e `INTERFAZ_ARTISTLY.md`.
