import { cookies } from "next/headers";

const isUserAuth = () => {
    const cookiesStore = cookies()
    return cookiesStore.get("jwt")
}

export default isUserAuth;