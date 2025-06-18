import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
});

export function register({ username, email, password }) {
  return api.post('/auth/register', { username, email, password });
}

export function login({ email, password }) {
  return api.post('/auth/login', { email, password });
}
