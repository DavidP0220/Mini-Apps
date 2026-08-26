#!/usr/bin/env node
/**
 * Hook PreToolUse: impide leer de golpe los archivos caros del repo.
 *
 *   1. apps/<app>/content.json  -> usa tools/content.mjs
 *   2. human-chronicles/**.md grandes -> usa human-chronicles/tools/hc.mjs
 *
 * Esos archivos, una vez leídos, se pagan en todos los turnos siguientes de la
 * sesión. Casi siempre basta con un capítulo o una sección.
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

const negar = (razon) => {
  console.log(JSON.stringify({
    hookSpecificOutput: {
      hookEventName: 'PreToolUse',
      permissionDecision: 'deny',
      permissionDecisionReason: razon,
    },
  }));
  process.exit(0);
};

const normalizada = ruta.replace(/\\/g, '/');

// --- 1. content.json de una app ---
const app = normalizada.match(/apps\/([^/]+)\/content\.json$/)?.[1];
if (app) {
  negar(
    `No leas apps/${app}/content.json entero: son ~5.200 tokens que se pagan en ` +
    `cada turno posterior. Usa en su lugar:\n` +
    `  node tools/content.mjs listar ${app}              (índice, ~200 tokens)\n` +
    `  node tools/content.mjs ver ${app} <capituloId>    (un capítulo, ~400 tokens)\n` +
    `  node tools/content.mjs set ${app} <capId> <n> --body "..."  (editar)\n` +
    `Si de verdad necesitas el archivo completo, léelo con Bash (cat).`);
}

// --- 2. documentos grandes de Human Chronicles ---
// Leer los 39 enteros cuesta ~71.000 tokens. Casi siempre basta una sección.
const UMBRAL_BYTES = 6000;
const doc = normalizada.match(/human-chronicles\/(.+\.md)$/)?.[1];
if (doc && !/^(SINTESIS|README)\.md$/.test(doc)) {
  const { statSync } = await import('node:fs');
  let bytes = 0;
  try { bytes = statSync(ruta).size; } catch { process.exit(0); }
  if (bytes > UMBRAL_BYTES) {
    const nombre = doc.split('/').pop();
    negar(
      `No leas human-chronicles/${doc} entero: ${Math.round(bytes / 1024)} KB ` +
      `(~${Math.round(bytes / 3.8)} tokens) que se pagan en cada turno posterior. Usa:\n` +
      `  node human-chronicles/tools/hc.mjs ver ${nombre}       (índice de secciones)\n` +
      `  node human-chronicles/tools/hc.mjs ver ${nombre} <n>   (SOLO esa sección)\n` +
      `  node human-chronicles/tools/hc.mjs buscar "texto"      (grep sobre todo)\n` +
      `Empieza siempre por human-chronicles/SINTESIS.md, que sí se puede leer entero.\n` +
      `Excepción legítima: ERRORES_A_EVITAR.md se lee entero antes de trabajar en el ` +
      `canal — para eso, léelo con Bash (cat).`);
  }
}

process.exit(0);
