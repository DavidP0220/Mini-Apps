# Pendientes — agenda de construccion e investigacion

> Documento vivo, mismo formato que el resto: se anade y se corrige, no se reescribe.
> Cada punto dice **que falta, por que importa y como se comprueba que quedo resuelto.**
> Ultima actualizacion: 2026-08-26.

---

## A. Lo primero, y es una sola cosa

### A-1. La primera generacion real. [GASTO — requiere OK del dueno: $5-$20]

**Que falta:** cargar saldo en fal.ai, crear una clave, pegarla en Ajustes, pasar a modo real y
generar un clip.

**Por que importa:** es el unico paso que convierte "la herramienta funciona en demo" en "la
herramienta funciona". Ademas responde de golpe las tres incognitas de la seccion 6 de
[`MEMORIA.md`](MEMORIA.md): si CORS deja pasar la llamada, si los IDs del catalogo son correctos, y
cuanto cuesta de verdad un clip.

**Como se comprueba:** hay un video descargado en la Biblioteca y un cargo visible en el panel de
fal.ai. Anotar el costo real y compararlo contra lo que estimo la app.

**Cuanto cargar:** **$5 basta** para 15-30 clips de prueba. El roadmap original decia $20; con la
arquitectura actual no hay que financiar ningun experimento de infraestructura, solo generar.

**Si CORS falla** (la llamada nunca sale y la app dice que revises el proxy): desplegar
[`proxy/worker.js`](proxy/worker.js) en Cloudflare Workers — plan gratis, ~10 minutos, las
instrucciones estan dentro del archivo — y pegar su URL en Ajustes → Proxy. No hay plan C necesario.

---

## B. Investigacion continua (esto es lo que se revisa periodicamente)

> Regla heredada del paquete original: **un dato con mas de 4-6 semanas se vuelve a verificar antes
> de usarlo para decidir algo.** Este mercado se movio 4x en 8 meses.

| # | Pregunta | Cada cuanto | Por que importa | Estado |
|---|---|---|---|---|
| B-1 | ¿Cambiaron los IDs o los precios de los modelos de fal.ai? | mensual | `modelos.json` se desactualiza solo; un ID muerto rompe una generacion | **abierta** — nunca verificado contra la API |
| B-2 | ¿Salio un modelo de video mejor o mas barato? | mensual | es literalmente cambiar una linea de JSON para adoptarlo | **abierta** |
| B-3 | ¿Suno o Udio abrieron API publica self-serve? | bimestral | es el unico hueco funcional grande: hoy no se puede generar musica | **abierta** — Suno abrio intake curado de partners el 1-jul-2026, no self-serve |
| B-4 | ¿ElevenLabs sigue costando $299/mes el plan Scale? ¿hay tier util mas barato? | trimestral | la voz es el siguiente hueco despues de la musica | **abierta** |
| B-5 | ¿Higgsfield cambio precios, o dejo de caducar los creditos? | trimestral | si dejan de caducar, la comparacion de la pantalla Gasto hay que corregirla | **abierta** |
| B-6 | ¿Aparecio un competidor de nicho en mindset/motivacion? | trimestral | solo importa si algun dia se vende | sin competidor directo al 2026-08-25 |
| B-7 | ¿fal.ai cambio sus ToS (secciones 4(b)(ii), 6(e)(xii), 17)? | trimestral | define exactamente cuando el proxy pasa de opcional a obligatorio | leidos al 2026-08-25, sin cambios detectados |
| B-8 | ¿Sigue siendo fal.ai el agregador mas barato? | trimestral | es un cambio de un solo archivo (`proveedor.js`) si deja de serlo | si al 2026-08-25 |

**Heredadas del paquete original y todavia abiertas:** leer los ToS de Kling y Google Veo con el
mismo detalle que se leyeron los de Runway/ElevenLabs/fal.ai; confirmar si Runway empuja a
Enterprise por limites operativos aunque el contrato estandar lo permita; confirmar directamente en
higgsfield.ai si existen los planes Team ($79) y Scale (~$169).

**Recordatorio de fecha dura:** la API de **Sora 2 cierra el 24-sep-2026**. Forja no la usa
(verificado: no aparece en `modelos.json` ni en el codigo), asi que no hay nada que hacer. Se anota
porque es el precedente que justifica toda la arquitectura anti-lock-in.

---

## C. Mejoras de la herramienta, por orden de valor

Ordenadas por **cuanto valor dan dividido entre lo que cuestan**, no por lo llamativas que suenan.

1. **Imagen → video en dos pasos, encadenado.** Hoy los dos modos existen por separado. Encadenarlos
   (generar 4 imagenes baratas con Flux, elegir una, animarla con Kling) es *el* flujo que abarata
   la produccion: fallas en imagenes de $0.025 en vez de en videos de $0.47. **Es la mejora de mayor
   impacto economico que queda por hacer.**
2. **Lotes.** Una idea, seis presets, una sola pasada. Es como se produce contenido de canal de
   verdad, y la cola ya lo soporta sin cambios.
3. **Costo real leido del proveedor**, no estimado, cuando fal lo reporte en la respuesta.
4. **Guiones a clips:** pegar un guion, partirlo en tomas, generar cada una. Es el puente entre esta
   herramienta y el pipeline de video que ya existe en los canales.
5. **Voz (ElevenLabs u otro), cuando haya un tier que no cueste $299/mes.**
6. **Musica**, cuando exista API publica (ver B-3). Mientras tanto: libreria de audio licenciado.
7. **Exportar a formato vertical con subtitulos**, para Shorts/Reels/TikTok.

**Deliberadamente fuera de alcance por ahora:** editor por capas, lipsync, avatares. Son meses de
trabajo y son exactamente donde Higgsfield tiene $400M de ventaja. Si algun dia hacen falta de
verdad, sale mas barato pagar un mes suelto de Higgsfield que construirlos.

---

## D. Si algun dia se vende (D-007 en pausa, no cancelado)

En orden. Ninguno de estos pasos obliga a tirar nada de lo construido.

1. **Desplegar el proxy y quitar el modo de clave en el navegador.** No es opcional ni cosmetico:
   sin esto se viola la seccion 4(b)(ii) de los ToS de fal.ai y se reparte el saldo propio. Ya escrito.
2. **Cuentas y aislamiento de datos.** Hoy no existen porque no hacen falta.
3. **Cobro** (Stripe) y modelo de precios — reactivar D-004 y D-005 tal como estan escritas.
4. **Textos legales.** El doc 04 es tajante: la indemnizacion frente a reclamos de usuarios finales
   recae en el proyecto, no en fal.ai. Antes de cobrarle a un tercero real: consulta legal puntual
   ($100-$300, una vez).
5. **Medir el costo real por usuario** antes de fijar el margen 3x de D-005.

**El orden importa:** 1 y 4 son requisitos legales, no mejoras. 2 y 3 son producto.

---

## E. Errores y lecciones de este tramo

> Mismo formato heredado: sintoma → causa → arreglo → como evitarlo.
> Se anade cada vez que algo salga mal. **Ninguna entrada se borra, aunque ya este arreglada.**

### E-1. El entorno de construccion no podia alcanzar al proveedor
**Sintoma:** al intentar leer la documentacion y probar la API de fal.ai desde el entorno donde se
construyo la herramienta, todo devolvia `EGRESS_BLOCKED`.
**Causa:** politica de red del entorno remoto; `fal.ai` no esta en su lista de destinos permitidos.
**Arreglo:** se verificaron los contratos de la API por fuentes secundarias accesibles (clientes
oficiales, referencias publicas) y se construyo el **modo demo**, que implementa el mismo contrato
sin red — lo que permitio probar de punta a punta la cola, la persistencia y la biblioteca sin
tocar el proveedor real.
**Como evitarlo:** cuando el entorno no pueda alcanzar una dependencia externa, no se declara
"probado" lo que no se probo. Se construye un doble que cumpla el mismo contrato, se prueba contra
el, y **se escribe explicitamente que falta la prueba real** — es lo que hace la seccion 6 de
`MEMORIA.md` y el punto A-1 de aqui.

### E-2. La carpeta nueva se verifico contra git antes de escribir dentro (leccion aplicada, no repetida)
**Contexto:** el error propio numero 1 del paquete original fue que toda la carpeta de investigacion
paso 24 h sin respaldo en git por un `.gitignore` de lista blanca, repitiendo un bug documentado el
dia anterior en otro modulo.
**Que se hizo distinto:** antes de escribir un solo archivo dentro de `forja/`, se corrio
`git check-ignore -v forja/app/index.html` para confirmar que no estaba ignorada. No lo estaba (el
`.gitignore` de este repositorio es lista negra normal, no lista blanca).
**Por que se anota igual habiendo salido bien:** porque la leccion del paquete original no era "el
`.gitignore` estaba mal", era **"una leccion documentada no sirve si nadie la consulta al crear
infraestructura nueva"**. Consultarla y anotar que se consulto es lo que cierra ese ciclo.
