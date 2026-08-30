# Plan de produccion — 225 imagenes unicas, consistencia perfecta

Decision de David: **cero reciclaje**. Cada sub-clip lleva su propia imagen.
225 sub-clips = 225 generaciones. La calidad manda.

---

## 1. Donde esta el riesgo ahora

Al no reciclar, el peligro ya no es que se vea repetido. Es la **deriva del
personaje a lo largo de 225 generaciones**. Artistly deja seleccionada como
referencia la ultima imagen que genero: si no se reselecciona el original,
la 50 desciende de la 49, la 51 de la 50, y para la 120 el host ya es otro
hombre. Nadie lo nota mientras genera. Se nota al montar el video.

**Por eso hay puntos de control obligatorios cada 20.**

---

## 2. Las 12 sesiones

225 imagenes a ~1,5 min = **5 a 6 horas** de trabajo real, partidas en
12 sesiones de media hora. Dos por dia: **una semana**.

| Sesion | Imagenes | Tramo del video |
|---|---|---|
| 1  | 001-020 | hook, 4 movimientos |
| 2  | 021-040 | la pregunta del titulo |
| 3  | 041-060 | explicacion facil y su muerte |
| 4  | 061-080 | explicacion social y su muerte |
| 5  | 081-100 | CTA "comment one / comment zero" |
| 6  | 101-120 | escena en 2a persona |
| 7  | 121-140 | el mecanismo evolutivo |
| 8  | 141-160 | giro oscuro, "I want to be honest" |
| 9  | 161-180 | giro meta, "And here's where it flips" |
| 10 | 181-200 | consecuencia |
| 11 | 201-215 | CTA "comment eight" |
| 12 | 216-225 | cierre e inversion citable |

**Nunca dos sesiones pegadas.** El error de la referencia aparece cuando uno
entra en piloto automatico.

---

## 3. El ciclo, imagen por imagen

1. Consistent Characters → **3d & 2d Style Images**
2. **Reseleccionar `HOST_CORRECTO.png`** ← el paso que decide todo
3. Poner **16:9**
4. Pegar el prompt del numero, completo
5. Generar **una sola**
6. Descargar y guardar como `SH0XX.png`
7. Volver al paso 2

---

## 4. Control de deriva — obligatorio al cerrar cada sesion

Abrir `SH001.png` y la ultima de la sesion, lado a lado:

- [ ] misma altura y ancho de cabeza
- [ ] gorra apoyada directo en el craneo, mismo azul
- [ ] dos ovalos negros macizos, mismo tamano
- [ ] costado de la cabeza: curva limpia de gorra a mandibula
- [ ] mismo grosor de contorno negro
- [ ] mismo tono crema de piel

Si una falla: **parar y rehacer esa sesion**. Nunca seguir "para no perder
lo hecho": la deriva no se devuelve sola, se acumula.

---

## 5. Lo que evita que se vea repetido (que no es el numero de imagenes)

La sensacion de repetido no viene de reciclar. Viene de que **todo se ve
igual encuadrado igual**. Reglas duras para el guion:

- **Nunca dos planos seguidos del mismo tamano.** Si el 47 es Medium shot,
  el 48 es Wide o Close-up.
- **El entorno cambia cada 5 a 8 planos.** Cama, calle, sabana, quirofano,
  interior del cuerpo, multitud.
- **Pattern interrupt cada 25-35 s:** un plano que rompe todo — silueta a
  contraluz, plano cenital, negro casi total, un solo color plano.
- **La emocion va en la escena, la luz y el encuadre.** La cara del host es
  siempre la misma: neutra, boca recta. Esa es la marca del canal.

---

## 6. Si una imagen sale casi bien

**Inpaint, jamas regenerar.** Regenerar da un hombre nuevo. El inpaint
conserva el 95% correcto y arregla solo el pedazo.

---

## 7. Nomenclatura

```
apendice/
  img/  SH001.png ... SH225.png
  LOTE_01.txt ... LOTE_12.txt
  HOST_CORRECTO.png
```

El numero del archivo es el numero de la hoja. VideoExpress se arma en
orden numerico, sin pensar.

---

## 8. Reparto

| Quien | Que |
|---|---|
| Claude (prompt maestro) | guion + las 225 escenas, de 20 en 20 |
| Claude (lote.py) | pega la ficha del personaje identica en las 225 |
| David | 12 sesiones en Artistly, con control cada 20 |
| VideoExpress 3.0 | movimiento de camara y montaje |

**Nota de costo:** 225 generaciones consumen creditos de Artistly. Vale la
pena revisar cuantos quedan antes de arrancar la sesion 1, para no quedarse
a mitad de camino con el guion ya montado.
