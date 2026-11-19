"use client";
import Link from "next/link";
import { useSearchParams } from "next/navigation";
import { useMemo, useState } from "react";
import { fabrics, looks, purposes, slots } from "@/lib/content";
import { whatsappLink } from "@/lib/site";

type Purpose = (typeof purposes)[number]["id"];

const iso = (d: Date) => `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`;

function nextDays(n: number) {
  const out: Date[] = [];
  const d = new Date();
  d.setHours(0, 0, 0, 0);
  while (out.length < n) {
    d.setDate(d.getDate() + 1);
    if (d.getDay() !== 0) out.push(new Date(d)); // Sundays are by appointment over WhatsApp
  }
  return out;
}

export function BookingForm() {
  const params = useSearchParams();
  const initialPurpose = (purposes.find((p) => p.id === params.get("purpose"))?.id ?? "") as Purpose | "";
  const look = looks.find((l) => l.code === params.get("look"));
  const fabric = fabrics.find((f) => f.id === params.get("fabric"));
  const pkg = params.get("package");

  const [step, setStep] = useState(initialPurpose ? 1 : 0);
  const [purpose, setPurpose] = useState<Purpose | "">(initialPurpose);
  const [date, setDate] = useState("");
  const [slot, setSlot] = useState("");
  const [form, setForm] = useState({
    name: "",
    phone: "",
    email: "",
    weddingDate: params.get("wedding") ?? "",
    notes: pkg ? `Interested in the ${pkg} package.` : "",
    company: "",
  });
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");
  const [done, setDone] = useState<{ ref: string } | null>(null);

  const days = useMemo(() => nextDays(18), []);
  const purposeLabel = purposes.find((p) => p.id === purpose)?.label ?? "";
  const dateLabel = date ? new Date(date + "T00:00:00").toLocaleDateString("en-IN", { weekday: "long", day: "numeric", month: "long" }) : "";

  const set = (k: keyof typeof form) => (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => setForm((f) => ({ ...f, [k]: e.target.value }));

  async function submit(e: React.FormEvent) {
    e.preventDefault();
    setBusy(true);
    setError("");
    try {
      const res = await fetch("/api/bookings", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({ purpose, date, slot, ...form, look: look?.code, fabric: fabric?.id }),
      });
      const json = await res.json();
      if (!json.ok) throw new Error(json.error || "Something went wrong");
      setDone({ ref: json.ref });
      setStep(3);
      window.scrollTo({ top: 0, behavior: "smooth" });
    } catch (err) {
      setError(err instanceof Error ? err.message : "Something went wrong. Please try WhatsApp instead.");
    } finally {
      setBusy(false);
    }
  }

  const confirmMessage = done
    ? [
        `Hi Tezoro, I've booked a fitting.`,
        `Ref: ${done.ref}`,
        `For: ${purposeLabel}`,
        `When: ${dateLabel}, ${slot}`,
        `Name: ${form.name}`,
        form.weddingDate ? `Wedding date: ${form.weddingDate}` : "",
        look ? `Look: ${look.title} (${look.code})` : "",
        fabric ? `Fabric: ${fabric.name}` : "",
        form.notes ? `Notes: ${form.notes}` : "",
      ]
        .filter(Boolean)
        .join("\n")
    : "";

  const steps = ["Purpose", "Date & time", "Your details"];

  return (
    <div className="mx-auto max-w-3xl">
      {step < 3 && (
        <ol className="mb-12 flex gap-2" aria-label="Booking steps">
          {steps.map((s, i) => (
            <li key={s} className="flex-1">
              <button
                type="button"
                disabled={i > step}
                onClick={() => setStep(i)}
                className={`w-full border-t-2 pt-3 text-left transition-colors ${i <= step ? "border-champagne" : "border-navy/15"}`}
              >
                <span className="eyebrow text-[0.6rem] text-stone">0{i + 1}</span>
                <span className={`block text-sm ${i === step ? "text-navy" : "text-ink/50"}`}>{s}</span>
              </button>
            </li>
          ))}
        </ol>
      )}

      {(look || fabric || pkg) && step < 3 && (
        <p className="mb-8 border-l-2 border-champagne bg-white/60 px-4 py-3 text-sm text-ink/80">
          {look && <>Bringing look <strong className="text-navy">{look.title}</strong> to your fitting. </>}
          {fabric && <>We will have <strong className="text-navy">{fabric.name}</strong> ready on the table. </>}
          {pkg && <>Package: <strong className="text-navy">{pkg}</strong>.</>}
        </p>
      )}

      {step === 0 && (
        <fieldset>
          <legend className="display text-4xl text-navy">What brings you in?</legend>
          <div className="mt-8 grid gap-3 sm:grid-cols-2">
            {purposes.map((p) => (
              <button
                type="button"
                key={p.id}
                onClick={() => {
                  setPurpose(p.id);
                  setStep(1);
                }}
                className={`group border p-6 text-left transition-all duration-300 hover:border-navy ${purpose === p.id ? "border-navy bg-navy text-ivory" : "border-navy/20 bg-white/50"}`}
              >
                <span className="display block text-3xl">{p.label}</span>
                <span className={`mt-1 block text-sm ${purpose === p.id ? "text-ivory/70" : "text-stone"}`}>{p.hint}</span>
              </button>
            ))}
          </div>
        </fieldset>
      )}

      {step === 1 && (
        <fieldset>
          <legend className="display text-4xl text-navy">Pick a day</legend>
          <div className="no-scrollbar -mx-4 mt-8 flex gap-2 overflow-x-auto px-4 pb-2 sm:mx-0 sm:grid sm:grid-cols-6 sm:px-0">
            {days.map((d) => {
              const v = iso(d);
              const on = v === date;
              return (
                <button
                  type="button"
                  key={v}
                  onClick={() => setDate(v)}
                  className={`flex min-w-[72px] shrink-0 flex-col items-center border py-3 transition-colors ${on ? "border-navy bg-navy text-ivory" : "border-navy/15 bg-white/50 text-navy hover:border-navy"}`}
                >
                  <span className="eyebrow text-[0.55rem] opacity-70">{d.toLocaleDateString("en-IN", { weekday: "short" })}</span>
                  <span className="display text-3xl">{d.getDate()}</span>
                  <span className="text-[0.65rem] opacity-70">{d.toLocaleDateString("en-IN", { month: "short" })}</span>
                </button>
              );
            })}
          </div>
          <p className="mt-3 text-xs text-stone">Sundays are by appointment. Ask us on WhatsApp.</p>

          <div className={`transition-opacity duration-500 ${date ? "opacity-100" : "pointer-events-none opacity-30"}`}>
            <p className="display mt-10 text-3xl text-navy">And a time</p>
            <div className="mt-5 grid grid-cols-3 gap-2 sm:grid-cols-7">
              {slots.map((s) => (
                <button
                  type="button"
                  key={s}
                  onClick={() => setSlot(s)}
                  className={`border py-3 text-sm transition-colors ${slot === s ? "border-navy bg-navy text-ivory" : "border-navy/15 bg-white/50 text-navy hover:border-navy"}`}
                >
                  {s}
                </button>
              ))}
            </div>
          </div>
          <button type="button" disabled={!date || !slot} onClick={() => setStep(2)} className="btn btn-navy mt-10 w-full disabled:opacity-40 sm:w-auto">
            Continue
          </button>
        </fieldset>
      )}

      {step === 2 && (
        <form onSubmit={submit} noValidate={false}>
          <h2 className="display text-4xl text-navy">Almost there</h2>
          <p className="mt-2 text-stone">
            {purposeLabel} · {dateLabel} · {slot}
          </p>
          <div className="mt-8 grid gap-5 sm:grid-cols-2">
            <label className="block">
              <span className="eyebrow text-[0.6rem] text-stone">Your name</span>
              <input required minLength={2} autoComplete="name" value={form.name} onChange={set("name")} className="field mt-2" />
            </label>
            <label className="block">
              <span className="eyebrow text-[0.6rem] text-stone">Mobile / WhatsApp</span>
              <input required type="tel" inputMode="tel" autoComplete="tel" pattern="[+0-9 ]{10,16}" placeholder="+91" value={form.phone} onChange={set("phone")} className="field mt-2" />
            </label>
            <label className="block">
              <span className="eyebrow text-[0.6rem] text-stone">Email (optional)</span>
              <input type="email" autoComplete="email" value={form.email} onChange={set("email")} className="field mt-2" />
            </label>
            {purpose === "wedding" && (
              <label className="block">
                <span className="eyebrow text-[0.6rem] text-stone">Wedding date</span>
                <input type="date" value={form.weddingDate} onChange={set("weddingDate")} className="field mt-2" />
              </label>
            )}
            <label className="block sm:col-span-2">
              <span className="eyebrow text-[0.6rem] text-stone">Anything we should know? (optional)</span>
              <textarea rows={3} value={form.notes} onChange={set("notes")} className="field mt-2" placeholder="Occasion, colours you love, how many outfits..." />
            </label>
            <input type="text" tabIndex={-1} autoComplete="off" value={form.company} onChange={set("company")} className="hidden" aria-hidden="true" />
          </div>
          {error && <p className="mt-6 text-sm text-maroon">{error}</p>}
          <button type="submit" disabled={busy} className="btn btn-navy mt-10 w-full disabled:opacity-60 sm:w-auto">
            {busy ? "Booking…" : "Confirm my fitting"}
          </button>
        </form>
      )}

      {step === 3 && done && (
        <div className="text-center">
          <p className="eyebrow text-gold">Booked</p>
          <h2 className="display mt-4 text-5xl text-navy sm:text-6xl">
            See you on <em>{dateLabel.split(",")[0]}</em>
          </h2>
          <p className="mt-4 text-ink/70">
            {dateLabel} at {slot}. Your reference is <strong className="text-navy">{done.ref}</strong>.
          </p>
          <p className="mx-auto mt-6 max-w-md text-sm text-stone">
            Send it to us on WhatsApp so we can confirm and remind you the day before.
          </p>
          <div className="mt-10 flex flex-col justify-center gap-3 sm:flex-row">
            <a href={whatsappLink(confirmMessage)} target="_blank" rel="noopener" className="btn bg-[#1f8f4e] text-white hover:bg-[#1a7a43]">
              Confirm on WhatsApp
            </a>
            <Link href="/fabrics" className="btn btn-ghost-dark">
              Browse fabrics meanwhile
            </Link>
          </div>
        </div>
      )}
    </div>
  );
}
