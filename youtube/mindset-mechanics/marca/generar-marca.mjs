// FACTORY SETTINGS — avatar + banner desde el arte generado con IA (_gen1.png)
// Regenerar b64:  python3 -c "import base64;open('_g1.b64','w').write('data:image/png;base64,'+base64.b64encode(open('_gen1.png','rb').read()).decode())"
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import { readFileSync } from 'fs';
const A = readFileSync('_g1.b64','utf8');
const AMBER='#FF8A1F', CREAM='#FFF3E0';

// AVATAR 800x800 — recorte cerrado al simbolo encendido. Fuente 1280x720.
// recorte 480x480 centrado en el simbolo (655,270) -> x 415, y 30 ; escala 800/480 = 1.6667
const avatar = `<style>html,body{margin:0}
 .a{position:relative;width:800px;height:800px;overflow:hidden;background:#02060E}
 img{position:absolute;width:2133px;left:-692px;top:-50px;filter:saturate(1.12) contrast(1.08)}
 .vig{position:absolute;inset:0;background:radial-gradient(circle at 50% 46%,rgba(0,0,0,0) 46%,rgba(2,6,14,.80) 100%)}
</style><div class="a"><img src="${A}"><div class="vig"></div></div>`;

// BANNER 2560x1440 — zona segura movil 1546x423 centrada: x 507..2053, y 508..931
const banner = `<style>html,body{margin:0}
 .b{position:relative;width:2560px;height:1440px;overflow:hidden;background:#02060E}
 .bg{position:absolute;inset:-90px;background:url('${A}') center/cover;filter:blur(90px) brightness(.45) saturate(1.2)}
 img.f{position:absolute;width:3000px;left:300px;top:-124px;filter:saturate(1.10) contrast(1.06);
   -webkit-mask-image:radial-gradient(ellipse 46% 60% at 50% 50%,#000 42%,rgba(0,0,0,.9) 70%,transparent 98%);
   mask-image:radial-gradient(ellipse 46% 60% at 50% 50%,#000 42%,rgba(0,0,0,.9) 70%,transparent 98%)}
 .fade{position:absolute;inset:0;background:linear-gradient(to right,rgba(2,6,14,.97) 0%,rgba(2,6,14,.93) 24%,rgba(2,6,14,.45) 42%,rgba(2,6,14,0) 55%)}
 .vig{position:absolute;inset:0;background:radial-gradient(ellipse 1650px 980px at 50% 50%,rgba(0,0,0,0) 56%,rgba(0,0,0,.66) 100%)}
 .txt{position:absolute;left:520px;top:508px;width:1000px;height:423px;display:flex;flex-direction:column;justify-content:center}
 h1{margin:0;font:900 150px/0.88 'Arial Black',Helvetica,sans-serif;letter-spacing:-4px;color:${CREAM};
    text-shadow:0 0 70px rgba(255,138,31,.35),0 8px 44px rgba(0,0,0,.95)}
 .rule{width:140px;height:10px;background:${AMBER};border-radius:5px;margin:30px 0 24px;box-shadow:0 0 34px ${AMBER}}
 p{margin:0;font:700 44px/1.28 Verdana,Geneva,sans-serif;color:#E8EEF6;text-shadow:0 3px 26px rgba(0,0,0,.95)}
 .s{margin-top:20px;font:700 29px/1 Verdana,sans-serif;color:${AMBER};letter-spacing:4px}
</style><div class="b"><div class="bg"></div><img class="f" src="${A}"><div class="fade"></div><div class="vig"></div>
 <div class="txt"><h1>FACTORY<br>SETTINGS</h1><div class="rule"></div>
 <p>Your brain shipped in 200,000 BC.<br>Nobody sent the update.</p>
 <div class="s">NEW VIDEO EVERY 4 DAYS</div></div></div>`;

const br = await chromium.launch();
for (const [h,s,o,w,ht] of [[avatar,'.a','avatar.png',800,800],[banner,'.b','banner.png',2560,1440]]) {
  const p = await br.newPage({viewport:{width:w,height:ht},deviceScaleFactor:1});
  await p.setContent(h); await p.waitForLoadState('networkidle');
  await p.locator(s).screenshot({path:o}); console.log(o,'ok'); await p.close();
}
await br.close();
