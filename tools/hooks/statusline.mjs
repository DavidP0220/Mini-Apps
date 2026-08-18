#!/usr/bin/env node
/**
 * Línea de estado: muestra modelo, contexto usado y costo de la sesión.
 *
 * Claude Code envía por stdin un JSON con datos de la sesión. Se leen de forma
 * defensiva (si un campo no está, simplemente no se muestra) y el contexto se
 * calcula desde la transcripción, que es el dato fiable.
 */

import fs from 'node:fs';

let entrada = '';
process.stdin.setEncoding('utf8');
for await (const trozo of process.stdin) entrada += trozo;

let d = {};
try { d = JSON.parse(entrada); } catch {}

const partes = [];

const modelo = d?.model?.display_name || d?.model?.id;
if (modelo) partes.push(modelo);

// Contexto: último uso registrado en la transcripción.
const transcripcion = d?.transcript_path;
if (transcripcion && fs.existsSync(transcripcion)) {
  try {
    let ctx = 0;
    for (const linea of fs.readFileSync(transcripcion, 'utf8').split('\n')) {
      if (!linea.includes('"usage"')) continue;
      let o;
      try { o = JSON.parse(linea); } catch { continue; }
      const u = o?.message?.usage;
      if (o?.type !== 'assistant' || !u) continue;
      const total = (u.input_tokens || 0) + (u.cache_creation_input_tokens || 0) + (u.cache_read_input_tokens || 0);
      if (total) ctx = total;
    }
    if (ctx) {
      // La ventana depende del modelo: se elige la estándar más pequeña que quepa.
      const ventana = [200_000, 500_000, 1_000_000].find((v) => ctx <= v) || 1_000_000;
      const pct = Math.round((ctx / ventana) * 100);
      const señal = pct >= 80 ? '!' : pct >= 50 ? '~' : '';
      partes.push(`ctx ${Math.round(ctx / 1000)}k (${pct}%)${señal}`);
    }
  } catch {}
}

const costo = d?.cost?.total_cost_usd;
if (typeof costo === 'number' && costo > 0) partes.push('$' + costo.toFixed(2));

const dir = d?.workspace?.current_dir || d?.cwd;
if (dir) partes.push(dir.split(/[/\\]/).filter(Boolean).pop());

console.log(partes.join('  |  ') || 'Mini-Apps');
