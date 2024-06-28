import { LoginUserForm, RegisterUserForm, CartStore } from "@/utils/types";
import { create } from "zustand";

interface UserStore {
    username: string;
    email: string;
    isLoggedIn: boolean;
}

interface UserStoreActions {
    register: (values: RegisterUserForm) => Promise<void>;
    login: (values: LoginUserForm) => Promise<void>;
    logout: () => void;
    isLoggedWithCookie: (boolean: boolean) => void;
}

const useUserStore = create<UserStore & UserStoreActions & CartStore>((set, get) => ({
    username: "",
    email: "",
    isLoggedIn: false,
    products: [],

    isLoggedWithCookie: (boolean) => {
        set({ isLoggedIn: boolean })
    },
    register: async (values) => {
        try {
            const response = await fetch('http://localhost:8000/user/create/', {
                method: 'POST',
                credentials: 'include',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(values)
            })
            const data = await response.json()
            set({ username: data.username, email: data.email, isLoggedIn: true })
        } catch (error) {
            console.error('Error:', error)
        }
    },
    login: async (values) => {
        try {
            const response = await fetch('http://localhost:8000/user/login/', {
                method: 'POST',
                credentials: 'include',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(values)
            })
            const data = await response.json()
            set({ username: data.username, email: data.email, isLoggedIn: true })
        } catch (error) {
            console.error('Error:', error)
        }
    },
    logout: async () => {
        try {
            const response = await fetch('http://localhost:8000/user/logout/', {
                method: 'POST',
                credentials: 'include',
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            const data = await response.json()
            set({ username: "", email: "", isLoggedIn: false })
        } catch (error) {
            console.error('Error:', error)
        }
    },
    addProduct: (product) => {
        const isLogged = get().isLoggedIn
        if (!isLogged) {
            throw new Error('You need to be logged in to add products to the cart')
        }

        set((state) => {
            const products = [...state.products]
            const productIndex = products.findIndex((p) => p.id === product.id)
            if (productIndex === -1) {
                products.push({ ...product, quantity: 1 })
            } else {
                products[productIndex].quantity += 1
            }
            return { products }
        })        
    },
    removeProduct: (productId) => {

    }
}))

export default useUserStore;