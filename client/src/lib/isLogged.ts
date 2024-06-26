import { cookies } from "next/headers";

export const isUserAuthenticated = () => {
    const cookiesStore = cookies();
    return Boolean(cookiesStore.get("jwt")?.value);
}