# CATÁLOGO DE ERRORES — para no repetirlos

**Este es el documento más caro del proyecto.** Cada ficha de aquí costó tiempo, créditos o
un video rechazado. Se lee **antes** de aprobar cualquier plan, no después de fallar.

Fuente de las fichas E-01 a E-14: el archivo histórico del proyecto anterior
(`canal/archivo/2026-08-26_traslado_mindset_mechanics/`), en concreto los handoffs y reportes
del puente con Kimi (23 al 26 de agosto de 2026) y la memoria persistente de aquellas sesiones.

**Cómo se usa:** el agente `arqueologo-memoria` contrasta cada plan nuevo contra esta lista y
responde *"choca con E-XX"* o *"limpio"*. Es un veto técnico, no una opinión.
**Cómo crece:** cada fallo nuevo entra aquí el mismo día, con causa raíz real. Nunca se borra
una ficha; si deja de aplicar se marca OBSOLETA con fecha y motivo.

---

### E-01 — Parchear sin investigar primero
**Cuándo:** 2026-08-23 · **Coste:** dos rondas de generación desperdiciadas
**Síntoma:** ante un fallo de calidad se aplicó el primer arreglo que se ocurrió, dos veces seguidas, y las dos veces volvió a fallar.
**Causa raíz:** se trató un problema de método como si fuera un bug puntual. No se consultó cómo lo resuelve el resto del mercado ni la documentación de la propia herramienta antes de tocar nada.
**Antídoto:** ante cualquier problema no trivial, **investigar primero** (web, documentación oficial, cómo lo hacen los que ya lo resolvieron) y **después** ejecutar el arreglo. No hace falta pedir permiso para investigar: es parte de arreglar.
**Verificación:** todo reporte de fix incluye la fuente que respalda el método elegido.

---

### E-02 — Pasar el control de calidad técnico y fallar el del usuario
**Cuándo:** 2026-08-23 · **Coste:** un video completo de 12 escenas rechazado entero
**Síntoma:** el video superó la checklist automatizada de estilo por fotograma, y al verlo David lo rechazó: *"las animaciones duran más de 5 segundos, se repiten, se ve muy cuadriculado, no se ve para nada dinámico, no hay transiciones cinematográficas, tampoco hay cambios de ángulo o de perspectiva"*.
**Causa raíz:** el defecto no estaba en la plantilla de estilo sino en la **arquitectura del ensamblaje**: un clip real corto (5-8 s) seguido de un fotograma congelado con zoom durante 30-53 s. La checklist medía estilo por fotograma, así que era ciega a un problema de movimiento y de montaje.
**Antídoto:** ningún plano se sostiene más de 5 s sin cambio real de ángulo, escala o movimiento. Varias tomas reales por escena, no una toma y relleno. Y **el control de calidad se hace viendo el video, no leyendo una checklist de fotogramas**: una checklist que no puede detectar el defecto no es un control de calidad.
**Verificación:** el storyboard declara la duración de cada plano y qué cambia entre planos consecutivos; el revisor ve el render completo antes de aprobar.

---

### E-03 — Actuar sobre datos que venían de un resumen, no de la fuente
**Cuándo:** 2026-08-23 · **Coste:** 5 de 14 enlaces mal puestos, detectados por casualidad
**Síntoma:** el listado de IDs de video que se arrastraba de una sesión anterior no coincidía con la realidad del canal; varios enlaces apuntaban a videos equivocados.
**Causa raíz:** se confió en un resumen de contexto de una sesión previa en vez de leer el estado real en la plataforma. Los resúmenes comprimen y envejecen.
**Antídoto:** **cualquier lista de identificadores, cifras o estados que venga de contexto resumido se re-verifica contra la fuente real** (YouTube Studio, la API, el archivo) antes de actuar sobre ella.
**Verificación:** el reporte dice explícitamente "verificado contra <fuente> el <fecha>", uno por uno, no "enlazado".

---

### E-04 — Leer ruido estadístico como si fuera señal
**Cuándo:** 2026-08-26 · **Coste:** casi un rediseño de miniatura innecesario
**Síntoma:** un video mostraba un CTR aparentemente bajo y estuvo a punto de tratarse como una miniatura fallida. Tenía **23 impresiones**.
**Causa raíz:** se miró el porcentaje sin mirar el tamaño de la muestra.
**Antídoto:** por debajo de ~500 impresiones no se concluye nada y no se rediseña nada. Y la regla que va con ella: **nunca se cambia una miniatura que ya funciona.** El cuello de botella de un canal pequeño casi siempre es *pocas impresiones*, no *mal CTR* — y eso se arregla publicando más, no rediseñando.
**Verificación:** toda conclusión sobre CTR va acompañada del número de impresiones.

---

### E-05 — No parar a tiempo cuando la técnica de consistencia falla
**Cuándo:** 2026-08-23/25 · **Coste:** el presupuesto entero de generaciones (27) consumido en dos pasadas fallidas
**Síntoma:** el personaje seguía saliendo con rasgos que no le corresponden (orejas, nariz) pese a arreglos sucesivos del prompt. David: *"sigue siendo muy diferente al personaje que ya tenemos publicado"*.
**Causa raíz:** la técnica elegida tenía un techo real de fiabilidad, y se insistió con variantes del mismo método en vez de reconocer el techo y cambiar de técnica.
**Antídoto:** **dos pasadas fallidas del mismo método = stop y escalada.** No hay tercera tanda de créditos con la misma técnica; se escala a quien decide alcance y presupuesto, con las opciones ya evaluadas. Y los rasgos prohibidos se declaran en negativo explícito en cada prompt, comparando siempre contra la referencia publicada.
**Verificación:** el reporte de cada tanda dice cuántas pasadas lleva esa técnica.

---

### E-06 — Mezclar el contenido de un canal dentro del repositorio de otro
**Cuándo:** 2026-08-25 (segunda vez; ya había pasado antes) · **Coste:** historial ensuciado y una corrección manual
**Síntoma:** documentos de estrategia de un canal terminaron commiteados dentro del repo de otro canal distinto. La primera vez incluso se añadieron a la lista blanca del `.gitignore`, lo que lo hizo invisible.
**Causa raíz:** cercanía física en el disco tratada como pertenencia al mismo proyecto.
**Antídoto:** cada canal tiene su espacio. Entre proyectos **solo** se comparten habilidades técnicas (patrones de código, arreglos genéricos) y hallazgos generales (algoritmo, requisitos de monetización, buenas prácticas de título o miniatura). **Nunca** se comparten documentos de estrategia, guiones, biblias de estilo ni datos de cuenta.
**Verificación:** antes de commitear, revisar que ningún archivo nuevo pertenezca a otro canal.

---

### E-07 — Comunicarse con David en inglés
**Cuándo:** regla fijada 2026-08-23 · **Coste:** instrucciones no entendidas
**Síntoma:** explicaciones y pasos narrados en inglés a un usuario que no lee inglés.
**Causa raíz:** confundir el idioma del **producto** (el canal publica en inglés) con el idioma de la **conversación**.
**Antídoto:** todo lo dirigido a David va en español, incluidos los pasos que se hagan dentro de YouTube Studio aunque la interfaz esté en inglés. El contenido del canal, los prompts y las descripciones públicas siguen en inglés.
**Verificación:** ningún documento de trabajo ni resumen sale en inglés.

---

### E-08 — Bajar la calidad para ir más rápido
**Cuándo:** regla fijada 2026-08-23 · **Coste:** ninguno todavía, es preventiva
**Síntoma:** riesgo de exportar por debajo de 1080p, o de elegir la vía rápida frente a la buena.
**Causa raíz:** tratar la calidad como una variable de ajuste.
**Antídoto:** mínimo **1080p** en todo, largos y Shorts por igual, verificando la resolución real de salida y no asumiéndola. Regla general de David: *"nunca bajar la calidad de nada — antes subirla siempre: de producción, de ideas, de estrategias, de optimización del canal"*. Ante cualquier disyuntiva velocidad/calidad, se elige calidad.
**Verificación:** la resolución de salida se comprueba en el archivo, no en la configuración.

---

### E-09 — Dejar links rotos en contenido público tras resubir un video
**Cuándo:** detectado 2026-08-23 · **Coste:** tres descripciones públicas apuntando a un video eliminado
**Síntoma:** tres publicaciones tenían en su descripción un enlace a un video que ya no existe, porque ese video se había resubido con otro identificador.
**Causa raíz:** al resubir se actualizó el video pero no todo lo que apuntaba a él. No existía una lista de referencias a revisar.
**Antídoto:** cuando cambia el identificador de un video, se revisan **todas** sus referencias: descripciones, tarjetas, videos relacionados, comentarios fijados, enlaces externos. Y se comprueba abriendo el enlace, no leyéndolo.
**Verificación:** cada enlace público se abre una vez después del cambio.

---

### E-10 — Activos de producción sin respaldo real
**Cuándo:** reportado 2026-08-25, **riesgo abierto** · **Coste potencial:** ~669 MB de video irrecuperable
**Síntoma:** los videos finales y muchos Shorts existían **solo** en el disco de David y en las plataformas que los generaron. Esas plataformas borran los archivos a los 60 días.
**Causa raíz:** confundir "está en la plataforma" con "está respaldado", y que el repositorio rechaza archivos de más de 100 MB.
**Antídoto:** todo activo aprobado se copia a almacenamiento en la nube propio. Un archivo que existe en un solo sitio, o solo en un servicio que caduca, **cuenta como no respaldado** y se reporta como riesgo abierto hasta que deje de serlo. El inventario de lo que está fuera del repositorio se mantiene al día con ruta y tamaño.
**Verificación:** el inventario dice, por cada activo pesado, en cuántos sitios distintos vive.

---

### E-11 — `.gitignore` de lista blanca que ignora carpetas nuevas en silencio
**Cuándo:** 2026-08 · **Coste:** trabajo commiteado que en realidad no se subió
**Síntoma:** carpetas nuevas no aparecían en el repositorio pese a haber hecho commit.
**Causa raíz:** el `.gitignore` estaba escrito como lista blanca (ignora todo salvo lo permitido), así que cualquier carpeta nueva quedaba fuera sin aviso.
**Antídoto:** revisar el `.gitignore` **antes** de crear una carpeta nueva, y después de commitear comprobar con `git status --ignored` que no quedó nada fuera. Ojo también con los `.gitignore` que vengan dentro de material archivado: se renombran al archivar.
**Verificación:** `git status` limpio **y** el archivo visible en el remoto.

---

### E-12 — Invertir en Shorts esperando que arrastren a los videos largos
**Cuándo:** medido 2026-08-22, confirmado 2026-08-25 · **Coste:** 19 Shorts producidos, 0 suscriptores atribuibles
**Síntoma:** 95 vistas de Shorts produjeron 8 minutos vistos y 0 suscriptores; 146 vistas de videos largos produjeron 398 minutos y 4 suscriptores.
**Causa raíz:** no es un problema de ejecución: la plataforma **separó el ranking de formato corto y largo**, así que un Short ya no empuja al espectador hacia el video largo por sí solo.
**Antídoto:** el formato largo es el que convierte y el que suma horas de visualización. Si se retoma el formato corto, cada pieza necesita un gancho explícito hacia el video largo (comentario fijado, llamada en pantalla, enlace) porque el algoritmo ya no hace esa conexión solo.
**Verificación:** cada hora de producción se justifica contra el número que mueve.

---

### E-13 — Cruzar un gate del plan activo sin autorización
**Cuándo:** regla del puente, vigente · **Coste:** potencialmente un presupuesto entero
**Síntoma:** riesgo de lanzar una producción completa mientras un piloto reducido sigue pendiente de veredicto.
**Causa raíz:** confundir "el trabajo está listo" con "el trabajo está autorizado".
**Antídoto:** el plan activo es el último `HANDOFF_*.md`. Sus gates no se cruzan sin autorización escrita. Si la investigación sugiere cambiar el plan, se propone en un handoff nuevo que diga explícitamente **qué reemplaza** — no se ejecuta directamente. Mientras hay un gate cerrado, se avanza solo en tareas de coste cero.
**Verificación:** cada ronda empieza leyendo el handoff más reciente y nombrando los gates abiertos.

---

### E-14 — Asumir que la herramienta soporta un formato sin verificarlo
**Cuándo:** 2026-08-25 · **Coste:** replanteo de toda la producción de imágenes
**Síntoma:** se dio por hecho que el generador de imágenes producía 16:9 exacto. No lo hace: su lista de tamaños es cerrada por familia de modelo, y el más ancho disponible se queda fuera de la tolerancia, mientras que el sistema de animación **solo** acepta 16:9 o 9:16.
**Causa raíz:** se asumió una capacidad en vez de comprobarla en la documentación de referencia de la propia herramienta.
**Antídoto:** antes de construir un pipeline sobre una capacidad de una herramienta externa, **verificarla en su documentación oficial** y dejar la cita en la ficha. Las capacidades de estas plataformas cambian y no son intuitivas.
**Verificación:** la ficha de la herramienta enlaza el apartado concreto de la documentación que respalda la capacidad usada.

---
---

### E-15 — Producir con plantilla + IA + volumen: el perfil que YouTube está terminando
**Cuándo:** enforcement real de enero de 2026, fichado aquí el 2026-08-27 · **Coste potencial:** el canal entero, y la expulsión permanente del programa de socios
**Síntoma:** el atajo obvio para monetizar rápido — una plantilla de guion, narración de IA uniforme, visuales genéricos y mucho volumen — es exactamente el perfil que la política de "contenido no auténtico" persigue.
**Causa raíz:** la política no castiga el formato sin rostro ni el uso de IA por separado. Castiga la **combinación** de salida masiva plantillada sin ángulo editorial propio. Es fácil caer en ella sin querer cuando el objetivo es "monetizar rápido".
**Evidencia:** en enero de 2026 se terminaron **16 canales con 35 millones de suscriptores combinados y 4.700 millones de vistas**. Caso documentado: un canal de ~588.000 suscriptores fue desmonetizado por narración de IA uniforme, visuales plantillados y estructura repetitiva. Sistema de tres avisos: aviso → suspensión de 90 días → expulsión permanente. Fuentes citadas en `PLAN_MAESTRO_PORTAFOLIO.md` del repositorio `DavidP0220/mindset-mechanics`.
**Antídoto:** **guion original y ángulo editorial propio en cada video** — nunca la misma plantilla rellenada. Identidad visual diferenciada por canal. Y la regla dura que ya estaba escrita y sigue vigente: **cero generación de contenido pago para un canal hasta que tenga nombre confirmado y cuentas reales creadas.** Si un canal del portafolio empieza a parecerse a otro, eso es la señal de alarma, no una eficiencia.
**Verificación:** antes de publicar, la pregunta es "¿este video tiene un ángulo que no tendría ningún otro canal del nicho?". Si la respuesta es no, no se publica.

---

### E-16 — Dos líneas de trabajo en paralelo que no se ven entre sí
**Cuándo:** 23 al 26 de agosto de 2026, detectado el 2026-08-27 · **Coste:** tres decisiones estratégicas paradas cuatro días, y dos pipelines distintos construidos para lo mismo
**Síntoma:** el proyecto avanzó simultáneamente en tres sitios que no se sincronizaban: el repositorio donde trabaja Kimi, un paquete de traslado de otra máquina, y un tercer repositorio. Los handoffs de Kimi del 23-ago se quedaron sin respuesta porque la sesión que siguió trabajando estaba en la otra línea.
**Causa raíz:** no había una **fuente única de verdad** declarada, y el puente con el estratega dependía de un traslado manual que nadie ejecutó. Ya había un antecedente: dos sesiones de Claude Code trabajando sobre el mismo repositorio a la vez, con commits casi idénticos.
**Antídoto:** una sola fuente de verdad declarada por escrito, y una sesión activa a la vez. Antes de empezar a trabajar, verificar la fecha del último commit real (`git log -1`) y de los handoffs pendientes; si hay trabajo posterior a lo que tenemos, se consolida **antes** de producir nada nuevo.
**Verificación:** cada ronda abre nombrando cuál es la fuente única y cuál fue su último movimiento.



## Los seis antipatrones, en una línea cada uno

1. **Asumir en vez de verificar** (E-03, E-14) — la fuente real, siempre, aunque cueste 5 minutos.
2. **Insistir con un método que ya falló** (E-01, E-05) — dos fallos y se para.
3. **Confundir la métrica con la señal** (E-04, E-12) — mira el tamaño de muestra y el número que de verdad importa.
4. **Dar por respaldado lo que solo existe en un sitio** (E-10, E-11) — un sitio es cero sitios.
5. **Aprobarse el trabajo a uno mismo** (E-02, E-13) — el control de calidad y la autorización son de otro.
6. **Trabajar sin fuente única de verdad** (E-15, E-16) — dos líneas en paralelo producen el doble de trabajo y la mitad de avance, y el atajo plantillado cuesta el canal.
