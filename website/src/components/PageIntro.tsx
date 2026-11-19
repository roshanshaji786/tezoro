export function PageIntro({
  eyebrow,
  title,
  children,
  dark = false,
}: {
  eyebrow: string;
  title: React.ReactNode;
  children?: React.ReactNode;
  dark?: boolean;
}) {
  return (
    <section className={`${dark ? "grain bg-navy text-ivory" : "bg-ivory text-navy"} pt-36 pb-16 sm:pt-44 sm:pb-20`}>
      <div className="relative z-[2] mx-auto max-w-7xl px-4 sm:px-8">
        <p className={`eyebrow ${dark ? "text-champagne" : "text-gold"}`}>{eyebrow}</p>
        <h1 className="display mt-5 max-w-4xl text-5xl sm:text-7xl">{title}</h1>
        {children && <div className={`mt-6 max-w-2xl text-lg leading-relaxed ${dark ? "text-ivory/70" : "text-ink/70"}`}>{children}</div>}
      </div>
    </section>
  );
}

export function SectionTitle({ eyebrow, title, light = false, className = "" }: { eyebrow: string; title: React.ReactNode; light?: boolean; className?: string }) {
  return (
    <div className={className}>
      <p className={`eyebrow ${light ? "text-champagne" : "text-gold"}`}>{eyebrow}</p>
      <h2 className={`display mt-4 text-4xl sm:text-6xl ${light ? "text-ivory" : "text-navy"}`}>{title}</h2>
    </div>
  );
}
