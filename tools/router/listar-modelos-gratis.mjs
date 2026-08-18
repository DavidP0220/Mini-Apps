#!/usr/bin/env node
/**
 * Lista los modelos GRATUITOS disponibles hoy en OpenRouter.
 * Los IDs cambian con frecuencia, así que verifica con este script antes de
 * copiar cualquier ID a la configuración.
 *
 * Uso:  node tools/router/listar-modelos-gratis.mjs
 */
const res = await fetch('https://openrouter.ai/api/v1/models');
if (!res.ok) {
  console.error('No se pudo consultar OpenRouter:', res.status, res.statusText);
  process.exit(1);
}
const { data } = await res.json();
const gratis = data
  .filter((m) => Number(m.pricing?.prompt) === 0 && Number(m.pricing?.completion) === 0)
  .sort((a, b) => (b.context_length || 0) - (a.context_length || 0));

console.log(`${gratis.length} modelos gratuitos disponibles:\n`);
for (const m of gratis) {
  const ctx = (m.context_length || 0).toLocaleString('es-CO');
  console.log(`${m.id.padEnd(52)} ctx ${ctx.padStart(9)}  ${m.name}`);
}
console.log('\nCopia los IDs que quieras a ~/.claude-code-router/config.json');
console.log('Los modelos ":free" tienen límites de uso por día y pueden saturarse.');
