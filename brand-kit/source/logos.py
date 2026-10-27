"""Tezoro logo geometry. Every mark is built from solid shapes and outlined
type (no live fonts), so the SVG files work in any app, cutter or
embroidery-digitising software."""
import os
from functools import lru_cache
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, 'fonts')


@lru_cache(None)
def _font(name, wght):
    f = TTFont(os.path.join(FONT_DIR, name + '.ttf'))
    return instancer.instantiateVariableFont(f, {'wght': wght})


def text_path(text, name='Cormorant', wght=500, size=100, tracking=0.0):
    """Outline `text` into one SVG path. tracking is in em. Returns
    (d, width, cap_height) with the baseline at y=0."""
    f = _font(name, wght)
    gs, cmap, hmtx = f.getGlyphSet(), f.getBestCmap(), f['hmtx']
    upm = f['head'].unitsPerEm
    s = size / upm
    pen = SVGPathPen(gs)
    x = 0.0
    for i, ch in enumerate(text):
        g = cmap[ord(ch)]
        if ch != ' ':
            gs[g].draw(TransformPen(pen, (s, 0, 0, -s, x, 0)))
        x += hmtx[g][0] * s
        if i < len(text) - 1:
            x += tracking * size
    bp = BoundsPen(gs)
    gs[cmap[ord('H')]].draw(bp)
    cap = bp.bounds[3] * s
    return pen.getCommands(), x, cap


# ---------- the symbol: needle button ----------
# A tailor's button ring with a needle that forms the T. The needle has an
# eye (cut-out) at large sizes; the "small" cut drops the eye and thickens
# the ring so it survives a 10 mm woven label or a 6 mm embroidery.
def symbol_body(eye=True, ring=5.2):
    stem = 'M45.2 37 H54.8 L53.3 71 L50 83.5 L46.7 71 Z'
    eye_d = ' M48.7 42.5 a1.3 1.3 0 0 1 2.6 0 V54 a1.3 1.3 0 0 1 -2.6 0 Z' if eye else ''
    r_out, r_in = 44, 44 - ring
    ring_d = (f'M50 {50-r_out} a{r_out} {r_out} 0 1 1 0 {2*r_out} a{r_out} {r_out} 0 1 1 0 {-2*r_out} Z '
              f'M50 {50-r_in} a{r_in} {r_in} 0 1 0 0 {2*r_in} a{r_in} {r_in} 0 1 0 0 {-2*r_in} Z')
    bar = 'M27 28.5 H73 V37 H27 Z'
    return (f'<path fill-rule="evenodd" d="{ring_d}"/>'
            f'<path d="{bar}"/>'
            f'<path fill-rule="evenodd" d="{stem}{eye_d}"/>')


def monogram_body(eye=True):
    """Needle T alone, for buttons, cufflinks, cuffs and favicons."""
    bar = 'M18 14 H82 V27 H18 Z'
    stem = 'M43 27 H57 L54.8 76 L50 94 L45.2 76 Z'
    eye_d = ' M48.1 35 a1.9 1.9 0 0 1 3.8 0 V52 a1.9 1.9 0 0 1 -3.8 0 Z' if eye else ''
    return f'<path d="{bar}"/><path fill-rule="evenodd" d="{stem}{eye_d}"/>'


def svg(body, w, h, fill='#14213D', bg=None, vb=None, extra=''):
    vb = vb or f'0 0 {w:.2f} {h:.2f}'
    bgr = f'<rect width="100%" height="100%" fill="{bg}"/>' if bg else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" '
            f'width="{w:.2f}" height="{h:.2f}" {extra}>{bgr}<g fill="{fill}">{body}</g></svg>')


def _word(size=100, wght=500):
    return text_path('TEZORO', 'Cormorant', wght, size, tracking=0.30)


def _sub(text='ATELIER', size=30, wght=500, tracking=0.62):
    return text_path(text, 'Cinzel', wght, size, tracking)


# ---------- lockups (return (body, w, h)) with two colours ----------
def wordmark(sub=True, c1='#14213D', c2=None, subtext='ATELIER'):
    c2 = c2 or c1
    d, w, cap = _word()
    out = f'<path fill="{c1}" transform="translate(0 {cap:.2f})" d="{d}"/>'
    h = cap
    if sub:
        sd, sw, scap = _sub(subtext, size=26)
        y = cap + 34 + scap
        out += f'<path fill="{c2}" transform="translate({(w - sw) / 2:.2f} {y:.2f})" d="{sd}"/>'
        h = y
    return out, w, h


def horizontal(c1='#14213D', c2='#B8893E', sub=True, subtext='ATELIER'):
    wb, ww, wh = wordmark(sub, c1, c2, subtext)
    sym = 168
    gap, rule = 54, 3
    sx = 0
    rx = sym + gap
    tx = rx + rule + gap
    H = max(sym, wh)
    body = (f'<g fill="{c1}" transform="translate(0 {(H - sym) / 2:.2f}) scale({sym / 100})">{symbol_body()}</g>'
            f'<rect fill="{c2}" x="{rx}" y="{(H - sym * .8) / 2:.2f}" width="{rule}" height="{sym * .8:.2f}"/>'
            f'<g transform="translate({tx} {(H - wh) / 2:.2f})">{wb}</g>')
    return body, tx + ww, H


def stacked(c1='#14213D', c2='#B8893E', sub=True, subtext='ATELIER'):
    wb, ww, wh = wordmark(sub, c1, c2, subtext)
    sym = 200
    gap = 56
    W = max(ww, sym)
    body = (f'<g fill="{c1}" transform="translate({(W - sym) / 2:.2f} 0) scale({sym / 100})">{symbol_body()}</g>'
            f'<g transform="translate({(W - ww) / 2:.2f} {sym + gap})">{wb}</g>')
    return body, W, sym + gap + wh


def symbol(c='#14213D', eye=True):
    return f'<g fill="{c}">{symbol_body(eye)}</g>', 100, 100


def monogram(c='#14213D', eye=True):
    return f'<g fill="{c}">{monogram_body(eye)}</g>', 100, 100


def seal(c='#14213D', bg='none'):
    """Round badge for woven patches, stickers and wax/emboss."""
    R = 200
    body = f'<circle cx="{R}" cy="{R}" r="{R}" fill="{bg}"/>' if bg != 'none' else ''
    body += (f'<path fill="{c}" fill-rule="evenodd" d="M{R} 0 a{R} {R} 0 1 1 0 {2*R} a{R} {R} 0 1 1 0 {-2*R} Z '
             f'M{R} 10 a{R-10} {R-10} 0 1 0 0 {2*R-20} a{R-10} {R-10} 0 1 0 0 {-2*R+20} Z"/>')
    # circular text: place each outlined glyph along the circle
    import math
    f = _font('Cinzel', 600)
    gs, cmap, hmtx = f.getGlyphSet(), f.getBestCmap(), f['hmtx']
    size = 40
    s = size / 1000

    band = R - 56          # radius of the text band centre
    cap = size * 0.70

    def ring_text(txt, centre_deg, top=True):
        widths = [hmtx[cmap[ord(ch)]][0] * s for ch in txt]
        track = 0.32 * size
        rad = band - cap / 2 if top else band + cap / 2
        total = sum(widths) + track * (len(txt) - 1)
        span = total / rad
        a = math.radians(centre_deg) + (-span / 2 if top else span / 2)
        out = ''
        for ch, w in zip(txt, widths):
            half = (w / 2) / rad
            mid = a + (half if top else -half)
            if ch != ' ':
                pen = SVGPathPen(gs)
                gs[cmap[ord(ch)]].draw(TransformPen(pen, (s, 0, 0, -s, -w / 2, 0)))
                x = R + rad * math.sin(mid)
                y = R - rad * math.cos(mid)
                rot = math.degrees(mid) + (0 if top else 180)
                out += (f'<path fill="{c}" transform="translate({x:.2f} {y:.2f}) rotate({rot:.2f})" '
                        f'd="{pen.getCommands()}"/>')
            step = (w + track) / rad
            a += step if top else -step
        return out
    body += ring_text('TEZORO', 0, True)
    body += ring_text('ATELIER', 180, False)
    for deg in (90, 270):
        x = R + band * math.sin(math.radians(deg)); y = R - band * math.cos(math.radians(deg))
        body += f'<circle fill="{c}" cx="{x:.2f}" cy="{y:.2f}" r="5"/>'
    sym = 178
    body += f'<g fill="{c}" transform="translate({R - sym / 2} {R - sym / 2}) scale({sym / 100})">{symbol_body()}</g>'
    return body, 2 * R, 2 * R


def signature(c='#14213D'):
    d, w, cap = text_path('Tezoro', 'Cormorant-Italic', 500, 100, tracking=0.01)
    return f'<path fill="{c}" transform="translate(0 {cap:.2f})" d="{d}"/>', w, cap + 22


def inline(fn, *a, height=None, width=None, pad=0, **k):
    """Inline SVG markup for use inside HTML pages."""
    body, w, h = fn(*a, **k)
    if height:
        width = w * height / h
    elif width:
        height = h * width / w
    else:
        width, height = w, h
    p = pad
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-p} {-p} {w + 2*p:.2f} {h + 2*p:.2f}" '
            f'width="{width:.2f}" height="{height:.2f}" style="display:block;overflow:visible">{body}</svg>')
