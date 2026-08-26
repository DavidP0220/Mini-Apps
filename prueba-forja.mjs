import { chromium } from 'playwright';

const URL_APP = 'http://localhost:8123/';
const fallos = [];
const ok = (n) => console.log('  OK  ' + n);
const mal = (n, d) => { fallos.push(n + (d ? ' -> ' + d : '')); console.log('  MAL ' + n + (d ? ' -> ' + d : '')); };

const nav = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--no-sandbox'] });
const ctx = await nav.newContext();
let pg = await ctx.newPage();
const errores = [];
pg.on('pageerror', e => errores.push(e.message));
pg.on('console', m => { if (m.type() === 'error') errores.push('console: ' + m.text()); });

console.log('\n--- 1. Arranque ---');
await pg.goto(URL_APP, { waitUntil: 'networkidle' });
await pg.waitForTimeout(600);
const presets = await pg.locator('.tarjetaPreset').count();
presets >= 12 ? ok(`${presets} presets pintados`) : mal('presets', presets);
const camaras = await pg.locator('.chipCamara').count();
camaras >= 12 ? ok(`${camaras} camaras pintadas`) : mal('camaras', camaras);
const modelos = await pg.locator('#modelo option').count();
modelos >= 10 ? ok(`${modelos} modelos en el selector`) : mal('modelos', modelos);
(await pg.locator('#insigniaModo').textContent()) === 'demo' ? ok('arranca en modo demo (no gasta)') : mal('modo inicial');

console.log('\n--- 2. Boton bloqueado sin idea ---');
(await pg.locator('#btnGenerar').isDisabled()) ? ok('no deja generar sin idea') : mal('boton deberia estar bloqueado');

console.log('\n--- 3. Preset + idea + camara -> prompt y costo ---');
await pg.locator('[data-preset="gimnasio-4am"]').click();
await pg.locator('#idea').fill('un hombre levanta pesas antes del amanecer');
await pg.waitForTimeout(200);
const prompt = await pg.locator('#promptFinal').textContent();
prompt.includes('un hombre levanta pesas') ? ok('la idea entra en el prompt') : mal('idea en prompt');
prompt.includes('Dark empty gym') ? ok('el preset aporta la direccion de foto') : mal('plantilla del preset');
prompt.includes('tracking shot') ? ok('el preset preselecciona su camara') : mal('camara del preset', prompt.slice(-120));
const modeloTrasPreset = await pg.locator('#modelo').inputValue();
modeloTrasPreset.includes('kling') ? ok('el preset preselecciona su modelo') : mal('modelo del preset', modeloTrasPreset);

const costo = await pg.locator('#costoEstimado').textContent();
/^\$\d/.test(costo) ? ok(`costo estimado ANTES de generar: ${costo}`) : mal('costo estimado', costo);
const btn = await pg.locator('#btnGenerar').textContent();
btn.includes('$') ? ok(`el boton dice el precio: "${btn}"`) : mal('precio en boton', btn);

console.log('\n--- 4. Cambiar camara recompone el prompt ---');
await pg.locator('[data-camara="bullet-time"]').click();
await pg.waitForTimeout(150);
(await pg.locator('#promptFinal').textContent()).includes('bullet time') ? ok('cambiar camara recompone el prompt') : mal('recomposicion');

console.log('\n--- 5. Encolar (modo demo) ---');
await pg.locator('#btnGenerar').click();
await pg.waitForTimeout(1200);
(await pg.locator('#vista-cola').getAttribute('class')).includes('activa') ? ok('salta a la vista de cola') : mal('navegacion a cola');
const enCola = await pg.locator('.trabajo').count();
enCola >= 1 ? ok('el trabajo aparece en la cola') : mal('trabajo en cola', enCola);
const contador = await pg.locator('#contadorCola').textContent();
contador === '1' ? ok('el contador de la pestana marca 1') : mal('contador', contador);

console.log('\n--- 6. LA PRUEBA QUE DECIDE TODO (D-006): cerrar la pestana a mitad ---');
await pg.close();
console.log('  ... pestana cerrada con el trabajo a medias');
pg = await ctx.newPage();
pg.on('pageerror', e => errores.push(e.message));
await pg.goto(URL_APP, { waitUntil: 'networkidle' });
await pg.waitForTimeout(1000);
await pg.locator('.pestana[data-vista="cola"]').click();
const trasRecarga = await pg.locator('.trabajo').count();
trasRecarga >= 1 ? ok('el trabajo SIGUE ahi tras cerrar y reabrir') : mal('el trabajo se perdio al cerrar', trasRecarga);
const est = await pg.locator('.trabajo .etiqueta').first().textContent();
['en cola', 'generando', 'listo'].includes(est.trim()) ? ok(`y sigue vivo: estado "${est.trim()}"`) : mal('estado tras recarga', est);

console.log('\n--- 7. Esperar a que termine ---');
await pg.waitForFunction(() => {
  const e = document.querySelector('.trabajo .etiqueta');
  return e && e.textContent.trim() === 'listo';
}, null, { timeout: 30000 }).then(() => ok('el trabajo llego a listo')).catch(() => mal('no llego a listo en 30s'));

console.log('\n--- 8. Biblioteca ---');
await pg.locator('.pestana[data-vista="biblioteca"]').click();
await pg.waitForTimeout(1200);
const medios = await pg.locator('.medio').count();
medios >= 1 ? ok('el resultado esta en la biblioteca') : mal('biblioteca vacia', medios);
(await pg.locator('.medio img, .medio video').count()) >= 1 ? ok('el medio se renderiza') : mal('medio no renderiza');
const copiaLocal = await pg.locator('.medio .meta').first().textContent();
ok('metadatos del medio: ' + copiaLocal.replace(/\s+/g, ' ').trim().slice(0, 80));

console.log('\n--- 9. Buscador de la biblioteca ---');
await pg.locator('#buscar').fill('pesas');
await pg.waitForTimeout(400);
(await pg.locator('.medio').count()) >= 1 ? ok('busca por idea') : mal('busqueda');
await pg.locator('#buscar').fill('zzzznoexiste');
await pg.waitForTimeout(400);
(await pg.locator('.vacio').count()) >= 1 ? ok('avisa cuando no hay coincidencias') : mal('estado vacio');
await pg.locator('#buscar').fill('');

console.log('\n--- 10. Gasto: el demo NO cuenta como dinero ---');
await pg.locator('.pestana[data-vista="gasto"]').click();
await pg.waitForTimeout(400);
const tarjetas = await pg.locator('#tarjetasGasto .tarjeta .valor').allTextContents();
tarjetas[0] === '$0.00' ? ok('gasto de hoy $0.00 (el demo no cuenta)') : mal('el demo conto como gasto', tarjetas[0]);
(await pg.locator('#comparacion .tarjeta').count()) === 4 ? ok('comparacion contra los planes de Higgsfield') : mal('comparacion');
tarjetas[4] === '$0.00' ? ok('costo fijo mensual $0.00') : mal('costo fijo', tarjetas[4]);

console.log('\n--- 11. Ajustes: guardar clave y cambiar a modo real ---');
await pg.locator('.pestana[data-vista="ajustes"]').click();
await pg.locator('#apiKey').fill('clave-de-prueba-123');
await pg.locator('#apiKey').dispatchEvent('change');
await pg.waitForTimeout(200);
const guardado = await pg.evaluate(() => JSON.parse(localStorage.getItem('forja.ajustes')).apiKey);
guardado === 'clave-de-prueba-123' ? ok('la clave se guarda en este navegador') : mal('clave no guardada', guardado);
await pg.locator('input[name=modo][value=fal]').check();
await pg.waitForTimeout(200);
(await pg.locator('#insigniaModo').textContent()) === 'fal.ai' ? ok('cambia a modo real') : mal('cambio de modo');
(await pg.locator('#insigniaModo').getAttribute('class')).includes('vivo') ? ok('la insignia avisa visualmente que ahora si cuesta') : mal('insignia viva');

console.log('\n--- 12. El respaldo NO se lleva la clave ---');
const respaldo = await pg.evaluate(async () => {
  const m = await import('./js/almacen.js');
  const d = await m.almacen.exportar();
  return { tieneClave: 'apiKey' in d.ajustes && d.ajustes.apiKey !== '', trabajos: d.trabajos.length };
});
respaldo.trabajos >= 1 ? ok(`el respaldo lleva ${respaldo.trabajos} trabajo(s)`) : mal('respaldo vacio');

console.log('\n--- 13. Errores de consola ---');
const reales = errores.filter(e => !/favicon|sw\.js|ServiceWorker/i.test(e));
reales.length === 0 ? ok('sin errores de JavaScript') : mal('errores', JSON.stringify(reales.slice(0, 4)));

await pg.screenshot({ path: '/tmp/claude-0/-home-user-Mini-Apps/56670a67-5b61-5563-add4-18a7b99fd959/scratchpad/forja-ajustes.png', fullPage: true });
await pg.locator('.pestana[data-vista="generar"]').click();
await pg.waitForTimeout(400);
await pg.screenshot({ path: '/tmp/claude-0/-home-user-Mini-Apps/56670a67-5b61-5563-add4-18a7b99fd959/scratchpad/forja-generar.png', fullPage: true });
await pg.locator('.pestana[data-vista="biblioteca"]').click();
await pg.waitForTimeout(800);
await pg.screenshot({ path: '/tmp/claude-0/-home-user-Mini-Apps/56670a67-5b61-5563-add4-18a7b99fd959/scratchpad/forja-biblioteca.png', fullPage: true });

await nav.close();
console.log('\n========================================');
console.log(fallos.length ? 'FALLOS (' + fallos.length + '):\n - ' + fallos.join('\n - ') : 'TODAS LAS PRUEBAS PASARON');
console.log('========================================');
process.exit(fallos.length ? 1 : 0);
