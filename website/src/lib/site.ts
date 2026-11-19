// Business details in one place. Values marked PLACEHOLDER still need the client's confirmation.
export const site = {
  name: "Tezoro Atelier",
  short: "Tezoro",
  tagline: "Made for you, only you.",
  description:
    "Tezoro Atelier is a men's bespoke tailoring house and wedding floor in Pothencode, Thiruvananthapuram. Suits, shirts, sherwanis and wedding wear, cut for one man only.",
  url: process.env.NEXT_PUBLIC_SITE_URL ?? "https://tezoro.in", // PLACEHOLDER domain
  phone: "+91 96335 98100",
  phoneHref: "tel:+919633598100",
  whatsapp: "919633598100",
  email: "hello@tezoro.in", // PLACEHOLDER
  instagram: "https://instagram.com/tezoro.atelier", // PLACEHOLDER
  instagramHandle: "@tezoro.atelier",
  address: {
    line1: "Near Zudio, Pothencode",
    line2: "Thiruvananthapuram, Kerala 695584",
    mapQuery: "Zudio Pothencode Thiruvananthapuram",
  },
  hours: [
    { days: "Monday to Saturday", time: "10:00 am to 9:00 pm" },
    { days: "Sunday", time: "By appointment" },
  ],
} as const;

export const nav = [
  { href: "/bespoke", label: "Bespoke" },
  { href: "/wedding", label: "Wedding Floor" },
  { href: "/lookbook", label: "Lookbook" },
  { href: "/fabrics", label: "Fabrics" },
  { href: "/process", label: "How it works" },
  { href: "/one-of-one", label: "One of One" },
  { href: "/visit", label: "Visit" },
] as const;

export function whatsappLink(message: string) {
  return `https://wa.me/${site.whatsapp}?text=${encodeURIComponent(message)}`;
}
