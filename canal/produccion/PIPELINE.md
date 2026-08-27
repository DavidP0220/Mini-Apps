# PIPELINE DE PRODUCCIÓN — el orden, y no se salta ninguno

Esta es la cronología oficial de cada video. Existe para que **nada se genere antes de estar
decidido en papel**. Saltarse pasos es lo que produjo el rechazo del piloto anterior (error E-02)
y el consumo del presupuesto de generaciones (E-05).

```
 1. TEMA + TÍTULO          El título se elige PRIMERO. Manda sobre todo lo demás (decisión D-02)
 2. GUION                  Plantilla de hook + cuerpo con bucles abiertos + cierre citable
 3. BEATS                  Desglose emocional con marca de tiempo
 4. STORYBOARD  ◄── GATE   Panel a panel, 12 campos. Aquí se para hasta que David/Kimi aprueben
 5. PROMPTS                Derivados mecánicamente de cada panel. Nada se improvisa aquí
 6. STILLS                 Imágenes fijas contra la referencia publicada
 7. ANIMACIÓN              Solo de paneles ya aprobados
 8. VOZ + SONIDO           Voz, música, capa de sonido del storyboard
 9. ENSAMBLAJE             Montaje + normalización de audio
10. CONTROL DE CALIDAD     Viendo el video entero, no una checklist de fotogramas
11. MINIATURA + VARIANTES  2 miniaturas y 2-3 títulos para la prueba A/B (decisión D-06)
12. PUBLICACIÓN            Jueves o domingo, 1-2 h antes del pico (decisión D-05)
13. MEDICIÓN               A los 10 días: métricas al repositorio (analista-datos)
```

## Los tres gates que no se cruzan solos
| Gate | Dónde | Quién autoriza |
|---|---|---|
| Storyboard aprobado | paso 4 | David o Kimi |
| Gasto de créditos de generación | pasos 6 y 7 | David (presupuesto explícito) |
| Publicación de contenido público | paso 12 | David |

## Reglas de producción que vienen de errores ya pagados
- **Ningún plano sostenido más de 5 segundos** sin cambio real de ángulo, escala o movimiento.
  Congelar un fotograma y hacerle zoom durante medio minuto no es una escena (E-02).
- **Dos pasadas fallidas del mismo método de consistencia = stop y escalada.** No hay tercera
  tanda de créditos con la misma técnica (E-05).
- **Mínimo 1080p**, verificado en el archivo de salida. La calidad solo sube (E-08).
- **Antes de construir sobre una capacidad de una herramienta externa, se verifica en su
  documentación oficial.** No se asume (E-14).
- **Al terminar: respaldo del archivo final fuera del repositorio.** Un sitio es cero sitios (E-10).
- **Si el identificador de un video cambia, se revisan todas sus referencias** abriéndolas (E-09).

## Medir siempre lo mismo
Cada video publicado deja una fila en `../base-conocimiento/04-metricas/METRICAS.md` a los 10
días: impresiones, CTR, vistas, duración media, suscriptores ganados. Sin esa fila, el video no
enseñó nada al sistema.
