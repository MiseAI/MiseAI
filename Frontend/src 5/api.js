import axios from 'axios'

const API = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'
})

export function register(data) {
  return API.post('/auth/register', data).then(res => res.data)
}

export function login(data) {
  return API.post('/auth/login', data).then(res => res.data)
}
