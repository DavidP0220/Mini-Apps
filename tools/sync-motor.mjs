#!/usr/bin/env node
/**
 * Propaga los cambios del motor (template/) a todas las apps de apps/.
 *
 * Sin esto, cada mejora del motor obliga a repetir la misma edición en cada
 * app: N veces el mismo trabajo y el mismo gasto de tokens. Con esto, se
 * edita template/ una vez y se sincroniza con un comando.
 *
 * Respeta lo propio de cada app: content.json, el título, el color del tema,
 * el manifest y el nombre de la caché del service worker.
 *
 * Uso:
 *   node tools/sync-motor.mjs            # muestra qué cambiaría (no escribe)
 *   node tools/sync-motor.mjs --aplicar  # aplica los cambios
 */

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const RAIZ = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const PLANTILLA = path.join(RAIZ, 'template');
const APPS = path.join(RAIZ, 'apps');
const aplicar = process.argv.includes('--aplicar');

// Archivos que son 100% motor: se copian tal cual.
const MOTOR = ['app.js', 'styles.css'];

if (!fs.existsSync(APPS)) {
  console.log('No hay carpeta apps/.');
  process.exit(0);
}

const apps = fs.readdirSync(APPS).filter((d) => fs.statSync(path.join(APPS, d)).isDirectory());
if (!apps.length) {
  console.log('No hay apps que sincronizar.');
  process.exit(0);
}

let cambios = 0;

for (const app of apps) {
  const dir = path.join(APPS, app);
  const pendientes = [];

  for (const archivo of MOTOR) {
    const origen = path.join(PLANTILLA, archivo);
    const destino = path.join(dir, archivo);
    if (!fs.existsSync(origen)) continue;
    const nuevo = fs.readFileSync(origen, 'utf8');
    const viejo = fs.existsSync(destino) ? fs.readFileSync(destino, 'utf8') : null;
    if (viejo !== nuevo) {
      pendientes.push(archivo);
      if (aplicar) fs.writeFileSync(destino, nuevo);
    }
  }

  // sw.js: se copia la lógica del motor pero se conserva el nombre de caché
  // de la app y se sube su versión, para que el navegador recargue.
  const swOrigen = path.join(PLANTILLA, 'sw.js');
  const swDestino = path.join(dir, 'sw.js');
  if (fs.existsSync(swOrigen) && fs.existsSync(swDestino)) {
    const viejo = fs.readFileSync(swDestino, 'utf8');
    const m = viejo.match(/const CACHE = '(.*?)-v(\d+)';/);
    const nombre = m ? m[1] : app;
    const version = m ? Number(m[2]) : 1;
    const cuerpoNuevo = fs.readFileSync(swOrigen, 'utf8').replace(/const CACHE = '.*?';/, '');
    const cuerpoViejo = viejo.replace(/const CACHE = '.*?';/, '');
    if (cuerpoViejo !== cuerpoNuevo) {
      pendientes.push(`sw.js (caché -> ${nombre}-v${version + 1})`);
      if (aplicar) {
        fs.writeFileSync(swDestino, fs.readFileSync(swOrigen, 'utf8')
          .replace(/const CACHE = '.*?';/, `const CACHE = '${nombre}-v${version + 1}';`));
      }
    }
  }

  if (pendientes.length) {
    cambios += pendientes.length;
    console.log(`apps/${app}`);
    for (const p of pendientes) console.log(`   ${aplicar ? 'actualizado' : 'cambiaría'}: ${p}`);
  } else {
    console.log(`apps/${app}: al día`);
  }
}

console.log('');
if (!cambios) {
  console.log('Todo sincronizado. Nada que hacer.');
} else if (aplicar) {
  console.log(`${cambios} archivo(s) actualizados. Revisa con: git diff`);
} else {
  console.log(`${cambios} archivo(s) por actualizar. Para aplicarlos:`);
  console.log('   node tools/sync-motor.mjs --aplicar');
}

console.log('\nNota: index.html y manifest.json no se tocan (llevan el título y el');
console.log('color propios de cada app). Si cambia su estructura, avísalo a mano.');
