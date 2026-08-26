# Forja — estudio multimedia

Herramienta propia de generacion de video e imagen con IA. Corre entera en tu navegador,
no tiene suscripcion, y solo pagas la GPU que realmente consumes.

**Costo fijo mensual: $0.** Un clip de 5 segundos cuesta entre $0.25 y $0.50 segun el modelo.
Higgsfield, la referencia del sector, cobra $19-$129/mes con creditos que caducan cada ciclo.

---

## Empieza aqui (2 minutos, sin gastar nada)

```bash
node forja/servir.mjs
```

Abre <http://localhost:8123/>. **Arranca en modo demo**: todo funciona, nada sale a internet, nada
cuesta. Elige un preset, escribe una idea, aprieta Generar y mira como se comporta la cola.

> ¿Por que un servidor y no doble clic en `index.html`? Porque la app usa modulos de JavaScript, y
> los navegadores no los cargan desde `file://`. En GitHub Pages no hace falta nada de esto.

## Cuando quieras generar de verdad

1. Entra a **fal.ai**, crea la cuenta y carga saldo. **$5 alcanza para 15-30 clips de prueba.**
   Es prepago por uso, no una suscripcion.
2. Menu **API Keys** → crea una clave. **Se muestra una sola vez**: guardala en tu gestor de
   contrasenas antes de cerrar esa pantalla.
3. En Forja: **Ajustes** → pega la clave → cambia el modo a **fal.ai**.
4. La insignia de arriba a la izquierda pasa de gris a verde. A partir de ahi, cada generacion
   consume tu saldo.

La clave se guarda solo en este navegador. No entra al repositorio, no se sube a ningun lado, y el
respaldo que exporta la app la excluye a proposito.

> Si las generaciones fallan siempre con un error de red aunque la clave sea correcta, es tu
> navegador bloqueando la llamada (CORS). Se arregla desplegando `proxy/worker.js` en Cloudflare
> Workers (gratis, ~10 min, instrucciones dentro del archivo) y pegando su URL en Ajustes → Proxy.

---

## Las cinco pantallas

- **Generar** — preset + idea + camara. Ves el prompt final y **el costo en dolares antes de
  apretar el boton**.
- **Cola** — lo que se esta generando. **Puedes cerrar la pestana o apagar el equipo**: el trabajo
  corre en el servidor del proveedor y al volver se retoma solo.
- **Biblioteca** — todo lo generado, con copia local. Sigue siendo tuyo aunque canceles la cuenta.
- **Gasto** — dolares reales por dia, mes y total, desglosados por modelo, y la comparacion contra
  lo que costarian los planes de Higgsfield.
- **Ajustes** — clave, proxy, limite de gasto diario, respaldo, borrado.

## Personalizar sin tocar codigo

Dos archivos, y basta con recargar la pagina:

- **`app/presets.json`** — los presets y los movimientos de camara. Un preset es el prompt
  cinematografico ya escrito (luz, lente, color, grano); `{idea}` es donde entra lo que escribes tu.
  Anade los tuyos.
- **`app/modelos.json`** — los modelos y sus costos. Si fal saca uno nuevo manana, lo anades aqui
  (o lo pegas directo en la pantalla de Generar, en "Pegar otro modelo de fal.ai").

## Publicarla como app instalable

Es una PWA: `git push` a este repositorio con GitHub Pages activado y queda en
`https://<tu-usuario>.github.io/<repo>/forja/app/`, instalable desde el navegador en movil y
escritorio. Gratis.

> Si la publicas, **la clave sigue siendo tuya y sigue viviendo solo en tu navegador** — no viaja en
> el codigo. Pero si le pasas el enlace a otra persona, esa persona tendria que poner su propia
> clave, y ahi ya toca usar el proxy. Ver `PENDIENTES.md`, seccion D.

## Probar que todo sigue funcionando

```bash
npm install --no-save playwright   # una sola vez
node prueba-forja.mjs              # con el servidor corriendo
```

Verifica 30 cosas en un navegador real, incluida la que mas importa: **encola un trabajo, cierra la
pestana a mitad, la reabre y comprueba que sigue vivo y termina bien.**

---

## Los otros dos documentos

- **[`MEMORIA.md`](MEMORIA.md)** — de donde viene esto, que se investigo, que se decidio y por que,
  que hace mejor y peor que Higgsfield, y **que no esta verificado todavia**. Si vas a tocar algo,
  lee esto primero.
- **[`PENDIENTES.md`](PENDIENTES.md)** — que falta, que se revisa cada cuanto, y los pasos exactos
  si algun dia esto se vende.
- **[`fuente-original/`](fuente-original/)** — la investigacion completa de agosto 2026, intacta.
