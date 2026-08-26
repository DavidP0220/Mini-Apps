// Proxy opcional para fal.ai — Cloudflare Workers (plan gratis: 100.000 peticiones/dia).
//
// CUANDO HACE FALTA (no siempre):
//   1. Si tu navegador bloquea la llamada directa a fal.ai por CORS.
//   2. Si algun dia le das la herramienta a otra persona. Entonces es OBLIGATORIO:
//      los ToS de fal.ai (seccion 4(b)(ii)) prohiben exponer su API directamente a usuarios
//      finales, y ademas no querras repartir tu clave. Con este proxy la clave vive aqui,
//      en tu servidor, y nadie mas la ve.
//
// COMO SE USA:
//   1. Entra a dash.cloudflare.com -> Workers & Pages -> Create -> Worker.
//   2. Pega este archivo entero y despliega.
//   3. Settings -> Variables -> Add: FAL_KEY = tu clave de fal.ai (marcala como Secret).
//   4. Settings -> Variables -> Add: ORIGENES = https://tu-usuario.github.io
//   5. Copia la URL del worker y pegala en Forja -> Ajustes -> Proxy.

export default {
  async fetch(peticion, entorno) {
    const origen = peticion.headers.get('Origin') || '';
    const permitidos = (entorno.ORIGENES || '').split(',').map(s => s.trim()).filter(Boolean);
    const okOrigen = permitidos.length === 0 || permitidos.includes(origen);

    const cors = {
      'Access-Control-Allow-Origin': okOrigen ? (origen || '*') : 'null',
      'Access-Control-Allow-Methods': 'GET,POST,PUT,OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type,x-fal-target-url',
      'Access-Control-Max-Age': '86400'
    };

    if (peticion.method === 'OPTIONS') return new Response(null, { status: 204, headers: cors });
    if (!okOrigen) return new Response('Origen no permitido', { status: 403, headers: cors });

    const destino = peticion.headers.get('x-fal-target-url');
    if (!destino) return new Response('Falta la cabecera x-fal-target-url', { status: 400, headers: cors });

    // Solo se deja pasar a fal. Sin esto, cualquiera podria usar tu worker como proxy abierto.
    let url;
    try { url = new URL(destino); } catch { return new Response('URL invalida', { status: 400, headers: cors }); }
    if (!/(^|\.)fal\.run$|(^|\.)fal\.ai$/.test(url.hostname)) {
      return new Response('Destino no permitido', { status: 403, headers: cors });
    }

    const cabeceras = new Headers();
    cabeceras.set('Authorization', 'Key ' + entorno.FAL_KEY);
    if (peticion.headers.get('Content-Type')) cabeceras.set('Content-Type', peticion.headers.get('Content-Type'));

    const arriba = await fetch(url.toString(), {
      method: peticion.method,
      headers: cabeceras,
      body: ['GET', 'HEAD'].includes(peticion.method) ? undefined : await peticion.text()
    });

    const respuesta = new Response(arriba.body, { status: arriba.status, headers: arriba.headers });
    for (const [k, v] of Object.entries(cors)) respuesta.headers.set(k, v);
    // Retry-After tiene que sobrevivir: la app lo usa para respetar los 429.
    if (arriba.headers.get('Retry-After')) respuesta.headers.set('Retry-After', arriba.headers.get('Retry-After'));
    return respuesta;
  }
};
