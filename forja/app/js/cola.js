// cola.js — motor de cola persistente.
//
// Esto resuelve por construccion el riesgo que la investigacion dejo abierto (D-006 / doc 03):
// "que una generacion de varios minutos sobreviva a cerrar la pestana".
// No hace falta backend, ni Edge Functions, ni webhooks: fal.ai devuelve un request_id y unas URLs
// de estado. Las guardamos en IndexedDB ANTES de que nada pueda fallar. Al reabrir la app,
// reanudar() retoma el sondeo de todo lo que quedo a medias. Cerrar la pestana no pierde nada
// porque el trabajo vive en el servidor del proveedor, no en la memoria de la pagina.

import { almacen } from './almacen.js';
import { proveedorActivo, extraerMedios, ErrorProveedor } from './proveedor.js';

const ESTADOS_VIVOS = ['creando', 'en_cola', 'procesando'];
const TOPE_ARCHIVO = 60 * 1024 * 1024; // 60 MB por medio: por encima solo guardamos la URL

const oyentes = new Set();
const temporizadores = new Map();

export function alCambiar(fn) { oyentes.add(fn); return () => oyentes.delete(fn); }
function avisar(trabajo) { for (const fn of oyentes) { try { fn(trabajo); } catch (e) { console.error(e); } } }

function nuevoId() {
  return Date.now().toString(36) + '-' + Math.random().toString(36).slice(2, 8);
}

// Backoff de sondeo: rapido al principio, tranquilo despues. Un video tarda minutos;
// preguntar cada segundo durante 5 minutos es maltratar la API sin ganar nada.
function proximoIntervalo(n) {
  const escala = [2000, 3000, 5000, 8000, 10000, 15000];
  return escala[Math.min(n, escala.length - 1)];
}

/**
 * Encola una generacion.
 * El orden importa: primero se escribe la fila, despues se llama a la red.
 * Si la llamada falla o el navegador se cierra a mitad, el trabajo queda registrado igual.
 */
export async function encolar({ modelo, entrada, costoEstimado = 0, etiqueta = '', preset = null, tipo = 'video' }) {
  const trabajo = {
    id: nuevoId(),
    modelo, entrada, tipo, preset, etiqueta,
    costoEstimado,
    proveedor: proveedorActivo().nombre,
    estado: 'creando',
    creado: Date.now(),
    actualizado: Date.now(),
    intentos: 0,
    medios: [],
    error: null
  };
  await almacen.guardarTrabajo(trabajo);
  avisar(trabajo);

  try {
    const r = await proveedorActivo().enviar(modelo, entrada);
    trabajo.request_id = r.request_id;
    trabajo.status_url = r.status_url;
    trabajo.response_url = r.response_url;
    trabajo.cancel_url = r.cancel_url;
    trabajo.estado = 'en_cola';
    trabajo.posicion = r.queue_position;
  } catch (e) {
    trabajo.estado = 'fallido';
    trabajo.error = e.message;
    trabajo.codigoError = e.codigo || null;
  }
  trabajo.actualizado = Date.now();
  await almacen.guardarTrabajo(trabajo);
  avisar(trabajo);

  if (trabajo.estado === 'en_cola') programar(trabajo.id, 0);
  return trabajo;
}

function programar(id, n) {
  cancelarTemporizador(id);
  temporizadores.set(id, setTimeout(() => sondear(id, n), proximoIntervalo(n)));
}

function cancelarTemporizador(id) {
  const t = temporizadores.get(id);
  if (t) { clearTimeout(t); temporizadores.delete(id); }
}

async function sondear(id, n) {
  const trabajo = await almacen.obtenerTrabajo(id);
  if (!trabajo || !ESTADOS_VIVOS.includes(trabajo.estado)) { cancelarTemporizador(id); return; }

  try {
    const e = await proveedorActivo().estado(trabajo);
    const s = (e && e.status) || '';

    if (s === 'COMPLETED') {
      await recoger(trabajo);
      return;
    }
    trabajo.estado = s === 'IN_PROGRESS' ? 'procesando' : 'en_cola';
    trabajo.posicion = e.queue_position;
    trabajo.registro = (e.logs || []).map(l => l.message).filter(Boolean).slice(-3);
    trabajo.actualizado = Date.now();
    await almacen.guardarTrabajo(trabajo);
    avisar(trabajo);
    programar(id, n + 1);
  } catch (err) {
    if (err instanceof ErrorProveedor && err.reintentable && n < 20) {
      // Red caida o rate limit: seguimos sondeando, el trabajo sigue vivo del otro lado.
      programar(id, n + 1);
      return;
    }
    trabajo.estado = 'fallido';
    trabajo.error = err.message;
    trabajo.codigoError = err.codigo || null;
    trabajo.actualizado = Date.now();
    await almacen.guardarTrabajo(trabajo);
    avisar(trabajo);
    cancelarTemporizador(id);
  }
}

async function recoger(trabajo) {
  cancelarTemporizador(trabajo.id);
  try {
    const payload = await proveedorActivo().resultado(trabajo);
    trabajo.payload = payload;
    trabajo.medios = extraerMedios(payload);
    trabajo.estado = trabajo.medios.length ? 'listo' : 'fallido';
    if (!trabajo.medios.length) trabajo.error = 'El proveedor termino pero no devolvio ningun medio reconocible.';
    // El costo real, si el proveedor lo reporta. Si no, se queda el estimado.
    if (payload && payload.metrics && typeof payload.metrics.inference_time === 'number') {
      trabajo.tiempoInferencia = payload.metrics.inference_time;
    }
  } catch (err) {
    trabajo.estado = 'fallido';
    trabajo.error = err.message;
    trabajo.codigoError = err.codigo || null;
  }
  trabajo.actualizado = Date.now();
  await almacen.guardarTrabajo(trabajo);
  avisar(trabajo);

  // Archivar es best-effort y va DESPUES de guardar. Si falla la descarga del blob,
  // el trabajo ya esta registrado como listo y la URL sigue ahi. (Leccion 3 del doc 07.)
  if (trabajo.estado === 'listo') archivar(trabajo).catch(e => console.warn('archivo omitido:', e.message));
}

/**
 * Guarda una copia local del medio. Esta es una ventaja real sobre las plataformas de pago:
 * las URLs del CDN del proveedor caducan y su biblioteca vive en su servidor. Aqui lo generado
 * es tuyo y sigue existiendo aunque canceles la cuenta o el proveedor cierre.
 */
async function archivar(trabajo) {
  const { ajustes } = await import('./almacen.js');
  if (!ajustes.get('archivarMedios')) return;

  let cambio = false;
  for (let i = 0; i < trabajo.medios.length; i++) {
    const m = trabajo.medios[i];
    if (m.archivado || m.url.startsWith('data:')) continue;
    try {
      const r = await fetch(m.url);
      if (!r.ok) continue;
      const blob = await r.blob();
      if (blob.size > TOPE_ARCHIVO) { m.demasiadoGrande = true; cambio = true; continue; }
      const idMedio = trabajo.id + '-' + i;
      await almacen.guardarMedio(idMedio, blob, blob.type);
      m.archivado = idMedio;
      m.bytes = blob.size;
      cambio = true;
    } catch { /* CORS del CDN o red: nos quedamos con la URL, no es fatal */ }
  }
  if (cambio) {
    trabajo.actualizado = Date.now();
    await almacen.guardarTrabajo(trabajo);
    avisar(trabajo);
  }
}

/** Retoma todo lo que quedo a medias. Se llama al arrancar la app. */
export async function reanudar() {
  const todos = await almacen.listarTrabajos();
  const vivos = todos.filter(t => ESTADOS_VIVOS.includes(t.estado));
  for (const t of vivos) {
    if (t.estado === 'creando' && !t.request_id) {
      // Se cerro la pestana entre escribir la fila y recibir el request_id.
      // No sabemos si el proveedor lo acepto: lo marcamos para revision en vez de reenviar
      // (reenviar a ciegas es como reintentar un 5xx — puede cobrar dos veces).
      t.estado = 'fallido';
      t.error = 'Se interrumpio el envio antes de confirmar. No se reenvia solo para no arriesgar un cobro doble. Revisa tu panel del proveedor y vuelve a lanzarlo si no aparece.';
      await almacen.guardarTrabajo(t);
      avisar(t);
      continue;
    }
    programar(t.id, 0);
  }
  return vivos.length;
}

export async function cancelar(id) {
  const t = await almacen.obtenerTrabajo(id);
  if (!t) return;
  cancelarTemporizador(id);
  try { if (t.cancel_url) await proveedorActivo().cancelar(t); } catch { /* ya termino o no se puede */ }
  t.estado = 'cancelado';
  t.actualizado = Date.now();
  await almacen.guardarTrabajo(t);
  avisar(t);
}

export async function borrar(id) {
  const t = await almacen.obtenerTrabajo(id);
  cancelarTemporizador(id);
  if (t && t.medios) for (const m of t.medios) if (m.archivado) await almacen.borrarMedio(m.archivado).catch(() => {});
  await almacen.borrarTrabajo(id);
  avisar({ id, estado: 'borrado' });
}

export const estadosVivos = ESTADOS_VIVOS;
