import type { Metadata } from "next";
import Link from "next/link";
import { WeddingPlanner } from "./WeddingPlanner";
import { FabricArt } from "@/components/FabricArt";
import { Reveal } from "@/components/Reveal";
import { SectionTitle } from "@/components/PageIntro";
import { looks, fabricById, packages } from "@/lib/content";
import { whatsappLink } from "@/lib/site";

export const metadata: Metadata = {
  title: "The Wedding Floor · Sherwanis, bandhgalas and groom packages",
  description: "Wedding sherwanis, bandhgalas, reception suits and family outfits in Thiruvananthapuram. Plan your wedding wardrobe backwards from the date.",
};

export default function Wedding() {
  const weddingLooks = looks.filter((l) => l.category === "Wedding" || l.code === "L07" || l.code === "L02");
  return (
    <>
      <section className="grain relative overflow-hidden bg-maroon-deep pt-36 pb-20 text-ivory sm:pt-44">
        <div className="absolute inset-0 opacity-25">
          <FabricArt pattern="brocade" base="#3d1118" accent="#c8a66f" scale={2.2} />
        </div>
        <div className="absolute inset-0 bg-gradient-to-b from-maroon-deep/40 via-maroon-deep/70 to-maroon-deep" />
        <div className="relative z-[2] mx-auto max-w-7xl px-4 sm:px-8">
          <p className="eyebrow text-champagne">The Wedding Floor</p>
          <h1 className="display mt-5 max-w-4xl text-5xl sm:text-8xl">
            The most photographed
            <br />
            <em className="text-champagne">day of your life.</em>
          </h1>
          <p className="mt-6 max-w-xl text-lg text-ivory/75">
            Sherwanis, bandhgalas, reception suits and the whole family, planned backwards from your date so nothing is rushed.
          </p>
        </div>
      </section>

      <section className="bg-maroon text-ivory">
        <div className="mx-auto max-w-7xl px-4 py-20 sm:px-8 sm:py-28">
          <Reveal>
            <SectionTitle eyebrow="Wedding planner" title={<>Tell us the date. <em className="text-champagne">We plan the rest.</em></>} light />
          </Reveal>
          <div className="mt-14">
            <WeddingPlanner />
          </div>
        </div>
      </section>

      <section className="bg-ivory">
        <div className="mx-auto max-w-7xl px-4 py-24 sm:px-8 sm:py-32">
          <Reveal>
            <SectionTitle eyebrow="Packages" title="For the groom, and everyone beside him" />
          </Reveal>
          <div className="mt-14 grid gap-6 lg:grid-cols-3">
            {packages.map((p, i) => (
              <Reveal key={p.name} delay={i * 120}>
                <div className={`flex h-full flex-col p-8 sm:p-10 ${p.featured ? "bg-maroon text-ivory" : "border border-maroon/20 text-ink"}`}>
                  {p.featured && <p className="eyebrow mb-4 text-champagne">Most chosen</p>}
                  <h3 className={`display text-4xl ${p.featured ? "text-ivory" : "text-maroon"}`}>{p.name}</h3>
                  <p className={`display mt-3 text-2xl ${p.featured ? "text-champagne" : "text-stone"}`}>
                    {p.from === "On request" ? p.from : `from ${p.from}`}
                  </p>
                  <ul className={`mt-8 flex-1 space-y-3 text-sm ${p.featured ? "text-ivory/80" : "text-ink/70"}`}>
                    {p.items.map((it) => (
                      <li key={it} className="flex gap-3">
                        <span className="mt-2 h-px w-4 shrink-0 bg-champagne" />
                        {it}
                      </li>
                    ))}
                  </ul>
                  <Link href={`/book?purpose=wedding&package=${encodeURIComponent(p.name)}`} className={`btn mt-10 ${p.featured ? "btn-gold" : "btn-ghost-dark"}`}>
                    Book a consult
                  </Link>
                </div>
              </Reveal>
            ))}
          </div>
          <p className="mt-6 text-sm text-stone">Final price depends on fabric, embroidery and number of outfits. Quoted in writing after your consult.</p>
        </div>
      </section>

      <section className="bg-ivory-deep py-24">
        <div className="mx-auto max-w-7xl px-4 sm:px-8">
          <Reveal>
            <SectionTitle eyebrow="From the wedding floor" title={<>Looks for every <em>ceremony</em></>} />
          </Reveal>
          <div className="mt-12 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
            {weddingLooks.map((l, i) => {
              const f = fabricById(l.fabricId);
              return (
                <Reveal key={l.code} delay={i * 90}>
                  <a href={whatsappLink(`Hi Tezoro, I'd like something like ${l.title} (${l.code}) for my wedding.`)} target="_blank" rel="noopener" className="group block">
                    <div className="relative aspect-[3/4] overflow-hidden">
                      <div className="absolute inset-0 transition-transform duration-[1.4s] group-hover:scale-105">
                        <FabricArt pattern={f.pattern} base={f.base} accent={f.accent} scale={1.2} />
                      </div>
                    </div>
                    <p className="eyebrow mt-4 text-stone">{l.occasion}</p>
                    <h3 className="display mt-1 text-2xl text-maroon">{l.title}</h3>
                  </a>
                </Reveal>
              );
            })}
          </div>
        </div>
      </section>

      <section className="grain bg-maroon-deep text-ivory">
        <div className="relative z-[2] mx-auto grid max-w-7xl gap-10 px-4 py-24 sm:px-8 lg:grid-cols-2 lg:items-center">
          <Reveal>
            <h2 className="display text-4xl sm:text-6xl">
              We come to you, <em className="text-champagne">too.</em>
            </h2>
            <p className="mt-6 max-w-lg text-ivory/70">
              For family and groomsmen orders, we hold a measurement day at your home, so the whole party is measured in one afternoon.
            </p>
          </Reveal>
          <Reveal delay={120} className="flex flex-col gap-3 sm:flex-row lg:justify-end">
            <Link href="/book?purpose=wedding" className="btn btn-gold">
              Book a wedding consult
            </Link>
            <a href={whatsappLink("Hi Tezoro, I'd like to ask about a home measurement day for my wedding.")} target="_blank" rel="noopener" className="btn btn-ghost-light">
              Ask on WhatsApp
            </a>
          </Reveal>
        </div>
      </section>
    </>
  );
}
