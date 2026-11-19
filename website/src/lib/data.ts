import "server-only";
import { db, type Order } from "./db";
import { demoRegister, type RegisterEntry } from "./content";

export async function getRegister(): Promise<{ entries: RegisterEntry[]; demo: boolean }> {
  const c = db();
  if (c) {
    const { data, error } = await c.rpc("tezoro_list_register");
    if (!error && data && data.length) return { entries: data as RegisterEntry[], demo: false };
  }
  return { entries: demoRegister, demo: true };
}

// A sample order so the tracker can be shown before the database is connected.
const DEMO_ORDER: Order = {
  code: "TZ-0147",
  customer_name: "Sample customer",
  garment: "Ivory brocade sherwani",
  stage: 2,
  due_date: new Date(Date.now() + 9 * 86_400_000).toISOString().slice(0, 10),
  notes: "First fitting booked. Hand embroidery on the collar in progress.",
  register_no: 147,
  updated_at: new Date().toISOString(),
};

export function normaliseCode(code: string) {
  return code.trim().toUpperCase().replace(/\s+/g, "");
}

export async function getOrderByCode(raw: string): Promise<{ order: Order | null; demo: boolean }> {
  const code = normaliseCode(raw);
  if (!/^TZ-[A-Z0-9]{3,8}$/.test(code)) return { order: null, demo: false };
  const c = db();
  if (c) {
    const { data } = await c.rpc("tezoro_get_order", { p_code: code });
    if (Array.isArray(data) && data[0]) return { order: data[0] as Order, demo: false };
  }
  if (code === DEMO_ORDER.code) return { order: DEMO_ORDER, demo: true };
  return { order: null, demo: false };
}
