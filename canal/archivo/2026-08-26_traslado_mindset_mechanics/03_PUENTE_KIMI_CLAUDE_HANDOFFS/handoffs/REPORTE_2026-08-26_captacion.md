# REPORTE - Captacion de audiencia nueva - 2026-08-26

Agente: growth-acquisition-lead. Creditos gastados: 0 (solo lectura de repo + investigacion web).

---

## 1. Estado REAL de los "4 videos guionados" - verificado, no asumido

El plan asume 4 videos guionados y listos para produccion visual. La verificacion contra archivos reales muestra que solo 2 de los 4 tienen guion escrito, no 4.

1. Why Didn't Evolution Remove Social Anxiety? -- guion completo: script_social_anxiety_video.md (22-ago, ~1.680 palabras, 10:30-11:00). Sin storyboard, sin audio, cero produccion visual empezada.
2. Why Didn't Evolution Fix Your Attention Span? -- NO existe ningun guion, solo la linea de idea en PLAYBOOK_MONETIZACION.md seccion 9.
3. Why Didn't Evolution Remove Jealousy? -- NO existe ningun guion, solo la idea en seccion 9.
4. Psychology of People Who Check the Door Three Times (= "Resiliencia") -- guion completo: script_resilience_video.md (19-ago), pero el titulo actual del archivo es "Why Your Brain Breaks Under Pressure And How to Stop It", no el de formula C del playbook -- pendiente retitular. Tiene storyboard v1.1 (15 paneles, 94s del piloto, escenas 1-2 de 12) y audio de 553.4s medido con ffprobe.

Correccion al brief: solo hay 2 guiones reales, no 4. Attention Span y Jealousy estan en fase de idea/titulo, no de guion. Si se quiere sostener la cadencia de 1 cada 4-5 dias, hace falta escribir esos 2 guiones ya -- es tarea de guion, no de este rol, pero lo marco como el cuello de botella oculto que el plan no tenia visible.

## 2. Resiliencia - el bloqueo de Recraft sigue activo, y hay algo mas que David debe saber

Confirmado en handoffs/REPORTE_2026-08-25_piloto_animado.md y REPORTE_2026-08-26_storyboard.md: el piloto (escenas 1-2, 94s) esta detenido antes de gastar nada, esperando la decision de David sobre los 5 USD de saldo de la API de Recraft. Sigue bloqueado hoy -- no es mi decision, solo lo reporto.

Dato adicional que el brief no tenia: ya existe un Resiliencia completo renderizado (youtube_pipeline/channels/mindset_mechanics/output/resilience_v2/resilience_final_v2.mp4, 23-ago) de una via de produccion ANTERIOR (2 sub-clips + frame congelado). David lo rechazo por verse "cuadriculado y estatico" (handoffs/HANDOFF_2026-08-25_decision_tercera_via_resiliencia.md), lo que forzo el pivot a la 3a via (Recraft + storyboard) que hoy esta parada. Es decir: Resiliencia no esta "casi listo esperando un pago" -- esta rehaciendose desde cero visualmente y el pago de Recraft solo destraba el piloto de 94s de 12 escenas totales.

Correccion importante: el bloqueo de los 5 USD de Recraft API no es exclusivo de Resiliencia -- es el pipeline visual valido para CUALQUIER video nuevo (incluido Social Anxiety). Existe una alternativa parcial ya mencionada en el reporte del 25-ago: 630 creditos disponibles en la via web de Recraft (ya pagados, sin depender del saldo de API), mas lenta y fragil pero utilizable si David autoriza usarla mientras se resuelve el pago de la API.

## 3. Siguiente paso concreto para el video que NO depende del bloqueo de Resiliencia

Social Anxiety es el candidato correcto: tiene guion completo y cero produccion visual empezada, asi que no arrastra el problema de calidad ya rechazado de Resiliencia.

Siguiente paso, en orden, y de quien:
1. storyboard-director -- construir el storyboard tecnico completo de Social Anxiety (escena por escena, planos, Video Action Prompts) ANTES de generar ninguna imagen. Costo: 0 creditos, es planeacion.
2. Decision de David (pendiente, ya escalada) -- aprobar los 5 USD de la API de Recraft, o autorizar usar los 630 creditos web ya pagados para generar las imagenes base de Social Anxiety mientras se resuelve el punto anterior. Sin esto, ni Social Anxiety ni el resto de Resiliencia se pueden producir visualmente, storyboard o no.
3. Solo despues de tener storyboard + imagenes: animacion en VideoExpress con la arquitectura de 3 sub-clips reales de 12-18s (misma regla que ya rige para Resiliencia, HANDOFF_2026-08-25_decision_tercera_via_resiliencia.md Decision 2), para no repetir el error "cuadriculado y estatico" que ya costo una ronda completa en Resiliencia.

## 4. Variantes de titulo A/B (Test & Compare) - listas para usar

Con las formulas ya validadas del playbook (seccion 1, Formula A = maxima evidencia del dataset -- 10/10 videos mas vistos de Human Condition son de esta familia).

### Social Anxiety (proximo video con mas probabilidad de estar listo primero)
- A: "Why Didn't Evolution Remove Social Anxiety?"
- B: "Why Didn't Evolution Kill Your Fear of Rejection?"
  (misma formula A, mismo objeto emocional, reangulado a "rejection" en vez de "social anxiety" -- evita el termino clinico directo en el titulo, prueba si el objeto mas visceral compite mejor por CTR; ninguna de las dos usa calificador que segmente audiencia, ninguna usa "disadvantage/flaw", regla dura del playbook respetada en ambas)

### Resiliencia / "Checks the Door Three Times" (cuando se destrabe la produccion)
- A (Formula C, la del plan original): "Psychology of People Who Check the Door Three Times"
- B (Formula A, reangulada al mismo contenido): "Why Didn't Evolution Remove the Urge to Double-Check Everything?"
  (A vende reconocimiento de identidad sin mencionar evolucion; B vende la misma conducta desde el angulo evolutivo explicito que ya tiene 10/10 mejores videos del dataset -- es el A/B correcto porque enfrenta las dos formulas de mayor evidencia entre si, no una formula fuerte contra una debil)

Nota: el archivo script_resilience_video.md hoy tiene el titulo de trabajo "Why Your Brain Breaks Under Pressure And How to Stop It" -- ese titulo NO sigue ninguna de las 6 formulas del playbook (no interrogativo, no objeto concreto, suena a self-help generico). Pendiente: retitular el archivo del guion a una de las 2 variantes de arriba antes de publicar, para que el hook del guion (que si sigue la plantilla de la Seccion 2 del playbook) cuadre con el titulo.

## 5. Tactica nueva de bajo costo, no probada aun - investigacion de hoy (agosto 2026)

YouTube Community Tab -- sin umbral de suscriptores desde 2026, con boost de distribucion medido.

Hallazgo: en 2026 YouTube elimino el requisito historico de 500 suscriptores para usar la pestana Community -- cualquier canal nuevo puede usarla desde el dia uno. Y hay un mecanismo de algoritmo documentado que el canal no esta usando: un post de Community con 50+ interacciones 24-48h antes de subir un video le da a ese video 5-15% mas alcance temprano en el feed de suscriptores, porque el algoritmo 2026 anadio la metrica "Return Viewer Velocity" que cuenta la interaccion con community posts como senal positiva de autoridad de canal (vidIQ, Gyre, YT SEO Architect, fluxnote.io -- 2026).

Con 7 suscriptores el alcance absoluto de un post de Community es minimo hoy, pero el mecanismo es gratis, toma minutos, y compone con la cadencia de publicacion que ya se va a ejecutar: cada uno de los 4 videos nuevos deberia llevar un post de Community (encuesta, imagen teaser, pregunta) 24-48h antes de publicarse, no el mismo dia.

Accion concreta: antes de publicar Social Anxiety (o el que salga primero), programar un post de Community 24-48h antes -- encuesta tipo "Alguna vez reescribiste un mensaje 4 veces antes de enviarlo?" conecta directo con el hook del guion ya escrito (linea 19 de script_social_anxiety_video.md). Costo: 0. Nadie lo ha probado todavia en este canal.

Tactica descartada por ahora (sin evidencia solida en la busqueda de hoy): promocion directa en subreddits de psicologia evolutiva/self-improvement -- no se encontro evidencia de comunidades activas especificas del nicho ni de tasas de conversion medidas; el riesgo de spam/ban en Reddit es real y el retorno no esta probado. No se prioriza esta semana.

---

## Fuentes citadas (hoy)
- vidIQ - YouTube Community Tab Posts: How to Use It in 2026: https://vidiq.com/blog/post/community-tab-youtube/
- Gyre - How the YouTube Community tab helps you grow your channel in 2026: https://gyre.pro/blog/how-can-the-youtube-community-tab-help-you-grow-in
- YT SEO Architect - YouTube Community Posts Strategy 2026: https://yt-seo-architect.vercel.app/blog/youtube-community-posts-strategy-2026
- fluxnote.io - YouTube Community Tab Strategy 2026: Boost Engagement: https://fluxnote.io/guides/youtube-community-tab-strategy-2026
- DataSlayer - YouTube Algorithm 2026: How to Get Your Videos Recommended: https://www.dataslayer.ai/blog/youtube-algorithm-2025-how-to-get-your-videos-recommended

## Archivos leidos (verificacion de estado)
- script_social_anxiety_video.md, script_resilience_video.md
- storyboards/STORYBOARD_resilience_v3_piloto_SC01-SC02.md, storyboards/storyboard_resilience_v3_piloto.json
- handoffs/REPORTE_2026-08-25_piloto_animado.md, handoffs/REPORTE_2026-08-26_storyboard.md
- handoffs/HANDOFF_2026-08-25_decision_tercera_via_resiliencia.md
- handoffs/INVESTIGACION_2026-08-25_categoria_y_captacion.md
- PROYECTO MECHANICS OPTIMIZACIONES/PLAYBOOK_MONETIZACION.md
- youtube_pipeline/channels/mindset_mechanics/output/resilience_v2/ (listado de archivos, sin ejecutar nada)
