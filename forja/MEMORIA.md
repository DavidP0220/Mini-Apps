# Forja — memoria del proyecto

> **Regla de oro heredada del paquete original: si no esta escrito aqui, no existe.**
> Este documento se actualiza, nunca se reescribe. Ninguna entrada vieja se borra: si algo cambia,
> se anade una entrada nueva que explica el cambio y por que.
>
> **Ultima actualizacion: 2026-08-26.**
> **Dinero real gastado hasta hoy: $0.00.**
> **Estado: herramienta construida y probada en modo demo. Pendiente la primera generacion real.**

---

## 1. Que es esto y de donde viene

En agosto de 2026 se hizo una investigacion completa (informe PDF + 3 agentes + 3 validadores)
sobre construir una alternativa propia a **Higgsfield.ai**, la empresa dominante de IA generativa
de video/imagen ($5.400M de valoracion, $700M de ingresos anuales, 30M de usuarios, Serie B de
$400M cerrada el 17-ago-2026). Esa investigacion produjo 7 documentos, 6 decisiones (D-001 a D-006)
y un roadmap de 8 semanas. **No produjo ni una linea de codigo.**

El paquete completo de esa investigacion esta intacto en [`fuente-original/`](fuente-original/) —
nada se perdio, nada se resumio sin dejar el original. Este documento es la sintesis operativa.

**El 2026-08-26 el proyecto cambio de forma por una decision del dueno**, y ese cambio es el eje
de todo lo que sigue: *"primeramente solo la usare yo para mis proyectos y mayor economia".*

Eso convierte el proyecto de **"un SaaS que hay que validar y vender"** en **"una herramienta
personal que tiene que costar lo menos posible"**. No es un recorte del plan: es un plan distinto,
mas barato y sin riesgo, y deja la puerta abierta a vender despues sin rehacer nada.

---

## 2. Lo que ya sabiamos (sintesis de la investigacion, sin perder nada)

### 2.1 El competidor — por que no se le compite de frente

Higgsfield (fundada 2023 por Alex Mashrabov, ex-jefe de IA Generativa de Snap, y Yerzat Dulat)
orquesta multiples modelos (Veo, Kling, Seedance, Wan, mas su modelo propio **DoP** con 50+ presets
de camara), y ha crecido hacia **workspace de produccion**: EditLayers, lipsync, avatares,
Cinema Studio, Marketing Studio, Higgsfield Assist, Soul ID, plugins de Blender y After Effects,
academia, Discord de 183.000 miembros, festival con premio de $1M.

**Precios (verificado ago-2026):** Starter $19/mes (270 creditos), Plus $59/mes (1.200),
Ultra $129/mes (3.000), Enterprise a medida. Menciones no confirmadas de Team $79 y Scale ~$169.

**La grieta concreta:** *los creditos no usados expiran al fin del ciclo de facturacion*, lo que
"efectivamente duplica el costo real" para quien no consume todo. Es la queja mas repetida del
mercado y la mas barata de resolver — Forja no tiene creditos en absoluto.

**Lectura estrategica que sigue vigente:** Higgsfield se mueve *hacia arriba* (equipos, agencias,
productoras), no hacia abajo. El creador individual con presupuesto bajo queda mas desatendido, no
menos. Y no hay ningun competidor de nivel Higgsfield en el nicho mindset/motivacion — solo
herramientas genericas de entrada (InVideo, Reelsta, Mootion, Bigmotion, ReelsMakerAI, Hooked).

### 2.2 Los motores — que hay disponible via API

**Agregador elegido: fal.ai.** Cobra por segundo de GPU sin margen anadido, 30-50% mas barato que
Replicate, y con **una sola clave** cubre Kling, MiniMax/Hailuo, Flux, Wan, Veo y Seedream. Rango
real $0.02-$0.40 por output.

Descartados y por que: **Replicate** (cobra margen encima), **Midjourney** (sin API oficial en 2026,
riesgo de baneo via terceros), **Runway directo** (legalmente viable con plan API estandar, pero
obliga a mostrar "Powered by Runway" con enlace — regalarle la marca al competidor),
**Suno/Udio** (sin API publica self-serve; Suno abrio intake curado de partners el 1-jul-2026).

**Prohibido — no es opinion, es requisito:** **Sora 2 / OpenAI.** La app cerro el 26-abr-2026 y la
API cierra el **24-sep-2026**, sin sucesor ni migracion oficial. Quien la tenia cableada directo se
quedo roto. Ese precedente es la razon de ser de la capa de abstraccion (ver 4.3).

### 2.3 Lo legal — que cambia y que no con el uso personal

Del analisis linea por linea de los ToS (2026-08-25):

- **fal.ai** prohibe "exponer las APIs directamente a end users" (seccion 4(b)(ii)) y revender o
  sublicenciar los derechos de la cuenta (6(e)(xii)). Ademas **la indemnizacion va al reves de lo
  que uno esperaria**: el cliente debe defender a fal.ai ante reclamos de terceros derivados de su
  "Customer Solution" (seccion 17).
- **ElevenLabs:** revender el servicio requiere ser "Authorized Reseller" con permiso escrito;
  integrar sus voces en un producto propio y cobrar por ese producto, si esta permitido.
- **Runway:** el contrato de API estandar SI permite integrar su funcionalidad en un producto propio
  y exponerla a usuarios finales. Lo unico obligatorio es la atribucion visible.

**En uso personal, casi todo esto deja de aplicar hoy:** no hay end users, no hay reventa, no hay
terceros que puedan reclamar. Es tu clave, tu cuenta, tu saldo, tu contenido.
**Vuelve a aplicar entero el dia que otra persona use la herramienta** — y ese dia el requisito
tecnico concreto es el proxy (ya escrito, ver 4.4), no un abogado primero.

### 2.4 Las lecciones tecnicas heredadas (todas implementadas, ver 4.5)

Del pipeline de produccion existente de Mindset Mechanics:

1. **Rutas relativas + `.gitignore` de lista blanca = perdida silenciosa de datos.** Paso de verdad:
   toda la carpeta de investigacion estuvo 24 h sin respaldo en git por este bug, repitiendo un
   error documentado el dia anterior en otro modulo.
2. **429 sin manejo = generacion perdida o cobrada dos veces.** Backoff exponencial honrando
   `Retry-After`; **nunca reintentar un 5xx** (pudo ejecutarse y cobrarse del otro lado).
3. **Telemetria acoplada a llamadas de red opcionales** = se pierde el registro de algo ya pagado.
4. **Configuracion clavada a una sola maquina** (rutas de ejecutables hardcodeadas).

---

## 3. Decisiones nuevas (2026-08-26)

> Formato heredado. Las decisiones D-001 a D-006 viven completas en
> [`fuente-original/investigacion/06_DECISIONES_PRODUCTO.md`](fuente-original/investigacion/06_DECISIONES_PRODUCTO.md)
> y no se borran: abajo se dice explicitamente cual sigue viva y cual queda en pausa.

### D-007 — Uso personal primero. Todo lo de vender se aplaza, no se cancela.

**Decision:** la herramienta se construye para un solo usuario (su dueno) usando su propia cuenta
de fal.ai. Se aplazan Stripe, los paquetes de creditos, los textos legales, la consulta con abogado,
el dominio y la prueba cerrada con 10-30 personas.

**Razon:** lo pidio el dueno de forma explicita, y ademas es la decision correcta por economia. El
Nivel 1 del roadmap original costaba **$90-$230/mes** en regimen. En uso personal el costo fijo es
**$0/mes** y solo se paga la GPU efectivamente consumida. Todo el riesgo legal del doc 04 (que era
el documento que "mas puede frenar el proyecto") nace de cobrarle a un tercero: sin tercero, no hay
riesgo que gestionar hoy.

**Alternativas descartadas:** seguir el roadmap de 8 semanas hacia la venta — descartado porque
gasta dinero y semanas validando un negocio que el dueno todavia no quiere montar, cuando la
necesidad real e inmediata es tener la herramienta funcionando para sus propios canales.

**Reversible:** si, y ese es el punto. Lo que se aplaza esta enumerado y ordenado en
[`PENDIENTES.md`](PENDIENTES.md), seccion "Si algun dia se vende". Nada de lo construido hay que
tirarlo para vender: hay que anadir proxy (ya escrito), cuentas y cobro.

### D-008 — Se descarta Lovable.dev. Se construye directo, sin plataforma. (Revierte D-002.)

**Decision:** no se usa Lovable.dev ni Bubble ni Base44. La herramienta se escribe en HTML, CSS y
JavaScript puro, sin dependencias y sin paso de compilacion, dentro de este mismo repositorio.

**Razon:** D-002 eligio Lovable ($25/mes) porque el dueno no programa y porque genera codigo React
real sincronizado a GitHub, evitando el lock-in de Bubble. Pero el argumento decisivo era *"si esto
falla, con Lovable nos llevamos el codigo"* — o sea, el valor era el codigo, no la plataforma. Este
repositorio ya demuestra que la base HTML/CSS/JS puro funciona, se instala como app (PWA) y se
publica gratis en GitHub Pages. Pagar $25/mes por que una IA escriba el codigo que ya esta escrito,
con la complejidad extra de Supabase, Edge Functions y webhooks, no compra nada aqui.

**Lo que ahorra:** $25/mes de Lovable + $15-$30/mes de hosting = **$40-$55/mes**, mas las semanas
2-4 del cronograma original.

**Alternativas descartadas:** Bubble (curva de 3-6 semanas, mas caro, sin exportar codigo),
Base44/Wix (lock-in), white-label (~$500/mes de retainer y "no es tuyo").

**Reversible:** si, sin costo. Nada impide abrir una cuenta de Lovable manana; el codigo actual no
depende de nada externo.

### D-009 — Arquitectura local-first. Resuelve D-006 por construccion, sin backend.

**Decision:** no hay servidor. La app corre entera en el navegador. Cada generacion se envia a la
**API de cola de fal.ai**, que devuelve un `request_id` y unas URLs de estado; esas URLs se guardan
en **IndexedDB antes de que nada pueda fallar**. Al reabrir la app, `reanudar()` retoma el sondeo de
todo lo que quedo a medias.

**Razon:** D-006 declaraba que el riesgo tecnico numero uno — el unico que la investigacion dejo
explicitamente sin resolver — era si Lovable/Supabase aguantaba colas de IA de varios minutos, y
reservaba $20 y 5 dias habiles para averiguarlo con un prototipo desechable. **Ese riesgo desaparece
con esta arquitectura en vez de resolverse.** El trabajo pesado no corre en nuestra maquina ni en
nuestro backend: corre en el servidor de fal.ai. Cerrar la pestana no lo cancela, porque nunca
dependio de la pestana. No hay timeout de Edge Function que exceder porque no hay Edge Function.

**Verificado, no supuesto:** la prueba automatizada de este repositorio encola un trabajo,
**cierra la pestana a mitad**, la reabre y confirma que el trabajo sigue vivo y termina bien.
Se ejecuta con `node prueba-forja.mjs` y hoy pasa entera. Esa es la version ejecutable del semaforo
verde/rojo que pedia la Fase 2 del roadmap.

**Reversible:** si. Si algun dia hace falta un backend (para vender), el proxy ya escrito es el
primer paso y la app no cambia.

### D-010 — La clave de fal.ai vive en el navegador del dueno. El proxy es obligatorio el dia que la use otra persona.

**Decision:** en uso personal la clave se guarda en `localStorage` del navegador del dueno, la
introduce el a mano, y nunca entra al repositorio. El dia que otra persona use la herramienta, se
pasa al modo proxy (Ajustes → Proxy), con la clave viviendo en un Cloudflare Worker.

**Razon:** la documentacion de fal dice que sus endpoints "estan disenados para llamarse
directamente desde el cliente", y advierte contra **guardar la clave en el codigo fuente del
cliente** — que es un problema distinto y que aqui no ocurre: la clave no esta en el codigo, la
escribe el dueno en su propio equipo, igual que cualquier app de escritorio guarda su configuracion.
Con un solo usuario que es el titular de la cuenta, no hay a quien exponerle nada.

**El limite exacto, para que no se cruce por accidente:** en cuanto haya un segundo usuario, esto
viola la seccion 4(b)(ii) de los ToS de fal.ai *y* reparte tu saldo. Por eso el proxy no es una
mejora futura: esta escrito y probado en [`proxy/worker.js`](proxy/worker.js), con lista blanca de
origenes y de destino, listo para pegar.

**Reversible:** si, es un campo en Ajustes.

### D-011 — Sin creditos, sin margen, sin fichas. Dolares a la vista. (D-005 queda en pausa.)

**Decision:** la app no inventa una moneda propia. Muestra el **costo estimado en USD antes de
apretar el boton**, lleva la cuenta de lo gastado hoy/mes/total, y avisa al superar un limite diario
que fija el dueno.

**Razon:** D-005 diseno paquetes de creditos prepagados con margen 3x — eso es un **modelo de
venta**, y sin venta no tiene sentido cobrarse margen a uno mismo. Lo que si se conserva es el
*diagnostico* que produjo D-005: los creditos que expiran son la queja concreta del mercado. Aqui el
problema simplemente no existe: el saldo prepago de fal.ai no caduca y no hay conversion opaca de
dolares a fichas.

**D-005 no se borra: queda en pausa** y vuelve tal cual si algun dia se vende.

### Que sigue vigente sin cambios de las decisiones viejas

- **D-001 (nicho mindset/motivacion):** vigente, pero degradado de *posicionamiento de marca* a
  *contenido de la herramienta*. Los 6 presets que D-001 pedia estan implementados literalmente
  ("Amanecer/disciplina", "Gimnasio 4am", "Ciudad de noche/soledad", "Naturaleza/calma",
  "Exito/oficina", "Superacion/lluvia") y se anadieron 6 mas para el canal Human Chronicles
  (historia) y para miniaturas.
- **D-003 (fal.ai + capa de abstraccion obligatoria):** vigente y **cumplida al pie de la letra**.
  Todo lo que sale a internet pasa por [`app/js/proveedor.js`](app/js/proveedor.js) y por nada mas.
- **D-004 (Stripe):** en pausa junto con D-007.
- **D-006 (probar las colas antes que nada):** cumplida por una via distinta a la prevista — ver D-009.

---

## 4. Como esta construido

### 4.1 Estructura

```
forja/
  app/                    la herramienta (HTML/CSS/JS puro, PWA, sin dependencias, sin build)
    index.html            5 pantallas: Generar, Cola, Biblioteca, Gasto, Ajustes
    styles.css
    modelos.json          catalogo de modelos y costos  <- editable sin tocar codigo
    presets.json          presets y movimientos de camara <- editable sin tocar codigo
    js/
      proveedor.js        LA CAPA UNICA. Lo unico que sabe que fal.ai existe.
      cola.js             motor de cola persistente (sobrevive a cerrar la pestana)
      almacen.js          IndexedDB (trabajos + copias de medios) y ajustes
      catalogo.js         carga de catalogos, composicion de prompts, estimacion de costo
      app.js              interfaz
    sw.js, manifest.json, icons/      instalable como app
  proxy/worker.js         proxy opcional de Cloudflare (obligatorio si la usa otra persona)
  servir.mjs              servidor local sin dependencias: node forja/servir.mjs
  fuente-original/        el paquete de investigacion completo, intacto
  MEMORIA.md              este archivo
  PENDIENTES.md           lo que falta: agenda de investigacion y de construccion
```

Y en la raiz del repositorio: `prueba-forja.mjs`, la prueba automatizada de navegador.

### 4.2 El flujo, en una frase

Eliges un preset (que ya trae escrita la direccion de fotografia), escribes tu idea en una linea,
eliges el movimiento de camara, ves **el prompt final y el costo en dolares antes de decidir**, y
generas. El trabajo se va a la cola de fal.ai y puedes cerrar todo; cuando vuelvas, estara ahi.

### 4.3 La capa unica (D-003, la poliza de seguro contra un cierre tipo Sora 2)

`app/js/proveedor.js` es el unico archivo que menciona fal.ai. Define un contrato de cinco funciones
(`enviar`, `estado`, `resultado`, `cancelar`, `extraerMedios`) e implementa dos proveedores contra
el: el real y el de demo. Cambiar de proveedor, o meter un backend propio para vender, es cambiar
**ese archivo y nada mas**.

Detalle de diseno que importa: las URLs de estado y resultado **no se construyen a mano**, se toman
de lo que devuelve fal al enviar (`status_url`, `response_url`, `cancel_url`). Asi los modelos con
rutas anidadas (`fal-ai/kling-video/v2/master/text-to-video`) funcionan sin casos especiales, y si
fal cambia su esquema de rutas, no se rompe nada.

### 4.4 Modo demo — probar sin gastar

Arranca en modo demo: mismo flujo completo, cero red, cero costo, cero clave. Sirve para aprender la
herramienta, para probar cambios en los presets, y es lo que hace posible que la prueba automatizada
verifique la cola sin quemar saldo. Pasar a real es un radio en Ajustes, y la insignia de la barra
superior cambia de color para que nunca haya duda de si algo cuesta dinero.

### 4.5 Las lecciones heredadas, implementadas (no anotadas)

| Leccion del doc 07 | Donde vive en el codigo |
|---|---|
| Nunca reintentar un 5xx (cobra dos veces) | `proveedor.js` — se lanza error explicito con esa razon escrita |
| 429 con backoff honrando `Retry-After` | `proveedor.js` — hasta 5 reintentos |
| El registro nunca depende de una llamada opcional | `cola.js` — la fila se escribe **antes** de la red; archivar el medio va despues y es best-effort |
| Envio interrumpido sin confirmar | `cola.js` `reanudar()` — se marca para revision manual, **no se reenvia solo**, por la misma razon que no se reintenta un 5xx |
| Carpeta nueva ignorada por git | verificado con `git check-ignore` al crear `forja/`, antes de escribir nada dentro |

Ademas, dos protecciones nuevas propias de manejar dinero: el **freno de gasto diario** (avisa antes
de pasarse del limite) y el **respaldo que excluye la clave a proposito** al exportar.

---

## 5. Que hace mejor que Higgsfield (y que no)

**Mejor, para uso personal:**

| | Higgsfield | Forja |
|---|---|---|
| Costo fijo | $19-$129/mes | **$0** |
| Creditos sin usar | **caducan al fin del ciclo** | no hay creditos; el saldo de fal.ai no caduca |
| Costo por generacion | oculto tras fichas | **en dolares, antes de apretar el boton** |
| Tu biblioteca | en su servidor | copia local en tu equipo, tuya aunque cierres la cuenta |
| Modelos | los que ellos decidan | los que quieras; pegas el ID y listo |
| Presets | cerrados | un archivo JSON que editas tu |
| Si el proveedor cierra | te quedaste sin producto | se cambia un archivo |
| Probar sin gastar | no | modo demo completo |

**Peor, y hay que decirlo:** no tiene editor por capas (EditLayers), ni lipsync, ni avatares, ni
modelo propio de camara entrenado (DoP), ni comunidad, ni academia, ni apps moviles, ni soporte. No
genera musica (ningun proveedor tiene API publica self-serve). Higgsfield tiene $400M para construir
todo eso y aqui hay una persona. **La comparacion honesta no es "Forja vs. Higgsfield" sino "Forja
vs. pagar $19-$129/mes por funciones que quiza no uses".** Para generar clips y miniaturas para dos
canales propios, Forja gana por costo. Para produccion cinematografica en equipo, no.

---

## 6. Limitaciones conocidas hoy — lo que NO esta verificado

Esto es deliberadamente explicito. La habilidad #3 del paquete original ("verificar la fuente
primaria en vez de confiar en el resumen") exige decir donde no se pudo verificar.

1. **No se ha hecho ni una sola generacion real.** Todo lo probado es en modo demo. El entorno donde
   se construyo esto tiene `fal.ai` bloqueado por politica de red, asi que **fue imposible probar
   contra la API real desde aqui**. La primera generacion real es la prueba pendiente numero uno.
2. **CORS desde el navegador no esta confirmado empiricamente.** La documentacion de fal dice que
   sus endpoints estan disenados para llamarse desde el cliente, pero no se pudo comprobar. Si falla,
   no es un bloqueo: el proxy de `proxy/worker.js` lo resuelve y la app ya tiene el campo para
   apuntarlo.
3. **Los IDs de modelo y los precios de `modelos.json` son de referencia (ago-2026), no leidos de la
   API.** fal cambia su catalogo seguido. Por eso son un JSON editable y por eso la app acepta que
   pegues cualquier ID a mano. Si un ID no existe, fal responde con un error claro y la app lo muestra.
4. **El gasto que muestra la app es la suma de estimaciones, no de cobros reales.** El numero de
   verdad esta siempre en el panel de fal.ai. La app lo dice en pantalla.
5. **La copia local de los medios depende de que el CDN del proveedor permita descargarlos desde el
   navegador.** Si no lo permite, el enlace directo sigue funcionando y la app marca el medio como
   "solo enlace" en vez de fingir que lo archivo.

---

## 7. Registro de gasto real

| Fecha | Concepto | Importe | Aprobado |
|---|---|---|---|
| — | *(sin gastos al 2026-08-26)* | $0.00 | — |

**La regla de gasto del proyecto original sigue en pie y no es negociable:** nada activa una
suscripcion, mete una tarjeta ni consume saldo sin aprobacion explicita del dueno. La unica
diferencia es que ahora el software tambien la aplica solo: arranca en demo, y el modo real exige
poner la clave a mano y pasar un radio.
