// node render.js <page.html> <out.pdf> <width> <height> [previewDir]
// Renders the HTML to PDF and, optionally, one PNG per page for checking.
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [,, inp, out, w, h, prev] = process.argv;
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: +w, height: +h } });
  await p.goto('file://' + path.resolve(inp));
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(300);
  await p.pdf({ path: out, width: w + 'px', height: h + 'px', printBackground: true, preferCSSPageSize: true });
  if (prev) {
    const n = await p.$$eval('section', s => s.length);
    const secs = await p.$$('section');
    for (let i = 0; i < n; i++) await secs[i].screenshot({ path: path.join(prev, `p${String(i + 1).padStart(2, '0')}.png`) });
  }
  await b.close();
})();
