# Interfaz de Artistly — nombres reales

Extraidos del codigo de la aplicacion (manifest y bundles publicos), 2026-08-30.
No son de memoria: son los literales que renderiza la app.

## Direcciones directas

```
https://app.artistly.ai/consistent-character-3d   generador de personaje consistente
https://app.artistly.ai/ai-inpainter              arreglar sin regenerar
https://app.artistly.ai/personal-designs          todas las imagenes generadas
https://app.artistly.ai/train-your-own-ai         entrenar modelo propio
https://app.artistly.ai/download-zip              descarga en lote
```

Sin sesion iniciada, todas responden `302 -> /login`.

## Campos y botones

| Literal en pantalla | Que es |
|---|---|
| `Select A Category` | Realistic Images · Pixar Style · **3d & 2d Style Images** · Multi-consistent Characters |
| `Upload your characters` | referencia del personaje |
| `Please upload an image or select from personal designs.` | **se puede elegir de los disenos guardados, sin volver a subir** |
| `Choose Aspect Ratio` | viene en `Default`; hay que ponerlo en 16:9 cada vez |
| `Quantity` | cuantas variantes por generacion |
| `Enter prompt here` | campo del prompt |
| `Generate Image` | genera |
| `Generating design...` | esta trabajando |
| `Please wait until the previous request is completed!` | **la app obliga a una por vez** |

## Multi-consistent Characters

Pide `upload both character images`. Es la via para los planos con dos
personajes (host adulto + host nino, o host + antagonista).

## A.I. Inpainter

`Brush Size` · `Paint and add mask on specific areas of your image` ·
`Inpaint your design by adding a simple description` · boton `Inpaint Design`.
La imagen debe pesar menos de 5 MB.

## Train your own AI

Dice `ONLY Upload photos of one person` e `Instant Training of Your Photos`.
Flujo: `Create Model` -> `Start training`. Esta hecho para **fotos reales de
una persona**, no para un dibujo vectorial plano. Sin probar todavia; riesgo
de que no reproduzca el estilo plano.
