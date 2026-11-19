import type { Metadata } from "next";
import Link from "next/link";
import { LogoMark } from "@/components/Logo";
import { adminConfigured, isAdmin } from "@/lib/auth";
import { db, type Booking, type Order } from "@/lib/db";
import { orderStages, purposes, fabrics } from "@/lib/content";
import { whatsappLink } from "@/lib/site";
import { LoginForm } from "./LoginForm";
import { createOrder, issueNumber, logout, setBookingStatus, setOrderNote, setOrderStage } from "./actions";

export const metadata: Metadata = { title: "Atelier desk", robots: { index: false, follow: false } };
export const dynamic = "force-dynamic";

function Shell({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen bg-ivory">
      <div className="bg-navy text-ivory">
        <div className="mx-auto flex max-w-6xl items-center justify-between px-4 py-4 sm:px-8">
          <Link href="/admin" className="flex items-center gap-3">
            <LogoMark className="h-8 w-8" color="#D4B483" />
            <span className="eyebrow text-champagne">Atelier desk</span>
          </Link>
          <Link href="/" className="text-xs text-ivory/60 hover:text-champagne">
            View site →
          </Link>
        </div>
      </div>
      <div className="mx-auto max-w-6xl px-4 py-10 sm:px-8">{children}</div>
    </div>
  );
}

const waNumber = (p: string) => {
  const d = p.replace(/\D/g, "");
  return d.length === 10 ? "91" + d : d;
};

export default async function Admin({ searchParams }: { searchParams: Promise<{ tab?: string }> }) {
  if (!adminConfigured()) {
    return (
      <Shell>
        <h1 className="display text-4xl text-navy">Almost ready</h1>
        <p className="mt-4 max-w-xl text-ink/70">
          Set <code className="bg-white px-1">ADMIN_PASSWORD</code>, <code className="bg-white px-1">SUPABASE_URL</code> and{" "}
          <code className="bg-white px-1">SUPABASE_SERVICE_ROLE_KEY</code> in the hosting settings to switch on the staff desk.
        </p>
      </Shell>
    );
  }

  if (!(await isAdmin())) {
    return (
      <Shell>
        <div className="mx-auto max-w-sm pt-10">
          <h1 className="display text-4xl text-navy">Staff sign in</h1>
          <LoginForm />
        </div>
      </Shell>
    );
  }

  const c = db();
  const { tab = "bookings" } = await searchParams;

  if (!c) {
    return (
      <Shell>
        <h1 className="display text-4xl text-navy">Database not connected</h1>
        <p className="mt-4 text-ink/70">Add the Supabase keys in the hosting settings, then run supabase/schema.sql once.</p>
        <form action={logout} className="mt-8">
          <button className="btn btn-ghost-dark">Sign out</button>
        </form>
      </Shell>
    );
  }

  const today = new Date().toISOString().slice(0, 10);
  const [{ data: bookings }, { data: orders }] = await Promise.all([
    c.from("bookings").select("*").gte("preferred_date", new Date(Date.now() - 7 * 86_400_000).toISOString().slice(0, 10)).order("preferred_date").order("slot").limit(200),
    c.from("orders").select("*").order("updated_at", { ascending: false }).limit(200),
  ]);
  const b = (bookings ?? []) as Booking[];
  const o = (orders ?? []) as Order[];
  const todays = b.filter((x) => x.preferred_date === today && x.status !== "cancelled");
  const newCount = b.filter((x) => x.status === "new").length;
  const open = o.filter((x) => x.stage < 4).length;

  return (
    <Shell>
      <div className="flex flex-wrap items-end justify-between gap-4">
        <div>
          <p className="eyebrow text-champagne">{new Date().toLocaleDateString("en-IN", { weekday: "long", day: "numeric", month: "long" })}</p>
          <h1 className="display mt-2 text-5xl text-navy">Good day.</h1>
        </div>
        <form action={logout}>
          <button className="text-sm text-stone hover:text-navy">Sign out</button>
        </form>
      </div>

      <div className="mt-8 grid grid-cols-3 gap-3">
        {[
          { n: todays.length, l: "Fittings today" },
          { n: newCount, l: "New bookings" },
          { n: open, l: "Orders in work" },
        ].map((k) => (
          <div key={k.l} className="bg-white p-5">
            <p className="display text-4xl text-navy">{k.n}</p>
            <p className="eyebrow mt-1 text-[0.55rem] text-stone">{k.l}</p>
          </div>
        ))}
      </div>

      <nav className="mt-10 flex gap-2 border-b border-navy/10">
        {[
          ["bookings", "Bookings"],
          ["orders", "Orders"],
        ].map(([k, l]) => (
          <Link key={k} href={`/admin?tab=${k}`} className={`eyebrow -mb-px border-b-2 px-4 py-3 ${tab === k ? "border-navy text-navy" : "border-transparent text-stone"}`}>
            {l}
          </Link>
        ))}
      </nav>

      {tab === "bookings" ? (
        <section className="mt-8 space-y-3">
          {b.length === 0 && <p className="text-stone">No bookings yet. They will appear here as soon as someone books online.</p>}
          {b.map((x) => (
            <article key={x.id} className={`grid gap-4 bg-white p-5 sm:grid-cols-[1fr_auto] ${x.status === "cancelled" ? "opacity-50" : ""}`}>
              <div>
                <div className="flex flex-wrap items-center gap-3">
                  <span className="display text-2xl text-navy">{x.name}</span>
                  <span className={`eyebrow px-2 py-0.5 text-[0.55rem] ${x.status === "new" ? "bg-champagne text-navy" : "bg-navy/5 text-stone"}`}>{x.status}</span>
                  {x.preferred_date === today && <span className="eyebrow text-[0.55rem] text-maroon">Today</span>}
                </div>
                <p className="mt-1 text-sm text-ink/70">
                  {purposes.find((p) => p.id === x.purpose)?.label ?? x.purpose} ·{" "}
                  {new Date(x.preferred_date + "T00:00:00").toLocaleDateString("en-IN", { weekday: "short", day: "numeric", month: "short" })} · {x.slot}
                </p>
                <p className="mt-1 text-xs text-stone">
                  {x.ref}
                  {x.wedding_date && ` · Wedding ${x.wedding_date}`}
                  {x.look_code && ` · Look ${x.look_code}`}
                  {x.fabric_id && ` · ${fabrics.find((f) => f.id === x.fabric_id)?.name ?? x.fabric_id}`}
                </p>
                {x.notes && <p className="mt-2 text-sm text-ink/80 italic">“{x.notes}”</p>}
                <div className="mt-3 flex gap-4 text-sm">
                  <a href={`tel:${x.phone}`} className="text-navy underline-offset-4 hover:underline">
                    {x.phone}
                  </a>
                  <a
                    href={`https://wa.me/${waNumber(x.phone)}?text=${encodeURIComponent(`Hello ${x.name.split(" ")[0]}, this is Tezoro Atelier confirming your fitting on ${x.preferred_date} at ${x.slot}. See you then!`)}`}
                    target="_blank"
                    rel="noopener"
                    className="text-[#1f8f4e] underline-offset-4 hover:underline"
                  >
                    WhatsApp
                  </a>
                </div>
              </div>
              <div className="flex flex-wrap gap-2 sm:flex-col">
                {(["confirmed", "visited", "cancelled"] as const).map((st) => (
                  <form key={st} action={setBookingStatus}>
                    <input type="hidden" name="id" value={x.id} />
                    <input type="hidden" name="status" value={st} />
                    <button disabled={x.status === st} className="min-h-10 w-full border border-navy/15 px-3 text-xs text-navy capitalize hover:border-navy disabled:bg-navy disabled:text-ivory">
                      {st}
                    </button>
                  </form>
                ))}
              </div>
            </article>
          ))}
        </section>
      ) : (
        <section className="mt-8">
          <details className="bg-white p-5" open={o.length === 0}>
            <summary className="eyebrow cursor-pointer text-navy">+ New order</summary>
            <form action={createOrder} className="mt-5 grid gap-4 sm:grid-cols-2">
              <input name="customer_name" required placeholder="Customer name" className="field" />
              <input name="phone" placeholder="Phone" className="field" />
              <input name="garment" required placeholder="Garment, e.g. Navy three-piece suit" className="field sm:col-span-2" />
              <label className="text-xs text-stone">
                Ready by
                <input name="due_date" type="date" className="field mt-1" />
              </label>
              <input name="notes" placeholder="Note for the customer (optional)" className="field self-end" />
              <button className="btn btn-navy sm:col-span-2">Create order and code</button>
            </form>
          </details>

          <div className="mt-6 space-y-3">
            {o.map((x) => (
              <article key={x.id} className="bg-white p-5">
                <div className="flex flex-wrap items-baseline justify-between gap-3">
                  <div>
                    <span className="display text-2xl text-navy">{x.garment}</span>
                    <p className="text-sm text-stone">
                      {x.customer_name} · <span className="tracking-wider text-navy">{x.code}</span>
                      {x.register_no && <> · No. {String(x.register_no).padStart(4, "0")}</>}
                    </p>
                  </div>
                  <a
                    href={x.phone ? `https://wa.me/${waNumber(x.phone)}?text=${encodeURIComponent(`Hello ${x.customer_name.split(" ")[0]}, track your Tezoro order here: ${process.env.NEXT_PUBLIC_SITE_URL ?? ""}/track/${x.code}`)}` : whatsappLink("")}
                    target="_blank"
                    rel="noopener"
                    className="text-xs text-[#1f8f4e]"
                  >
                    Send tracking link
                  </a>
                </div>
                <div className="mt-4 grid grid-cols-5 gap-1">
                  {orderStages.map((st, i) => (
                    <form key={st} action={setOrderStage}>
                      <input type="hidden" name="id" value={x.id} />
                      <input type="hidden" name="stage" value={i} />
                      <button className={`min-h-11 w-full px-1 text-[0.65rem] leading-tight ${i <= x.stage ? "bg-navy text-ivory" : "bg-navy/5 text-stone hover:bg-navy/10"}`}>{st}</button>
                    </form>
                  ))}
                </div>
                <details className="mt-3">
                  <summary className="cursor-pointer text-xs text-stone">Edit note, date, or issue One of One number</summary>
                  <form action={setOrderNote} className="mt-3 grid gap-2 sm:grid-cols-[1fr_auto_auto]">
                    <input type="hidden" name="id" value={x.id} />
                    <input name="notes" defaultValue={x.notes ?? ""} placeholder="Note shown to the customer" className="field" />
                    <input name="due_date" type="date" defaultValue={x.due_date ?? ""} className="field" />
                    <button className="btn btn-ghost-dark">Save</button>
                  </form>
                  {!x.register_no && (
                    <form action={issueNumber} className="mt-3 grid gap-2 sm:grid-cols-[auto_1fr_auto_auto] sm:items-center">
                      <input type="hidden" name="id" value={x.id} />
                      <input name="occasion" placeholder="Occasion" className="field" />
                      <input name="note" placeholder="Register note (optional)" className="field" />
                      <label className="flex items-center gap-2 text-xs text-stone">
                        <input type="checkbox" name="public" defaultChecked /> Show publicly
                      </label>
                      <button className="btn btn-gold">Issue number</button>
                    </form>
                  )}
                </details>
              </article>
            ))}
          </div>
        </section>
      )}
    </Shell>
  );
}
