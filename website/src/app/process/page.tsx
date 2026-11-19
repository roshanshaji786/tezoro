import type { Metadata } from "next";
import Link from "next/link";
import { PageIntro } from "@/components/PageIntro";
import { Reveal } from "@/components/Reveal";
import { processSteps } from "@/lib/content";

export const metadata: Metadata = {
  title: "How it works",
  description: "How a Tezoro bespoke garment is made: consult, fabric, measurements, two fittings and collection. About three weeks from first visit.",
};

const faqs = [
  { q: "How long does a suit take?", a: "About three weeks from your first visit, with two fittings in between. Wedding orders are planned backwards from your date." },
  { q: "Do I pay everything up front?", a: "No. A part payment confirms the order and reserves the cloth. The balance is due at collection." },
  { q: "Can I bring my own fabric?", a: "Yes. Bring it to the consult and we will tell you honestly how it will wear and drape." },
  { q: "I live abroad. Can I still order?", a: "Visit once to be measured and fitted. After that your pattern is kept, and shirts and trousers can be reordered on WhatsApp and couriered to you." },
  { q: "What if it does not fit perfectly?", a: "Alterations on your Tezoro piece are free for the first three months. Bodies change. We adjust." },
  { q: "Do you do alterations on clothes from elsewhere?", a: "Yes, for suits, shirts, trousers and sherwanis. Book an alteration slot and bring the piece." },
];

export default function Process() {
  return (
    <>
      <PageIntro eyebrow="How it works" title={<>Six steps, <em>about three weeks</em></>}>
        Unhurried by design. Every step is a chance to make it more yours.
      </PageIntro>

      <section className="mx-auto max-w-5xl px-4 pb-24 sm:px-8">
        <ol className="relative">
          <span className="absolute top-3 bottom-3 left-6 w-px bg-champagne/40 sm:left-1/2" aria-hidden="true" />
          {processSteps.map((s, i) => (
            <Reveal as="li" key={s.n} className={`relative grid gap-4 pb-16 pl-16 sm:grid-cols-2 sm:gap-16 sm:pl-0 ${i % 2 ? "sm:[&>div:first-child]:order-2" : ""}`}>
              <div className={`${i % 2 ? "sm:pl-12" : "sm:pr-12 sm:text-right"}`}>
                <p className="eyebrow text-stone">{s.days}</p>
                <h2 className="display mt-2 text-4xl text-navy sm:text-5xl">{s.title}</h2>
              </div>
              <div className={`${i % 2 ? "sm:pr-12 sm:text-right" : "sm:pl-12"}`}>
                <p className="leading-relaxed text-ink/70 sm:pt-7">{s.text}</p>
              </div>
              <span className="display absolute top-0 left-0 flex h-12 w-12 items-center justify-center rounded-full border border-champagne bg-ivory text-lg text-gold sm:left-1/2 sm:-translate-x-1/2">
                {s.n}
              </span>
            </Reveal>
          ))}
        </ol>
      </section>

      <section className="bg-ivory-deep">
        <div className="mx-auto max-w-4xl px-4 py-24 sm:px-8">
          <p className="eyebrow text-gold">Questions</p>
          <h2 className="display mt-4 text-4xl text-navy sm:text-6xl">Asked often</h2>
          <div className="mt-10 divide-y divide-navy/10 border-y border-navy/10">
            {faqs.map((f) => (
              <details key={f.q} className="group py-6">
                <summary className="flex cursor-pointer list-none items-center justify-between gap-6 text-lg text-navy">
                  {f.q}
                  <span className="text-2xl text-champagne transition-transform duration-300 group-open:rotate-45">+</span>
                </summary>
                <p className="mt-4 max-w-2xl leading-relaxed text-ink/70">{f.a}</p>
              </details>
            ))}
          </div>
          <Link href="/book" className="btn btn-navy mt-12">
            Book your consult
          </Link>
        </div>
      </section>
    </>
  );
}
