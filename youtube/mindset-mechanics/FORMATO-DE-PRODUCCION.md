# Formato de producción — decisión y evidencia

**Decidido el 2026-08-26.** Esta decisión va **antes** que la marca visual: define qué se ve en cada
video, y la marca tiene que derivarse de ella, no al revés.

---

## 1. Qué formato usan los que ganan en el nicho

De `PLAYBOOK_MONETIZACION.md`, datos ya verificados:

| Canal | Formato | Resultado |
|---|---|---|
| **Zenn** | Documental animado faceless, 8:00-8:40 | 32 videos → **179.000 subs**, 550k vistas de media |
| **Professor Stickman** | **Pictogramas, host ausente** | 200-540k por video con solo **24.400 subs** |
| **Decode The Brain** | **Sin host, narración sobre pictogramas** | *"Vía de producción más barata y rápida"* |
| ONLI | Personaje 2D, cabeza ovalada | 785k el video top |
| PsychToons | Cartoon | — |

**Ningún ganador del nicho usa 3D fotorrealista.** Dominan el 2D animado y los pictogramas.

## 2. La restricción que decide todo: tu capacidad real

Historial medido, de `LEEME-PRIMERO-HANDOFF.md`:

- **4 videos largos publicados en 5 semanas.**
- El quinto salió **impublicable**. Causa documentada: *"Personaje inconsistente — cara distinta en
  casi cada escena."*
- Toda la deuda técnica del paquete (`import_local_image()`, "Use Consistent Character", las tres
  iteraciones de `style_lock_v1..v3`) existe para resolver **ese único problema**.

El plan pide **8 largos al mes**. Con animación de personaje a ~50 escenas por video, el historial dice
que no ocurre. El personaje recurrente es la pieza más cara y más frágil del pipeline.

## 3. Decisión: documental cinematográfico sin personaje

Imágenes fijas generadas con IA + movimientos lentos de cámara (push in, paneo, tilt) + tipografía
animada + narración.

### Por qué

| Ventaja | Detalle |
|---|---|
| **Elimina el problema, no lo gestiona** | Sin personaje recurrente no hay consistencia que mantener. Es la causa raíz del único video fallido. |
| **~30 imágenes por video** en vez de 50 escenas animadas | 8 largos al mes pasa de imposible a realista. |
| **Las miniaturas salen gratis** | Cada video produce 30 frames cinematográficos; cualquiera sirve de miniatura, ya en la paleta de marca. |
| **Coherencia total** | El banner, el avatar y cada escena viven en el mismo mundo visual. |
| **Diferenciación** | En un feed donde todos los canales de psicología son cartoon plano, esto no se parece a nada. |

### El riesgo, dicho claro

Lo probado en este nicho es 2D y pictograma. Este formato **no está validado aquí**. Es una apuesta a
destacar por diferencia en vez de copiar lo que funciona. Si tras 3-4 videos el CTR no acompaña, la
salida es el formato pictograma de Professor Stickman, que es aún más barato de producir.

## 4. Biblia visual — Factory Settings

| Elemento | Regla |
|---|---|
| **Paleta** | Fondo `#02060E` casi negro · acento `#FF8A1F` ámbar incandescente · luz fría azul como contrapunto |
| **Luz** | **Un solo foco cálido por plano.** Fuego, brasa, lámpara, pantalla. Nunca dos focos compitiendo. |
| **Los dos colores nunca se tocan** | El ámbar es lo antiguo, el azul frío es lo moderno. Esa separación **es** la tesis. |
| **Caras** | Silueta o contraluz. **Nunca un rostro identificable.** Elimina el problema de consistencia y sube el misterio. |
| **Espacio negativo** | Generoso y deliberado. La distancia entre elementos carga el significado. |
| **Textura** | Grano de película, polvo en suspensión, luz volumétrica, profundidad de campo real. |
| **Prohibido** | Cartoon, 3D render brillante, vector plano, fondos blancos, texto dentro de la imagen generada. |

### Plantilla de prompt

```
A cinematic documentary still. [ESCENA]. Single warm amber light source
[fuente concreta] carving rim light onto [sujeto]. Cold blue darkness
everywhere else — the two colors never touch. Faces in silhouette or
backlit, never identifiable. Generous negative space. Volumetric light,
drifting dust motes, film grain, photographic depth of field, painterly
realism. Absolutely no text, no letters, no words anywhere.
No cartoon, no 3D render.
```

## 5. Cómo se monta un video

1. **Guion** (1.500-2.000 palabras para 10-13 min, a 150-172 palabras/minuto).
2. **Marcar 30 puntos de escena**, uno cada ~25 segundos.
3. **Generar 30 imágenes** con la plantilla de arriba.
4. **Animar**: push in lento (2-4% de zoom) o paneo por escena. Nunca cortes secos entre imágenes;
   fundidos de 0,4-0,6 s.
5. **Subtítulos quemados** obligatorios — de ellos dependen los recortes de Shorts.
6. **Salida 1920×1080 mínimo.**
7. **Miniatura**: elegir el frame más fuerte y añadirle 2-3 palabras encima, con el texto compuesto
   aparte, nunca generado dentro de la imagen.

## 6. Archivo de referencia

`marca/escena-ejemplo.png` — frame real generado para *The Psychology of People Who Apologize for
Everything*: el grupo alrededor del fuego, el excluido solo en el frío azul. Es el estándar visual a
igualar.

**Nota sobre el scoring:** vidIQ puntuó esa imagen 84 y criticó *"demasiado espacio vacío"*. Ese
criterio aplica a **miniaturas**, no a escenas. En un frame de video ese vacío es el mensaje. No
optimizar escenas con reglas de miniatura.
