# HANDOFF — Tezoro × DARTS AI

> **Read this first.** It is the single source of truth for this repo. An LLM or teammate should be able to continue the work from this file alone.
> Last updated: 2026-10-20 · Status: **Final proposal delivered (v5)** · Next step: send to client, await palette choice.

---

## 0. TL;DR (30-second context)

```
WHO        DARTS AI (brand of DanRosh Tech Solutions Pvt Ltd) → sending a proposal/quotation
TO         Tezoro — premium men's custom-tailoring + men's wedding-floor boutique, Pothencode (Thiruvananthapuram, Kerala)
CLIENT     Mr. Safnal
WHAT       8-page A4 PDF brochure-quote: brand identity + website
PRICE      ₹28,000 one-time = Website & Brand Identity ₹25,000 + Logo Design ₹3,000
           domain & hosting INCLUDED · NO GST shown/collected
FINAL FILE proposal/Tezoro_Brand_Proposal_DARTS_AI.pdf   (built from proposal/source/brochure.html)
DESIGN     "v1 luxury" look: charcoal #1A1814 / ivory #F5EFE6 / antique gold #B8893E, Cormorant + Cinzel + Inter
```

---

## 1. Repo tree

```
tezoro/
├── HANDOFF.md                      ← you are here (master context)
├── AGENTS.md / CLAUDE.md           ← short pointers for AI agents → this file
├── README.md                       ← human summary + build command
├── proposal/                       ← ★ CURRENT DELIVERABLE
│   ├── Tezoro_Brand_Proposal_DARTS_AI.pdf     final 8-page A4 PDF (v5)
│   └── source/
│       ├── brochure.html           ★ edit this — all copy, CSS, layout (single file)
│       ├── render.py               HTML → PDF (Playwright/Chromium, A4, backgrounds on)
│       ├── fonts/                  Cormorant (+Italic), Cinzel — variable TTFs (Inter = system font)
│       ├── logo_original.png       DARTS AI logo as supplied (white bg) → used on LAST page in a white card
│       ├── logo_dark.png           cut-out, black parts recoloured ivory → used on COVER (dark bg)
│       └── logo_light.png          transparent cut-out, original colours (not used in v5)
├── context/
│   ├── conversation-log.md         every request → decision, in order (why things are the way they are)
│   ├── final-content.md            final copy, page by page (plain text, easy to reuse)
│   └── brand-palettes.json         the 4 colour options + brochure design tokens (machine-readable)
├── references/
│   ├── client-renders/             AI renders of the planned storefront (day/night) — NOT real; do not use as design basis
│   └── darts-ai/darts-ai-logo-original.png
└── archive/                        superseded versions (kept for reference; do not send)
    ├── v1-luxury/                  original v1 (₹25k, free logo) — design the client liked
    ├── v2-3d/                      3D-illustration edition (rejected: "boring")
    ├── v3-minimal/                 white minimal edition (rejected: user preferred v1)
    └── v4-deck-landscape/          16:9 deck using a pitch-deck template's layout (rejected: "just need v1")
```

Not in repo (public repo, third-party/licensed): the purchased **"Minimalist Pitch Deck" Google Slides template** zip and the **"AM Design Studio" bag photo** used as a colour reference. See §6.

---

## 2. Client brief (as understood)

- **Business:** Tezoro (store signage in renders: "TEZORO ATELIER"), opening near **Zudio, Pothencode**.
- **Concept:** exclusive, premium men's **custom tailoring** + a boutique-style **men's wedding floor**.
- **Core idea:** *every man dresses unique — no duplicates* (unlike mass retail where many people wear the same piece). Brand promise used: **"Every man deserves a look that is his alone."** / "Made for you, only you."
- **Concept reference:** instagram.com/thritchfashion
- **Website references (for later build):** tajtailor.com, modasou.com
- **Initial services wanted:** minimalist logo, brand colours, website.
- **Name note:** "tesoro" = treasure (IT/ES); brand spells it **Tezoro**.

## 3. Sender details (DARTS AI)

| Field | Value |
|---|---|
| Brand | DARTS AI (DARTS AI Academy logo) |
| Company | DanRosh Tech Solutions Pvt Ltd |
| Offices | India · Slovenia (HQ) · United States |
| Phone / WhatsApp | +91 70120 45854 |
| Email (for this quote) | **cto@dartsai.in** (not contact@) |
| Website | info.dartsai.in |
| GST | not shown, not collected |
| Quote no. | DAI/TZ/2026/001 · dated 20 October 2026 |

## 4. Final brochure — page map (v5)

| # | Page | Background | Key content |
|---|---|---|---|
| 1 | Cover | dark | DARTS logo (ivory-recoloured), quote no/date, "Brand Identity & *Digital Presence* Proposal", Prepared for **TEZORO** · *Mr. Safnal* |
| 2 | 01 About Us | ivory | "Technology that builds brands", 3 stats, 4 services, India·Slovenia·USA — **no logo** |
| 3 | 02 Our Understanding | ivory | Tezoro idea, promise quote, 4 pillars |
| 4 | 03 Our Approach | ivory | 5 steps Discover→Define→Design→Digitise→Grow + "What Tezoro achieves" (4 points) |
| 5 | 04 Brand Colours | ivory | **4 palettes A–D** + logo direction (minimal serif wordmark + "T" monogram) |
| 6 | 05 Why It Matters | ivory + dark hero | branding ×3, digital marketing ×3, "24/7" line |
| 7 | 06 Investment | dark (flat, no glow) | **Premium Starter Kit ₹28,000** (₹25,000 + ₹3,000), 6 inclusions by name, 5 platform advantages |
| 8 | Contact | dark | **original logo on white card**, phone, email, website |

## 5. Pricing (locked)

```
PREMIUM STARTER KIT ............................ ₹28,000  (one-time)
 ├─ Website & Brand Identity ................... ₹25,000
 │    premium business website · brand colours & typography · 3D brand assets & mockups
 │    · professional brand elements · domain & hosting (included)
 └─ Logo Design ................................ ₹3,000   (no longer "free")
Not shown (removed on request): add-ons, timeline, terms, GST, itemised "market value" list.
Website platform: Shopify-based, but NEVER name Shopify — only describe benefits
(sell online anytime, UPI/cards/wallets, SSL/uptime, no-code updates, scales to more stores).
```

## 6. Brand colour options (see context/brand-palettes.json)

| Opt | Name | Colours | Note |
|---|---|---|---|
| A | Ivory & Antique Gold | #F5EFE6 · #B8893E · #2B2B2B | timeless luxury |
| B | Midnight Navy & Champagne | #14213D · #D4B483 · #F4F1EA | suits-first |
| C | Royal Emerald & Gold | #0F3D2E · #C9A227 · #FAF7F0 | wedding floor |
| D | Espresso & Taupe | #2E241D · #BFAE99 · #E4D9CA | from user's mood photo (dark-brown gift bag, taupe arched tag, black grosgrain ribbon, sandstone plinth) |

## 7. Style rules / user preferences learned (follow these)

- User prefers the **v1 luxury design** over 3D, minimal-white and deck-landscape variants.
- **DARTS logo only on first and last page.** Last page uses the **original-colour logo on a white card**.
- **No pink/purple on the pricing page** (removed violet "FREE" badge and the warm glow).
- Don't use "opposite of Zudio" wording — describe how *we* will brand Tezoro and what Tezoro gains by staying with DARTS AI.
- No portfolio/project list in About.
- Store renders are AI-generated → ignore them as design input.
- Copy should stay short (user asked for ~25% cuts).
- Client name on cover: "Mr. Safnal" (no "Attn.").

## 8. How to edit & rebuild

```bash
pip install playwright && playwright install chromium     # Inter font must be installed system-wide
cd proposal/source && python3 render.py                    # → ../Tezoro_Brand_Proposal_DARTS_AI.pdf
```
Gotchas (Chromium → PDF):
- Don't fill SVG `<text>` with gradients — renders as a solid gradient box. Use solid colours.
- `background-clip:text` gradients leave edge artefacts in PDF — use solid colour + text-shadow.
- Cinzel variable font can mis-render "Z" at some sizes; Cormorant uppercase is the safe wordmark font.
- Each page is a fixed 210×297mm `<section class="page">`; content overflowing into the footer is the usual failure — re-render and check page 7 especially.

## 9. Open items / next steps

- [ ] Send PDF to Mr. Safnal; get palette choice (A/B/C/D).
- [ ] Confirm GSTIN situation if invoices are needed later (currently none).
- [ ] After approval: logo concepts → brand kit → website (refs: tajtailor.com, modasou.com).
- [ ] Check trademark / Instagram handle availability for "Tezoro" (suggested early; not done).
