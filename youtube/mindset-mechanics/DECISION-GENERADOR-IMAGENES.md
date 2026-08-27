# Decisión final — generador de imágenes para producción en masa

**Investigado el 2026-08-27.** Precios verificados en fuentes independientes.

---

## 1. Qué significa "ilimitado" en cada opción

Ninguna herramienta comercial es realmente ilimitada. Estos son los topes reales:

| Herramienta | Precio | Tope real |
|---|---|---|
| **Artistly** | **$49 pago único** (Commercial) · $147 (Premium) | *"Ilimitado"* con **límite de uso justo de 400 imágenes/día**. Y su propio ToS aclara que *"lifetime"* significa **la vida comercial del producto, no la tuya** |
| **ChatGPT Plus** | $20/mes | ~**50 imágenes por ventana móvil de 3 h** ≈ 200/día en el mejor caso. Cada imagen consume además del límite de 160 mensajes |
| **Midjourney** | $30/mes (Standard) | Relax ilimitado, pero operación manual |
| **LTX Studio** | $15 / $35 / $125 mes | Plataforma de **video**, no de imagen. Ilimitado solo en Enterprise |
| **Atlabs** | $30 / $75 mes | Plataforma de **video**. El plan Pro da 10 exports |
| **API FLUX schnell** | $0,0012–0,003 / imagen | Sin tope. 1.000 imágenes = **$1,20 a $3** |
| **ComfyUI local** | **$0 por imagen, para siempre** | **El único realmente ilimitado.** Requiere GPU |

**Conclusión del punto 1:** el único "sin límites" verdadero es ComfyUI local. Artistly no es ilimitado
—son 400/día— y su "lifetime" depende de que la empresa siga existiendo.

---

## 2. La restricción que decide, y que no aparece en ninguna comparativa

**Yo solo puedo operar APIs.** Artistly, ChatGPT, Midjourney, LTX y Atlabs son aplicaciones web: las
manejas tú, imagen por imagen, en tu navegador.

| Vía | Quién genera | Ciclo de iteración |
|---|---|---|
| API (HuggingFace, fal, Together) | **Yo, desde aquí** | Segundos. Genero 5 variantes, las veo, corrijo y repito |
| Artistly / ChatGPT / Midjourney | **Tú, a mano** | Cada ronda es un ida y vuelta contigo |
| ComfyUI local | **Tú**, pero automatizable con scripts | Rápido una vez montado |

Esta sesión ya lleva varias rondas de diseño perdidas justamente por eso. Con una API, el ciclo
"genero → miro → corrijo" pasa de horas a segundos.

---

## 3. Lo que realmente necesitas — dimensionado

| Necesidad | Volumen/mes | Cubierto por |
|---|---|---|
| Escenas de los videos largos | ~400 | **VideoExpress 3.0 — ya pagado** |
| Miniaturas de Shorts | 0 | Frames del propio video |
| Miniaturas de largos | ~30 con iteraciones | **Pendiente** |
| Avatar y banner | Una vez | **Pendiente** |

**Lo pendiente son ~40 imágenes al mes.**

Coste de esas 40 imágenes:

| Vía | Coste mensual real |
|---|---|
| HuggingFace | **$0** |
| API FLUX schnell | **$0,05 – $0,12** |
| Artistly | $49 una vez ≈ $4/mes el primer año |
| ChatGPT Plus | $20/mes |

**Pagar $20 o $49 por 40 imágenes que cuestan 12 centavos no es invertir, es gastar de más.**

---

## 4. Sobre el storyboard

Tu paquete ya lo cubre. `INVESTIGACION_tutoriales_videoexpress.md` documenta el **storyboard de
VideoExpress**, y `MANUAL_PRODUCCION.md` §2 trae las dos técnicas de consistencia de personaje, con la
Técnica B ya **validada en vivo con alta fidelidad**.

Las herramientas de storyboard con consistencia (Atlabs $30-75/mes, LTX Studio $15-125/mes, Drawstory)
son **plataformas de video que duplican lo que VideoExpress ya hace y ya pagaste**. Comprar una sería
pagar dos veces por la misma función.

Lo que sí vale la pena robarles es el **método**: generar una **hoja de referencia del personaje con
varias vistas** (frente, espalda, perfil izquierdo, perfil derecho) antes de producir escena alguna, y
usarla como condicionamiento en cada frame. Eso es exactamente la **Técnica A** de tu manual, que está
a medio implementar.

---

## 5. Consistencia: el problema real, en tres niveles

| Nivel | Método | Fiabilidad | Dónde |
|---|---|---|---|
| 1 | Ficha de personaje repetida verbatim en cada prompt | Media-alta | Ya validado en tu proyecto. Coste cero |
| 2 | Hoja de referencia multi-vista + condicionamiento | Alta | VideoExpress (Técnica A) o IPAdapter |
| 3 | **LoRA de estilo entrenado** | **Máxima** | Solo ComfyUI local o fal.ai |

Un LoRA se entrena una vez con 20-40 imágenes coherentes y a partir de ahí **las 400 escenas del mes
salen idénticas**. Es la única solución definitiva, y **Artistly no lo permite**.

---

## 6. Recomendación

**No compres Artistly ni ChatGPT Plus para esto.** Ninguno resuelve la consistencia, ninguno es
realmente ilimitado, y ambos me dejan fuera del ciclo de iteración.

**Ruta en tres capas:**

1. **Ahora, $0 — token de HuggingFace.** Genero e itero desde aquí. Cubre de sobra las 40 imágenes
   mensuales y resuelve avatar, banner y miniaturas esta semana.
2. **Si HuggingFace se queda corto, $5 en fal.ai.** Más de un año de producción a este volumen, sin
   topes, y admite LoRA.
3. **Cuando el canal facture — ComfyUI local con LoRA de estilo.** Es el único ilimitado de verdad,
   $0 por imagen para siempre, y la única vía que garantiza consistencia perfecta a escala.

**Las escenas de video siguen saliendo de VideoExpress.** Ahí solo hay que cambiar la ficha de estilo
del prompt al estilo cartoon plano.

**Dato que falta para cerrar el punto 3:** qué GPU tiene el PC. SDXL necesita 8-12 GB de VRAM;
FLUX.1 Dev, 16-24 GB, o 6 GB en versión cuantizada GGUF Q4.
