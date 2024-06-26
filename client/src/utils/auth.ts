export function fetchLogin(username: string, password: string) {
    try {
        let response = fetch('http://localhost:8000/user/login/', {
            method: 'POST',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({username, password})
        })
        return response
    } catch (error) {
        console.error('Error:', error)   
    }
}

export async function fetchRegister(username: string, password: string) {
    try {
        let response = await fetch('http://localhost:8000/user/create/', {
            method: 'POST',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({username, password})
        })
        return response
    } catch (error) {
        console.error('Error:', error)   
    }
}