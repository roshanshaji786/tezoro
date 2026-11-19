import "server-only";
import { cookies } from "next/headers";
import { createHmac, timingSafeEqual } from "crypto";

const COOKIE = "tz_admin";
const MAX_AGE = 60 * 60 * 12; // 12 hours

function secret() {
  return process.env.ADMIN_SECRET || process.env.ADMIN_PASSWORD || "";
}

function sign(value: string) {
  return createHmac("sha256", secret()).update(value).digest("hex");
}

export function adminConfigured() {
  return Boolean(process.env.ADMIN_PASSWORD);
}

export function passwordMatches(input: string) {
  const expected = process.env.ADMIN_PASSWORD ?? "";
  if (!expected) return false;
  const a = Buffer.from(sign(input));
  const b = Buffer.from(sign(expected));
  return a.length === b.length && timingSafeEqual(a, b);
}

export async function startSession() {
  const exp = String(Date.now() + MAX_AGE * 1000);
  (await cookies()).set(COOKIE, `${exp}.${sign(exp)}`, {
    httpOnly: true,
    secure: process.env.NODE_ENV === "production",
    sameSite: "lax",
    maxAge: MAX_AGE,
    path: "/",
  });
}

export async function endSession() {
  (await cookies()).delete(COOKIE);
}

export async function isAdmin() {
  if (!adminConfigured()) return false;
  const raw = (await cookies()).get(COOKIE)?.value;
  if (!raw) return false;
  const [exp, sig] = raw.split(".");
  if (!exp || !sig || Number(exp) < Date.now()) return false;
  const a = Buffer.from(sig);
  const b = Buffer.from(sign(exp));
  return a.length === b.length && timingSafeEqual(a, b);
}
