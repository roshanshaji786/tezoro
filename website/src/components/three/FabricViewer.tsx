"use client";
import { Canvas, useFrame } from "@react-three/fiber";
import { OrbitControls } from "@react-three/drei";
import { useEffect, useMemo, useRef } from "react";
import * as THREE from "three";
import { patternGLSL } from "./cloth";
import type { Fabric, Pattern } from "@/lib/content";

// Shader colours stay in sRGB because the shader writes straight to the screen.
const raw = (hex: string) => new THREE.Color().setHex(parseInt(hex.slice(1), 16), THREE.LinearSRGBColorSpace);

const PATTERNS: Pattern[] = ["twill", "pinstripe", "herringbone", "brocade", "linen", "velvet", "check", "silk"];

const vertex = /* glsl */ `
uniform float uTime;
uniform float uDrape;
varying vec3 vPos;
varying vec2 vUv;
varying vec3 vView;
void main() {
  vUv = uv;
  vec3 p = position;
  // Drape: the swatch hangs from its top edge and sways.
  float hang = 1.0 - uv.y;
  p.z += sin(p.x * 2.2 + uTime * 1.1) * 0.12 * hang * uDrape;
  p.z += sin(p.y * 3.0 + uTime * 0.8) * 0.06 * uDrape;
  p.z -= hang * hang * 0.35 * uDrape;
  p.x += sin(p.y * 2.0 + uTime * 0.7) * 0.03 * hang * uDrape;
  vPos = p;
  vec4 mv = modelViewMatrix * vec4(p, 1.0);
  vView = -mv.xyz;
  gl_Position = projectionMatrix * mv;
}
`;

const fragment = /* glsl */ `
uniform vec3 uBase;
uniform vec3 uAccent;
uniform int uPattern;
uniform float uSheen;
varying vec3 vPos;
varying vec2 vUv;
varying vec3 vView;
${patternGLSL}
void main() {
  vec3 N = normalize(cross(dFdx(vPos), dFdy(vPos)));
  if (!gl_FrontFacing) N = -N;
  vec3 V = normalize(vView);
  vec3 L = normalize(vec3(-0.5, 0.9, 1.0));
  float diff = clamp(dot(N, L) * 0.55 + 0.45, 0.0, 1.0);
  float rim = pow(1.0 - abs(dot(N, V)), 2.0);
  float spec = pow(max(dot(reflect(-L, N), V), 0.0), 24.0);
  float w = weave(vUv, uPattern);
  vec3 col = mix(uBase, uAccent, clamp(w, 0.0, 1.0));
  col *= 0.55 + 0.6 * diff;
  col += vec3(1.0, 0.94, 0.82) * (spec * 0.35 + rim * uSheen);
  gl_FragColor = vec4(col, 1.0);
}
`;

function Swatch({ fabric }: { fabric: Fabric }) {
  const target = useRef({ base: raw(fabric.base), accent: raw(fabric.accent) });
  const mat = useMemo(
    () =>
      new THREE.ShaderMaterial({
        vertexShader: vertex,
        fragmentShader: fragment,
        side: THREE.DoubleSide,
        uniforms: {
          uTime: { value: 0 },
          uDrape: { value: 1 },
          uBase: { value: raw(fabric.base) },
          uAccent: { value: raw(fabric.accent) },
          uPattern: { value: PATTERNS.indexOf(fabric.pattern) },
          uSheen: { value: 0.3 },
        },
      }),
    // eslint-disable-next-line react-hooks/exhaustive-deps
    [],
  );
  const geo = useMemo(() => new THREE.PlaneGeometry(2.4, 3, 96, 120), []);

  useEffect(() => {
    target.current.base.copy(raw(fabric.base));
    target.current.accent.copy(raw(fabric.accent));
    mat.uniforms.uPattern.value = PATTERNS.indexOf(fabric.pattern);
    const sheen = { velvet: 0.65, silk: 0.45, brocade: 0.5 } as Record<string, number>;
    mat.uniforms.uSheen.value = sheen[fabric.pattern] ?? 0.25;
  }, [fabric, mat]);

  useFrame((s) => {
    mat.uniforms.uTime.value = s.clock.elapsedTime;
    (mat.uniforms.uBase.value as THREE.Color).lerp(target.current.base, 0.12);
    (mat.uniforms.uAccent.value as THREE.Color).lerp(target.current.accent, 0.12);
  });

  return (
    <group position={[0, 0.15, 0]}>
      <mesh geometry={geo} material={mat} />
      {/* brass hanger rod */}
      <mesh position={[0, 1.52, 0]} rotation={[0, 0, Math.PI / 2]}>
        <cylinderGeometry args={[0.035, 0.035, 2.7, 24]} />
        <meshStandardMaterial color="#bfa08c" metalness={0.9} roughness={0.3} />
      </mesh>
    </group>
  );
}

export default function FabricViewer({ fabric }: { fabric: Fabric }) {
  return (
    <Canvas dpr={[1, 1.75]} camera={{ position: [0, 0, 5.4], fov: 40 }} gl={{ antialias: true }}>
      <ambientLight intensity={0.8} />
      <directionalLight position={[2, 3, 4]} intensity={1.6} />
      <Swatch fabric={fabric} />
      <OrbitControls
        enablePan={false}
        enableZoom={false}
        minPolarAngle={Math.PI / 2 - 0.5}
        maxPolarAngle={Math.PI / 2 + 0.3}
        minAzimuthAngle={-0.9}
        maxAzimuthAngle={0.9}
        enableDamping
      />
    </Canvas>
  );
}
