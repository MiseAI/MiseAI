// src/api.js
import axios from 'axios';

const API_BASE = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

export const client = axios.create({
  baseURL: API_BASE,
  withCredentials: true,    // if you plan to use cookies
});

// then your calls
export function register(data) {
  return client.post('/auth/register', data).then(r => r.data);
}
export function login(data) {
  return client.post('/auth/login', data).then(r => r.data);
}