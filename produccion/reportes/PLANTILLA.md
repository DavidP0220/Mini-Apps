# Reporte de tanda — LOTE_NN — AAAA-MM-DD

Lo escribe el Claude del PC al terminar cada bloque, y lo sube al repo:

```
git add produccion/reportes/ && git commit -m "Reporte del lote NN" && git push
```

Asi el Claude del servidor lo lee con `git pull` y corrige sin que David tenga
que copiar y pegar nada.

---

## Generadas

| plano | estado | nota |
|---|---|---|
| SH0XX | ok | |
| SH0XX | inpaint | que se corrigio |
| SH0XX | rehacer | por que |

## Control de deriva

Comparacion de `SH001.png` con la ultima del bloque:

- [ ] alto y ancho de cabeza
- [ ] gorra apoyada en el craneo, mismo azul
- [ ] dos ovalos negros macizos, mismo tamano
- [ ] costado de la cabeza, curva limpia
- [ ] grosor del contorno negro
- [ ] tono crema de la piel

Veredicto: **se mantuvo / se derivo**

## Prompts que Artistly no obedecio

Uno por linea: numero de plano, que pedia el prompt, que dibujo en realidad.
**No los arregles tu.** Aqui se reportan y el servidor los corrige en
`escenas.py`.

## Creditos

Gastados en esta tanda: N. Restantes: N.

## Bloqueos

Lo que impide seguir, si hay algo.
