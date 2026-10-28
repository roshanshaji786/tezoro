"""Builds profile.html: Tezoro's company profile (A4 portrait brochure),
designed in the new identity."""
from common import *
import logos as L
import mockups as M

W, H = 794, 1123
PAGES = []

CSS = BASE_CSS + f"""
@page{{size:{W}px {H}px;margin:0}}
section.pg{{width:{W}px;height:{H}px;position:relative;overflow:hidden;page-break-after:always;break-after:page}}
.in{{position:absolute;left:64px;right:64px;top:72px;bottom:80px}}
.pf{{position:absolute;left:64px;right:64px;bottom:34px;display:flex;justify-content:space-between;font-size:9.5px;letter-spacing:.16em;text-transform:uppercase;opacity:.55}}
.eyebrow{{font-family:Cinz;font-size:11px;letter-spacing:.34em;text-transform:uppercase;color:{GOLD}}}
.navy .eyebrow,.maroon .eyebrow{{color:{CHAMP}}}
h2{{font-family:Corm;font-weight:500;font-size:52px;line-height:1;margin-top:12px}}
h2 em{{color:{GOLD}}}.navy h2 em,.maroon h2 em{{color:{CHAMP}}}
p.b{{font-size:13.5px;line-height:1.7;color:{MUTED};margin-top:16px}}
.navy p.b,.maroon p.b{{color:rgba(244,241,234,.75)}}
.h4{{font-family:Corm;font-size:24px;line-height:1.1}}
.sm{{font-size:11.5px;line-height:1.6;color:{MUTED}}}
.navy .sm,.maroon .sm{{color:rgba(244,241,234,.7)}}
.num{{font-family:Corm;font-style:italic;color:{GOLD};font-size:20px}}
.maroon .num,.navy .num{{color:{CHAMP}}}
.shadow{{box-shadow:0 24px 40px -18px rgba(13,21,38,.5),0 8px 14px -8px rgba(13,21,38,.3)}}
"""


def page(content, bg='paper', foot=True, label=''):
    n = len(PAGES) + 1
    f = f'<div class="pf"><span>Tezoro · Company Profile</span><span>{label}{" · " if label else ""}{n:02d}</span></div>' if foot else ''
    PAGES.append(f'<section class="pg {bg}">{content}{f}</section>')


# 1 cover -------------------------------------------------------------
page(f'''
<div style="position:absolute;inset:0;background:{pattern_monogram(CHAMP, NAVY, 60, .35)};opacity:.35"></div>
<div style="position:absolute;inset:0;background:radial-gradient(ellipse at 50% 42%,rgba(20,33,61,.2),rgba(13,21,38,.95) 72%)"></div>
<div style="position:absolute;inset:40px;border:1px solid rgba(212,180,131,.35)"></div>
<div class="flex col center" style="position:absolute;inset:0;text-align:center">
  {L.inline(L.stacked, height=250, c1=IVORY, c2=CHAMP)}
  <div style="width:50px;height:1px;background:{CHAMP};margin:54px 0 24px"></div>
  <div class="caps" style="font-size:12px;color:{CHAMP}">Company Profile · 2026</div>
  <div class="serif it" style="font-size:24px;margin-top:14px;opacity:.8">Bespoke menswear &amp; the wedding atelier</div>
</div>
<div style="position:absolute;left:0;right:0;bottom:70px;text-align:center" class="caps"><span style="font-size:10px;opacity:.55">Pothencode · Thiruvananthapuram · Kerala</span></div>
''', 'navy', foot=False)

# 2 welcome -----------------------------------------------------------
page(f'''
<div class="in">
  <div class="eyebrow">Welcome to Tezoro</div>
  <h2>A treasure,<br><em>made to measure.</em></h2>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:36px;margin-top:30px">
    <div><p class="b" style="margin-top:0">Tezoro takes its name from <i>tesoro</i>, the word for treasure. We are a premium men's tailoring house and wedding atelier in Pothencode, created for men who would rather be measured than matched to a rack.</p>
    <p class="b">Every Tezoro garment begins with a conversation and ends with a final fitting. In between, it is cut, sewn and finished for one man only. Nothing is repeated, and nothing leaves the atelier until it fits.</p></div>
    <div><p class="b" style="margin-top:0">Under one roof you will find bespoke suits, shirts and trousers for every day, and a dedicated wedding floor where grooms and their families can plan the most important outfits of their lives in private, at their own pace.</p>
    <p class="b">We believe a well-made garment changes how a man stands, walks and feels. That belief is the whole of our business.</p></div>
  </div>
  <div class="navy" style="margin-top:44px;padding:50px 48px;position:relative">
    <div class="serif" style="font-size:96px;line-height:.5;height:30px;color:{CHAMP}">“</div>
    <div class="serif" style="font-size:36px;line-height:1.15">Every man deserves a look that is <em style="color:{CHAMP}">his alone.</em></div>
    <div style="display:flex;align-items:center;justify-content:space-between;margin-top:30px">
      <div><div class="serif it" style="font-size:26px;color:{CHAMP}">Safnal</div><div class="caps" style="font-size:9.5px;opacity:.6;margin-top:4px">Founder, Tezoro</div></div>
      {L.inline(L.symbol, height=54, c=CHAMP)}</div>
  </div>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);margin-top:40px;border-top:1px solid {LINE}">
   {''.join(f'<div style="padding:22px 0 0;{b}"><div class="serif" style="font-size:40px;color:{NAVY};line-height:1">{a}</div><div class="sm" style="margin-top:6px">{c}</div></div>' for a,c,b in [('1 of 1','Every garment is cut for one client',''),('2 floors','Bespoke tailoring and the wedding atelier','padding-left:24px;border-left:1px solid '+LINE),('3 fittings','To get every line exactly right','padding-left:24px;border-left:1px solid '+LINE)])}
  </div>
</div>''', label='Welcome')

# 3 philosophy --------------------------------------------------------
pillars = [('I', 'One man, one look', 'No duplicates, ever. Your cut, cloth and details are recorded for you alone, so you will never meet your suit on someone else.'),
           ('II', 'Crafted by hand', 'Premium cloth, precise measurement and expert finishing by tailors who have spent years at the bench.'),
           ('III', 'The wedding destination', 'A dedicated floor for grooms, families and celebrations, from engagement to reception.'),
           ('IV', 'Time for you', 'A boutique pace. Appointments are private, unhurried and built around your calendar.')]
page(f'''
<div style="position:absolute;left:0;right:0;top:0;height:420px;background:{pattern_pinstitch(CHAMP, NAVY, 22, .35)}"></div>
<div style="position:absolute;left:0;right:0;top:0;height:420px;background:linear-gradient(180deg,rgba(20,33,61,.3),{NAVY})"></div>
<div style="position:absolute;left:64px;right:64px;top:90px;color:{IVORY}">
  <div class="eyebrow" style="color:{CHAMP}">Our philosophy</div>
  <h2 style="color:{IVORY}">One man.<br><em style="color:{CHAMP}">One look.</em></h2>
  <p class="b" style="color:rgba(244,241,234,.78);max-width:440px">Off the rack, a hundred men can own the same shirt. At Tezoro, every piece is made to belong to one man, and only him.</p>
</div>
<div style="position:absolute;left:64px;right:64px;top:470px;display:grid;grid-template-columns:1fr 1fr;gap:40px 40px">
  {''.join(f'<div style="border-top:2px solid {NAVY};padding-top:18px"><div class="num" style="font-size:26px">{a}</div><div class="h4" style="font-size:28px;margin:6px 0 10px">{b}</div><div class="sm" style="font-size:12.5px">{c}</div></div>' for a,b,c in pillars)}
</div>''', label='Philosophy')

# 4 what we make ------------------------------------------------------
svc = [('jacket', 'Bespoke suits', 'Two- and three-piece suits, blazers and tuxedos, cut from a pattern drafted for you.'),
       ('shirt', 'Shirts', 'Formal and casual shirts in cotton, linen and poplin, with your choice of collar and cuff.'),
       ('trousers', 'Trousers', 'Formal trousers and chinos with a balanced drape and a clean break.'),
       ('sherwani', 'Sherwanis &amp; bandhgalas', 'Wedding and festive wear, from classic sherwanis to Jodhpuri bandhgalas.'),
       ('fabric', 'Kurtas &amp; Indo-western', 'Kurta sets, jackets and modern Indo-western pieces for every occasion.'),
       ('scissors', 'Alterations &amp; aftercare', 'Re-fitting, repairs and refreshing of Tezoro garments for as long as you wear them.')]
page(f'''
<div class="in">
  <div class="eyebrow">What we make</div>
  <h2>From the first suit<br>to <em>the wedding day.</em></h2>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:0 36px;margin-top:40px">
   {''.join(f'<div style="display:grid;grid-template-columns:56px 1fr;gap:16px;padding:26px 0;border-top:1px solid {LINE}"><div style="width:56px;height:56px;border:1px solid {LINE};display:flex;align-items:center;justify-content:center;background:#fff">{icon(i, 30, NAVY)}</div><div><div class="h4">{a}</div><div class="sm" style="margin-top:6px">{b}</div></div></div>' for i,a,b in svc)}
  </div>
  <div class="navy" style="margin-top:34px;display:grid;grid-template-columns:240px 1fr;height:300px">
    <div style="background:{pattern_pinstitch(CHAMP, NAVY, 20, .25)};display:flex;align-items:center;justify-content:center">{M.jacket_art(150, CHAMP, 2)}</div>
    <div style="padding:36px 36px;display:flex;flex-direction:column;justify-content:space-between">
      <div><div class="caps" style="font-size:10px;color:{CHAMP}">Your pattern, kept on file</div><div class="serif" style="font-size:28px;line-height:1.15;margin-top:10px">Every Tezoro suit begins as a paper pattern drafted for one man, and kept for every order after.</div></div>
      <div style="display:flex;justify-content:space-between;align-items:end"><div class="sm">Also at Tezoro: ties, pocket squares, cufflinks,<br>stoles and safas, chosen to finish each look.</div>{M.mono_svg(40, CHAMP)}</div></div></div>
</div>''', label='Services')

# 5 wedding -----------------------------------------------------------
page(f'''
<div style="position:absolute;inset:0;background:{pattern_arch(CHAMP, MAROON, 80)};opacity:.35"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(90,26,36,.6),{MAROON} 55%)"></div>
<div class="in">
  {L.inline(L.horizontal, width=300, c1=IVORY, c2=CHAMP, subtext='WEDDING')}
  <h2 style="margin-top:46px">The day you'll<br><em>always remember.</em></h2>
  <p class="b" style="max-width:520px">The Tezoro Wedding floor is a private space for the groom, his family and his closest friends. Bring your ideas, your colours and your rituals; we bring the cloth, the craft and the calm.</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:30px 36px;margin-top:40px">
   {''.join(f'<div style="border-top:1px solid rgba(212,180,131,.45);padding-top:16px"><div class="h4">{a}</div><div class="sm" style="margin-top:6px">{b}</div></div>' for a,b in [
     ('For the groom','Sherwanis, bandhgalas, three-piece suits and reception tuxedos, for every function from engagement to reception.'),
     ('For the family','Coordinated looks for fathers, brothers and groomsmen, in one palette and one fitting schedule.'),
     ('Private consultation','A dedicated hour on the wedding floor to plan each outfit, choose cloth and set fitting dates.'),
     ('Finished together','Safas, stoles, mojaris, cufflinks and buttons chosen with the outfit, delivered as one.')])}
  </div>
  <div style="position:absolute;left:-20px;right:0;bottom:50px;display:flex;align-items:end;justify-content:space-between">
    <div>{M.bag(150, 300, MAROON, CHAMP, CHAMP, 'WEDDING')}</div>
    <div style="margin-bottom:10px">{M.box_svg(330).replace('fill="url(#lidtop)"', 'fill="#6A2030"').replace('#0F1A30', '#45121B').replace('#0B1427', '#350C14').replace('#17254A', '#5A1A26').replace('#101C38', '#4A1420')}</div>
  </div>
  <div style="position:absolute;left:0;right:0;bottom:0;display:flex;align-items:center;gap:20px">
    <div style="flex:1;height:1px;background:rgba(212,180,131,.5)"></div><span class="caps" style="font-size:10px;color:{CHAMP}">Consultations by appointment</span><div style="flex:1;height:1px;background:rgba(212,180,131,.5)"></div></div>
</div>''', 'maroon', label='Tezoro Wedding')

# 6 process -----------------------------------------------------------
steps = [('Consultation', 'We talk about the occasion, your style and how you like to wear your clothes.', 'chat'),
         ('Measurement', 'More than twenty measurements and notes on posture, recorded in your Fitting Book.', 'measure'),
         ('Cloth &amp; details', 'Choose cloth, lining, buttons, lapels and pockets, with guidance at every step.', 'fabric'),
         ('Fittings', 'Two or three fittings refine the garment on you until every line sits right.', 'needle'),
         ('Finishing &amp; delivery', 'Hand-finished, pressed and delivered in a Tezoro garment bag or box.', 'gift')]
page(f'''
<div class="in">
  <div class="eyebrow">The Tezoro process</div>
  <h2>Five steps,<br><em>one garment.</em></h2>
  <p class="b" style="max-width:520px">Bespoke takes a little longer than buying off the rack. Here is how your time is spent, and why it is worth it.</p>
  <div style="position:relative;margin-top:40px">
    <div style="position:absolute;left:27px;top:20px;bottom:40px;border-left:2px dashed {STONE}"></div>
    {''.join(f'<div style="display:grid;grid-template-columns:56px 1fr 60px;gap:24px;align-items:center;padding:16px 0;position:relative"><div style="width:56px;height:56px;border-radius:50%;background:{NAVY};color:{CHAMP};display:flex;align-items:center;justify-content:center;font-family:Corm;font-style:italic;font-size:24px">{n+1}</div><div style="border-bottom:1px solid {LINE};padding-bottom:16px"><div class="h4" style="font-size:27px">{a}</div><div class="sm" style="margin-top:6px;font-size:12.5px">{b}</div></div><div style="opacity:.9">{icon(i, 34, GOLD)}</div></div>' for n,(a,b,i) in enumerate(steps))}
  </div>
  <div class="sand" style="margin-top:20px;padding:20px 26px;display:flex;gap:16px;align-items:center">{icon('clock', 26, NAVY)}<div class="sm" style="color:{INK}">Most garments are ready in two to four weeks. For weddings, we recommend starting <b>eight to twelve weeks</b> before the first function.</div></div>
</div>''', label='Process')

# 7 cloth & craft -----------------------------------------------------
cloths = [('Wool suiting', NAVY, f'{twill()}'), ('Linen', '#D8CCB6', 'repeating-linear-gradient(0deg,rgba(0,0,0,.05) 0 1px,transparent 1px 3px),repeating-linear-gradient(90deg,rgba(0,0,0,.05) 0 1px,transparent 1px 4px)'),
          ('Cotton poplin', '#F7F5F0', 'repeating-linear-gradient(90deg,rgba(20,33,61,.05) 0 1px,transparent 1px 5px)'),
          ('Raw silk', '#C9B48E', 'repeating-linear-gradient(0deg,rgba(255,255,255,.12) 0 1px,transparent 1px 7px)'),
          ('Brocade', MAROON, pattern_arch(CHAMP, MAROON, 30)), ('Velvet', '#1E2B4A', 'radial-gradient(circle at 30% 20%,rgba(255,255,255,.12),transparent 60%)')]
page(f'''
<div class="in">
  <div class="eyebrow">Cloth &amp; craft</div>
  <h2>The details<br><em>you can feel.</em></h2>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:36px">
   {''.join(f'<div><div style="height:130px;background-color:{c};background-image:url({chr(39)}{noise(.12)}{chr(39)}),{t};border:1px solid {LINE}"></div><div class="caps" style="font-size:9.5px;margin-top:8px">{n}</div></div>' for n,c,t in cloths)}
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:30px 36px;margin-top:40px">
   {''.join(f'<div style="display:grid;grid-template-columns:30px 1fr;gap:12px"><span class="num" style="font-size:24px">{n}</span><div><div class="h4">{a}</div><div class="sm" style="margin-top:6px">{b}</div></div></div>' for n,a,b in [
     ('i','A pattern of your own','Drafted from your measurements and kept on file, so every new order starts from a perfect fit.'),
     ('ii','Hand-finished details','Buttonholes, collars and hems finished by hand where it matters most.'),
     ('iii','Your monogram','The Tezoro monogram, or your own initials, stitched inside every jacket.'),
     ('iv','Numbered labels','Each garment carries a woven label and a numbered care label: one of one.')])}
  </div>
  <div style="display:flex;gap:16px;margin-top:40px;align-items:stretch">
    <div style="flex:1">{M.embroidery_swatch(320, 180)}</div><div style="flex:1">{M.woven_swatch(320, 180)}</div></div>
</div>''', label='Cloth &amp; craft')

# 8 experience --------------------------------------------------------
page(f'''
<div class="in">
  <div class="eyebrow">The Tezoro experience</div>
  <h2>Remembered,<br><em>fitting by fitting.</em></h2>
  <p class="b" style="max-width:540px">From your first visit you have a Fitting Book with your measurements and garments, a cutter who knows your preferences, and appointment reminders on WhatsApp. When your garment is ready, it goes home in a breathable Tezoro garment bag on a wooden hanger.</p>
  <div style="position:relative;height:500px;margin-top:30px">
    <div style="position:absolute;left:0;top:10px">{M.bag(200, 420, NAVY, IVORY, CHAMP)}</div>
    <div style="position:absolute;left:250px;top:180px;transform:rotate(-4deg)">{M.bcard_front(280)}</div>
    <div style="position:absolute;left:330px;top:310px;transform:rotate(3deg)">{M.bcard_back(300)}</div>
    <div style="position:absolute;right:-10px;top:0">{M.box_svg(250)}</div>
  </div>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px;border-top:1px solid {LINE};padding-top:20px">
   {''.join(f'<div><div class="h4" style="font-size:21px">{a}</div><div class="sm" style="margin-top:4px">{b}</div></div>' for a,b in [('Private appointments','Weekday evenings and weekends'),('Aftercare','Pressing, repairs and re-fits'),('Gift cards','Give the gift of a first fitting')])}
  </div>
</div>''', label='Experience')

# 9 visit -------------------------------------------------------------
page(f'''
<div class="in">
  <div class="eyebrow">Visit the atelier</div>
  <h2>Come in for<br><em>a first fitting.</em></h2>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:36px;margin-top:36px">
    <div style="display:flex;flex-direction:column;gap:24px">
      {''.join(f'<div style="display:grid;grid-template-columns:34px 1fr;gap:14px">{icon(i, 26, GOLD)}<div><div class="caps" style="font-size:10px">{a}</div><div class="serif" style="font-size:19px;line-height:1.35;margin-top:4px">{b}</div></div></div>' for i,a,b in [
        ('pin','Address','Tezoro Atelier<br>Near Zudio, Pothencode<br>Thiruvananthapuram, Kerala'),
        ('clock','Hours','Monday to Saturday, 10 am – 9 pm<br>Sunday by appointment'),
        ('chat','Call or WhatsApp','+91 96335 98100'),
        ('calendar','Online','tezoro.in · @tezoro.atelier')])}
    </div>
    <div class="navy" style="position:relative;height:420px;overflow:hidden">
      <svg width="100%" height="100%" viewBox="0 0 320 420" style="position:absolute;inset:0">
        <g stroke="rgba(244,241,234,.14)" fill="none"><path d="M-10 120 C80 140 180 100 330 130" stroke-width="10"/><path d="M150 -10 C140 120 170 260 150 430" stroke-width="14"/>
        <path d="M-10 300 C100 280 200 320 330 290" stroke-width="6"/><path d="M60 -10 L90 430" stroke-width="4"/><path d="M260 -10 L230 430" stroke-width="4"/></g>
        <text x="160" y="30" fill="rgba(244,241,234,.45)" font-family="Inter" font-size="9" letter-spacing="2">MAIN ROAD</text>
        <rect x="170" y="160" width="48" height="26" fill="rgba(244,241,234,.15)"/><text x="176" y="177" fill="rgba(244,241,234,.6)" font-family="Inter" font-size="8">ZUDIO</text>
      </svg>
      <div style="position:absolute;left:96px;top:176px;display:flex;flex-direction:column;align-items:center">
        <div style="width:64px;height:64px;border-radius:50%;background:{CHAMP};display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 8px rgba(212,180,131,.25)">{L.inline(L.symbol, height=40, c=NAVY)}</div>
        <div style="width:2px;height:20px;background:{CHAMP}"></div>
        <div class="caps" style="font-size:9px;color:{CHAMP};margin-top:4px">Tezoro</div></div>
      <div style="position:absolute;left:0;right:0;bottom:0;padding:16px 20px;background:rgba(13,21,38,.7);font-size:11px;color:rgba(244,241,234,.75)">Pothencode, Thiruvananthapuram · next to Zudio</div>
    </div>
  </div>
  <div class="sand" style="margin-top:40px;padding:30px 34px;display:flex;justify-content:space-between;align-items:center">
    <div><div class="serif" style="font-size:28px;line-height:1.1;color:{NAVY}">Book a private consultation</div><div class="sm" style="margin-top:6px;color:{INK}">Message us on WhatsApp with your preferred day and time.</div></div>
    <span class="caps" style="background:{NAVY};color:{IVORY};padding:14px 22px;font-size:10px">Book a fitting</span></div>
</div>''', label='Visit')

# 10 back cover -------------------------------------------------------
page(f'''
<div style="position:absolute;inset:0;background:{pattern_monogram(CHAMP, NAVY, 60, .35)};opacity:.25"></div>
<div class="flex col center" style="position:absolute;inset:0;text-align:center">
  {L.inline(L.seal, height=200, c=CHAMP)}
  <div class="serif" style="font-size:44px;margin-top:46px">Made for you, <em style="color:{CHAMP}">only you.</em></div>
  <div class="caps" style="font-size:10px;margin-top:20px;color:{CHAMP}">tezoro.in · @tezoro.atelier · Pothencode</div>
</div>''', 'navy', foot=False)

html = f'<!doctype html><html><head><meta charset="utf-8"><title>Tezoro Company Profile</title><style>{CSS}{M.CSS}</style></head><body>{M.DEFS}{"".join(PAGES)}</body></html>'
open('profile.html', 'w').write(html)
print(len(PAGES), 'pages')
