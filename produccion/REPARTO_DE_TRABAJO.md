# Reparto de trabajo — quien hace que

Hay dos Claude trabajando en Mindset Mechanics. **No hacen lo mismo, y no se
pisan.** Este archivo es el contrato entre los dos.

| | Claude del servidor (claude.ai/code) | Claude del PC (ventana negra) |
|---|---|---|
| Donde corre | nube de Anthropic | maquina de David |
| Ve el navegador | no | **si**, extension Claude in Chrome |
| Escribe en el repo | **si**, empuja a la rama | lee con `git pull` |
| Su trabajo | guion, escenas, ritmo, prompts, titulos, miniaturas, estrategia | generar en Artistly, inpaint, descargar, montar en VideoExpress |

**No hay canal directo entre los dos.** El unico puente es este repositorio, y
funciona en los dos sentidos:

```
   servidor  --- git push --->  GitHub  --- git pull --->  PC
   servidor  <--- git pull ---  GitHub  <--- git push ---  PC
```

- **De ida:** el servidor empuja guion, escenas y hojas de prompts.
- **De vuelta:** el PC escribe un reporte en `produccion/reportes/` al terminar
  cada tanda y lo sube. El servidor lo lee con `git pull` y corrige.

Con eso David no tiene que copiar y pegar entre las dos ventanas: solo dice
"sigue" en una y "ya reporto" en la otra.

---

## Regla de oro

**El Claude del PC no escribe prompts de imagen. El del servidor no toca el
navegador.** Si uno se mete en el terreno del otro, se duplica trabajo y se
rompe la consistencia del personaje.

Si el Claude del PC ve que un prompt esta mal (como paso con SH002, que pedia
`seen from behind` y Artistly lo ignoro), **no lo arregla por su cuenta**: lo
reporta, el del servidor lo corrige en `escenas.py`, lo empuja, y el del PC
hace `git pull` y regenera. Asi el arreglo queda escrito y no se vuelve a
cometer en los 185 planos que faltan.

---

## Estado a hoy

**Video en produccion:** *Why Didn't Evolution Remove Your Fear of Being Seen?*
Miniatura `DONT BE SEEN`. 225 planos, 15:03.

Hecho:
- `GUION_impostor.md` — guion completo, 2379 palabras, los 8 beats verificados
- `PLANOS_VO.md` / `.json` — los 225 planos con tiempo de entrada, duracion,
  movimiento de camara y su linea de voz
- `impostor/escenas.py` — **40 escenas de 225** (bloques 1 y 2)
- `LOTE_01.txt` y `LOTE_02.txt` — prompts listos para pegar

Pendiente:
- 185 escenas por escribir (SH041 a SH225) — del servidor
- revisar los bloques 1 y 2 contra su linea de voz: se escribieron **antes**
  del guion — del servidor
- generar en Artistly — del PC

---

## Herramientas del repo

```
python3 lote.py N        genera LOTE_NN.txt desde escenas.py
python3 ritmo.py         recorta el guion en 225 planos por curva de ritmo
python3 auditoria.py     barrido completo; sale con codigo 1 si algo no cuadra
```

**`auditoria.py` se corre antes de cualquier tanda de generacion.** Si sale en
rojo, no se generan imagenes: se arregla primero. Una imagen generada sobre
una base rota cuesta creditos y hay que rehacerla.

---

## Lo aprendido que no se repite

1. La identidad del personaje viene de `HOST_CORRECTO.png`, **no del texto**.
   Reseleccionarla antes de CADA generacion.
2. Artistly **ignora las instrucciones de camara**. `seen from behind` no
   significa nada: hay que describir la espalda como objeto del cuadro.
3. Cero negaciones. El generador dibuja lo que se le prohibe.
4. Un detalle malo se arregla con `ai-inpainter`, nunca regenerando.
5. Si falla la seleccion de la referencia, **no dar Generate**: se gastan
   creditos en una imagen que hay que botar.
