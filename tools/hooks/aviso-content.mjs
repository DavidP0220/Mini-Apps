#!/usr/bin/env node
/**
 * Hook PreToolUse: impide leer apps/<app>/content.json completo.
 *
 * Ese archivo pesa ~20 KB (~5.200 tokens) y, una vez leído, se paga en todos
 * los turnos siguientes de la sesión. Casi siempre basta con un capítulo.
 *
 * Recibe el JSON del hook por stdin y responde en stdout indicando que se use
 * tools/content.mjs. Si algo sale mal, no bloquea nada (falla en silencio).
 */

let entrada = '';
process.stdin.setEncoding('utf8');
for await (const trozo of process.stdin) entrada += trozo;

let ruta = '';
try {
  ruta = JSON.parse(entrada)?.tool_input?.file_path || '';
} catch {
  process.exit(0);
}

const normalizada = ruta.replace(/\\/g, '/');
const m = normalizada.match(/apps\/([^/]+)\/content\.json$/);
if (!m) process.exit(0);

const app = m[1];

console.log(JSON.stringify({
  hookSpecificOutput: {
    hookEventName: 'PreToolUse',
    permissionDecision: 'deny',
    permissionDecisionReason:
      `No leas apps/${app}/content.json entero: son ~5.200 tokens que se pagan en ` +
      `cada turno posterior. Usa en su lugar:\n` +
      `  node tools/content.mjs listar ${app}              (índice, ~200 tokens)\n` +
      `  node tools/content.mjs ver ${app} <capituloId>    (un capítulo, ~400 tokens)\n` +
      `  node tools/content.mjs set ${app} <capId> <n> --body "..."  (editar)\n` +
      `Si de verdad necesitas el archivo completo, léelo con Bash (cat).`,
  },
}));
