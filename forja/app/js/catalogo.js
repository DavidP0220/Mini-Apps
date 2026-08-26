// catalogo.js — modelos, presets y calculo de costo.
// Todo sale de modelos.json y presets.json: cambiarlos NO requiere tocar codigo.

let _modelos = null, _presets = null, _camaras = null;

export async function cargar() {
  if (_modelos) return { modelos: _modelos, presets: _presets, camaras: _camaras };
  const [m, p] = await Promise.all([
    fetch('modelos.json').then(r => r.json()),
    fetch('presets.json').then(r => r.json())
  ]);
  _modelos = m.modelos;
  _presets = p.presets;
  _camaras = p.camaras;
  return { modelos: _modelos, presets: _presets, camaras: _camaras };
}

export function modelos() { return _modelos || []; }
export function presets() { return _presets || []; }
export function camaras() { return _camaras || []; }

export function modelo(id) {
  return (_modelos || []).find(m => m.id === id) || null;
}

export function camara(id) {
  return (_camaras || []).find(c => c.id === id) || null;
}

export function preset(id) {
  return (_presets || []).find(p => p.id === id) || null;
}

/**
 * Costo estimado en USD, ANTES de apretar el boton.
 * Esta es la diferencia mas concreta frente a comprar creditos: aqui ves dolares,
 * no fichas opacas cuyo valor real solo conoce el vendedor.
 * Devuelve null si el modelo no esta en el catalogo (ID pegado a mano) — y la UI lo dice.
 */
export function estimarCosto(modeloId, { duracion = 5, salidas = 1 } = {}) {
  const m = modelo(modeloId);
  if (!m || !m.costo) return null;
  if (m.costo.modo === 'por_segundo') return m.costo.usd * duracion * salidas;
  return m.costo.usd * salidas;
}

/** Arma el prompt final combinando preset + idea + camara. */
export function componerPrompt({ presetId, idea, camaraId }) {
  const p = preset(presetId);
  const c = camara(camaraId);
  const fraseCamara = c ? c.frase : '';
  if (!p) return [idea, fraseCamara].filter(Boolean).join('. ');
  return p.plantilla
    .replace('{idea}', idea || '')
    .replace('{camara}', fraseCamara)
    .replace(/\s+/g, ' ')
    .trim();
}

/** Traduce nuestros campos genericos a lo que espera cada modelo de fal. */
export function construirEntrada(modeloId, { prompt, duracion, aspecto, resolucion, salidas, imagenUrl }) {
  const m = modelo(modeloId);
  const campos = (m && m.campos) || ['prompt'];
  const entrada = { prompt };
  if (campos.includes('duration')) entrada.duration = String(duracion);
  if (campos.includes('aspect_ratio') && aspecto) entrada.aspect_ratio = aspecto;
  if (campos.includes('resolution') && resolucion) entrada.resolution = resolucion;
  if (campos.includes('num_images') && salidas > 1) entrada.num_images = salidas;
  if (campos.includes('image_size') && aspecto) entrada.image_size = aspectoAImageSize(aspecto);
  if (campos.includes('image_url') && imagenUrl) entrada.image_url = imagenUrl;
  return entrada;
}

function aspectoAImageSize(a) {
  return { '16:9': 'landscape_16_9', '9:16': 'portrait_16_9', '1:1': 'square_hd', '4:3': 'landscape_4_3' }[a] || 'landscape_16_9';
}
