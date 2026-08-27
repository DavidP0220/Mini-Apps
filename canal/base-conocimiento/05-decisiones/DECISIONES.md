# DECISIONES — qué se decidió, cuándo y por qué

Registro **append-only** de las decisiones cerradas del proyecto. Una decisión que aquí figura
como vigente **no se reabre** sin evidencia nueva y posterior que la contradiga; si se reabre,
se añade una decisión nueva que diga explícitamente **a cuál reemplaza**, y la vieja se marca
SUPERADA con fecha. Nunca se borra.

Formato: `D-NN · fecha · decisión · por qué · quién · estado`.

---

### D-01 · 2026-08-22 · La vía a la monetización es el formato largo, no el corto
**Por qué:** 11 de los 12 canales analizados crecieron con cero o casi cero formato corto. Dato
propio: 95 vistas de corto → 0 suscriptores; 146 de largo → 4 suscriptores y 398 minutos. Y el
motivo estructural (confirmado en agosto de 2026): la plataforma separó el ranking de corto y
largo, así que el corto ya no arrastra espectadores al largo por sí solo.
**Quién:** estrategia, sobre dataset medido. **Estado:** VIGENTE. Ver error E-12.

### D-02 · 2026-08-22 · El título es el cuello de botella, antes que el tema y que la producción
**Por qué:** mismo canal, mismo guionista, misma calidad de miniatura, hasta 70x de diferencia
de vistas cambiando solo la fórmula del título. Antes de tocar producción, se arregla el título.
**Estado:** VIGENTE.

### D-03 · 2026-08-22 · No se pide la suscripción en voz alta
**Por qué:** 6 de 6 canales analizados en profundidad tienen cero menciones habladas de
suscripción en sus guiones top y convierten igual o mejor. Pedirla cuesta retención justo en el
segundo en que el espectador decide si se queda. Se sustituye por "comenta un número" y por una
frase final citable; la línea de suscripción vive solo en la descripción.
**Estado:** VIGENTE.

### D-04 · 2026-08-22 · Volumen sobre perfección, con horizonte de 6-9 meses
**Por qué:** ley de potencia del nicho: el 3-10% de los videos hace el 75-90% de las vistas.
Se publica la misma plantilla con disciplina y se espera a que 1 de cada 8-15 rompa.
**Estado:** VIGENTE.

### D-05 · 2026-08-25 · Cadencia: 2 videos largos por semana, jueves y domingo, nunca lunes
**Por qué:** investigación de agosto de 2026 sobre franjas de publicación; domingo es
especialmente fuerte para contenido de desarrollo personal. Se publica 1-2 h antes del pico
porque la plataforma decide cuánto empujar en las primeras 2-4 horas.
**Estado:** VIGENTE, **a revisar con datos propios a las 6-8 semanas** de publicar. Es un punto
de partida genérico, no una verdad fija: la ventana óptima varía hasta 4 h entre canales del
mismo nicho.

### D-06 · 2026-08-25 · Toda publicación pasa por prueba A/B nativa de título y miniatura
**Por qué:** 2-3 variantes de título y 2 de miniatura por video, corriendo en la herramienta de
comparación de la propia plataforma. Prohibido el clickbait que el contenido no paga: el
algoritmo lo castiga activamente, no es solo una norma editorial.
**Estado:** VIGENTE.

### D-07 · 2026-08-25 · Nada se genera sin storyboard aprobado
**Por qué:** el piloto que se produjo sin storyboard completo fue rechazado entero (E-02) y
consumió el presupuesto de generaciones (E-05). El storyboard es el punto donde se decide en
papel lo que si no se descubre pagando en pantalla.
**Estado:** VIGENTE.

### D-08 · 2026-08-25 · Los activos aprobados se respaldan fuera del repositorio
**Por qué:** el repositorio rechaza archivos de más de 100 MB, y las plataformas generadoras
borran los originales a los 60 días. Un archivo que solo vive en un sitio no está respaldado.
**Estado:** VIGENTE, con **riesgo abierto** mientras el respaldo no esté hecho. Ver E-10.

### D-09 · 2026-08-25 · Cada canal, su propio espacio; entre canales solo se comparte técnica
**Por qué:** mezclar documentos de un canal dentro del repositorio de otro ya pasó dos veces y
ensucia el historial y el contexto de ambos. Se comparten habilidades técnicas y hallazgos
generales; nunca estrategia, guiones, biblias de estilo ni datos de cuenta.
**Estado:** VIGENTE. Ver E-06.

### D-10 · 2026-08-27 · Este sistema de agentes vive en `canal/`, aislado del motor de mini-apps
**Por qué:** consecuencia directa de D-09 aplicada a este repositorio. `canal/` es autocontenido
para poder moverse entero a un repositorio propio del canal en cuanto exista, sin tocar nada del
motor de mini-apps ni de las apps.
**Quién:** acordado al montar el sistema. **Estado:** VIGENTE.

---

## Decisiones pendientes (las que bloquean, y de quién dependen)

| # | Decisión pendiente | Depende de | Bloquea |
|---|---|---|---|
| P-01 | Nombre, nicho exacto y ángulo del canal nuevo | David + Kimi, con el análisis de `investigador-nicho` sobre la mesa | Todo lo demás |
| P-02 | Formato de producción: con personaje fijo o narración sobre pictogramas | David | Coste y velocidad de cada video |
| P-03 | Presupuesto mensual de generación (imagen/video/voz) | David | Cuántos videos por semana son realistas |
| P-04 | Dónde se respaldan los activos pesados | David | Riesgo E-10 |
