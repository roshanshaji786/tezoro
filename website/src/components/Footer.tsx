import Link from "next/link";
import { Logo } from "./Logo";
import { nav, site, whatsappLink } from "@/lib/site";

export function Footer() {
  return (
    <footer className="grain bg-navy-deep text-ivory/70">
      <div className="relative z-[2] mx-auto max-w-7xl px-4 pt-20 pb-10 sm:px-8">
        <div className="grid gap-12 md:grid-cols-[1.4fr_1fr_1fr_1fr]">
          <div>
            <Logo light />
            <p className="display mt-6 max-w-xs text-2xl text-ivory/90 italic">{site.tagline}</p>
          </div>
          <div>
            <p className="eyebrow mb-5 text-champagne">Explore</p>
            <ul className="space-y-3 text-sm">
              {nav.map((n) => (
                <li key={n.href}>
                  <Link href={n.href} className="hover:text-champagne">
                    {n.label}
                  </Link>
                </li>
              ))}
            </ul>
          </div>
          <div>
            <p className="eyebrow mb-5 text-champagne">Atelier</p>
            <address className="space-y-1 text-sm not-italic">
              <p>{site.address.line1}</p>
              <p>{site.address.line2}</p>
            </address>
            <ul className="mt-5 space-y-1 text-sm">
              {site.hours.map((h) => (
                <li key={h.days}>
                  {h.days}: {h.time}
                </li>
              ))}
            </ul>
          </div>
          <div>
            <p className="eyebrow mb-5 text-champagne">Talk to us</p>
            <ul className="space-y-3 text-sm">
              <li>
                <a href={whatsappLink("Hi Tezoro, I'd like to know more.")} className="hover:text-champagne">
                  WhatsApp
                </a>
              </li>
              <li>
                <a href={site.phoneHref} className="hover:text-champagne">
                  {site.phone}
                </a>
              </li>
              <li>
                <a href={`mailto:${site.email}`} className="hover:text-champagne">
                  {site.email}
                </a>
              </li>
              <li>
                <a href={site.instagram} className="hover:text-champagne">
                  {site.instagramHandle}
                </a>
              </li>
              <li>
                <Link href="/track" className="hover:text-champagne">
                  Track my order
                </Link>
              </li>
            </ul>
          </div>
        </div>
        <div className="hairline mt-16 opacity-40" />
        <div className="mt-6 flex flex-col justify-between gap-2 text-xs text-ivory/40 sm:flex-row">
          <p>© {new Date().getFullYear()} Tezoro Atelier. Every piece, one of one.</p>
          <p>
            Crafted by <a href="https://info.dartsai.in" className="hover:text-champagne">DARTS AI</a>
          </p>
        </div>
      </div>
    </footer>
  );
}
