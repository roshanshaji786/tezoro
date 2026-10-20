"""Tezoro proposal v4 — deck-style landscape (template concept) in v1's charcoal / ivory / gold look."""

CSS = r"""
@font-face{font-family:"Cormorant";src:url("../../proposal/source/fonts/Cormorant.ttf");font-weight:300 700;font-style:normal}
@font-face{font-family:"Cormorant";src:url("../../proposal/source/fonts/Cormorant-Italic.ttf");font-weight:300 700;font-style:italic}
@font-face{font-family:"Cinzel";src:url("../../proposal/source/fonts/Cinzel.ttf");font-weight:400 900}
:root{--ink:#1A1814;--ink2:#26231E;--ivory:#F5EFE6;--paper:#F7F2EA;--gold:#B8893E;--gold-lt:#D9B877;--muted:#6B6358;--muted-d:#A89D8C;--line:rgba(26,24,20,.14);--line-d:rgba(245,239,230,.16)}
@page{size:338.667mm 190.5mm;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:#777}
body{font-family:"Inter",sans-serif;font-size:9.2pt;line-height:1.55;color:var(--ink);-webkit-print-color-adjust:exact;print-color-adjust:exact}
.s{width:338.667mm;height:190.5mm;position:relative;overflow:hidden;page-break-after:always}
.s:last-child{page-break-after:auto}
.abs{position:absolute}

/* mesh backgrounds */
.light{background:#F5EFE6}
.m1{background:
  radial-gradient(55% 85% at 102% 105%, rgba(184,137,62,.55), rgba(184,137,62,0) 70%),
  radial-gradient(45% 70% at 85% 95%, rgba(226,186,160,.75), rgba(226,186,160,0) 70%),
  radial-gradient(60% 80% at 0% 0%, rgba(255,255,255,.95), rgba(255,255,255,0) 70%),
  linear-gradient(135deg,#F7F2EA 0%,#F1E7DA 55%,#ECDCC6 100%)}
.m2{background:
  radial-gradient(50% 80% at -2% -5%, rgba(184,137,62,.45), rgba(184,137,62,0) 70%),
  radial-gradient(45% 70% at 18% 8%, rgba(230,196,170,.7), rgba(230,196,170,0) 70%),
  radial-gradient(60% 90% at 100% 100%, rgba(255,255,255,.9), rgba(255,255,255,0) 70%),
  linear-gradient(135deg,#EFE3D2 0%,#F4ECE1 45%,#F8F4EE 100%)}
.m3{background:
  radial-gradient(50% 80% at 102% -5%, rgba(184,137,62,.5), rgba(184,137,62,0) 70%),
  radial-gradient(45% 70% at 80% 5%, rgba(228,192,166,.7), rgba(228,192,166,0) 70%),
  radial-gradient(55% 80% at 0% 100%, rgba(255,255,255,.95), rgba(255,255,255,0) 70%),
  linear-gradient(225deg,#EEE1CE 0%,#F4ECE1 50%,#F8F4EE 100%)}
.dark{color:var(--ivory);background:
  radial-gradient(55% 90% at 104% 108%, rgba(184,137,62,.55), rgba(184,137,62,0) 70%),
  radial-gradient(40% 70% at 88% 100%, rgba(196,140,110,.35), rgba(196,140,110,0) 70%),
  radial-gradient(50% 80% at -5% -10%, rgba(92,66,38,.55), rgba(92,66,38,0) 70%),
  #1A1814}
.dark.d2{background:
  radial-gradient(55% 90% at -4% 108%, rgba(184,137,62,.5), rgba(184,137,62,0) 70%),
  radial-gradient(40% 70% at 12% 100%, rgba(196,140,110,.3), rgba(196,140,110,0) 70%),
  radial-gradient(50% 80% at 105% -10%, rgba(92,66,38,.55), rgba(92,66,38,0) 70%),
  #1A1814}

/* top bar */
.bar{position:absolute;top:9mm;left:14mm;right:14mm;display:flex;justify-content:space-between;font-size:6.6pt;letter-spacing:.24em;text-transform:uppercase;font-weight:600;color:var(--ink);z-index:5}
.dark .bar{color:var(--ivory)}
.bar span:last-child{font-weight:500}
.pg{position:absolute;right:14mm;bottom:8mm;font-family:"Cormorant";font-size:10pt;color:var(--gold);z-index:5}
.dark .pg{color:var(--gold-lt)}

/* type */
h1{font-family:"Cormorant";font-weight:500;font-size:50pt;line-height:.98;letter-spacing:-.005em}
h1 .l2{display:block;font-style:italic;color:var(--gold)}
.dark h1 .l2{color:var(--gold-lt)}
h1.xl{font-size:62pt}
h1.md{font-size:42pt}
h3{font-family:"Cormorant";font-weight:600;font-size:14pt;line-height:1.2}
.eyebrow{font-family:"Cinzel";font-size:7.4pt;letter-spacing:.32em;color:var(--gold);text-transform:uppercase}
.dark .eyebrow{color:var(--gold-lt)}
.small{font-size:8.6pt;line-height:1.6;color:var(--muted)}
.dark .small{color:var(--muted-d)}
.lead{font-size:10.4pt;line-height:1.6;color:#3A352E}
.dark .lead{color:#D8CFC1}
.num{font-family:"Cormorant";font-weight:500;line-height:1;color:var(--gold)}
.dark .num{color:var(--gold-lt)}
.arr{display:inline-block;width:8mm;height:8mm;color:var(--ink)}
.dark .arr{color:var(--ivory)}
.arr svg{width:100%;height:100%;fill:none;stroke:currentColor;stroke-width:1.1}
.rule{height:1px;background:var(--line)}
.dark .rule{background:var(--line-d)}

/* contents */
.toc{position:absolute;left:182mm;right:14mm;top:34mm}
.toc .row{display:grid;grid-template-columns:12mm 1fr 10mm;align-items:baseline;padding:3.1mm 0;border-bottom:1px solid var(--line)}
.toc .row:first-child{border-top:1px solid var(--line)}
.toc .row b{font-family:"Cormorant";font-weight:600;font-size:11pt;color:var(--gold)}
.toc .row span{font-family:"Cormorant";font-size:15pt;font-weight:500}
.toc .row i{font-style:normal;text-align:right;font-size:7.6pt;letter-spacing:.14em;color:var(--muted)}

/* about */
.svc-grid{display:grid;grid-template-columns:1fr 1fr;gap:0;border:1px solid var(--line-d);background:rgba(255,255,255,.03)}
.svc-grid > div{padding:5mm 6mm;border-right:1px solid var(--line-d);border-bottom:1px solid var(--line-d)}
.svc-grid > div:nth-child(2n){border-right:0}
.svc-grid > div:nth-child(n+3){border-bottom:0}
.svc-grid h3{font-size:13pt;margin:1mm 0 .8mm}
.svc-grid p{font-size:8.2pt;color:var(--muted-d);line-height:1.5}
.svc-grid .k{font-family:"Cinzel";font-size:6.6pt;letter-spacing:.28em;color:var(--gold-lt)}

/* pillars */
.p2{display:grid;grid-template-columns:1fr 1fr;column-gap:9mm}
.p2 > div{padding:4.2mm 0;border-top:1px solid var(--line)}
.p2 h3{font-size:13.5pt;margin-bottom:.8mm}
.p2 p{font-size:8.4pt;color:var(--muted);line-height:1.5}
.p2 .k{font-family:"Cormorant";font-weight:600;font-size:10pt;color:var(--gold)}

/* arc steps */
.step{position:absolute;width:56mm}
.step .k{font-family:"Cinzel";font-size:6.6pt;letter-spacing:.28em;color:var(--gold)}
.step h3{font-size:17pt;margin:.6mm 0 .8mm}
.step p{font-size:8.4pt;color:var(--muted);line-height:1.5}

/* achieve */
.ach{position:absolute;left:14mm;right:14mm;bottom:20mm;display:grid;grid-template-columns:repeat(4,1fr);gap:8mm}
.ach > div{border-top:1px solid var(--line-d);padding-top:5mm}
.ach .num{font-size:46pt;margin-bottom:3mm;display:block}
.ach h3{font-size:15pt;margin-bottom:1mm}
.ach p{font-size:8.6pt;color:var(--muted-d);line-height:1.55}

/* colours */
.pals{position:absolute;left:14mm;right:14mm;bottom:15mm;display:grid;grid-template-columns:repeat(4,1fr);gap:6mm}
.pal .tile{height:44mm;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2mm;position:relative;box-shadow:0 14px 26px -18px rgba(40,28,10,.6)}
.pal .tile b{font-family:"Cormorant";font-weight:600;font-size:19pt;letter-spacing:.24em;padding-left:.24em;line-height:1}
.pal .tile .ln{width:16mm;height:1px}
.pal .tile i{font-style:normal;font-family:"Inter";font-weight:500;font-size:5pt;letter-spacing:.6em;padding-left:.6em}
.pal .tile .new{position:absolute;top:3mm;right:3mm;font-family:"Inter";font-size:5.4pt;font-weight:700;letter-spacing:.2em;padding:.7mm 1.8mm;border:1px solid currentColor}
.pal .strip{display:grid;grid-template-columns:repeat(3,1fr);height:9mm}
.pal .meta{display:grid;grid-template-columns:repeat(3,1fr);margin-top:1.6mm}
.pal .meta span{font-size:6.2pt;color:var(--muted);line-height:1.35}
.pal .meta span b{display:block;color:var(--ink);font-weight:600;font-size:6.4pt}
.pal .opt{margin-top:3.5mm;font-family:"Cinzel";font-size:6.6pt;letter-spacing:.28em;color:var(--gold)}
.pal h3{font-size:14pt;margin:.6mm 0 .4mm}
.pal p{font-size:8pt;color:var(--muted);line-height:1.45}

/* logo direction */
.logo-panel{position:absolute;right:14mm;top:24mm;bottom:20mm;width:170mm;background:#F5EFE6;color:var(--ink);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8mm;box-shadow:0 30px 60px -30px rgba(0,0,0,.8)}
.logo-panel .lockup{display:flex;align-items:center;gap:9mm}
.mono{width:30mm;height:30mm;border:1px solid var(--ink);display:flex;align-items:center;justify-content:center;position:relative}
.mono::after{content:"";position:absolute;inset:1.6mm;border:1px solid rgba(184,137,62,.6)}
.mono span{font-family:"Cormorant";font-weight:500;font-size:50pt;line-height:1}
.wm b{display:block;font-family:"Cormorant";font-weight:600;font-size:36pt;letter-spacing:.24em;line-height:1}
.wm .ln{width:22mm;height:1px;background:var(--gold);margin:3mm 0 2.4mm}
.wm i{font-style:normal;font-family:"Inter";font-weight:500;font-size:7pt;letter-spacing:.7em;color:var(--gold)}
.logo-panel .uses{display:flex;gap:10mm;font-size:6.6pt;letter-spacing:.24em;text-transform:uppercase;color:var(--muted)}
.logo-panel .uses span::before{content:"";display:inline-block;width:1.6mm;height:1.6mm;background:var(--gold);transform:rotate(45deg);margin-right:2mm;vertical-align:middle}

/* why */
.wcols{position:absolute;left:182mm;right:14mm;top:30mm;display:grid;grid-template-columns:1fr 1fr;gap:9mm}
.wcols .h{font-family:"Cinzel";font-size:6.8pt;letter-spacing:.28em;color:var(--gold);padding-bottom:2.4mm;border-bottom:1px solid var(--ink)}
.wcols .it{padding:3.6mm 0;border-bottom:1px solid var(--line)}
.wcols h3{font-size:12.5pt;margin-bottom:.6mm}
.wcols p{font-size:8.2pt;color:var(--muted);line-height:1.5}

/* investment */
.kit{position:absolute;right:14mm;top:26mm;bottom:20mm;width:168mm;border:1px solid rgba(217,184,119,.55);background:linear-gradient(180deg,rgba(43,39,33,.88),rgba(22,20,17,.88));padding:9mm 10mm 8mm;display:flex;flex-direction:column;box-shadow:0 30px 60px -30px rgba(0,0,0,.9)}
.kit::before{content:"";position:absolute;inset:2mm;border:1px solid rgba(184,137,62,.22);pointer-events:none}
.kit .hd{display:flex;justify-content:space-between;align-items:center;padding-bottom:4mm;border-bottom:1px solid var(--line-d)}
.kit .hd .nm{font-family:"Cormorant";font-weight:600;font-size:18pt;letter-spacing:.12em;white-space:nowrap}
.kit .tag{white-space:nowrap;font-size:5.6pt;font-weight:700;letter-spacing:.22em;color:var(--ink);background:linear-gradient(90deg,#B8893E,#E9C77E);padding:1.2mm 3mm}
.kit .ln{display:grid;grid-template-columns:1fr 32mm;gap:6mm;padding:7mm 0;border-bottom:1px solid var(--line-d)}
.kit .ln h4{font-family:"Cormorant";font-weight:600;font-size:17pt}
.kit .ln p{font-size:8.6pt;color:var(--muted-d);line-height:1.5;margin-top:.6mm}
.kit .ln .amt{text-align:right;font-family:"Cormorant";font-weight:500;font-size:22pt;color:var(--ivory)}
.kit .tot{margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end}
.kit .tot .eyebrow{margin-bottom:1.6mm}
.kit .tot .amt{font-family:"Cormorant";font-weight:500;font-size:56pt;line-height:.9;color:#E2BC6E}
.rs{font-family:"Inter";font-weight:300;font-size:.5em;vertical-align:.62em;margin-right:1mm}
.plat{position:absolute;left:14mm;width:140mm;bottom:20mm}
.plat .row{display:grid;grid-template-columns:5mm 44mm 1fr;align-items:baseline;padding:2.3mm 0;border-bottom:1px solid var(--line-d)}
.plat .row i{display:block;width:1.8mm;height:1.8mm;background:var(--gold-lt);transform:rotate(45deg)}
.plat .row b{font-family:"Cormorant";font-weight:600;font-size:12pt}
.plat .row span{font-size:8pt;color:var(--muted-d)}

/* contact */
.cgrid{position:absolute;left:14mm;right:14mm;bottom:18mm;display:grid;grid-template-columns:1fr 1fr 1fr 1.1fr;gap:8mm;border-top:1px solid var(--ink);padding-top:5mm}
.cgrid .eyebrow{margin-bottom:2mm}
.cgrid p{font-family:"Cormorant";font-weight:500;font-size:17pt;line-height:1.2}
.cgrid p.s2{font-family:"Inter";font-size:8.4pt;color:var(--muted);line-height:1.5}
"""

ARROW = '<span class="arr"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="11"/><path d="M8.6 15.4l6.8-6.8M10 8.6h5.4V14"/></svg></span>'
N = 11


def bar():
    return '<div class="bar"><span>Tezoro · Brand Proposal</span><span>2026</span></div>'


def pg(i):
    return f'<div class="pg">{i:02d} / {N:02d}</div>'


slides = []

# 1 COVER
slides.append(f'''
<section class="s m1">{bar()}
  <div class="abs" style="left:14mm;bottom:18mm;width:92mm">
    <p class="small" style="color:#4A443B">This proposal outlines a brand identity and digital presence designed to launch Tezoro as a premium, made-for-you menswear destination in Pothencode.</p>
    <div class="rule" style="margin:5mm 0 4mm;width:30mm;background:var(--gold)"></div>
    <div class="eyebrow" style="color:var(--ink);letter-spacing:.26em">Prepared for Tezoro</div>
    <div class="small" style="margin-top:1mm">Attn. Safnal · Quote DAI/TZ/2026/001 · 20 October 2026</div>
  </div>
  <div class="abs" style="left:170mm;bottom:16mm">
    <div class="eyebrow" style="margin-bottom:6mm">Proposal &amp; Quotation</div>
    <h1 class="xl">Brand Identity &amp;<span class="l2">Digital Presence</span></h1>
  </div>
  {pg(1)}
</section>''')

# 2 CONTENTS
toc = [("About DARTS AI", 3), ("Our Understanding", 4), ("Our Approach", 5), ("What Tezoro Achieves", 6),
       ("Brand Colours", 7), ("Logo Direction", 8), ("Why It Matters", 9), ("Investment", 10), ("Contact", 11)]
toc_html = "".join(f'<div class="row"><b>{i+1:02d}</b><span>{t}</span><i>P.{p:02d}</i></div>' for i, (t, p) in enumerate(toc))
slides.append(f'''
<section class="s m2">{bar()}
  <div class="abs" style="left:14mm;bottom:18mm">
    <h1>Table of<span class="l2">Contents</span></h1>
  </div>
  <div class="toc">{toc_html}</div>
  {pg(2)}
</section>''')

# 3 ABOUT
slides.append(f'''
<section class="s dark">{bar()}
  <div class="abs" style="left:14mm;top:24mm;width:120mm">
    <div class="num" style="font-size:64pt">03</div>
    <div class="small" style="margin-top:2mm;width:60mm">Continents — offices in India, Slovenia and the United States.</div>
  </div>
  <div class="abs" style="left:182mm;top:24mm;right:14mm;display:flex;gap:6mm;align-items:flex-start">
    {ARROW}
    <h1 class="md">Technology that<span class="l2">builds brands.</span></h1>
  </div>
  <div class="abs" style="left:14mm;bottom:18mm;width:150mm">
    <div class="svc-grid">
      <div><div class="k">01</div><h3>Brand Identity</h3><p>Logos, colour systems, typography and brand guides.</p></div>
      <div><div class="k">02</div><h3>Websites &amp; E-commerce</h3><p>Fast, mobile-first websites and online stores.</p></div>
      <div><div class="k">03</div><h3>AI-Powered Marketing</h3><p>Targeted campaigns with measurable results.</p></div>
      <div><div class="k">04</div><h3>Cloud Hosting &amp; Support</h3><p>Secure hosting and a team that stays with you.</p></div>
    </div>
  </div>
  <div class="abs" style="left:182mm;right:14mm;bottom:18mm">
    <div class="eyebrow" style="margin-bottom:3mm">DARTS AI · DanRosh Tech Solutions Pvt Ltd</div>
    <p class="lead">DARTS AI is a brand of DanRosh Tech Solutions Pvt Ltd, a technology company operating across India, Slovenia and the United States. We combine design, technology and AI-driven marketing so that brands don't just look premium — they perform online.</p>
  </div>
  {pg(3)}
</section>''')

# 4 UNDERSTANDING
slides.append(f'''
<section class="s m3">{bar()}
  <div class="abs" style="left:14mm;top:24mm;width:118mm;display:flex;gap:5mm;align-items:flex-start">
    {ARROW}
    <p class="lead" style="margin-top:.6mm">Tezoro brings premium custom tailoring and an exclusive men's wedding floor to Pothencode — a place where every customer walks out in something made for him, and only him.</p>
  </div>
  <div class="abs" style="left:14mm;bottom:18mm">
    <div class="eyebrow" style="margin-bottom:5mm">Our Understanding</div>
    <h1>The idea behind<span class="l2">Tezoro.</span></h1>
  </div>
  <div class="abs" style="left:182mm;right:14mm;top:24mm">
    <div style="font-family:Cormorant;font-style:italic;font-size:24pt;line-height:1.15">“Every man deserves a look that is his alone.”</div>
    <div class="eyebrow" style="margin:3mm 0 9mm">— The Tezoro Promise</div>
    <div class="p2">
      <div><div class="k">01</div><h3>One man, one look</h3><p>Tailored to his fit, his fabric and his style.</p></div>
      <div><div class="k">02</div><h3>Bespoke craftsmanship</h3><p>Premium fabrics, precise measurements, expert finishing.</p></div>
      <div><div class="k">03</div><h3>A men's wedding destination</h3><p>A dedicated floor for grooms, families and celebrations.</p></div>
      <div><div class="k">04</div><h3>A boutique experience</h3><p>Personal attention and time with every customer.</p></div>
    </div>
  </div>
  {pg(4)}
</section>''')

# 5 APPROACH — arc timeline
W, H = 338.667, 190.5
# quadratic bezier in mm: P0 (-10, 150), P1 (169, 52), P2 (349, 150)
P0, P1, P2 = (-10.0, 152.0), (169.3, 50.0), (348.7, 152.0)
def qb(t):
    x = (1-t)**2*P0[0] + 2*(1-t)*t*P1[0] + t**2*P2[0]
    y = (1-t)**2*P0[1] + 2*(1-t)*t*P1[1] + t**2*P2[1]
    return x, y
steps = [("Discover", "We understand Tezoro's customers, market and the feeling the brand should create."),
         ("Define", "We shape the brand personality and voice around “made for you, only you.”"),
         ("Design", "We create the logo, colours, typography and 3D brand assets."),
         ("Digitise", "We build a website that works as Tezoro's 24/7 digital showroom."),
         ("Grow", "Targeted digital marketing reaches grooms and style-conscious men.")]
ts = [0.12, 0.31, 0.5, 0.69, 0.88]
arc_svg = (f'<svg class="abs" style="left:0;top:0" width="{W}mm" height="{H}mm" viewBox="0 0 {W} {H}">'
           f'<path d="M{P0[0]} {P0[1]} Q{P1[0]} {P1[1]} {P2[0]} {P2[1]}" fill="none" stroke="#1A1814" stroke-width=".3"/>')
step_html = ""
for i, ((name, desc), t) in enumerate(zip(steps, ts)):
    x, y = qb(t)
    last = i == len(steps) - 1
    fill = "#B8893E" if last else "#F5EFE6"
    arc_svg += f'<circle cx="{x:.2f}" cy="{y:.2f}" r="2.2" fill="{fill}" stroke="#1A1814" stroke-width=".3"/>'
    if last:
        arc_svg += f'<circle cx="{x:.2f}" cy="{y:.2f}" r="4" fill="none" stroke="#B8893E" stroke-width=".25"/>'
    if t < 0.45:
        pos = f"left:{x-4:.1f}mm;top:{y+6:.1f}mm;width:46mm"; al = "left"
    elif t > 0.55:
        pos = f"left:{x+4-46:.1f}mm;top:{y+6:.1f}mm;width:46mm"; al = "right"
    else:
        pos = f"left:{x-23:.1f}mm;top:{y+7:.1f}mm;width:46mm"; al = "center"
    step_html += (f'<div class="step" style="{pos};text-align:{al}"><div class="k">Step {i+1:02d}</div>'
                  f'<h3>{name}</h3><p>{desc}</p></div>')
arc_svg += '</svg>'
slides.append(f'''
<section class="s m1">{bar()}
  {arc_svg}
  <div class="abs" style="left:14mm;top:22mm">
    <div class="eyebrow" style="margin-bottom:4mm">Our Approach</div>
    <h1 class="md">How we will<span class="l2">build Tezoro.</span></h1>
  </div>
  <div class="abs" style="left:228mm;right:14mm;top:24mm;display:flex;gap:5mm;align-items:flex-start">
    {ARROW}<p class="small" style="margin-top:.5mm;color:#4A443B">Five steps, one team — each one raising Tezoro higher, from first insight to a brand that grows.</p>
  </div>
  {step_html}
  {pg(5)}
</section>''')

# 6 ACHIEVE
slides.append(f'''
<section class="s dark d2">{bar()}
  <div class="abs" style="left:14mm;top:22mm">
    <div class="eyebrow" style="margin-bottom:4mm">Why DARTS AI</div>
    <h1>What Tezoro<span class="l2">achieves with us.</span></h1>
  </div>
  <div class="abs" style="left:228mm;right:14mm;top:24mm;display:flex;gap:5mm;align-items:flex-start">
    {ARROW}<p class="small" style="margin-top:.5mm">Brand, website and marketing from one partner — so Tezoro grows without ever starting over.</p>
  </div>
  <div class="ach">
    <div><span class="num">01</span><h3>Premium from day one</h3><p>A look that justifies premium pricing from the very first customer.</p></div>
    <div><span class="num">02</span><h3>Consistency everywhere</h3><p>One identity across the store, Instagram, website, bags and tags.</p></div>
    <div><span class="num">03</span><h3>Trust before the first visit</h3><p>Customers check online before they walk in — Tezoro is ready for them.</p></div>
    <div><span class="num">04</span><h3>One partner for everything</h3><p>Brand, web and marketing under one roof, ready to grow with Tezoro.</p></div>
  </div>
  {pg(6)}
</section>''')

# 7 COLOURS
pals = [
    ("A", "Ivory &amp; Antique Gold", "Timeless luxury for bespoke tailoring.", "#F5EFE6", "#2B2B2B", "#B8893E",
     [("Ivory", "#F5EFE6"), ("Antique Gold", "#B8893E"), ("Charcoal", "#2B2B2B")], False),
    ("B", "Midnight Navy &amp; Champagne", "The confidence of a perfect suit.", "#14213D", "#D4B483", "#F4F1EA",
     [("Midnight Navy", "#14213D"), ("Champagne", "#D4B483"), ("Soft White", "#F4F1EA")], False),
    ("C", "Royal Emerald &amp; Gold", "Regal and celebratory — made for the wedding floor.", "#0F3D2E", "#C9A227", "#FAF7F0",
     [("Royal Emerald", "#0F3D2E"), ("Gold", "#C9A227"), ("Cream", "#FAF7F0")], False),
    ("D", "Espresso &amp; Taupe", "Quiet, tactile luxury — rich, warm and understated.", "#2E241D", "#E4D9CA", "#BFAE99",
     [("Espresso", "#2E241D"), ("Taupe", "#BFAE99"), ("Sandstone", "#E4D9CA")], True),
]
pal_html = ""
for code, name, desc, bg, fg, sub, sw, new in pals:
    strip = "".join(f'<div style="background:{h}"></div>' for _, h in sw)
    meta = "".join(f'<span><b>{n}</b>{h}</span>' for n, h in sw)
    newtag = f'<span class="new" style="color:{sub}">NEW</span>' if new else ""
    pal_html += (f'<div class="pal"><div class="tile" style="background:{bg}">{newtag}<b style="color:{fg}">TEZORO</b>'
                 f'<div class="ln" style="background:{sub}"></div><i style="color:{sub}">ATELIER</i></div>'
                 f'<div class="strip">{strip}</div><div class="meta">{meta}</div>'
                 f'<div class="opt">Option {code}</div><h3>{name}</h3><p>{desc}</p></div>')
slides.append(f'''
<section class="s m2">{bar()}
  <div class="abs" style="left:14mm;top:22mm">
    <div class="eyebrow" style="margin-bottom:4mm">Brand Colours</div>
    <h1 class="md">Four directions.<span class="l2">One signature.</span></h1>
  </div>
  <div class="abs" style="left:228mm;right:14mm;top:24mm;display:flex;gap:5mm;align-items:flex-start">
    {ARROW}<p class="small" style="margin-top:.5mm;color:#4A443B">Tezoro picks one palette, and we build the full identity — logo, website, bags and tags — around it.</p>
  </div>
  <div class="pals">{pal_html}</div>
  {pg(7)}
</section>''')

# 8 LOGO DIRECTION
slides.append(f'''
<section class="s dark">{bar()}
  <div class="abs" style="left:14mm;top:24mm;width:130mm;display:flex;gap:5mm;align-items:flex-start">
    {ARROW}<p class="lead" style="margin-top:.4mm">A minimalist serif wordmark with a subtle “T” monogram. Understated, confident and made to last — as sharp on a garment tag as on a phone screen.</p>
  </div>
  <div class="abs" style="left:14mm;bottom:18mm">
    <div class="eyebrow" style="margin-bottom:5mm">Logo Direction</div>
    <h1>Minimal<span class="l2">&amp; timeless.</span></h1>
  </div>
  <div class="logo-panel">
    <div class="lockup">
      <div class="mono"><span>T</span></div>
      <div class="wm"><b>TEZORO</b><div class="ln"></div><i>ATELIER</i></div>
    </div>
    <div class="uses"><span>Signage</span><span>Garment tags</span><span>Carry bags</span><span>Website</span><span>Instagram</span></div>
  </div>
  {pg(8)}
</section>''')

# 9 WHY
slides.append(f'''
<section class="s m3">{bar()}
  <div class="abs" style="left:14mm;top:22mm;width:150mm">
    <div class="eyebrow" style="margin-bottom:4mm">Why It Matters</div>
    <h1>Your brand is<span class="l2">the first fitting.</span></h1>
    <p class="lead" style="margin-top:6mm;width:120mm">Before a customer feels the fabric, he judges the name, the logo and the Instagram page.</p>
  </div>
  <div class="abs" style="left:14mm;bottom:18mm;width:150mm;display:flex;gap:7mm;align-items:center;border-top:1px solid var(--ink);padding-top:5mm">
    <div class="num" style="font-size:54pt">24/7</div>
    <p class="small" style="color:#3A352E"><b style="color:var(--ink)">Online, Tezoro is open even when the shutters are down</b> — showcasing collections, answering enquiries and taking bookings around the clock.</p>
  </div>
  <div class="wcols">
    <div>
      <div class="h">The power of branding</div>
      <div class="it"><h3>Premium brands earn premium prices</h3><p>Customers pay more when a brand feels exclusive and trustworthy.</p></div>
      <div class="it"><h3>Recognition builds loyalty</h3><p>Tezoro becomes the first name men think of for weddings.</p></div>
      <div class="it"><h3>A silent salesman</h3><p>Your brand works on every bag, tag and post — every day.</p></div>
    </div>
    <div>
      <div class="h">Why digital marketing</div>
      <div class="it"><h3>Customers are online first</h3><p>Men search and compare on Instagram and Google before visiting.</p></div>
      <div class="it"><h3>Wedding plans start early</h3><p>Digital campaigns reach grooms and families months ahead.</p></div>
      <div class="it"><h3>Results are measurable</h3><p>Every enquiry, visit and booking can be tracked.</p></div>
    </div>
  </div>
  {pg(9)}
</section>''')

# 10 INVESTMENT
slides.append(f'''
<section class="s dark d2">{bar()}
  <div class="abs" style="left:14mm;top:22mm;width:140mm">
    <div class="eyebrow" style="margin-bottom:4mm">Investment</div>
    <h1>One investment.<span class="l2">A complete brand.</span></h1>
    <p class="lead" style="margin-top:5mm">Everything Tezoro needs to launch as a premium brand — designed, built and hosted by one team.</p>
  </div>
  <div class="plat">
    <div class="eyebrow" style="margin-bottom:2mm">Built on a world-class platform</div>
    <div class="row"><i></i><b>Ready to sell online</b><span>Switch on orders whenever Tezoro is ready</span></div>
    <div class="row"><i></i><b>Secure payments</b><span>UPI, cards and wallets built in</span></div>
    <div class="row"><i></i><b>Enterprise hosting</b><span>SSL, speed and high uptime</span></div>
    <div class="row"><i></i><b>Easy to manage</b><span>Update anytime, no coding needed</span></div>
    <div class="row"><i></i><b>Scales with you</b><span>One boutique today, many tomorrow</span></div>
  </div>
  <div class="kit">
    <div class="hd"><div class="nm">PREMIUM STARTER KIT</div><div class="tag">RECOMMENDED FOR TEZORO</div></div>
    <div class="ln"><div><h4>Website &amp; Brand Identity</h4><p>Premium business website · Brand colours &amp; typography · 3D brand assets &amp; mockups · Professional brand elements · Domain &amp; hosting</p></div><div class="amt"><span class="rs">₹</span>25,000</div></div>
    <div class="ln"><div><h4>Logo Design</h4><p>Minimalist logo with concepts, revisions and final files for print and digital</p></div><div class="amt"><span class="rs">₹</span>3,000</div></div>
    <div class="tot">
      <div><div class="eyebrow">Total investment</div><div class="small">One-time · Domain &amp; hosting included</div></div>
      <div class="amt"><span class="rs">₹</span>28,000</div>
    </div>
  </div>
  {pg(10)}
</section>''')

# 11 CONTACT — only page with the DARTS logo
slides.append(f'''
<section class="s m1">{bar()}
  <img class="abs" src="logo_light.png" alt="DARTS AI" style="left:14mm;top:22mm;height:34mm">
  <div class="abs" style="left:170mm;top:30mm">
    <div class="eyebrow" style="margin-bottom:5mm">Thank You</div>
    <h1 class="xl">Let's build<span class="l2">Tezoro together.</span></h1>
  </div>
  <div class="cgrid">
    <div><div class="eyebrow">Phone / WhatsApp</div><p>+91 70120 45854</p></div>
    <div><div class="eyebrow">Email</div><p>cto@dartsai.in</p></div>
    <div><div class="eyebrow">Website</div><p>info.dartsai.in</p></div>
    <div><div class="eyebrow">Company</div><p class="s2">DARTS AI<br>DanRosh Tech Solutions Pvt Ltd</p></div>
  </div>
  {pg(11)}
</section>''')

html = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Tezoro Brand Proposal — DARTS AI</title>'
        f'<style>{CSS}</style></head><body>{"".join(slides)}</body></html>')
open("/home/claude/build/brochure_v4.html", "w").write(html)
print("ok", len(slides))
