// FACTORY SETTINGS — avatar + banner desde personaje.png (2D animado, generado con IA)
// b64: python3 -c "import base64;open('_p.b64','w').write('data:image/png;base64,'+base64.b64encode(open('personaje.png','rb').read()).decode())"
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import { readFileSync } from 'fs';
const P = readFileSync('_p.b64','utf8');
const AMBER='#FF9A2E', CREAM='#FFF3E0';

// AVATAR 800x800 — cara llenando el circulo. fuente 1280x720, escala 1.35
const avatar = `<style>html,body{margin:0}
 .a{position:relative;width:800px;height:800px;overflow:hidden;background:#050A14}
 img{position:absolute;width:1728px;left:-437px;top:-25px}
 .vig{position:absolute;inset:0;background:radial-gradient(circle at 50% 46%,rgba(0,0,0,0) 52%,rgba(5,10,20,.72) 100%)}
</style><div class="a"><img src="${P}"><div class="vig"></div></div>`;

// BANNER 2560x1440 — zona segura movil 1546x423: x 507..2053, y 508..931
const banner = `<style>html,body{margin:0}
 .b{position:relative;width:2560px;height:1440px;overflow:hidden;background:#050A14}
 .bg{position:absolute;inset:-90px;background:url('${P}') center/cover;filter:blur(85px) brightness(.5) saturate(1.15)}
 img.f{position:absolute;width:2048px;left:858px;top:224px;
   -webkit-mask-image:radial-gradient(ellipse 44% 66% at 48% 46%,#000 44%,rgba(0,0,0,.88) 72%,transparent 99%);
   mask-image:radial-gradient(ellipse 44% 66% at 48% 46%,#000 44%,rgba(0,0,0,.88) 72%,transparent 99%)}
 .fade{position:absolute;inset:0;background:linear-gradient(to right,rgba(5,10,20,.97) 0%,rgba(5,10,20,.92) 24%,rgba(5,10,20,.42) 42%,rgba(5,10,20,0) 56%)}
 .vig{position:absolute;inset:0;background:radial-gradient(ellipse 1650px 980px at 50% 50%,rgba(0,0,0,0) 56%,rgba(0,0,0,.62) 100%)}
 .txt{position:absolute;left:520px;top:508px;width:1020px;height:423px;display:flex;flex-direction:column;justify-content:center}
 h1{margin:0;font:900 148px/0.88 'Arial Black',Helvetica,sans-serif;letter-spacing:-4px;color:${CREAM};
    text-shadow:0 0 80px rgba(255,154,46,.32),0 8px 44px rgba(0,0,0,.95)}
 .rule{width:138px;height:10px;background:${AMBER};border-radius:5px;margin:30px 0 24px;box-shadow:0 0 32px ${AMBER}}
 p{margin:0;font:700 43px/1.28 Verdana,Geneva,sans-serif;color:#E8EEF6;text-shadow:0 3px 26px rgba(0,0,0,.95)}
 .s{margin-top:20px;font:700 29px/1 Verdana,sans-serif;color:${AMBER};letter-spacing:4px}
</style><div class="b"><div class="bg"></div><img class="f" src="${P}"><div class="fade"></div><div class="vig"></div>
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
