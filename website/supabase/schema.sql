-- Tezoro Atelier database. Run once in the Supabase SQL editor (or apply as a migration).
-- RLS is enabled with no policies: only the server (service role key) can read or write.

create extension if not exists pgcrypto;

create table if not exists public.tezoro_bookings (
  id uuid primary key default gen_random_uuid(),
  ref text not null unique,
  purpose text not null,
  preferred_date date not null,
  slot text not null,
  name text not null,
  phone text not null,
  email text,
  wedding_date date,
  look_code text,
  fabric_id text,
  notes text,
  status text not null default 'new' check (status in ('new','confirmed','visited','cancelled')),
  created_at timestamptz not null default now()
);
create index if not exists tezoro_bookings_date_idx on public.tezoro_bookings (preferred_date);

create table if not exists public.tezoro_orders (
  id uuid primary key default gen_random_uuid(),
  code text not null unique,
  customer_name text not null,
  phone text,
  garment text not null,
  stage smallint not null default 0 check (stage between 0 and 4),
  due_date date,
  notes text,
  register_no integer,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists public.tezoro_register (
  no serial primary key,
  garment text not null,
  occasion text not null,
  month text not null,
  note text,
  public boolean not null default true,
  created_at timestamptz not null default now()
);

alter table public.tezoro_bookings enable row level security;
alter table public.tezoro_orders enable row level security;
alter table public.tezoro_register enable row level security;
