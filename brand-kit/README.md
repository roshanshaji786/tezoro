# Tezoro brand kit

Client-facing brand identity for Tezoro (built by DARTS AI after the proposal).

| File | What it is |
|---|---|
| `Tezoro_Brand_Guidelines.pdf` | 46-slide 16:9 brand guidelines presentation: overview, foundation, logo on four grounds, logo suite, do and don't, fabric/production specs, colour, type, patterns, icons, photography direction, mockups incl. email signature and mobile app, Tezoro Wedding sub-brand |
| `Tezoro_Company_Profile.pdf` | 10-page A4 company profile for Tezoro, in the new identity |
| `logo-files/` | Outlined SVG + transparent PNG (2400 px) for 12 logo forms in 7 colourways, app icon, profile picture, `tezoro-colours.css/json` |

Direction used (client has not chosen yet): **G · Needle button** symbol + TEZORO / ATELIER wordmark,
palette **B Midnight Navy & Champagne** with ivory, plus maroon for the wedding floor.
All colours live in `source/common.py`; change them there and rebuild to re-colour everything.

Phone: +91 96335 98100 (Mr. Safnal). Placeholders to confirm with the client: `tezoro.in`, `@tezoro.atelier`,
opening hours, "Safnal · Founder" title, sample client names/orders on mockups.

## Build
```bash
pip install fonttools          # Playwright (node) + Chromium are used for rendering
cd brand-kit/source
python3 brandkit.py && node render.js brandkit.html ../Tezoro_Brand_Guidelines.pdf 1600 900
python3 profile.py  && node render.js profile.html  ../Tezoro_Company_Profile.pdf 794 1123
python3 export.py   && node png.js                  # logo-files/
```
Add a 5th argument (a folder) to `render.js` to also get one PNG per page for visual checks.
