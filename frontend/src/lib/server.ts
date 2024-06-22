import { cookies } from "next/headers";

const isUserAuth = () => {
    const cookiesStore = cookies()
    return Boolean(cookiesStore.get("jwt")?.value) 
}

export default isUserAuth;