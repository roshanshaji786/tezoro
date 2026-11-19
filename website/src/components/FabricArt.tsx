import { useId } from "react";
import type { Pattern } from "@/lib/content";

// Woven-cloth illustrations drawn in SVG. Stand-ins until the photo shoot; they keep the
// site honest (no stock photos of clothes we did not make).
export function FabricArt({
  pattern,
  base,
  accent,
  className = "",
  scale = 1,
}: {
  pattern: Pattern;
  base: string;
  accent: string;
  className?: string;
  scale?: number;
}) {
  const id = useId().replace(/:/g, "");
  const s = scale;
  let tile: React.ReactNode;
  let size = 12 * s;

  switch (pattern) {
    case "twill":
      size = 8 * s;
      tile = <path d={`M0 ${size} L${size} 0`} stroke={accent} strokeWidth={1.6 * s} opacity={0.55} />;
      break;
    case "pinstripe":
      size = 14 * s;
      tile = (
        <>
          <path d={`M0 ${size} L${size} 0`} stroke="#000" strokeOpacity={0.12} strokeWidth={1.4 * s} />
          <line x1={size / 2} y1={0} x2={size / 2} y2={size} stroke={accent} strokeWidth={0.7 * s} opacity={0.75} />
        </>
      );
      break;
    case "herringbone":
      size = 16 * s;
      tile = (
        <path
          d={`M0 0 L${size / 2} ${size / 2} L0 ${size} M${size / 2} 0 L${size} ${size / 2} L${size / 2} ${size}`}
          stroke={accent}
          strokeWidth={2.2 * s}
          fill="none"
          opacity={0.75}
        />
      );
      break;
    case "brocade":
      size = 28 * s;
      tile = (
        <g fill="none" stroke={accent} strokeWidth={1.1 * s} opacity={0.9}>
          <path
            d={`M${size / 2} ${2 * s} C${size * 0.8} ${size * 0.3} ${size * 0.8} ${size * 0.7} ${size / 2} ${size - 2 * s} C${size * 0.2} ${size * 0.7} ${size * 0.2} ${size * 0.3} ${size / 2} ${2 * s} Z`}
          />
          <circle cx={size / 2} cy={size / 2} r={2.4 * s} fill={accent} />
          <circle cx={0} cy={0} r={1.6 * s} fill={accent} />
          <circle cx={size} cy={size} r={1.6 * s} fill={accent} />
          <circle cx={size} cy={0} r={1.6 * s} fill={accent} />
          <circle cx={0} cy={size} r={1.6 * s} fill={accent} />
        </g>
      );
      break;
    case "linen":
      size = 6 * s;
      tile = (
        <>
          <line x1={0} y1={size / 3} x2={size} y2={size / 3} stroke={accent} strokeWidth={0.9 * s} opacity={0.7} />
          <line x1={size / 2} y1={0} x2={size / 2} y2={size} stroke={accent} strokeWidth={0.6 * s} opacity={0.5} />
        </>
      );
      break;
    case "velvet":
      size = 40 * s;
      tile = <circle cx={size / 2} cy={size / 2} r={size / 2.2} fill={accent} opacity={0.12} />;
      break;
    case "check":
      size = 24 * s;
      tile = (
        <>
          <rect x={0} y={0} width={size / 2} height={size / 2} fill={accent} opacity={0.35} />
          <rect x={size / 2} y={size / 2} width={size / 2} height={size / 2} fill={accent} opacity={0.35} />
          <line x1={size * 0.75} y1={0} x2={size * 0.75} y2={size} stroke="#c9b48a" strokeWidth={0.6 * s} opacity={0.6} />
        </>
      );
      break;
    case "silk":
      size = 10 * s;
      tile = (
        <>
          <line x1={0} y1={size / 2} x2={size} y2={size / 2} stroke={accent} strokeWidth={0.8 * s} opacity={0.6} />
          <rect x={size * 0.2} y={size * 0.42} width={size * 0.35} height={size * 0.16} fill={accent} opacity={0.5} rx={0.5} />
        </>
      );
      break;
  }

  return (
    <svg className={className} preserveAspectRatio="none" aria-hidden="true" width="100%" height="100%">
      <defs>
        <pattern id={`p${id}`} width={size} height={size} patternUnits="userSpaceOnUse">
          {tile}
        </pattern>
        <linearGradient id={`g${id}`} x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" stopColor="#fff" stopOpacity="0.16" />
          <stop offset="0.45" stopColor="#fff" stopOpacity="0" />
          <stop offset="0.7" stopColor="#000" stopOpacity="0.12" />
          <stop offset="1" stopColor="#000" stopOpacity="0.28" />
        </linearGradient>
      </defs>
      <rect width="100%" height="100%" fill={base} />
      <rect width="100%" height="100%" fill={`url(#p${id})`} />
      <rect width="100%" height="100%" fill={`url(#g${id})`} />
    </svg>
  );
}
