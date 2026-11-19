import type { Metadata, Viewport } from "next";
import localFont from "next/font/local";
import "./globals.css";
import { Header } from "@/components/Header";
import { Footer } from "@/components/Footer";
import { WhatsAppFab } from "@/components/WhatsAppFab";
import { site } from "@/lib/site";

const cormorant = localFont({
  src: [
    { path: "../fonts/Cormorant.ttf", style: "normal" },
    { path: "../fonts/Cormorant-Italic.ttf", style: "italic" },
  ],
  variable: "--font-cormorant",
  display: "swap",
});

const cinzel = localFont({
  src: "../fonts/Cinzel.ttf",
  variable: "--font-cinzel",
  display: "swap",
});

export const metadata: Metadata = {
  metadataBase: new URL(site.url),
  title: {
    default: "Tezoro Atelier · Bespoke tailoring and wedding wear, Thiruvananthapuram",
    template: "%s · Tezoro Atelier",
  },
  description: site.description,
  openGraph: {
    title: "Tezoro Atelier",
    description: site.description,
    siteName: "Tezoro Atelier",
    locale: "en_IN",
    type: "website",
  },
  icons: { icon: "/icon.svg" },
};

export const viewport: Viewport = {
  themeColor: "#14213D",
};

const jsonLd = {
  "@context": "https://schema.org",
  "@type": "ClothingStore",
  name: site.name,
  description: site.description,
  url: site.url,
  telephone: site.phone,
  email: site.email,
  address: {
    "@type": "PostalAddress",
    streetAddress: site.address.line1,
    addressLocality: "Thiruvananthapuram",
    addressRegion: "Kerala",
    postalCode: "695584",
    addressCountry: "IN",
  },
  openingHours: "Mo-Sa 10:00-21:00",
  sameAs: [site.instagram],
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en-IN" className={`${cormorant.variable} ${cinzel.variable}`}>
      <body>
        <a href="#main" className="sr-only focus:not-sr-only focus:fixed focus:top-2 focus:left-2 focus:z-[100] focus:bg-navy focus:p-3 focus:text-ivory">
          Skip to content
        </a>
        <Header />
        <main id="main">{children}</main>
        <Footer />
        <WhatsAppFab />
        <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />
      </body>
    </html>
  );
}
