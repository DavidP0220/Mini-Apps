#!/usr/bin/env node
/**
 * Crea una mini-app nueva copiando el motor de `template/` sin gastar tokens.
 *
 * En vez de que Claude reescriba a mano index.html, app.js, styles.css, sw.js,
 * manifest.json e iconos (~40 KB ≈ 10.000 tokens por app), este script los copia
 * y solo deja pendiente `content.json`, que es lo único realmente nuevo.
 *
 * Uso:
 *   node tools/new-app.mjs <carpeta> --titulo "Mi App" [--corto "MiApp"] [--color "#2D6CDF"] [--fondo "#F7F6FB"]
 *
 * Ejemplo:
 *   node tools/new-app.mjs curso-ayuno --titulo "Ayuno Intermitente 21 días" --color "#E67E22"
 */

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const RAIZ = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const PLANTILLA = path.join(RAIZ, 'template');

const args = process.argv.slice(2);
const carpeta = args.find((a) => !a.startsWith('--'));
const opt = (nombre, def) => {
  const i = args.indexOf('--' + nombre);
  return i >= 0 && args[i + 1] ? args[i + 1] : def;
};

if (!carpeta) {
  console.error('Falta el nombre de la carpeta.\n' +
    'Uso: node tools/new-app.mjs <carpeta> --titulo "Mi App" [--color "#2D6CDF"]');
  process.exit(1);
}

const titulo = opt('titulo', carpeta);
const corto = opt('corto', titulo.slice(0, 12));
const color = opt('color', '#2D6CDF');
const fondo = opt('fondo', '#F7F6FB');
const destino = path.join(RAIZ, 'apps', carpeta);

if (fs.existsSync(destino)) {
  console.error(`La carpeta apps/${carpeta} ya existe. Bórrala o usa otro nombre.`);
  process.exit(1);
}

fs.cpSync(PLANTILLA, destino, { recursive: true });

const parchea = (archivo, cambios) => {
  const ruta = path.join(destino, archivo);
  let texto = fs.readFileSync(ruta, 'utf8');
  for (const [de, a] of cambios) texto = texto.replace(de, a);
  fs.writeFileSync(ruta, texto);
};

parchea('index.html', [
  [/<title>.*?<\/title>/, `<title>${titulo}</title>`],
  [/<meta name="theme-color" content="[^"]*">/, `<meta name="theme-color" content="${color}">`],
]);

const manifest = JSON.parse(fs.readFileSync(path.join(destino, 'manifest.json'), 'utf8'));
manifest.name = titulo;
manifest.short_name = corto;
manifest.theme_color = color;
manifest.background_color = fondo;
fs.writeFileSync(path.join(destino, 'manifest.json'), JSON.stringify(manifest, null, 2) + '\n');

// Cada app necesita su propio nombre de caché para no pisar a las demás en el navegador.
parchea('sw.js', [[/const CACHE = '[^']*';/, `const CACHE = '${carpeta}-v1';`]]);

// content.json queda como esqueleto: es lo único que hay que redactar.
const esqueleto = {
  meta: { id: carpeta, title: titulo, subtitle: '', author: '', themeColor: color, accentColor: color },
  chapters: [
    {
      id: 'intro',
      title: 'Introducción',
      icon: '📘',
      sections: [{ type: 'text', heading: 'Bienvenido', body: 'Pendiente de redactar.' }],
    },
  ],
};
fs.writeFileSync(path.join(destino, 'content.json'), JSON.stringify(esqueleto, null, 2) + '\n');

console.log(`Listo: apps/${carpeta}`);
console.log('Motor copiado (index.html, app.js, styles.css, sw.js, manifest.json, icons/).');
console.log('Falta solo redactar apps/' + carpeta + '/content.json con el contenido real.');
