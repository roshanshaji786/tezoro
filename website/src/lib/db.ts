import "server-only";
import { createClient, type SupabaseClient } from "@supabase/supabase-js";

// All database access happens on the server with the service role key.
// Row level security is on and has no public policies, so the browser can never read client data.
let client: SupabaseClient | null | undefined;

export function db(): SupabaseClient | null {
  if (client !== undefined) return client;
  const url = process.env.SUPABASE_URL;
  const key = process.env.SUPABASE_SERVICE_ROLE_KEY;
  client = url && key ? createClient(url, key, { auth: { persistSession: false } }) : null;
  return client;
}

export const dbReady = () => db() !== null;

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
  id: string;
  code: string;
  customer_name: string;
  phone: string | null;
  garment: string;
  stage: number;
  due_date: string | null;
  notes: string | null;
  register_no: number | null;
  created_at: string;
  updated_at: string;
};
