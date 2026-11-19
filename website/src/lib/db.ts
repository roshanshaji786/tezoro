import "server-only";
import { createClient, type SupabaseClient } from "@supabase/supabase-js";

// Database access goes only through Postgres functions (tezoro_*). The tables themselves have RLS on,
// no policies and no grants, so neither the browser nor the public key can read or write them directly.
// Staff actions also need TEZORO_DB_SECRET, which only this server knows.
let client: SupabaseClient | null | undefined;

export function db(): SupabaseClient | null {
  if (client !== undefined) return client;
  const url = process.env.SUPABASE_URL;
  const key = process.env.SUPABASE_PUBLISHABLE_KEY;
  client = url && key ? createClient(url, key, { auth: { persistSession: false, autoRefreshToken: false } }) : null;
  return client;
}

export const dbReady = () => db() !== null;

export async function adminRpc<T = unknown>(action: string, payload: Record<string, unknown> = {}): Promise<T> {
  const c = db();
  const secret = process.env.TEZORO_DB_SECRET;
  if (!c || !secret) throw new Error("Database is not connected");
  const { data, error } = await c.rpc("tezoro_admin", { p_secret: secret, p_action: action, p: payload });
  if (error) throw new Error(error.message);
  return data as T;
}

export type Booking = {
  id: string;
  ref: string;
  purpose: string;
  preferred_date: string;
  slot: string;
  name: string;
  phone: string;
  email: string | null;
  wedding_date: string | null;
  look_code: string | null;
  fabric_id: string | null;
  notes: string | null;
  status: "new" | "confirmed" | "visited" | "cancelled";
  created_at: string;
};

export type Order = {
  id?: string;
  code: string;
  customer_name: string;
  phone?: string | null;
  garment: string;
  stage: number;
  due_date: string | null;
  notes: string | null;
  register_no: number | null;
  updated_at: string;
};
