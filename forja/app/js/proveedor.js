// proveedor.js — LA CAPA UNICA. Todo lo que sale a internet pasa por aqui.
//
// Esto ejecuta la decision D-003 (abstraccion anti-lock-in). Si manana fal.ai sube precios,
// cierra su API (precedente Sora 2) o hay que meter un backend propio para vender la herramienta,
// se cambia SOLO este archivo. El resto de la app no sabe que existe fal.ai.
//
// Contrato que cualquier proveedor debe cumplir:
//   enviar(modeloId, entrada)  -> { request_id, status_url, response_url, cancel_url }
//   estado(trabajo)            -> { status, queue_position?, logs? }
//   resultado(trabajo)         -> payload crudo del proveedor
//   cancelar(trabajo)          -> void
//   extraerMedios(payload)     -> [{ url, tipo, ancho?, alto? }]

import { ajustes } from './almacen.js';

const BASE_COLA = 'https://queue.fal.run';

// ---------------------------------------------------------------------------
// Errores tipados: la UI necesita distinguir "no reintentes" de "reintenta".
// ---------------------------------------------------------------------------
export class ErrorProveedor extends Error {
  constructor(mensaje, { codigo, reintentable = false, cuerpo = null } = {}) {
    super(mensaje);
    this.codigo = codigo;
    this.reintentable = reintentable;
    this.cuerpo = cuerpo;
  }
}

function esperar(ms) { return new Promise(r => setTimeout(r, ms)); }

// ---------------------------------------------------------------------------
// fetch con la politica de reintentos de 07_ERRORES_Y_LECCIONES (leccion 2):
//   - 429  -> reintentar con backoff exponencial honrando Retry-After.
//   - 5xx  -> NUNCA reintentar. El proveedor pudo haber ejecutado y cobrado la generacion;
//             reintentar la cobra dos veces. Se marca fallida y se avisa.
//   - 401/403 -> clave mala. No reintentar, decirlo claro.
// ---------------------------------------------------------------------------
async function pedir(url, opciones = {}, intento = 0) {
  const a = ajustes.todos();
  const cabeceras = { 'Content-Type': 'application/json', ...(opciones.headers || {}) };

  let destino = url;
  if (a.proxyUrl) {
    // Modo proxy: la clave vive en el servidor, no aqui. Mismo contrato que el proxy oficial de fal.
    cabeceras['x-fal-target-url'] = url;
    destino = a.proxyUrl;
  } else {
    if (!a.apiKey) throw new ErrorProveedor('No hay clave de fal.ai configurada. Ve a Ajustes.', { codigo: 'sin_clave' });
    cabeceras['Authorization'] = 'Key ' + a.apiKey;
  }

  let r;
  try {
    r = await fetch(destino, { ...opciones, headers: cabeceras });
  } catch (e) {
    // Fallo de red o CORS bloqueado. Es reintentable, pero hay que nombrarlo bien.
    throw new ErrorProveedor(
      'No se pudo contactar al proveedor. Si esto pasa siempre y la clave es correcta, ' +
      'tu navegador esta bloqueando la llamada (CORS): configura un proxy en Ajustes. Detalle: ' + e.message,
      { codigo: 'red', reintentable: true }
    );
  }

  if (r.status === 429) {
    if (intento >= 5) throw new ErrorProveedor('Limite de peticiones del proveedor (429) tras 5 reintentos.', { codigo: 'rate_limit', reintentable: true });
    const ra = parseInt(r.headers.get('Retry-After') || '', 10);
    const espera = Number.isFinite(ra) ? ra * 1000 : Math.min(30000, 1000 * Math.pow(2, intento));
    await esperar(espera);
    return pedir(url, opciones, intento + 1);
  }

  if (r.status === 401 || r.status === 403) {
    throw new ErrorProveedor('El proveedor rechazo la clave (' + r.status + '). Revisa la clave en Ajustes.', { codigo: 'auth' });
  }

  if (r.status >= 500) {
    // Deliberadamente NO se reintenta. Ver leccion 2 del registro de errores.
    throw new ErrorProveedor(
      'Error del proveedor (' + r.status + '). No se reintenta a proposito: la generacion pudo haberse ' +
      'ejecutado y cobrado del otro lado, y reintentar la cobraria dos veces. Revisa tu saldo antes de repetir.',
      { codigo: 'servidor' }
    );
  }

  if (!r.ok) {
    let cuerpo = null;
    try { cuerpo = await r.json(); } catch { try { cuerpo = await r.text(); } catch { /* nada */ } }
    const detalle = typeof cuerpo === 'string' ? cuerpo : JSON.stringify(cuerpo);
    throw new ErrorProveedor('El proveedor rechazo la peticion (' + r.status + '): ' + (detalle || '').slice(0, 400), { codigo: 'peticion', cuerpo });
  }

  if (r.status === 204) return null;
  return r.json();
}

// ---------------------------------------------------------------------------
// Proveedor real: fal.ai vía su API de cola.
// Clave del diseno: NO construimos las URLs de estado/resultado a mano. fal las devuelve
// en la respuesta de envio (status_url, response_url, cancel_url) y las guardamos tal cual.
// Asi los modelos con rutas anidadas (fal-ai/kling-video/v2/master/...) funcionan sin casos especiales.
// ---------------------------------------------------------------------------
const fal = {
  nombre: 'fal.ai',

  async enviar(modeloId, entrada) {
    const r = await pedir(BASE_COLA + '/' + modeloId, { method: 'POST', body: JSON.stringify(entrada) });
    if (!r || !r.request_id) throw new ErrorProveedor('El proveedor no devolvio request_id.', { codigo: 'respuesta_rara', cuerpo: r });
    return {
      request_id: r.request_id,
      status_url: r.status_url || (BASE_COLA + '/' + modeloId + '/requests/' + r.request_id + '/status'),
      response_url: r.response_url || (BASE_COLA + '/' + modeloId + '/requests/' + r.request_id),
      cancel_url: r.cancel_url || (BASE_COLA + '/' + modeloId + '/requests/' + r.request_id + '/cancel'),
      queue_position: r.queue_position
    };
  },

  estado: (t) => pedir(t.status_url + '?logs=1', { method: 'GET' }),
  resultado: (t) => pedir(t.response_url, { method: 'GET' }),
  cancelar: (t) => pedir(t.cancel_url, { method: 'PUT' })
};

// ---------------------------------------------------------------------------
// Proveedor demo: mismo contrato, cero red, cero costo. Sirve para dos cosas:
//   1. Probar toda la app (cola, persistencia, biblioteca) sin gastar un centavo ni tener clave.
//   2. Verificar que la cola sobrevive a cerrar la pestana, que es el riesgo D-006.
// ---------------------------------------------------------------------------
const DEMO_MS = 12000; // una "generacion" demo tarda 12s: suficiente para cerrar la pestana y volver

const demo = {
  nombre: 'demo',

  async enviar(modeloId, entrada) {
    const id = 'demo-' + Math.random().toString(36).slice(2, 10);
    const fin = Date.now() + DEMO_MS;
    localStorage.setItem('forja.demo.' + id, JSON.stringify({ fin, modeloId, entrada }));
    await esperar(250);
    return { request_id: id, status_url: 'demo:' + id, response_url: 'demo:' + id, cancel_url: 'demo:' + id, queue_position: 1 };
  },

  async estado(t) {
    const d = JSON.parse(localStorage.getItem('forja.demo.' + t.request_id) || 'null');
    if (!d) return { status: 'COMPLETED' };
    const restante = d.fin - Date.now();
    if (restante <= 0) return { status: 'COMPLETED' };
    if (restante > DEMO_MS * 0.6) return { status: 'IN_QUEUE', queue_position: 1 };
    return { status: 'IN_PROGRESS', logs: [{ message: 'renderizando... faltan ' + Math.ceil(restante / 1000) + 's' }] };
  },

  async resultado(t) {
    const d = JSON.parse(localStorage.getItem('forja.demo.' + t.request_id) || 'null');
    const prompt = (d && d.entrada && d.entrada.prompt) || 'demo';
    localStorage.removeItem('forja.demo.' + t.request_id);
    return { images: [{ url: svgDemo(prompt), content_type: 'image/svg+xml', width: 1024, height: 576 }] };
  },

  async cancelar(t) { localStorage.removeItem('forja.demo.' + t.request_id); }
};

function svgDemo(texto) {
  const limpio = String(texto).slice(0, 90).replace(/[<>&"]/g, ' ');
  const tono = Math.abs(hash(texto)) % 360;
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="576">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="hsl(${tono},65%,22%)"/><stop offset="1" stop-color="hsl(${(tono + 55) % 360},70%,48%)"/>
</linearGradient></defs>
<rect width="1024" height="576" fill="url(#g)"/>
<text x="512" y="270" font-family="system-ui,sans-serif" font-size="34" font-weight="700" fill="#fff" text-anchor="middle">MODO DEMO</text>
<text x="512" y="320" font-family="system-ui,sans-serif" font-size="19" fill="#ffffffcc" text-anchor="middle">${limpio}</text>
<text x="512" y="360" font-family="system-ui,sans-serif" font-size="14" fill="#ffffff88" text-anchor="middle">sin costo, sin red, sin clave</text>
</svg>`;
  return 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg);
}

function hash(s) { let h = 0; for (let i = 0; i < s.length; i++) h = (h * 31 + s.charCodeAt(i)) | 0; return h; }

// ---------------------------------------------------------------------------
// Selector y utilidades comunes
// ---------------------------------------------------------------------------
export function proveedorActivo() {
  return ajustes.get('modo') === 'fal' ? fal : demo;
}

// Los proveedores devuelven el medio en campos distintos segun el modelo.
// Normalizamos aqui para que la biblioteca no tenga que saberlo.
export function extraerMedios(payload) {
  if (!payload || typeof payload !== 'object') return [];
  const medios = [];
  const empujar = (o, tipo) => {
    if (!o) return;
    const url = typeof o === 'string' ? o : o.url;
    if (url) medios.push({ url, tipo: tipo || (o.content_type || '').split('/')[0] || 'imagen', ancho: o.width, alto: o.height });
  };
  if (payload.video) empujar(payload.video, 'video');
  if (Array.isArray(payload.videos)) payload.videos.forEach(v => empujar(v, 'video'));
  if (Array.isArray(payload.images)) payload.images.forEach(i => empujar(i, 'image'));
  if (payload.image) empujar(payload.image, 'image');
  if (payload.audio) empujar(payload.audio, 'audio');
  // Ultimo recurso: cualquier campo que parezca una URL de medio.
  if (!medios.length) {
    for (const v of Object.values(payload)) {
      if (typeof v === 'string' && /^https?:\/\/.+\.(mp4|webm|png|jpe?g|webp|mp3|wav)/i.test(v)) empujar(v);
    }
  }
  return medios;
}

export const _internos = { fal, demo, pedir };
