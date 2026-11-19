import type { MetadataRoute } from "next";
import { site } from "@/lib/site";

export default function sitemap(): MetadataRoute.Sitemap {
  const pages = ["", "/bespoke", "/wedding", "/lookbook", "/fabrics", "/process", "/one-of-one", "/visit", "/book", "/track"];
  return pages.map((p) => ({ url: `${site.url}${p}`, changeFrequency: "weekly", priority: p === "" ? 1 : 0.7 }));
}
