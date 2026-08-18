#!/usr/bin/env node
/**
 * Reporte de consumo de tokens de Claude Code.
 *
 * Lee las transcripciones que Claude Code guarda en ~/.claude/projects/<proyecto>/*.jsonl
 * y resume cuántos tokens se gastaron, en qué, y cuánto costó aproximadamente.
 *
 * Uso:
 *   node tools/token-report.mjs                 # todas las sesiones de este proyecto
 *   node tools/token-report.mjs --all           # todos los proyectos
 *   node tools/token-report.mjs --top 15        # top N consumidores de contexto
 *   node tools/token-report.mjs --json          # salida en JSON
 */

import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';

// Precios aproximados en USD por millón de tokens (ajusta si cambian).
// cache_write = input x1.25 ; cache_read = input x0.10
const PRECIOS = [
  { match: /opus/i,   entrada: 15, salida: 75 },
  { match: /sonnet/i, entrada: 3,  salida: 15 },
  { match: /haiku/i,  entrada: 1,  salida: 5  },
  { match: /.*/,      entrada: 3,  salida: 15 },
];

const args = process.argv.slice(2);
const flag = (n) => args.includes(n);
const valor = (n, def) => {
  const i = args.indexOf(n);
  return i >= 0 && args[i + 1] ? args[i + 1] : def;
};

const RAIZ = path.join(os.homedir(), '.claude', 'projects');
const TOP = Number(valor('--top', 10));

function slugProyecto(cwd) {
  return cwd.replace(/[/\\:]/g, '-');
}

function carpetas() {
  if (!fs.existsSync(RAIZ)) return [];
  const todas = fs.readdirSync(RAIZ).filter((d) => fs.statSync(path.join(RAIZ, d)).isDirectory());
  if (flag('--all')) return todas.map((d) => path.join(RAIZ, d));
  const objetivo = slugProyecto(process.cwd());
  const propia = todas.filter((d) => d === objetivo);
  return (propia.length ? propia : todas).map((d) => path.join(RAIZ, d));
}

function precio(modelo = '') {
  return PRECIOS.find((p) => p.match.test(modelo)) ?? PRECIOS[PRECIOS.length - 1];
}

function costo(u, modelo) {
  const p = precio(modelo);
  return (
    ((u.input_tokens || 0) * p.entrada +
      (u.cache_creation_input_tokens || 0) * p.entrada * 1.25 +
      (u.cache_read_input_tokens || 0) * p.entrada * 0.1 +
      (u.output_tokens || 0) * p.salida) /
    1_000_000
  );
}

const cero = () => ({
  input: 0, output: 0, thinking: 0, cacheWrite: 0, cacheRead: 0, costo: 0, turnos: 0,
});

function acumula(dest, u, modelo) {
  dest.input += u.input_tokens || 0;
  dest.output += u.output_tokens || 0;
  dest.thinking += u.output_tokens_details?.thinking_tokens || 0;
  dest.cacheWrite += u.cache_creation_input_tokens || 0;
  dest.cacheRead += u.cache_read_input_tokens || 0;
  dest.costo += costo(u, modelo);
  dest.turnos += 1;
}

const total = cero();
const porModelo = new Map();
const porSesion = new Map();
const porHerramienta = new Map(); // tokens estimados devueltos por cada herramienta
const turnosGrandes = [];
const vistos = new Set(); // requestId, para no contar dos veces los mensajes en streaming
const nombrePorId = new Map(); // tool_use_id -> nombre de la herramienta

function estimaTokens(texto) {
  return Math.round(texto.length / 4);
}

function textoDeContenido(c) {
  if (typeof c === 'string') return c;
  if (Array.isArray(c)) return c.map(textoDeContenido).join('');
  if (c && typeof c === 'object') return JSON.stringify(c);
  return '';
}

for (const dir of carpetas()) {
  for (const archivo of fs.readdirSync(dir).filter((f) => f.endsWith('.jsonl'))) {
    const ruta = path.join(dir, archivo);
    const sesion = archivo.replace(/\.jsonl$/, '');
    const s = porSesion.get(sesion) ?? cero();
    porSesion.set(sesion, s);

    for (const linea of fs.readFileSync(ruta, 'utf8').split('\n')) {
      if (!linea.trim()) continue;
      let o;
      try { o = JSON.parse(linea); } catch { continue; }

      // Uso real de tokens (mensajes del asistente)
      const u = o.message?.usage;
      if (o.type === 'assistant' && u) {
        const clave = o.requestId || o.message?.id || o.uuid;
        if (clave && vistos.has(clave)) continue;
        if (clave) vistos.add(clave);
        const modelo = o.message?.model || 'desconocido';
        acumula(total, u, modelo);
        acumula(s, u, modelo);
        const m = porModelo.get(modelo) ?? cero();
        acumula(m, u, modelo);
        porModelo.set(modelo, m);

        const contexto = (u.input_tokens || 0) + (u.cache_creation_input_tokens || 0) + (u.cache_read_input_tokens || 0);
        turnosGrandes.push({ sesion, ts: o.timestamp, contexto, salida: u.output_tokens || 0, modelo });
      }

      // Peso de los resultados de herramientas (aquí se esconde gran parte del gasto)
      if (o.type === 'user' && Array.isArray(o.message?.content)) {
        for (const bloque of o.message.content) {
          if (bloque?.type !== 'tool_result') continue;
          const nombre = nombrePorId.get(bloque.tool_use_id) || o.toolUseResult?.type || 'resultado';
          const t = estimaTokens(textoDeContenido(bloque.content));
          porHerramienta.set(nombre, (porHerramienta.get(nombre) || 0) + t);
        }
      }
      if (o.type === 'assistant' && Array.isArray(o.message?.content)) {
        for (const bloque of o.message.content) {
          if (bloque?.type !== 'tool_use') continue;
          if (bloque.id) nombrePorId.set(bloque.id, `resultado:${bloque.name}`);
          const t = estimaTokens(textoDeContenido(bloque.input));
          const k = `llamada:${bloque.name}`;
          porHerramienta.set(k, (porHerramienta.get(k) || 0) + t);
        }
      }

      // Herramientas MCP cargadas en el contexto (coste fijo por sesión)
      if (o.attachment?.addedNames) {
        for (const n of o.attachment.addedNames) {
          const srv = n.startsWith('mcp__') ? `MCP:${n.split('__')[1]}` : 'herramientas nativas';
          porHerramienta.set(srv, (porHerramienta.get(srv) || 0) + 0);
        }
      }
    }
  }
}

const n = (x) => x.toLocaleString('es-CO');
const usd = (x) => '$' + x.toFixed(2);

if (flag('--json')) {
  console.log(JSON.stringify({ total, porModelo: [...porModelo], porSesion: [...porSesion] }, null, 2));
  process.exit(0);
}

if (total.turnos === 0) {
  console.log('No se encontraron transcripciones en ' + RAIZ);
  console.log('Ejecuta este comando en la misma máquina donde usas Claude Code.');
  process.exit(0);
}

console.log('\n=== CONSUMO TOTAL ===');
console.log(`Turnos del asistente : ${n(total.turnos)}`);
console.log(`Entrada (fresca)     : ${n(total.input)} tokens`);
console.log(`Escritura de caché   : ${n(total.cacheWrite)} tokens   <- contexto NUEVO enviado`);
console.log(`Lectura de caché     : ${n(total.cacheRead)} tokens   <- contexto reutilizado (10x más barato)`);
console.log(`Salida               : ${n(total.output)} tokens (${n(total.thinking)} de razonamiento)`);
console.log(`Costo aproximado     : ${usd(total.costo)}`);

const contextoTotal = total.input + total.cacheWrite + total.cacheRead;
const reuso = contextoTotal ? (total.cacheRead / contextoTotal) * 100 : 0;
console.log(`Reuso de caché       : ${reuso.toFixed(1)}%  (cuanto más alto, más barato)`);

console.log('\n=== POR MODELO ===');
for (const [modelo, m] of [...porModelo].sort((a, b) => b[1].costo - a[1].costo)) {
  console.log(`${modelo.padEnd(32)} ${String(m.turnos).padStart(5)} turnos  ${usd(m.costo).padStart(9)}`);
}

console.log('\n=== POR SESIÓN ===');
for (const [sesion, s] of [...porSesion].sort((a, b) => b[1].costo - a[1].costo).slice(0, TOP)) {
  console.log(`${sesion.slice(0, 8)}  ${String(s.turnos).padStart(4)} turnos  ${usd(s.costo).padStart(9)}  ` +
    `ctx ${n(s.cacheWrite + s.cacheRead + s.input)}`);
}

const herramientas = [...porHerramienta].filter(([, v]) => v > 0).sort((a, b) => b[1] - a[1]).slice(0, TOP);
if (herramientas.length) {
  console.log('\n=== TOKENS QUE ENTRAN POR HERRAMIENTAS (estimado) ===');
  for (const [nombre, t] of herramientas) {
    console.log(`${nombre.padEnd(34)} ~${n(t)} tokens`);
  }
}

console.log('\n=== TURNOS MÁS CAROS (contexto enviado) ===');
for (const t of turnosGrandes.sort((a, b) => b.contexto - a.contexto).slice(0, TOP)) {
  console.log(`${(t.ts || '').slice(0, 19).replace('T', ' ')}  ctx ${n(t.contexto).padStart(9)}  out ${n(t.salida).padStart(6)}  ${t.modelo}`);
}

console.log('\nSugerencia: si "Escritura de caché" es mucho mayor que "Lectura de caché",');
console.log('estás reiniciando el contexto demasiado seguido (sesiones cortas, /clear frecuente,');
console.log('o demasiados servidores MCP conectados). Ver docs/OPTIMIZACION-TOKENS.md\n');
