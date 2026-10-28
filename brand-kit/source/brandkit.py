"""Builds brandkit.html: the Tezoro brand guidelines presentation (16:9)."""
from common import *
import logos as L
import mockups as M

W, H = 1600, 900
TOTAL = []

CSS = BASE_CSS + f"""
@page{{size:{W}px {H}px;margin:0}}
.slide{{width:{W}px;height:{H}px;position:relative;overflow:hidden;page-break-after:always;break-after:page}}
.chrome{{position:absolute;left:72px;right:72px;top:44px;display:flex;justify-content:space-between;
  font-family:Cinz;font-size:11.5px;letter-spacing:.3em;text-transform:uppercase;opacity:.75;z-index:5}}
.foot{{position:absolute;left:72px;right:72px;bottom:38px;display:flex;justify-content:space-between;align-items:center;
  font-size:11px;letter-spacing:.14em;text-transform:uppercase;opacity:.55;z-index:5}}
.eyebrow{{font-family:Cinz;font-size:13px;letter-spacing:.34em;text-transform:uppercase;color:{GOLD}}}
.navy .eyebrow,.ink .eyebrow,.maroon .eyebrow{{color:{CHAMP}}}
h1{{font-family:Corm;font-weight:500;font-size:96px;line-height:.95;letter-spacing:-.01em}}
h2{{font-family:Corm;font-weight:500;font-size:62px;line-height:1.0;letter-spacing:-.005em;margin-top:14px}}
h2 em,h1 em{{color:{GOLD};font-weight:500}}
.navy h2 em,.ink h2 em,.maroon h2 em,.navy h1 em{{color:{CHAMP}}}
h3{{font-family:Cinz;font-size:14px;letter-spacing:.24em;text-transform:uppercase;font-weight:600}}
.lead{{font-size:17px;line-height:1.6;color:{MUTED};max-width:520px;margin-top:22px}}
.navy .lead,.ink .lead,.maroon .lead{{color:rgba(244,241,234,.72)}}
.small{{font-size:13px;line-height:1.55;color:{MUTED}}}
.navy .small,.ink .small,.maroon .small{{color:rgba(244,241,234,.66)}}
.tag{{font-family:Cinz;font-size:10.5px;letter-spacing:.26em;text-transform:uppercase;color:{MUTED}}}
.navy .tag,.ink .tag,.maroon .tag{{color:rgba(244,241,234,.6)}}
.pad{{position:absolute;left:72px;right:72px;top:110px;bottom:90px}}
.rule{{height:1px;background:{LINE}}}
.navy .rule,.ink .rule{{background:rgba(212,180,131,.25)}}
.card{{background:#fff;border:1px solid {LINE}}}
.num{{font-family:Corm;font-size:22px;color:{GOLD};font-style:italic}}
.shadow{{box-shadow:0 30px 60px -20px rgba(13,21,38,.45),0 10px 20px -10px rgba(13,21,38,.3)}}
.x{{position:absolute;top:10px;right:10px;width:26px;height:26px;border-radius:50%;background:{MAROON};color:#fff;
  font-size:15px;display:flex;align-items:center;justify-content:center;font-weight:600}}
.tick{{background:{NAVY}}}
.ok{{position:absolute;top:10px;right:10px;width:26px;height:26px;border-radius:50%;background:{NAVY};color:#fff;font-size:14px;display:flex;align-items:center;justify-content:center;font-weight:600;box-shadow:0 0 0 2px #fff}}
"""


def slide(content, bg='paper', section='', foot=True, chrome=True):
    n = len(TOTAL) + 1
    ch = (f'<div class="chrome"><span>Tezoro · Brand Guidelines</span><span>{section}</span></div>'
          if chrome else '')
    ft = (f'<div class="foot"><span>Made for you, only you.</span><span>{n:02d}</span></div>' if foot else '')
    TOTAL.append(f'<section class="slide {bg}">{ch}{content}{ft}</section>')


def head(eyebrow, title, lead=None, w=560):
    out = f'<div class="eyebrow">{eyebrow}</div><h2>{title}</h2>'
    if lead:
        out += f'<p class="lead" style="max-width:{w}px">{lead}</p>'
    return out


# =====================================================================
# 01 COVER
# =====================================================================
slide(f'''
<div style="position:absolute;inset:0;background:{pattern_pinstitch(CHAMP, NAVY)};opacity:.16"></div>
<div style="position:absolute;inset:0;background:radial-gradient(ellipse at 50% 45%,rgba(20,33,61,0) 0%,rgba(13,21,38,.85) 75%)"></div>
<div class="flex col center" style="position:absolute;inset:0">
  {L.inline(L.stacked, height=300, c1=IVORY, c2=CHAMP)}
  <div style="width:60px;height:1px;background:{CHAMP};margin:56px 0 26px"></div>
  <div class="caps" style="font-size:14px;color:{CHAMP}">Brand Identity Guidelines</div>
  <div class="it" style="font-size:22px;margin-top:12px;opacity:.75">Edition 01 · 2026</div>
</div>
<div class="foot" style="opacity:.5"><span>Premium Men's Tailoring &amp; Wedding Atelier · Pothencode</span><span>Confidential</span></div>
''', 'navy', chrome=False, foot=False)

# =====================================================================
# OVERVIEW
# =====================================================================
slide(f"""
<div style="position:absolute;inset:0;display:grid;grid-template-columns:1fr 1fr">
 <div class="navy" style="position:relative;display:flex;align-items:center;justify-content:center">
   <div style="position:absolute;inset:0;background:{pattern_pinstitch(CHAMP, NAVY, 22, .16)}"></div>
   <div style="position:absolute;left:72px;top:44px;font-family:Cinz;font-size:11.5px;letter-spacing:.3em;opacity:.6">TEZORO · BRAND GUIDELINES</div>
   <div style="position:relative">{L.inline(L.stacked, height=330, c1=IVORY, c2=CHAMP)}</div>
   <div style="position:absolute;left:72px;bottom:38px;font-size:11px;letter-spacing:.14em;opacity:.5">MADE FOR YOU, ONLY YOU.</div></div>
 <div class="paper" style="position:relative;padding:0 80px;display:flex;flex-direction:column;justify-content:center">
   <div class="eyebrow">Brand overview</div>
   <h2>Tezoro <em>Atelier</em></h2>
   <div class="serif it" style="font-size:30px;margin-top:12px;color:{NAVY}">Made for you, only you.</div>
   <p class="lead" style="max-width:600px">A premium men's tailoring house and wedding atelier in Pothencode, Thiruvananthapuram. Every garment is measured, cut and finished for one client, so no two men ever wear the same piece.</p>
   <div style="display:grid;grid-template-columns:1fr 1fr;gap:0 40px;margin-top:34px;border-top:1px solid {LINE}">
    {''.join(f'<div style="padding:16px 0;border-bottom:1px solid {LINE}"><div class="serif" style="font-size:26px;line-height:1">{a}</div><div class="small" style="margin-top:4px">{c}</div></div>' for a,c in [('Assured','Confident, never loud'),('Refined','Precise, never stiff'),('Personal','Warm, never casual'),('Celebratory','Festive, never flashy')])}
   </div>
   <div style="display:flex;gap:30px;align-items:center;margin-top:30px">
     <div style="display:flex">{''.join(f'<span style="width:34px;height:34px;border-radius:50%;background:{c};margin-right:-8px;border:2px solid {IVORY}"></span>' for c in [NAVY, CHAMP, IVORY, GOLD, MAROON])}</div>
     <div class="small" style="font-size:12.5px">Midnight Navy · Champagne · Soft Ivory<br>Cormorant Garamond · Cinzel · Inter</div></div>
   <div style="position:absolute;right:72px;bottom:38px;font-size:11px;letter-spacing:.14em;opacity:.5">02</div></div>
</div>""", chrome=False, foot=False)

# =====================================================================
# 02 CONTENTS
# =====================================================================
toc = [('01', 'Brand foundation', 'Story, promise, personality, voice'),
       ('02', 'Logo', 'Symbol, suite, spacing, sizes, misuse'),
       ('03', 'Fabric & production', 'Embroidery, woven, leather, engraving'),
       ('04', 'Colour', 'Palette, proportions, pairings'),
       ('05', 'Typography', 'Typefaces and hierarchy'),
       ('06', 'Graphic language', 'Patterns, icons, details, photography'),
       ('07', 'Brand in use', 'Labels, packaging, stationery, store, web, app, email'),
       ('08', 'Tezoro Wedding', 'The wedding-floor sub-brand')]
rows = ''.join(f'''<div style="display:grid;grid-template-columns:70px 1fr 1fr;align-items:baseline;padding:17px 0;border-bottom:1px solid {LINE}">
  <span class="num">{a}</span><span class="serif" style="font-size:30px">{b}</span><span class="small">{c}</span></div>''' for a, b, c in toc)
slide(f'''
<div class="pad" style="display:grid;grid-template-columns:480px 1fr;gap:90px">
  <div>{head('Contents', 'Inside <em>this guide</em>', 'Everything needed to present Tezoro the same way, every time: on a collar, a carrier bag, a shop front or a phone screen.', 400)}
  <div style="margin-top:60px">{L.inline(L.symbol, height=120, c=NAVY)}</div></div>
  <div style="border-top:1px solid {LINE}">{rows}</div>
</div>''', section='Contents')

# =====================================================================
# 03 DIVIDER
# =====================================================================
def divider(n, title, sub, bg='navy', pat=None):
    p = pat or pattern_monogram(CHAMP, NAVY if bg == 'navy' else MAROON, 70, .35)
    slide(f'''
<div style="position:absolute;right:0;top:0;bottom:0;width:760px;background:{p};opacity:.5"></div>
<div style="position:absolute;right:0;top:0;bottom:0;width:760px;background:linear-gradient(90deg,{NAVY if bg=='navy' else MAROON} 0%,rgba(0,0,0,.15) 70%)"></div>
<div style="position:absolute;right:150px;top:200px;opacity:.9">{L.inline(L.symbol, height=500, c=CHAMP)}</div>
<div style="position:absolute;left:72px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center">
  <div class="serif it" style="font-size:150px;color:{CHAMP};line-height:1">{n}</div>
  <h1 style="margin-top:10px">{title}</h1>
  <p class="lead">{sub}</p>
</div>''', bg, section=title)


divider('01', 'Brand foundation', 'Who Tezoro is, what it promises, and how it speaks.')

# =====================================================================
# 04 STORY
# =====================================================================
slide(f'''
<div class="pad" style="display:grid;grid-template-columns:1fr 1fr;gap:100px">
  <div>
    {head('The idea', 'A treasure, <em>made to measure.</em>')}
    <p class="lead">Tezoro takes its name from <i>tesoro</i>, the word for treasure. It is a premium men's tailoring house and wedding atelier in Pothencode, built on one belief: no two men should leave in the same garment.</p>
    <p class="lead" style="margin-top:14px">In a world of racks and repeats, Tezoro measures, cuts and finishes every piece for one man only. The identity is quiet, precise and confident, like a well-cut suit. It never shouts.</p>
  </div>
  <div style="display:flex;flex-direction:column;justify-content:center">
    <div class="navy" style="padding:70px 64px;position:relative">
      <div class="serif" style="font-size:120px;line-height:.5;color:{CHAMP};height:40px">“</div>
      <div class="serif" style="font-size:46px;line-height:1.12">Every man deserves a look that is <em style="color:{CHAMP}">his alone.</em></div>
      <div class="caps" style="font-size:11px;color:{CHAMP};margin-top:30px">The Tezoro promise</div>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:1px;background:{LINE};margin-top:1px">
      <div class="paper" style="padding:26px 30px"><div class="tag">Tagline</div><div class="serif it" style="font-size:28px;margin-top:6px">Made for you, only you.</div></div>
      <div class="paper" style="padding:26px 30px"><div class="tag">Short form</div><div class="serif it" style="font-size:28px;margin-top:6px">One man. One look.</div></div>
    </div>
  </div>
</div>''', section='01 · Brand foundation')

# =====================================================================
# 05 PILLARS + PERSONALITY
# =====================================================================
pillars = [('I', 'One man, one look', 'Every garment is cut for a single client. No duplicates, ever.'),
           ('II', 'Crafted by hand', 'Premium cloth, precise measurement and expert finishing.'),
           ('III', 'The wedding destination', 'A dedicated floor for grooms, families and celebrations.'),
           ('IV', 'Time for you', 'A boutique pace: personal attention at every fitting.')]
pers = [('Assured', 'not loud'), ('Refined', 'not stiff'), ('Personal', 'not casual'), ('Celebratory', 'not flashy')]
slide(f'''
<div class="pad" style="display:flex;flex-direction:column;justify-content:center">
  {head('Pillars &amp; personality', 'What we stand for.')}
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:24px;margin-top:46px">
   {''.join(f'<div style="border-top:2px solid {NAVY};padding-top:22px"><div class="num" style="font-size:30px">{a}</div><div class="serif" style="font-size:30px;margin:8px 0 10px">{b}</div><div class="small" style="font-size:14px">{c}</div></div>' for a,b,c in pillars)}
  </div>
  <div class="navy" style="margin-top:50px;padding:34px 44px;display:grid;grid-template-columns:200px repeat(4,1fr);align-items:center;gap:20px">
    <div class="caps" style="font-size:12px;color:{CHAMP}">Personality</div>
    {''.join(f'<div><div class="serif" style="font-size:34px">{a}</div><div class="it" style="font-size:20px;opacity:.6">{b}</div></div>' for a,b in pers)}
  </div>
</div>''', section='01 · Brand foundation')

# =====================================================================
# 06 VOICE
# =====================================================================
say = [('“Your fitting is ready, Mr. Arun.”', '“Hey! Ur order is done!!”'),
       ('“Cut for you. Finished by hand.”', '“Best quality, cheapest price!”'),
       ('“Wedding season appointments are open.”', '“HURRY! LIMITED OFFER!!!”'),
       ('“Let us find the cloth that suits the day.”', '“We have 1000+ designs in stock.”')]
slide(f'''
<div class="pad" style="display:grid;grid-template-columns:440px 1fr;gap:90px;align-items:center">
  <div>{head('Tone of voice', 'Speak like a <em>master tailor.</em>', 'Calm, warm and exact. Short sentences. Address the client by name. Talk about fit, cloth and craft, never about discounts or stock. In Malayalam or English, the manner is the same: respectful and unhurried.', 420)}
  <div style="margin-top:34px;display:flex;flex-direction:column;gap:12px">
   {''.join(f'<div style="display:flex;gap:14px;align-items:center"><span style="width:8px;height:8px;background:{GOLD};transform:rotate(45deg)"></span><span style="font-size:15px">{t}</span></div>' for t in ['Use “client”, not “customer”','Use “fitting”, “cut”, “cloth”, “finish”','No exclamation marks, no ALL CAPS','Emoji only on Instagram stories, sparingly'])}
  </div></div>
  <div>
   <div style="display:grid;grid-template-columns:1fr 1fr;gap:0 40px;padding-bottom:14px;border-bottom:2px solid {NAVY}">
     <div class="caps" style="font-size:12px;color:{NAVY}">We say</div><div class="caps" style="font-size:12px;color:{MUTED}">We don't say</div></div>
   {''.join(f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:0 40px;padding:26px 0;border-bottom:1px solid {LINE}"><div class="serif" style="font-size:30px;line-height:1.15">{a}</div><div style="font-size:17px;color:#9a8f86;text-decoration:line-through;text-decoration-color:rgba(90,26,36,.5);align-self:center">{b}</div></div>' for a,b in say)}
  </div>
</div>''', section='01 · Brand foundation')

# =====================================================================
# LOGO
# =====================================================================
divider('02', 'Logo', 'A needle, a button and a T. The whole craft in one small mark.')

# anatomy
sym_big = L.inline(L.symbol, height=520, c=NAVY)
slide(f'''
<div class="pad" style="display:grid;grid-template-columns:520px 1fr;gap:90px;align-items:center">
  <div>{head('The symbol', 'The needle <em>button.</em>', 'Three ideas in one solid shape, drawn to be stitched. Nothing in it is thinner than 0.5 mm at label size, so it embroiders, weaves and engraves cleanly.', 480)}
    <div style="margin-top:40px;display:flex;flex-direction:column;gap:22px">
      {''.join(f'<div style="display:grid;grid-template-columns:44px 1fr;gap:16px;align-items:start"><span class="num" style="font-size:28px">{a}</span><div><div class="serif" style="font-size:26px">{b}</div><div class="small" style="font-size:14px;margin-top:2px">{c}</div></div></div>' for a,b,c in [('1','The button','The ring is a tailor\'s button: the finishing touch on every Tezoro garment.'),('2','The needle','The stem is a needle, eye and point. Handwork, precision, made by people.'),('3','The T','Together they spell T for Tezoro, the house signature.')])}
    </div></div>
  <div style="position:relative;height:640px;display:flex;align-items:center;justify-content:center">
    <div style="position:absolute;width:640px;height:640px;background-image:linear-gradient({LINE} 1px,transparent 1px),linear-gradient(90deg,{LINE} 1px,transparent 1px);background-size:64px 64px;background-position:-1px -1px;opacity:.9"></div>
    <div style="position:absolute;width:572px;height:572px;border:1px dashed {GOLD};border-radius:50%"></div>
    <div style="position:absolute;width:1px;height:640px;background:{GOLD};opacity:.6"></div>
    <div style="position:absolute;height:1px;width:640px;background:{GOLD};opacity:.6"></div>
    <div style="position:relative">{sym_big}
    {''.join(f'<div style="position:absolute;{pos}"><span style="display:inline-flex;width:34px;height:34px;border-radius:50%;background:{GOLD};color:#fff;font-family:Corm;font-size:20px;font-style:italic;align-items:center;justify-content:center">{n}</span></div>' for n,pos in [('1','left:-56px;top:243px'),('2','left:284px;top:236px'),('3','left:392px;top:128px')])}</div>
  </div>
</div>''', section='02 · Logo')

# primary
slide(f'''
<div style="position:absolute;inset:0;display:grid;grid-template-columns:1fr 1fr">
  <div class="paper flex center">{L.inline(L.horizontal, width=600, c1=NAVY, c2=GOLD)}</div>
  <div class="navy flex center">{L.inline(L.horizontal, width=600, c1=IVORY, c2=CHAMP)}</div>
</div>
<div style="position:absolute;left:72px;top:110px">{head('Primary logo', 'The <em>signature</em> lockup.')}</div>
<div style="position:absolute;left:72px;bottom:90px;width:600px" class="small">Our first choice wherever there is room: shop fascia, website header, letterhead, garment bags. Navy on ivory, or ivory and champagne on navy.</div>
''', 'paper', section='02 · Logo')

# primary on four backgrounds
bg4 = [('#FFFFFF', NAVY, GOLD, 'Pure white', '#FFFFFF · full colour'),
       (IVORY, NAVY, GOLD, 'Soft ivory', '#F4F1EA · full colour'),
       ('#0B0B0C', IVORY, CHAMP, 'Deep black', '#0B0B0C · reversed'),
       (NAVY, IVORY, CHAMP, 'Midnight navy', '#14213D · reversed')]
slide(f"""
<div class="pad" style="top:100px">
  <div style="display:flex;justify-content:space-between;align-items:end">{'<div>'+head('Primary logo', 'On every <em>approved ground.</em>')+'</div>'}<p class="small" style="width:420px;font-size:14px">The approved logo, centred with clear space of at least half the symbol on every side. Full colour on light grounds, reversed ivory and champagne on dark.</p></div>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:34px">
   {''.join(f'<div><div style="background:{bg};height:470px;display:flex;align-items:center;justify-content:center;border:1px solid {LINE}">{L.inline(L.stacked, width=250, c1=c1, c2=c2)}</div><div style="display:flex;justify-content:space-between;margin-top:12px"><span class="caps" style="font-size:10.5px;font-weight:600">{n}</span><span class="small" style="font-size:12px">{d}</span></div></div>' for bg,c1,c2,n,d in bg4)}
  </div></div>""", section='02 · Logo')

# suite
suite = [
    ('Primary horizontal', L.inline(L.horizontal, width=330, c1=NAVY, c2=GOLD), 'Signage, web header, stationery'),
    ('Stacked', L.inline(L.stacked, height=172, c1=NAVY, c2=GOLD), 'Square spaces, bags, boxes, social'),
    ('Wordmark', L.inline(L.wordmark, width=300, c1=NAVY, c2=GOLD), 'Woven labels, footers, fine print'),
    ('Symbol', L.inline(L.symbol, height=160, c=NAVY), 'Patches, buttons, profile picture'),
    ('Monogram', L.inline(L.monogram, height=150, c=NAVY), 'Cuffs, cufflinks, favicon, pattern'),
    ('Seal', L.inline(L.seal, height=180, c=CHAMP, bg=NAVY), 'Stickers, wax seals, emboss, patches'),
    ('Signature', L.inline(L.signature, width=280, c=NAVY), 'Thank-you notes, invitations'),
    ('Wordmark, no sub-line', L.inline(L.wordmark, width=300, sub=False, c1=NAVY), 'Narrow labels below 30 mm'),
]
slide(f'''
<div class="pad" style="top:100px">
  <div style="display:flex;justify-content:space-between;align-items:end">{'<div>'+head('Logo suite', 'One family, <em>eight forms.</em>')+'</div>'}<p class="small" style="width:420px;font-size:14px">Use the largest form the space allows. Every version is supplied as vector SVG and transparent PNG in navy, ivory, champagne, black and white.</p></div>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:34px">
   {''.join(f'<div class="card" style="height:282px;display:flex;flex-direction:column"><div style="flex:1;display:flex;align-items:center;justify-content:center;padding:20px">{svg}</div><div style="padding:14px 18px;border-top:1px solid {LINE}"><div class="caps" style="font-size:10.5px;font-weight:600">{n}</div><div class="small" style="font-size:12px;margin-top:3px">{u}</div></div></div>' for n,svg,u in suite)}
  </div>
</div>''', section='02 · Logo')

# clear space & min size
cs = L.inline(L.horizontal, width=520, c1=NAVY, c2=GOLD)
slide(f'''
<div class="pad" style="display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center">
  <div>{head('Clear space', 'Give it <em>room to breathe.</em>', 'Keep a margin of at least <b>X</b> on every side, where X is the height of the needle-button ring\'s crossbar to its point, or roughly half the symbol. Nothing else may enter this space.', 520)}
    <div style="margin-top:44px;position:relative;width:640px;height:300px;background:{GOLD}1f;display:flex;align-items:center;justify-content:center;border:1px dashed {GOLD}">
      <div style="background:{IVORY};padding:0">{cs}</div>
      {''.join(f'<span class="it" style="position:absolute;{p};font-size:22px;color:{GOLD}">x</span>' for p in ['left:22px;top:136px','right:22px;top:136px','top:20px;left:316px','bottom:20px;left:316px'])}
    </div></div>
  <div>{head('Minimum size', 'Small, <em>never lost.</em>', 'Below these sizes, switch to the small cut (no needle eye, heavier ring), or to the monogram.', 520)}
    <div style="margin-top:40px;display:grid;grid-template-columns:repeat(3,1fr);gap:14px">
     {''.join(f'<div class="card" style="padding:26px 20px;height:220px;display:flex;flex-direction:column;justify-content:space-between"><div style="height:90px;display:flex;align-items:center">{s}</div><div><div class="caps" style="font-size:10.5px;font-weight:600">{n}</div><div class="small" style="font-size:12.5px;margin-top:4px">{d}</div></div></div>' for n,s,d in [
        ('Horizontal', L.inline(L.horizontal, width=150, c1=NAVY, c2=GOLD), 'Print 35 mm · Screen 140 px'),
        ('Stacked', L.inline(L.stacked, height=80, c1=NAVY, c2=GOLD), 'Print 18 mm · Screen 72 px'),
        ('Symbol', L.inline(L.symbol, height=44, c=NAVY), 'Print 8 mm · Screen 24 px'),
        ('Symbol, small cut', L.inline(L.symbol, height=26, c=NAVY, eye=False), 'Embroidery 6 mm · Favicon 16 px'),
        ('Monogram', L.inline(L.monogram, height=26, c=NAVY, eye=False), 'Engraving 4 mm · Cuff 8 mm'),
        ('Wordmark', L.inline(L.wordmark, width=110, sub=False, c1=NAVY), 'Woven 20 mm · Screen 90 px')])}
    </div></div>
</div>''', section='02 · Logo')

# colour versions
cv = [(IVORY, NAVY, GOLD, 'Full colour on ivory'), (NAVY, IVORY, CHAMP, 'Reversed on navy'),
      ('#FFFFFF', NAVY, NAVY, 'Single colour navy'), (INK, CHAMP, CHAMP, 'Single colour champagne'),
      (SAND, INK, INK, 'Black on light neutrals'), (MAROON, CHAMP, CHAMP, 'Wedding maroon'),
      (STONE, NAVY, NAVY, 'Navy on taupe board'), ('#000', '#FFFFFF', '#FFFFFF', 'White on black / photo')]
slide(f'''
<div class="pad" style="top:100px">
  {head('Colour versions', 'Always in <em>approved colours.</em>')}
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:34px">
  {''.join(f'<div><div style="background:{bg};height:250px;display:flex;align-items:center;justify-content:center;border:1px solid {LINE}">{L.inline(L.stacked, height=150, c1=c1, c2=c2)}</div><div class="tag" style="margin-top:10px">{n}</div></div>' for bg,c1,c2,n in cv)}
  </div></div>''', section='02 · Logo')

# do
def do_tile(label, art, bg='#fff'):
    return (f'<div><div class="card" style="position:relative;height:300px;display:flex;align-items:center;justify-content:center;overflow:hidden;background:{bg}">'
            f'{art}<span class="ok">✓</span></div><div class="tag" style="margin-top:10px">{label}</div></div>')


slide(f"""
<div class="pad" style="top:100px">
  {head('Correct use', 'Please <em>do.</em>')}
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:34px">
   {do_tile('Use the logo exactly as supplied', L.inline(L.stacked, height=160, c1=NAVY, c2=GOLD), IVORY)}
   {do_tile('Keep the clear space', f'<div style="border:1px dashed {GOLD};padding:34px 30px;background:{GOLD}14">' + L.inline(L.stacked, height=120, c1=NAVY, c2=GOLD) + '</div>')}
   {do_tile('Use approved colour versions', L.inline(L.stacked, height=160, c1=IVORY, c2=CHAMP), NAVY)}
   {do_tile('Choose clean, high-contrast grounds', L.inline(L.stacked, height=160, c1=NAVY, c2=NAVY), SAND)}
  </div></div>""", section='02 · Logo')

# misuse
mis = [('Don\'t stretch or squash', 'transform:scaleX(1.3)'),
       ('Don\'t rotate', 'transform:rotate(-14deg)'),
       ('Don\'t skew', 'transform:skewX(-18deg)'),
       ('Don\'t crop', 'CROP'),
       ('Don\'t use low contrast', 'LOW'),
       ('Don\'t add shadows or effects', 'filter:drop-shadow(6px 6px 3px rgba(0,0,0,.55))'),
       ('Don\'t use off-brand colours', 'filter:hue-rotate(150deg) saturate(3)'),
       ('Don\'t outline', 'OUTLINE'),
       ('Don\'t place on busy patterns', 'BUSY'),
       ('Don\'t retype in another font', 'FONT')]


def mis_tile(label, style):
    if style == 'OUTLINE':
        b, w, h = L.stacked(c1='none', c2='none')
        art = f'<svg viewBox="0 0 {w} {h}" height="140" width="{140*w/h:.0f}"><g stroke="{NAVY}" stroke-width="3">{b}</g></svg>'
    elif style == 'REARR':
        art = f'<div style="display:flex;flex-direction:row-reverse;align-items:center;gap:16px">{L.inline(L.symbol, height=70, c=NAVY)}{L.inline(L.wordmark, width=170, c1=NAVY, c2=GOLD)}</div>'
    elif style == 'BUSY':
        art = f'<div style="position:absolute;inset:0;background:repeating-linear-gradient(45deg,#C9A227 0 14px,#0F3D2E 14px 28px)"></div><div style="position:relative">{L.inline(L.stacked, height=140, c1=NAVY, c2=GOLD)}</div>'
    elif style == 'CROP':
        art = f'<div style="position:absolute;left:46%;top:-30px">{L.inline(L.stacked, height=200, c1=NAVY, c2=GOLD)}</div>'
    elif style == 'LOW':
        art = f'<div style="position:absolute;inset:0;background:{SAND}"></div><div style="position:relative">{L.inline(L.stacked, height=130, c1=STONE, c2=IVORY)}</div>'
    elif style == 'FONT':
        art = f'<div style="text-align:center"><div style="display:flex;justify-content:center">{L.inline(L.symbol, height=70, c=NAVY)}</div><div style="font-family:Arial Black,Arial;font-weight:900;font-size:34px;color:{NAVY};margin-top:10px">TEZORO</div></div>'
    else:
        art = f'<div style="{style}">{L.inline(L.stacked, height=130, c1=NAVY, c2=GOLD)}</div>'
    return (f'<div><div class="card" style="position:relative;height:244px;display:flex;align-items:center;justify-content:center;overflow:hidden">'
            f'{art}<span class="x">✕</span></div><div class="tag" style="margin-top:10px">{label}</div></div>')


slide(f'''
<div class="pad" style="top:100px">
  {head('Misuse', 'Please <em>don\'t.</em>')}
  <div style="display:grid;grid-template-columns:repeat(5,1fr);gap:12px;margin-top:30px">{''.join(mis_tile(a, b) for a, b in mis)}</div>
</div>''', section='02 · Logo')

# =====================================================================
# 03 FABRIC & PRODUCTION
# =====================================================================
divider('03', 'Fabric &amp; production', 'Built to be stitched, woven, pressed and engraved. Specifications for suppliers.')

slide(f'''
<div class="pad" style="top:100px">
  {head('Production versions', 'One mark, <em>four crafts.</em>')}
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:32px">
   {M.embroidery_swatch(340, 380)}
   {M.woven_swatch(340, 380)}
   {M.leather_swatch(340, 380)}
   {M.engraved_swatch(340, 380)}
  </div>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:18px">
   {''.join(f'<div><h3 style="font-size:12px">{a}</h3><div class="small" style="margin-top:8px;font-size:13px">{b}</div></div>' for a,b in [
     ('Embroidery','Satin stitch for the ring and bar, fill stitch for the needle. Small cut below 15 mm. Thread: champagne or ivory on navy cloth; navy on white shirting.'),
     ('Woven jacquard','High-density damask weave. Wordmark at 20 mm minimum width; symbol at 8 mm. Navy ground, champagne weft. Folded or end-fold labels.'),
     ('Leather &amp; deboss','Blind deboss or champagne foil on tan or navy leather. Seal at 25 mm or more; symbol at 12 mm or more. Keep needle eye above 20 mm.'),
     ('Laser &amp; engraving','Monogram for buttons and cufflinks, 4 mm minimum. Seal or stacked lockup for hangers and wooden boxes. Single-line depth 0.2 mm.')])}
  </div>
</div>''', section='03 · Fabric &amp; production')

# specs table
specs = [('Neck label (woven)', 'Wordmark + sub-line', '50 × 15 mm', 'Navy ground, champagne'),
         ('Size label (woven)', 'Monogram + size', '15 × 15 mm', 'Navy ground, ivory'),
         ('Chest / cuff embroidery', 'Monogram, small cut', '8 to 12 mm', 'Thread to match cloth tone'),
         ('Blazer lining patch', 'Seal', '35 mm round', 'Champagne on navy'),
         ('Buttons (custom)', 'Monogram, engraved', '4 to 6 mm', 'Horn, corozo or metal'),
         ('Hang tag', 'Stacked lockup', '55 × 95 mm arch', 'Taupe board, navy print'),
         ('Garment bag', 'Stacked lockup', '160 mm wide', 'Navy non-woven, champagne'),
         ('Shop fascia', 'Primary horizontal', '2400 mm wide', 'Backlit champagne letters')]
slide(f'''
<div class="pad" style="display:grid;grid-template-columns:400px 1fr;gap:70px;align-items:center">
  <div>{head('Supplier sheet', 'Specs at <em>a glance.</em>', 'Send this page to label, embroidery and print suppliers with the logo files. Always ask for a physical sample before a full run, and match colours by eye to the Tezoro swatch card, not to a screen.', 380)}</div>
  <div style="font-size:15px">
   <div style="display:grid;grid-template-columns:1.3fr 1.2fr .9fr 1.3fr;gap:20px;padding:0 0 14px;border-bottom:2px solid {NAVY}" class="caps"><span style="font-size:10.5px">Item</span><span style="font-size:10.5px">Logo form</span><span style="font-size:10.5px">Size</span><span style="font-size:10.5px">Colour</span></div>
   {''.join(f'<div style="display:grid;grid-template-columns:1.3fr 1.2fr .9fr 1.3fr;gap:20px;padding:17px 0;border-bottom:1px solid {LINE}"><span class="serif" style="font-size:22px">{a}</span><span>{b}</span><span>{c}</span><span style="color:{MUTED}">{d}</span></div>' for a,b,c,d in specs)}
  </div>
</div>''', section='03 · Fabric &amp; production')

# =====================================================================
# 04 COLOUR
# =====================================================================
divider('04', 'Colour', 'Midnight navy and champagne, grounded in ivory. The colours of evening wear.')


def swatch(name, hx, role, desc, big=False):
    r, g, b = rgb(hx)
    c, m, y, k = cmyk(hx)
    dark = lum(hx) < .25
    fg = IVORY if dark else INK
    return f'''<div style="background:{hx};color:{fg};padding:26px 26px 22px;display:flex;flex-direction:column;justify-content:space-between;{'grid-row:span 2;' if big else ''}border:1px solid rgba(0,0,0,.05)">
      <div><div class="caps" style="font-size:10px;opacity:.7">{role}</div><div class="serif" style="font-size:{40 if big else 28}px;margin-top:6px;line-height:1">{name}</div>
      {f'<div style="font-size:13px;line-height:1.5;margin-top:12px;opacity:.75;max-width:300px">{desc}</div>' if big else ''}</div>
      <div style="font-size:12px;line-height:1.7;opacity:.85;font-variant-numeric:tabular-nums"><b>{hx}</b><br>RGB {r} {g} {b}<br>CMYK {c} {m} {y} {k}</div></div>'''


def swatch2(name, hx, role, desc, h):
    r, g, bb = rgb(hx)
    c, m, y, k = cmyk(hx)
    fg = IVORY if lum(hx) < .25 else INK
    return f"""<div style="background:{hx};color:{fg};height:{h}px;padding:22px 22px 20px;display:flex;flex-direction:column;justify-content:space-between;border:1px solid rgba(0,0,0,.06)">
      <div><div class="serif" style="font-size:30px;line-height:1">{name}</div><div style="font-size:12px;line-height:1.5;margin-top:10px;opacity:.78">{desc}</div></div>
      <div style="font-size:11.5px;line-height:1.7;opacity:.85;font-variant-numeric:tabular-nums"><b>{hx}</b><br>RGB {r} {g} {bb}<br>CMYK {c} {m} {y} {k}</div></div>"""


P = {n: (n, h, r, d) for n, h, r, d in PALETTE}
groups = [('Primary', 'Logo, main surfaces, key accents', 2, ['Midnight Navy', 'Champagne']),
          ('Secondary', 'Small type, text, the wedding floor', 3, ['Antique Gold', 'Deep Ink', 'Wedding Maroon']),
          ('Neutral', 'Backgrounds, paper, packaging', 3, ['Soft Ivory', 'Taupe Stone', 'Sandstone'])]
slide(f"""
<div class="pad" style="top:100px">
  <div style="display:flex;justify-content:space-between;align-items:end">{'<div>'+head('Palette', 'A colour system, <em>not a collection.</em>')+'</div>'}<p class="small" style="width:420px;font-size:14px">Taken from the approved logo: navy for the mark, champagne and antique gold for the sub-line and rule. Supporting colours keep the same warm, quiet temperature. CMYK values are starting points: proof on the final stock.</p></div>
  <div style="display:grid;grid-template-columns:2fr 3fr 3fr;gap:22px;margin-top:30px">
   {''.join(f'<div><div style="display:flex;justify-content:space-between;align-items:baseline;border-bottom:2px solid {NAVY};padding-bottom:8px;margin-bottom:12px"><span class="caps" style="font-size:11px;font-weight:600">{g}</span><span class="small" style="font-size:11.5px">{u}</span></div><div style="display:grid;grid-template-columns:repeat({n},1fr);gap:8px">' + ''.join(swatch2(*P[c], 520) for c in cs) + '</div></div>' for g,u,n,cs in groups)}
  </div>
</div>""", section='04 · Colour')

# proportion + pairings
pairs = [(IVORY, NAVY), (NAVY, IVORY), (NAVY, CHAMP), (IVORY, GOLD), (MAROON, CHAMP), (SAND, INK)]
slide(f'''
<div class="pad" style="display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center">
  <div>{head('Proportion', 'Mostly quiet, <em>a little gold.</em>', 'Ivory and navy carry the brand. Champagne is the thread that catches the light, so keep it small: rules, logos, single words. Maroon appears only on the wedding floor.', 520)}
    <div style="display:flex;height:220px;margin-top:44px">
      {''.join(f'<div style="flex:{f};background:{c};display:flex;align-items:end;padding:12px;font-size:12px;color:{t}">{p}</div>' for f,c,t,p in [(50,IVORY,INK,'50% Ivory'),(30,NAVY,IVORY,'30% Navy'),(10,STONE,INK,'10%'),(6,CHAMP,INK,'6%'),(4,MAROON,IVORY,'')])}
    </div>
    <div class="small" style="margin-top:10px">Ivory · Navy · Stone and sand · Champagne and gold · Maroon (wedding only)</div></div>
  <div>{head('Pairings', 'Readable <em>by design.</em>', 'Contrast ratios for type. AA needs 4.5 for body text and 3.0 for large headings.', 520)}
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:40px">
     {''.join(f'<div style="background:{bg};color:{fg};height:190px;padding:20px;display:flex;flex-direction:column;justify-content:space-between;border:1px solid {LINE}"><span class="serif" style="font-size:56px;line-height:1">Aa</span><span style="font-size:12px"><b>{contrast(bg,fg):.1f} : 1</b> · {"AA body" if contrast(bg,fg)>=4.5 else "Headings only"}</span></div>' for bg,fg in pairs)}
    </div></div>
</div>''', section='04 · Colour')

# =====================================================================
# 05 TYPE
# =====================================================================
divider('05', 'Typography', 'A classical serif, engraved capitals and a modern sans. All three are free, open-licence fonts.')

slide(f'''
<div class="pad" style="top:100px;display:grid;grid-template-columns:repeat(3,1fr);gap:22px">
  {''.join(f"""<div class="{cls}" style="padding:34px 32px;display:flex;flex-direction:column;justify-content:space-between;border:1px solid {LINE}">
    <div><div class="tag">{role}</div><div style="font-family:{fam};font-size:34px;margin-top:10px;{xs}">{name}</div></div>
    <div style="font-family:{fam};font-size:150px;line-height:1;{xs}">{big}</div>
    <div style="font-family:{fam};font-size:19px;line-height:1.5;{xs}word-break:break-all">ABCDEFGHIJKLM<br>abcdefghijklm<br>0123456789</div>
    <div class="small" style="font-size:13px">{desc}</div></div>""" for cls,role,fam,name,big,xs,desc in [
    ('paper','Display · headings','Corm','Cormorant Garamond','Aa','font-weight:500;','Headlines, quotes and the wordmark. Light to medium weights; italic in gold for emphasis.'),
    ('navy','Labels · navigation','Cinz','Cinzel','Aa','letter-spacing:.06em;','Capitals only, widely spaced (+0.25 em). Eyebrows, labels, buttons, signage lines.'),
    ('paper','Body · interface','Inter','Inter','Aa','','Body copy, prices, forms, captions and the website. Regular and medium, 15 to 18 px.')])}
</div>''', section='05 · Typography')

slide(f'''
<div class="pad" style="display:grid;grid-template-columns:1fr 1.1fr;gap:80px;align-items:center">
  <div>{head('Hierarchy', 'Setting the <em>page.</em>', 'A quiet rhythm: one capital eyebrow, one serif headline, one paragraph. Generous space between them, and never more than two sizes of serif on one surface.', 480)}
   <div style="margin-top:36px;font-size:14px;line-height:2.1;color:{MUTED}">
    {''.join(f'<div style="display:flex;justify-content:space-between;border-bottom:1px solid {LINE}"><span>{a}</span><span style="color:{INK}">{b}</span></div>' for a,b in [('Eyebrow','Cinzel 600 · 12–14 · +0.32 em'),('Display','Cormorant 500 · 64–120 · −0.01 em'),('Headline','Cormorant 500 · 36–56'),('Emphasis','Cormorant italic · Antique Gold'),('Body','Inter 400 · 15–18 · 1.6 leading'),('Caption','Inter 500 · 11–12 · +0.14 em caps')])}
   </div></div>
  <div class="card" style="padding:64px 60px">
    <div class="eyebrow">The wedding collection</div>
    <div class="serif" style="font-size:72px;line-height:1;margin-top:18px">Cut for the <em style="color:{GOLD}">day you'll remember.</em></div>
    <div class="serif" style="font-size:28px;line-height:1.2;margin-top:18px;color:{NAVY}">Private consultations on the wedding floor</div>
    <p style="font-size:17px;line-height:1.65;color:{MUTED};margin-top:24px">Sherwanis, bandhgalas and three-piece suits, made to your measure from cloth you choose. Book a private consultation on the wedding floor.</p>
    <div style="display:flex;gap:14px;margin-top:34px"><span class="caps" style="background:{NAVY};color:{IVORY};padding:16px 26px;font-size:11.5px">Book a fitting</span><span class="caps" style="border:1px solid {NAVY};padding:16px 26px;font-size:11.5px">View the lookbook</span></div>
    <div style="font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;color:{MUTED};margin-top:26px;font-weight:500">Pictured: ivory raw-silk sherwani, No. TZ-0152</div>
  </div>
</div>''', section='05 · Typography')

# type scale
sc = [('Display', 'Corm', 96, 500, '−0.01 em', '1.0', 'Made to measure.'),
      ('Headline', 'Corm', 56, 500, '0', '1.05', 'The wedding collection'),
      ('Subheading', 'Corm', 32, 500, '0', '1.2', 'Private consultations, by appointment'),
      ('Eyebrow / label', 'Cinz', 13, 600, '+0.32 em', '1.4', 'BESPOKE TAILORING · POTHENCODE'),
      ('Body', 'Inter', 17, 400, '0', '1.6', 'Suits, shirts and wedding wear cut to your measure from cloth you choose.'),
      ('Caption', 'Inter', 12, 500, '+0.14 em', '1.5', 'NAVY WOOL TWILL · No. TZ-0147'),
      ('Button', 'Cinz', 12, 600, '+0.28 em', '1', 'BOOK A FITTING')]
slide(f"""
<div class="pad" style="top:100px">
  <div style="display:flex;justify-content:space-between;align-items:end">{'<div>'+head('Type scale', 'Sizes, weights, <em>spacing.</em>')+'</div>'}<p class="small" style="width:420px;font-size:14px">A 1.6 ratio scale for print and screen. Leave one line of the larger size above a heading, and half a line below it.</p></div>
  <div style="margin-top:26px;border-top:2px solid {NAVY}">
   {''.join(f'<div style="display:grid;grid-template-columns:170px 260px 1fr;gap:30px;align-items:center;padding:{10 if s<40 else 6}px 0;border-bottom:1px solid {LINE}"><span class="caps" style="font-size:10.5px;font-weight:600">{n}</span><span class="small" style="font-size:12px;font-variant-numeric:tabular-nums">{ {"Corm":"Cormorant","Cinz":"Cinzel","Inter":"Inter"}[f]} {w} · {s}px · {t} · lh {lh}</span><span style="font-family:{f};font-size:{s}px;font-weight:{w};line-height:{lh};letter-spacing:{t.replace("−","-").replace(" em","em") if t!="0" else "0"};{"color:"+NAVY if f=="Corm" else ""};white-space:nowrap;overflow:hidden">{ex if n!="Button" else f"<span style=\'display:inline-block;background:{NAVY};color:{IVORY};padding:14px 24px\'>{ex}</span>"}</span></div>' for n,f,s,w,t,lh,ex in sc)}
  </div></div>""", section='05 · Typography')

# =====================================================================
# 06 GRAPHIC LANGUAGE
# =====================================================================
divider('06', 'Graphic language', 'Patterns, icons and stitch details that extend the identity.')

pats = [(pattern_monogram(CHAMP, NAVY, 60), 'Monogram repeat', 'Linings, tissue, garment bags'),
        (pattern_pinstitch(CHAMP, NAVY), 'Pin-stitch stripe', 'Boxes, backgrounds, web'),
        (pattern_buttons(CHAMP, NAVY), 'Button field', 'Gift wrap, story backgrounds'),
        (pattern_arch(CHAMP, MAROON), 'Mandap arch', 'Tezoro Wedding only'),
        (pattern_monogram(NAVY, IVORY, 60, .22), 'Monogram, tonal', 'Letterhead, shirt boxes'),
        (pattern_pinstitch(NAVY, SAND), 'Pin-stitch on sand', 'Tags, invoices, packaging')]
slide(f'''
<div class="pad" style="top:100px">
  {head('Patterns', 'Quiet <em>repeats.</em>')}
  <div style="display:grid;grid-template-columns:repeat(6,1fr);gap:12px;margin-top:32px">
   {''.join(f'<div><div style="height:500px;background:{p};border:1px solid {LINE}"></div><div class="caps" style="font-size:10.5px;margin-top:12px;font-weight:600">{n}</div><div class="small" style="font-size:12px;margin-top:3px">{u}</div></div>' for p,n,u in pats)}
  </div></div>''', section='06 · Graphic language')

icons_list = [('shirt', 'Shirts'), ('jacket', 'Suits'), ('sherwani', 'Sherwani'), ('trousers', 'Trousers'),
              ('measure', 'Measure'), ('needle', 'Handwork'), ('fabric', 'Cloth'), ('scissors', 'Alterations'),
              ('ring', 'Wedding'), ('calendar', 'Appointment'), ('gift', 'Gifting'), ('pin', 'Visit')]
slide(f'''
<div class="pad" style="display:grid;grid-template-columns:1.25fr 1fr;gap:70px;align-items:center">
  <div>{head('Icons', 'Drawn with <em>a single thread.</em>', 'Outline icons on a 24-unit grid, 1.4 stroke, round ends. Navy on light, champagne on dark. For the website, menus, signage and Instagram highlights.', 520)}
   <div style="display:grid;grid-template-columns:repeat(6,1fr);gap:10px;margin-top:40px">
    {''.join(f'<div class="card" style="height:150px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px">{icon(i,46)}<span class="tag" style="font-size:9.5px">{n}</span></div>' for i,n in icons_list)}
   </div></div>
  <div>{head('Details', 'The <em>finishing</em> touches.')}
   <div style="margin-top:40px;display:flex;flex-direction:column;gap:26px">
    <div><div style="height:2px;background:repeating-linear-gradient(90deg,{GOLD} 0 14px,transparent 14px 22px)"></div><div class="small" style="margin-top:10px">Stitch rule: divides sections, edges cards and tags</div></div>
    <div style="display:flex;align-items:center;gap:18px"><div style="flex:1;height:1px;background:{GOLD}"></div>{L.inline(L.monogram, height=22, c=GOLD, eye=False)}<div style="flex:1;height:1px;background:{GOLD}"></div></div>
    <div class="small" style="margin-top:-14px">Monogram divider: for menus, certificates and invitations</div>
    <div style="height:46px;background:{SAND};position:relative;border-top:1px solid {STONE};border-bottom:1px solid {STONE};background-image:repeating-linear-gradient(90deg,{INK} 0 1px,transparent 1px 10px),repeating-linear-gradient(90deg,{INK} 0 1.5px,transparent 1.5px 50px);background-size:100% 12px,100% 22px;background-repeat:no-repeat"><span style="position:absolute;right:12px;top:16px;font-size:11px;letter-spacing:.2em;font-family:Cinz">TEZORO</span></div>
    <div class="small" style="margin-top:-14px">Tape-measure band: footers, packaging tape, web loaders</div>
    <div style="width:110px;height:170px;background:{NAVY};border-radius:55px 55px 4px 4px;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:10px"><span style="width:10px;height:10px;border-radius:50%;background:{IVORY}"></span>{L.inline(L.symbol, height=40, c=CHAMP)}</div>
    <div class="small" style="margin-top:-14px">Arch frame: from the hang tag, used for photos and stories</div>
   </div></div>
</div>''', section='06 · Graphic language')

slide(M.photography_scene(), section='06 · Photography')

# =====================================================================
# 07 BRAND IN USE
# =====================================================================
divider('07', 'Brand in use', 'How Tezoro looks in the hand, on the street and on the screen.')

slide(M.labels_scene(), 'sand', section='07 · Labels')
slide(M.embroidery_scene(), 'navy', section='07 · Embroidery &amp; buttons')
slide(M.hangtag_scene(), 'paper', section='07 · Hang tags')
slide(M.garmentbag_scene(), 'sand', section='07 · Garment bag')
slide(M.packaging_scene(), 'paper', section='07 · Packaging')
slide(M.stationery_scene(), 'sand', section='07 · Stationery')
slide(M.store_scene(), 'ink', section='07 · Store front')
slide(M.instagram_scene(), 'paper', section='07 · Instagram')
slide(M.website_scene(), 'sand', section='07 · Website')
slide(M.app_scene(), 'paper', section='07 · Mobile app')
slide(M.email_scene(), 'sand', section='07 · Email signature')
slide(M.passport_scene(), 'navy', section='07 · Client experience')

# =====================================================================
# 08 WEDDING
# =====================================================================
divider('08', 'Tezoro Wedding', 'The wedding floor speaks in maroon and gold, with the same calm voice.', 'maroon',
        pattern_arch(CHAMP, MAROON, 90))
slide(M.wedding_scene(), 'maroon', section='08 · Tezoro Wedding')

# =====================================================================
# CLOSING
# =====================================================================
slide(f'''
<div style="position:absolute;inset:0;background:{pattern_monogram(CHAMP, NAVY, 70)};opacity:.12"></div>
<div class="flex col center" style="position:absolute;inset:0">
  {L.inline(L.seal, height=230, c=CHAMP)}
  <div class="serif" style="font-size:60px;margin-top:50px">Made for you, <em style="color:{CHAMP}">only you.</em></div>
  <div class="caps" style="font-size:12px;margin-top:22px;color:{CHAMP}">Tezoro Atelier · Pothencode · Thiruvananthapuram</div>
</div>
<div class="foot" style="opacity:.45"><span>Brand identity by DARTS AI · Edition 01 · 2026</span><span>Logo files: SVG · PNG · in every approved colour</span></div>
''', 'navy', chrome=False, foot=False)

html = f'<!doctype html><html><head><meta charset="utf-8"><title>Tezoro Brand Guidelines</title><style>{CSS}{M.CSS}</style></head><body>{M.DEFS}{"".join(TOTAL)}</body></html>'
open('brandkit.html', 'w').write(html)
print(len(TOTAL), 'slides')
