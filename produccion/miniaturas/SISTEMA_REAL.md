# El sistema de miniaturas del canal — leido de las miniaturas reales

Analizado el 2026-08-30 sobre `dMsnFlswfi8` (OVERTHINK EVERYTHING) y
`2xASNuYxalw` (IT'S BEING HUNTED), descargadas en maxresdefault.

**No es una descripcion de estilo. Es la plantilla.**

---

## EL HALLAZGO QUE EXPLICA EL ERROR ANTERIOR

**El host de las miniaturas NO es el host de los videos.**

| | En el video | En la miniatura |
|---|---|---|
| Nariz | no tiene | **si tiene** |
| Orejas | no tiene | **si tiene** |
| Expresion | neutra, boca recta | **boca abierta, cejas quebradas, ojos grandes** |
| Sombreado | plano, cel-shading duro | **volumen, luz de borde calida** |
| Textura | limpia | **desgastada, con grano** |

Son dos personajes distintos a proposito. El del video es plano y neutro
porque se repite 225 veces. El de la miniatura tiene cara, luz y detalle
porque compite contra otras nueve miniaturas en la pantalla.

**Por eso la miniatura que reemplazamos quedo "muy normal":** se genero con el
personaje plano del video. En miniatura, plano = invisible.

---

## La plantilla, elemento por elemento

**1. Fondo.** Negro casi total, o **division calido/frio**: masa clara y calida
a la izquierda, azul frio a la derecha. Contraste de valor extremo: es lo que
la hace legible a 210x118 px.

**2. Reparto del cuadro.** Texto en el 45% izquierdo. Imagen en el 55% derecho.
Siempre.

**2b. La escala. Esto es lo que mas subio la calidad.** La version nueva
abandona el plano medio del host y usa un **primer plano extremo**: un solo ojo
ocupando media miniatura, la cara cortada por los bordes. Un ojo enorme gana a
una persona entera. Ademas permite sudor, venas rojas y textura, que a tamano
de plano medio no se verian.

**3. El texto. La version nueva son CUATRO lineas:**

```
banda roja de brochazo   texto BLANCO pequeno en mayusculas    <- la premisa
palabra BLANCA enorme    contorno negro, textura desgastada
palabra AMARILLA enorme  con un brochazo rojo debajo           <- el golpe
barra NEGRA fina         texto blanco + UNA palabra en ROJO    <- la especificidad
```

Ejemplos reales, en orden de evolucion:

| banda roja | blanco | amarillo | barra negra |
|---|---|---|---|
| 95% OF PEOPLE | OVERTHINK | EVERYTHING | — |
| YOUR BRAIN THINKS | IT'S BEING | HUNTED | — |
| YOUR BRAIN THINKS | IT'S STILL | HUNTING | THE 40,000 YEAR OLD **GLITCH** |

La banda roja pone la premisa. El blanco arranca la frase. **El amarillo remata
con la palabra que duele.** Y la barra negra, que es lo nuevo, **mete un numero
concreto y una sola palabra en rojo**: el numero da credibilidad, la palabra
roja da el concepto. `40,000 YEAR OLD` + `GLITCH`.

Esa cuarta linea es la mejora. Un numero especifico convierte una frase
generica en una promesa concreta.

**4. Tipografia.** Condensada, muy alta y estrecha, tipo Anton. Mayusculas.
Contorno negro grueso. Textura rayada encima, no plana.

**5. Luz sobre el host.** Luz de borde calida naranja por un lado, contra el
fondo negro. Nunca iluminacion plana.

**6. Firma visual, arriba a la derecha.** Un garabato blanco enredado, signos
de interrogacion y rayos pequenos. Esta en las dos. Es marca de canal.

**7. Objeto de marca, abajo.** La taza negra que dice DISCIPLINE FOCUS FUTURE.
Aparece en las dos. Es lo que hace que se reconozcan como del mismo canal
antes de leer el titulo.

---

## Miniatura del video 7

*Why Didn't Evolution Remove Your Fear of Being Seen?*

**Texto. CERRADO por David el 2026-08-30:**

```
banda roja    →  IT'S NOT SHYNESS
blanco        →  YOUR BRAIN
amarillo      →  IS HIDING YOU              (subrayado rojo)
barra negra   →  AND IT LEARNED IT  300,000 YEARS AGO
```

Sigue la formula de la miniatura de `IT'S NOT AN ADDICTION`, que es la mejor
del canal, y no la de las anteriores:

- **La banda roja contradice**, no presenta. `IT'S NOT SHYNESS` le dice al
  espectador que lo que cree esta mal antes de que lea nada mas.
- **El texto grande es una frase completa**, con sujeto y verbo:
  `YOUR BRAIN IS HIDING YOU`. Un fragmento como `DON'T BE SEEN` describe;
  una frase con sujeto acusa.
- **La barra negra es una acusacion, no un dato.** `THE 40,000 YEAR OLD GLITCH`
  es informacion: la lees y ya sabes. `AND IT LEARNED IT 300,000 YEARS AGO`
  abre una pregunta que solo el video responde. Eso es lo que hace el clic.

El numero es 300.000 y no 40.000 por dos razones: es la cifra que afirma el
guion, y 40.000 ya se uso en la miniatura anterior. Repetir el mismo numero
entre videos le quita fuerza a los dos.

**Escena, con la escala nueva.** Primer plano extremo de la cara del host
cortada por los bordes, ocupando la mitad izquierda-centro. **Un ojo enorme muy
abierto**, con venas rojas y gotas de sudor bajando por la piel agrietada.
Sobre el ojo cae en diagonal **una franja de luz blanca y dura de reflector**.

En la mitad derecha, en el azul frio: **una pared de decenas de caras palidas
pequenas mirandolo**, tratadas con el mismo glitch de rayas y aberracion.

La ironia dramatica: **el reflector ya lo encontro.** El ojo esta reaccionando
a una luz que lleva rato encima.

Arriba a la derecha: el garabato blanco, los signos, los rayos.

---

---

## COMO SE CONSTRUYE — por codigo, no con IA generativa

Metodo del Claude del PC, 2026-08-30. Vive en `_miniaturas.py` y tarda
segundos en sacar cualquier variante.

**Generar la miniatura con IA es la via equivocada.** Componerla por codigo
desde las imagenes del propio video garantiza dos cosas que la IA no puede:
el personaje es exactamente el del video, y la tipografia es **identica** entre
miniaturas, no parecida. Ese era el problema que llevabamos meses arrastrando.

Los seis pasos:

1. **La base es un fotograma del propio video**, escalado a 1080p y recortado a
   1280x720 desplazando el encuadre para dejar al personaje a la derecha.
   No se genera nada nuevo.
2. **Degradado oscuro sobre el lado izquierdo**, suave. Es lo que le da al
   texto donde respirar y lo que lo hace legible a tamano pequeno.
3. **Texto en Anton** (de Google Fonts; la fuente del canal **no era Impact**),
   con el contorno negro dibujado en varias pasadas alrededor de cada letra.
4. **Textura de aranazos**: rayas y puntos al azar aplicados **solo sobre el
   relleno de la letra, nunca sobre el contorno**. Ese detalle es lo que da el
   aspecto desgastado de las miniaturas buenas.
5. **La banda roja no es un rectangulo**: es un poligono con los bordes
   irregulares al azar, para que parezca dada a brocha.
6. **Fusion de dos imagenes del video** con mascara desenfocada, para que la
   union no se note.

### El limite de este metodo, y cuando NO aplica

Recortar un fotograma solo sirve si los fotogramas tienen suficiente detalle.

- **Video 5:** sus imagenes vienen de Google Flow, con volumen y textura. El
  recorte funciona perfecto.
- **Video 7:** sus imagenes son **planas a proposito** — cel-shading, contorno
  duro, cara neutra. Recortar un fotograma plano da exactamente la miniatura
  sosa que ya rechazamos una vez.

**Regla:** en videos de estilo plano, la imagen base de la miniatura **se
genera aparte**, con detalle, volumen y expresion — y despues pasa por los
pasos 2 a 6 igual que las demas. La tipografia siempre por codigo. Lo unico
que cambia es de donde sale la base.

---

## Prueba obligatoria antes de aprobar

Bajarla a **210x118 px** y mirarla. Si el amarillo no se lee o el host se
vuelve una mancha, no sirve. Ese es el tamano al que la ve la mitad de la
audiencia.
