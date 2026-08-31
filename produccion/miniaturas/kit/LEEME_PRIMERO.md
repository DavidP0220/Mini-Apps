# KIT DE MINIATURAS — Mindset Mechanics

Todo lo necesario para sacar una miniatura con la formula que rinde **13-14% de CTR**
en el canal. No gasta creditos de ninguna IA: es codigo, tarda segundos.

## Que hay aqui

| Archivo | Para que sirve |
|---|---|
| `miniatura.py` | El generador. Es lo unico que hay que ejecutar |
| `Anton-Regular.ttf` | La fuente correcta. **No es Impact ni Arial** |
| `FORMULA_MINIATURAS_MM.md` | Los 9 elementos de la formula, medidos sobre miniaturas reales |
| `REFERENCIA_la_que_rinde_14.7pct.jpg` | La mejor del canal. **Contrastar siempre contra esta** |
| `REFERENCIA_la_que_rinde_13pct.jpg` | La segunda mejor |
| `EJEMPLO_resultado_final.jpg` | Lo que produce la herramienta |

## Uso

```bash
python miniatura.py <imagen> "SETUP" "CUERPO" "REMATE" "SUBTITULO" "PALABRA_ROJA" salida.jpg
```

Ejemplo real (el del Video 5):

```bash
python miniatura.py base.jpg "THIS IS NOT ADDICTION" "IT'S STILL" "HUNTING" \
       "4 HOURS A DAY" "BY DESIGN" mi_miniatura.jpg
```

Necesita Python con Pillow: `pip install pillow`

## Los 5 textos, y que hace cada uno

| Hueco | Donde sale | Regla |
|---|---|---|
| **SETUP** | arriba, en banda roja de brocha | Prepara. 3-4 palabras |
| **CUERPO** | grande, blanco | **Maximo 2-3 palabras.** Cada palabra de mas encoge la letra |
| **REMATE** | grande, **AMARILLO** | La palabra que vende. UNA sola si se puede |
| **SUBTITULO** | abajo, blanco | El contexto o el dato |
| **PALABRA_ROJA** | abajo, en rojo | El cierre del subtitulo |

## Las 6 reglas que de verdad importan

1. **Texto izquierda, personaje derecha.** Invariable en las dos que rinden.
2. **Fondo casi negro** con el sujeto recortado por la luz. Nada de fondos claros.
3. **El personaje NUNCA con cara neutra.** Preocupado, sorprendido, agotado, con cejas
   marcadas. Una cara neutra mata la miniatura.
4. **Densidad alta.** En este nicho, limpio = invisible.
5. **El amarillo es para el remate y solo para el remate.**
6. **Comprobarla a 168 px de ancho** antes de darla por buena: el 70% de las impresiones
   son moviles. Si no se lee ahi, no existe.

## Como elegir la imagen base

- Cara **grande** en el encuadre. Si el personaje esta lejos, a tamano movil es una mancha.
- Emocion **legible** de un vistazo.
- Que la mitad derecha aguante sola: la izquierda se oscurece para el texto.
- Truco: reducela a 168x94 px y miralas. La que sigue funcionando ahi, gana.

## Lo que le falta a la herramienta (hacerlo aparte)

Las miniaturas del canal que rinden usan el personaje en **version detallada** —con orejas,
sombreado rico, casi 3D— que **no es** el personaje plano del video. Y llevan atrezzo de marca:
la taza negra con DISCIPLINE/FOCUS/FUTURE y el garabato de ovillo mental.

Eso hay que generarlo en **Artistly** y pasarselo a la herramienta como imagen base. La
herramienta hace el texto y la composicion perfectos; la calidad del personaje depende de la
imagen que le des.

## Contrastar con la competencia (gratis)

Sacar los IDs de los videos que estan pegando en la busqueda de YouTube y bajar sus miniaturas:

```
https://i.ytimg.com/vi/<VIDEO_ID>/maxresdefault.jpg
```

Son los datos reales de lo que funciona hoy, no la opinion de un blog.
