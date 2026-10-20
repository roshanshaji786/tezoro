import art

CSS = r"""
@font-face{font-family:"Cormorant";src:url("../../proposal/source/fonts/Cormorant.ttf");font-weight:300 700;font-style:normal}
@font-face{font-family:"Cormorant";src:url("../../proposal/source/fonts/Cormorant-Italic.ttf");font-weight:300 700;font-style:italic}
@font-face{font-family:"Cinzel";src:url("../../proposal/source/fonts/Cinzel.ttf");font-weight:400 900}
:root{--ink:#1A1814;--ink2:#26231E;--ivory:#F5EFE6;--paper:#FBF8F3;--gold:#B8893E;--gold-lt:#D9B877;--muted:#6B6358;--line:#E3D8C6;--violet:#6D3BE8}
@page{size:A4;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:#777}
body{font-family:"Inter",sans-serif;color:var(--ink);font-size:10.3pt;line-height:1.55;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:210mm;height:297mm;position:relative;overflow:hidden;background:var(--paper);page-break-after:always;padding:22mm 20mm 24mm}
.page:last-child{page-break-after:auto}
.dark{background:var(--ink);color:var(--ivory)}
.abs{position:absolute}
.pattern{position:absolute;inset:0;opacity:.07}
.eyebrow{font-family:"Cinzel",serif;font-size:8.2pt;letter-spacing:.32em;text-transform:uppercase;color:var(--gold);display:flex;align-items:center;gap:10px;position:relative;z-index:2}
.eyebrow .num{font-family:"Cormorant",serif;font-size:13pt;letter-spacing:0;font-weight:600}
.eyebrow::after{content:"";flex:0 0 24mm;height:1px;background:currentColor;opacity:.6}
.dark .eyebrow{color:var(--gold-lt)}
h1{font-family:"Cormorant",serif;font-weight:500;font-size:46pt;line-height:1.0}
h2{font-family:"Cormorant",serif;font-weight:500;font-size:32pt;line-height:1.06;margin:6mm 0 4.5mm;position:relative;z-index:2}
h1 em,h2 em{font-style:italic;color:var(--gold)}
.dark h1 em,.dark h2 em{color:var(--gold-lt)}
h3{font-family:"Cormorant",serif;font-weight:600;font-size:15pt;line-height:1.2;margin-bottom:1.2mm}
.lead{font-size:11.2pt;line-height:1.65;color:#3A352E;position:relative;z-index:2}
.dark .lead{color:#D8CFC1}
.foot{position:absolute;left:20mm;right:20mm;bottom:11mm;display:flex;justify-content:space-between;align-items:center;font-size:7.4pt;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);border-top:1px solid var(--line);padding-top:3.5mm;z-index:3}
.dark .foot{border-color:#3A352E;color:#9C9284}
.foot .pg{font-family:"Cormorant",serif;font-size:11pt;letter-spacing:.05em;color:var(--gold)}
.frame{position:absolute;inset:10mm;border:1px solid rgba(184,137,62,.5);z-index:1;pointer-events:none}
.frame::after{content:"";position:absolute;inset:2.2mm;border:1px solid rgba(184,137,62,.2)}
.glow{position:absolute;border-radius:50%}
.g-gold{background:radial-gradient(circle,rgba(184,137,62,.32),rgba(184,137,62,0) 65%)}
.g-violet{background:radial-gradient(circle,rgba(109,59,232,.30),rgba(109,59,232,0) 65%)}
.g-gold-l{background:radial-gradient(circle,rgba(217,184,119,.35),rgba(217,184,119,0) 65%)}
.g-violet-l{background:radial-gradient(circle,rgba(109,59,232,.13),rgba(109,59,232,0) 65%)}

/* cover */
.cover{padding:0}
.cover .top{position:absolute;top:22mm;left:22mm;right:22mm;display:flex;justify-content:space-between;align-items:flex-start;z-index:3}
.cover .top img{height:33mm}
.cover .meta{text-align:right;font-size:7.4pt;letter-spacing:.2em;text-transform:uppercase;color:#A89D8C;line-height:2}
.cover .meta b{color:var(--gold-lt);font-weight:500}
.cover .title{position:absolute;left:22mm;top:70mm;z-index:3;width:120mm}
.cover h1{color:var(--ivory);margin-top:6mm}
.cover .art{position:absolute;right:6mm;bottom:30mm;width:128mm;z-index:2}
.cover .for{position:absolute;left:22mm;bottom:42mm;z-index:3;display:flex;gap:7mm}
.cover .for .bar{width:1px;background:var(--gold)}
.cover .label{font-size:7.4pt;letter-spacing:.3em;text-transform:uppercase;color:#A89D8C;margin-bottom:3mm}
.cover .wm{font-family:"Cinzel",serif;font-size:30pt;letter-spacing:.14em;color:var(--gold-lt);line-height:1}
.cover .sub{font-family:"Cinzel",serif;font-size:7.2pt;letter-spacing:.34em;color:#CFC4B2;margin-top:3mm;line-height:1.8;width:62mm}
.cover .client{margin-top:3mm;font-family:"Cormorant",serif;font-style:italic;font-size:14pt;color:var(--ivory)}
.cover .bottom{position:absolute;left:22mm;right:22mm;bottom:20mm;display:flex;justify-content:space-between;font-size:7.4pt;letter-spacing:.2em;text-transform:uppercase;color:#A89D8C;z-index:3}
.cover .bottom .co{font-family:"Cinzel",serif;letter-spacing:.24em;color:var(--ivory);font-size:8pt}

/* about */
.about-top{display:grid;grid-template-columns:1fr 66mm;gap:6mm;align-items:center}
.about-top .stack{width:70mm;margin-top:4mm}
.stack-legend{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm;margin:8mm 0 12mm}
.leg{display:flex;align-items:center;gap:2.5mm;font-size:7.6pt;letter-spacing:.16em;text-transform:uppercase;color:var(--muted)}
.leg i{width:4mm;height:4mm;transform:rotate(45deg);flex:0 0 4mm}
.services{display:grid;grid-template-columns:1fr 1fr;gap:5mm}
.svc{background:#fff;border:1px solid var(--line);padding:8mm 6.5mm;display:flex;gap:5mm;align-items:flex-start;box-shadow:0 10px 24px -14px rgba(59,42,16,.35);position:relative;overflow:hidden}
.svc::after{content:"";position:absolute;right:-8mm;top:-8mm;width:22mm;height:22mm;border-radius:50%;background:radial-gradient(circle at 35% 30%,rgba(217,184,119,.35),rgba(217,184,119,0) 70%)}
.svc .ic{flex:0 0 12mm;height:12mm;border-radius:50%;background:radial-gradient(circle at 35% 30%,#FFF6DA,#E3BB6C 30%,#A8772E 75%,#5E3E13);display:flex;align-items:center;justify-content:center;box-shadow:0 6px 10px -4px rgba(94,62,19,.6)}
.svc .ic svg{width:5.4mm;height:5.4mm;stroke:#1A1814;fill:none;stroke-width:1.7}
.svc h3{font-size:13.5pt;margin-bottom:1mm}
.svc p{font-size:8.9pt;color:var(--muted);margin:0;line-height:1.5}
.flags{margin-top:14mm;display:flex;gap:4mm;align-items:center;font-size:7.8pt;letter-spacing:.24em;text-transform:uppercase;color:var(--muted)}
.flags .sep{width:4px;height:4px;background:var(--gold);transform:rotate(45deg)}

/* understanding */
.und-top{display:grid;grid-template-columns:1fr 62mm;gap:6mm;align-items:center}
.und-top .medal{width:66mm}
.quote-block{position:relative;margin:10mm 0 12mm;padding:14mm 13mm 13mm;background:var(--ink);color:var(--ivory);overflow:hidden}
.quote-block .qm{position:absolute;top:-3mm;left:8mm;font-family:"Cormorant",serif;font-size:84pt;line-height:1;color:var(--gold)}
.quote-block blockquote{font-family:"Cormorant",serif;font-style:italic;font-size:25pt;line-height:1.2;padding-left:4mm;position:relative;z-index:2}
.quote-block .attr{margin-top:4mm;padding-left:4mm;font-family:"Cinzel",serif;font-size:7.8pt;letter-spacing:.3em;color:var(--gold-lt);position:relative;z-index:2}
.quote-block .orb{position:absolute;right:-6mm;top:-10mm;width:52mm;opacity:.95}
.pillars{display:grid;grid-template-columns:1fr 1fr;gap:6mm}
.pillar{background:#fff;border:1px solid var(--line);padding:8mm 7mm 8mm;position:relative;box-shadow:0 10px 24px -16px rgba(59,42,16,.35)}
.pillar .n{position:absolute;right:5mm;top:3mm;font-family:"Cormorant",serif;font-size:30pt;font-weight:500;color:#EADFCB;line-height:1}
.pillar .dia{width:3.2mm;height:3.2mm;background:var(--gold);transform:rotate(45deg);margin-bottom:3mm}
.pillar h3{font-size:16pt}
.pillar p{font-size:9.4pt;color:var(--muted);margin:0}

/* process */
.pillars-art{width:170mm;margin-top:8mm}
.step-cols{display:grid;grid-template-columns:repeat(5,1fr);gap:3mm;text-align:center;margin-top:1mm}
.step-cols h3{font-size:15pt;margin-bottom:.5mm}
.step-cols small{display:block;font-family:"Cinzel",serif;font-size:6.6pt;letter-spacing:.26em;color:var(--gold);margin-bottom:1.6mm}
.step-cols p{font-size:8.8pt;color:var(--muted);line-height:1.45}
.achieve{margin-top:14mm;background:var(--ink);color:var(--ivory);padding:9mm 10mm;position:relative;overflow:hidden}
.achieve .orbs{position:absolute;right:-2mm;bottom:-4mm;width:36mm;opacity:.9}
.achieve .eyebrow{margin-bottom:5mm;color:var(--gold-lt)}
.achieve ul{list-style:none;display:grid;grid-template-columns:1fr 1fr;gap:5mm 9mm;position:relative;z-index:2;padding-right:28mm}
.achieve li{display:flex;gap:3.5mm;font-size:9.2pt;line-height:1.5;color:#D8CFC1}
.achieve li b{color:var(--ivory);font-weight:600;display:block;font-size:10pt}
.achieve li .tick{flex:0 0 4.5mm;height:4.5mm;margin-top:.8mm;border:1px solid var(--gold);transform:rotate(45deg);position:relative}
.achieve li .tick::after{content:"";position:absolute;inset:1.1mm;background:var(--gold)}

/* colours */
.pal-row{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:6mm;margin-top:5mm}
.pal{text-align:center}
.pal .stage{height:80mm;border-radius:2mm;position:relative;display:flex;align-items:flex-end;justify-content:center;padding-bottom:2mm;overflow:hidden}
.pal .stage svg{width:52mm;position:relative;z-index:2}
.pal .stage .spot{position:absolute;width:60mm;height:60mm;left:50%;top:44%;transform:translate(-50%,-50%);border-radius:50%;background:radial-gradient(circle,rgba(255,255,255,.9),rgba(255,255,255,0) 65%)}
.pal .tag{font-family:"Cinzel",serif;font-size:7.2pt;letter-spacing:.28em;color:var(--gold);margin-top:4mm}
.pal h3{font-size:12.4pt;margin:.8mm 0 .6mm;white-space:nowrap}
.pal p{font-size:8.6pt;color:var(--muted);min-height:9mm}
.sw{display:flex;justify-content:center;gap:2mm;margin-top:2.5mm}
.sw div{display:flex;flex-direction:column;align-items:center;gap:1.2mm;font-size:6.4pt;color:var(--muted);letter-spacing:.04em}
.sw i{display:block;width:13mm;height:13mm;border-radius:50%;box-shadow:inset -3px -4px 6px rgba(0,0,0,.25),inset 3px 3px 6px rgba(255,255,255,.35),0 5px 9px -4px rgba(0,0,0,.35)}
.sw b{color:var(--ink);font-weight:600;font-size:6.6pt}
.logo-dir{margin-top:11mm;display:grid;grid-template-columns:32mm 1fr;gap:7mm;align-items:center;padding:6mm 7mm;background:#fff;border:1px solid var(--line);box-shadow:0 10px 24px -16px rgba(59,42,16,.35)}
.logo-dir svg{width:30mm}
.logo-dir h3{font-size:16pt}
.logo-dir p{font-size:9.3pt;color:var(--muted);margin:0}

/* why */
.why-hero{background:var(--ink);color:var(--ivory);margin:-22mm -20mm 0;padding:22mm 20mm 0;height:134mm;position:relative;overflow:hidden}
.why-hero .txt{width:92mm;position:relative;z-index:3}
.why-hero h2{color:var(--ivory);font-size:38pt}
.why-hero .lead{color:#D8CFC1}
.why-hero .phone{position:absolute;right:26mm;top:14mm;width:58mm;transform:rotate(-7deg);z-index:2}
.notif{position:absolute;z-index:4;background:rgba(251,248,243,.97);color:var(--ink);padding:3mm 3.6mm;border-radius:3mm;display:flex;gap:2.6mm;align-items:center;box-shadow:0 14px 26px -10px rgba(0,0,0,.6);width:56mm}
.notif .ni{flex:0 0 8mm;height:8mm;border-radius:50%;display:flex;align-items:center;justify-content:center}
.notif .ni svg{width:4.2mm;height:4.2mm;fill:none;stroke-width:1.8}
.notif b{display:block;font-size:7.8pt;line-height:1.3}
.notif span{display:block;font-size:7pt;color:var(--muted);line-height:1.35}
.why-cols{display:grid;grid-template-columns:1fr 1fr;gap:10mm;margin-top:10mm}
.why-cols h4{font-family:"Cinzel",serif;font-size:8.2pt;letter-spacing:.3em;color:var(--gold);font-weight:500;padding-bottom:3mm;margin-bottom:4.5mm;border-bottom:1px solid var(--gold)}
.why-item{margin-bottom:5mm;display:flex;gap:3.5mm}
.why-item .d{flex:0 0 3mm;height:3mm;background:var(--gold);transform:rotate(45deg);margin-top:2.6mm}
.why-item h3{font-size:14pt;margin-bottom:.5mm}
.why-item p{font-size:9pt;color:var(--muted);margin:0}
.statline{margin-top:2mm;display:flex;gap:6mm;align-items:center;padding:6mm 8mm;background:linear-gradient(90deg,#F3E8D3,#FBF8F3);border-left:3px solid var(--gold)}
.statline .big{font-family:"Cormorant",serif;font-size:30pt;color:var(--gold);line-height:1;font-weight:500;white-space:nowrap}
.statline p{margin:0;font-size:9.4pt;color:#3A352E}

/* invest */
.invest{padding:22mm 20mm 24mm}
.inv-top{display:grid;grid-template-columns:78mm 1fr;gap:2mm;align-items:center;position:relative;z-index:2}
.inv-top .lap{width:96mm;margin-right:-8mm;margin-top:2mm}
.invest h2{font-size:30pt;margin-top:5mm}
.price-card{margin-top:5mm;border:1px solid var(--gold);padding:9mm 11mm 8mm;position:relative;background:linear-gradient(180deg,rgba(43,39,33,.95),rgba(22,20,17,.95));text-align:center;z-index:2;box-shadow:0 30px 50px -25px rgba(0,0,0,.8)}
.price-card::before{content:"";position:absolute;inset:2.2mm;border:1px solid rgba(184,137,62,.28);pointer-events:none}
.badge{position:absolute;top:-4mm;left:50%;transform:translateX(-50%);background:linear-gradient(90deg,#8A6224,#E9C77E,#B8893E);color:var(--ink);font-family:"Cinzel",serif;font-size:7pt;letter-spacing:.3em;padding:1.8mm 5mm;font-weight:700;white-space:nowrap}
.kit-name{font-family:"Cinzel",serif;font-size:20pt;letter-spacing:.16em;color:var(--ivory);margin-top:1.5mm}
.kit-sub{font-family:"Cormorant",serif;font-style:italic;font-size:13pt;color:#CFC4B2;margin-top:1mm}
.price{font-family:"Cormorant",serif;font-weight:500;font-size:58pt;line-height:1;margin:3mm 0 1.5mm;color:#E2BC6E;text-shadow:0 2px 0 #7E561C,0 10px 24px rgba(184,137,62,.35)}
.price .rs{font-size:34pt;vertical-align:.55em;margin-right:1mm}
.price-note{font-size:7.6pt;letter-spacing:.26em;text-transform:uppercase;color:#A89D8C}
.incl{display:grid;grid-template-columns:repeat(3,1fr);gap:3.5mm;margin-top:6mm;text-align:left}
.inc{border:1px solid #3E392F;padding:4mm 3.6mm;display:flex;gap:3mm;align-items:center;position:relative;background:linear-gradient(135deg,rgba(255,255,255,.05),rgba(255,255,255,0))}
.inc .ic{flex:0 0 8.5mm;height:8.5mm;border-radius:50%;background:radial-gradient(circle at 35% 30%,#FFF6DA,#E3BB6C 30%,#A8772E 75%,#5E3E13);display:flex;align-items:center;justify-content:center;box-shadow:0 5px 9px -3px rgba(0,0,0,.6)}
.inc .ic svg{width:4.4mm;height:4.4mm;stroke:#1A1814;fill:none;stroke-width:1.7}
.inc span{font-size:8.6pt;color:var(--ivory);line-height:1.3;font-weight:500}
.inc .free{position:absolute;top:-2.3mm;right:3mm;background:var(--violet);color:#fff;font-size:6pt;letter-spacing:.2em;padding:.6mm 2mm;font-weight:700}
.platform{margin-top:6mm;position:relative;z-index:2}
.platform .ttl{text-align:center;font-family:"Cinzel",serif;font-size:8pt;letter-spacing:.32em;color:var(--gold-lt);margin-bottom:4mm}
.plat-grid{display:grid;grid-template-columns:repeat(5,1fr);border-top:1px solid #3A352E;border-bottom:1px solid #3A352E}
.plat{padding:3mm 2.5mm;text-align:center;border-left:1px solid #3A352E}
.plat:first-child{border-left:0}
.plat svg{width:6.5mm;height:6.5mm;stroke:var(--gold);fill:none;stroke-width:1.4;margin-bottom:1.6mm}
.plat b{display:block;font-family:"Cormorant",serif;font-size:12.5pt;font-weight:600;color:var(--ivory);line-height:1.15}
.plat small{display:block;font-size:7.3pt;color:#A89D8C;margin-top:1mm;line-height:1.4}
.closing-line{text-align:center;margin-top:4mm;font-family:"Cormorant",serif;font-style:italic;font-size:14.5pt;color:#D8CFC1;position:relative;z-index:2}
.closing-line b{font-style:normal;color:var(--gold-lt);font-weight:600}

/* contact */
.contact{padding:0}
.contact .orbs{position:absolute;inset:0;width:100%;height:100%;z-index:1}
.contact .c-inner{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 26mm;z-index:3}
.contact img{height:56mm;margin-bottom:11mm}
.contact h2{color:var(--ivory);font-size:42pt;margin:0 0 4mm}
.contact .lead{margin:0 auto 10mm;max-width:125mm;text-align:center}
.card-glass{width:120mm;padding:8mm 9mm;border:1px solid rgba(217,184,119,.45);background:linear-gradient(135deg,rgba(255,255,255,.08),rgba(255,255,255,.02));display:flex;flex-direction:column;gap:4.5mm;box-shadow:0 30px 50px -25px rgba(0,0,0,.8)}
.cline{display:flex;align-items:center;gap:4mm;font-size:12pt;color:var(--ivory);letter-spacing:.03em}
.cline .ic{flex:0 0 9mm;height:9mm;border-radius:50%;background:radial-gradient(circle at 35% 30%,#FFF6DA,#E3BB6C 30%,#A8772E 75%,#5E3E13);display:flex;align-items:center;justify-content:center}
.cline .ic svg{width:4.5mm;height:4.5mm;stroke:#1A1814;fill:none;stroke-width:1.8}
.cline small{display:block;font-size:6.8pt;letter-spacing:.28em;color:#A89D8C;text-transform:uppercase;text-align:left}
.cline div{text-align:left}
.contact .company{margin-top:12mm;font-family:"Cinzel",serif;font-size:8pt;letter-spacing:.32em;color:#A89D8C}
"""

IC = {
 "star":'<path d="M12 3l2.6 5.6L20 9.4l-4 4 1 5.6-5-2.8-5 2.8 1-5.6-4-4 5.4-.8z"/>',
 "screen":'<rect x="3" y="4" width="18" height="14" rx="1.5"/><path d="M3 8h18M8 21h8M12 18v3"/>',
 "trend":'<path d="M4 19l5-6 4 3 7-9"/><path d="M15 7h5v5"/>',
 "cloud":'<path d="M7 18a4 4 0 010-8 5.5 5.5 0 0110.6 1.5A3.3 3.3 0 0117 18z"/>',
 "palette":'<circle cx="8" cy="9" r="3.5"/><circle cx="16" cy="9" r="3.5"/><circle cx="12" cy="15.5" r="3.5"/>',
 "cube":'<path d="M12 2.5l8.5 4.8v9.4L12 21.5l-8.5-4.8V7.3z"/><path d="M3.5 7.3L12 12l8.5-4.7M12 12v9.5"/>',
 "doc":'<rect x="4" y="3" width="16" height="18" rx="1.5"/><path d="M8 8h8M8 12h8M8 16h5"/>',
 "globe":'<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 010 18M12 3a14 14 0 000 18"/>',
 "cart":'<path d="M4 6h16l-1.5 9h-13z"/><circle cx="9" cy="19" r="1.3"/><circle cx="16" cy="19" r="1.3"/>',
 "card":'<rect x="3" y="6" width="18" height="12" rx="1.5"/><path d="M3 10h18M7 14h3"/>',
 "shield":'<path d="M12 3l7 3v5c0 4.5-3 8.3-7 10-4-1.7-7-5.5-7-10V6z"/><path d="M9 12l2 2 4-4"/>',
 "pen":'<path d="M4 20l4-1 11-11-3-3L5 16z"/><path d="M14 6l3 3"/>',
 "bars":'<path d="M4 19h16M7 15v4M12 10v9M17 5v14"/>',
 "mail":'<rect x="3" y="5" width="18" height="14" rx="1.5"/><path d="M3 7l9 6 9-6"/>',
 "phone":'<path d="M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a1 1 0 01-1 1A16 16 0 014 5a1 1 0 011-1z"/>',
 "cal":'<rect x="4" y="5" width="16" height="15" rx="1.5"/><path d="M4 10h16M9 3v4M15 3v4"/>',
 "chat":'<path d="M4 5h16v11H9l-5 4z"/>',
}
def ic(name): return f'<svg viewBox="0 0 24 24">{IC[name]}</svg>'

def foot(n): return f'<div class="foot"><span>DARTS AI · Tezoro Proposal</span><span class="pg">{n:02d}</span></div>'

PATTERN = '<svg class="pattern" width="100%" height="100%"><rect width="100%" height="100%" fill="url(#lattice)"/></svg>'

pages = []

# 1 COVER
pages.append(f'''
<section class="page cover dark">
  {PATTERN}
  <div class="glow g-gold" style="width:190mm;height:190mm;right:-60mm;bottom:10mm"></div>
  <div class="glow g-violet" style="width:150mm;height:150mm;left:-70mm;top:-40mm"></div>
  <div class="frame"></div>
  <div class="top">
    <img src="logo_dark.png" alt="DARTS AI">
    <div class="meta">Quote No &nbsp;<b>DAI/TZ/2026/001</b><br>Date &nbsp;<b>20 October 2026</b></div>
  </div>
  <div class="title">
    <div class="eyebrow">Proposal &amp; Quotation</div>
    <h1>Brand Identity &amp;<br><em>Digital Presence</em><br>Proposal</h1>
  </div>
  <div class="art">{art.cover_art()}</div>
  <div class="for">
    <div class="bar"></div>
    <div>
      <div class="label">Prepared for</div>
      <div class="wm">TEZORO</div>
      <div class="sub">PREMIUM MEN'S TAILORING &amp; WEDDING ATELIER</div>
      <div class="client">Attn. Safnal · Pothencode</div>
    </div>
  </div>
  <div class="bottom"><div class="co">DARTS AI &nbsp;|&nbsp; DanRosh Tech Solutions Pvt Ltd</div><div>India · Slovenia · USA</div></div>
</section>''')

# 2 ABOUT
pages.append(f'''
<section class="page">
  <div class="glow g-gold-l" style="width:150mm;height:150mm;right:-50mm;top:-30mm"></div>
  <div class="about-top">
    <div>
      <div class="eyebrow"><span class="num">01</span> About Us</div>
      <h2>Technology that<br><em>builds brands.</em></h2>
      <p class="lead">DARTS AI is a brand of DanRosh Tech Solutions Pvt Ltd, a technology company operating across India, Slovenia and the United States. We combine design, technology and AI-driven marketing so that brands don't just look premium — they perform online.</p>
    </div>
    <div class="stack">{art.about_stack()}</div>
  </div>
  <div class="stack-legend">
    <div class="leg"><i style="background:linear-gradient(135deg,#F6E3B4,#B8893E)"></i>Brand</div>
    <div class="leg"><i style="background:#F5EFE6;border:1px solid #C9BBA2"></i>Web</div>
    <div class="leg"><i style="background:linear-gradient(135deg,#A881FF,#4C26B5)"></i>AI Marketing</div>
    <div class="leg"><i style="background:#2B2620"></i>Cloud</div>
  </div>
  <div class="eyebrow" style="margin-bottom:5mm">What We Do</div>
  <div class="services">
    <div class="svc"><div class="ic">{ic("star")}</div><div><h3>Brand Identity</h3><p>Logos, colour systems, typography and brand guides that set you apart.</p></div></div>
    <div class="svc"><div class="ic">{ic("screen")}</div><div><h3>Websites &amp; E-commerce</h3><p>Fast, mobile-first websites and online stores built to convert.</p></div></div>
    <div class="svc"><div class="ic">{ic("trend")}</div><div><h3>AI-Powered Marketing</h3><p>Targeted campaigns that reach the right customers and prove results.</p></div></div>
    <div class="svc"><div class="ic">{ic("cloud")}</div><div><h3>Cloud Hosting &amp; Support</h3><p>Secure hosting, maintenance and a team that stays with you.</p></div></div>
  </div>
  <div class="flags"><span>India</span><span class="sep"></span><span>Slovenia</span><span class="sep"></span><span>United States</span></div>
  {foot(2)}
</section>''')

# 3 UNDERSTANDING
pages.append(f'''
<section class="page">
  <div class="glow g-violet-l" style="width:140mm;height:140mm;right:-40mm;top:-20mm"></div>
  <div class="und-top">
    <div>
      <div class="eyebrow"><span class="num">02</span> Our Understanding</div>
      <h2>The idea behind<br><em>Tezoro.</em></h2>
      <p class="lead">Tezoro brings premium custom tailoring and an exclusive men's wedding floor to Pothencode — a place where every customer walks out in something made for him, and only him.</p>
    </div>
    <div class="medal">{art.medallion()}</div>
  </div>
  <div class="quote-block">
    <div class="qm">“</div>
    <blockquote>Every man deserves a look<br>that is his alone.</blockquote>
    <div class="attr">— THE TEZORO PROMISE</div>
    <div class="glow g-gold" style="width:90mm;height:90mm;right:-30mm;top:-40mm"></div>
  </div>
  <div class="pillars">
    <div class="pillar"><div class="n">01</div><div class="dia"></div><h3>One man, one look</h3><p>Every piece is tailored to his fit, his fabric and his style.</p></div>
    <div class="pillar"><div class="n">02</div><div class="dia"></div><h3>Bespoke craftsmanship</h3><p>Premium fabrics, precise measurements and expert finishing.</p></div>
    <div class="pillar"><div class="n">03</div><div class="dia"></div><h3>A men's wedding destination</h3><p>A dedicated floor for grooms, families and celebrations.</p></div>
    <div class="pillar"><div class="n">04</div><div class="dia"></div><h3>A boutique experience</h3><p>Personal attention and time with every customer.</p></div>
  </div>
  {foot(3)}
</section>''')

# 4 PROCESS
steps = [("Discover","UNDERSTAND","We understand Tezoro's customers, market and the feeling the brand should create."),
         ("Define","SHAPE","We shape the brand personality and voice around “made for you, only you.”"),
         ("Design","CREATE","We create the logo, colours, typography and 3D brand assets."),
         ("Digitise","LAUNCH","We build a website that works as Tezoro's 24/7 digital showroom."),
         ("Grow","REACH","Targeted digital marketing reaches grooms and style-conscious men.")]
cols = "".join(f'<div><h3>{a}</h3><small>{b}</small><p>{c}</p></div>' for a,b,c in steps)
orbs_small = '<svg viewBox="0 0 120 120">' + art.sphere(60,60,30,"sGold",shadow=False) + art.sphere(98,24,10,"sViolet",shadow=False) + art.ring(60,60,48,15,rot=-20,w=6) + '</svg>'
pages.append(f'''
<section class="page">
  <div class="glow g-gold-l" style="width:160mm;height:160mm;left:-60mm;top:40mm"></div>
  <div class="eyebrow"><span class="num">03</span> Our Approach</div>
  <h2>How we will build<br>the <em>Tezoro</em> brand.</h2>
  <p class="lead" style="max-width:140mm">Five steps — each one raising Tezoro higher.</p>
  <div class="pillars-art">{art.pillars()}</div>
  <div class="step-cols">{cols}</div>
  <div class="achieve">
    <div class="eyebrow">What Tezoro achieves with DARTS AI</div>
    <ul>
      <li><span class="tick"></span><div><b>Premium from day one</b>A look that justifies premium pricing.</div></li>
      <li><span class="tick"></span><div><b>Consistency everywhere</b>Store, Instagram, website, bags and tags.</div></li>
      <li><span class="tick"></span><div><b>Trust before the first visit</b>Customers check online before they walk in.</div></li>
      <li><span class="tick"></span><div><b>One partner for everything</b>Brand, web and marketing — ready to grow with Tezoro.</div></li>
    </ul>
    <div class="orbs">{orbs_small}</div>
  </div>
  {foot(4)}
</section>''')

# 5 COLOURS
pals = [
 ("A","Ivory &amp; Antique Gold","Timeless luxury for bespoke tailoring.",
  ("#FFFDF8","#E9DFCD"),("#D8CCB6","#C2B394"),"#B8893E","#2B2B2B","#B8893E",
  "radial-gradient(circle at 50% 40%,#FFFFFF,#EFE6D6 45%,#D9CCB4)",
  [("Ivory","#F5EFE6"),("Antique Gold","#B8893E"),("Charcoal","#2B2B2B")]),
 ("B","Midnight Navy &amp; Champagne","The confidence of a perfect suit.",
  ("#1E2F55","#101A33"),("#0A1226","#16213D"),"#D4B483","#D4B483","#F4F1EA",
  "radial-gradient(circle at 50% 40%,#FFFFFF,#EDE6DA 45%,#CFC5B3)",
  [("Midnight Navy","#14213D"),("Champagne","#D4B483"),("Soft White","#F4F1EA")]),
 ("C","Royal Emerald &amp; Gold","Regal and celebratory — made for the wedding floor.",
  ("#17533F","#0B2F23"),("#06231A","#0F3D2E"),"#C9A227","#C9A227","#FAF7F0",
  "radial-gradient(circle at 50% 40%,#FFFFFF,#ECE5D8 45%,#CEC4B1)",
  [("Royal Emerald","#0F3D2E"),("Gold","#C9A227"),("Cream","#FAF7F0")]),
]
pal_html = ""
for code,name,desc,front,side,acc,txt,sub,stage,sw in pals:
    sws = "".join(f'<div><i style="background:{h}"></i><b>{n}</b>{h}</div>' for n,h in sw)
    pal_html += f'''<div class="pal"><div class="stage" style="background:{stage}">{art.palette_bag("p"+code,front,side,acc,txt,sub)}</div>
      <div class="tag">OPTION {code}</div><h3>{name}</h3><p>{desc}</p><div class="sw">{sws}</div></div>'''
pages.append(f'''
<section class="page">
  <div class="eyebrow"><span class="num">04</span> Brand Colours</div>
  <h2 style="margin-bottom:3mm">Three directions.<br><em>One signature.</em></h2>
  <p class="lead">Tezoro picks one palette, and we build the full identity around it.</p>
  <div class="pal-row">{pal_html}</div>
  <div class="logo-dir">
    {art.mono3d()}
    <div><h3>Logo direction</h3><p>A minimalist serif wordmark with a subtle “T” monogram. Understated, confident and made to last — as sharp on a garment tag as on a phone screen.</p></div>
  </div>
  {foot(5)}
</section>''')

# 6 WHY
pages.append(f'''
<section class="page">
  <div class="why-hero">
    {PATTERN}
    <div class="glow g-gold" style="width:140mm;height:140mm;right:-20mm;top:-10mm"></div>
    <div class="glow g-violet" style="width:110mm;height:110mm;right:40mm;top:40mm"></div>
    <div class="txt">
      <div class="eyebrow"><span class="num">05</span> Why It Matters</div>
      <h2>Your brand is the<br><em>first fitting.</em></h2>
      <p class="lead">Before a customer feels the fabric, he judges the name, the logo and the Instagram page.</p>
    </div>
    <div class="phone">{art.phone_insta()}</div>
    <div class="notif" style="right:66mm;top:100mm;width:62mm"><div class="ni" style="background:#F1E3C4">{ic("cal").replace('<svg','<svg style="stroke:#8A6224"')}</div><div><b>New fitting booked</b><span>Wedding suit · Saturday, 11:00 AM</span></div></div>
    <div class="notif" style="right:6mm;top:56mm;width:52mm"><div class="ni" style="background:#E9E0FF">{ic("chat").replace('<svg','<svg style="stroke:#6D3BE8"')}</div><div><b>New WhatsApp enquiry</b><span>“Can I book a bespoke sherwani?”</span></div></div>
  </div>
  <div class="why-cols">
    <div>
      <h4>THE POWER OF BRANDING</h4>
      <div class="why-item"><div class="d"></div><div><h3>Premium brands earn premium prices</h3><p>Customers pay more when a brand feels exclusive and trustworthy.</p></div></div>
      <div class="why-item"><div class="d"></div><div><h3>Recognition builds loyalty</h3><p>Tezoro becomes the first name men think of for weddings.</p></div></div>
      <div class="why-item"><div class="d"></div><div><h3>A silent salesman</h3><p>Your brand works on every bag, tag and post — every day.</p></div></div>
    </div>
    <div>
      <h4>WHY DIGITAL MARKETING</h4>
      <div class="why-item"><div class="d"></div><div><h3>Customers are online first</h3><p>Men search and compare on Instagram and Google before visiting.</p></div></div>
      <div class="why-item"><div class="d"></div><div><h3>Wedding plans start early</h3><p>Digital campaigns reach grooms and families months ahead.</p></div></div>
      <div class="why-item"><div class="d"></div><div><h3>Results are measurable</h3><p>Every enquiry, visit and booking can be tracked.</p></div></div>
    </div>
  </div>
  <div class="statline"><div class="big">24 / 7</div><p><b>Online, Tezoro is open even when the shutters are down</b> — showcasing collections, answering enquiries and taking bookings around the clock.</p></div>
  {foot(6)}
</section>''')

# 7 INVEST
incl = [("screen","Premium Business Website",False),("star","Minimalist Logo Design",True),("palette","Brand Colours &amp; Typography",False),
        ("cube","3D Brand Assets &amp; Mockups",False),("doc","Professional Brand Elements",False),("globe","Domain &amp; Hosting",False)]
incl_html = "".join(f'<div class="inc">{"<div class=free>FREE</div>" if f else ""}<div class="ic">{ic(i)}</div><span>{t}</span></div>' for i,t,f in incl)
plats = [("cart","Ready to sell online","Switch on orders whenever Tezoro is ready"),("card","Secure payments","UPI, cards &amp; wallets built in"),
         ("shield","Enterprise hosting","SSL, speed &amp; high uptime"),("pen","Easy to manage","Update anytime, no coding"),("bars","Scales with you","One boutique today, many tomorrow")]
plat_html = "".join(f'<div class="plat">{ic(i)}<b>{t}</b><small>{d}</small></div>' for i,t,d in plats)
pages.append(f'''
<section class="page invest dark">
  {PATTERN}
  <div class="glow g-gold" style="width:200mm;height:200mm;left:5mm;top:60mm"></div>
  <div class="glow g-violet" style="width:120mm;height:120mm;right:-40mm;top:-30mm"></div>
  <div class="inv-top">
    <div>
      <div class="eyebrow"><span class="num">06</span> Investment</div>
      <h2>One investment.<br><em>A complete brand.</em></h2>
      <p class="lead" style="font-size:10.4pt">Everything Tezoro needs to launch as a premium brand — designed, built and hosted by one team.</p>
    </div>
    <div class="lap">{art.laptop()}</div>
  </div>
  <div class="price-card">
    <div class="badge">RECOMMENDED FOR TEZORO</div>
    <div class="kit-name">PREMIUM STARTER KIT</div>
    <div class="kit-sub">Brand identity &amp; website, ready to launch</div>
    <div class="price"><span class="rs">₹</span>25,000</div>
    <div class="price-note">One-time investment · Domain &amp; hosting included</div>
    <div class="incl">{incl_html}</div>
  </div>
  <div class="platform"><div class="ttl">BUILT ON A WORLD-CLASS PLATFORM</div><div class="plat-grid">{plat_html}</div></div>
  <div class="closing-line">One team. One investment. <b>A brand that works for Tezoro every day.</b></div>
  {foot(7)}
</section>''')

# 8 CONTACT
pages.append(f'''
<section class="page contact dark">
  {PATTERN}
  <div class="glow g-violet" style="width:190mm;height:190mm;left:10mm;top:30mm"></div>
  <div class="glow g-gold" style="width:150mm;height:150mm;right:-50mm;bottom:-40mm"></div>
  <div class="orbs">{art.orbs_contact()}</div>
  <div class="frame"></div>
  <div class="c-inner">
    <img src="logo_dark.png" alt="DARTS AI">
    <h2>Let's build <em>Tezoro</em> together.</h2>
    <p class="lead">We'd love to bring the Tezoro vision to life. Reach out and we'll get started.</p>
    <div class="card-glass">
      <div class="cline"><div class="ic">{ic("phone")}</div><div><small>Call / WhatsApp</small>+91 70120 45854</div></div>
      <div class="cline"><div class="ic">{ic("mail")}</div><div><small>Email</small>cto@dartsai.in</div></div>
      <div class="cline"><div class="ic">{ic("globe")}</div><div><small>Website</small>info.dartsai.in</div></div>
    </div>
    <div class="company">DARTS AI &nbsp;|&nbsp; DANROSH TECH SOLUTIONS PVT LTD</div>
  </div>
</section>''')

html = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Tezoro Brand Proposal — DARTS AI</title><style>{CSS}</style></head>
<body>{art.DEFS}{"".join(pages)}</body></html>'''
open("brochure_v2.html","w").write(html)
print("ok")
