import axios from 'axios'

const BASE = import.meta.env.VITE_API_BASE_URL

export function register(data) {
  return axios.post(`${BASE}/auth/register`, data).then(r => r.data)
}

export function login(data) {
  return axios.post(`${BASE}/auth/login`, data).then(r => r.data)
}
