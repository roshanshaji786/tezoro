import type { Metadata } from "next";
import { redirect } from "next/navigation";
import { normaliseCode } from "@/lib/data";

export const metadata: Metadata = {
  title: "Track my order",
  description: "Follow your Tezoro garment from fabric cut to collection.",
};

async function go(formData: FormData) {
  "use server";
  const code = normaliseCode(String(formData.get("code") ?? ""));
  redirect(`/track/${encodeURIComponent(code || "none")}`);
}

export default function Track() {
  return (
    <section className="grain min-h-[85vh] bg-navy-deep px-4 pt-36 pb-24 text-ivory sm:px-8 sm:pt-44">
      <div className="relative z-[2] mx-auto max-w-2xl">
        <p className="eyebrow text-champagne">Order tracker</p>
        <h1 className="display mt-5 text-5xl sm:text-7xl">
          Where is <em className="text-champagne">my piece?</em>
        </h1>
        <p className="mt-6 text-ivory/65">Enter the order code on your receipt. It looks like TZ-0147.</p>
        <form action={go} className="mt-10 flex flex-col gap-3 sm:flex-row">
          <label htmlFor="code" className="sr-only">
            Order code
          </label>
          <input
            id="code"
            name="code"
            required
            placeholder="TZ-0147"
            autoCapitalize="characters"
            className="min-h-14 flex-1 border border-champagne/40 bg-transparent px-5 text-xl tracking-[0.2em] text-ivory uppercase placeholder:text-ivory/30 focus:border-champagne focus:outline-none"
          />
          <button className="btn btn-gold min-h-14">Track</button>
        </form>
        <p className="mt-6 text-sm text-ivory/40">Try the sample code TZ-0147 to see how it works.</p>
      </div>
    </section>
  );
}
