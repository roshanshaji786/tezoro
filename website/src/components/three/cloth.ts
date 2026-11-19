// Shared cloth maths: the same wave runs in JS (for the thread and needle) and in GLSL (for the cloth),
// so the stitch always sits on the moving fabric.

export function wave(x: number, y: number, t: number) {
  return (
    0.48 * Math.sin(x * 0.55 + t * 0.6) * Math.cos(y * 0.42 + t * 0.35) +
    0.16 * Math.sin((x + y) * 0.9 + t * 0.85) +
    0.06 * Math.sin(x * 2.1 - t * 1.3)
  );
}

export const waveGLSL = /* glsl */ `
float wave(float x, float y, float t) {
  return 0.48 * sin(x * 0.55 + t * 0.6) * cos(y * 0.42 + t * 0.35)
       + 0.16 * sin((x + y) * 0.9 + t * 0.85)
       + 0.06 * sin(x * 2.1 - t * 1.3);
}
`;

export const noiseGLSL = /* glsl */ `
float hash(vec2 p) { return fract(sin(dot(p, vec2(127.1, 311.7))) * 43758.5453); }
float vnoise(vec2 p) {
  vec2 i = floor(p), f = fract(p);
  vec2 u = f * f * (3.0 - 2.0 * f);
  return mix(mix(hash(i), hash(i + vec2(1, 0)), u.x), mix(hash(i + vec2(0, 1)), hash(i + vec2(1, 1)), u.x), u.y);
}
`;

// Woven patterns, chosen by uPattern (same order as the Pattern type in content.ts).
export const patternGLSL = /* glsl */ `
${noiseGLSL}
float weave(vec2 uv, int p) {
  if (p == 0) { // twill
    return smoothstep(0.35, 0.65, abs(fract((uv.x + uv.y) * 38.0) - 0.5) * 2.0) * 0.6;
  } else if (p == 1) { // pinstripe
    float twill = abs(fract((uv.x + uv.y) * 60.0) - 0.5) * 0.25;
    return max(1.0 - smoothstep(0.0, 0.012, abs(fract(uv.x * 9.0) - 0.5)), twill);
  } else if (p == 2) { // herringbone
    float col = floor(uv.x * 14.0);
    float dir = mod(col, 2.0) < 1.0 ? 1.0 : -1.0;
    return smoothstep(0.3, 0.7, abs(fract(uv.y * 22.0 + dir * uv.x * 22.0) - 0.5) * 2.0) * 0.8;
  } else if (p == 3) { // brocade
    vec2 c = fract(uv * 6.0) - 0.5;
    vec2 c2 = fract(uv * 6.0 + 0.5) - 0.5;
    float petal = 1.0 - smoothstep(0.02, 0.05, abs(length(c * vec2(1.0, 0.62)) - 0.26));
    float dot1 = 1.0 - smoothstep(0.05, 0.08, length(c));
    float dot2 = 1.0 - smoothstep(0.03, 0.06, length(c2));
    return max(max(petal, dot1), dot2);
  } else if (p == 4) { // linen
    float h = smoothstep(0.4, 0.6, abs(fract(uv.y * 90.0 + vnoise(uv * vec2(4.0, 120.0)) * 0.6) - 0.5) * 2.0);
    float v = smoothstep(0.4, 0.6, abs(fract(uv.x * 90.0) - 0.5) * 2.0);
    return (h * 0.5 + v * 0.3) * (0.7 + 0.6 * vnoise(uv * vec2(220.0, 8.0)));
  } else if (p == 5) { // velvet
    return vnoise(uv * 40.0) * 0.25;
  } else if (p == 6) { // glen check
    vec2 g = step(0.5, fract(uv * 5.0));
    float chk = abs(g.x - g.y);
    float over = 1.0 - smoothstep(0.0, 0.01, abs(fract(uv.x * 5.0 + 0.25) - 0.5));
    return chk * 0.55 + over * 0.6;
  }
  // raw silk: slubbed horizontal threads
  float slub = smoothstep(0.75, 0.95, vnoise(uv * vec2(14.0, 160.0)));
  return smoothstep(0.4, 0.6, abs(fract(uv.y * 120.0) - 0.5) * 2.0) * 0.4 + slub * 0.7;
}
`;
