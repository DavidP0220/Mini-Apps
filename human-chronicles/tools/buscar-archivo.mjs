#!/usr/bin/env node
// buscar-archivo.mjs — busca material de dominio público en Wikimedia Commons,
// Library of Congress e Internet Archive, descarta lo que no tenga licencia
// legible, y genera el sources_<video>.md obligatorio del canal.
//
//   node human-chronicles/tools/buscar-archivo.mjs "Constantinople 1453" --video video-01
//   node human-chronicles/tools/buscar-archivo.mjs "roman aqueduct" --limite 15 --solo commons
//
// ⚠️ ESCRITO PERO NO EJECUTADO NUNCA (2026-08-26): el entorno remoto donde se
//    escribió bloquea archive.org, loc.gov y commons.wikimedia.org en el proxy
//    de red. La primera corrida en la máquina de David ES el paso de validación.
//    Ver investigacion/2026-08-26_hueco-02_archivo-dominio-publico.md §4.

import { writeFileSync, mkdirSync, existsSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

const RAIZ = join(fileURLToPath(new URL('.', import.meta.url)), '..');

const argv = process.argv.slice(2);
const consulta = argv.filter(a => !a.startsWith('--'))[0];
const opcion = (nombre, def) => {
  const i = argv.indexOf(`--${nombre}`);
  return i === -1 ? def : argv[i + 1];
};
const video = opcion('video', null);
const limite = Number(opcion('limite', 10));
const solo = opcion('solo', null); // commons | loc | archive

if (!consulta) {
  console.error('Uso: buscar-archivo.mjs "termino de busqueda" [--video video-01] [--limite 10] [--solo commons|loc|archive]');
  process.exit(1);
}

// Licencias que se aceptan sin revisión adicional. Todo lo demás se descarta:
// lo que la API no pueda afirmar, NO entra (hueco-02 §2, paso 2).
const LICENCIAS_OK = [
  /public\s*domain/i, /^pd[-\s]/i, /\bpd\b/i, /cc0/i,
  /cc[-\s]?by(?![-\s]?(nc|nd))/i, /cc[-\s]?by[-\s]?sa/i,
  /no known restrictions/i, /attribution/i,
];
const LICENCIAS_NO = [/\bnc\b/i, /non[-\s]?commercial/i, /\bnd\b/i, /no\s?deriv/i, /all rights reserved/i];

const aceptable = txt => {
  if (!txt) return false;
  if (LICENCIAS_NO.some(r => r.test(txt))) return false;
  return LICENCIAS_OK.some(r => r.test(txt));
};

const pedir = async (url, etiqueta) => {
  try {
    const r = await fetch(url, { headers: { 'User-Agent': 'HumanChronicles-Research/1.0 (canal de historia; uso de dominio publico)' } });
    if (!r.ok) throw new Error(`HTTP ${r.status}`);
    return await r.json();
  } catch (e) {
    console.error(`  ⚠️  ${etiqueta} falló: ${e.message}`);
    return null;
  }
};

async function commons() {
  const url = 'https://commons.wikimedia.org/w/api.php?action=query&format=json&origin=*'
    + `&generator=search&gsrsearch=${encodeURIComponent(consulta)}&gsrnamespace=6&gsrlimit=${limite}`
    + '&prop=imageinfo&iiprop=url|extmetadata';
  const j = await pedir(url, 'Wikimedia Commons');
  const paginas = j?.query?.pages ? Object.values(j.query.pages) : [];
  return paginas.map(p => {
    const info = p.imageinfo?.[0] || {};
    const meta = info.extmetadata || {};
    const licencia = meta.LicenseShortName?.value || meta.UsageTerms?.value || '';
    return {
      fuente: 'Wikimedia Commons',
      titulo: (p.title || '').replace(/^File:/, ''),
      url: info.descriptionurl || `https://commons.wikimedia.org/wiki/${encodeURIComponent(p.title)}`,
      archivo: info.url || '',
      licencia,
      autor: (meta.Artist?.value || '').replace(/<[^>]+>/g, '').trim().slice(0, 80),
    };
  });
}

async function loc() {
  const url = `https://www.loc.gov/search/?q=${encodeURIComponent(consulta)}&fo=json&c=${limite}`;
  const j = await pedir(url, 'Library of Congress');
  return (j?.results || []).map(r => ({
    fuente: 'Library of Congress',
    titulo: Array.isArray(r.title) ? r.title[0] : (r.title || ''),
    url: r.id || r.url || '',
    archivo: (r.image_url && r.image_url[r.image_url.length - 1]) || '',
    licencia: [].concat(r.rights_advisory || r.rights || []).join('; '),
    autor: [].concat(r.contributor || []).join(', ').slice(0, 80),
  }));
}

async function archive() {
  const q = `${consulta} AND mediatype:(movies OR image)`;
  const campos = ['identifier', 'title', 'licenseurl', 'rights', 'creator', 'year']
    .map(c => `&fl%5B%5D=${c}`).join('');
  const url = `https://archive.org/advancedsearch.php?q=${encodeURIComponent(q)}${campos}&rows=${limite}&page=1&output=json`;
  const j = await pedir(url, 'Internet Archive');
  return (j?.response?.docs || []).map(d => ({
    fuente: 'Internet Archive',
    titulo: d.title || d.identifier,
    url: `https://archive.org/details/${d.identifier}`,
    archivo: '',
    licencia: d.licenseurl || d.rights || '',
    autor: [].concat(d.creator || []).join(', ').slice(0, 80),
  }));
}

const tareas = [];
if (!solo || solo === 'commons') tareas.push(commons());
if (!solo || solo === 'loc') tareas.push(loc());
if (!solo || solo === 'archive') tareas.push(archive());

console.log(`\nBuscando "${consulta}" en ${tareas.length} archivo(s)…\n`);
const todo = (await Promise.all(tareas)).flat();
const validos = todo.filter(i => aceptable(i.licencia));
const descartados = todo.length - validos.length;

console.log(`  ${todo.length} resultados · ${validos.length} con licencia utilizable · ${descartados} descartados\n`);
for (const i of validos) {
  console.log(`  [${i.fuente}] ${i.titulo.slice(0, 62)}`);
  console.log(`      ${i.licencia.slice(0, 60)}  ${i.url}`);
}

if (video) {
  const dir = join(RAIZ, 'produccion', video);
  if (!existsSync(dir)) mkdirSync(dir, { recursive: true });
  const ruta = join(dir, `sources_${video}.md`);
  const hoy = new Date().toISOString().slice(0, 10);
  const filas = validos.map(i =>
    `| ${i.titulo.replace(/\|/g, '/')} | ${i.fuente} | ${i.url} | ${i.licencia.replace(/\|/g, '/')} | ${i.autor.replace(/\|/g, '/') || '—'} | ${hoy} | ⬜ |`
  ).join('\n');
  writeFileSync(ruta, `# Procedencia del material — ${video}

**Consulta:** \`${consulta}\` · **Generado:** ${hoy} por \`tools/buscar-archivo.mjs\`

Obligatorio por \`ESTILO_HUMAN_CHRONICLES.md\` §4. Sirve para responder un reclamo de Content ID
con evidencia y como señal de esfuerzo humano ante la política de contenido no auténtico.

> **La columna "Revisado" NO la rellena la herramienta.** El filtro automático solo comprueba la
> licencia declarada del contenedor. Queda por comprobar a ojo, ítem por ítem, lo que ninguna API
> resuelve: **dominio público del video ≠ dominio público de todo su contenido** — música con
> derechos, obra de arte protegida, personas identificables. Marca ✅ solo lo que hayas mirado.

| Ítem | Fuente | URL | Licencia | Autor | Descargado | Revisado |
|---|---|---|---|---|---|---|
${filas || '| (sin resultados con licencia utilizable) | | | | | | |'}

**Descartados automáticamente por licencia no utilizable o ilegible:** ${descartados}
`);
  console.log(`\n  → ${ruta.replace(RAIZ, 'human-chronicles')}`);
  console.log(`     Recuerda rellenar la columna "Revisado" a mano.\n`);
} else {
  console.log(`\n  (usa --video <nombre> para generar el sources_<video>.md)\n`);
}
