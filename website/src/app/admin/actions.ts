"use server";
import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";
import { randomInt } from "crypto";
import { db } from "@/lib/db";
import { endSession, isAdmin, passwordMatches, startSession } from "@/lib/auth";

async function guard() {
  if (!(await isAdmin())) redirect("/admin");
  const c = db();
  if (!c) throw new Error("Database is not connected");
  return c;
}

const s = (f: FormData, k: string, max = 200) => String(f.get(k) ?? "").trim().slice(0, max);

export async function login(_: unknown, form: FormData) {
  if (!passwordMatches(s(form, "password", 200))) {
    await new Promise((r) => setTimeout(r, 600));
    return { error: "That password is not right." };
  }
  await startSession();
  redirect("/admin");
}

export async function logout() {
  await endSession();
  redirect("/admin");
}

export async function setBookingStatus(form: FormData) {
  const c = await guard();
  const status = s(form, "status", 20);
  if (!["new", "confirmed", "visited", "cancelled"].includes(status)) return;
  await c.from("bookings").update({ status }).eq("id", s(form, "id", 40));
  revalidatePath("/admin");
}

export async function createOrder(form: FormData) {
  const c = await guard();
  const customer_name = s(form, "customer_name", 80);
  const garment = s(form, "garment", 120);
  if (!customer_name || !garment) return;
  for (let i = 0; i < 5; i++) {
    const code = `TZ-${randomInt(1000, 9999)}`;
    const { error } = await c.from("orders").insert({
      code,
      customer_name,
      garment,
      phone: s(form, "phone", 20) || null,
      due_date: s(form, "due_date", 10) || null,
      notes: s(form, "notes", 400) || null,
    });
    if (!error) break;
    if (!error.message.includes("duplicate")) throw new Error(error.message);
  }
  revalidatePath("/admin");
}

export async function setOrderStage(form: FormData) {
  const c = await guard();
  const stage = Math.max(0, Math.min(4, Number(s(form, "stage", 2))));
  await c.from("orders").update({ stage, updated_at: new Date().toISOString() }).eq("id", s(form, "id", 40));
  revalidatePath("/admin");
}

export async function setOrderNote(form: FormData) {
  const c = await guard();
  await c
    .from("orders")
    .update({ notes: s(form, "notes", 400) || null, due_date: s(form, "due_date", 10) || null, updated_at: new Date().toISOString() })
    .eq("id", s(form, "id", 40));
  revalidatePath("/admin");
}

// Marks an order ready and gives it the next One of One number.
export async function issueNumber(form: FormData) {
  const c = await guard();
  const id = s(form, "id", 40);
  const { data: order } = await c.from("orders").select("garment, register_no").eq("id", id).single();
  if (!order || order.register_no) return;
  const month = new Date().toLocaleDateString("en-IN", { month: "short", year: "numeric" });
  const { data: entry, error } = await c
    .from("register")
    .insert({ garment: order.garment, occasion: s(form, "occasion", 40) || "Bespoke", month, note: s(form, "note", 160) || null, public: form.get("public") === "on" })
    .select("no")
    .single();
  if (error || !entry) throw new Error(error?.message ?? "Could not add to the register");
  await c.from("orders").update({ register_no: entry.no, stage: 4, updated_at: new Date().toISOString() }).eq("id", id);
  revalidatePath("/admin");
  revalidatePath("/one-of-one");
}
