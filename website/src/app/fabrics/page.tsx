import type { Metadata } from "next";
import { FabricLibrary } from "./FabricLibrary";

export const metadata: Metadata = {
  title: "Fabric library",
  description: "Explore Tezoro's cloth in 3D: Italian wool, Irish linen, Banarasi brocade, tussar silk and velvet, with notes on weight and season.",
};

export default function Fabrics() {
  return (
    <div className="grain bg-navy-deep">
      <section className="relative z-[2] mx-auto max-w-7xl px-4 pt-36 pb-28 sm:px-8 sm:pt-44">
        <p className="eyebrow text-champagne">The fabric library</p>
        <h1 className="display mt-5 max-w-3xl text-5xl text-ivory sm:text-7xl">
          Feel it with your eyes. <em className="text-champagne">Then with your hands.</em>
        </h1>
        <p className="mt-6 max-w-2xl text-lg text-ivory/65">
          Turn each cloth in 3D, read how it wears in Kerala weather, and add it to your fitting. The real swatch will be waiting on the table.
        </p>
        <div className="mt-16">
          <FabricLibrary />
        </div>
      </section>
    </div>
  );
}
