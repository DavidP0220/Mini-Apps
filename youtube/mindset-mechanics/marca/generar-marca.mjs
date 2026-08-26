import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import { readFileSync } from 'fs';
// Regenerar: cp ../paquete-2026-08-23/REFERENCIA_personaje.png _src.png
// python3 -c "import base64;open('_src.b64','w').write('data:image/png;base64,'+base64.b64encode(open('_src.png','rb').read()).decode())"
const SRC = readFileSync('_src.b64','utf8');
const AMBER='#F5A93C', CREAM='#F8EAD2';

// AVATAR 800x800 — recorte cerrado: visera + cejas + ojos. Debe leerse a 32px.
// fuente 1920x760; recorte x 852..1452 (600), y 24..624 -> escala 800/600 = 1.3333
const avatar = `<style>
 html,body{margin:0}
 .a{position:relative;width:800px;height:800px;overflow:hidden;background:#0A1020}
 .bg{position:absolute;inset:-60px;background:url('${SRC}') center/cover;filter:blur(50px) brightness(.55)}
 .f{position:absolute;width:2440px;left:-1074px;top:-56px;filter:saturate(1.25) contrast(1.16) brightness(1.07)}
 .glow{position:absolute;inset:0;background:radial-gradient(circle at 50% 44%,rgba(245,169,60,.26) 0%,rgba(245,169,60,0) 60%)}
 .vig{position:absolute;inset:0;background:radial-gradient(circle at 50% 46%,rgba(0,0,0,0) 50%,rgba(0,0,0,.68) 100%)}
</style>
<div class="a"><div class="bg"></div><img class="f" src="${SRC}"><div class="glow"></div><div class="vig"></div></div>`;

// BANNER 2560x1440 — zona segura movil 1546x423 centrada: x 507..2053, y 508..931
const banner = `<style>
 html,body{margin:0}
 .b{position:relative;width:2560px;height:1440px;overflow:hidden;background:#080D18}
 .bg{position:absolute;inset:-80px;background:url('${SRC}') center/cover;filter:blur(80px) brightness(.62) saturate(1.15)}
 .f{position:absolute;left:652px;top:387px;width:2000px;filter:saturate(1.20) contrast(1.12) brightness(1.05);
    -webkit-mask-image:radial-gradient(ellipse 52% 54% at 58% 47%,#000 30%,rgba(0,0,0,.85) 62%,transparent 96%);
    mask-image:radial-gradient(ellipse 52% 54% at 58% 47%,#000 30%,rgba(0,0,0,.85) 62%,transparent 96%)}
 .warm{position:absolute;inset:0;background:radial-gradient(ellipse 1300px 800px at 72% 56%,rgba(245,169,60,.16) 0%,rgba(245,169,60,0) 64%)}
 .fade{position:absolute;inset:0;background:linear-gradient(to right,rgba(6,10,20,.97) 0%,rgba(6,10,20,.93) 22%,rgba(6,10,20,.55) 40%,rgba(6,10,20,0) 56%)}
 .vig{position:absolute;inset:0;background:radial-gradient(ellipse 1600px 950px at 50% 50%,rgba(0,0,0,0) 58%,rgba(0,0,0,.62) 100%)}
 .txt{position:absolute;left:520px;top:508px;width:1180px;height:423px;display:flex;flex-direction:column;justify-content:center}
 h1{margin:0;font:900 142px/0.90 'Arial Black',Helvetica,sans-serif;letter-spacing:-3px;color:${CREAM};text-shadow:0 8px 46px rgba(0,0,0,.92)}
 .rule{width:128px;height:9px;background:${AMBER};border-radius:5px;margin:28px 0 22px;box-shadow:0 0 30px ${AMBER}cc}
 p{margin:0;font:700 43px/1.3 Verdana,Geneva,sans-serif;color:#E4EBF4;text-shadow:0 3px 26px rgba(0,0,0,.95)}
 .s{margin-top:18px;font:700 29px/1 Verdana,sans-serif;color:${AMBER};letter-spacing:3.5px;text-shadow:0 2px 18px rgba(0,0,0,.9)}
</style>
<div class="b"><div class="bg"></div><img class="f" src="${SRC}"><div class="warm"></div><div class="fade"></div><div class="vig"></div>
 <div class="txt"><h1>MENTAL<br>MECHANICS</h1><div class="rule"></div>
 <p>You&rsquo;re not broken. You&rsquo;re running old code.</p><div class="s">NEW VIDEO EVERY 4 DAYS</div></div></div>`;

const br = await chromium.launch();
for (const [html,sel,out,w,h] of [[avatar,'.a','avatar.png',800,800],[banner,'.b','banner.png',2560,1440]]) {
  const p = await br.newPage({viewport:{width:w,height:h},deviceScaleFactor:1});
  await p.setContent(html); await p.waitForLoadState('networkidle');
  await p.locator(sel).screenshot({path:out}); console.log(out,'ok'); await p.close();
}
await br.close();
