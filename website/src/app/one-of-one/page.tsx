import type { Metadata } from "next";
import Link from "next/link";
import { Reveal } from "@/components/Reveal";
import { getRegister } from "@/lib/data";

export const metadata: Metadata = {
  title: "The One of One register",
  description: "Every Tezoro garment is numbered and recorded. A public register of pieces we have made, each one only once.",
};

export const revalidate = 300;

export default async function OneOfOne() {
  const { entries } = await getRegister();
  const latest = entries[0]?.no ?? 0;

  return (
    <div className="grain bg-navy-deep text-ivory">
      <section className="relative z-[2] mx-auto max-w-7xl px-4 pt-36 pb-16 sm:px-8 sm:pt-44">
        <p className="eyebrow text-champagne">The One of One register</p>
        <h1 className="display mt-5 max-w-4xl text-5xl sm:text-8xl">
          Made once. <em className="text-champagne">Recorded forever.</em>
        </h1>
        <p className="mt-6 max-w-2xl text-lg text-ivory/65">
          Each finished Tezoro garment gets a number, sewn into a label inside and written here. If you ever see two the same, the second one is not ours.
        </p>
        <div className="mt-14 grid max-w-3xl grid-cols-3 gap-6 border-y border-champagne/20 py-8">
          <div>
            <p className="display text-5xl text-champagne sm:text-6xl">{String(latest).padStart(4, "0")}</p>
            <p className="eyebrow mt-2 text-[0.6rem] text-ivory/50">Latest number</p>
          </div>
          <div>
            <p className="display text-5xl text-champagne sm:text-6xl">0</p>
            <p className="eyebrow mt-2 text-[0.6rem] text-ivory/50">Duplicates</p>
          </div>
          <div>
            <p className="display text-5xl text-champagne sm:text-6xl">1</p>
            <p className="eyebrow mt-2 text-[0.6rem] text-ivory/50">Of each</p>
          </div>
        </div>
      </section>

      <section className="relative z-[2] mx-auto max-w-7xl px-4 pb-28 sm:px-8">
        <ul className="grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
          {entries.map((e, i) => (
            <Reveal as="li" key={e.no} delay={(i % 3) * 90}>
              <div className="group relative h-full bg-ivory p-6 text-navy transition-transform duration-700 hover:-translate-y-1">
                <div className="flex h-full flex-col border border-champagne/50 p-5">
                  <div className="flex justify-between">
                    <span className="eyebrow text-[0.55rem] text-stone">{e.month}</span>
                    <span className="eyebrow text-[0.55rem] text-gold">{e.occasion}</span>
                  </div>
                  <p className="display mt-6 text-5xl">No. {String(e.no).padStart(4, "0")}</p>
                  <p className="display mt-3 text-2xl text-navy/90">{e.garment}</p>
                  {e.note && <p className="mt-3 text-sm text-stone italic">{e.note}</p>}
                </div>
              </div>
            </Reveal>
          ))}
        </ul>
        <div className="mt-16 flex flex-col gap-3 sm:flex-row">
          <Link href="/book" className="btn btn-gold">
            Start my number
          </Link>
          <Link href="/track" className="btn btn-ghost-light">
            Track my order
          </Link>
        </div>
      </section>
    </div>
  );
}
