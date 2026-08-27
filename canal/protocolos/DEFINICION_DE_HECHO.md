# DEFINICIÓN DE "HECHO"

Una tarea no está hecha porque el agente diga que la hizo. Está hecha cuando cumple **todo**
lo que le aplica de esta lista. El jefe no aprueba nada que no la cumpla.

## Para cualquier entrega
- [ ] Está **escrito en un archivo del repositorio**, no solo dicho en el chat. Lo que no está en el repo, no existe.
- [ ] Está **en español** (si va dirigido a David).
- [ ] Tiene **fecha** y dice **qué agente** lo produjo.
- [ ] El índice `canal/base-conocimiento/00-INDICE.md` está actualizado.
- [ ] Hay una entrada en `canal/bitacora/` de esa ronda.
- [ ] Está **commiteado y pusheado**, y verificado en el remoto.

## Para una investigación
- [ ] Cada dato lleva **fuente + fecha de consulta**.
- [ ] Cada porcentaje lleva su **tamaño de muestra**.
- [ ] Termina en una **recomendación cerrada**: adoptar / probar con presupuesto X / descartar y por qué.
- [ ] Dice qué decisión previa **confirma o contradice**.

## Para un análisis de datos
- [ ] Las cifras vienen de la **fuente real**, con fecha de captura, no de un resumen.
- [ ] Ningún veredicto sobre una muestra por debajo del umbral (`04-metricas/METRICAS.md` §3).
- [ ] Dice explícitamente **qué número del objetivo mueve** esa conclusión.

## Para un storyboard
- [ ] Los **doce campos** rellenos en **todos** los paneles.
- [ ] Ningún plano sostenido más de 5 s sin cambio real de ángulo, escala o movimiento.
- [ ] La escala de plano **varía** entre paneles consecutivos.
- [ ] La checklist de verificación está rellenada punto por punto al final del documento.
- [ ] Aprobado por David o por Kimi. **Un agente no aprueba su propio trabajo.**

## Para un video
- [ ] Mínimo **1080p** verificado **en el archivo de salida**, no en la configuración.
- [ ] Audio normalizado.
- [ ] Revisado **viéndolo entero**, no leyendo una checklist de fotogramas (error E-02).
- [ ] Variantes de título y miniatura listas para la prueba A/B.
- [ ] Todas las referencias al video (descripciones, tarjetas, enlaces) comprobadas **abriéndolas** (error E-09).
- [ ] Copia de respaldo del archivo final fuera del repositorio (error E-10).

## Para cerrar una ronda
- [ ] `canal/ESTADO.md` actualizado: números de hoy contra los de la ronda anterior, qué se
      movió, qué se debe, las 3 acciones de mañana con responsable, y el bloqueante más caro.
- [ ] Si hay algo que decidir arriba, hay un `HANDOFF_` en `canal/puente-kimi/` con la pregunta
      **cerrada** y las opciones ya evaluadas.
