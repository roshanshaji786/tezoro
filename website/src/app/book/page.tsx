import type { Metadata } from "next";
import { Suspense } from "react";
import { BookingForm } from "./BookingForm";

export const metadata: Metadata = {
  title: "Book a fitting",
  description: "Book a consult or fitting at Tezoro Atelier, Pothencode. Three steps, confirmed on WhatsApp.",
};

export default function Book() {
  return (
    <section className="min-h-screen px-4 pt-32 pb-28 sm:px-8 sm:pt-40">
      <div className="mx-auto max-w-3xl">
        <p className="eyebrow text-gold">Book a fitting</p>
        <h1 className="display mt-4 text-5xl text-navy sm:text-7xl">
          Thirty quiet minutes, <em>all about you.</em>
        </h1>
        <div className="hairline mt-10 mb-12" />
      </div>
      <Suspense>
        <BookingForm />
      </Suspense>
    </section>
  );
}
