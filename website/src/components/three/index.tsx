"use client";
import dynamic from "next/dynamic";

// WebGL scenes load only in the browser, after the page itself is visible.
export const HeroScene = dynamic(() => import("./HeroScene"), { ssr: false });
export const FabricViewer = dynamic(() => import("./FabricViewer"), {
  ssr: false,
  loading: () => <div className="h-full w-full animate-pulse bg-navy/5" />,
});
