import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';

const host = `
<svg viewBox="0 0 560 700" class="host">
 <g stroke="#141414" stroke-width="10" stroke-linejoin="round" stroke-linecap="round">
  <path d="M110 700 V560 q0-78 78-98 l72-18 72 18 q78 20 78 98 v140 Z" fill="#E9A63F"/>
  <path d="M232 452 h96 v70 h-96 Z" fill="#E3B189"/>
  <path d="M206 512 q74 52 148 0 l-18-26 q-56 36-112 0 Z" fill="#9BA4AE"/>
  <ellipse cx="280" cy="278" rx="148" ry="168" fill="#F2CDA8"/>
  <ellipse cx="132" cy="296" rx="22" ry="34" fill="#F2CDA8"/>
  <ellipse cx="428" cy="296" rx="22" ry="34" fill="#F2CDA8"/>
  <path d="M133 258 q6-146 147-148 q141 2 147 148 q-20-64-70-80 q-46 34-138 26 q-58-6-86 54 Z" fill="#46291D"/>
 </g>
 <path d="M196 232 q38-20 74-6" stroke="#46291D" stroke-width="13" fill="none" stroke-linecap="round"/>
 <path d="M290 226 q36-14 74 6" stroke="#46291D" stroke-width="13" fill="none" stroke-linecap="round"/>
 <g fill="#FFFFFF" stroke="#141414" stroke-width="8">
   <ellipse cx="228" cy="300" rx="36" ry="30"/><ellipse cx="332" cy="300" rx="36" ry="30"/>
 </g>
 <circle cx="228" cy="304" r="14" fill="#141414"/><circle cx="332" cy="304" r="14" fill="#141414"/>
 <path d="M204 282 q34-16 62-4" stroke="#141414" stroke-width="9" fill="none" stroke-linecap="round"/>
 <path d="M298 278 q30-12 60 4" stroke="#141414" stroke-width="9" fill="none" stroke-linecap="round"/>
 <path d="M278 316 q-16 40 8 46" stroke="#CE9269" stroke-width="8" fill="none" stroke-linecap="round"/>
 <path d="M238 400 q42 18 84 0" stroke="#141414" stroke-width="9" fill="none" stroke-linecap="round"/>
 <g stroke="#141414" stroke-width="10" stroke-linejoin="round" stroke-linecap="round">
   <path d="M392 620 q92-30 96-132 q4-64-54-84" fill="#E9A63F"/>
   <path d="M430 372 q54-6 62 40 q6 42-34 52 q-42 8-52-26 q-8-34 24-66 Z" fill="#F2CDA8"/>
 </g>
</svg>`;

const thumb = (lines) => `

<style>
 html,body{margin:0}
 .t{position:relative;width:1280px;height:720px;background:#FCFBF6;overflow:hidden}
 .host{position:absolute;right:-46px;bottom:-24px;height:790px}
 .bubble{position:absolute;left:40px;top:112px;width:640px;background:#FFE500;border-radius:52px;
   padding:38px 44px 46px;box-shadow:0 12px 0 rgba(0,0,0,.09)}
 .bubble div{font-family:Anton,'Arial Black',sans-serif;font-size:104px;line-height:.98;color:#0D0D0D;letter-spacing:1px}
 .arrow{position:absolute;left:600px;top:22px;width:330px;height:200px}
 .q{position:absolute;font-family:Anton,'Arial Black',sans-serif;color:#0D0D0D}
 .q1{right:104px;top:2px;font-size:100px;transform:rotate(14deg)}
 .q2{right:52px;top:60px;font-size:62px;transform:rotate(-10deg)}
</style>
<div class="t">
  ${host}
  <div class="bubble">${lines.map(l=>`<div>${l}</div>`).join('')}</div>
  <svg class="arrow" viewBox="0 0 330 200">
    <path d="M10 168 C70 46 200 8 296 52" stroke="#E01B1B" stroke-width="15" fill="none" stroke-linecap="round"/>
    <path d="M256 22 L304 54 L252 84" stroke="#E01B1B" stroke-width="15" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
  <div class="q q1">?</div><div class="q q2">?</div>
</div>`;

const TITULOS = [
  [['People Who','Apologize','For Everything'],'miniatura-01.png'],
  [['People Who',"Can't Sit","In Silence"],'miniatura-02.png'],
  [['People Who','Rehearse','Conversations'],'miniatura-03.png'],
];
const br = await chromium.launch();
const p = await br.newPage({viewport:{width:1280,height:720},deviceScaleFactor:1});
for (const [lineas,out] of TITULOS) {
  await p.setContent(thumb(lineas));
  await p.waitForLoadState('networkidle');
  await p.evaluate(()=>document.fonts.ready);
  await p.locator('.t').screenshot({path:out});
  console.log(out,'ok');
}
await br.close();
