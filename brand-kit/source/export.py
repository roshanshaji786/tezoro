"""Writes the logo file pack: outlined SVGs in every approved colourway,
plus a manifest that png.js turns into transparent PNGs."""
import json
import os
import logos as L
from common import NAVY, CHAMP, GOLD, IVORY, INK, MAROON, PALETTE, rgb, cmyk

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logo-files')

# colourway name -> (main colour, accent colour)
WAYS = {
    'full-colour': (NAVY, GOLD),
    'reversed': (IVORY, CHAMP),
    'navy': (NAVY, NAVY),
    'champagne': (CHAMP, CHAMP),
    'ivory': (IVORY, IVORY),
    'black': ('#000000', '#000000'),
    'white': ('#FFFFFF', '#FFFFFF'),
}

FORMS = {
    'horizontal': lambda a, b: L.horizontal(c1=a, c2=b),
    'stacked': lambda a, b: L.stacked(c1=a, c2=b),
    'wordmark': lambda a, b: L.wordmark(c1=a, c2=b),
    'wordmark-no-subline': lambda a, b: L.wordmark(sub=False, c1=a),
    'symbol': lambda a, b: L.symbol(c=a),
    'symbol-small-cut': lambda a, b: L.symbol(c=a, eye=False),
    'monogram': lambda a, b: L.monogram(c=a),
    'monogram-small-cut': lambda a, b: L.monogram(c=a, eye=False),
    'seal': lambda a, b: L.seal(c=a),
    'signature': lambda a, b: L.signature(c=a),
    'wedding-horizontal': lambda a, b: L.horizontal(c1=a, c2=b, subtext='WEDDING'),
    'wedding-stacked': lambda a, b: L.stacked(c1=a, c2=b, subtext='WEDDING'),
}


def write(path, body, w, h, pad):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-pad:.2f} {-pad:.2f} {w + 2*pad:.2f} {h + 2*pad:.2f}" '
           f'width="{w + 2*pad:.0f}" height="{h + 2*pad:.0f}">{body}</svg>')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w').write(svg)
    return (w + 2 * pad) / (h + 2 * pad)


manifest = []
for form, fn in FORMS.items():
    ways = dict(WAYS)
    if form.startswith('wedding'):
        ways['wedding-maroon'] = (MAROON, GOLD)
    for way, (a, b) in ways.items():
        body, w, h = fn(a, b)
        pad = 0.06 * max(w, h)
        rel = f'svg/{form}/tezoro-{form}-{way}.svg'
        ratio = write(os.path.join(OUT, rel), body, w, h, pad)
        manifest.append({'svg': rel, 'png': rel.replace('svg/', 'png/').replace('.svg', '.png'), 'ratio': ratio,
                         'dark': way in ('reversed', 'champagne', 'ivory', 'white')})

# favicon / app icon: symbol on navy, square
body, w, h = L.symbol(c=CHAMP, eye=False)
fav = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-18 -18 136 136" width="512" height="512">'
       f'<rect x="-18" y="-18" width="136" height="136" fill="{NAVY}"/>{body}</svg>')
os.makedirs(os.path.join(OUT, 'svg', 'app-icon'), exist_ok=True)
open(os.path.join(OUT, 'svg', 'app-icon', 'tezoro-app-icon.svg'), 'w').write(fav)
manifest.append({'svg': 'svg/app-icon/tezoro-app-icon.svg', 'png': 'png/app-icon/tezoro-app-icon.png', 'ratio': 1, 'dark': False})
# profile picture: seal on navy circle
body, w, h = L.seal(c=CHAMP, bg=NAVY)
open(os.path.join(OUT, 'svg', 'app-icon', 'tezoro-profile-picture.svg'), 'w').write(
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="1080" height="1080">{body}</svg>')
manifest.append({'svg': 'svg/app-icon/tezoro-profile-picture.svg', 'png': 'png/app-icon/tezoro-profile-picture.png', 'ratio': 1, 'dark': False})

json.dump(manifest, open(os.path.join(OUT, 'manifest.json'), 'w'), indent=1)

# colour tokens for designers and the website
pal = [{'name': n, 'hex': h, 'rgb': rgb(h), 'cmyk_approx': cmyk(h), 'role': r} for n, h, r, _ in PALETTE]
json.dump({'palette': pal, 'fonts': {'display': 'Cormorant Garamond', 'labels': 'Cinzel', 'body': 'Inter'}},
          open(os.path.join(OUT, 'tezoro-colours.json'), 'w'), indent=1)
css = ':root{\n' + ''.join(f'  --tz-{n.lower().replace(" ", "-")}: {h};\n' for n, h, _, _ in PALETTE) + '}\n'
open(os.path.join(OUT, 'tezoro-colours.css'), 'w').write(css)
print(len(manifest), 'files')
