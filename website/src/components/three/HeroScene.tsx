"use client";
import { Canvas, useFrame, useThree } from "@react-three/fiber";
import { Environment, Lightformer, Sparkles } from "@react-three/drei";
import { useEffect, useMemo, useRef, useState } from "react";
import * as THREE from "three";
import { wave, waveGLSL, noiseGLSL } from "./cloth";

const W = 24;
const H = 15;
const SEGMENTS = 220;

// Shader colours stay in sRGB because the shader writes straight to the screen.
const srgb = (hex: string) => {
  const c = new THREE.Color();
  c.setHex(parseInt(hex.slice(1), 16), THREE.LinearSRGBColorSpace);
  return new THREE.Vector3(c.r, c.g, c.b);
};
const STITCHES = 15;
const SEW_SECONDS = 9;

const clothVertex = /* glsl */ `
uniform float uTime;
varying vec3 vPos;
varying vec2 vUv;
varying vec3 vView;
varying vec3 vNormal;
${waveGLSL}
void main() {
  vUv = uv;
  vec3 p = position;
  float e = 0.02;
  float h = wave(p.x, p.y, uTime);
  float hx = wave(p.x + e, p.y, uTime);
  float hy = wave(p.x, p.y + e, uTime);
  vNormal = normalize(normalMatrix * normalize(vec3(-(hx - h) / e, -(hy - h) / e, 1.0)));
  p.z += h;
  vPos = p;
  vec4 mv = modelViewMatrix * vec4(p, 1.0);
  vView = -mv.xyz;
  gl_Position = projectionMatrix * mv;
}
`;

const clothFragment = /* glsl */ `
uniform float uTime;
uniform vec3 uBase;
uniform vec3 uSheen;
varying vec3 vPos;
varying vec2 vUv;
varying vec3 vView;
varying vec3 vNormal;
${noiseGLSL}
void main() {
  vec3 N = normalize(vNormal);
  if (!gl_FrontFacing) N = -N;
  vec3 V = normalize(vView);
  vec3 L = normalize(vec3(-0.6, 0.9, 0.5));
  float diff = clamp(dot(N, L) * 0.5 + 0.5, 0.0, 1.0);
  // anisotropic-looking silk sheen along the folds
  float rim = pow(1.0 - abs(dot(N, V)), 2.2);
  float spec = pow(max(dot(reflect(-L, N), V), 0.0), 18.0);
  float twill = abs(fract((vUv.x + vUv.y) * 140.0) - 0.5);
  float grain = vnoise(vUv * vec2(600.0, 30.0)) * 0.04;
  vec3 col = uBase * (0.2 + 1.25 * diff * diff) + grain * uSheen;
  col += uSheen * (rim * 0.5 + spec * 0.7);
  col *= 0.98 + twill * 0.04;
  // vignette towards the edges of the cloth
  float edge = smoothstep(0.0, 0.25, vUv.x) * smoothstep(1.0, 0.75, vUv.x) * smoothstep(0.0, 0.3, vUv.y) * smoothstep(1.0, 0.7, vUv.y);
  col = mix(vec3(0.04, 0.07, 0.14), col, 0.55 + 0.45 * edge);
  gl_FragColor = vec4(col, 1.0);
}
`;

function threadPoint(u: number, t: number, out: THREE.Vector3) {
  // A gentle S-curve across the cloth.
  const x = -2.2 + u * 9;
  const y = Math.sin(u * Math.PI * 1.2 + 0.4) * 1.1 - 1.4;
  // Running stitch: above the cloth on the "up" half, below it (hidden) on the "down" half.
  const s = Math.tanh(Math.sin(u * Math.PI * 2 * STITCHES) * 5);
  out.set(x, y, wave(x, y, t) + s * 0.06 + 0.005);
  return out;
}

function Scene({ reduced }: { reduced: boolean }) {
  const group = useRef<THREE.Group>(null);
  const thread = useRef<THREE.Mesh>(null);
  const needle = useRef<THREE.Group>(null);
  const { pointer, viewport } = useThree();
  const mobile = viewport.aspect < 0.9;

  const clothMat = useMemo(
    () =>
      new THREE.ShaderMaterial({
        vertexShader: clothVertex,
        fragmentShader: clothFragment,
        uniforms: {
          uTime: { value: 0 },
          uBase: { value: srgb("#2a3f75") },
          uSheen: { value: srgb("#d4b483") },
        },
        side: THREE.DoubleSide,
      }),
    [],
  );

  const clothGeo = useMemo(() => new THREE.PlaneGeometry(W, H, 240, 150), []);

  const pts = useMemo(() => Array.from({ length: SEGMENTS + 1 }, () => new THREE.Vector3()), []);
  const tmp = useMemo(() => ({ a: new THREE.Vector3(), b: new THREE.Vector3(), q: new THREE.Quaternion(), up: new THREE.Vector3(0, 1, 0) }), []);

  useFrame((state) => {
    const t = reduced ? 2 : state.clock.elapsedTime;
    clothMat.uniforms.uTime.value = t;

    // Sewing progress loops: sew across, hold, start again.
    const cycle = (t % (SEW_SECONDS + 2.5)) / SEW_SECONDS;
    const progress = reduced ? 0.72 : Math.min(cycle, 1);

    for (let i = 0; i <= SEGMENTS; i++) threadPoint(i / SEGMENTS, t, pts[i]);
    const curve = new THREE.CatmullRomCurve3(pts);
    const geo = new THREE.TubeGeometry(curve, SEGMENTS * 2, 0.03, 6, false);
    const count = geo.index!.count;
    geo.setDrawRange(0, Math.floor((count * progress) / 6) * 6);
    if (thread.current) {
      thread.current.geometry.dispose();
      thread.current.geometry = geo;
    }

    // Needle rides the tip of the thread, dipping in and out of the cloth.
    if (needle.current) {
      const u = Math.max(progress, 0.001);
      threadPoint(u, t, tmp.a);
      threadPoint(Math.min(u + 0.012, 1), t, tmp.b);
      const dir = tmp.b.sub(tmp.a).normalize();
      dir.z += Math.cos(u * Math.PI * 2 * STITCHES) * 0.9;
      dir.normalize();
      tmp.q.setFromUnitVectors(tmp.up, dir);
      needle.current.position.copy(tmp.a);
      needle.current.quaternion.slerp(tmp.q, 0.35);
      needle.current.visible = progress < 1;
    }

    // Soft parallax with the pointer.
    if (group.current) {
      group.current.rotation.x = THREE.MathUtils.lerp(group.current.rotation.x, -0.55 + pointer.y * 0.08, 0.04);
      group.current.rotation.y = THREE.MathUtils.lerp(group.current.rotation.y, pointer.x * 0.12, 0.04);
    }
  });

  return (
    <group ref={group} rotation={[-0.55, 0, -0.08]} position={mobile ? [-1.0, 1.6, 0] : [1.4, -0.3, 0]} scale={mobile ? 0.6 : 1}>
      <mesh geometry={clothGeo} material={clothMat} />
      <mesh ref={thread}>
        <bufferGeometry />
        <meshStandardMaterial color="#e2c58f" roughness={0.35} metalness={0.55} emissive="#5a4420" emissiveIntensity={0.25} />
      </mesh>
      <group ref={needle} scale={1.6}>
        {/* shaft, pointing along +Y; tip leads */}
        <mesh position={[0, -0.55, 0]}>
          <cylinderGeometry args={[0.03, 0.03, 1.1, 16]} />
          <meshStandardMaterial color="#e9e4da" metalness={1} roughness={0.18} />
        </mesh>
        <mesh position={[0, 0.12, 0]}>
          <coneGeometry args={[0.03, 0.26, 16]} />
          <meshStandardMaterial color="#e9e4da" metalness={1} roughness={0.18} />
        </mesh>
        <mesh position={[0, -1.02, 0]}>
          <torusGeometry args={[0.03, 0.009, 8, 20]} />
          <meshStandardMaterial color="#d4b483" metalness={1} roughness={0.25} />
        </mesh>
      </group>
    </group>
  );
}

export default function HeroScene() {
  const wrap = useRef<HTMLDivElement>(null);
  const [visible, setVisible] = useState(true);
  const [reduced, setReduced] = useState(false);

  useEffect(() => {
    setReduced(window.matchMedia("(prefers-reduced-motion: reduce)").matches);
    const el = wrap.current;
    if (!el) return;
    const io = new IntersectionObserver(([e]) => setVisible(e.isIntersecting));
    io.observe(el);
    return () => io.disconnect();
  }, []);

  return (
    <div ref={wrap} className="absolute inset-0">
      <Canvas
        frameloop={visible ? "always" : "never"}
        dpr={[1, 1.75]}
        camera={{ position: [0, 0, 7.2], fov: 42 }}
        gl={{ antialias: true, powerPreference: "high-performance" }}
        onCreated={({ gl }) => gl.setClearColor("#0b1426")}
      >
        <ambientLight intensity={0.5} />
        <directionalLight position={[-3, 4, 5]} intensity={2.2} color="#fff4e0" />
        <Environment resolution={64}>
          <Lightformer intensity={3} position={[0, 4, 4]} scale={[10, 2, 1]} color="#fff2dc" />
          <Lightformer intensity={1.5} position={[-5, 0, 2]} scale={[2, 6, 1]} color="#d4b483" />
          <Lightformer intensity={1} position={[5, -1, 2]} scale={[2, 6, 1]} color="#8aa0d0" />
        </Environment>
        <Scene reduced={reduced} />
        {!reduced && <Sparkles count={60} scale={[12, 6, 4]} size={2.2} speed={0.25} color="#d4b483" opacity={0.6} />}
        <fog attach="fog" args={["#0b1426", 7, 14]} />
      </Canvas>
    </div>
  );
}
