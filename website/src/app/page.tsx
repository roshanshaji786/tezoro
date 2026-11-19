import Link from "next/link";
import { HeroScene } from "@/components/three";
import { FabricArt } from "@/components/FabricArt";
import { Reveal } from "@/components/Reveal";
import { SectionTitle } from "@/components/PageIntro";
import { fabricById, looks, processSteps, services } from "@/lib/content";
import { site } from "@/lib/site";

const paths = [
  { href: "/bespoke", eyebrow: "I", title: "Bespoke", text: "Suits, shirts and trousers drafted for one man.", pattern: "twill", base: "#14213D", accent: "#2a3a63" },
  { href: "/wedding", eyebrow: "II", title: "The Wedding Floor", text: "Sherwanis, bandhgalas and the whole family, planned to the day.", pattern: "brocade", base: "#5A1A24", accent: "#c8a66f" },
  { href: "/lookbook", eyebrow: "III", title: "Lookbook", text: "Past commissions to spark your own. Never copied, only inspired.", pattern: "herringbone", base: "#a8957a", accent: "#cbb89b" },
] as const;

const promises = [
  { title: "One of one", text: "Every garment is numbered in our register. We never cut the same piece twice." },
  { title: "Two fittings, minimum", text: "Fit is made on your body, not on a size chart." },
  { title: "Your pattern, kept", text: "Reorder shirts from Dubai or Bengaluru with a single message." },
  { title: "Delivered on time", text: "For weddings we plan backwards from the date, with a buffer built in." },
];

export default function Home() {
  return (
    <>
      {/* HERO */}
      <section className="relative h-[100svh] min-h-[640px] overflow-hidden bg-navy-deep text-ivory">
        <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_60%_60%,#1b2b52_0%,#0b1426_70%)]" />
        <HeroScene />
        <div className="pointer-events-none absolute inset-0 bg-gradient-to-b from-navy-deep/60 via-transparent to-navy-deep/90" />
        <div className="pointer-events-none absolute inset-0 bg-gradient-to-r from-navy-deep/85 via-navy-deep/30 to-transparent max-sm:bg-gradient-to-t max-sm:from-navy-deep max-sm:via-navy-deep/60" />
        <div className="relative z-10 mx-auto flex h-full max-w-7xl flex-col justify-end px-4 pb-20 sm:px-8 sm:pb-24">
          <p className="eyebrow text-champagne">Bespoke tailoring · Wedding floor · Thiruvananthapuram</p>
          <h1 className="display mt-6 max-w-4xl text-[3.4rem] sm:text-8xl lg:text-[7.5rem]">
            Made for you,
            <br />
            <em className="text-champagne">only you.</em>
          </h1>
          <p className="mt-6 max-w-lg text-base leading-relaxed text-ivory/75 sm:text-lg">
            No racks of the same jacket. Every Tezoro piece is drafted, cut and fitted for one man, then numbered so it can never be made again.
          </p>
          <div className="pointer-events-auto mt-10 flex flex-col gap-3 sm:flex-row">
            <Link href="/book" className="btn btn-gold">
              Book a fitting
            </Link>
            <Link href="/wedding" className="btn btn-ghost-light">
              The Wedding Floor
            </Link>
          </div>
        </div>
        <div className="absolute right-6 bottom-8 hidden items-center gap-3 text-ivory/50 sm:flex">
          <span className="eyebrow">Scroll</span>
          <span className="h-10 w-px animate-pulse bg-champagne/60" />
        </div>
      </section>

      {/* THREE PATHS */}
      <section className="mx-auto max-w-7xl px-4 py-24 sm:px-8 sm:py-32">
        <Reveal>
          <SectionTitle eyebrow="Where would you like to begin" title={<>Three doors into <em>the atelier</em></>} />
        </Reveal>
        <div className="mt-14 grid gap-6 md:grid-cols-3">
          {paths.map((p, i) => (
            <Reveal key={p.href} delay={i * 120}>
              <Link href={p.href} className="group relative block aspect-[4/5] overflow-hidden">
                <div className="absolute inset-0 transition-transform duration-[1.6s] ease-[var(--ease-silk)] group-hover:scale-105">
                  <FabricArt pattern={p.pattern} base={p.base} accent={p.accent} scale={1.4} />
                </div>
                <div className="absolute inset-0 bg-gradient-to-t from-black/70 via-black/10 to-transparent" />
                <div className="absolute inset-x-0 bottom-0 p-7 text-ivory">
                  <p className="eyebrow text-champagne">{p.eyebrow}</p>
                  <h3 className="display mt-3 text-4xl">{p.title}</h3>
                  <p className="mt-3 max-w-xs text-sm text-ivory/75">{p.text}</p>
                  <span className="eyebrow mt-6 inline-flex items-center gap-3 text-champagne">
                    Enter <span className="h-px w-8 bg-champagne transition-all duration-500 group-hover:w-14" />
                  </span>
                </div>
              </Link>
            </Reveal>
          ))}
        </div>
      </section>

      {/* MANIFESTO */}
      <section className="grain bg-navy text-ivory">
        <div className="relative z-[2] mx-auto grid max-w-7xl gap-12 px-4 py-24 sm:px-8 sm:py-32 lg:grid-cols-2">
          <Reveal>
            <p className="eyebrow text-champagne">Tezoro · treasure</p>
            <p className="display mt-6 text-4xl leading-tight sm:text-5xl">
              In a town where a hundred men wear the same shirt from the same shop, we make the one that is <em className="text-champagne">only yours</em>.
            </p>
          </Reveal>
          <div className="grid gap-8 sm:grid-cols-2">
            {promises.map((p, i) => (
              <Reveal key={p.title} delay={i * 100}>
                <div className="border-t border-champagne/30 pt-5">
                  <h3 className="display text-2xl text-champagne">{p.title}</h3>
                  <p className="mt-2 text-sm leading-relaxed text-ivory/70">{p.text}</p>
                </div>
              </Reveal>
            ))}
          </div>
        </div>
      </section>

      {/* PROCESS */}
      <section className="mx-auto max-w-7xl px-4 py-24 sm:px-8 sm:py-32">
        <div className="flex flex-col justify-between gap-6 md:flex-row md:items-end">
          <Reveal>
            <SectionTitle eyebrow="How it works" title={<>From first chalk mark <br className="hidden sm:block" />to final press</>} />
          </Reveal>
          <Link href="/process" className="btn btn-ghost-dark self-start md:self-auto">
            The full process
          </Link>
        </div>
        <ol className="mt-14 grid gap-px overflow-hidden bg-navy/10 sm:grid-cols-2 lg:grid-cols-3">
          {processSteps.map((s, i) => (
            <Reveal as="li" key={s.n} delay={i * 80} className="bg-ivory p-8">
              <p className="display text-5xl text-gold">{s.n}</p>
              <h3 className="display mt-4 text-3xl text-navy">{s.title}</h3>
              <p className="mt-3 text-sm leading-relaxed text-ink/70">{s.text}</p>
              <p className="eyebrow mt-5 text-stone">{s.days}</p>
            </Reveal>
          ))}
        </ol>
      </section>

      {/* LOOKBOOK STRIP */}
      <section className="bg-ivory-deep py-24 sm:py-32">
        <div className="mx-auto flex max-w-7xl items-end justify-between gap-6 px-4 sm:px-8">
          <Reveal>
            <SectionTitle eyebrow="Lookbook" title={<>Recent <em>commissions</em></>} />
          </Reveal>
          <Link href="/lookbook" className="eyebrow hidden text-navy hover:text-champagne sm:block">
            View all →
          </Link>
        </div>
        <div className="no-scrollbar mt-12 flex snap-x snap-mandatory gap-5 overflow-x-auto px-4 pb-4 sm:px-8">
          {looks.slice(0, 6).map((l) => {
            const f = fabricById(l.fabricId);
            return (
              <Link key={l.code} href={`/lookbook#${l.code}`} className="group w-[72vw] max-w-[320px] shrink-0 snap-start">
                <div className="relative aspect-[3/4] overflow-hidden">
                  <div className="absolute inset-0 transition-transform duration-[1.4s] group-hover:scale-105">
                    <FabricArt pattern={f.pattern} base={f.base} accent={f.accent} scale={1.2} />
                  </div>
                  <span className="eyebrow absolute top-4 left-4 bg-ivory/90 px-2 py-1 text-[0.6rem] text-navy">{l.code}</span>
                </div>
                <p className="eyebrow mt-4 text-stone">{l.occasion}</p>
                <h3 className="display mt-1 text-2xl text-navy">{l.title}</h3>
              </Link>
            );
          })}
        </div>
      </section>

      {/* ONE OF ONE */}
      <section className="grain relative overflow-hidden bg-navy-deep text-ivory">
        <div className="relative z-[2] mx-auto grid max-w-7xl items-center gap-12 px-4 py-24 sm:px-8 sm:py-32 lg:grid-cols-[1fr_1.1fr]">
          <Reveal>
            <p className="eyebrow text-champagne">The One of One register</p>
            <h2 className="display mt-5 text-5xl sm:text-6xl">
              No. 0001 to now.
              <br />
              <em className="text-champagne">No two alike.</em>
            </h2>
            <p className="mt-6 max-w-md text-ivory/70">
              Each finished garment carries a hand-numbered label inside, and an entry in our public register. It is our promise, written down.
            </p>
            <Link href="/one-of-one" className="btn btn-gold mt-10">
              See the register
            </Link>
          </Reveal>
          <Reveal delay={150}>
            <div className="relative mx-auto aspect-[5/3] w-full max-w-lg rotate-[-3deg] bg-ivory p-8 text-navy shadow-[0_40px_80px_rgba(0,0,0,0.45)]">
              <div className="flex h-full flex-col justify-between border border-champagne/60 p-6">
                <div className="flex items-start justify-between">
                  <p className="eyebrow text-[0.6rem] text-stone">Tezoro Atelier · Pothencode</p>
                  <p className="eyebrow text-[0.6rem] text-gold">One of one</p>
                </div>
                <p className="display text-center text-6xl sm:text-7xl">No. 0147</p>
                <div className="flex items-end justify-between text-xs text-stone">
                  <span>Cut for: A. R.</span>
                  <span>Ivory brocade sherwani</span>
                  <span>Nov 2026</span>
                </div>
              </div>
            </div>
          </Reveal>
        </div>
      </section>

      {/* SERVICES TEASER */}
      <section className="mx-auto max-w-7xl px-4 py-24 sm:px-8 sm:py-32">
        <Reveal>
          <SectionTitle eyebrow="What we make" title="Cut to measure, priced with care" />
        </Reveal>
        <div className="mt-14 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
          {services.map((s, i) => (
            <Reveal key={s.title} delay={i * 90}>
              <Link href="/bespoke" className="group block">
                <div className="relative aspect-square overflow-hidden">
                  <div className="absolute inset-0 transition-transform duration-[1.4s] group-hover:scale-105">
                    <FabricArt pattern={s.pattern} base={s.base} accent={s.accent} scale={1.3} />
                  </div>
                </div>
                <h3 className="display mt-5 text-3xl text-navy">{s.title}</h3>
                <p className="eyebrow mt-2 text-stone">From {s.from}</p>
              </Link>
            </Reveal>
          ))}
        </div>
      </section>

      {/* VISIT */}
      <section className="bg-ivory-deep">
        <div className="mx-auto grid max-w-7xl gap-10 px-4 py-24 sm:px-8 lg:grid-cols-2">
          <Reveal>
            <SectionTitle eyebrow="Visit the atelier" title={<>Tea is on us. <em>Take your time.</em></>} />
            <p className="mt-6 text-ink/70">
              {site.address.line1}, {site.address.line2}
            </p>
            <ul className="mt-4 space-y-1 text-ink/70">
              {site.hours.map((h) => (
                <li key={h.days}>
                  <span className="text-navy">{h.days}</span> · {h.time}
                </li>
              ))}
            </ul>
            <div className="mt-8 flex flex-col gap-3 sm:flex-row">
              <Link href="/book" className="btn btn-navy">
                Book a fitting
              </Link>
              <Link href="/visit" className="btn btn-ghost-dark">
                Directions
              </Link>
            </div>
          </Reveal>
          <Reveal delay={120}>
            <div className="aspect-[4/3] w-full overflow-hidden bg-navy/10">
              <iframe
                title="Map to Tezoro Atelier"
                className="h-full w-full grayscale-[60%]"
                loading="lazy"
                src={`https://maps.google.com/maps?q=${encodeURIComponent(site.address.mapQuery)}&z=15&output=embed`}
              />
            </div>
          </Reveal>
        </div>
      </section>
    </>
  );
}
