# Plantilla de miniatura — estilo validado del nicho

Réplica de la fórmula visual de los dos mayores breakouts del nicho
(Mindspoke 863.686 vistas, PsySense 663.837 vistas), ambos desde canales de menos de 4.500 subs.

## La fórmula

| Elemento | Especificación |
|---|---|
| Fondo | Blanco roto `#FCFBF6`, plano, sin textura |
| Bloque de texto | Globo redondeado amarillo `#FFE500`, radio 52px, sombra dura desplazada |
| Tipografía | **Anton** (condensada pesada), 104px, negro `#0D0D0D` |
| Texto | 3 líneas, 2-3 palabras por línea. Nunca el título completo |
| Personaje | Cartoon plano, contorno negro de 10px, a la derecha, sangrado por abajo |
| Flecha | Roja `#E01B1B`, curva, trazo de 15px, apunta a la cabeza |
| Interrogantes | Dos, tamaños distintos, rotados |

## Por qué así

`PLAYBOOK_MONETIZACION.md` §5, regla dura: *"menos elementos, cara/personaje más grande, texto 0-3
palabras, emoción legible a 100px, fondo de color plano saturado. Escenas pobladas y detalladas
pierden sistemáticamente contra composiciones simples."*

Y de `competencia/`: los cuatro referentes usan fondo blanco, amarillo saturado tras el texto, negro
grueso y rojo para la señal. Ninguno usa oscuridad ni iluminación cinematográfica.

## Uso

```bash
node plantilla.mjs
```

Los títulos se editan en el array `TITULOS` al final del script. Cada entrada son las líneas del
globo y el nombre del archivo de salida. Salida a 1280×720.

La fuente Anton está instalada en `~/.local/share/fonts/`. Si falta:

```bash
curl -o ~/.local/share/fonts/Anton-Regular.ttf \
  "https://fonts.gstatic.com/s/anton/v27/1Ptgg87LROyAm0K0.ttf" && fc-cache -f
```

## Pendiente de pulir

- La mano no toca la cabeza con claridad
- El cuadrante inferior izquierdo queda vacío
- Los ojos leen como sorpresa, no como cansancio
- Falta variar la pose del personaje por tipo de video
