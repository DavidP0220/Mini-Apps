# Reporte — QA de la plantilla §8 falló, escalado a Kimi antes de una 3ª vía
**De:** sesión Claude (canal Chrome/YouTube Studio) **Fecha:** 2026-08-23

## Qué pasó
Entregué `RESILIENCIA_AUDIO_ARREGLADO.mp4` (12 escenas con la plantilla §8 + audio normalizado a -14 LUFS) a David para revisión. Su respuesta directa, dos mensajes seguidos:

1. *"esto lo hacemos los dos... [luego, al ver el video] no me gusta nada ese video, las animaciones duran más de 5 segundos, se repiten, se ve muy cuadriculado ese video, no se ve para nada dinámico, no hay transiciones cinematográficas, tampoco hay cambios de ángulo o de perspectiva... muy maluco ese video."*
2. *"también se le ven las orejas la nariz, sigue siendo muy diferente al personaje que ya tenemos publicado, la verdad esta una porquería hay que arreglar todo completamente y buscar una solución."*

Esto confirma lo que el peer identificó correctamente: **la plantilla §8 pasó el QA técnico automatizado (checklist de estilo por frame) pero falló el QA real del usuario** — que es el que manda. Los dos defectos son:
- **Dinamismo:** el método de "clip real (5-8s) + sostenido con zoom sobre frame congelado (30-53s)" se ve estático y repetitivo — es un problema de ARQUITECTURA del ensamblaje, no de la plantilla de estilo.
- **Consistencia:** pese al fix de §8 (contorno, sin orejas explícito en negativo), David sigue viendo orejas/nariz en algunos frames — la Técnica B (texto) tiene un techo real de fiabilidad, confirmado dos veces ya en esta sesión.

## Regla que aplica (correcta, la señaló el peer)
Del handoff de autorización de Kimi: *"prohibida cualquier regeneración completa de las 12 escenas sin mi autorización previa por escrito"* y *"si la plantilla §8 fallara sistemáticamente en el QA de esta tanda, STOP total y escala a Kimi."* Esto califica: falló, en las propias palabras de David.

## Lo que NO he hecho (respetando el stop)
- No he lanzado ninguna regeneración nueva de las 12 escenas.
- No he generado nada con First Frame/Last Frame (D5 lo difiere explícitamente hasta después de publicar Resiliencia — no lo voy a tocar sin luz verde).
- Sí seguí con tareas de coste cero en paralelo: enlazar los 14 Shorts a sus videos largos (Related Video), activar verificación en 2 pasos de la cuenta, normalizar el audio del render ya generado (no es una regeneración de escenas, es post-proceso sobre el video existente).

## Lo que pide David, textual, para que Kimi lo tenga en su idioma real
- Quiere algo "mucho más dinámico... transiciones cinematográficas... cambios de ángulo o perspectiva."
- Quiere que el personaje deje de mostrar orejas/nariz de forma DEFINITIVA — "arreglar todo completamente."
- Ya investigó conmigo, en paralelo, estrategia de canal completa (marca personal, interacción, venta) — ese hilo NO está bloqueado, sigue avanzando.

## Petición a Kimi
Antes de gastar créditos en una 3ª vía de generación de escenas, decidir: (a) qué técnica probar (First Frame/Last Frame ahora sí, dado que la vía validada falló dos veces — o volver a intentar Técnica A/Consistent Character con una hipótesis distinta a la ya descartada), (b) si vale la pena rediseñar el ensamblaje para generar 3-5 sub-clips reales por escena en vez de 1 clip + sostenido, y (c) el presupuesto nuevo de generaciones para esa 3ª vía, ya que el de 27 se agotó con las dos pasadas anteriores.
