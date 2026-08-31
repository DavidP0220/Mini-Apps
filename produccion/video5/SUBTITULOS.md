# Subtitulos — canon del canal

**No negociable.** Arial Bold, MAYUSCULAS, amarillo, contorno negro, tercio
inferior, **3 a 4 palabras** por bloque.

## Estilo ASS listo para usar

Para 1920x1080. Se aplica con ffmpeg sobre el video ya montado.

```
[V4+ Styles]
Format: Name,Fontname,Fontsize,PrimaryColour,OutlineColour,BackColour,Bold,Italic,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding
Style: MM,Arial,72,&H0000D9FA,&H00000000,&H00000000,-1,0,1,5,2,2,80,80,110,1
```

Que significa cada cosa:

| Campo | Valor | Por que |
|---|---|---|
| Fontsize | 72 | legible en telefono sin tapar la imagen |
| PrimaryColour | `&H0000D9FA` | amarillo del canal, en BGR (no RGB) |
| OutlineColour | `&H00000000` | negro |
| Bold | -1 | activado |
| Outline | 5 | contorno grueso: sobrevive sobre fondo claro |
| Shadow | 2 | despega el texto de la imagen |
| Alignment | 2 | centrado abajo |
| MarginV | 110 | tercio inferior, sin chocar con la barra de YouTube |

## Comando

```
ffmpeg -i video.mp4 -vf "ass=subs.ass" -c:a copy salida.mp4
```

## Regla de corte

**3 a 4 palabras por bloque, nunca mas.** El bloque cambia con la voz, no con
un reloj fijo: cada linea entra cuando se dice y sale cuando termina.

Palabra por palabra **no** se usa en este canal, aunque se vea en otros: el
canon son 3-4 palabras y eso manda.

## Verificacion antes de publicar

- [ ] ninguna linea pasa de 4 palabras
- [ ] ningun bloque dura menos de 0,4 s
- [ ] el texto no tapa la cara del host en ningun plano
- [ ] se lee sobre el fondo mas claro del video
