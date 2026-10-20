"""SVG 3D-style illustration helpers for the Tezoro brochure."""

DEFS = """
<svg width="0" height="0" style="position:absolute" aria-hidden="true">
<defs>
  <linearGradient id="gGold" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#F6E3B4"/><stop offset=".42" stop-color="#D4A653"/><stop offset="1" stop-color="#7E561C"/>
  </linearGradient>
  <linearGradient id="gGoldV" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#F6E3B4"/><stop offset=".5" stop-color="#C9973F"/><stop offset="1" stop-color="#7E561C"/>
  </linearGradient>
  <linearGradient id="gGoldH" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#8A6224"/><stop offset=".35" stop-color="#E9C77E"/><stop offset=".6" stop-color="#C9973F"/><stop offset="1" stop-color="#7E561C"/>
  </linearGradient>
  <radialGradient id="sGold" cx=".34" cy=".3" r=".78">
    <stop offset="0" stop-color="#FFF6DA"/><stop offset=".22" stop-color="#EDC97F"/><stop offset=".6" stop-color="#B78637"/><stop offset="1" stop-color="#4A300C"/>
  </radialGradient>
  <radialGradient id="sViolet" cx=".34" cy=".3" r=".78">
    <stop offset="0" stop-color="#F1EAFF"/><stop offset=".25" stop-color="#A881FF"/><stop offset=".65" stop-color="#6D3BE8"/><stop offset="1" stop-color="#1E0B52"/>
  </radialGradient>
  <radialGradient id="sIvory" cx=".34" cy=".3" r=".78">
    <stop offset="0" stop-color="#FFFFFF"/><stop offset=".35" stop-color="#F3EADB"/><stop offset=".75" stop-color="#C9BBA2"/><stop offset="1" stop-color="#6E624F"/>
  </radialGradient>
  <radialGradient id="sInk" cx=".34" cy=".3" r=".78">
    <stop offset="0" stop-color="#6A6258"/><stop offset=".35" stop-color="#2E2A25"/><stop offset="1" stop-color="#050505"/>
  </radialGradient>
  <radialGradient id="shadowDark" cx=".5" cy=".5" r=".5">
    <stop offset="0" stop-color="#000" stop-opacity=".7"/><stop offset="1" stop-color="#000" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="shadowLight" cx=".5" cy=".5" r=".5">
    <stop offset="0" stop-color="#3B2A10" stop-opacity=".32"/><stop offset="1" stop-color="#3B2A10" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="gTag" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#FFFDF8"/><stop offset=".6" stop-color="#F1E7D6"/><stop offset="1" stop-color="#D8C9AE"/>
  </linearGradient>
  <linearGradient id="gPhone" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#4A443B"/><stop offset=".25" stop-color="#1D1B18"/><stop offset=".8" stop-color="#0E0D0B"/><stop offset="1" stop-color="#3B362F"/>
  </linearGradient>
  <linearGradient id="gMetal" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#5A544A"/><stop offset=".35" stop-color="#2B2823"/><stop offset="1" stop-color="#0E0D0B"/>
  </linearGradient>
  <linearGradient id="gHero" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#2A2620"/><stop offset="1" stop-color="#121110"/>
  </linearGradient>
  <linearGradient id="gGlass" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#FFFFFF" stop-opacity=".22"/><stop offset="1" stop-color="#FFFFFF" stop-opacity=".03"/>
  </linearGradient>
  <filter id="drop" x="-30%" y="-30%" width="160%" height="170%">
    <feDropShadow dx="0" dy="9" stdDeviation="9" flood-color="#000" flood-opacity=".45"/>
  </filter>
  <filter id="dropSoft" x="-30%" y="-30%" width="160%" height="170%">
    <feDropShadow dx="0" dy="8" stdDeviation="10" flood-color="#3B2A10" flood-opacity=".22"/>
  </filter>
  <filter id="blur6"><feGaussianBlur stdDeviation="6"/></filter>
  <pattern id="lattice" width="22" height="22" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
    <rect x="0" y="0" width="22" height="22" fill="none" stroke="#B8893E" stroke-width=".6"/>
    <circle cx="11" cy="11" r="1.1" fill="#B8893E"/>
  </pattern>
</defs>
</svg>
"""


def sphere(cx, cy, r, grad="sGold", shadow=True, dark=True, sh_dy=None):
    out = ""
    if shadow:
        dy = sh_dy if sh_dy is not None else r * 1.6
        sid = "shadowDark" if dark else "shadowLight"
        out += f'<ellipse cx="{cx}" cy="{cy+dy}" rx="{r*1.05}" ry="{r*0.22}" fill="url(#{sid})"/>'
    out += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#{grad})"/>'
    out += f'<ellipse cx="{cx-r*0.32}" cy="{cy-r*0.4}" rx="{r*0.26}" ry="{r*0.15}" fill="#fff" opacity=".55" transform="rotate(-30 {cx-r*0.32} {cy-r*0.4})"/>'
    return out


def ring(cx, cy, rx, ry, rot=-18, w=9):
    return (f'<g transform="rotate({rot} {cx} {cy})">'
            f'<ellipse cx="{cx}" cy="{cy+2}" rx="{rx}" ry="{ry}" fill="none" stroke="#5E3E13" stroke-width="{w}"/>'
            f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="url(#gGoldH)" stroke-width="{w}"/>'
            f'<ellipse cx="{cx}" cy="{cy-w*0.25}" rx="{rx}" ry="{ry}" fill="none" stroke="#FFF3D0" stroke-opacity=".55" stroke-width="{w*0.18}"/>'
            f'</g>')


def bag(uid, front=("#3D372F", "#1A1815"), side=("#0F0E0C", "#1C1A17"), inside="#070706",
        accent="#C9973F", text="#DDB874", sub="#C9973F", tag=True, dark_bg=True, handle="url(#gGoldV)"):
    """3D shopping bag in a 400x470 box."""
    sh = "shadowDark" if dark_bg else "shadowLight"
    s = f'''
<defs>
  <linearGradient id="bf{uid}" x1="0" y1="0" x2="1" y2="0.25"><stop offset="0" stop-color="{front[0]}"/><stop offset="1" stop-color="{front[1]}"/></linearGradient>
  <linearGradient id="bs{uid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{side[0]}"/><stop offset="1" stop-color="{side[1]}"/></linearGradient>
</defs>
<ellipse cx="225" cy="436" rx="175" ry="20" fill="url(#{sh})"/>
<path d="M190 124 C190 36, 300 36, 300 124" fill="none" stroke="{accent}" stroke-opacity=".55" stroke-width="7" stroke-linecap="round"/>
<polygon points="90,150 290,150 350,122 150,122" fill="{inside}"/>
<polygon points="290,150 350,122 350,394 290,424" fill="{side[0]}"/><polygon points="290,150 350,122 350,394 290,424" fill="url(#bs{uid})"/>
<line x1="290" y1="150" x2="290" y2="424" stroke="#000" stroke-opacity=".35"/>
<rect x="90" y="150" width="200" height="274" fill="{front[1]}"/><rect x="90" y="150" width="200" height="274" fill="url(#bf{uid})"/>
<polygon points="90,150 165,150 90,290" fill="#fff" opacity=".05"/>
<line x1="90" y1="150" x2="90" y2="424" stroke="#fff" stroke-opacity=".16"/>
<line x1="90" y1="168" x2="290" y2="168" stroke="{accent}" stroke-opacity=".75" stroke-width="1.2"/>
<line x1="290" y1="168" x2="350" y2="140" stroke="{accent}" stroke-opacity=".45" stroke-width="1.2"/>
<path d="M135 152 C135 46, 245 46, 245 152" fill="none" stroke="{handle}" stroke-width="8" stroke-linecap="round"/>
<circle cx="135" cy="162" r="5" fill="{accent}"/><circle cx="245" cy="162" r="5" fill="{accent}"/>
<text x="190" y="300" text-anchor="middle" font-family="Cinzel" font-size="33" letter-spacing="4" fill="{text}">TEZORO</text>
<line x1="158" y1="316" x2="222" y2="316" stroke="{sub}" stroke-width="1"/>
<rect x="186.5" y="312.5" width="7" height="7" fill="{sub}" transform="rotate(45 190 316)"/>
<text x="191" y="338" text-anchor="middle" font-family="Cinzel" font-size="10" letter-spacing="6" fill="{sub}">ATELIER</text>
'''
    if tag:
        s += '''
<path d="M245 160 C268 175, 290 200, 318 236" fill="none" stroke="#D9B877" stroke-width="1.6"/>
<g transform="translate(296 230) rotate(16)" filter="url(#drop)">
  <polygon points="0,16 16,0 48,0 64,16 64,108 0,108" fill="url(#gTag)"/>
  <circle cx="32" cy="17" r="4.5" fill="#2B2620"/>
  <line x1="10" y1="36" x2="54" y2="36" stroke="#C9973F" stroke-width=".8"/>
  <text x="32" y="70" text-anchor="middle" font-family="Cormorant" font-weight="600" font-size="26" fill="#A8772E">1/1</text>
  <text x="32" y="90" text-anchor="middle" font-family="Cinzel" font-size="6.6" letter-spacing="2" fill="#6B6358">UNIQUE</text>
</g>'''
    return s


def iso_block(cx, y, a, t, top, left, right, label=None, label_fill="#C9973F", label_size=22):
    p_top = f"{cx},{y} {cx+a},{y+a/2} {cx},{y+a} {cx-a},{y+a/2}"
    p_left = f"{cx-a},{y+a/2} {cx},{y+a} {cx},{y+a+t} {cx-a},{y+a/2+t}"
    p_right = f"{cx},{y+a} {cx+a},{y+a/2} {cx+a},{y+a/2+t} {cx},{y+a+t}"
    s = (f'<polygon points="{p_left}" fill="{left}"/>'
         f'<polygon points="{p_right}" fill="{right}"/>'
         f'<polygon points="{p_top}" fill="{top}"/>'
         f'<polyline points="{cx-a},{y+a/2} {cx},{y+a} {cx+a},{y+a/2}" fill="none" stroke="#fff" stroke-opacity=".18"/>')
    if label is not None:
        ty = y + a / 2
        s += (f'<g transform="translate({cx} {ty}) scale(1 .58)"><text x="0" y="{label_size*0.36}" text-anchor="middle" '
              f'font-family="Cormorant" font-weight="600" font-size="{label_size}" fill="{label_fill}">{label}</text></g>')
    return s


def medallion():
    s = '<svg viewBox="0 0 300 310" xmlns="http://www.w3.org/2000/svg">'
    s += '<ellipse cx="150" cy="292" rx="110" ry="12" fill="url(#shadowLight)"/>'
    s += '<defs><linearGradient id="coinFace" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F8E6B8"/><stop offset=".45" stop-color="#D3A452"/><stop offset="1" stop-color="#8A5F20"/></linearGradient>'
    s += '<radialGradient id="coinField" cx=".4" cy=".35" r=".8"><stop offset="0" stop-color="#F2D79A"/><stop offset=".7" stop-color="#C08C3B"/><stop offset="1" stop-color="#94662A"/></radialGradient></defs>'
    s += '<circle cx="150" cy="158" r="120" fill="#6B4A17"/>'
    s += '<circle cx="150" cy="150" r="120" fill="url(#coinFace)"/>'
    s += '<circle cx="150" cy="150" r="112" fill="none" stroke="#7E561C" stroke-width="7" stroke-dasharray="2 3.2" opacity=".55"/>'
    s += '<circle cx="150" cy="150" r="96" fill="none" stroke="#FFF1C9" stroke-opacity=".7" stroke-width="1.4"/>'
    s += '<circle cx="150" cy="150" r="90" fill="url(#coinField)"/>'
    s += '<circle cx="150" cy="150" r="90" fill="none" stroke="#7E561C" stroke-opacity=".5" stroke-width="1"/>'
    for txt, y, size, fam, ls, w in [("1", 172, 104, "Cormorant", 0, 600)]:
        s += f'<text x="152" y="{y+2.5}" text-anchor="middle" font-family="{fam}" font-weight="{w}" font-size="{size}" fill="#6B4A17" opacity=".75">{txt}</text>'
        s += f'<text x="149" y="{y-1}" text-anchor="middle" font-family="{fam}" font-weight="{w}" font-size="{size}" fill="#FFF3D0" opacity=".7">{txt}</text>'
        s += f'<text x="150" y="{y}" text-anchor="middle" font-family="{fam}" font-weight="{w}" font-size="{size}" fill="#C8933F">{txt}</text>'
    s += '<text x="150" y="203" text-anchor="middle" font-family="Cinzel" font-size="13" letter-spacing="6" fill="#5A3C10">OF ONE</text>'
    s += '<text x="150" y="98" text-anchor="middle" font-family="Cinzel" font-size="9" letter-spacing="4" fill="#5A3C10">TEZORO</text>'
    for ang in (-1, 1):
        s += f'<rect x="{150+ang*72-4}" y="146" width="8" height="8" fill="#5A3C10" transform="rotate(45 {150+ang*72} 150)"/>'
    s += '<ellipse cx="108" cy="78" rx="38" ry="14" fill="#fff" opacity=".22" transform="rotate(-35 108 78)"/>'
    s += sphere(262, 52, 15, "sViolet", shadow=False)
    s += sphere(36, 230, 11, "sGold", shadow=False)
    s += '</svg>'
    return s


def pillars():
    s = '<svg viewBox="0 0 600 250" xmlns="http://www.w3.org/2000/svg">'
    a = 34
    ground = 228
    for i in range(5):
        cx = 60 + i * 120
        t = 34 + i * 26
        y = ground - a - t
        s += f'<ellipse cx="{cx}" cy="{ground-a/2+6}" rx="{a*1.5}" ry="{a*0.42}" fill="url(#shadowLight)"/>'
        last = i == 4
        s += iso_block(cx, y, a, t,
                       top="url(#gGold)" if last else "#3A352E",
                       left="#B8893E" if last else "#26231E",
                       right="#7E561C" if last else "#141210",
                       label=str(i + 1), label_fill="#1A1814" if last else "#D9B877", label_size=26)
    s += sphere(540, 22, 13, "sGold", shadow=False)
    s += sphere(500, 50, 7, "sViolet", shadow=False)
    s += '</svg>'
    return s


def phone_insta():
    s = '<svg viewBox="0 0 260 520" xmlns="http://www.w3.org/2000/svg">'
    s += '<g filter="url(#drop)">'
    s += '<rect x="10" y="10" width="240" height="500" rx="40" fill="url(#gPhone)"/>'
    s += '<rect x="10.8" y="10.8" width="238.4" height="498.4" rx="39" fill="none" stroke="#D9B877" stroke-opacity=".45" stroke-width="1.2"/>'
    s += '</g>'
    s += '<rect x="22" y="22" width="216" height="476" rx="29" fill="#FBF8F3"/>'
    s += '<rect x="98" y="31" width="64" height="17" rx="8.5" fill="#0E0D0B"/>'
    s += '<text x="40" y="76" font-family="Inter" font-weight="700" font-size="11" fill="#1A1814">tezoro.atelier</text>'
    s += '<circle cx="218" cy="72" r="2" fill="#1A1814"/><circle cx="210" cy="72" r="2" fill="#1A1814"/><circle cx="202" cy="72" r="2" fill="#1A1814"/>'
    s += '<circle cx="66" cy="118" r="29" fill="none" stroke="url(#gGold)" stroke-width="2.4"/>'
    s += '<circle cx="66" cy="118" r="24.5" fill="#1A1814"/>'
    s += '<text x="66" y="128" text-anchor="middle" font-family="Cormorant" font-weight="600" font-size="28" fill="#D9B877">T</text>'
    for i, lab in enumerate(["Bespoke", "Wedding", "Atelier"]):
        x = 118 + i * 40
        s += f'<rect x="{x}" y="104" width="36" height="28" rx="6" fill="#F1E9DC"/>'
        s += f'<circle cx="{x+18}" cy="113" r="3.2" fill="#B8893E"/>'
        s += f'<text x="{x+18}" y="126" text-anchor="middle" font-family="Inter" font-size="6" fill="#6B6358">{lab}</text>'
    s += '<text x="40" y="168" font-family="Inter" font-weight="700" font-size="9.5" fill="#1A1814">TEZORO Atelier</text>'
    s += '<text x="40" y="182" font-family="Inter" font-size="8.4" fill="#4A443B">Made for you. Only you.</text>'
    s += '<text x="40" y="195" font-family="Inter" font-size="8.4" fill="#6B6358">Bespoke tailoring · Pothencode</text>'
    s += '<rect x="40" y="206" width="180" height="22" rx="6" fill="url(#gGoldH)"/>'
    s += '<text x="130" y="220.5" text-anchor="middle" font-family="Inter" font-weight="700" font-size="8" letter-spacing=".8" fill="#1A1814">BOOK A FITTING</text>'
    tiles = [("#14213D", "#2A3B66"), ("#C9973F", "#E9C77E"), ("#0F3D2E", "#1F5C47"),
             ("#2B2B2B", "#4A453E"), ("#F1E7D6", "#D8C9AE"), ("#14213D", "#22345C"),
             ("#B8893E", "#7E561C"), ("#1A1814", "#3A352E"), ("#0F3D2E", "#2B6B53")]
    for k, (c1, c2) in enumerate(tiles):
        r, c = divmod(k, 3)
        x = 32 + c * 66
        y = 242 + r * 66
        s += f'<defs><linearGradient id="tile{k}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c2}"/><stop offset="1" stop-color="{c1}"/></linearGradient></defs>'
        s += f'<rect x="{x}" y="{y}" width="62" height="62" fill="url(#tile{k})"/>'
        light = c1 in ("#F1E7D6", "#C9973F", "#B8893E")
        ic = "#1A1814" if light else "#E9C77E"
        if k in (0, 2, 4, 6, 8):
            # stylised jacket
            cx, cy = x + 31, y + 33
            s += (f'<path d="M{cx-14} {cy-12} L{cx-5} {cy-17} L{cx} {cy-6} L{cx+5} {cy-17} L{cx+14} {cy-12} '
                  f'L{cx+16} {cy+18} L{cx-16} {cy+18} Z" fill="none" stroke="{ic}" stroke-width="1.3" stroke-linejoin="round"/>'
                  f'<path d="M{cx} {cy-6} L{cx} {cy+18}" stroke="{ic}" stroke-width="1"/>'
                  f'<circle cx="{cx+2.6}" cy="{cy+4}" r="1" fill="{ic}"/><circle cx="{cx+2.6}" cy="{cy+10}" r="1" fill="{ic}"/>')
        else:
            cx, cy = x + 31, y + 31
            s += f'<text x="{cx}" y="{cy+6}" text-anchor="middle" font-family="Cinzel" font-size="13" letter-spacing="1.5" fill="{ic}">1/1</text>'
    s += '<rect x="22" y="452" width="216" height="46" rx="0" fill="#FBF8F3"/>'
    s += '<path d="M22 452 h216 v17 a29 29 0 0 1 -29 29 h-158 a29 29 0 0 1 -29 -29 Z" fill="#FBF8F3"/>'
    for i in range(5):
        s += f'<circle cx="{58+i*36}" cy="472" r="{4 if i!=2 else 5}" fill="{"#B8893E" if i==2 else "#C9BBA2"}"/>'
    s += '<rect x="104" y="488" width="52" height="4" rx="2" fill="#1A1814" opacity=".6"/>'
    s += '<path d="M40 30 L120 30 L40 300 Z" fill="url(#gGlass)" opacity=".35"/>'
    s += '</svg>'
    return s


def laptop():
    s = '<svg viewBox="0 0 440 290" xmlns="http://www.w3.org/2000/svg">'
    s += '<ellipse cx="215" cy="268" rx="215" ry="16" fill="url(#shadowDark)"/>'
    # lid
    s += '<g filter="url(#drop)"><rect x="55" y="12" width="320" height="210" rx="12" fill="#14120F"/></g>'
    s += '<rect x="55.6" y="12.6" width="318.8" height="208.8" rx="11.5" fill="none" stroke="#5A544A" stroke-width="1.2"/>'
    s += '<rect x="66" y="23" width="298" height="187" rx="3" fill="#FBF8F3"/>'
    # nav
    s += '<text x="78" y="36" font-family="Cinzel" font-size="8.5" letter-spacing="2" fill="#1A1814">TEZORO</text>'
    for i, w in enumerate([22, 26, 24, 20]):
        s += f'<rect x="{200+i*34}" y="31" width="{w}" height="3" rx="1.5" fill="#B8A88E"/>'
    # hero
    s += '<rect x="66" y="43" width="298" height="96" fill="url(#gHero)"/>'
    s += '<text x="80" y="76" font-family="Cormorant" font-weight="500" font-size="20" fill="#F5EFE6">Made for you.</text>'
    s += '<text x="80" y="98" font-family="Cormorant" font-style="italic" font-weight="500" font-size="20" fill="#D9B877">Only you.</text>'
    s += '<rect x="80" y="110" width="62" height="14" rx="1" fill="url(#gGoldH)"/>'
    s += '<text x="111" y="119.5" text-anchor="middle" font-family="Inter" font-weight="700" font-size="5.2" letter-spacing=".8" fill="#1A1814">BOOK A FITTING</text>'
    # hero art: mini bag + sphere
    s += '<circle cx="300" cy="92" r="40" fill="#B8893E" opacity=".14" filter="url(#blur6)"/>'
    s += '<g transform="translate(262 52) scale(.19)">' + bag("lap", tag=False) + '</g>'
    s += sphere(342, 66, 7, "sGold", shadow=False)
    # tiles
    labels = [("Bespoke", "#14213D", "#2A3B66"), ("Wedding Floor", "#0F3D2E", "#1F5C47"), ("Ready-to-Wear", "#7E561C", "#D4A653")]
    for i, (lab, c1, c2) in enumerate(labels):
        x = 78 + i * 94
        s += f'<defs><linearGradient id="lt{i}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c2}"/><stop offset="1" stop-color="{c1}"/></linearGradient></defs>'
        s += f'<rect x="{x}" y="148" width="86" height="40" fill="url(#lt{i})"/>'
        s += f'<text x="{x+6}" y="200" font-family="Inter" font-weight="600" font-size="6" fill="#1A1814">{lab}</text>'
        cx, cy = x + 43, 168
        s += (f'<path d="M{cx-8} {cy-8} L{cx-3} {cy-11} L{cx} {cy-4} L{cx+3} {cy-11} L{cx+8} {cy-8} L{cx+9} {cy+10} L{cx-9} {cy+10} Z" '
              f'fill="none" stroke="#F1D9A0" stroke-width="1"/>')
    # base
    s += '<path d="M14 226 L416 226 L404 246 Q400 251 390 251 L40 251 Q30 251 26 246 Z" fill="url(#gMetal)"/>'
    s += '<rect x="14" y="224" width="402" height="5" rx="2" fill="#6A6258"/>'
    s += '<rect x="185" y="226" width="60" height="5" rx="2.5" fill="#2B2823"/>'
    s += '<path d="M66 23 L150 23 L66 140 Z" fill="#fff" opacity=".06"/>'
    # small phone
    s += '<g transform="translate(366 120)">'
    s += '<g filter="url(#drop)"><rect x="0" y="0" width="64" height="130" rx="12" fill="url(#gPhone)"/></g>'
    s += '<rect x="4" y="4" width="56" height="122" rx="9" fill="#FBF8F3"/>'
    s += '<rect x="4" y="14" width="56" height="52" fill="url(#gHero)"/>'
    s += '<text x="10" y="11.5" font-family="Cinzel" font-size="5" letter-spacing="1" fill="#1A1814">TEZORO</text>'
    s += '<text x="10" y="34" font-family="Cormorant" font-size="9" fill="#F5EFE6">Made for you.</text>'
    s += '<text x="10" y="45" font-family="Cormorant" font-style="italic" font-size="9" fill="#D9B877">Only you.</text>'
    s += '<rect x="10" y="51" width="28" height="7" fill="url(#gGoldH)"/>'
    s += '<rect x="10" y="72" width="44" height="22" fill="#14213D"/><rect x="10" y="98" width="21" height="20" fill="#0F3D2E"/><rect x="33" y="98" width="21" height="20" fill="#C9973F"/>'
    s += '</g>'
    s += '</svg>'
    return s


def about_stack():
    s = '<svg viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg">'
    s += '<ellipse cx="130" cy="262" rx="120" ry="24" fill="url(#shadowLight)"/>'
    layers = [
        ("#26231E", "#141210", "#3A352E"),
        ("#4C26B5", "#2E1580", "url(#sViolet)"),
        ("#D8CCB6", "#B8A88E", "#F5EFE6"),
        ("#B8893E", "#7E561C", "url(#gGold)"),
    ]
    a = 92
    t = 18
    base = 190
    for i, (left, right, top) in enumerate(layers):
        y = base - i * 40
        s += iso_block(130, y - a / 2, a, t, top, left, right)
    s += '<ellipse cx="130" cy="72" rx="18" ry="5" fill="#3B2A10" opacity=".35"/>'
    s += sphere(130, 56, 16, "sGold", shadow=False)
    s += sphere(258, 70, 10, "sViolet", shadow=False)
    s += '</svg>'
    return s


def orbs_contact():
    s = '<svg viewBox="0 0 600 850" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">'
    s += sphere(90, 150, 46, "sGold", shadow=False)
    s += sphere(520, 120, 26, "sViolet", shadow=False)
    s += sphere(530, 700, 54, "sInk", shadow=False)
    s += sphere(70, 720, 20, "sViolet", shadow=False)
    s += sphere(470, 770, 14, "sGold", shadow=False)
    s += ring(510, 230, 46, 16, rot=-22, w=8)
    s += ring(100, 620, 38, 13, rot=18, w=7)
    s += '</svg>'
    return s


def cover_art():
    s = '<svg viewBox="0 0 480 520" xmlns="http://www.w3.org/2000/svg">'
    s += '<circle cx="250" cy="250" r="190" fill="#B8893E" opacity=".18" filter="url(#blur6)"/>'
    s += '<g transform="translate(40 30)">' + bag("cov") + '</g>'
    s += sphere(58, 330, 30, "sGold", shadow=True, sh_dy=140)
    s += sphere(430, 92, 18, "sViolet", shadow=False)
    s += sphere(455, 420, 11, "sGold", shadow=False)
    s += ring(116, 104, 44, 15, rot=-24, w=8)
    s += '</svg>'
    return s


def palette_bag(uid, c_front, c_side, accent, text, sub):
    s = '<svg viewBox="40 20 360 450" xmlns="http://www.w3.org/2000/svg">'
    s += bag(uid, front=c_front, side=c_side, inside="#000", accent=accent, text=text, sub=sub,
             tag=False, dark_bg=False, handle=accent)
    s += '</svg>'
    return s


def mono3d():
    s = '<svg viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">'
    s += '<ellipse cx="60" cy="110" rx="40" ry="6" fill="url(#shadowLight)"/>'
    s += '<rect x="14" y="14" width="88" height="88" fill="#1A1814"/>'
    s += '<polygon points="102,14 110,8 110,96 102,102" fill="#0E0D0B"/>'
    s += '<polygon points="14,14 22,8 110,8 102,14" fill="#3A352E"/>'
    s += '<rect x="20" y="20" width="76" height="76" fill="none" stroke="#B8893E" stroke-opacity=".6"/>'
    for i in range(6, 0, -1):
        s += f'<text x="{58+i*0.7}" y="{80+i*0.7}" text-anchor="middle" font-family="Cormorant" font-weight="600" font-size="62" fill="#5E3E13">T</text>'
    s += '<text x="58" y="80" text-anchor="middle" font-family="Cormorant" font-weight="600" font-size="62" fill="#D4A653">T</text>'
    s += '</svg>'
    return s
