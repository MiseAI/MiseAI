export async function register(data) {
  const resp = await fetch(`${import.meta.env.VITE_API_BASE_URL}/auth/register`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  })
  return resp.json()
}

export async function login(data) {
  const resp = await fetch(`${import.meta.env.VITE_API_BASE_URL}/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  })
  return resp.json()
}

export async function fetchMe(token) {
  const resp = await fetch(`${import.meta.env.VITE_API_BASE_URL}/users/me`, {
    headers: { 'Authorization': `Bearer ${token}` },
  })
  return resp.json()
}
