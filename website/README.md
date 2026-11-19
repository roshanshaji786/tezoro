# Tezoro Atelier website

Custom site for Tezoro Atelier (men's bespoke tailoring and wedding floor, Pothencode). Built by DARTS AI.

**Stack:** Next.js 15 (App Router) · Tailwind CSS 4 · Three.js via React Three Fiber · Supabase (Postgres) · Vercel. All on free tiers.

## What is in it

| Page | What it does |
|---|---|
| `/` | 3D silk hero: a needle sews a champagne running stitch across moving navy cloth (WebGL, pauses off-screen, still frame for reduced motion) |
| `/bespoke` | Services with "from" prices, craft details, style options |
| `/wedding` | Maroon sub-brand. Wedding planner: enter the date, get a backwards fitting timeline. Packages. |
| `/lookbook` | Filterable past commissions. "Have one made" opens WhatsApp with the look code. |
| `/fabrics` | Fabric library with a draggable 3D swatch per cloth (procedural woven shaders) |
| `/process` | Six steps plus FAQ |
| `/one-of-one` | Public register of numbered garments (database, falls back to sample entries) |
| `/book` | Three-step booking: purpose, date and slot, details. Saved to the database, then confirmed on WhatsApp. |
| `/track/[code]` | Customer order tracker (sample code `TZ-0147`) |
| `/visit` | Map, hours, directions |
| `/admin` | Staff desk: today's fittings, booking status, orders with one-tap stage updates, issue One of One numbers |

The floating WhatsApp button pre-fills a message that matches the page the visitor is on.

## Run locally

```bash
npm install
cp .env.example .env.local   # fill in the values
npm run dev
```

## Database

1. Create a Supabase project (free tier).
2. Run `supabase/schema.sql` in the SQL editor.
3. Set `SUPABASE_URL` and `SUPABASE_SERVICE_ROLE_KEY` in Vercel. The key is only used on the server; RLS is on with no public policies.
4. Set `ADMIN_PASSWORD` (and optionally `ADMIN_SECRET`) to switch on `/admin`.

Without the database the site still works: bookings go through WhatsApp, the register and tracker show sample data.

## To confirm with the client (placeholders)

- Domain, email and Instagram handle (`src/lib/site.ts`)
- All "from" prices and package prices (`src/lib/content.ts`)
- Policies in the FAQ: part payment, free alterations for three months, home measurement day
- Opening hours, slot times
- Logo: the hanger-arch mark in `src/components/Logo.tsx` is not final
- Real photography to replace the woven-cloth illustrations
