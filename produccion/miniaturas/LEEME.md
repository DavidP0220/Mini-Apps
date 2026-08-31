# Miniaturas — una sola herramienta

**La oficial es `kit/miniatura.py`.** Trae la formula medida sobre las
miniaturas del canal que rinden **13-14% de CTR**, la fuente Anton correcta y
las dos referencias contra las que se contrasta.

```bash
python kit/miniatura.py IMAGEN "SETUP" "CUERPO" "REMATE" "SUBTITULO" "PALABRA_ROJA" salida.jpg
```

`_miniaturas.py` y `detalle.py` quedan **retirados**: hacian lo mismo peor y
por duplicado. Lo unico que aportaban y que conviene recuperar algun dia es el
encaje automatico del ancho de linea; mientras tanto, la regla del kit lo
cubre: **cuerpo de 2-3 palabras, remate de una.**

## Lo unico que falta, y no lo resuelve el codigo

La imagen base. El propio LEEME del kit lo dice: *la calidad del personaje
depende de la imagen que le des*. Las miniaturas que rinden usan el personaje
en **version detallada**, que se genera en Artistly y se le pasa a la
herramienta.

Un fotograma plano del video no sirve: el personaje sale centrado y de frente,
y al recortar a la derecha solo se ve la capucha.

## Orejas: CERRADO — van SIN orejas

David, 2026-08-31: *"va sin orejas y ya"*. **Esto anula el punto 7 de
`FORMULA_MINIATURAS_MM.md`**, que decia lo contrario y estaba ratificado el
2026-08-30.

Queda constancia del costo, porque el dato es del propio canal: las dos
miniaturas que rinden **13-14% de CTR** llevan orejas y sombreado 3D. Se cambia
igual, por decision de David, y si algun dia se quiere medir se hace como
prueba A/B explicita.

**Regla vigente:** el personaje de miniatura va **sin orejas, sin pelo y sin
nariz**, igual que el del video. Lo que lo separa del personaje del video no es
la anatomia sino **la expresion, el volumen y la luz**: cejas quebradas, boca
tensa, luz de borde calida y textura. Una cara neutra mata la miniatura
(punto 4 de la formula, ese sigue vigente).

## Medidas de la composicion, tomadas de la referencia

| | |
|---|---|
| El ojo ocupa | la mitad del ancho del cuadro |
| Centro del ojo | 65% del ancho · 47% del alto |
| La zona fria empieza | 64% del ancho |
| Prueba de legibilidad | **168 px de ancho** (el kit manda sobre mi 210) |
