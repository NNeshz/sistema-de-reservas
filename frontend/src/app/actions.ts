import { register, login } from "./auth";

export async function actionRegister(
  _currentState: unknown,
  username: string,
  password: string
) {
  try {
    let response = await register({ username, password });
    return response;
  } catch (error) {
    console.error(`Failed to register: ${error}`);
  }
}

export async function actionLogin(
  _currentState: unknown,
  username: string,
  password: string
) {
  try {
    let response = await login({ username, password });
    return response;
  } catch (error) {
    console.error(`Failed to register: ${error}`);
  }
}