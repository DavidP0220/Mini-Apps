# Pruebas de generación de personaje

## Estado

Dirección de estilo confirmada por el usuario: **Rick and Morty** — contornos negros gruesos,
colores planos, ojos ovalados grandes con pupilas pequeñas, expresiones simples.

`rm1.jpg` y `rm2.jpg` validan que el estilo se consigue con el prompt correcto. Lo que falla es la
**nitidez**: el único modelo gratuito disponible en Pollinations es `sana`, que devuelve resultados
suaves y desenfocados, sin la línea limpia que exige este estilo.

## Prompt que funciona

```
Rick and Morty art style, adult swim cartoon, thick black outlines, flat colors,
man with big oval eyes and tiny pupils, worried nervous expression, simple flat
white background, character portrait
```

## Generadores evaluados

| Vía | Estado | Nota |
|---|---|---|
| Pollinations (`sana`) | Gratis, sin key | Único modelo disponible. **Borroso**, no sirve para línea limpia |
| Cloudinary MCP | **Desconectado** | Tenía Recraft, Flux, Ideogram y Nano Banana. Recraft es especialista en vectores. Quedaban 33 generaciones |
| vidIQ `generate_thumbnail` | 17 créditos | Insuficiente: cuesta 22 por llamada. Recarga el 18-sep |
| SVG a mano | Descartado | Queda rígido comparado con la referencia |

## Siguiente paso

Reconectar el conector de Cloudinary y generar con **Recraft**, que es el modelo indicado para
ilustración vectorial de línea limpia.
