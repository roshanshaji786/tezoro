// Hanger-arch needle mark ("H" direction). Not final yet: swap the paths here when the logo is signed off.
const RING =
  "M50 6 a44 44 0 1 1 0 88 a44 44 0 1 1 0 -88 Z M50 11.2 a38.8 38.8 0 1 0 0 77.6 a38.8 38.8 0 1 0 0 -77.6 Z";
const ARCH = "M26 36 Q50 24 74 36 L74 44 Q50 32 26 44 Z";
const NEEDLE =
  "M45.2 37 H54.8 L53.87 58 L50 86.6 L46.13 58 Z M48.7 42.5 a1.3 1.3 0 0 1 2.6 0 V54 a1.3 1.3 0 0 1 -2.6 0 Z";

export function LogoMark({ className = "", color = "currentColor" }: { className?: string; color?: string }) {
  return (
    <svg viewBox="0 0 100 100" className={className} fill={color} aria-hidden="true">
      <path fillRule="evenodd" d={RING} />
      <path d={ARCH} />
      <path fillRule="evenodd" d={NEEDLE} />
    </svg>
  );
}

export function Logo({ light = false, className = "" }: { light?: boolean; className?: string }) {
  return (
    <span className={`flex items-center gap-3 ${className}`}>
      <LogoMark className="h-9 w-9 shrink-0" color={light ? "#D4B483" : "#14213D"} />
      <span className="flex flex-col leading-none">
        <span
          className={`font-[family-name:var(--font-display)] text-[1.35rem] tracking-[0.34em] ${light ? "text-ivory" : "text-navy"}`}
        >
          TEZORO
        </span>
        <span className="mt-1 font-[family-name:var(--font-caps)] text-[0.5rem] tracking-[0.62em] text-champagne">
          ATELIER
        </span>
      </span>
      <span className="sr-only">Tezoro Atelier</span>
    </span>
  );
}
