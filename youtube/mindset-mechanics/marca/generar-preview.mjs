import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import { readFileSync } from 'fs';
const av = 'data:image/png;base64,' + readFileSync('avatar.png').toString('base64');
const html = `<style>html,body{margin:0;background:#181818;font-family:Arial}
 .row{display:flex;align-items:center;gap:40px;padding:40px}
 .c{text-align:center;color:#aaa;font-size:13px}
 img{border-radius:50%;display:block;margin:0 auto 8px}
 .s32 img{width:32px;height:32px}.s48 img{width:48px;height:48px}
 .s88 img{width:88px;height:88px}.s160 img{width:160px;height:160px}</style>
 <div class="row">
  <div class="c s32"><img src="${av}">32px · comentarios</div>
  <div class="c s48"><img src="${av}">48px · búsqueda</div>
  <div class="c s88"><img src="${av}">88px · sidebar</div>
  <div class="c s160"><img src="${av}">160px · canal</div>
 </div>`;
const br = await chromium.launch();
const p = await br.newPage({viewport:{width:620,height:260},deviceScaleFactor:2});
await p.setContent(html); await p.waitForLoadState('networkidle');
await p.locator('.row').screenshot({path:'preview-tamanos.png'});
await br.close(); console.log('preview ok');
