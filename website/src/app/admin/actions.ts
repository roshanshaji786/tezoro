"use server";
import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";
import { adminRpc } from "@/lib/db";
import { endSession, isAdmin, passwordMatches, startSession } from "@/lib/auth";

async function guard() {
  if (!(await isAdmin())) redirect("/admin");
}

const s = (f: FormData, k: string, max = 200) => String(f.get(k) ?? "").trim().slice(0, max);
const UUID = /^[0-9a-f-]{36}$/i;

export async function login(_: unknown, form: FormData) {
  if (!passwordMatches(s(form, "password", 200))) {
    await new Promise((r) => setTimeout(r, 800));
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
  await guard();
  const id = s(form, "id", 40);
  const status = s(form, "status", 20);
  if (!UUID.test(id) || !["new", "confirmed", "visited", "cancelled"].includes(status)) return;
  await adminRpc("set_booking_status", { id, status });
  revalidatePath("/admin");
}

export async function createOrder(form: FormData) {
  await guard();
  const customer_name = s(form, "customer_name", 80);
  const garment = s(form, "garment", 120);
  if (!customer_name || !garment) return;
  await adminRpc("create_order", {
    customer_name,
    garment,
    phone: s(form, "phone", 20),
    due_date: s(form, "due_date", 10),
    notes: s(form, "notes", 400),
  });
  revalidatePath("/admin");
}

export async function setOrderStage(form: FormData) {
  await guard();
  const id = s(form, "id", 40);
  if (!UUID.test(id)) return;
  await adminRpc("set_order_stage", { id, stage: Number(s(form, "stage", 2)) || 0 });
  revalidatePath("/admin");
}

export async function setOrderNote(form: FormData) {
  await guard();
  const id = s(form, "id", 40);
  if (!UUID.test(id)) return;
  await adminRpc("set_order_note", { id, notes: s(form, "notes", 400), due_date: s(form, "due_date", 10) });
  revalidatePath("/admin");
}

// Marks an order ready and gives it the next One of One number.
export async function issueNumber(form: FormData) {
  await guard();
  const id = s(form, "id", 40);
  if (!UUID.test(id)) return;
  await adminRpc("issue_number", { id, occasion: s(form, "occasion", 40), note: s(form, "note", 160), public: form.get("public") === "on" });
  revalidatePath("/admin");
  revalidatePath("/one-of-one");
}
