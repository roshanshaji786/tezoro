"""Drawn mockups (HTML + inline SVG) of the Tezoro identity in use.
Every scene returns the inner HTML of one 1600 x 900 slide."""
from common import *
import logos as L

SYM = L.symbol_body
MONO = L.monogram_body

# shared SVG defs: satin-stitch fills, metal and wood gradients
DEFS = f'''<svg width="0" height="0" style="position:absolute"><defs>
<pattern id="satG" width="2.4" height="2.4" patternUnits="userSpaceOnUse" patternTransform="rotate(38)">
  <rect width="2.4" height="2.4" fill="#C8A86F"/><rect width="2.4" height="1.1" fill="#EBD5A6"/></pattern>
<pattern id="satG2" width="2.4" height="2.4" patternUnits="userSpaceOnUse" patternTransform="rotate(-38)">
  <rect width="2.4" height="2.4" fill="#C3A26A"/><rect width="2.4" height="1.1" fill="#E6CF9E"/></pattern>
<pattern id="satN" width="2.2" height="2.2" patternUnits="userSpaceOnUse" patternTransform="rotate(38)">
  <rect width="2.2" height="2.2" fill="#101B33"/><rect width="2.2" height="1" fill="#2A3A5E"/></pattern>
<pattern id="satI" width="2.4" height="2.4" patternUnits="userSpaceOnUse" patternTransform="rotate(38)">
  <rect width="2.4" height="2.4" fill="#E3DDD0"/><rect width="2.4" height="1.1" fill="#FFFDF7"/></pattern>
<linearGradient id="foil" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0" stop-color="#E9D3A2"/><stop offset=".35" stop-color="#C9A35E"/><stop offset=".55" stop-color="#F3E2B8"/><stop offset=".8" stop-color="#B8893E"/><stop offset="1" stop-color="#D9BC80"/></linearGradient>
<linearGradient id="wood" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#9A6B43"/><stop offset=".5" stop-color="#7A4F2E"/><stop offset="1" stop-color="#5C3A21"/></linearGradient>
<linearGradient id="chrome" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0" stop-color="#8C8C8C"/><stop offset=".5" stop-color="#F2F2F2"/><stop offset="1" stop-color="#7A7A7A"/></linearGradient>
<radialGradient id="horn" cx=".4" cy=".35" r=".8">
  <stop offset="0" stop-color="#5A4636"/><stop offset=".6" stop-color="#2E231B"/><stop offset="1" stop-color="#17110D"/></radialGradient>
<radialGradient id="gold" cx=".35" cy=".3" r=".9">
  <stop offset="0" stop-color="#F6E7C1"/><stop offset=".45" stop-color="#D4B06A"/><stop offset="1" stop-color="#8E6A2C"/></radialGradient>
<filter id="stitch" x="-10%" y="-10%" width="120%" height="120%">
  <feDropShadow dx="0.5" dy="0.9" stdDeviation="0.6" flood-color="#000" flood-opacity=".55"/></filter>
<filter id="glow" x="-30%" y="-30%" width="160%" height="160%">
  <feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs></svg>'''

CSS = f"""
.wlabel{{position:relative;background-color:{NAVY};background-image:{weave()};display:flex;align-items:center;justify-content:center;
  box-shadow:0 2px 3px rgba(0,0,0,.25),0 10px 18px -8px rgba(0,0,0,.35);border-radius:1px}}
.wlabel:before,.wlabel:after{{content:"";position:absolute;top:6%;bottom:6%;width:0;border-left:2px dashed rgba(255,255,255,.35)}}
.wlabel:before{{left:9px}}.wlabel:after{{right:9px}}
.board{{background:{STONE} url("{noise(.14, 1.2)}")}}
.shirting{{background:#FBFAF7 url("{noise(.05, 1.4)}");background-image:url("{noise(.05, 1.4)}"),repeating-linear-gradient(90deg,rgba(20,33,61,.045) 0 1px,transparent 1px 6px)}}
.suiting{{background-color:{NAVY};background-image:url("{noise(.18, 1.1)}"),{twill()}}}
.lbl{{font-family:Cinz;font-size:10.5px;letter-spacing:.24em;text-transform:uppercase;opacity:.6}}
.phone{{background:#0B0B0D;border-radius:46px;padding:12px;box-shadow:0 40px 80px -30px rgba(0,0,0,.6),inset 0 0 0 2px #2A2A2E}}
.phone .scr{{border-radius:36px;overflow:hidden;position:relative;height:100%}}
"""


def sym_svg(size, fill, eye=True, filt=None, extra=''):
    f = f' filter="url(#{filt})"' if filt else ''
    return (f'<svg viewBox="-4 -4 108 108" width="{size}" height="{size}" style="display:block;overflow:visible{extra}">'
            f'<g fill="{fill}"{f}>{SYM(eye)}</g></svg>')


def mono_svg(size, fill, eye=False, filt=None):
    f = f' filter="url(#{filt})"' if filt else ''
    return (f'<svg viewBox="0 0 100 100" width="{size}" height="{size}" style="display:block;overflow:visible">'
            f'<g fill="{fill}"{f}>{MONO(eye)}</g></svg>')


def debossed(size, base, hi, lo, mono=False, eye=True):
    body = MONO(eye) if mono else SYM(eye)
    return (f'<svg viewBox="-4 -4 108 108" width="{size}" height="{size}" style="display:block">'
            f'<g fill="{hi}" transform="translate(.8 .9)">{body}</g><g fill="{lo}" transform="translate(-.6 -.7)">{body}</g>'
            f'<g fill="{base}">{body}</g></svg>')


def text_block(eyebrow, title, body, w=420, dark=False):
    c = 'rgba(244,241,234,.72)' if dark else MUTED
    return (f'<div style="width:{w}px"><div class="eyebrow">{eyebrow}</div><h2>{title}</h2>'
            f'<p class="lead" style="color:{c};max-width:{w}px">{body}</p></div>')


def caption(t, dark=False):
    return f'<div class="lbl" style="margin-top:14px;color:{IVORY if dark else INK}">{t}</div>'


# ---------------------------------------------------------------- swatches
def embroidery_swatch(w, h):
    return f'''<div class="suiting" style="height:{h}px;display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden">
  <div style="position:absolute;inset:0;background:radial-gradient(circle at 40% 30%,rgba(255,255,255,.08),rgba(0,0,0,.35))"></div>
  <div style="position:relative">{sym_svg(170, 'url(#satG)', filt='stitch')}</div></div>'''


def woven_swatch(w, h):
    return f'''<div class="sand" style="height:{h}px;display:flex;align-items:center;justify-content:center">
  <div class="wlabel" style="width:270px;height:96px">{L.inline(L.wordmark, width=170, c1=CHAMP, c2=CHAMP)}</div></div>'''


def leather_swatch(w, h):
    return f'''<div style="height:{h}px;display:flex;align-items:center;justify-content:center;background:#8A5A3B url('{noise(.25, .8)}');position:relative">
  <div style="position:absolute;inset:16px;border:2px dashed rgba(240,220,190,.35);border-radius:6px"></div>
  {debossed(150, '#77492D', 'rgba(255,230,200,.35)', 'rgba(40,20,8,.6)')}</div>'''


def engraved_swatch(w, h):
    holes = ''.join(f'<circle cx="{x}" cy="{y}" r="3.4" fill="#0E0A08"/>' for x, y in [(92, 92), (108, 92), (92, 108), (108, 108)])
    return f'''<div class="paper" style="height:{h}px;display:flex;align-items:center;justify-content:center;gap:26px">
  <svg viewBox="0 0 200 200" width="150" height="150"><circle cx="100" cy="100" r="92" fill="url(#horn)"/>
   <circle cx="100" cy="100" r="80" fill="none" stroke="rgba(255,255,255,.08)" stroke-width="5"/>
   <g transform="translate(64 40) scale(.72)" fill="#120D0A"><g transform="translate(.8 .8)" fill="rgba(255,255,255,.12)">{MONO(False)}</g>{MONO(False)}</g>
   {''.join(f'<circle cx="{x}" cy="{y}" r="3.6" fill="#0E0A08"/>' for x, y in [(90, 150), (110, 150)])}</svg>
  <svg viewBox="0 0 200 200" width="96" height="96"><circle cx="100" cy="100" r="92" fill="url(#gold)"/>
   <circle cx="100" cy="100" r="78" fill="none" stroke="rgba(90,60,20,.35)" stroke-width="4"/>
   <g transform="translate(55 52) scale(.9)" fill="rgba(110,75,25,.85)">{MONO(False)}</g></svg></div>'''


# ---------------------------------------------------------------- labels
def labels_scene():
    collar = f'''
<div style="position:absolute;right:0;top:0;width:900px;height:900px;overflow:hidden">
  <div class="shirting" style="position:absolute;inset:0"></div>
  <svg width="900" height="900" style="position:absolute;inset:0">
    <path d="M-20 120 C200 320 700 320 920 120 L920 0 L-20 0 Z" fill="#F3F1EC"/>
    <path d="M-20 120 C200 320 700 320 920 120" fill="none" stroke="rgba(20,33,61,.12)" stroke-width="2"/>
    <path d="M-20 150 C200 350 700 350 920 150" fill="none" stroke="rgba(20,33,61,.10)" stroke-width="1.5" stroke-dasharray="6 5"/>
    <path d="M-20 120 C200 320 700 320 920 120 L920 150 C700 350 200 350 -20 150 Z" fill="rgba(0,0,0,.03)"/>
  </svg>
  <div class="wlabel" style="position:absolute;left:230px;top:250px;width:460px;height:140px">{L.inline(L.wordmark, width=290, c1=CHAMP, c2=CHAMP)}</div>
  <div style="position:absolute;left:420px;top:390px;width:84px;height:330px;background:#fff url('{noise(.04)}');box-shadow:0 6px 12px -6px rgba(0,0,0,.3);padding:16px 6px;font-size:8.5px;line-height:1.5;color:#555;text-align:center;transform:rotate(1deg)">
    <div style="font-family:Cinz;font-size:7px;letter-spacing:.1em;color:{NAVY}">TEZORO</div><div style="height:1px;background:#ddd;margin:6px 0"></div>
    100% WOOL<br>SUPER 120s<br><br>DRY CLEAN<br>ONLY<br><br><span style="font-size:13px;letter-spacing:4px">◯ ✕ ▢</span><br><br>MADE IN<br>KERALA<br>INDIA<br><br>No. 0147</div>
  <div class="wlabel" style="position:absolute;left:330px;top:400px;width:74px;height:74px;flex-direction:column;gap:3px">{mono_svg(24, IVORY)}<span style="font-family:Corm;font-size:20px;color:{IVORY};line-height:1">40</span></div>
</div>'''
    loose = f'''
<div style="position:absolute;left:72px;bottom:110px;display:flex;gap:26px;align-items:end">
  <div><div class="wlabel" style="width:200px;height:200px;border-radius:50%">
    <svg width="160" height="160" viewBox="0 0 400 400">{L.seal(c=CHAMP)[0]}</svg></div>{caption('Blazer lining patch · 35 mm')}</div>
  <div><div class="wlabel" style="width:230px;height:76px;background-color:{IVORY};background-image:{weave('rgba(0,0,0,.04)','rgba(0,0,0,.05)')}">
    {L.inline(L.horizontal, width=150, c1=NAVY, c2=NAVY)}</div>{caption('Trouser waistband · 45 mm')}</div>
</div>'''
    return f'''<div class="pad" style="right:auto;width:560px">{text_block('Woven labels', 'Sewn into <em>every piece.</em>', 'Damask-woven neck labels in navy and champagne, a size tab with the monogram, and a numbered care label, because each garment is one of one.', 520)}</div>{collar}{loose}'''


# ---------------------------------------------------------------- embroidery
def embroidery_scene():
    holes = ''.join(f'<circle cx="{x}" cy="{y}" r="3.2" fill="#C9C3B6"/>' for x, y in [(-5, -5), (5, -5), (-5, 5), (5, 5)])
    cuff = f'''
<div style="position:relative;width:100%;height:330px;overflow:hidden">
  <div class="shirting" style="position:absolute;inset:0"></div>
  <svg width="430" height="330" style="position:absolute;inset:0">
    <rect x="0" y="70" width="430" height="200" fill="#F7F5F0"/>
    <line x1="0" y1="70" x2="430" y2="70" stroke="rgba(0,0,0,.14)" stroke-width="2"/>
    <line x1="0" y1="82" x2="430" y2="82" stroke="rgba(0,0,0,.12)" stroke-dasharray="5 4"/>
    <line x1="0" y1="258" x2="430" y2="258" stroke="rgba(0,0,0,.12)" stroke-dasharray="5 4"/>
    <line x1="0" y1="270" x2="430" y2="270" stroke="rgba(0,0,0,.16)" stroke-width="2"/>
    <rect x="0" y="270" width="430" height="60" fill="rgba(0,0,0,.04)"/>
    <g transform="translate(330 170)"><circle r="20" fill="#FBFAF6" stroke="#D9D3C6" stroke-width="2.5"/>{holes}</g>
    <rect x="232" y="165" width="58" height="10" rx="5" fill="none" stroke="#D3CCBD" stroke-width="2.5"/>
    <g transform="translate(70 125) scale(.85)" fill="url(#satN)" filter="url(#stitch)">{MONO(False)}</g>
  </svg></div>'''
    btn = lambda s, x: f'''<svg viewBox="0 0 200 200" width="{s}" height="{s}"><circle cx="100" cy="100" r="94" fill="url(#horn)"/>
   <circle cx="100" cy="100" r="80" fill="none" stroke="rgba(255,255,255,.07)" stroke-width="6"/>
   <g transform="translate(60 38) scale(.8)"><g transform="translate(1 1)" fill="rgba(255,255,255,.14)">{MONO(False)}</g><g fill="#0F0B08">{MONO(False)}</g></g>
   <circle cx="90" cy="152" r="4" fill="#0E0A08"/><circle cx="110" cy="152" r="4" fill="#0E0A08"/></svg>'''
    link = lambda: f'''<svg viewBox="0 0 160 200" width="130" height="162"><rect x="10" y="10" width="140" height="140" rx="22" fill="url(#gold)"/>
   <rect x="22" y="22" width="116" height="116" rx="14" fill="none" stroke="rgba(110,75,25,.35)" stroke-width="3"/>
   <g transform="translate(38 36) scale(.84)" fill="rgba(105,70,22,.9)">{MONO(False)}</g>
   <rect x="72" y="150" width="16" height="40" rx="4" fill="url(#chrome)"/></svg>'''
    return f'''
<div class="pad" style="display:grid;grid-template-columns:400px 1fr;gap:50px;top:120px">
  <div>{text_block('Embroidery &amp; trims', 'The mark, <em>in thread.</em>', 'Satin-stitched in champagne on suiting, tonal navy on a shirt cuff, and engraved into horn buttons and cufflinks. The small cut keeps every edge crisp at 8 mm.', 390, True)}</div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px">
    <div><div class="suiting" style="height:560px;position:relative;display:flex;align-items:center;justify-content:center;overflow:hidden">
       <div style="position:absolute;inset:0;background:radial-gradient(circle at 35% 30%,rgba(255,255,255,.10),rgba(0,0,0,.45))"></div>
       <div style="position:absolute;left:0;right:0;top:70px;height:0;border-top:2px dashed rgba(212,180,131,.35)"></div>
       <div style="position:relative">{sym_svg(300, 'url(#satG)', filt='stitch')}</div></div>{caption('Satin-stitch patch on suiting', True)}</div>
    <div><div style="display:grid;grid-template-rows:330px 210px;gap:20px;height:560px">
       <div style="overflow:hidden;position:relative">{cuff}</div>
       <div class="paper" style="display:flex;align-items:center;justify-content:center;gap:24px">{btn(130,0)}{btn(90,0)}{link()}</div></div>
       {caption('Cuff monogram · engraved horn buttons · cufflinks', True)}</div>
  </div></div>'''


# ---------------------------------------------------------------- hang tags
def hangtag_scene():
    def tag(content, rot, x, y, w=300, h=500, bg='board'):
        return f'''<div style="position:absolute;left:{x}px;top:{y}px;transform:rotate({rot}deg);transform-origin:50% 0">
  <div class="{bg} shadow" style="width:{w}px;height:{h}px;border-radius:{w/2}px {w/2}px 6px 6px;position:relative;display:flex;flex-direction:column;align-items:center;padding-top:{w*.32}px">
   <div style="position:absolute;top:{w*.16}px;left:50%;width:22px;height:22px;margin-left:-11px;border-radius:50%;background:#E9E4DA;box-shadow:inset 0 2px 3px rgba(0,0,0,.4)"></div>
   <div style="position:absolute;inset:12px;border-radius:{w/2-12}px {w/2-12}px 2px 2px;border:1.5px dashed rgba(20,33,61,.28)"></div>
   {content}</div></div>'''
    front = f'<div style="margin-top:60px">{L.inline(L.stacked, width=200, c1=NAVY, c2=NAVY)}</div>'
    back = f'''<div style="width:220px;color:{NAVY};text-align:center">
     <div style="margin-top:14px;display:flex;justify-content:center">{mono_svg(34, NAVY)}</div>
     <div class="caps" style="font-size:10px;margin-top:22px">Made for</div>
     <div class="serif it" style="font-size:30px;margin-top:6px;border-bottom:1px solid rgba(20,33,61,.4);padding-bottom:4px">Mr. Arun Nair</div>
     <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:22px;text-align:left;font-size:11px">
       <div><div class="caps" style="font-size:8.5px;opacity:.7">Order</div><div style="font-size:15px;margin-top:3px">TZ-0147</div></div>
       <div><div class="caps" style="font-size:8.5px;opacity:.7">Fitting</div><div style="font-size:15px;margin-top:3px">2nd</div></div>
       <div><div class="caps" style="font-size:8.5px;opacity:.7">Cloth</div><div style="font-size:15px;margin-top:3px">Wool 120s</div></div>
       <div><div class="caps" style="font-size:8.5px;opacity:.7">Cutter</div><div style="font-size:15px;margin-top:3px">S.</div></div></div>
     <div class="serif it" style="font-size:18px;margin-top:26px;opacity:.85">Made for you, only you.</div></div>'''
    string = '''<svg width="1600" height="900" style="position:absolute;left:0;top:0;z-index:4;overflow:visible;pointer-events:none">
     <path d="M916 249 C895 150 990 70 1085 92 C1170 112 1258 175 1255 279" fill="none" stroke="#1B1B1B" stroke-width="6" stroke-linecap="round"/>
     <path d="M1085 92 C1110 40 1160 34 1205 58 M1085 92 C1060 46 1020 40 985 52" fill="none" stroke="#1B1B1B" stroke-width="6" stroke-linecap="round"/>
     <circle cx="1085" cy="92" r="8" fill="#1B1B1B"/></svg>'''
    sticker = f'''<div style="position:absolute;left:1360px;top:640px">
      <div class="shadow" style="width:150px;height:150px;border-radius:50%;background:{NAVY};display:flex;align-items:center;justify-content:center">
      <svg width="128" height="128" viewBox="0 0 400 400">{L.seal(c=CHAMP)[0]}</svg></div>{caption('Seal sticker · 50 mm')}</div>'''
    return f'''<div class="pad" style="right:auto;width:520px">{text_block('Hang tags', 'Signed, <em>for one man.</em>', 'The arched tag from the mood board, on taupe board with a black grosgrain cord. The front carries the stacked logo; the back is written by hand with the client\'s name and order.', 470)}</div>
    {tag(front, -6, 760, 190)}{tag(back, 5, 1110, 220)}{string}{sticker}'''


# ---------------------------------------------------------------- garment bag
def hanger(w=300):
    return f'''<svg viewBox="0 0 300 120" width="{w}" height="{w*.4}" style="display:block;overflow:visible">
   <path d="M150 50 V26 a14 14 0 1 0 -14 -14" fill="none" stroke="url(#chrome)" stroke-width="5" stroke-linecap="round"/>
   <path d="M12 110 Q20 92 150 52 Q280 92 288 110 Q290 118 280 118 H20 Q10 118 12 110 Z" fill="url(#wood)"/>
   <g transform="translate(140 84) scale(.2)" fill="rgba(40,22,10,.55)">{MONO(False)}</g></svg>'''


def bag(w, h, bg, c1, c2, sub='ATELIER', zip_c='rgba(212,180,131,.55)'):
    return f'''<div style="position:relative;width:{w}px">
  <div style="display:flex;justify-content:center;margin-bottom:-26px;position:relative;z-index:2">{hanger(w*.78)}</div>
  <div class="shadow" style="width:{w}px;height:{h}px;background:{bg} url('{noise(.16)}');clip-path:polygon(28% 0,72% 0,100% 7%,100% 100%,0 100%,0 7%);position:relative">
    <div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,0,0,.25),rgba(255,255,255,.06) 30%,rgba(0,0,0,0) 55%,rgba(0,0,0,.28))"></div>
    <div style="position:absolute;left:50%;top:9%;bottom:3%;border-left:3px dotted {zip_c}"></div>
    <div style="position:absolute;left:0;right:0;top:20%;display:flex;justify-content:center"><div style="background:{bg};padding:14px 18px;box-shadow:0 0 0 1px rgba(0,0,0,.04)">{L.inline(L.stacked, width=w*.44, c1=c1, c2=c2, subtext=sub)}</div></div>
    <div style="position:absolute;left:0;right:0;bottom:6%;text-align:center;font-family:Corm;font-style:italic;font-size:{w*.06}px;color:{c2};opacity:.8">Made for you, only you.</div>
  </div></div>'''


def garmentbag_scene():
    return f'''<div class="pad" style="right:auto;width:470px">{text_block('Garment bags', 'Carried home <em>with care.</em>', 'Breathable navy suit carriers with a centre zip and a champagne stacked logo, on a solid wood hanger engraved with the monogram. Ivory for shirts, maroon for the wedding floor.', 440)}</div>
  <div style="position:absolute;left:640px;top:96px;display:flex;gap:40px;align-items:start">
    <div style="margin-top:110px">{bag(230, 500, IVORY, NAVY, GOLD, zip_c='rgba(20,33,61,.4)')}</div>
    <div>{bag(310, 610, NAVY, IVORY, CHAMP)}</div>
    <div style="margin-top:60px">{bag(250, 550, MAROON, CHAMP, CHAMP, 'WEDDING')}</div>
  </div>'''


# ---------------------------------------------------------------- packaging
def box_svg(w=560):
    # isometric shirt box: lid top, front and side faces
    pat = pattern_monogram(CHAMP, NAVY, 40, .0)
    return f'''<svg viewBox="0 0 560 420" width="{w}" height="{w*.75}" style="display:block;overflow:visible">
  <defs><linearGradient id="lidtop" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1E2D4F"/><stop offset="1" stop-color="#121C33"/></linearGradient></defs>
  <ellipse cx="290" cy="395" rx="260" ry="26" fill="rgba(0,0,0,.18)"/>
  <path d="M40 170 L300 260 L300 390 L40 300 Z" fill="#0F1A30"/>
  <path d="M300 260 L530 160 L530 290 L300 390 Z" fill="#0B1427"/>
  <path d="M40 170 L270 70 L530 160 L300 260 Z" fill="url(#lidtop)"/>
  <path d="M40 170 L300 260 L300 286 L40 196 Z" fill="#17254A"/>
  <path d="M300 260 L530 160 L530 186 L300 286 Z" fill="#101C38"/>
  <!-- ribbon -->
  <path d="M141.2 126 L168.8 114 L428.8 204 L401.2 216 Z" fill="{CHAMP}"/>
  <path d="M401.2 216 L428.8 204 L428.8 334 L401.2 346 Z" fill="#A98B5C"/>
  <path d="M155.8 210.1 L184.2 219.9 L414.2 119.9 L385.8 110.1 Z" fill="#E3C89A"/>
  <path d="M155.8 210.1 L184.2 219.9 L184.2 349.9 L155.8 340.1 Z" fill="#BE9F6C"/>
  <!-- seal -->
  <g transform="translate(285 164) scale(1 .55) rotate(0)"><circle r="46" fill="url(#foil)"/><circle r="40" fill="none" stroke="rgba(110,75,25,.4)" stroke-width="2"/>
   <g transform="translate(-30 -30) scale(.6)" fill="rgba(90,60,20,.85)">{SYM(False)}</g></g>
  <g transform="translate(60 0) "></g>
</svg>'''


def shopper(w, bg, c1, c2, sub='ATELIER'):
    h = w * 1.18
    return f'''<div style="position:relative;width:{w*1.22}px;height:{h+90}px">
  <svg width="{w*1.22}" height="{h+90}" style="position:absolute;inset:0;overflow:visible">
    <ellipse cx="{w*.62}" cy="{h+82}" rx="{w*.62}" ry="14" fill="rgba(0,0,0,.16)"/>
    <path d="M{w*.25} 92 C{w*.25} 10 {w*.75} 10 {w*.75} 92" fill="none" stroke="{c2}" stroke-width="5"/>
    <path d="M{w} 80 L{w*1.22} 70 L{w*1.22} {h+60} L{w} {h+80} Z" fill="{bg}" style="filter:brightness(.72)"/>
    <path d="M{w} 80 L{w*1.11} 75 L{w*1.11} {h+70} L{w} {h+80} Z" fill="rgba(0,0,0,.18)"/>
  </svg>
  <div style="position:absolute;left:0;top:80px;width:{w}px;height:{h}px;background:{bg} url('{noise(.12)}');display:flex;flex-direction:column;align-items:center;justify-content:center">
    <div style="position:absolute;inset:0;background:linear-gradient(100deg,rgba(255,255,255,.08),rgba(0,0,0,.12))"></div>
    <div style="position:absolute;top:0;left:0;right:0;height:46px;background:rgba(0,0,0,.08)"></div>
    {L.inline(L.stacked, width=w*.5, c1=c1, c2=c2, subtext=sub)}
  </div></div>'''


def packaging_scene():
    tissue = f'''<div style="position:absolute;left:72px;bottom:110px;width:420px;height:230px;background:{pattern_monogram(NAVY, '#ECE6DA', 46, .18)};transform:rotate(-4deg)" class="shadow"></div>'''
    return f'''<div class="pad" style="right:auto;width:470px">{text_block('Packaging', 'Unboxed like <em>a gift.</em>', 'Rigid navy shirt and suit boxes with a champagne grosgrain ribbon and a foil seal, monogram tissue inside, and paper carriers with cord handles.', 440)}</div>
  {tissue}
  <div style="position:absolute;left:560px;top:250px">{box_svg(560)}</div>
  <div style="position:absolute;left:1150px;top:170px">{shopper(280, NAVY, IVORY, CHAMP)}</div>'''


# ---------------------------------------------------------------- stationery
def bcard_front(w=420):
    h = w * .583
    return f'''<div class="shadow" style="width:{w}px;height:{h}px;background:{NAVY} url('{noise(.12)}');display:flex;align-items:center;justify-content:center;border-radius:4px">
    <svg viewBox="-4 -4 108 108" width="{h*.42}" height="{h*.42}"><g fill="url(#foil)">{SYM()}</g></svg></div>'''


def bcard_back(w=420):
    h = w * .583
    return f'''<div class="shadow" style="width:{w}px;height:{h}px;background:{IVORY} url('{noise(.05)}');border-radius:4px;padding:{w*.075}px;display:flex;flex-direction:column;justify-content:space-between;color:{NAVY}">
    <div style="display:flex;justify-content:space-between;align-items:start">
      <div><div class="serif" style="font-size:{w*.075}px;line-height:1">Safnal</div><div class="caps" style="font-size:{w*.022}px;color:{GOLD};margin-top:8px">Founder</div></div>
      {L.inline(L.symbol, height=w*.09, c=NAVY)}</div>
    <div style="font-size:{w*.027}px;line-height:1.7">+91 00000 00000<br>hello@tezoro.in · tezoro.in<br>Near Zudio, Pothencode, Thiruvananthapuram</div></div>'''


def letterhead(w=440):
    h = w * 1.414
    return f'''<div class="shadow" style="width:{w}px;height:{h}px;background:#FDFBF6 url('{noise(.04)}');padding:{w*.09}px;position:relative;color:{INK}">
   <div style="display:flex;justify-content:space-between;align-items:center">{L.inline(L.horizontal, width=w*.42, c1=NAVY, c2=GOLD)}
     <div style="font-size:{w*.019}px;text-align:right;line-height:1.6;color:{MUTED}">Near Zudio, Pothencode<br>Thiruvananthapuram, Kerala<br>+91 00000 00000</div></div>
   <div style="height:1px;background:{GOLD};margin:{w*.05}px 0;opacity:.6"></div>
   <div style="font-size:{w*.022}px;line-height:1.8;color:{MUTED}">27 October 2026<br><br><span style="color:{INK}">Dear Mr. Arun,</span><br><br>
   {''.join(f'<div style="height:{w*.012}px;background:#E9E3D8;margin:{w*.022}px 0;width:{x}%"></div>' for x in [100,96,100,88,100,92,60])}
   <br><span class="serif it" style="font-size:{w*.05}px;color:{NAVY}">Safnal</span></div>
   <div style="position:absolute;left:{w*.09}px;right:{w*.09}px;bottom:{w*.06}px;display:flex;justify-content:space-between;align-items:center;font-size:{w*.017}px;color:{MUTED}">
     <span class="caps" style="font-size:{w*.016}px">Made for you, only you.</span>{L.inline(L.monogram, height=w*.04, c=GOLD, eye=False)}<span>tezoro.in</span></div></div>'''


def envelope(w=440):
    h = w * .5
    return f'''<div class="shadow" style="width:{w}px;height:{h}px;background:{NAVY} url('{noise(.12)}');position:relative;overflow:hidden">
    <svg width="{w}" height="{h}" style="position:absolute;inset:0"><path d="M0 0 L{w/2} {h*.58} L{w} 0" fill="rgba(0,0,0,.18)" stroke="rgba(255,255,255,.06)"/></svg>
    <div style="position:absolute;left:{w/2-36}px;top:{h*.58-36}px;width:72px;height:72px;border-radius:50%;background:{MAROON};box-shadow:0 3px 6px rgba(0,0,0,.4);display:flex;align-items:center;justify-content:center">
      <svg viewBox="0 0 400 400" width="62" height="62">{L.seal(c='#3E0F18')[0]}</svg></div></div>'''


def stationery_scene():
    return f'''<div class="pad" style="right:auto;width:440px">{text_block('Stationery', 'Paper that <em>feels tailored.</em>', 'Heavy cotton card with champagne foil on navy, letterhead with a single gold rule, and envelopes closed with a maroon wax seal.', 420)}</div>
  <div style="position:absolute;left:560px;top:120px;transform:rotate(-3deg)">{letterhead(420)}</div>
  <div style="position:absolute;left:1030px;top:130px;transform:rotate(4deg)">{bcard_front(400)}</div>
  <div style="position:absolute;left:1060px;top:390px;transform:rotate(-2deg)">{bcard_back(400)}</div>
  <div style="position:absolute;left:1020px;top:650px;transform:rotate(1.5deg)">{envelope(430)}</div>'''


# ---------------------------------------------------------------- storefront
def mannequin(x, h, jacket=NAVY):
    w = h * .42
    return f'''<g transform="translate({x} 0)">
    <rect x="{-3}" y="{560-h*.08}" width="6" height="{h*.08}" fill="#222"/>
    <ellipse cx="0" cy="560" rx="{w*.45}" ry="5" fill="#1A1A1A"/>
    <path d="M{-w*.5} {560-h*.95} Q0 {560-h*1.05} {w*.5} {560-h*.95} L{w*.42} {560-h*.45} L{w*.36} {560-h*.1} L{-w*.36} {560-h*.1} L{-w*.42} {560-h*.45} Z" fill="{jacket}"/>
    <path d="M{-w*.12} {560-h*1.0} L0 {560-h*.7} L{w*.12} {560-h*1.0}" fill="#EDE6D6"/>
    <path d="M{-w*.15} {560-h*.99} L{-w*.02} {560-h*.62} L{-w*.2} {560-h*.84} Z M{w*.15} {560-h*.99} L{w*.02} {560-h*.62} L{w*.2} {560-h*.84} Z" fill="rgba(0,0,0,.25)"/>
    <rect x="-8" y="{560-h*1.1}" width="16" height="{h*.08}" fill="#C8BFAF"/></g>'''


def store_scene():
    W = 1456
    fascia = L.inline(L.horizontal, width=560, c1=CHAMP, c2=CHAMP)
    return f'''
<div style="position:absolute;left:72px;right:72px;top:96px;bottom:104px;overflow:hidden;background:#2B2A2E url('{noise(.2, .6)}')">
  <div style="position:absolute;inset:0;background:repeating-linear-gradient(0deg,rgba(255,255,255,.025) 0 2px,transparent 2px 60px)"></div>
  <!-- fascia -->
  <div style="position:absolute;left:120px;right:120px;top:40px;height:150px;background:{NAVY} url('{noise(.14)}');box-shadow:0 20px 40px rgba(0,0,0,.6);display:flex;align-items:center;justify-content:center">
    <div style="filter:drop-shadow(0 0 10px rgba(233,206,150,.75)) drop-shadow(0 0 26px rgba(233,206,150,.35))">{fascia}</div>
    {''.join(f'<div style="position:absolute;top:-28px;left:{p}%;width:22px;height:28px;background:#1a1a1a"></div><div style="position:absolute;top:-4px;left:calc({p}% - 30px);width:82px;height:120px;background:radial-gradient(ellipse at top,rgba(255,236,200,.18),transparent 70%)"></div>' for p in (20, 50, 80))}
  </div>
  <!-- blade sign -->
  <div style="position:absolute;right:40px;top:230px;width:10px;height:14px;background:#111"></div>
  <div style="position:absolute;right:20px;top:240px;width:50px;height:4px;background:#111"></div>
  <div style="position:absolute;right:0;top:246px;width:120px;height:120px;border-radius:50%;background:{NAVY};display:flex;align-items:center;justify-content:center;box-shadow:0 10px 20px rgba(0,0,0,.6)">
    <svg viewBox="0 0 400 400" width="104" height="104" style="filter:drop-shadow(0 0 6px rgba(233,206,150,.8))">{L.seal(c=CHAMP)[0]}</svg></div>
  <!-- windows -->
  <svg width="{W}" height="620" style="position:absolute;left:0;top:200px"><g transform="translate(109 0) scale(.85)">
    <defs><linearGradient id="warm" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F3E3C3"/><stop offset=".55" stop-color="#D9BE90"/><stop offset="1" stop-color="#8C6E48"/></linearGradient>
    <radialGradient id="spot" cx=".5" cy="0" r=".9"><stop offset="0" stop-color="rgba(255,250,235,.9)"/><stop offset="1" stop-color="rgba(255,250,235,0)"/></radialGradient></defs>
    <rect x="160" y="10" width="440" height="560" fill="url(#warm)"/><rect x="160" y="10" width="440" height="300" fill="url(#spot)"/>
    <rect x="856" y="10" width="440" height="560" fill="url(#warm)"/><rect x="856" y="10" width="440" height="300" fill="url(#spot)"/>
    <rect x="640" y="10" width="176" height="560" fill="#3A2E22"/>
    <rect x="650" y="20" width="156" height="550" fill="url(#warm)" opacity=".9"/>
    {mannequin(290, 380)}{mannequin(470, 400, MAROON)}{mannequin(1000, 390, '#2A2A2A')}{mannequin(1170, 370)}
    <rect x="156" y="6" width="448" height="568" fill="none" stroke="#151515" stroke-width="10"/>
    <rect x="852" y="6" width="448" height="568" fill="none" stroke="#151515" stroke-width="10"/>
    <rect x="644" y="14" width="168" height="560" fill="none" stroke="#151515" stroke-width="8"/>
    <rect x="790" y="270" width="6" height="90" rx="3" fill="url(#chrome)"/>
    <path d="M160 10 L380 10 L160 300 Z" fill="rgba(255,255,255,.08)"/><path d="M856 10 L1090 10 L856 320 Z" fill="rgba(255,255,255,.08)"/>
    <rect x="-200" y="574" width="{W+400}" height="60" fill="#1A1A1C"/>
  </g></svg>
  <div style="position:absolute;left:672px;top:270px;width:96px;text-align:center;color:{NAVY}">
    {L.inline(L.symbol, height=50, c=NAVY)}<div class="caps" style="font-size:7px;margin-top:10px;letter-spacing:.18em;line-height:1.8">Open daily<br>10 am – 9 pm<br>By appointment</div></div>
  <div style="position:absolute;left:245px;top:226px;width:374px;text-align:center;font-family:Cinz;font-size:12px;letter-spacing:.4em;color:{NAVY};opacity:.7">BESPOKE TAILORING</div>
  <div style="position:absolute;left:837px;top:226px;width:374px;text-align:center;font-family:Cinz;font-size:12px;letter-spacing:.4em;color:{MAROON};opacity:.8">THE WEDDING FLOOR</div>
</div>
<div style="position:absolute;left:72px;bottom:66px;font-size:13px;color:rgba(244,241,234,.6)">Shop front at night: backlit champagne letters on a navy fascia, a round projecting seal, and window vinyls for each floor.</div>'''


# ---------------------------------------------------------------- instagram
def post(kind, s):
    if kind == 'quote':
        return f'<div class="navy" style="width:{s}px;height:{s}px;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:{s*.1}px;text-align:center"><div class="serif" style="font-size:{s*.12}px;line-height:1.05">One man.<br><em style="color:{CHAMP}">One look.</em></div><div style="margin-top:{s*.08}px">{L.inline(L.symbol, height=s*.12, c=CHAMP)}</div></div>'
    if kind == 'pattern':
        return f'<div style="width:{s}px;height:{s}px;background:{pattern_monogram(CHAMP, NAVY, s*.28)}"></div>'
    if kind == 'logo':
        return f'<div class="paper" style="width:{s}px;height:{s}px;display:flex;align-items:center;justify-content:center">{L.inline(L.stacked, height=s*.56, c1=NAVY, c2=GOLD)}</div>'
    if kind == 'wedding':
        return f'<div style="width:{s}px;height:{s}px;background:{pattern_arch(CHAMP, MAROON, s*.25)};display:flex;align-items:center;justify-content:center"><div class="maroon" style="padding:{s*.07}px {s*.06}px;text-align:center"><div class="caps" style="font-size:{s*.04}px;color:{CHAMP}">Wedding season</div><div class="serif" style="font-size:{s*.1}px;line-height:1;margin-top:{s*.03}px;color:{IVORY}">Now <em>booking</em></div></div></div>'
    if kind == 'fabric':
        return f'<div class="suiting" style="width:{s}px;height:{s}px;display:flex;align-items:end;padding:{s*.08}px"><div><div class="caps" style="font-size:{s*.04}px;color:{CHAMP}">Cloth of the week</div><div class="serif" style="font-size:{s*.09}px;color:{IVORY};line-height:1.05">Midnight<br>wool twill</div></div></div>'
    if kind == 'process':
        return f'<div class="sand" style="width:{s}px;height:{s}px;padding:{s*.09}px;display:flex;flex-direction:column;justify-content:space-between"><div class="num" style="font-size:{s*.14}px">02</div><div><div class="serif" style="font-size:{s*.11}px;line-height:1;color:{NAVY}">Measured,<br>not guessed.</div><div style="margin-top:{s*.05}px">{icon("measure", s*.14, NAVY)}</div></div></div>'
    if kind == 'emb':
        return f'<div class="suiting" style="width:{s}px;height:{s}px;display:flex;align-items:center;justify-content:center;position:relative"><div style="position:absolute;inset:0;background:radial-gradient(circle,rgba(255,255,255,.08),rgba(0,0,0,.4))"></div><div style="position:relative">{sym_svg(s*.5, "url(#satG)", filt="stitch")}</div></div>'
    if kind == 'jacket':
        return f'<div style="width:{s}px;height:{s}px;background:{CHAMP};display:flex;align-items:center;justify-content:center">{jacket_art(s*.75, NAVY, 1.8)}</div>'
    if kind == 'visit':
        return f'<div class="paper" style="width:{s}px;height:{s}px;padding:{s*.09}px;display:flex;flex-direction:column;justify-content:space-between;color:{NAVY}"><div>{icon("pin", s*.14, GOLD)}</div><div><div class="serif" style="font-size:{s*.1}px;line-height:1">Visit the<br><em style="color:{GOLD}">atelier</em></div><div class="caps" style="font-size:{s*.035}px;margin-top:{s*.05}px">Pothencode</div></div></div>'


def phone(w, inner):
    h = w * 2.05
    return f'<div class="phone" style="width:{w}px;height:{h}px"><div class="scr">{inner}</div></div>'


def instagram_scene():
    pw = 330
    sw = pw - 24
    t = (sw - 4) / 3
    grid = ''.join(f'<div style="width:{t}px;height:{t}px;overflow:hidden">{post(k, t)}</div>' for k in
                   ['quote', 'emb', 'wedding', 'fabric', 'logo', 'process', 'jacket', 'pattern', 'visit'])
    hl = ''.join(f'<div style="text-align:center"><div style="width:44px;height:44px;border-radius:50%;border:1.5px solid {LINE};display:flex;align-items:center;justify-content:center;background:{IVORY}">{icon(i, 20, NAVY)}</div><div style="font-size:8.5px;margin-top:4px">{n}</div></div>'
                 for i, n in [('jacket', 'Suits'), ('ring', 'Wedding'), ('fabric', 'Cloth'), ('measure', 'Fittings'), ('pin', 'Visit')])
    prof = f'''<div style="background:#fff;height:100%;font-size:10px;color:#111">
      <div style="height:38px;display:flex;align-items:end;justify-content:space-between;padding:0 18px 6px;font-weight:600;font-size:10px"><span>9:41</span><span>●●● ▮</span></div>
      <div style="padding:6px 14px;font-weight:700;font-size:13px">tezoro.atelier</div>
      <div style="display:flex;align-items:center;gap:18px;padding:6px 14px">
        <div style="width:70px;height:70px;border-radius:50%;background:{NAVY};display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 2px #fff,0 0 0 3.5px {CHAMP}"><svg viewBox="0 0 400 400" width="62" height="62">{L.seal(c=CHAMP)[0]}</svg></div>
        <div style="display:flex;gap:16px;text-align:center">{''.join(f'<div><b style="font-size:13px">{a}</b><br>{b}</div>' for a,b in [('48','posts'),('2,140','followers'),('12','following')])}</div></div>
      <div style="padding:2px 14px;line-height:1.45"><b>Tezoro Atelier</b><br><span style="color:#777">Clothing (brand)</span><br>Bespoke menswear &amp; wedding floor.<br>Made for you, only you. ✂︎<br>📍 Near Zudio, Pothencode<br><span style="color:#1d4f91">tezoro.in</span></div>
      <div style="display:flex;gap:6px;padding:8px 14px"><div style="flex:1;background:#EFEFEF;border-radius:6px;padding:6px;text-align:center;font-weight:600">Book a fitting</div><div style="flex:1;background:#EFEFEF;border-radius:6px;padding:6px;text-align:center;font-weight:600">WhatsApp</div></div>
      <div style="display:flex;gap:12px;padding:6px 14px 10px">{hl}</div>
      <div style="display:grid;grid-template-columns:repeat(3,{t}px);gap:2px;border-top:1px solid #eee;padding-top:2px">{grid}</div></div>'''
    story = f'''<div style="height:100%;background:{pattern_buttons(CHAMP, NAVY, 70)};position:relative;color:{IVORY}">
      <div style="position:absolute;left:10px;right:10px;top:12px;display:flex;gap:3px">{''.join('<div style="flex:1;height:2px;background:rgba(255,255,255,.%s)"></div>' % o for o in ('9','9','4','4'))}</div>
      <div style="position:absolute;left:14px;top:24px;display:flex;align-items:center;gap:8px;font-size:10px;font-weight:600"><div style="width:26px;height:26px;border-radius:50%;background:{NAVY};display:flex;align-items:center;justify-content:center;border:1px solid {CHAMP}">{L.inline(L.symbol, height=16, c=CHAMP)}</div>tezoro.atelier</div>
      <div style="position:absolute;left:24px;right:24px;top:130px;bottom:130px;background:{NAVY};border-radius:130px 130px 6px 6px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:30px;border:1px solid rgba(212,180,131,.4)">
        <div class="caps" style="font-size:9px;color:{CHAMP}">Behind the cut</div>
        <div class="serif" style="font-size:30px;line-height:1.05;margin:16px 0">Twelve<br>measurements.<br><em style="color:{CHAMP}">One man.</em></div>
        {icon('measure', 44, CHAMP)}</div>
      <div style="position:absolute;left:0;right:0;bottom:40px;display:flex;justify-content:center"><div class="caps" style="background:{IVORY};color:{NAVY};font-size:9px;padding:10px 18px;border-radius:30px">Book a fitting</div></div></div>'''
    return f'''<div class="pad" style="right:auto;width:400px">{text_block('Instagram', 'A feed with <em>a rhythm.</em>', 'Alternate navy, ivory and cloth textures so the grid reads as one wardrobe. Seal as the profile picture, outline icons for highlights, arch frames for stories.', 380)}</div>
  <div style="position:absolute;left:560px;top:96px">{phone(pw, prof)}</div>
  <div style="position:absolute;left:940px;top:150px">{phone(300, story)}</div>
  <div style="position:absolute;left:1290px;top:150px;display:flex;flex-direction:column;gap:18px">
    <div class="shadow">{post('quote', 240)}</div><div class="shadow">{post('wedding', 240)}</div></div>'''


# ---------------------------------------------------------------- website
def jacket_art(w, c, sw=2.0):
    return f'''<svg viewBox="0 0 300 410" width="{w}" height="{w*1.37}" fill="none" stroke="{c}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round" style="display:block">
  <path d="M125 30 L50 62 C42 140 40 260 44 380 L150 392 L256 380 C260 260 258 140 250 62 L175 30"/>
  <path d="M50 62 C30 100 22 250 20 360 L48 364 C52 260 58 160 62 120"/>
  <path d="M250 62 C270 100 278 250 280 360 L252 364 C248 260 242 160 238 120"/>
  <path d="M125 30 L110 72 L132 92 L116 104 L150 240"/><path d="M175 30 L190 72 L168 92 L184 104 L150 240"/>
  <path d="M125 30 L150 84 L175 30"/><path d="M146 86 L154 86 L157 200 L150 212 L143 200 Z"/>
  <path d="M150 240 L150 392"/><circle cx="150" cy="268" r="4"/><circle cx="150" cy="306" r="4"/>
  <path d="M70 286 H122"/><path d="M178 286 H230"/><path d="M186 152 H222"/><path d="M192 152 L198 140 L206 150 L212 138 L218 152"/>
  <path d="M38 330 L48 332 M262 332 L272 330" stroke-dasharray="3 3"/></svg>'''


def site_hero(w):
    h = w * .56
    nav = ''.join(f'<span>{n}</span>' for n in ['Bespoke', 'Wedding', 'Cloth', 'Process', 'Visit'])
    return f'''<div style="width:{w}px;height:{h}px;background:{IVORY};position:relative;overflow:hidden;font-size:{w*.011}px;color:{INK}">
   <div style="height:{h*.1}px;display:flex;align-items:center;justify-content:space-between;padding:0 {w*.04}px;border-bottom:1px solid {LINE}">
     {L.inline(L.horizontal, height=h*.055, c1=NAVY, c2=GOLD)}
     <div class="caps" style="display:flex;gap:{w*.03}px;font-size:{w*.0085}px;letter-spacing:.22em">{nav}</div>
     <span class="caps" style="background:{NAVY};color:{IVORY};padding:{w*.008}px {w*.016}px;font-size:{w*.008}px">Book a fitting</span></div>
   <div style="display:grid;grid-template-columns:1fr 1fr;height:{h*.9}px">
     <div style="padding:{w*.06}px {w*.04}px;display:flex;flex-direction:column;justify-content:center">
       <div class="eyebrow" style="font-size:{w*.0085}px">Bespoke tailoring · Pothencode</div>
       <div class="serif" style="font-size:{w*.055}px;line-height:.98;margin-top:{w*.012}px">Made for you.<br><em style="color:{GOLD}">Only you.</em></div>
       <p style="font-size:{w*.0115}px;line-height:1.6;color:{MUTED};margin-top:{w*.016}px;max-width:{w*.34}px">Suits, shirts and wedding wear cut to your measure from cloth you choose. No racks, no repeats.</p>
       <div style="display:flex;gap:{w*.01}px;margin-top:{w*.024}px"><span class="caps" style="background:{NAVY};color:{IVORY};padding:{w*.011}px {w*.02}px;font-size:{w*.008}px">Book a fitting</span><span class="caps" style="border:1px solid {NAVY};padding:{w*.011}px {w*.02}px;font-size:{w*.008}px">Explore the wedding floor</span></div>
       <div style="display:flex;gap:{w*.03}px;margin-top:{w*.04}px">{''.join(f'<div><div class="serif" style="font-size:{w*.022}px;color:{NAVY}">{a}</div><div style="font-size:{w*.008}px;color:{MUTED};letter-spacing:.1em;text-transform:uppercase">{b}</div></div>' for a,b in [('1 of 1','every garment'),('3','fittings'),('100%','made to measure')])}</div>
     </div>
     <div style="background:{pattern_pinstitch(CHAMP, NAVY, 22, .3)};position:relative;display:flex;align-items:center;justify-content:center">
       <div style="position:absolute;inset:{w*.03}px;border:1px solid rgba(212,180,131,.35);border-radius:{w*.2}px {w*.2}px 0 0"></div>
       {jacket_art(w*.22, CHAMP, 1.6)}
       <div style="position:absolute;right:{w*.03}px;bottom:{w*.03}px;width:{w*.08}px;height:{w*.08}px;border-radius:50%;background:{NAVY};display:flex;align-items:center;justify-content:center"><svg viewBox="0 0 400 400" width="{w*.07}" height="{w*.07}">{L.seal(c=CHAMP)[0]}</svg></div>
     </div></div></div>'''


def mobile_site(w):
    return f'''<div style="height:100%;background:{IVORY};font-size:9px">
     <div style="height:30px"></div>
     <div style="display:flex;justify-content:space-between;align-items:center;padding:8px 16px;border-bottom:1px solid {LINE}">{L.inline(L.horizontal, height=22, c1=NAVY, c2=GOLD)}<span style="font-size:16px;color:{NAVY}">☰</span></div>
     <div style="height:230px;background:{pattern_pinstitch(CHAMP, NAVY, 22, .3)};display:flex;align-items:center;justify-content:center">{jacket_art(120, CHAMP, 2)}</div>
     <div style="padding:20px 16px"><div class="eyebrow" style="font-size:8px">Bespoke tailoring</div>
       <div class="serif" style="font-size:34px;line-height:1;margin-top:8px">Made for you.<br><em style="color:{GOLD}">Only you.</em></div>
       <div class="caps" style="background:{NAVY};color:{IVORY};padding:12px;text-align:center;font-size:8px;margin-top:18px">Book a fitting</div>
       <div class="caps" style="border:1px solid {NAVY};padding:12px;text-align:center;font-size:8px;margin-top:8px">WhatsApp us</div></div></div>'''


def website_scene():
    lw = 900
    return f'''<div class="pad" style="right:auto;width:380px">{text_block('Website', 'A showroom <em>open 24/7.</em>', 'Ivory pages, navy calls to action and generous serif headlines. Booking a fitting is always one tap away, on every screen.', 360)}</div>
  <div style="position:absolute;left:500px;top:150px">
    <div style="background:#111;border-radius:18px 18px 0 0;padding:16px 16px 22px;box-shadow:0 40px 80px -30px rgba(0,0,0,.6)">{site_hero(lw)}</div>
    <div style="width:{lw+120}px;margin-left:-28px;height:22px;background:linear-gradient(#D8D8DA,#A9A9AD);border-radius:0 0 18px 18px"></div>
    <div style="width:{lw+120}px;margin-left:-28px;height:10px;background:radial-gradient(ellipse at top,rgba(0,0,0,.25),transparent 70%)"></div></div>
  <div style="position:absolute;left:1300px;top:260px">{phone(240, mobile_site(216))}</div>'''


# ---------------------------------------------------------------- client experience
def passport_scene():
    rows = [('Chest', '40'), ('Waist', '34'), ('Shoulder', '18'), ('Sleeve', '25'), ('Jacket length', '30'), ('Neck', '15.5')]
    book = f'''<div style="display:flex" class="shadow">
     <div style="width:300px;height:420px;background:{IVORY} url('{noise(.05)}');padding:30px;color:{NAVY};border-right:1px solid {LINE}">
       <div class="caps" style="font-size:9.5px;color:{GOLD}">Fitting record</div>
       <div class="serif" style="font-size:28px;margin-top:6px">Mr. Arun Nair</div>
       <div style="margin-top:18px;font-size:12px">{''.join(f'<div style="display:flex;justify-content:space-between;border-bottom:1px solid {LINE};padding:8px 0"><span>{a}</span><span class="serif it" style="font-size:17px">{b}″</span></div>' for a,b in rows)}</div>
       <div style="font-size:10px;color:{MUTED};margin-top:16px">Cutter: S. · Last fitting 27.10.2026</div></div>
     <div style="width:300px;height:420px;background:{IVORY} url('{noise(.05)}');padding:30px;color:{NAVY};display:flex;flex-direction:column;justify-content:space-between">
       <div><div class="caps" style="font-size:9.5px;color:{GOLD}">Your garments</div>
       {''.join(f'<div style="display:flex;gap:12px;align-items:center;margin-top:16px">{icon(i,26,NAVY)}<div><div class="serif" style="font-size:19px">{a}</div><div style="font-size:10px;color:{MUTED}">{b}</div></div></div>' for i,a,b in [('jacket','Two-piece suit','Navy wool twill · TZ-0147'),('shirt','Dress shirt × 2','White poplin · TZ-0148'),('sherwani','Wedding sherwani','Ivory raw silk · TZ-0152')])}</div>
       <div style="display:flex;justify-content:center">{L.inline(L.monogram, height=26, c=GOLD, eye=False)}</div></div></div>'''
    cover = f'''<div class="shadow" style="width:300px;height:420px;background:{NAVY} url('{noise(.14)}');display:flex;flex-direction:column;align-items:center;justify-content:center;border-left:8px solid #0E1830">
       <svg viewBox="-4 -4 108 108" width="110" height="110"><g fill="url(#foil)">{SYM()}</g></svg>
       <div class="caps" style="font-size:11px;color:{CHAMP};margin-top:30px">The Fitting Book</div>
       <div class="serif it" style="font-size:18px;color:{IVORY};opacity:.7;margin-top:8px">No. 0147</div></div>'''
    appt = f'''<div class="shadow" style="width:340px;height:200px;background:{IVORY};padding:26px 28px;color:{NAVY};position:relative">
       <div style="display:flex;justify-content:space-between"><div class="caps" style="font-size:9.5px;color:{GOLD}">Your next fitting</div>{L.inline(L.symbol, height=26, c=NAVY)}</div>
       <div class="serif" style="font-size:34px;margin-top:14px;line-height:1">Sat, 7 November</div>
       <div style="font-size:12px;margin-top:8px;color:{MUTED}">11:30 am · Second fitting · Two-piece suit</div>
       <div style="position:absolute;left:0;right:0;bottom:0;height:8px;background:repeating-linear-gradient(90deg,{NAVY} 0 1px,transparent 1px 8px),{SAND}"></div></div>'''
    thanks = f'''<div class="shadow" style="width:340px;height:200px;background:{SAND} url('{noise(.06)}');display:flex;flex-direction:column;align-items:center;justify-content:center;color:{NAVY}">
       {L.inline(L.signature, width=150, c=NAVY)}<div class="serif it" style="font-size:20px;margin-top:10px">Thank you for trusting us with your day.</div>
       <div style="margin-top:12px;width:60px;height:1px;background:{GOLD}"></div></div>'''
    return f'''<div class="pad" style="right:auto;width:400px">{text_block('Client experience', 'Remembered, <em>fitting by fitting.</em>', 'Every client receives a Fitting Book with his measurements and garments, appointment cards between fittings, and a handwritten thank-you with the finished piece.', 380, True)}</div>
  <div style="position:absolute;left:530px;top:130px;display:flex;gap:24px">{cover}{book}</div>
  <div style="position:absolute;left:530px;top:600px;display:flex;gap:30px">{appt}{thanks}</div>'''


# ---------------------------------------------------------------- wedding
def wedding_scene():
    box = f'''<svg viewBox="0 0 560 420" width="520" height="390" style="display:block;overflow:visible">
  <ellipse cx="290" cy="395" rx="260" ry="24" fill="rgba(0,0,0,.25)"/>
  <path d="M40 170 L300 260 L300 390 L40 300 Z" fill="#45121B"/>
  <path d="M300 260 L530 160 L530 290 L300 390 Z" fill="#350C14"/>
  <path d="M40 170 L270 70 L530 160 L300 260 Z" fill="#6A2030"/>
  <path d="M40 170 L300 260 L300 286 L40 196 Z" fill="#5A1A26"/><path d="M300 260 L530 160 L530 186 L300 286 Z" fill="#4A1420"/>
  <path d="M40 170 L270 70 L530 160 L300 260 Z" fill="none" stroke="{CHAMP}" stroke-width="2" opacity=".7"/>
  <path d="M70 168 L270 82 L500 160 L300 246 Z" fill="none" stroke="{CHAMP}" stroke-width="1" opacity=".5" stroke-dasharray="6 5"/>
  <g transform="translate(285 164) scale(1 .55)"><circle r="54" fill="url(#foil)"/><g transform="translate(-36 -36) scale(.72)" fill="rgba(90,30,30,.85)">{SYM(False)}</g></g></svg>'''
    invite = f'''<div class="shadow" style="width:330px;height:460px;background:{IVORY} url('{noise(.05)}');padding:16px;transform:rotate(3deg)">
     <div style="border:1px solid {GOLD};height:100%;border-radius:150px 150px 2px 2px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:30px;color:{MAROON}">
      {L.inline(L.symbol, height=56, c=MAROON)}
      <div class="caps" style="font-size:9.5px;color:{GOLD};margin-top:22px">The groom's consultation</div>
      <div class="serif" style="font-size:34px;line-height:1.05;margin-top:12px">A private hour on <em style="color:{GOLD}">the wedding floor</em></div>
      <div style="width:50px;height:1px;background:{GOLD};margin:18px 0"></div>
      <div style="font-size:11.5px;line-height:1.7;color:#7A4A50">Sherwani · Bandhgala · Three-piece<br>For the groom and his family<br>By appointment</div></div></div>'''
    return f'''<div class="pad" style="right:auto;width:420px">
    {text_block('Sub-brand', 'Tezoro <em>Wedding.</em>', 'Same symbol, same wordmark, a new sub-line. Maroon and gold appear only on wedding-floor material: sherwani boxes, garment bags, consultation cards and wedding-season posts.', 400, True)}
    <div style="margin-top:40px">{L.inline(L.horizontal, width=380, c1=IVORY, c2=CHAMP, subtext='WEDDING')}</div></div>
  <div style="position:absolute;left:600px;top:210px">{box}</div>
  <div style="position:absolute;left:1150px;top:170px">{invite}</div>'''
