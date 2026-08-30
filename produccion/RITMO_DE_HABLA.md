# Ritmo de habla — que dice la medicion, no la intuicion

## Por que importa

El video 5 quedo con la voz en 10:46 y las imagenes sumando 13:00. Parecia
que faltaba guion. No falta: **es el mismo texto leido mas rapido.**

```
Para 195 imagenes x 4 s   ->  780 s de voz
El guion tiene            ->  1.887 palabras
1.887 palabras en 780 s   ->  145 wpm    <- para esto se escribio
La voz salio en           ->  646 s (10:46)
1.887 palabras en 646 s   ->  175 wpm    <- asi lo leyo Edge TTS
```

El hueco de 2:14 es el 21% de velocidad de mas. Ni una frase falta, ni una
imagen sobra.

## Lo medido en el proyecto (capitulos con marca de tiempo de competidores)

```
283 palabras / 107 s  =  158,7 wpm
223 palabras /  90 s  =  148,7 wpm
```

Rango de trabajo: **148 a 159 wpm**. La voz a 175 esta fuera.

## La correccion, sin tocar nada mas

`--rate=-15%` en Edge TTS:

```
175 x 0,85            =  149 wpm     dentro del rango medido
1.887 palabras a 149  =  12:40
12:40 / 195 imagenes  =  3,9 s por imagen
```

Una decima menos que los 4,0 planeados. **No se toca ni una fila del guion
sincronizado, ni una imagen, ni una escena.** Los 2:14 de hueco se caen a 20
segundos repartidos en 195 planos.

## Pendiente de confirmar con dato fresco

La medicion de arriba viene de dos muestras. Falta ampliarla. Desde el
servidor **no se puede**: YouTube devuelve 429 en la pagina del video y
UNPLAYABLE por la ruta del reproductor. La busqueda si pasa; el contenido no.

**Lo mide el Claude del PC**, que tiene navegador con sesion. Cuatro videos de
la formula del video 5, con su transcripcion cronometrada:

```
LGx_cmEH8Lw   7,1M   Psychology of People Who Don't Post their Photos
UCP_be8pT50   2,5M   The Psychology of People Who Are Lazy but Ambitious
SoXWxrvXB1A   769k   The Psychology of People Who Are Deep Thinkers
01FfDlraiHc   639k   The Psychology of People Who Quietly Escape the Rat Race
```

Regla: **si la mediana cae fuera de 148-159, manda la mediana, no el rango
viejo.** Se ajusta el `--rate` a ese numero y se anota aqui.

## Hallazgo aparte, del listado de busqueda

El techo de la formula `The Psychology Of People Who [conducta]` no son 3,37 M
como decia el documento del PC: es **7,14 M**. Y hay un video con el mismo
molde en 88.651 vistas — la formula no salva un tema flojo, pero multiplica
uno bueno.
