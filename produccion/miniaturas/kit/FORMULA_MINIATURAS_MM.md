# FÓRMULA DE MINIATURAS — Mindset Mechanics

**Extraída el 2026-08-29 analizando las miniaturas reales del canal**, no de teoría. Las dos con
mejor CTR comparten una estructura idéntica; la de peor CTR la rompe.

| Video | CTR | ¿Sigue la fórmula? |
|---|---|---|
| Your DNA Hates Predator Meat | **14,7 %** | ✅ completa |
| The 300000 Year Old Glitch | **13,0 %** | ✅ completa |
| The Psychological Secret | 4,4 % | ❌ la rompe |

---

## LA FÓRMULA (los 8 elementos)

### 1. Texto en 3 bloques, con jerarquía de color fija

| Bloque | Contenido | Formato |
|---|---|---|
| **Setup** (pequeño, arriba) | "WHY DON'T WE" · "YOUR BRAIN THINKS" | Texto **BLANCO** sobre **BANDA ROJA** pintada a brocha |
| **Cuerpo** (grande) | "EAT" · "IT'S BEING" | **BLANCO** con textura desgastada |
| **Remate** (grande) | "PREDATORS?" · "HUNTED" | **AMARILLO** — es la palabra que vende |
| *(opcional)* Subtítulo | "THE SURPRISING BIOLOGICAL TRUTH" | Blanco + una palabra en rojo |

**La banda roja del setup aparece en las dos ganadoras y en ninguna otra.** Es el elemento
más distintivo de la marca.

### 2. Composición: texto IZQUIERDA · personaje DERECHA
Invariable en las tres.

### 3. Fondo casi negro con iluminación dramática
Nada de fondos claros o medios. Negro/marrón muy oscuro, con una fuente de luz cálida que recorta
la silueta (**rim light**).

### 4. El personaje tiene EXPRESIÓN FUERTE, nunca neutra
Preocupado, sorprendido, pensativo con la mano en el mentón, cejas marcadas. **Una cara neutra
mata la miniatura.**

### 5. Atrezzo recurrente de marca (aparece en las dos ganadoras)
- **Taza negra con "DISCIPLINE / FOCUS / FUTURE"** — abajo a la derecha
- **Signos de interrogación + garabato de ovillo mental** — arriba a la derecha
- Un **objeto-tema central** que resume el video de un vistazo (el bistec, el teléfono)

### 6. Tipografía pesada y condensada, con textura
No es la Arial limpia de los subtítulos. Es una condensada bold con desgaste. **Ojo: la regla de
Arial Bold es para los SUBTÍTULOS QUEMADOS del video, no para las miniaturas.**

### 7. El personaje de la miniatura NO es el del video
En las miniaturas aparece **con orejas, con más detalle, sombreado rico y estilo casi 3D**. En el
video es plano y sin orejas. **Y las miniaturas con ese estilo son justo las que rinden 13-14 %.**

> ⚠️ **Consecuencia importante:** la consistencia del personaje se exige **dentro del video**, no
> en la miniatura. La miniatura tiene su propio lenguaje y está funcionando. Cambiarla al estilo
> plano del video sería igualar hacia abajo algo que ya gana.

> ✅ **RATIFICADO POR DAVID EL 2026-08-30.** El loop de identidad visual generó una miniatura
> alternativa con el personaje plano y sin orejas (V6, en `IDENTIDAD_VISUAL_2026-08-30/`). David la
> comparó con la actual y **eligió mantener la de orejas y estilo 3D**. Este punto 7 deja de ser un
> conflicto abierto y pasa a ser regla: **ningún agente propone quitarle las orejas al personaje de
> una miniatura.** Si alguna vez se quiere medir, es un test A/B explícito, no una "corrección".

### 8. Densidad alta
Las ganadoras están **cargadas**: personaje + objeto + atrezzo + garabato + 3 bloques de texto.
La de 4,4 % es más limpia. En este nicho, limpio = invisible.

---

## Por qué la miniatura de "Discipline" fallaba

No es solo que el personaje fuera musculoso. **Rompía la fórmula entera**: sin banda roja, sin
taza, sin garabato, sin objeto-tema, y con un personaje ajeno al canal.

## Checklist antes de dar una miniatura por buena

- [ ] Banda roja con el setup en blanco, arriba a la izquierda
- [ ] Cuerpo en blanco + remate en **amarillo**
- [ ] Texto a la izquierda, personaje a la derecha
- [ ] Fondo casi negro con rim light
- [ ] Expresión facial fuerte, nunca neutra
- [ ] Taza "DISCIPLINE FOCUS FUTURE"
- [ ] Interrogaciones + ovillo mental arriba a la derecha
- [ ] Objeto-tema que se entienda de un vistazo
- [ ] **Legible a 210 px de ancho** (tamaño real en móvil)

---

## HERRAMIENTA AUTOMATICA (2026-08-30)

La formula de arriba esta implementada en **`miniatura.py`** (raiz de CLAUDE AUTOMATIC y copia en
esta carpeta). Genera una miniatura completa en segundos, sin gastar creditos de ninguna IA.

```bash
python miniatura.py <imagen> "SETUP" "CUERPO" "REMATE" "SUBTITULO" "PALABRA_ROJA" salida.jpg
```

Aplica sola: fuente **Anton** (se descarga sola si falta), banda roja de brocha con bordes
irregulares, textura de aranazos **solo sobre el relleno** de la letra, degradado oscuro a la
izquierda, remate en amarillo y subtitulo con una palabra en rojo.

**Aviso:** usa un fotograma del propio video como base. Las miniaturas del canal que rinden 13-14%
usan el personaje en version detallada (con orejas, sombreado 3D), que hay que generar en Artistly.
Para igualar ese estandar del todo, generar esa imagen aparte y pasarsela a la herramienta.

---

## REVISION 2026-08-30 — contrastada con los outliers ACTUALES del nicho

Se descargaron y midieron las miniaturas de los dos videos que estan facturando ahora con la
misma formula de titulo que usa Mindset Mechanics:

| Video | Vistas | Fondo | Color de remate | Cifra | Densidad |
|---|---|---|---|---|---|
| "Imagine Fake Scenarios" | 262.000 (4 sem) | **BLANCO** | rojo | no | **baja** |
| "People Who Rebuild Their Lives In Secret" | 158.000 (4 sem) | escena | ninguno | no | media |

**Lo que CONTRADICE la formula de este canal:**
- Ninguna de las dos usa **amarillo**.
- Ninguna usa **cifras**.
- Ninguna es tan **densa** como las de Mindset Mechanics.
- Una usa **fondo blanco**, lo contrario al fondo casi negro del canon.

**Por que NO se cambia la formula pese a eso:** el 13-14% de CTR de `predators` y `glitch` son
datos propios, de la audiencia real de este canal. Los de esos videos son de otros canales con
otro publico. **No se tira lo que funciona por lo que le funciona a un tercero.**

**Lo unico que SI se corrigio, porque ambas referencias coinciden y el canal se quedaba corto:**

### 9. EL TEXTO TIENE QUE SER MAS GRANDE
Las dos referencias dedican casi la mitad del ancho al texto. Las miniaturas del canal se quedaban
por debajo. **Escala aplicada: +22%** sobre el tamano anterior (`esc=1.22` en `miniatura.py`),
con el degradado oscuro extendido al 74% del ancho para que el texto respire.

Se descarto el +40%: gana legibilidad pero tapa al personaje, y el punto 4 de esta formula dice
que la expresion fuerte del personaje es lo que hace funcionar la miniatura.

**Metodo reutilizable:** sacar los IDs de los videos outlier de la busqueda de YouTube y bajar sus
miniaturas de `https://i.ytimg.com/vi/<ID>/maxresdefault.jpg`. Es gratis y son los datos reales.
