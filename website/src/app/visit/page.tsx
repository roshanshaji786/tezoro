import type { Metadata } from "next";
import Link from "next/link";
import { PageIntro } from "@/components/PageIntro";
import { site, whatsappLink } from "@/lib/site";

export const metadata: Metadata = {
  title: "Visit the atelier",
  description: "Tezoro Atelier, near Zudio, Pothencode, Thiruvananthapuram. Open Monday to Saturday, 10 am to 9 pm. Sundays by appointment.",
};

export default function Visit() {
  const directions = `https://www.google.com/maps/dir/?api=1&destination=${encodeURIComponent(site.address.mapQuery)}`;
  return (
    <>
      <PageIntro eyebrow="Visit" title={<>Find us in <em>Pothencode</em></>}>
        Walk in any time we are open. Book ahead and your fabrics, tea and tailor will be waiting.
      </PageIntro>
      <section className="mx-auto grid max-w-7xl gap-12 px-4 pb-28 sm:px-8 lg:grid-cols-[0.8fr_1.2fr]">
        <div className="space-y-10">
          <div>
            <p className="eyebrow text-stone">Address</p>
            <p className="display mt-3 text-3xl text-navy">{site.address.line1}</p>
            <p className="text-ink/70">{site.address.line2}</p>
            <a href={directions} target="_blank" rel="noopener" className="eyebrow mt-4 inline-block text-navy hover:text-champagne">
              Get directions →
            </a>
          </div>
          <div>
            <p className="eyebrow text-stone">Hours</p>
            <ul className="mt-3 space-y-2">
              {site.hours.map((h) => (
                <li key={h.days} className="flex justify-between gap-6 border-b border-navy/10 pb-2 text-ink/80">
                  <span>{h.days}</span>
                  <span className="text-navy">{h.time}</span>
                </li>
              ))}
            </ul>
          </div>
          <div>
            <p className="eyebrow text-stone">Talk to us</p>
            <div className="mt-4 flex flex-col gap-3">
              <a href={whatsappLink("Hi Tezoro, I'd like to visit the atelier.")} target="_blank" rel="noopener" className="btn btn-navy">
                WhatsApp us
              </a>
              <a href={site.phoneHref} className="btn btn-ghost-dark">
                Call {site.phone}
              </a>
              <Link href="/book" className="btn btn-ghost-dark">
                Book a fitting
              </Link>
            </div>
          </div>
        </div>
        <div className="min-h-[420px] overflow-hidden bg-navy/10">
          <iframe
            title="Map to Tezoro Atelier"
            className="h-full min-h-[420px] w-full grayscale-[60%]"
            loading="lazy"
            src={`https://maps.google.com/maps?q=${encodeURIComponent(site.address.mapQuery)}&z=16&output=embed`}
          />
        </div>
      </section>
    </>
  );
}
