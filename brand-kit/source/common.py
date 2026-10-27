"""Shared tokens, CSS, textures and small drawing helpers for the Tezoro
brand kit and company profile. Change the palette here and rebuild to
re-colour every page and mockup."""
import base64
import logos as L

NAVY = '#14213D'      # Midnight Navy  - primary
INK = '#0D1526'       # Deep Ink       - text, darkest surfaces
CHAMP = '#D4B483'     # Champagne      - accent on dark
GOLD = '#B8893E'      # Antique Gold   - accent on light
IVORY = '#F4F1EA'     # Soft Ivory     - paper
STONE = '#BFAE99'     # Taupe Stone    - neutral, tags, packaging
SAND = '#E4D9CA'      # Sandstone      - light neutral
MAROON = '#5A1A24'    # Wedding Maroon - Tezoro Wedding sub-brand
MUTED = '#6B6A73'
LINE = '#DCD3C4'

PALETTE = [
    ('Midnight Navy', NAVY, 'Primary', 'The colour of a perfect evening suit. Our main surface and logo colour.'),
    ('Champagne', CHAMP, 'Accent', 'Thread, foil and light on dark grounds. Never for long text on ivory.'),
    ('Soft Ivory', IVORY, 'Base', 'Paper, shirts and quiet space. The calm behind everything.'),
    ('Antique Gold', GOLD, 'Accent on light', 'Champagne\'s deeper twin, used for small type and rules on ivory.'),
    ('Deep Ink', INK, 'Text', 'Body copy and the darkest surfaces.'),
    ('Taupe Stone', STONE, 'Neutral', 'Tags, tissue and packaging board.'),
    ('Sandstone', SAND, 'Neutral', 'Soft backgrounds and dividers.'),
    ('Wedding Maroon', MAROON, 'Sub-brand', 'Reserved for the Tezoro Wedding floor.'),
]


def rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def cmyk(h):
    r, g, b = [v / 255 for v in rgb(h)]
    k = 1 - max(r, g, b)
    if k >= 1:
        return (0, 0, 0, 100)
    c, m, y = [(1 - v - k) / (1 - k) for v in (r, g, b)]
    return tuple(round(v * 100) for v in (c, m, y, k))


def lum(h):
    def ch(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = [ch(v) for v in rgb(h)]
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True)
    return (la + 0.05) / (lb + 0.05)


def data_svg(svg):
    return 'data:image/svg+xml;base64,' + base64.b64encode(svg.encode()).decode()


# ---------- textures (data-URI SVGs used as CSS backgrounds) ----------
def noise(alpha=0.10, freq=0.9, size=240, seed=3):
    return data_svg(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}">'
        f'<filter id="n"><feTurbulence type="fractalNoise" baseFrequency="{freq}" numOctaves="2" seed="{seed}" stitchTiles="stitch"/>'
        f'<feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 {alpha} 0"/></filter>'
        f'<rect width="100%" height="100%" filter="url(#n)"/></svg>')


def twill(c1='rgba(255,255,255,.035)', c2='rgba(0,0,0,.10)', step=5):
    """Diagonal twill weave for suiting."""
    return (f'repeating-linear-gradient(45deg,{c1} 0 1px,transparent 1px {step}px),'
            f'repeating-linear-gradient(-45deg,{c2} 0 1px,transparent 1px {step * 1.6}px)')


def herringbone(fg='rgba(255,255,255,.05)', size=18):
    s = size
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s*2}">'
           f'<g stroke="{fg}" stroke-width="1.2">'
           + ''.join(f'<line x1="0" y1="{i}" x2="{s/2}" y2="{i+s/2}"/><line x1="{s/2}" y1="{i+s/2}" x2="{s}" y2="{i}"/>'
                     for i in range(-s, s * 2 + s, 4)) +
           '</g></svg>')
    return f"url('{data_svg(svg)}')"


def weave(fg='rgba(255,255,255,.06)', bg='rgba(0,0,0,.10)'):
    """Fine jacquard weave for woven labels."""
    return (f'repeating-linear-gradient(0deg,{fg} 0 1px,transparent 1px 3px),'
            f'repeating-linear-gradient(90deg,{bg} 0 1px,transparent 1px 2px)')


# ---------- brand patterns ----------
def pattern_monogram(fg=CHAMP, bg=NAVY, cell=64, op=1.0):
    m = L.monogram_body(eye=False)
    c = cell
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{c*2}" height="{c*2}">'
           f'<rect width="100%" height="100%" fill="{bg}"/>'
           f'<g fill="{fg}" opacity="{op}">'
           f'<g transform="translate({c*.32} {c*.32}) scale({c*.36/100})">{m}</g>'
           f'<g transform="translate({c*1.32} {c*1.32}) scale({c*.36/100})">{m}</g></g>'
           f'<g fill="{fg}" opacity="{op*.55}"><circle cx="{c*1.5}" cy="{c*.5}" r="{c*.025}"/><circle cx="{c*.5}" cy="{c*1.5}" r="{c*.025}"/></g>'
           '</svg>')
    return f"url('{data_svg(svg)}')"


def pattern_pinstitch(fg=CHAMP, bg=NAVY, gap=26, op=.55):
    """Chalk-stripe made of running stitches: a nod to tailor's tacking."""
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{gap}" height="24">'
           f'<rect width="100%" height="100%" fill="{bg}"/>'
           f'<rect x="{gap/2-0.9}" y="2" width="1.8" height="12" rx=".9" fill="{fg}" opacity="{op}"/></svg>')
    return f"url('{data_svg(svg)}')"


def pattern_buttons(fg=CHAMP, bg=NAVY, cell=90):
    c = cell
    btn = (f'<circle cx="0" cy="0" r="{c*.16}" fill="none" stroke="{fg}" stroke-width="{c*.022}"/>'
           + ''.join(f'<circle cx="{dx}" cy="{dy}" r="{c*.022}" fill="{fg}"/>'
                     for dx, dy in [(-c*.05, -c*.05), (c*.05, -c*.05), (-c*.05, c*.05), (c*.05, c*.05)]))
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{c}" height="{c}">'
           f'<rect width="100%" height="100%" fill="{bg}"/>'
           f'<g opacity=".6"><g transform="translate({c*.25} {c*.25})">{btn}</g>'
           f'<g transform="translate({c*.75} {c*.75})">{btn}</g></g>'
           f'<path d="M{c*.25} {c*.75} h{c*.0} M{c*.6} {c*.25} h{c*.3}" stroke="{fg}" stroke-width="{c*.012}" stroke-dasharray="{c*.04} {c*.03}" opacity=".45"/>'
           '</svg>')
    return f"url('{data_svg(svg)}')"


def pattern_arch(fg=CHAMP, bg=MAROON, cell=70):
    c = cell
    arch = (f'<path d="M{c*.3} {c*.9} V{c*.5} C{c*.3} {c*.32} {c*.5} {c*.3} {c*.5} {c*.1} '
            f'C{c*.5} {c*.3} {c*.7} {c*.32} {c*.7} {c*.5} V{c*.9}" fill="none" stroke="{fg}" stroke-width="{c*.03}"/>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{c}" height="{c}">'
           f'<rect width="100%" height="100%" fill="{bg}"/><g opacity=".55">{arch}</g></svg>')
    return f"url('{data_svg(svg)}')"


# ---------- line icons (24 grid, stroke) ----------
ICONS = {
    'shirt': 'M8 3 L4 5 L2 10 L5 11 L6 9 V21 H18 V9 L19 11 L22 10 L20 5 L16 3 L12 7 Z M12 7 V21 M8 3 L12 7 L16 3',
    'jacket': 'M8 2 L3 5 V21 H11 L12 12 L13 21 H21 V5 L16 2 L12 8 Z M8 2 L10 9 L12 8 M16 2 L14 9 L12 8 M15 15 h3',
    'sherwani': 'M9 2 H15 L14 4 L19 6 V22 H5 V6 L10 4 Z M12 4 V22 M10.5 8 h0 M12 8 h0 M12 11 h0 M12 14 h0 M12 17 h0',
    'trousers': 'M6 2 H18 L19 22 H14 L12 9 L10 22 H5 Z M6 5 H18',
    'measure': 'M3 8 H21 V16 H3 Z M6 8 V11 M9 8 V12 M12 8 V11 M15 8 V12 M18 8 V11',
    'needle': 'M19 3 L5 17 L3 21 L7 19 L21 5 Z M17 5 L19 7 M3 21 C8 21 6 14 12 14',
    'fabric': 'M4 6 C8 4 10 8 14 6 C17 4.5 19 5 20 6 V18 C19 17 17 16.5 14 18 C10 20 8 16 4 18 Z M4 10 C8 8 10 12 14 10 C17 8.5 19 9 20 10',
    'calendar': 'M4 5 H20 V21 H4 Z M4 9 H20 M8 3 V7 M16 3 V7 M8 13 h2 M12 13 h2 M8 17 h2',
    'ring': 'M12 9 a6 6 0 1 0 0.01 0 Z M9 4 L12 7 L15 4 L13 2 H11 Z',
    'scissors': 'M6 6 a3 3 0 1 0 0.01 0 M6 18 a3 3 0 1 0 0.01 0 M8.5 7.5 L20 18 M8.5 16.5 L20 6',
    'chat': 'M4 5 H20 V16 H10 L5 20 V16 H4 Z',
    'pin': 'M12 22 C12 22 5 14.5 5 9.5 a7 7 0 0 1 14 0 C19 14.5 12 22 12 22 Z M12 7 a2.5 2.5 0 1 0 0.01 0',
    'clock': 'M12 3 a9 9 0 1 0 0.01 0 M12 7 V12 L15 14',
    'gift': 'M3 9 H21 V13 H3 Z M5 13 V21 H19 V13 M12 9 V21 M12 9 C9 9 7 4 9.5 4 C11 4 12 9 12 9 C12 9 13 4 14.5 4 C17 4 15 9 12 9',
}


def icon(name, size=28, color=NAVY, sw=1.4):
    return (f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" stroke="{color}" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" style="display:block">'
            f'<path d="{ICONS[name]}"/></svg>')


def font_faces(prefix='fonts/'):
    return f"""
@font-face{{font-family:Corm;src:url({prefix}Cormorant.ttf);font-weight:300 700}}
@font-face{{font-family:Corm;src:url({prefix}Cormorant-Italic.ttf);font-weight:300 700;font-style:italic}}
@font-face{{font-family:Cinz;src:url({prefix}Cinzel.ttf);font-weight:400 900}}
"""


BASE_CSS = font_faces() + f"""
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{background:#888}}
body{{font-family:Inter,Arial,sans-serif;color:{INK};-webkit-font-smoothing:antialiased}}
.serif{{font-family:Corm,serif}}
.caps{{font-family:Cinz,serif;letter-spacing:.28em;text-transform:uppercase}}
em,.it{{font-family:Corm,serif;font-style:italic}}
.paper{{background:{IVORY} url("{noise(.05)}")}}
.navy{{background:{NAVY} url("{noise(.12)}");color:{IVORY}}}
.ink{{background:{INK} url("{noise(.12)}");color:{IVORY}}}
.maroon{{background:{MAROON} url("{noise(.12)}");color:{IVORY}}}
.sand{{background:{SAND} url("{noise(.06)}")}}
.flex{{display:flex}}.col{{flex-direction:column}}.center{{align-items:center;justify-content:center}}
"""
