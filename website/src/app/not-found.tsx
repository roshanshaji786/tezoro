import Link from "next/link";

export default function NotFound() {
  return (
    <section className="flex min-h-[80vh] flex-col items-center justify-center px-4 pt-24 text-center">
      <p className="eyebrow text-gold">404</p>
      <h1 className="display mt-4 text-5xl text-navy sm:text-7xl">
        This page was <em>never cut.</em>
      </h1>
      <Link href="/" className="btn btn-navy mt-10">
        Back to the atelier
      </Link>
    </section>
  );
}
