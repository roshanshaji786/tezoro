import type { Metadata } from "next";
import Link from "next/link";
import { PageIntro, SectionTitle } from "@/components/PageIntro";
import { FabricArt } from "@/components/FabricArt";
import { Reveal } from "@/components/Reveal";
import { services } from "@/lib/content";

export const metadata: Metadata = {
  title: "Bespoke suits, shirts and trousers",
  description: "Bespoke suits, shirts, trousers and ethnic wear in Thiruvananthapuram, drafted and cut by hand for one man.",
};

const details = [
  { title: "Hand-drafted pattern", text: "Your paper pattern is drawn from scratch and kept on file. It improves with every order." },
  { title: "Half-canvas construction", text: "A floating canvas chest that moulds to you over time. Fused only where it should be." },
  { title: "Made for Kerala", text: "Lighter linings, breathable cloth and open weaves, because 32°C is a normal day here." },
  { title: "Your details", text: "Lapel width, pocket style, lining colour, monogram, working cuffs. Every choice is yours." },
];

const options = [
  { group: "Lapel", items: ["Notch", "Peak", "Shawl", "Mandarin"] },
  { group: "Fit", items: ["Classic", "Tailored", "Slim"] },
  { group: "Vents", items: ["Single", "Double", "None"] },
  { group: "Collar (shirts)", items: ["Spread", "Cutaway", "Button-down", "Band"] },
];

export default function Bespoke() {
  return (
    <>
      <PageIntro eyebrow="Bespoke" title={<>Cut for your shoulders, <em>nobody else&apos;s</em></>}>
        Every suit, shirt and trouser begins as a blank sheet of pattern paper and your measurements. No blocks, no sizes, no copies.
      </PageIntro>

      <section className="mx-auto max-w-7xl px-4 pb-24 sm:px-8">
        <div className="grid gap-px bg-navy/10 md:grid-cols-2">
          {services.map((s, i) => (
            <Reveal key={s.title} delay={(i % 2) * 120} className="grid bg-ivory sm:grid-cols-[0.9fr_1.1fr]">
              <div className="relative aspect-square sm:aspect-auto">
                <FabricArt pattern={s.pattern} base={s.base} accent={s.accent} scale={1.3} className="absolute inset-0" />
              </div>
              <div className="flex flex-col p-8">
                <h2 className="display text-4xl text-navy">{s.title}</h2>
                <p className="eyebrow mt-2 text-gold">From {s.from}</p>
                <p className="mt-4 flex-1 text-ink/70">{s.text}</p>
                <Link href={`/book?purpose=${s.title === "Shirts" ? "shirts" : s.title === "Ethnic" ? "ethnic" : "suit"}`} className="eyebrow mt-6 inline-block py-3 text-navy hover:text-champagne">
                  Book a consult →
                </Link>
              </div>
            </Reveal>
          ))}
        </div>
      </section>

      <section className="grain bg-navy text-ivory">
        <div className="relative z-[2] mx-auto max-w-7xl px-4 py-24 sm:px-8">
          <Reveal>
            <SectionTitle eyebrow="The craft" title={<>What you cannot see <em className="text-champagne">is what you feel</em></>} light />
          </Reveal>
          <div className="mt-14 grid gap-10 sm:grid-cols-2 lg:grid-cols-4">
            {details.map((d, i) => (
              <Reveal key={d.title} delay={i * 90} className="border-t border-champagne/30 pt-6">
                <h3 className="display text-2xl text-champagne">{d.title}</h3>
                <p className="mt-3 text-sm leading-relaxed text-ivory/70">{d.text}</p>
              </Reveal>
            ))}
          </div>
        </div>
      </section>

      <section className="mx-auto max-w-7xl px-4 py-24 sm:px-8">
        <Reveal>
          <SectionTitle eyebrow="Your choices" title="A few of the decisions we make together" />
        </Reveal>
        <div className="mt-12 grid gap-8 sm:grid-cols-2 lg:grid-cols-4">
          {options.map((o) => (
            <Reveal key={o.group}>
              <p className="eyebrow text-stone">{o.group}</p>
              <ul className="mt-4 flex flex-wrap gap-2">
                {o.items.map((it) => (
                  <li key={it} className="border border-navy/20 px-3 py-1.5 text-sm text-navy">
                    {it}
                  </li>
                ))}
              </ul>
            </Reveal>
          ))}
        </div>
        <div className="mt-16 flex flex-col gap-3 sm:flex-row">
          <Link href="/book?purpose=suit" className="btn btn-navy">
            Book a fitting
          </Link>
          <Link href="/fabrics" className="btn btn-ghost-dark">
            Explore fabrics in 3D
          </Link>
        </div>
      </section>
    </>
  );
}
