"use client";
import { useActionState } from "react";
import { login } from "./actions";

export function LoginForm() {
  const [state, action, pending] = useActionState(login, null);
  return (
    <form action={action} className="mt-8 space-y-4">
      <label className="block">
        <span className="eyebrow text-[0.6rem] text-stone">Staff password</span>
        <input name="password" type="password" required autoComplete="current-password" className="field mt-2" />
      </label>
      {state?.error && <p className="text-sm text-maroon">{state.error}</p>}
      <button disabled={pending} className="btn btn-navy w-full">
        {pending ? "Checking…" : "Sign in"}
      </button>
    </form>
  );
}
