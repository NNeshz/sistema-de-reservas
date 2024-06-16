"use server";

import { signIn } from "@/app/auth";

export async function authenticate(
  _currentState: unknown,
  username: string,
  password: string
) {
  try {
    let response = await signIn({ username, password });
    return response;
  } catch (error) {
    console.error(`Failed to authenticate: ${error}`);
  }
}
