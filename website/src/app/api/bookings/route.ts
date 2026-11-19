import { NextResponse } from "next/server";
import { randomBytes } from "crypto";
import { db } from "@/lib/db";
import { purposes, slots } from "@/lib/content";
import { clientIp, limited } from "@/lib/ratelimit";

const ALPHABET = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789";
function makeRef() {
  const b = randomBytes(6);
  return "TB-" + Array.from(b, (x) => ALPHABET[x % ALPHABET.length]).join("");
}

const clean = (v: unknown, max = 200) => (typeof v === "string" ? v.trim().slice(0, max) : "");
const isDate = (v: string) => /^\d{4}-\d{2}-\d{2}$/.test(v) && !Number.isNaN(Date.parse(v));

export async function POST(req: Request) {
  if (limited("book:" + clientIp(req.headers), 5, 10 * 60_000)) {
    return NextResponse.json({ ok: false, error: "Too many bookings from this connection. Please message us on WhatsApp." }, { status: 429 });
  }
  const origin = req.headers.get("origin");
  if (origin && new URL(origin).host !== req.headers.get("host")) {
    return NextResponse.json({ ok: false, error: "Invalid origin" }, { status: 403 });
  }
  if (Number(req.headers.get("content-length") ?? 0) > 8_000) {
    return NextResponse.json({ ok: false, error: "Request too large" }, { status: 413 });
  }
  let body: Record<string, unknown>;
  try {
    body = await req.json();
  } catch {
    return NextResponse.json({ ok: false, error: "Invalid request" }, { status: 400 });
  }

  // Honeypot: real people never fill this hidden field.
  if (clean(body.company)) return NextResponse.json({ ok: true, ref: makeRef(), stored: false });

  const purpose = clean(body.purpose, 20);
  const preferred_date = clean(body.date, 10);
  const slot = clean(body.slot, 10);
  const name = clean(body.name, 80);
  const phone = clean(body.phone, 20).replace(/[^\d+ ]/g, "");
  const email = clean(body.email, 120) || null;
  const wedding_date = clean(body.weddingDate, 10) || null;
  const look_code = clean(body.look, 8) || null;
  const fabric_id = clean(body.fabric, 8) || null;
  const notes = clean(body.notes, 800) || null;

  const errors: string[] = [];
  if (!purposes.some((p) => p.id === purpose)) errors.push("purpose");
  const day = Date.parse(preferred_date);
  if (!isDate(preferred_date) || day < Date.now() - 86_400_000 || day > Date.now() + 120 * 86_400_000) errors.push("date");
  if (!slots.includes(slot)) errors.push("slot");
  if (name.length < 2 || /[<>]/.test(name)) errors.push("name");
  if (phone.replace(/\D/g, "").length < 10) errors.push("phone");
  if (email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) errors.push("email");
  if (wedding_date && !isDate(wedding_date)) errors.push("weddingDate");
  if (errors.length) return NextResponse.json({ ok: false, error: "Please check: " + errors.join(", ") }, { status: 422 });

  const ref = makeRef();
  const c = db();
  let stored = false;
  if (c) {
    const { error } = await c.rpc("tezoro_create_booking", { p: { ref, purpose, preferred_date, slot, name, phone, email, wedding_date, look_code, fabric_id, notes } });
    if (error) {
      console.error("booking insert failed", error.message);
    } else {
      stored = true;
    }
  }
  return NextResponse.json({ ok: true, ref, stored });
}
