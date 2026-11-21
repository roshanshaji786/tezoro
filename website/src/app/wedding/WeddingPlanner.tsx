"use client";
import Link from "next/link";
import { useMemo, useState } from "react";
import { weddingMilestones } from "@/lib/content";

const DAY = 86_400_000;
const fmt = (d: Date) => d.toLocaleDateString("en-IN", { weekday: "short", day: "numeric", month: "short", year: "numeric" });
const iso = (d: Date) => d.toISOString().slice(0, 10);

export function WeddingPlanner() {
  const [date, setDate] = useState("");
  const today = useMemo(() => {
    const t = new Date();
    t.setHours(0, 0, 0, 0);
    return t;
  }, []);

  const wedding = date ? new Date(date + "T00:00:00") : null;
  const daysLeft = wedding ? Math.round((wedding.getTime() - today.getTime()) / DAY) : null;

  const plan = wedding
    ? weddingMilestones.map((m) => {
        const d = new Date(wedding.getTime() - m.daysBefore * DAY);
        return { ...m, date: d, past: d < today };
      })
    : [];

  const next = plan.find((p) => !p.past);
  const status =
    daysLeft === null
      ? null
      : daysLeft < 0
        ? { tone: "warn", text: "That date has passed. Pick your wedding date to see your plan." }
        : daysLeft < 21
          ? { tone: "warn", text: "Tight, but we have done it. Message us today and we will tell you honestly what is possible." }
          : daysLeft < 60
            ? { tone: "ok", text: "Good timing for a groom's outfit. Book soon to include the family." }
            : { tone: "great", text: "Perfect timing. You have room for every outfit, every fitting, and no stress." };

  return (
    <div className="grid gap-10 lg:grid-cols-[0.8fr_1.2fr]">
      <div>
        <label htmlFor="wd" className="eyebrow text-champagne">
          Your wedding date
        </label>
        <input
          id="wd"
          type="date"
          min={iso(today)}
          value={date}
          onChange={(e) => setDate(e.target.value)}
          className="mt-4 block min-h-14 w-full border border-champagne/40 bg-transparent px-4 text-xl text-ivory [color-scheme:dark] focus:border-champagne focus:outline-none"
        />
        {daysLeft !== null && daysLeft >= 0 && (
          <div className="mt-10">
            <p className="display text-8xl text-champagne">{daysLeft}</p>
            <p className="eyebrow mt-2 text-ivory/60">days to go</p>
          </div>
        )}
        {status && (
          <p className={`mt-6 border-l-2 pl-4 text-sm leading-relaxed ${status.tone === "warn" ? "border-[#e2876f] text-[#f3c3b5]" : "border-champagne text-ivory/80"}`}>
            {status.text}
          </p>
        )}
        {wedding && daysLeft !== null && daysLeft >= 0 && (
          <Link href={`/book?purpose=wedding&wedding=${date}`} className="btn btn-gold mt-8 w-full sm:w-auto">
            Book my wedding consult
          </Link>
        )}
      </div>

      <ol className="relative">
        <span className="absolute top-2 bottom-2 left-[7px] w-px bg-champagne/30" aria-hidden="true" />
        {(plan.length ? plan : weddingMilestones.map((m) => ({ ...m, date: null as Date | null, past: false }))).map((m) => {
          const isNext = next && m.title === next.title;
          return (
            <li key={m.title} className={`relative pb-8 pl-10 transition-opacity duration-500 ${m.past ? "opacity-40" : ""}`}>
              <span
                className={`absolute top-1.5 left-0 h-[15px] w-[15px] rounded-full border ${
                  isNext ? "border-champagne bg-champagne shadow-[0_0_0_6px_rgba(185,155,136,0.2)]" : "border-champagne/60 bg-maroon-deep"
                }`}
              />
              <p className="eyebrow text-champagne/80">{m.date ? fmt(m.date) : `${m.daysBefore} days before`}</p>
              <h3 className="display mt-1 text-3xl text-ivory">
                {m.title} {isNext && <span className="eyebrow ml-2 align-middle text-[0.6rem] text-champagne">Next</span>}
              </h3>
              <p className="mt-1 text-sm text-ivory/60">{m.text}</p>
            </li>
          );
        })}
        <li className="relative pl-10">
          <span className="absolute top-1.5 left-0 h-[15px] w-[15px] rotate-45 bg-champagne" />
          <p className="eyebrow text-champagne/80">{wedding ? fmt(wedding) : "The day"}</p>
          <h3 className="display mt-1 text-3xl text-champagne">Your wedding</h3>
        </li>
      </ol>
    </div>
  );
}
