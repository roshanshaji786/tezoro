// Rasterises every SVG listed in ../logo-files/manifest.json to a
// transparent PNG, 2400 px on the long side.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
(async () => {
  const root = path.join(__dirname, '..', 'logo-files');
  const items = JSON.parse(fs.readFileSync(path.join(root, 'manifest.json')));
  const b = await chromium.launch();
  const p = await b.newPage();
  for (const it of items) {
    const long = 2400;
    const w = Math.round(it.ratio >= 1 ? long : long * it.ratio);
    const h = Math.round(it.ratio >= 1 ? long / it.ratio : long);
    await p.setViewportSize({ width: w, height: h });
    const svg = fs.readFileSync(path.join(root, it.svg), 'utf8')
      .replace(/width="[\d.]+" height="[\d.]+"/, `width="${w}" height="${h}"`);
    await p.setContent(`<html><body style="margin:0;background:transparent">${svg}</body></html>`);
    const out = path.join(root, it.png);
    fs.mkdirSync(path.dirname(out), { recursive: true });
    await p.screenshot({ path: out, omitBackground: true, clip: { x: 0, y: 0, width: w, height: h } });
  }
  await b.close();
  console.log(items.length, 'PNGs');
})();
