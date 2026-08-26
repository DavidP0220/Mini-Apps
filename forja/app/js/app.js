// app.js — interfaz. Une catalogo + cola + almacen. Nada de logica de proveedor vive aqui.

import { almacen, ajustes } from './almacen.js';
import * as cat from './catalogo.js';
import * as cola from './cola.js';

const $ = (s) => document.querySelector(s);
const $$ = (s) => Array.from(document.querySelectorAll(s));

const estado = {
  preset: null,
  camara: null,
  categoria: 'todas',
  trabajos: []
};

// ---------------------------------------------------------------- utilidades
const usd = (n) => '$' + (n || 0).toFixed(n && n < 0.1 ? 3 : 2);

function brindis(mensaje, clase = '') {
  const b = $('#brindis');
  b.textContent = mensaje;
  b.className = 'brindis visible ' + clase;
  clearTimeout(brindis._t);
  brindis._t = setTimeout(() => { b.className = 'brindis ' + clase; }, 5200);
}

function haceRato(ts) {
  const s = Math.floor((Date.now() - ts) / 1000);
  if (s < 60) return 'hace ' + s + 's';
  if (s < 3600) return 'hace ' + Math.floor(s / 60) + ' min';
  if (s < 86400) return 'hace ' + Math.floor(s / 3600) + ' h';
  return new Date(ts).toLocaleDateString('es');
}

const NOMBRE_ESTADO = {
  creando: 'enviando', en_cola: 'en cola', procesando: 'generando',
  listo: 'listo', fallido: 'fallo', cancelado: 'cancelado'
};

// ---------------------------------------------------------------- arranque
async function arrancar() {
  await cat.cargar();
  pintarFiltros();
  pintarPresets();
  pintarCamaras();
  pintarModelos();
  cargarAjustesEnFormulario();
  conectarEventos();

  estado.trabajos = await almacen.listarTrabajos();
  cola.alCambiar(alCambiarTrabajo);

  const retomados = await cola.reanudar();
  if (retomados) brindis(retomados + ' trabajo(s) en curso retomados. Cerrar la pestana no los pierde.', 'bien');

  refrescarTodo();

  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('sw.js').catch(() => {});
  }
}

// ---------------------------------------------------------------- generar
function pintarFiltros() {
  const cats = ['todas', ...new Set(cat.presets().map(p => p.categoria))];
  $('#filtrosPreset').innerHTML = cats.map(c =>
    `<button class="filtro ${c === estado.categoria ? 'activo' : ''}" data-cat="${c}">${c}</button>`
  ).join('');
}

function pintarPresets() {
  const lista = cat.presets().filter(p => estado.categoria === 'todas' || p.categoria === estado.categoria);
  $('#rejillaPresets').innerHTML = lista.map(p => `
    <button class="tarjetaPreset ${estado.preset === p.id ? 'elegido' : ''}" data-preset="${p.id}">
      <span class="emoji">${p.emoji}</span>
      <span class="nombre">${p.nombre}</span>
      <span class="cat">${p.categoria}</span>
    </button>`).join('');
}

function pintarCamaras() {
  $('#rejillaCamaras').innerHTML = cat.camaras().map(c =>
    `<button class="chipCamara ${estado.camara === c.id ? 'elegido' : ''}" data-camara="${c.id}">${c.nombre}</button>`
  ).join('');
}

function pintarModelos() {
  const sel = $('#modelo');
  const grupos = { video: [], imagen: [] };
  cat.modelos().forEach(m => grupos[m.tipo] && grupos[m.tipo].push(m));
  sel.innerHTML =
    `<optgroup label="Video">${grupos.video.map(m => `<option value="${m.id}">${m.nombre}</option>`).join('')}</optgroup>` +
    `<optgroup label="Imagen">${grupos.imagen.map(m => `<option value="${m.id}">${m.nombre}</option>`).join('')}</optgroup>`;
}

function modeloElegido() {
  const manual = $('#modeloManual').value.trim();
  return manual || $('#modelo').value;
}

function pintarDuraciones() {
  const m = cat.modelo(modeloElegido());
  const sel = $('#duracion');
  const previa = sel.value;
  if (!m || m.tipo === 'imagen') {
    sel.innerHTML = '<option value="0">—</option>';
    sel.disabled = true;
  } else {
    const ds = m.duraciones || [5, 10];
    sel.innerHTML = ds.map(d => `<option value="${d}">${d} s</option>`).join('');
    sel.disabled = false;
    if (ds.includes(Number(previa))) sel.value = previa;
  }
}

function refrescarGenerar() {
  pintarDuraciones();

  const idModelo = modeloElegido();
  const m = cat.modelo(idModelo);
  $('#notaModelo').textContent = m ? m.notas : 'Modelo fuera del catalogo: la app lo enviara igual, pero no puede estimar el costo.';

  const prompt = cat.componerPrompt({
    presetId: estado.preset,
    idea: $('#idea').value.trim(),
    camaraId: estado.camara
  });
  $('#promptFinal').textContent = prompt || '—';

  const duracion = Number($('#duracion').value) || 5;
  const salidas = Number($('#salidas').value) || 1;
  const costo = cat.estimarCosto(idModelo, { duracion, salidas });
  $('#costoEstimado').textContent = costo === null ? 'desconocido' : usd(costo);

  const listo = Boolean($('#idea').value.trim());
  $('#btnGenerar').disabled = !listo;
  $('#btnGenerar').textContent = listo
    ? (costo === null ? 'Generar' : `Generar · ${usd(costo)}`)
    : 'Escribe tu idea';
}

async function generar() {
  const idea = $('#idea').value.trim();
  if (!idea) return;

  const idModelo = modeloElegido();
  const m = cat.modelo(idModelo);
  const duracion = Number($('#duracion').value) || 5;
  const salidas = Number($('#salidas').value) || 1;
  const costo = cat.estimarCosto(idModelo, { duracion, salidas }) || 0;

  const a = ajustes.todos();
  if (a.modo === 'fal' && !a.apiKey && !a.proxyUrl) {
    brindis('Falta la clave de fal.ai. Ve a Ajustes, o quedate en modo demo para probar sin gastar.', 'mal');
    irA('ajustes');
    return;
  }

  // Freno de mano: avisa antes de pasarte del limite diario que tu mismo pusiste.
  if (a.modo === 'fal') {
    const hoy = gastoDe(estado.trabajos, 'hoy');
    if (hoy + costo > a.limiteGastoDiario) {
      const seguir = confirm(
        `Esto llevaria tu gasto de hoy a ${usd(hoy + costo)}, por encima del limite de ${usd(a.limiteGastoDiario)} que configuraste.\n\n¿Generar de todos modos?`
      );
      if (!seguir) return;
    }
  }

  const prompt = cat.componerPrompt({ presetId: estado.preset, idea, camaraId: estado.camara });
  const entrada = cat.construirEntrada(idModelo, {
    prompt, duracion, aspecto: $('#aspecto').value, salidas,
    resolucion: '1080p'
  });

  $('#btnGenerar').disabled = true;
  try {
    await cola.encolar({
      modelo: idModelo,
      entrada,
      costoEstimado: costo,
      etiqueta: idea,
      preset: estado.preset,
      tipo: m ? m.tipo : 'video'
    });
    brindis('Encolado. Puedes cerrar la pestana: al volver se retoma solo.', 'bien');
    irA('cola');
  } catch (e) {
    brindis('No se pudo encolar: ' + e.message, 'mal');
  } finally {
    refrescarGenerar();
  }
}

// ---------------------------------------------------------------- cola
function pintarCola() {
  const vivos = estado.trabajos.filter(t => cola.estadosVivos.includes(t.estado));
  const recientes = estado.trabajos.filter(t => !cola.estadosVivos.includes(t.estado)).slice(0, 8);

  const c = $('#contadorCola');
  c.textContent = vivos.length;
  c.classList.toggle('oculto', vivos.length === 0);

  const lista = [...vivos, ...recientes];
  $('#listaCola').innerHTML = lista.length
    ? lista.map(filaTrabajo).join('')
    : '<p class="vacio">Nada en la cola. Genera algo desde la pestana Generar.</p>';
}

function filaTrabajo(t) {
  const vivo = cola.estadosVivos.includes(t.estado);
  const p = cat.preset(t.preset);
  const m = cat.modelo(t.modelo);
  return `
  <div class="trabajo" data-id="${t.id}">
    <div>
      <div class="idea">${escapar(t.etiqueta || '(sin titulo)')}</div>
      <div class="meta">
        <span class="etiqueta e-${t.estado}">${NOMBRE_ESTADO[t.estado] || t.estado}</span>
        ${p ? p.emoji + ' ' + escapar(p.nombre) + ' · ' : ''}${escapar(m ? m.nombre : t.modelo)}
        · ${haceRato(t.creado)}
        ${t.posicion != null && t.estado === 'en_cola' ? ' · puesto ' + t.posicion : ''}
        ${t.costoEstimado ? ' · ' + usd(t.costoEstimado) : ''}
        ${t.proveedor === 'demo' ? ' · <em>demo</em>' : ''}
      </div>
      ${t.error ? `<div class="error">${escapar(t.error)}</div>` : ''}
      ${vivo ? '<div class="barraProgreso"><i></i></div>' : ''}
    </div>
    <div class="botones">
      ${vivo ? `<button class="accion" data-accion="cancelar" data-id="${t.id}">Cancelar</button>` : ''}
      ${t.estado === 'fallido' ? `<button class="accion" data-accion="reintentar" data-id="${t.id}">Reintentar</button>` : ''}
      ${!vivo ? `<button class="accion peligro" data-accion="borrar" data-id="${t.id}">Borrar</button>` : ''}
    </div>
  </div>`;
}

// ---------------------------------------------------------------- biblioteca
async function pintarBiblioteca() {
  const q = $('#buscar').value.trim().toLowerCase();
  const listos = estado.trabajos.filter(t => t.estado === 'listo' && t.medios && t.medios.length);
  const filtrados = q
    ? listos.filter(t => (t.etiqueta + ' ' + t.modelo + ' ' + (t.preset || '')).toLowerCase().includes(q))
    : listos;

  if (!filtrados.length) {
    $('#rejillaBiblioteca').innerHTML = '<p class="vacio">' +
      (listos.length ? 'Nada coincide con esa busqueda.' : 'Todavia no hay nada generado.') + '</p>';
    return;
  }

  const tarjetas = [];
  for (const t of filtrados) {
    for (let i = 0; i < t.medios.length; i++) {
      const med = t.medios[i];
      let src = med.url;
      if (med.archivado) {
        const guardado = await almacen.obtenerMedio(med.archivado);
        if (guardado && guardado.blob) src = URL.createObjectURL(guardado.blob);
      }
      const esVideo = med.tipo === 'video' || /\.(mp4|webm)(\?|$)/i.test(med.url);
      const m = cat.modelo(t.modelo);
      tarjetas.push(`
        <div class="medio">
          <div class="lienzo">${esVideo
            ? `<video src="${src}" controls preload="metadata" playsinline></video>`
            : `<img src="${src}" alt="${escapar(t.etiqueta)}" loading="lazy">`}</div>
          <div class="cuerpo">
            <div class="idea">${escapar(t.etiqueta || '(sin titulo)')}</div>
            <div class="meta">${escapar(m ? m.nombre : t.modelo)} · ${haceRato(t.creado)} · ${usd(t.costoEstimado)}
              ${med.archivado ? ' · <span style="color:var(--ok)">copia local</span>' : ' · solo enlace'}</div>
            <div class="acciones">
              <a href="${src}" download="forja-${t.id}-${i}">Descargar</a>
              <button data-accion="rehacer" data-id="${t.id}">Rehacer</button>
              <button class="peligro" data-accion="borrar" data-id="${t.id}">Borrar</button>
            </div>
          </div>
        </div>`);
    }
  }
  $('#rejillaBiblioteca').innerHTML = tarjetas.join('');
}

// ---------------------------------------------------------------- gasto
function gastoDe(trabajos, periodo) {
  const ahora = new Date();
  const inicioHoy = new Date(ahora.getFullYear(), ahora.getMonth(), ahora.getDate()).getTime();
  const inicioMes = new Date(ahora.getFullYear(), ahora.getMonth(), 1).getTime();
  return trabajos
    .filter(t => t.proveedor !== 'demo' && ['listo', 'procesando', 'en_cola'].includes(t.estado))
    .filter(t => periodo === 'todo' || (periodo === 'hoy' ? t.creado >= inicioHoy : t.creado >= inicioMes))
    .reduce((s, t) => s + (t.costoEstimado || 0), 0);
}

function pintarGasto() {
  const T = estado.trabajos;
  const hoy = gastoDe(T, 'hoy'), mes = gastoDe(T, 'mes'), todo = gastoDe(T, 'todo');
  const reales = T.filter(t => t.proveedor !== 'demo' && t.estado === 'listo');

  $('#gastoHoy').textContent = usd(hoy);

  $('#tarjetasGasto').innerHTML = `
    <div class="tarjeta"><div class="valor">${usd(hoy)}</div><div class="rotulo">hoy</div></div>
    <div class="tarjeta"><div class="valor">${usd(mes)}</div><div class="rotulo">este mes</div></div>
    <div class="tarjeta"><div class="valor">${usd(todo)}</div><div class="rotulo">desde el inicio</div></div>
    <div class="tarjeta"><div class="valor">${reales.length}</div><div class="rotulo">generaciones reales</div></div>
    <div class="tarjeta"><div class="valor">$0.00</div><div class="rotulo">costo fijo mensual</div></div>`;

  const porModelo = {};
  for (const t of reales) {
    const k = t.modelo;
    porModelo[k] = porModelo[k] || { n: 0, usd: 0 };
    porModelo[k].n++;
    porModelo[k].usd += t.costoEstimado || 0;
  }
  const filas = Object.entries(porModelo).sort((a, b) => b[1].usd - a[1].usd);
  $('#tablaGasto').innerHTML = filas.length ? `
    <table><thead><tr><th>Modelo</th><th class="num">Generaciones</th><th class="num">Gasto</th><th class="num">Promedio</th></tr></thead>
    <tbody>${filas.map(([id, d]) => {
      const m = cat.modelo(id);
      return `<tr><td>${escapar(m ? m.nombre : id)}</td><td class="num">${d.n}</td><td class="num">${usd(d.usd)}</td><td class="num">${usd(d.usd / d.n)}</td></tr>`;
    }).join('')}</tbody></table>`
    : '<p class="vacio">Sin generaciones reales todavia. El modo demo no cuenta como gasto.</p>';

  // La comparacion honesta: que costaria el mismo uso en una suscripcion.
  const mesUsd = mes;
  $('#comparacion').innerHTML = `
    <div class="tarjeta destacada"><div class="valor">${usd(mesUsd)}</div><div class="rotulo">Forja este mes<br>(solo GPU, sin cuota)</div></div>
    <div class="tarjeta"><div class="valor">$19.00</div><div class="rotulo">Higgsfield Starter<br>270 creditos que caducan</div></div>
    <div class="tarjeta"><div class="valor">$59.00</div><div class="rotulo">Higgsfield Plus<br>1.200 creditos que caducan</div></div>
    <div class="tarjeta"><div class="valor">$129.00</div><div class="rotulo">Higgsfield Ultra<br>3.000 creditos que caducan</div></div>`;
}

// ---------------------------------------------------------------- ajustes
function cargarAjustesEnFormulario() {
  const a = ajustes.todos();
  $$('input[name=modo]').forEach(r => r.checked = r.value === a.modo);
  $('#apiKey').value = a.apiKey;
  $('#proxyUrl').value = a.proxyUrl;
  $('#limiteGasto').value = a.limiteGastoDiario;
  $('#archivarMedios').checked = a.archivarMedios;
  pintarInsignia();
}

function pintarInsignia() {
  const a = ajustes.todos();
  const i = $('#insigniaModo');
  const real = a.modo === 'fal';
  i.textContent = real ? 'fal.ai' : 'demo';
  i.classList.toggle('vivo', real);
  $('#avisoModo').textContent = real
    ? 'Modo real: cada generacion consume saldo de tu cuenta de fal.ai.'
    : 'Modo demo: no sale nada a internet y no cuesta nada.';
}

async function pintarUsoDisco() {
  const e = await almacen.espacioUsado();
  $('#usoDisco').textContent = e
    ? `Ocupado ${(e.usado / 1048576).toFixed(1)} MB de ~${(e.disponible / 1048576).toFixed(0)} MB disponibles en este navegador.`
    : 'Este navegador no reporta el espacio usado.';
}

// ---------------------------------------------------------------- navegacion y eventos
function irA(vista) {
  $$('.pestana').forEach(b => b.classList.toggle('activa', b.dataset.vista === vista));
  $$('.vista').forEach(s => s.classList.toggle('activa', s.id === 'vista-' + vista));
  if (vista === 'biblioteca') pintarBiblioteca();
  if (vista === 'gasto') pintarGasto();
  if (vista === 'ajustes') pintarUsoDisco();
}

async function alCambiarTrabajo() {
  estado.trabajos = await almacen.listarTrabajos();
  refrescarTodo();
}

function refrescarTodo() {
  pintarCola();
  pintarGasto();
  refrescarGenerar();
  if ($('#vista-biblioteca').classList.contains('activa')) pintarBiblioteca();
}

function conectarEventos() {
  $('#pestanas').addEventListener('click', e => {
    const b = e.target.closest('.pestana');
    if (b) irA(b.dataset.vista);
  });

  $('#filtrosPreset').addEventListener('click', e => {
    const b = e.target.closest('.filtro');
    if (!b) return;
    estado.categoria = b.dataset.cat;
    pintarFiltros(); pintarPresets();
  });

  $('#rejillaPresets').addEventListener('click', e => {
    const b = e.target.closest('.tarjetaPreset');
    if (!b) return;
    estado.preset = estado.preset === b.dataset.preset ? null : b.dataset.preset;
    const p = cat.preset(estado.preset);
    if (p) {
      if (p.camara) estado.camara = p.camara;
      if (p.modelo && cat.modelo(p.modelo)) { $('#modeloManual').value = ''; $('#modelo').value = p.modelo; }
    }
    pintarPresets(); pintarCamaras(); refrescarGenerar();
  });

  $('#rejillaCamaras').addEventListener('click', e => {
    const b = e.target.closest('.chipCamara');
    if (!b) return;
    estado.camara = estado.camara === b.dataset.camara ? null : b.dataset.camara;
    pintarCamaras(); refrescarGenerar();
  });

  ['#idea', '#modelo', '#modeloManual', '#duracion', '#aspecto', '#salidas']
    .forEach(s => $(s).addEventListener('input', refrescarGenerar));
  $('#modelo').addEventListener('change', refrescarGenerar);

  $('#btnGenerar').addEventListener('click', generar);
  $('#buscar').addEventListener('input', pintarBiblioteca);

  document.addEventListener('click', async e => {
    const b = e.target.closest('[data-accion]');
    if (!b) return;
    const id = b.dataset.id;
    if (b.dataset.accion === 'cancelar') { await cola.cancelar(id); brindis('Cancelado.'); }
    if (b.dataset.accion === 'borrar') {
      if (confirm('¿Borrar este trabajo y su copia local? No se puede deshacer.')) {
        await cola.borrar(id); await alCambiarTrabajo(); pintarBiblioteca();
      }
    }
    if (b.dataset.accion === 'reintentar' || b.dataset.accion === 'rehacer') {
      const t = await almacen.obtenerTrabajo(id);
      if (!t) return;
      $('#idea').value = t.etiqueta || '';
      estado.preset = t.preset;
      if (cat.modelo(t.modelo)) $('#modelo').value = t.modelo;
      pintarPresets(); refrescarGenerar(); irA('generar');
      brindis('Cargado en el generador. Revisa y aprieta Generar.');
    }
  });

  // --- ajustes ---
  $$('input[name=modo]').forEach(r => r.addEventListener('change', () => {
    ajustes.set('modo', r.value);
    pintarInsignia(); refrescarGenerar();
  }));
  $('#apiKey').addEventListener('change', () => { ajustes.set('apiKey', $('#apiKey').value.trim()); brindis('Clave guardada en este navegador.'); });
  $('#proxyUrl').addEventListener('change', () => ajustes.set('proxyUrl', $('#proxyUrl').value.trim()));
  $('#limiteGasto').addEventListener('change', () => ajustes.set('limiteGastoDiario', Number($('#limiteGasto').value) || 0));
  $('#archivarMedios').addEventListener('change', () => ajustes.set('archivarMedios', $('#archivarMedios').checked));

  $('#btnExportar').addEventListener('click', async () => {
    const datos = await almacen.exportar();
    delete datos.ajustes.apiKey; // un respaldo nunca lleva la clave dentro
    const url = URL.createObjectURL(new Blob([JSON.stringify(datos, null, 2)], { type: 'application/json' }));
    const a = document.createElement('a');
    a.href = url; a.download = 'forja-respaldo-' + new Date().toISOString().slice(0, 10) + '.json';
    a.click(); URL.revokeObjectURL(url);
    brindis('Respaldo descargado (sin la clave, a proposito).', 'bien');
  });

  $('#btnImportar').addEventListener('click', () => $('#ficheroImportar').click());
  $('#ficheroImportar').addEventListener('change', async e => {
    const f = e.target.files[0];
    if (!f) return;
    try {
      const n = await almacen.importar(JSON.parse(await f.text()));
      await alCambiarTrabajo();
      brindis(n + ' trabajos importados.', 'bien');
    } catch (err) { brindis('No se pudo importar: ' + err.message, 'mal'); }
  });

  $('#btnBorrarTodo').addEventListener('click', async () => {
    if (!confirm('Esto borra todos los trabajos y las copias locales de este navegador. ¿Seguro?')) return;
    for (const t of estado.trabajos) await cola.borrar(t.id);
    await alCambiarTrabajo();
    brindis('Todo borrado.');
  });
}

function escapar(s) {
  return String(s == null ? '' : s).replace(/[&<>"']/g, c =>
    ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
}

// Refresco del "hace rato" sin depender de eventos de red.
setInterval(() => { if ($('#vista-cola').classList.contains('activa')) pintarCola(); }, 5000);

arrancar().catch(e => {
  document.body.innerHTML = '<div style="padding:40px;font-family:system-ui;color:#e6ebf4">' +
    '<h1>No arranco</h1><pre>' + e.message + '</pre>' +
    '<p>Si abriste el archivo con doble clic, no va a funcionar: los modulos de JavaScript necesitan un servidor. ' +
    'Ejecuta <code>node forja/servir.mjs</code> y entra a la direccion que imprime.</p></div>';
  console.error(e);
});
