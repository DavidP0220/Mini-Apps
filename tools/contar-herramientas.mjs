#!/usr/bin/env node
/**
 * Cuenta cuántas herramientas se cargaron en la sesión (el "equipaje" que se
 * paga en CADA turno) y de qué conector viene cada una.
 *
 * Sirve para comprobar el antes/después de apagar conectores en
 * https://claude.ai/customize/connectors
 *
 * Uso:
 *   node tools/contar-herramientas.mjs          # la sesión más reciente
 *   node tools/contar-herramientas.mjs --todas  # todas las sesiones
 */

import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';

const RAIZ = path.join(os.homedir(), '.claude', 'projects');
const todas = process.argv.includes('--todas');

if (!fs.existsSync(RAIZ)) {
  console.log('No hay transcripciones en ' + RAIZ);
  console.log('Ejecuta esto en la máquina donde usas Claude Code.');
  process.exit(0);
}

const archivos = [];
for (const dir of fs.readdirSync(RAIZ)) {
  const ruta = path.join(RAIZ, dir);
  if (!fs.statSync(ruta).isDirectory()) continue;
  for (const f of fs.readdirSync(ruta).filter((x) => x.endsWith('.jsonl'))) {
    const completa = path.join(ruta, f);
    archivos.push({ ruta: completa, mtime: fs.statSync(completa).mtimeMs, nombre: f });
  }
}

if (!archivos.length) {
  console.log('No se encontraron sesiones.');
  process.exit(0);
}

archivos.sort((a, b) => b.mtime - a.mtime);
const objetivo = todas ? archivos : [archivos[0]];

for (const { ruta, nombre } of objetivo) {
  const herramientas = new Set();
  let contextoInicial = 0;

  for (const linea of fs.readFileSync(ruta, 'utf8').split('\n')) {
    if (!linea.trim()) continue;
    let o;
    try { o = JSON.parse(linea); } catch { continue; }
    // El transcript registra altas y bajas: hay que aplicar ambas, en orden.
    o.attachment?.addedNames?.forEach((n) => herramientas.add(n));
    o.attachment?.readdedNames?.forEach((n) => herramientas.add(n));
    o.attachment?.removedNames?.forEach((n) => herramientas.delete(n));
    const u = o.message?.usage;
    if (!contextoInicial && o.type === 'assistant' && u) {
      contextoInicial = (u.input_tokens || 0) + (u.cache_creation_input_tokens || 0) + (u.cache_read_input_tokens || 0);
    }
  }

  const porServidor = {};
  for (const n of herramientas) {
    const srv = n.startsWith('mcp__') ? n.split('__')[1] : '(nativas de Claude Code)';
    porServidor[srv] = (porServidor[srv] || 0) + 1;
  }

  const mcp = Object.entries(porServidor).filter(([k]) => k !== '(nativas de Claude Code)');
  const totalMcp = mcp.reduce((a, [, v]) => a + v, 0);

  console.log(`\n=== Sesión ${nombre.slice(0, 8)} ===`);
  console.log(`Contexto del primer turno : ${contextoInicial.toLocaleString('es-CO')} tokens`);
  console.log(`Herramientas cargadas     : ${herramientas.size}  (${totalMcp} de conectores MCP)`);

  if (mcp.length) {
    console.log('\nConectores activos:');
    for (const [srv, n] of mcp.sort((a, b) => b[1] - a[1])) {
      console.log(`  ${srv.padEnd(36)} ${String(n).padStart(4)} herramientas`);
    }
  } else {
    console.log('\nSin conectores MCP. Este es el escenario más barato.');
  }

  console.log('\nReferencia medida el 2026-08-18 (antes de limpiar):');
  console.log('  547 herramientas, 509 de MCP, 69.005 tokens de contexto inicial.');
  if (herramientas.size < 300) console.log('  -> Vas bien: menos de la mitad del equipaje original.');
}
