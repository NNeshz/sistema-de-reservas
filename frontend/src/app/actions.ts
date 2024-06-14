"use server";

import { signIn } from "@/app/auth";

export async function authenticate(
  _currentState: unknown,
  username: string,
  password: string
) {
  try {
    await signIn({ username, password });
  } catch (error) {
    console.error(`Failed to authenticate: ${error}`);
  }
}
