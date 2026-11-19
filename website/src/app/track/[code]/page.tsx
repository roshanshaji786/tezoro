import type { Metadata } from "next";
import Link from "next/link";
import { getOrderByCode } from "@/lib/data";
import { orderStages } from "@/lib/content";
import { whatsappLink } from "@/lib/site";

export const dynamic = "force-dynamic";
export const metadata: Metadata = { title: "Order status", robots: { index: false } };

export default async function TrackOrder({ params }: { params: Promise<{ code: string }> }) {
  const { code } = await params;
  const { order, demo } = await getOrderByCode(decodeURIComponent(code));

  if (!order) {
    return (
      <section className="grain min-h-[85vh] bg-navy-deep px-4 pt-36 pb-24 text-ivory sm:px-8 sm:pt-44">
        <div className="relative z-[2] mx-auto max-w-2xl">
          <p className="eyebrow text-champagne">Order tracker</p>
          <h1 className="display mt-5 text-5xl">We could not find that code.</h1>
          <p className="mt-4 text-ivory/65">Check the code on your receipt, or ask us and we will look it up.</p>
          <div className="mt-10 flex flex-col gap-3 sm:flex-row">
            <Link href="/track" className="btn btn-gold">
              Try again
            </Link>
            <a href={whatsappLink("Hi Tezoro, could you tell me the status of my order?")} target="_blank" rel="noopener" className="btn btn-ghost-light">
              Ask on WhatsApp
            </a>
          </div>
        </div>
      </section>
    );
  }

  const first = order.customer_name.split(" ")[0];
  const due = order.due_date ? new Date(order.due_date + "T00:00:00").toLocaleDateString("en-IN", { weekday: "long", day: "numeric", month: "long" }) : null;

  return (
    <section className="grain min-h-[85vh] bg-navy-deep px-4 pt-36 pb-24 text-ivory sm:px-8 sm:pt-44">
      <div className="relative z-[2] mx-auto max-w-3xl">
        <p className="eyebrow text-champagne">
          Order {order.code} {demo && <span className="ml-2 text-ivory/40">(sample)</span>}
        </p>
        <h1 className="display mt-5 text-5xl sm:text-6xl">
          {order.stage >= 4 ? <>Ready for you, <em className="text-champagne">{first}.</em></> : <>Your {order.garment.toLowerCase()} is <em className="text-champagne">{orderStages[order.stage].toLowerCase()}</em>.</>}
        </h1>
        {due && order.stage < 4 && <p className="mt-4 text-ivory/65">Expected ready by {due}.</p>}

        <ol className="mt-14 grid gap-0 sm:grid-cols-5">
          {orderStages.map((s, i) => {
            const doneStage = i < order.stage;
            const current = i === order.stage;
            return (
              <li key={s} className="relative flex gap-4 pb-8 sm:block sm:pb-0">
                <div className="relative flex flex-col items-center sm:flex-row">
                  <span
                    className={`relative z-[1] flex h-10 w-10 shrink-0 items-center justify-center rounded-full border text-sm ${
                      current ? "border-champagne bg-champagne text-navy shadow-[0_0_0_8px_rgba(212,180,131,0.18)]" : doneStage ? "border-champagne bg-champagne/20 text-champagne" : "border-ivory/20 text-ivory/30"
                    }`}
                  >
                    {doneStage ? "✓" : i + 1}
                  </span>
                  {i < orderStages.length - 1 && (
                    <span className={`absolute top-10 left-1/2 h-[calc(100%+2rem)] w-px -translate-x-1/2 sm:top-1/2 sm:left-10 sm:h-px sm:w-[calc(100%-2.5rem)] sm:translate-x-0 ${doneStage ? "bg-champagne" : "bg-ivory/15"}`} />
                  )}
                </div>
                <p className={`text-sm sm:mt-4 sm:pr-3 ${current ? "text-champagne" : doneStage ? "text-ivory/80" : "text-ivory/35"}`}>{s}</p>
              </li>
            );
          })}
        </ol>

        {order.notes && (
          <div className="mt-14 border-l-2 border-champagne pl-5">
            <p className="eyebrow text-[0.6rem] text-ivory/50">From your tailor</p>
            <p className="display mt-2 text-2xl text-ivory/90 italic">{order.notes}</p>
          </div>
        )}

        {order.register_no && (
          <p className="mt-10 text-sm text-ivory/55">
            One of One register: <span className="text-champagne">No. {String(order.register_no).padStart(4, "0")}</span>
          </p>
        )}

        <div className="mt-12 flex flex-col gap-3 sm:flex-row">
          <a href={whatsappLink(`Hi Tezoro, a question about my order ${order.code}.`)} target="_blank" rel="noopener" className="btn btn-gold">
            Message my tailor
          </a>
          <Link href="/visit" className="btn btn-ghost-light">
            Directions to the atelier
          </Link>
        </div>
      </div>
    </section>
  );
}
