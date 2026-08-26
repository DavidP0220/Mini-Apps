#!/usr/bin/env node
// hc.mjs — lector selectivo del conocimiento de Human Chronicles.
// Existe por la misma razón que tools/content.mjs: leer un documento entero cuesta
// miles de tokens. Aquí se trae solo la sección que hace falta.
//
//   node human-chronicles/tools/hc.mjs listar
//   node human-chronicles/tools/hc.mjs ver <doc> [n-seccion]
//   node human-chronicles/tools/hc.mjs buscar "texto"
//   node human-chronicles/tools/hc.mjs estado
//   node human-chronicles/tools/hc.mjs huecos

import { readdirSync, readFileSync, statSync } from 'node:fs';
import { join, relative, basename } from 'node:path';
import { fileURLToPath } from 'node:url';

const RAIZ = join(fileURLToPath(new URL('.', import.meta.url)), '..');
const IGNORAR = new Set(['tools', 'icons']);

function documentos() {
  const salida = [];
  (function recorrer(dir) {
    for (const entrada of readdirSync(dir)) {
      if (IGNORAR.has(entrada)) continue;
      const ruta = join(dir, entrada);
      if (statSync(ruta).isDirectory()) recorrer(ruta);
      else if (entrada.endsWith('.md')) salida.push(ruta);
    }
  })(RAIZ);
  return salida.sort();
}

function resolver(clave) {
  const docs = documentos();
  const k = clave.toLowerCase();
  return docs.find(d => basename(d).toLowerCase() === k)
      || docs.find(d => basename(d, '.md').toLowerCase() === k)
      || docs.find(d => basename(d).toLowerCase().includes(k))
      || docs.find(d => relative(RAIZ, d).toLowerCase().includes(k));
}

// Corta por encabezados de nivel 1-2. Devuelve [{titulo, cuerpo}].
function secciones(texto) {
  const lineas = texto.split('\n');
  const bloques = [];
  let actual = { titulo: '(cabecera)', cuerpo: [] };
  for (const linea of lineas) {
    if (/^#{1,2} /.test(linea)) {
      if (actual.cuerpo.length || actual.titulo !== '(cabecera)') bloques.push(actual);
      actual = { titulo: linea.replace(/^#+ /, '').trim(), cuerpo: [] };
    } else actual.cuerpo.push(linea);
  }
  bloques.push(actual);
  return bloques;
}

const tokens = n => Math.round(n / 3.8); // aprox. es/markdown

const [cmd, ...args] = process.argv.slice(2);

if (cmd === 'listar') {
  const docs = documentos();
  let total = 0;
  console.log(`\n${docs.length} documentos en human-chronicles/\n`);
  let grupoAnterior = '';
  for (const d of docs) {
    const rel = relative(RAIZ, d);
    const grupo = rel.includes('/') ? rel.split('/')[0] : '.';
    if (grupo !== grupoAnterior) { console.log(`  ${grupo}/`); grupoAnterior = grupo; }
    const bytes = statSync(d).size;
    total += bytes;
    const secs = secciones(readFileSync(d, 'utf8')).length;
    console.log(`    ${basename(d).padEnd(52)} ${String(Math.round(bytes / 1024)).padStart(3)} KB  ~${String(tokens(bytes)).padStart(5)} tok  ${secs} secc.`);
  }
  console.log(`\n  TOTAL ${Math.round(total / 1024)} KB ≈ ${tokens(total).toLocaleString('es')} tokens si se leyera entero.`);
  console.log(`  Usa "ver <doc> <n>" para traer una sola sección.\n`);

} else if (cmd === 'ver') {
  const doc = resolver(args[0] || '');
  if (!doc) { console.error(`No encuentro "${args[0]}". Prueba: hc.mjs listar`); process.exit(1); }
  const secs = secciones(readFileSync(doc, 'utf8'));
  const n = args[1];
  if (n === undefined) {
    console.log(`\n${relative(RAIZ, doc)} — ${secs.length} secciones:\n`);
    secs.forEach((s, i) => {
      const b = s.cuerpo.join('\n').length;
      console.log(`  [${String(i).padStart(2)}] ${s.titulo.slice(0, 66).padEnd(68)} ~${tokens(b)} tok`);
    });
    console.log(`\nUsa: hc.mjs ver ${args[0]} <n>\n`);
  } else {
    const s = secs[Number(n)];
    if (!s) { console.error(`Sección ${n} no existe (0-${secs.length - 1}).`); process.exit(1); }
    console.log(`\n## ${s.titulo}\n${s.cuerpo.join('\n')}`);
  }

} else if (cmd === 'buscar') {
  const aguja = (args.join(' ') || '').toLowerCase();
  if (!aguja) { console.error('Falta el texto a buscar.'); process.exit(1); }
  let hallazgos = 0;
  for (const d of documentos()) {
    readFileSync(d, 'utf8').split('\n').forEach((linea, i) => {
      if (linea.toLowerCase().includes(aguja)) {
        hallazgos++;
        console.log(`${relative(RAIZ, d)}:${i + 1}: ${linea.trim().slice(0, 150)}`);
      }
    });
  }
  console.log(`\n${hallazgos} coincidencias.`);

} else if (cmd === 'estado' || cmd === 'huecos') {
  const doc = cmd === 'estado'
    ? resolver('ESTADO_CANAL.md')
    : resolver('PERFIL_DEL_PROYECTO.md');
  const secs = secciones(readFileSync(doc, 'utf8'));
  const clave = cmd === 'estado' ? 'ficha del canal' : 'habilidades que faltan';
  const s = secs.find(x => x.titulo.toLowerCase().includes(clave)) || secs[1];
  console.log(`\n(${relative(RAIZ, doc)})\n\n## ${s.titulo}\n${s.cuerpo.join('\n')}`);

} else {
  console.log(`
hc.mjs — lector selectivo de Human Chronicles (ahorro de tokens)

  listar                  índice de documentos con su coste en tokens
  ver <doc>               secciones de un documento y lo que cuesta cada una
  ver <doc> <n>           SOLO esa sección
  buscar "texto"          grep sobre todo el conocimiento
  estado                  ficha del canal (fuente única de verdad)
  huecos                  tabla de lo que falta por aprender
`);
}
