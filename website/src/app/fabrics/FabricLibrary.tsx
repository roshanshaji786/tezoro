"use client";
import Link from "next/link";
import { useState } from "react";
import { FabricViewer } from "@/components/three";
import { FabricArt } from "@/components/FabricArt";
import { fabrics } from "@/lib/content";

export function FabricLibrary() {
  const [active, setActive] = useState(fabrics[0]);

  return (
    <div className="grid gap-10 lg:grid-cols-[1.1fr_0.9fr]">
      <div className="lg:sticky lg:top-24 lg:self-start">
        <div className="relative aspect-[4/5] w-full overflow-hidden bg-[radial-gradient(ellipse_at_50%_35%,#24345a_0%,#0b1426_75%)] sm:aspect-[5/5]">
          <FabricViewer fabric={active} />
          <p className="eyebrow pointer-events-none absolute bottom-4 left-4 text-[0.6rem] text-ivory/50">Drag to turn the cloth</p>
        </div>
        <div className="mt-6 text-ivory">
          <p className="eyebrow text-champagne">{active.origin}</p>
          <h2 className="display mt-2 text-4xl sm:text-5xl">{active.name}</h2>
          <dl className="mt-6 grid grid-cols-2 gap-x-6 gap-y-4 text-sm">
            <div>
              <dt className="eyebrow text-[0.6rem] text-ivory/50">Weight</dt>
              <dd className="mt-1 text-ivory/85">{active.weight}</dd>
            </div>
            <div>
              <dt className="eyebrow text-[0.6rem] text-ivory/50">Feel</dt>
              <dd className="mt-1 text-ivory/85">{active.feel}</dd>
            </div>
            <div>
              <dt className="eyebrow text-[0.6rem] text-ivory/50">Wear it for</dt>
              <dd className="mt-1 text-ivory/85">{active.season}</dd>
            </div>
            <div>
              <dt className="eyebrow text-[0.6rem] text-ivory/50">Best for</dt>
              <dd className="mt-1 text-ivory/85">{active.bestFor.join(", ")}</dd>
            </div>
          </dl>
          <Link href={`/book?fabric=${active.id}`} className="btn btn-gold mt-8 w-full sm:w-auto">
            Show me this at my fitting
          </Link>
        </div>
      </div>

      <ul className="grid grid-cols-2 gap-4 sm:gap-5" aria-label="Fabrics">
        {fabrics.map((f) => {
          const on = f.id === active.id;
          return (
            <li key={f.id}>
              <button
                onClick={() => setActive(f)}
                aria-pressed={on}
                className={`group block w-full text-left transition-all duration-500 ${on ? "" : "opacity-75 hover:opacity-100"}`}
              >
                <div className={`relative aspect-square overflow-hidden outline-offset-4 ${on ? "outline outline-1 outline-champagne" : ""}`}>
                  <FabricArt pattern={f.pattern} base={f.base} accent={f.accent} scale={0.9} />
                </div>
                <p className="display mt-3 text-xl text-ivory">{f.name}</p>
                <p className="text-xs text-ivory/50">{f.origin}</p>
              </button>
            </li>
          );
        })}
      </ul>
    </div>
  );
}
