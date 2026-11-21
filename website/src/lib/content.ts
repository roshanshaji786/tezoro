// Site content. Prices are "from" prices and are PLACEHOLDERS until the client confirms them.

export type Pattern = "twill" | "pinstripe" | "herringbone" | "brocade" | "linen" | "velvet" | "check" | "silk";

export type Fabric = {
  id: string;
  name: string;
  origin: string;
  weight: string;
  season: string;
  feel: string;
  pattern: Pattern;
  base: string;
  accent: string;
  bestFor: string[];
};

export const fabrics: Fabric[] = [
  { id: "f01", name: "Midnight Super 120s", origin: "Italian worsted wool", weight: "260 g/m", season: "Evenings, air-conditioned halls", feel: "Smooth, cool, holds a crease", pattern: "twill", base: "#14213D", accent: "#2a3a63", bestFor: ["Reception suit", "Tuxedo"] },
  { id: "f02", name: "Banker's Chalk Stripe", origin: "English wool blend", weight: "280 g/m", season: "Year round indoors", feel: "Firm, structured drape", pattern: "pinstripe", base: "#1d2433", accent: "#c9c3b4", bestFor: ["Business suit", "Waistcoat"] },
  { id: "f03", name: "Sandstone Herringbone", origin: "Wool and linen", weight: "240 g/m", season: "Day events, monsoon evenings", feel: "Textured, soft hand", pattern: "herringbone", base: "#a8957a", accent: "#cbb89b", bestFor: ["Sports jacket", "Bandhgala"] },
  { id: "f04", name: "Champagne Zari Brocade", origin: "Banarasi silk brocade", weight: "320 g/m", season: "Wedding ceremony", feel: "Rich, rigid, catches light", pattern: "brocade", base: "#c8a66f", accent: "#f0dcae", bestFor: ["Sherwani", "Wedding bandhgala"] },
  { id: "f05", name: "Kerala Ivory Linen", origin: "Pure Irish linen", weight: "160 g/m", season: "Kerala summer, beach weddings", feel: "Crisp, breathes, softens with wear", pattern: "linen", base: "#ece4d3", accent: "#d6ccb6", bestFor: ["Shirts", "Kurta", "Summer suit"] },
  { id: "f06", name: "Maroon Silk Velvet", origin: "Silk-viscose velvet", weight: "300 g/m", season: "Reception night", feel: "Deep pile, warm glow", pattern: "velvet", base: "#5A1A24", accent: "#8a3443", bestFor: ["Reception jacket", "Nehru jacket"] },
  { id: "f07", name: "Glen Check Grey", origin: "Wool-mohair", weight: "250 g/m", season: "Year round", feel: "Lively, wrinkle resistant", pattern: "check", base: "#6f7179", accent: "#9da0a8", bestFor: ["Business suit", "Trousers"] },
  { id: "f08", name: "Raw Tussar Silk", origin: "Jharkhand tussar", weight: "180 g/m", season: "Haldi, mehendi, temple wedding", feel: "Slubbed, natural sheen", pattern: "silk", base: "#d9c08e", accent: "#ead6a8", bestFor: ["Kurta", "Mundu set", "Sherwani lining"] },
];

export type Look = {
  code: string;
  title: string;
  category: "Wedding" | "Suits" | "Shirts" | "Ethnic";
  occasion: string;
  fabricId: string;
  note: string;
};

export const looks: Look[] = [
  { code: "L01", title: "The Ivory Sherwani", category: "Wedding", occasion: "Nikah, muhurtham", fabricId: "f04", note: "Hand-finished zari collar, champagne lining, nine covered buttons." },
  { code: "L02", title: "Midnight Reception Tux", category: "Suits", occasion: "Reception", fabricId: "f01", note: "Peak lapel in silk satin, single button, tapered trouser." },
  { code: "L03", title: "Monsoon Herringbone", category: "Suits", occasion: "Engagement, office", fabricId: "f03", note: "Soft shoulder, patch pockets, unlined for Kerala weather." },
  { code: "L04", title: "Maroon Velvet Bandhgala", category: "Wedding", occasion: "Reception night", fabricId: "f06", note: "Mandarin collar, antique brass buttons, ivory trouser." },
  { code: "L05", title: "The Boardroom Stripe", category: "Suits", occasion: "Work, interviews", fabricId: "f02", note: "Two-button, half canvas, matching waistcoat." },
  { code: "L06", title: "Ivory Linen Kurta Set", category: "Ethnic", occasion: "Haldi, Onam, Eid", fabricId: "f05", note: "Hidden placket, side slits, gold kasavu piping." },
  { code: "L07", title: "Tussar Temple Set", category: "Ethnic", occasion: "Temple wedding", fabricId: "f08", note: "Raw silk shirt with a matching mundu and angavastram." },
  { code: "L08", title: "Everyday White Shirt", category: "Shirts", occasion: "Everyday", fabricId: "f05", note: "Your collar, your cuff, your monogram on the placket." },
  { code: "L09", title: "Glen Check Two-Piece", category: "Suits", occasion: "Business travel", fabricId: "f07", note: "Wrinkle-resistant wool-mohair, travels from Kochi to Dubai." },
];

export const services = [
  { title: "Bespoke Suits", from: "₹14,900", text: "Two and three-piece suits drafted to your measurements and cut by hand. Two fittings, one pattern, one man.", pattern: "twill" as Pattern, base: "#263B32", accent: "#3b5a4c" },
  { title: "Shirts", from: "₹2,490", text: "Choose collar, cuff, placket and monogram. Your pattern is saved, so the next shirt is a message away.", pattern: "linen" as Pattern, base: "#ece4d3", accent: "#d6ccb6" },
  { title: "Trousers", from: "₹2,990", text: "Rise, break and seat cut for how you sit, walk and stand. Wool, linen and cotton.", pattern: "check" as Pattern, base: "#6f7179", accent: "#9da0a8" },
  { title: "Ethnic", from: "₹5,900", text: "Kurtas, bandhgalas, Nehru jackets and mundu sets in silk, linen and khadi.", pattern: "silk" as Pattern, base: "#d9c08e", accent: "#ead6a8" },
];

export const packages = [
  {
    name: "The Groom",
    from: "₹39,900",
    items: ["Wedding sherwani or bandhgala", "Reception suit or tux", "Two shirts and accessories styling", "Three fittings, pressed and delivered"],
  },
  {
    name: "Groom & Family",
    from: "₹79,900",
    featured: true,
    items: ["Everything in The Groom", "Father and brothers, up to 4 outfits", "Colour story across the family", "Priority slots and a personal stylist"],
  },
  {
    name: "Full Wedding Party",
    from: "On request",
    items: ["Groom, family and groomsmen", "Coordinated fabrics and fits", "Group measurement day at your home", "Final fitting on the eve of the wedding"],
  },
];

export const processSteps = [
  { n: "01", title: "Consult", text: "Thirty quiet minutes over tea. Occasion, lifestyle, how you want to feel in it.", days: "Day 1" },
  { n: "02", title: "Choose", text: "Touch real cloth from our library. We shortlist three fabrics and build the look together.", days: "Day 1" },
  { n: "03", title: "Measure", text: "Over 30 measurements and posture notes. Your pattern is drafted by hand for you alone.", days: "Day 1" },
  { n: "04", title: "First fitting", text: "A basted garment, pinned and chalked on you. This is where fit is truly made.", days: "Day 10 to 14" },
  { n: "05", title: "Final fitting", text: "Finished garment, final adjustments, buttons sewn by hand.", days: "Day 18 to 21" },
  { n: "06", title: "Collect", text: "Pressed, numbered in the One of One register, and yours.", days: "Day 21+" },
];

export const weddingMilestones = [
  { daysBefore: 90, title: "Wedding consult", text: "Plan every event, outfits for the family, colour story." },
  { daysBefore: 75, title: "Fabrics and measurements", text: "Fabrics reserved, patterns drafted for each outfit." },
  { daysBefore: 45, title: "First fitting", text: "Basted fittings for the groom, then the family." },
  { daysBefore: 21, title: "Second fitting", text: "Embroidery and finishing approved." },
  { daysBefore: 10, title: "Final fitting", text: "Everything on, one last look in the mirror." },
  { daysBefore: 4, title: "Collection", text: "Pressed, packed and ready. Or delivered to your home." },
];

export type RegisterEntry = { no: number; garment: string; occasion: string; month: string; note?: string };

// Demo entries, shown until the live register in the database has entries.
export const demoRegister: RegisterEntry[] = [
  { no: 12, garment: "Ivory brocade sherwani", occasion: "Wedding", month: "Nov 2026", note: "Nine covered buttons, mother's initials inside the collar" },
  { no: 11, garment: "Midnight tuxedo", occasion: "Reception", month: "Nov 2026" },
  { no: 10, garment: "Linen kurta set", occasion: "Haldi", month: "Nov 2026" },
  { no: 9, garment: "Chalk stripe three-piece", occasion: "Work", month: "Oct 2026", note: "Lining in his daughter's favourite colour" },
  { no: 8, garment: "Tussar silk shirt and mundu", occasion: "Temple wedding", month: "Oct 2026" },
  { no: 7, garment: "Maroon velvet bandhgala", occasion: "Reception", month: "Oct 2026" },
];

export const purposes = [
  { id: "wedding", label: "Wedding", hint: "Groom, family or the full party" },
  { id: "suit", label: "Bespoke suit", hint: "Business, reception, occasion" },
  { id: "shirts", label: "Shirts", hint: "One or a wardrobe" },
  { id: "ethnic", label: "Ethnic wear", hint: "Kurta, bandhgala, mundu set" },
  { id: "alteration", label: "Alteration", hint: "Make what you own fit" },
] as const;

export const slots = ["10:30 am", "12:00 pm", "2:00 pm", "3:30 pm", "5:00 pm", "6:30 pm", "8:00 pm"];

export const orderStages = ["Order placed", "Fabric cut", "Stitching", "Fitting ready", "Ready to collect"] as const;

export function fabricById(id: string) {
  return fabrics.find((f) => f.id === id)!;
}
