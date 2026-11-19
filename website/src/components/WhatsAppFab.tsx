"use client";
import { usePathname } from "next/navigation";
import { whatsappLink } from "@/lib/site";

const messages: Record<string, string> = {
  "/wedding": "Hi Tezoro, I'm planning my wedding and would like to talk about outfits.",
  "/bespoke": "Hi Tezoro, I'd like to know more about a bespoke suit.",
  "/lookbook": "Hi Tezoro, I saw your lookbook and I'd like something made for me.",
  "/fabrics": "Hi Tezoro, I'd like to see some fabrics at the atelier.",
  "/visit": "Hi Tezoro, I'd like to visit the atelier.",
  "/one-of-one": "Hi Tezoro, I'd like my own One of One piece.",
};

export function WhatsAppFab() {
  const pathname = usePathname();
  if (pathname.startsWith("/admin")) return null;
  const msg = messages[pathname] ?? "Hi Tezoro, I'd like to know more.";
  return (
    <a
      href={whatsappLink(msg)}
      target="_blank"
      rel="noopener"
      aria-label="Chat with Tezoro on WhatsApp"
      className="group fixed right-4 bottom-4 z-40 flex h-14 w-14 items-center justify-center gap-3 rounded-full bg-[#1f8f4e] sm:w-auto sm:pr-5 sm:pl-4 text-white shadow-[0_10px_30px_rgba(0,0,0,0.25)] transition-transform duration-500 hover:-translate-y-0.5 sm:right-6 sm:bottom-6"
    >
      <svg viewBox="0 0 24 24" className="h-6 w-6" fill="currentColor" aria-hidden="true">
        <path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38a9.9 9.9 0 0 0 4.74 1.21h.01c5.46 0 9.9-4.45 9.9-9.91C21.95 6.45 17.5 2 12.04 2Zm5.8 14.04c-.24.69-1.42 1.32-1.96 1.36-.5.04-.97.22-3.27-.68-2.77-1.09-4.52-3.92-4.66-4.1-.13-.18-1.11-1.48-1.11-2.83s.71-2 .96-2.28c.25-.27.55-.34.73-.34l.52.01c.17.01.39-.06.61.47.24.55.79 1.9.86 2.04.07.14.11.3.02.48-.09.18-.14.3-.27.46-.14.16-.29.36-.41.48-.14.14-.28.29-.12.56.16.27.71 1.17 1.52 1.89 1.05.93 1.93 1.22 2.2 1.36.27.14.43.11.59-.07.16-.18.68-.79.86-1.07.18-.27.36-.23.61-.14.25.09 1.59.75 1.86.89.27.14.45.2.52.32.07.11.07.66-.17 1.35Z" />
      </svg>
      <span className="hidden text-sm font-medium tracking-wide sm:inline">Chat with us</span>
    </a>
  );
}
