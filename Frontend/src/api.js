import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
});

export function register(data) {
  return api.post('/auth/register', data).then(res => res.data);
}

export function login(data) {
  return api.post('/auth/login', data).then(res => res.data);
}
