import axios from 'axios';

const API = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL
});

export function register(data) {
  return API.post('/auth/register', data).then(res => res.data);
}

export function login(data) {
  return API.post('/auth/login', data).then(res => res.data);
}

export function getProfile(token) {
  return API.get('/users/me', {
    headers: { Authorization: `Bearer ${token}` }
  }).then(res => res.data);
}
