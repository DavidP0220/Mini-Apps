// Service worker. Cachea SOLO el armazon de la app.
// Los medios generados NO se cachean aqui: viven en IndexedDB, que es donde se pueden borrar
// selectivamente y no compiten con el limite de la cache.
const CACHE = 'forja-v1';
const ARMAZON = [
  './', './index.html', './styles.css', './manifest.json',
  './modelos.json', './presets.json',
  './js/app.js', './js/almacen.js', './js/proveedor.js', './js/cola.js', './js/catalogo.js'
];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(ARMAZON)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', e => {
  e.waitUntil(caches.keys()
    .then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k))))
    .then(() => self.clients.claim()));
});

self.addEventListener('fetch', e => {
  const url = new URL(e.request.url);
  // Nunca interceptar llamadas al proveedor ni a CDNs de medios.
  if (url.origin !== self.location.origin) return;
  if (e.request.method !== 'GET') return;

  // Red primero para los JSON de catalogo (para que editarlos surta efecto al recargar),
  // cache primero para el resto del armazon.
  if (url.pathname.endsWith('.json')) {
    e.respondWith(fetch(e.request).then(r => {
      const copia = r.clone();
      caches.open(CACHE).then(c => c.put(e.request, copia));
      return r;
    }).catch(() => caches.match(e.request)));
    return;
  }
  e.respondWith(caches.match(e.request).then(r => r || fetch(e.request)));
});
