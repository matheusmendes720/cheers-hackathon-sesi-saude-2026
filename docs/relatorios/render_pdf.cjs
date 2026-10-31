// Renderiza HTML em PDF com rodape numerado pelo proprio motor (pageNumber/totalPages).
// Uso: node render_pdf.cjs --in arq.html --out arq.pdf [--format A4] [--landscape] [--label "Texto"]
const path = require('path');
const fs = require('fs');

function loadPlaywright() {
  try { return require('playwright'); } catch (e) { /* cai para o global */ }
  const roots = [
    process.env.APPDATA ? path.join(process.env.APPDATA, 'npm', 'node_modules') : null,
    '/usr/local/lib/node_modules',
    '/usr/lib/node_modules',
  ].filter(Boolean);
  for (const r of roots) {
    try { return require(path.join(r, 'playwright')); } catch (e) { /* proximo */ }
  }
  throw new Error('playwright nao encontrado (instale com: npm install -g playwright)');
}
const { chromium } = loadPlaywright();

(async () => {
  const args = process.argv.slice(2);
  const get = (k) => { const i = args.indexOf('--' + k); return i >= 0 ? args[i + 1] : null; };
  const has = (k) => args.includes('--' + k);

  const input = get('in');
  const output = get('out');
  if (!input || !output) { console.error('uso: --in <html> --out <pdf>'); process.exit(1); }
  const format = (get('format') || 'A4').toUpperCase();
  const landscape = has('landscape');
  const label = get('label') || '';
  const wait = parseInt(get('wait') || '1200', 10);

  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file:///' + path.resolve(input).replace(/\\/g, '/'), { waitUntil: 'load' });
  await page.waitForTimeout(wait);

  const footer = `<div style="width:100%;font-family:'Segoe UI',Arial,sans-serif;font-size:8pt;color:#6B7A8C;
      padding:0 12mm;display:flex;justify-content:space-between;align-items:center;">
      <span>${label}</span>
      <span><span class="pageNumber"></span> / <span class="totalPages"></span></span>
    </div>`;

  await page.pdf({
    path: output,
    format,
    landscape,
    printBackground: true,
    displayHeaderFooter: !has('nofooter'),
    headerTemplate: '<div></div>',
    footerTemplate: footer,
    preferCSSPageSize: true,
    margin: has('nofooter')
      ? { top: '0', bottom: '0', left: '0', right: '0' }
      : { top: '14mm', bottom: '14mm', left: '12mm', right: '12mm' },
  });

  await browser.close();
  console.log(JSON.stringify({ status: 'ok', out: output, format, landscape }));
})().catch((e) => { console.error('ERRO:', e.message); process.exit(1); });
