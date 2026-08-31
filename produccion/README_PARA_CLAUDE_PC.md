# Instrucciones para el Claude que corre en el PC de David

Este repositorio es el puente. Aqui llegan las hojas de prompts ya escritas
y verificadas. Tu trabajo es generarlas en Artistly.

## Reparto

Lee primero `produccion/REPARTO_DE_TRABAJO.md`: define que hace cada Claude.
No escribas prompts de imagen — eso lo hace el del servidor y llega por el repo.

## Antes de empezar

Lee, en este orden:

1. `produccion/artistly/REGLAS_PROMPT_ARTISTLY.md` — barreras que no se negocian
2. `produccion/artistly/INTERFAZ_ARTISTLY.md` — nombres reales de los botones
3. `produccion/impostor/PLAN_PRODUCCION_225.md` — como se organiza el lote

## El ciclo, por cada imagen

Abre `https://app.artistly.ai/consistent-character-3d` en el Chrome de David
(perfil **Mindset, Profile 8**) con Playwright `channel="chrome"`.

Para CADA prompt de la hoja:

1. **Reselecciona `HOST_CORRECTO.png`** como referencia. Siempre, aunque
   parezca ya puesta: Artistly deja marcada la ultima imagen generada y el
   personaje se deriva sin que se note.
2. `Select A Category` -> **3d & 2d Style Images**
3. `Choose Aspect Ratio` -> **16:9** (vuelve solo a `Default`)
4. `Quantity` -> **2**
5. Pega el prompt completo en `Enter prompt here`
6. `Generate Image`, una sola vez, y espera
7. Revisa TU la imagen: cara sin nariz, costado de cabeza sin orejas, ojos
   como ovalos negros macizos, contorno negro grueso
8. Guarda como `SH0XX.png` en `img/`
9. Vuelve al paso 1

Si una imagen falla en un solo detalle: **`ai-inpainter`, jamas regenerar.**

## Control cada 20

Al terminar cada bloque de 20, compara `SH001.png` con la ultima:
alto de cabeza, gorra, ojos, costado de la cabeza, grosor de contorno, tono
de piel. Si algo cambio, **para y rehaz ese bloque**. La deriva no se corrige
sola, se acumula.

## Hojas disponibles

- `produccion/impostor/LOTE_01.txt` — 20 prompts, apertura de Impostor
- `produccion/impostor/LOTE_02.txt` — 20 prompts, la explicacion facil y su muerte
- `produccion/impostor/LOTE_03.txt` — 20 prompts, la muerte de la confianza y la explicacion social
- `produccion/impostor/LOTE_04.txt` — 20 prompts, la banda y la jerarquia inversa
- `produccion/impostor/LOTE_05.txt` — 20 prompts, el castigo del grupo
- `produccion/impostor/LOTE_06.txt` — 20 prompts, las apuestas reales y el evento de seleccion
- `produccion/impostor/LOTE_07.txt` — 20 prompts, el giro oscuro y la herencia
- `produccion/impostor/LOTE_08.txt` — 20 prompts, el giro meta: el exito es el disparador

## Para generar hojas nuevas

`produccion/impostor/lote.py` construye los prompts a partir de una tabla de
escenas cortas. La ficha del personaje y el sufijo de estilo se pegan solos,
identicos en todas, y audita que no haya ni una negacion.
