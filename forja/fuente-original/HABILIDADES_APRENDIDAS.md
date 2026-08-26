# Habilidades aprendidas construyendo este sistema

Este documento no habla del producto (eso está en `investigacion/`) — habla del **método** usado
para construirlo, para que otra sesión de Claude en otro proyecto pueda replicarlo sin
redescubrirlo desde cero. Cada habilidad incluye qué problema resuelve y evidencia concreta de
que funcionó en este proyecto.

## 1. Documentos vivos como memoria real de agentes sin estado

**El problema que resuelve:** un subagente no recuerda nada entre invocaciones. Sin un lugar donde
persista lo investigado, cada sesión nueva reinvestiga desde cero o, peor, actúa sobre supuestos
viejos sin saberlo.

**Cómo se hizo aquí:** 7 documentos markdown en `investigacion/`, cada uno con dueño único (un
agente específico), con estas reglas no negociables:
- Cada documento lleva su propia fecha de "última actualización" en el encabezado.
- Cada documento cierra con una sección **"Preguntas abiertas"** — lo que la última pasada de
  investigación no pudo resolver, para que la próxima sesión no empiece de cero ni repita lo ya
  hecho.
- Los agentes tienen instrucción explícita de **actualizar, nunca reescribir**: añadir lo nuevo,
  marcar qué cambió y desde cuándo, y nunca borrar una entrada vieja sin dejar rastro de que existió.

**Evidencia de que funcionó:** en la segunda pasada de investigación (2026-08-25/26), los agentes
`higgsfield-market-intel` y `higgsfield-tech-scout` cerraron 6 de las 9 preguntas abiertas
originales con búsquedas frescas, y una de ellas resultó en la corrección de un error real del
informe original (ver habilidad 3).

## 2. Un agente por dominio, con límites explícitos de qué NO hacer

**El problema que resuelve:** un solo agente "que haga de todo" mezcla investigación de mercado con
decisiones de gasto — y termina tomando decisiones de negocio con autoridad que nadie le dio.

**Cómo se hizo aquí:** 3 agentes, cada uno con una frase explícita en su propia definición sobre lo
que NO le corresponde decidir:
- `higgsfield-market-intel` — solo trae hechos de mercado, nunca decide estrategia.
- `higgsfield-tech-scout` — solo trae hechos técnicos/legales, nunca decide estrategia.
- `higgsfield-product-architect` — el único que decide y registra, pero con la regla dura de nunca
  ejecutar gasto real sin aprobación explícita del humano.

**Por qué importa:** permite lanzar a los dos primeros **en paralelo** sin riesgo de que pisen
decisiones del tercero, y que el tercero delegue investigación fresca a los otros dos (vía el tool
`Agent`) en vez de decidir sobre datos que podrían estar desactualizados.

## 3. Verificar la fuente primaria en vez de confiar en el resumen (incluso el propio)

**El problema que resuelve:** un informe de investigación (aunque venga "verificado por 3
validadores") puede tener errores de interpretación que se propagan si nadie vuelve a la fuente.

**Evidencia concreta de este proyecto:** el PDF original afirmaba que revender acceso a Runway
"requiere plan Enterprise". `higgsfield-tech-scout` leyó los ToS reales con `WebFetch` en vez de
confiar en ese resumen, y encontró que el informe mezclaba dos cosas legalmente distintas
(revender el *acceso a la cuenta* del proveedor vs. construir un *producto propio* que usa la API
como backend) — la segunda sí es legal sin plan Enterprise. Esa corrección cambió una decisión de
arquitectura real (`06_DECISIONES_PRODUCTO.md`, D-002/D-003).

**Regla derivada:** ante cualquier ToS, contrato o política que determine si algo es legal/posible,
leer el documento primario con `WebFetch`, no solo el resumen de un informe anterior — por bueno
que sea ese informe.

## 4. Gate de validación barato antes de construir caro

**El problema que resuelve:** construir un MVP completo antes de validar el supuesto técnico más
riesgoso desperdicia semanas si ese supuesto falla.

**Cómo se hizo aquí:** la investigación identificó que nadie sabe si Lovable/Supabase aguanta colas
de generación de IA de varios minutos (doc 03). En vez de construir el producto completo y
descubrirlo tarde, el roadmap (`05_PRESUPUESTO_Y_CRONOGRAMA.md`, Fase 2) aísla esa pregunta en una
prueba de **$20 y 5 días** con un semáforo verde/rojo explícito, antes de comprometer el resto del
presupuesto de Nivel 1 ($90-$230/mes).

**Regla derivada:** cuando la investigación deja un riesgo técnico sin resolver que ninguna
búsqueda web puede contestar (solo un experimento real lo prueba), ese experimento va primero en
el roadmap, aislado y barato, con criterio explícito de éxito/fracaso — no al final del MVP.

## 5. Marcar cada paso que cuesta dinero, no solo el presupuesto total

**El problema que resuelve:** un roadmap con "presupuesto total: $230/mes" no le dice a alguien no
técnico *cuándo* exactamente va a tener que sacar la tarjeta — y un agente con autoridad para
"avanzar el proyecto" podría activar un gasto sin que el humano se dé cuenta a tiempo.

**Cómo se hizo aquí:** cada paso del roadmap que implica gastar dinero real lleva la etiqueta
literal **`[GASTO — requiere OK de David]`**, y la regla está en la propia definición del agente
`higgsfield-product-architect`: "nunca ejecutas gasto real... sin que el usuario lo confirme
explícitamente". El roadmap distingue "costo real comprometido hasta hoy: $0.00" de "presupuesto
planeado".

## 6. Escribir para quien no sabe programar, sin perder precisión técnica

**El problema que resuelve:** un roadmap que dice "configura Supabase con Edge Functions" es inútil
para alguien sin experiencia técnica, aunque sea correcto.

**Cómo se hizo aquí:** cada paso del roadmap dice literalmente en qué sitio web entrar, qué botón
apretar, y cuando hace falta, el prompt exacto para copiar y pegar en Lovable (ver
`05_PRESUPUESTO_Y_CRONOGRAMA.md`, Fase 2, Paso 2.1) — sin sacrificar el detalle técnico real
(patrón webhook/callback, secretos de Supabase, etc.), solo traduciéndolo a acción concreta.

## 7. Revisión humana antes de comprometer un agente a ejecutar

**El problema que resuelve:** lanzar directo a "decidir y ejecutar" sin que el humano vea la
investigación cruda arriesga que apruebe algo que no entendió bien.

**Cómo se hizo aquí:** antes de lanzar a `higgsfield-product-architect`, se armó un **dossier
visual** (`dossier_html/dossier_higgsfield.html`, publicado también como Artifact) que resume los 4
documentos de investigación con las correcciones y preguntas abiertas más importantes, para que
David revisara con calma antes de decir "hágamolo". Esto separó explícitamente el momento de
"revisar investigación" del momento de "aprobar ejecución".

## 8. Sincronizar el resumen de decisiones con la fuente completa

**El problema que resuelve:** un resumen ejecutivo que vive solo en el chat se pierde cuando la
conversación se resume o termina.

**Cómo se hizo aquí:** cada decisión (`06_DECISIONES_PRODUCTO.md`) sigue un formato fijo — decisión,
razón con referencia al documento de evidencia, alternativas descartadas y por qué, y si es
reversible — de modo que el documento por sí solo (sin el chat) explica el razonamiento completo.

## 9. Auditar la propia infraestructura del sistema, no solo el producto

**El problema que resuelve:** un sistema de conocimiento "permanente" que en realidad no se está
respaldando es una falsa sensación de seguridad.

**Evidencia concreta de este proyecto:** al armar este mismo paquete (2026-08-26), se encontró que
la carpeta completa `investigacion/` (origen: `PROYECTO HIGGSFIELD ALTERNATIVA/`) llevaba 24 horas
sin ningún respaldo en git, por el mismo tipo de bug de `.gitignore` de lista blanca que ya se
había encontrado y arreglado un día antes en otro módulo del mismo proyecto (ver
`investigacion/07_ERRORES_Y_LECCIONES.md`, entrada 1). El error se repitió porque nadie verificó la
carpeta nueva contra esa lección ya documentada.

**Regla derivada:** una lección documentada en `07_ERRORES_Y_LECCIONES.md` no sirve si nadie la
consulta al crear infraestructura nueva — verificar contra el registro de errores existente es
parte de crear cualquier carpeta/módulo nuevo, no un paso opcional.
