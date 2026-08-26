// almacen.js — persistencia local. IndexedDB para trabajos y medios, localStorage para ajustes.
// Regla heredada de 07_ERRORES_Y_LECCIONES (leccion 3): el registro de un trabajo nunca depende
// de que una llamada de red opcional tenga exito. Se escribe primero, se enriquece despues.

const BD = 'forja';
const VERSION = 1;
let _bd = null;

function abrir() {
  if (_bd) return Promise.resolve(_bd);
  return new Promise((ok, mal) => {
    const req = indexedDB.open(BD, VERSION);
    req.onupgradeneeded = () => {
      const db = req.result;
      if (!db.objectStoreNames.contains('trabajos')) {
        const s = db.createObjectStore('trabajos', { keyPath: 'id' });
        s.createIndex('creado', 'creado');
        s.createIndex('estado', 'estado');
      }
      if (!db.objectStoreNames.contains('medios')) {
        db.createObjectStore('medios', { keyPath: 'id' });
      }
    };
    req.onsuccess = () => { _bd = req.result; ok(_bd); };
    req.onerror = () => mal(req.error);
  });
}

function tx(almacen, modo, fn) {
  return abrir().then(db => new Promise((ok, mal) => {
    const t = db.transaction(almacen, modo);
    const s = t.objectStore(almacen);
    let resultado;
    try { resultado = fn(s); } catch (e) { mal(e); return; }
    t.oncomplete = () => ok(resultado && resultado.result !== undefined ? resultado.result : resultado);
    t.onerror = () => mal(t.error);
    t.onabort = () => mal(t.error);
  }));
}

export const almacen = {
  guardarTrabajo: (t) => tx('trabajos', 'readwrite', s => s.put(t)).then(() => t),
  obtenerTrabajo: (id) => tx('trabajos', 'readonly', s => s.get(id)),
  borrarTrabajo: (id) => tx('trabajos', 'readwrite', s => s.delete(id)),
  listarTrabajos: () => tx('trabajos', 'readonly', s => s.getAll())
    .then(l => (l || []).sort((a, b) => b.creado - a.creado)),

  guardarMedio: (id, blob, tipo) => tx('medios', 'readwrite', s => s.put({ id, blob, tipo })),
  obtenerMedio: (id) => tx('medios', 'readonly', s => s.get(id)),
  borrarMedio: (id) => tx('medios', 'readwrite', s => s.delete(id)),

  async espacioUsado() {
    if (!navigator.storage || !navigator.storage.estimate) return null;
    const e = await navigator.storage.estimate();
    return { usado: e.usage || 0, disponible: e.quota || 0 };
  },

  async exportar() {
    const trabajos = await almacen.listarTrabajos();
    return { version: 1, exportado: Date.now(), ajustes: ajustes.todos(), trabajos };
  },

  async importar(datos) {
    if (!datos || !Array.isArray(datos.trabajos)) throw new Error('Respaldo invalido');
    for (const t of datos.trabajos) await almacen.guardarTrabajo(t);
    return datos.trabajos.length;
  }
};

// --- Ajustes (localStorage). La API key vive solo aqui, en este navegador, nunca en el codigo. ---
const CLAVE = 'forja.ajustes';
const POR_DEFECTO = {
  apiKey: '',
  proxyUrl: '',        // si se llena, las llamadas van al proxy en vez de directo a fal
  modo: 'demo',        // 'demo' | 'fal'
  archivarMedios: true,
  limiteGastoDiario: 5 // USD. Freno de mano: por encima de esto la app pide confirmacion extra.
};

export const ajustes = {
  todos() {
    try { return { ...POR_DEFECTO, ...JSON.parse(localStorage.getItem(CLAVE) || '{}') }; }
    catch { return { ...POR_DEFECTO }; }
  },
  get(k) { return ajustes.todos()[k]; },
  set(k, v) {
    const a = ajustes.todos(); a[k] = v;
    localStorage.setItem(CLAVE, JSON.stringify(a));
    return a;
  },
  merge(obj) {
    const a = { ...ajustes.todos(), ...obj };
    localStorage.setItem(CLAVE, JSON.stringify(a));
    return a;
  }
};
