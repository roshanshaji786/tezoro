"use client";
import Link from "next/link";
import { useState } from "react";
import { FabricArt } from "@/components/FabricArt";
import { fabricById, looks, type Look } from "@/lib/content";
import { whatsappLink } from "@/lib/site";

const filters = ["All", "Wedding", "Suits", "Shirts", "Ethnic"] as const;

export function LookGrid() {
  const [filter, setFilter] = useState<(typeof filters)[number]>("All");
  const shown = filter === "All" ? looks : looks.filter((l) => l.category === filter);

  return (
    <>
      <div className="no-scrollbar -mx-4 flex gap-2 overflow-x-auto px-4 sm:mx-0 sm:px-0" role="tablist" aria-label="Filter looks">
        {filters.map((f) => (
          <button
            key={f}
            role="tab"
            aria-selected={filter === f}
            onClick={() => setFilter(f)}
            className={`eyebrow shrink-0 border px-4 py-3 transition-colors ${
              filter === f ? "border-navy bg-navy text-ivory" : "border-navy/20 text-navy hover:border-navy"
            }`}
          >
            {f}
          </button>
        ))}
      </div>
      <div className="mt-10 grid gap-x-6 gap-y-14 sm:grid-cols-2 lg:grid-cols-3">
        {shown.map((l) => (
          <LookCard key={l.code} look={l} />
        ))}
      </div>
    </>
  );
}

function LookCard({ look }: { look: Look }) {
  const f = fabricById(look.fabricId);
  return (
    <article id={look.code} className="group scroll-mt-28">
      <div className="relative aspect-[3/4] overflow-hidden">
        <div className="absolute inset-0 transition-transform duration-[1.6s] ease-[var(--ease-silk)] group-hover:scale-105">
          <FabricArt pattern={f.pattern} base={f.base} accent={f.accent} scale={1.3} />
        </div>
        <div className="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent opacity-0 transition-opacity duration-500 group-hover:opacity-100" />
        <span className="eyebrow absolute top-4 left-4 bg-ivory/90 px-2 py-1 text-[0.6rem] text-navy">{look.code}</span>
        <span className="eyebrow absolute top-4 right-4 text-[0.6rem] text-ivory/90">{look.category}</span>
      </div>
      <p className="eyebrow mt-5 text-stone">{look.occasion}</p>
      <h2 className="display mt-1 text-3xl text-navy">{look.title}</h2>
      <p className="mt-2 text-sm leading-relaxed text-ink/70">{look.note}</p>
      <p className="mt-2 text-xs text-stone">Cloth: {f.name}</p>
      <div className="mt-5 flex flex-wrap gap-x-6 gap-y-2">
        <a
          href={whatsappLink(`Hi Tezoro, I'd like something made in the spirit of ${look.title} (${look.code}).`)}
          target="_blank"
          rel="noopener"
          className="eyebrow text-navy hover:text-champagne"
        >
          Have one made →
        </a>
        <Link href={`/book?look=${look.code}`} className="eyebrow text-stone hover:text-navy">
          Book with this look
        </Link>
      </div>
    </article>
  );
}
