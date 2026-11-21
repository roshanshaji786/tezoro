"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useEffect, useState } from "react";
import { Logo } from "./Logo";
import { nav } from "@/lib/site";

// Pages whose top section is dark, so the header starts in light-on-dark mode.
const DARK_TOP = ["/", "/wedding", "/one-of-one", "/fabrics"];

export function Header() {
  const pathname = usePathname();
  const [scrolled, setScrolled] = useState(false);
  const [open, setOpen] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 40);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  useEffect(() => setOpen(false), [pathname]);
  useEffect(() => {
    document.body.style.overflow = open ? "hidden" : "";
  }, [open]);

  if (pathname.startsWith("/admin")) return null;

  const darkTop = DARK_TOP.includes(pathname) || pathname.startsWith("/track");
  const light = !scrolled && darkTop && !open;
  const solid = scrolled || open;

  return (
    <header
      className={`fixed inset-x-0 top-0 z-50 transition-all duration-500 ${
        solid ? "bg-ivory/90 shadow-[0_1px_0_rgba(38,59,50,0.08)] backdrop-blur-md" : "bg-transparent"
      }`}
    >
      <div className="mx-auto flex h-18 max-w-7xl items-center justify-between px-4 sm:px-8" style={{ height: 72 }}>
        <Link href="/" aria-label="Tezoro Atelier home">
          <Logo light={light} />
        </Link>

        <nav className="hidden items-center gap-7 lg:flex" aria-label="Main">
          {nav.map((n) => {
            const active = pathname === n.href;
            return (
              <Link
                key={n.href}
                href={n.href}
                className={`relative font-[family-name:var(--font-caps)] text-[0.66rem] tracking-[0.22em] uppercase transition-colors ${
                  light ? "text-ivory/80 hover:text-champagne" : "text-navy/70 hover:text-navy"
                } ${active ? (light ? "!text-champagne" : "!text-navy") : ""}`}
              >
                {n.label}
                {active && <span className="absolute -bottom-2 left-0 h-px w-full bg-champagne" />}
              </Link>
            );
          })}
        </nav>

        <div className="flex items-center gap-3">
          <Link href="/book" className={`btn hidden sm:inline-flex ${light ? "btn-gold" : "btn-navy"}`} style={{ minHeight: 42 }}>
            Book a fitting
          </Link>
          <button
            onClick={() => setOpen((o) => !o)}
            className={`flex h-11 w-11 items-center justify-center lg:hidden ${light ? "text-ivory" : "text-navy"}`}
            aria-label={open ? "Close menu" : "Open menu"}
            aria-expanded={open}
          >
            <span className="relative block h-3 w-6">
              <span className={`absolute left-0 h-px w-6 bg-current transition-all duration-300 ${open ? "top-1.5 rotate-45" : "top-0"}`} />
              <span className={`absolute left-0 h-px w-6 bg-current transition-all duration-300 ${open ? "top-1.5 -rotate-45" : "top-3"}`} />
            </span>
          </button>
        </div>
      </div>

      <div
        className={`fixed inset-x-0 bottom-0 top-[72px] bg-ivory transition-all duration-500 lg:hidden ${
          open ? "visible opacity-100" : "invisible opacity-0"
        }`}
      >
        <nav className="flex h-full flex-col px-6 pt-6 pb-10" aria-label="Mobile">
          {nav.map((n, i) => (
            <Link
              key={n.href}
              href={n.href}
              className="display border-b border-navy/10 py-4 text-3xl text-navy transition-all duration-500"
              style={{ transitionDelay: open ? `${i * 40}ms` : "0ms", transform: open ? "none" : "translateY(10px)" }}
            >
              {n.label}
            </Link>
          ))}
          <div className="mt-auto grid gap-3">
            <Link href="/book" className="btn btn-navy w-full">
              Book a fitting
            </Link>
            <Link href="/track" className="btn btn-ghost-dark w-full">
              Track my order
            </Link>
          </div>
        </nav>
      </div>
    </header>
  );
}
