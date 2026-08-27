# INVESTIGACIÓN — Herramientas y método de storyboard

**Fecha:** 2026-08-27 · **Para:** David y Kimi
**Créditos de imagen consumidos en esta sesión: 50 unidades del add-on de Cloudinary** (agotado).
**Créditos de Recraft consumidos: 0.**

Este documento acumula todo lo extraído de los enlaces que David fue pasando, más lo verificado
contra el código y los logs del propio proyecto. Se va ampliando; no se reescribe.

---

## 0. Aviso de método — qué pude verificar y qué no

**El proxy de red de esta sesión bloquea casi cualquier web.** Devolvieron `EGRESS_BLOCKED`:
`youtube.com`, `instagram.com`, `storyboardthat.com`, `storyboardart.org`, `storyboarder.ai`.

Consecuencia: de esos sitios **no leí la página, leí resultados de búsqueda**. Todo lo que venga
de ahí va marcado como *sin verificar contra la fuente*, según la regla del proyecto de no
comunicar sobre fuente no verificada. Lo que sí está verificado de primera mano son las pruebas
de generación que corrí y la lectura del código y los logs del repo.

Para futuras referencias: **pega el texto o una captura**, no el enlace.

---

## 1. La técnica de la lámina viral (reel de Instagram)

*Fuente: reel bloqueado; técnica confirmada por búsqueda + reproducida por mí.*

Esas láminas de "DETAILED STORYBOARD + CHARACTER DESIGN SHEET + COLOR PALETTE" que circulan en
redes **son UNA sola imagen generada de una vez**, no un documento maquetado. Se hacen con
**Nano Banana** (Gemini) describiendo el pliego entero en el prompt: cabecera, rejilla de
viñetas, hoja de personaje, escenarios, paleta y barra inferior.

### Lo reproduje. Resultado verificado de primera mano:

| | Resultado |
|---|---|
| **Formato / maquetación** | ✅ Sale bordado. Idéntico a la referencia. |
| **Texto de los pies** | ❌ Ilegible. «Extreme close ologo of one oyo shifed in outer corner». Bajo CAMERA pone «Burnt amber», bajo SOUND «No blush». |
| **Ficha de personaje** | ❌ **Varias cabezas salen con nariz.** Es el defecto exacto que ya costó dos rondas rechazadas. |
| **Coste** | 14 unidades de add-on en una sola generación (vs 4 de Recraft). |

**Conclusión:** vale como pieza de presentación o de pitch. **No vale para producir**: nadie puede
generar a partir de esos pies, y un pliego generado de una vez no respeta una ficha bloqueada.

---

## 2. storyboardthat.com

*Sin verificar contra la fuente — página bloqueada, y las búsquedas no devolvieron precios
actuales. No cito cifras que no pude comprobar.*

**Qué es:** maquetador de storyboards por arrastrar y soltar, con librería propia de personajes
de clip-art. Orientado a educación y empresa.

**Por qué no encaja aquí:**

1. **Su producto es su librería de personajes.** El activo central del canal es un personaje
   bloqueado (cabeza lisa, gorra navy, sin pelo, sin orejas, sin nariz) que no existe en esa
   librería y no se puede construir con sus piezas.
2. **Subir imágenes propias es solo de pago y con 5 MB por archivo**
   (su centro de ayuda). Si subes tus imágenes es porque ya las generaste en Recraft — estarías
   pagando por un lienzo donde pegar lo que otra herramienta hizo.
3. **No habla el idioma del pipeline.** No emite `image_prompt` ni `video_action_prompt`; no hay
   salida que `generate_scene.py` pueda consumir.

**Veredicto: descartado.**

---

## 3. storyboardart.org

*Sin verificar contra la fuente — página bloqueada.*

**Qué es:** una **escuela** para formar dibujantes de storyboard. Mentorías de 12 meses,
currículos de 3 años, portafolio para que te contraten. Instructores con créditos en Pixar,
Disney, Lucasfilm, Marvel, Netflix y Warner.

**Veredicto: no es una herramienta y no es el camino** — un año de formación no publica un video.

**Pero el oficio que enseñan sí es aplicable, y es gratis.** Tres principios profesionales que
`SISTEMA_STORYBOARD_MINDSET_MECHANICS.md` **no contempla**:

### 3.1 Eye-trace (recorrido de la mirada) — el que más falta
Saber en qué punto del cuadro está el ojo del espectador **en el momento del corte**, y colocar
el punto de interés del plano siguiente ahí mismo, o moverlo a propósito para dar un golpe. Si
cada corte obliga a rebuscar dónde mirar, el espectador se agota sin saber por qué.
**Relevancia directa:** dos de los cuatro largos del canal tienen retención media del
**13,5 %** y **24,8 %**.

### 3.2 Notan / estructura de valores
Leer cada cuadro en tres valores (claro, medio, oscuro) para que el ojo aterrice donde toca. En
cel-shading plano es **más** decisivo que en fotografía, porque no hay profundidad de campo que
ayude. El sistema actual declara capas (primer plano / medio / fondo) pero **no dice nada de
valores**: las tres capas pueden salir del mismo tono y el cuadro se aplana.

### 3.3 Línea de acción y lectura en silueta
Cada pose sobre una curva dominante, y legible **rellenada de negro**. El checklist actual tiene
la prueba de rejilla (¿es el mismo personaje?) pero no la prueba de silueta (¿se entiende la pose
sin detalle?).

**Acción propuesta:** addendum §10 de `SISTEMA_STORYBOARD` (v1.3) con estas tres reglas hechas
ejecutables, aplicado a las 22 viñetas del Acto 1. Coste: 0 créditos.

---

## 4. storyboarder.ai

*Sin verificar contra la fuente — página bloqueada. Datos de búsqueda.*

Plataforma de preproducción: sube guion (Final Draft, PDF o texto plano) y genera desglose de
escenas, lista de planos y storyboard. Lo relevante para este proyecto:

- **Consistencia declarada:** permite definir y reutilizar personajes, props y localizaciones
  entre escenas, y **subir estilos de arte propios**.
- **Image-to-Video:** convierte el storyboard en animática. Eso pisa el terreno de VideoExpress.
- **Controles por plano:** tamaño, ángulo, lente, luz, acción, composición.
- **Precio de partida citado: 39 USD.** *Sin verificar.*

**Veredicto: es el único de los tres que merece una prueba**, y solo si la ruta interna falla.
Pero antes de pagarlo hay que leer el §5, porque el mecanismo que promete —consistencia de
personaje— **ya lo tienes pagado y sin usar**.

---

## 4.bis canva.com — maquetador, no generador

*Sin verificar contra la fuente — página bloqueada. Datos de búsqueda y de su documentación
para desarrolladores.*

**Qué es:** editor de diseño por arrastrar y soltar con plantillas de storyboard. Misma familia
que storyboardthat: **un lienzo, no un generador**. No puede producir tu personaje bloqueado.

**Lo único técnicamente interesante — y tiene trampa:** existen las **Canva Connect APIs**, que
permiten subir assets a la biblioteca del usuario y, con **Autofill + Brand Templates**, rellenar
una plantilla con datos externos de forma automática. Sobre el papel eso serviría para volcar
las 22 viñetas ya generadas en una lámina bonita sin tocarla a mano.

**La trampa:** según su propia documentación, **Autofill y Brand Templates son solo para clientes
Enterprise**. Para un canal de una persona, esa vía no existe.

**Veredicto para storyboard: descartado**, por la misma razón que los otros maquetadores.

### ⚠️ Pero Canva sí sirve — para el otro trabajo, que es el que de verdad importa

El cuello de botella medido del canal **no es el storyboard**: son **43 vistas por video**. Lo que
mueve ese número son **título y miniatura**, y para miniaturas Canva es exactamente la herramienta
correcta: plantillas 1280x720, texto grande, y la posibilidad de subir el PNG del host recortado
como elemento reutilizable.

Si vas a pagar una suscripción de diseño, **que sea para miniaturas, no para storyboards.** Ahí
el retorno es directo y medible en CTR.

---

## 4.ter visme.co — igual que Canva, algo más caro

*Sin verificar contra la fuente — página bloqueada.*

Creador de storyboards por arrastrar y soltar, con generación de diapositivas por IA a partir de
un prompt o un documento, marca personalizable, y exportación a PDF, JPG, PNG, PPTX y HTML5.
**Tiene API y se conecta con Zapier**, lo que lo pone por delante de Canva en automatización para
un usuario individual.

**Precios citados (sin verificar):** Gratis (5 proyectos, 100 MB) · Standard 15 USD/mes ·
Business 29 USD/mes · Enterprise a medida.

**Veredicto: descartado para storyboard**, misma razón de fondo — su IA genera *diapositivas a
partir de plantillas*, no tu personaje. Y para miniaturas, Canva hace lo mismo mejor y más barato.

---

## 5. ⚠️ EL HALLAZGO — Recraft tiene consistencia de personaje y el pipeline no la usa

Esto sí está **verificado de primera mano** contra el código y los logs del repo.

### 5.1 El mecanismo existe y está implementado

`recraft_ai/recraft_client.py` línea 547 ya tiene:

```python
def create_style(reference_images: list[Path], base_style: str = "digital_illustration") -> str:
    """POST /styles - crea un estilo propio a partir de imagenes de
    referencia y devuelve su style_id, reutilizable en generate_image()."""
```

Recraft permite crear un estilo propio con **3-5 imágenes de referencia** y devuelve un
`style_id` que fija la identidad **del lado del modelo**, no del prompt. Es su mecanismo oficial
de consistencia, y el canal tiene las referencias listas en `05_MEDIA_REFERENCIA/personaje_refs/`
y `style_locks/`.

### 5.2 Nunca se ha usado. Prueba, de sus propios logs

`recraft_ai/logs/generation_log_2026-08-26.jsonl`, las dos generaciones reales:

```
"model": "recraftv4_1_pro", "style": null, "style_id": null, "credits_spent": 210
"model": "recraftv4_1_pro", "style": null, "style_id": null, "credits_spent": 210
```

**`style_id: null` en las dos.** La consistencia se está intentando **a mano dentro del prompt**:
la segunda generación añade un párrafo entero de *"Consistent recurring character design,
identical in every scene: the same round cream-skinned head…"*. Eso es exactamente el parche que
`style_id` sustituye de raíz.

### 5.3 Y el script del piloto ni siquiera puede pasarlo

- `generate_scene.py` → **sí** acepta `--style-id` (línea 43).
- `generate_piloto_stills.py` → **no lo acepta**. Solo pasa `model=`.

Y el piloto se genera con `generate_piloto_stills.py`. O sea: **el script que va a generar las
imágenes del piloto no puede usar el mecanismo de consistencia aunque se decidiera usarlo.**
Es un bug de un parámetro que falta.

### 5.4 La matemática de créditos, que nadie ha hecho

De los logs: `credits_before: 5000` → `4790` → `4580`. **210 créditos por imagen** en
`recraftv4_1_pro` a 2688x1536.

| | Imágenes | × 3 (regla del manual) | Créditos |
|---|---|---|---|
| Acto 1 de Attention Span | 22 | 66 | **13.860** |
| Piloto de Resiliencia | 15 | 45 | **9.450** |
| Un largo entero | ~60 | 180 | **37.800** |

**Saldo del que parten los logs: 5.000.** Es decir: **con el saldo actual no sale ni el piloto de
Resiliencia**, y mucho menos un video completo. A 210 créditos por imagen, 5.000 créditos son
**23 generaciones**. La regla de paneles × 3 convierte eso en **7 paneles usables**.

Esto es más grave que cualquier decisión de herramienta y no está en ningún handoff.

### 5.5 La ruta que resuelve las tres cosas a la vez

`recraftv3 @ 1820x1024` es 16:9 nativo (sin recorte) y **el único modelo que soporta `style_id`**
— ya está documentado en `ERRORES_QUE_NO_SE_DEBEN_REPETIR.md` como decisión abierta.

Además, hoy comprobé de primera mano generando con los dos modelos:

- **recraft-v4 acepta la cláusula de negativos dentro del prompt positivo.** Generó bien.
- **recraft-v3 la RECHAZA** (`MG_00707: the model could not process the given inputs`) y **acepta
  el mismo prompt en cuanto se le quita la cláusula.**

Eso encaja con que V3 tiene parámetro `negative_prompt` propio: no quiere los negativos en el
texto porque los espera aparte. **Y eso cierra la bandera R2**, que llevaba días bloqueando dos
storyboards a la espera de una decisión.

**Ruta recomendada, que resuelve consistencia + negativos + coste de un golpe:**

1. `create_style()` con 3-5 imágenes de `personaje_refs/` → se obtiene un `style_id` **una vez**.
2. Generar con `recraftv3 @ 1820x1024` + ese `style_id`, 16:9 nativo sin recorte.
3. Los negativos por el parámetro `negative_prompt` de la API, fuera del prompt positivo — como
   manda `ESTILO` §6.bis y como V3 exige.
4. Añadir `--style-id` a `generate_piloto_stills.py`, que hoy no lo tiene.

Antes de comprometer nada: **medir el coste real por imagen de V3**, que puede ser muy distinto
de los 210 de V4.1 pro. Una sola generación lo dice.

---

## 6. Comparativa y decisión

| Camino | Consistencia de personaje | Sale al pipeline | Coste | Veredicto |
|---|---|---|---|---|
| **Recraft V3 + `style_id`** | **Oficial, del lado del modelo** | Sí, ya integrado | Por medir | ✅ **Primera opción** |
| Recraft V4.1 (actual) | Solo por prompt, frágil | Sí | 210 cr/imagen | ⚠️ Caro y sin consistencia real |
| Nano Banana (lámina) | No respeta ficha | No | 14 u/lámina | Solo presentación |
| storyboarder.ai | Declarada, sin verificar | Export, sin API confirmada | ~39 USD | Plan B |
| storyboardthat | No | No | — | ❌ Descartado |
| Canva | No | Solo API Enterprise | — | ❌ Para storyboard · ✅ **para miniaturas** |
| Visme | No | API + Zapier | 15-29 USD/mes | ❌ Descartado |
| storyboardart.org | — | — | — | ❌ Es una escuela |

**Camino más rápido, barato y de más calidad, en este orden:**

1. **Crear el `style_id` desde las referencias del personaje.** Una llamada. Es el arreglo de raíz
   del error nº1 del proyecto.
2. **Medir V3 @1820x1024**: coste por imagen y si el look aguanta contra los frames publicados.
3. **Parchear `generate_piloto_stills.py`** para que acepte `--style-id`.
4. **Aplicar el addendum §10** (eye-trace, notan, silueta) a las 22 viñetas. Cuesta 0.
5. Solo si 2 falla, probar storyboarder.ai con los 39 USD.

**Y en paralelo, lo que de verdad mueve las vistas:** miniaturas nuevas para los 4 largos, hechas
en Canva sobre el PNG del host. Eso no compite con nada de lo anterior y es lo único de esta lista
que toca directamente el 43.

---

## 7. Lo que sigue sin resolverse con ninguna herramienta

El canal tiene **11 suscriptores, 6,6 horas de reproducción y 43 vistas por video**. Ninguna
herramienta de storyboard mueve ese número: el storyboard afecta a la calidad del video, y el
problema medido es que **nadie los está viendo**. Lo que sí lo mueve, y cuesta 0: rehacer títulos
y miniaturas de los 4 largos, y hacer Shorts en serie copiando el que consiguió 99 % de retención
y trajo 4 de los 11 suscriptores.
