import axios from 'axios';

const API_BASE = import.meta.env.VITE_API_BASE || 'https://miseai-backend-production.up.railway.app';

export function register({ username, email, password }) {
  return axios.post(`${API_BASE}/auth/register`, { username, email, password });
}

export function login({ email, password }) {
  return axios.post(`${API_BASE}/auth/login`, { email, password });
}
