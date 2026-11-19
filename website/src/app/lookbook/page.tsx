import type { Metadata } from "next";
import { PageIntro } from "@/components/PageIntro";
import { LookGrid } from "./LookGrid";

export const metadata: Metadata = {
  title: "Lookbook",
  description: "Past Tezoro commissions: wedding sherwanis, reception suits, shirts and ethnic wear. Inspiration for your own piece.",
};

export default function Lookbook() {
  return (
    <>
      <PageIntro eyebrow="Lookbook" title={<>Inspiration, <em>never imitation</em></>}>
        These are pieces we have made. We will never make them again, but they are a good place to start a conversation about yours.
      </PageIntro>
      <section className="mx-auto max-w-7xl px-4 pb-28 sm:px-8">
        <LookGrid />
      </section>
    </>
  );
}
