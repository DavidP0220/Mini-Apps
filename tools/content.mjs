#!/usr/bin/env node
/**
 * Editor quirúrgico de content.json.
 *
 * Un content.json real pesa ~21 KB (~5.300 tokens). Cargarlo entero para
 * cambiar un párrafo se paga en CADA turno siguiente de la sesión.
 * Estos comandos leen y escriben solo el trozo necesario.
 *
 * Comandos:
 *   node tools/content.mjs stats <app>
 *   node tools/content.mjs listar <app>
 *   node tools/content.mjs ver <app> <capituloId>
 *   node tools/content.mjs set <app> <capituloId> <nSeccion> --body "texto" [--heading "titulo"]
 *   node tools/content.mjs reemplazar <app> <capituloId> --archivo capitulo.json
 *   node tools/content.mjs agregar-capitulo <app> --id nuevo --titulo "Título" [--icono 📗]
 *
 * <app> es el nombre de la carpeta dentro de apps/
 */

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const RAIZ = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const [comando, app, ...resto] = process.argv.slice(2);

const opt = (nombre) => {
  const i = resto.indexOf('--' + nombre);
  return i >= 0 && resto[i + 1] ? resto[i + 1] : null;
};
const sueltos = resto.filter((a, i) => !a.startsWith('--') && !(i > 0 && resto[i - 1].startsWith('--')));

function ayuda(msg) {
  if (msg) console.error('Error: ' + msg + '\n');
  console.error(fs.readFileSync(fileURLToPath(import.meta.url), 'utf8').split('*/')[0].replace(/^\/\*\*|^ \* ?/gm, '').trim());
  process.exit(msg ? 1 : 0);
}

if (!comando || comando === '--help') ayuda();
if (!app) ayuda('falta el nombre de la app (carpeta dentro de apps/)');

const ruta = path.join(RAIZ, 'apps', app, 'content.json');
if (!fs.existsSync(ruta)) ayuda(`no existe apps/${app}/content.json`);

const data = JSON.parse(fs.readFileSync(ruta, 'utf8'));
const guardar = () => fs.writeFileSync(ruta, JSON.stringify(data, null, 2) + '\n');
const tokens = (t) => Math.round(t.length / 4);
const buscaCapitulo = (id) => {
  const c = data.chapters.find((x) => x.id === id);
  if (!c) ayuda(`no existe el capítulo "${id}". Usa: node tools/content.mjs listar ${app}`);
  return c;
};

switch (comando) {
  case 'stats': {
    const bruto = fs.readFileSync(ruta, 'utf8');
    console.log(`apps/${app}/content.json`);
    console.log(`  Tamaño        : ${(bruto.length / 1024).toFixed(1)} KB (~${tokens(bruto).toLocaleString('es-CO')} tokens)`);
    console.log(`  Capítulos     : ${data.chapters.length}`);
    const secciones = data.chapters.reduce((a, c) => a + (c.sections?.length || 0), 0);
    console.log(`  Secciones     : ${secciones}`);
    console.log('\nCargar este archivo entero cuesta ~' + tokens(bruto).toLocaleString('es-CO') +
      ' tokens en cada turno posterior de la sesión.');
    console.log('Usa "ver <capitulo>" para traer solo lo necesario.');
    break;
  }

  case 'listar': {
    console.log(`${data.meta.title}  (apps/${app})\n`);
    data.chapters.forEach((c, i) => {
      const tipos = (c.sections || []).map((s) => s.type);
      const cuenta = tipos.reduce((a, t) => ((a[t] = (a[t] || 0) + 1), a), {});
      const detalle = Object.entries(cuenta).map(([t, n]) => `${n} ${t}`).join(', ');
      console.log(`${String(i).padStart(2)}. ${(c.id || '').padEnd(22)} ${c.title}`);
      console.log(`    ${(c.sections || []).length} secciones (${detalle || 'vacío'})`);
    });
    console.log('\nVer un capítulo:  node tools/content.mjs ver ' + app + ' <id>');
    break;
  }

  case 'ver': {
    const id = sueltos[0];
    if (!id) ayuda('falta el id del capítulo');
    const c = buscaCapitulo(id);
    const texto = JSON.stringify(c, null, 2);
    console.log(texto);
    console.error(`\n[~${tokens(texto).toLocaleString('es-CO')} tokens, en vez de ~${tokens(fs.readFileSync(ruta, 'utf8')).toLocaleString('es-CO')} del archivo completo]`);
    break;
  }

  case 'set': {
    const [id, nStr] = sueltos;
    if (!id || nStr === undefined) ayuda('uso: set <app> <capituloId> <nSeccion> --body "texto"');
    const c = buscaCapitulo(id);
    const n = Number(nStr);
    const s = (c.sections || [])[n];
    if (!s) ayuda(`el capítulo "${id}" no tiene sección ${n} (tiene ${(c.sections || []).length})`);
    const body = opt('body');
    const heading = opt('heading');
    if (body === null && heading === null) ayuda('indica --body y/o --heading');
    if (body !== null) s.body = body;
    if (heading !== null) s.heading = heading;
    guardar();
    console.log(`Actualizado: ${app} / ${id} / sección ${n}`);
    break;
  }

  case 'reemplazar': {
    const id = sueltos[0];
    const archivo = opt('archivo');
    if (!id || !archivo) ayuda('uso: reemplazar <app> <capituloId> --archivo capitulo.json');
    const nuevo = JSON.parse(fs.readFileSync(archivo, 'utf8'));
    const i = data.chapters.findIndex((x) => x.id === id);
    if (i < 0) ayuda(`no existe el capítulo "${id}"`);
    nuevo.id = nuevo.id || id;
    data.chapters[i] = nuevo;
    guardar();
    console.log(`Capítulo "${id}" reemplazado desde ${archivo}`);
    break;
  }

  case 'agregar-capitulo': {
    const id = opt('id');
    const titulo = opt('titulo');
    if (!id || !titulo) ayuda('uso: agregar-capitulo <app> --id nuevo --titulo "Título"');
    if (data.chapters.some((c) => c.id === id)) ayuda(`ya existe un capítulo con id "${id}"`);
    data.chapters.push({
      id,
      title: titulo,
      icon: opt('icono') || '📗',
      sections: [{ type: 'text', heading: titulo, body: 'Pendiente de redactar.' }],
    });
    guardar();
    console.log(`Capítulo "${id}" agregado al final (${data.chapters.length} en total)`);
    break;
  }

  default:
    ayuda(`comando desconocido "${comando}"`);
}
