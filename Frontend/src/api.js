import axios from 'axios';

const BASE = import.meta.env.VITE_API_BASE_URL;

export async function register(data) {
  return axios.post(`${BASE}/auth/register`, data);
}

export async function login(data) {
  const res = await axios.post(`${BASE}/auth/login`, data);
  const token = res.data.access_token;
  localStorage.setItem('jwt', token);
  return token;
}

export function getMe() {
  const token = localStorage.getItem('jwt');
  return axios.get(`${BASE}/users/me`, {
    headers: { Authorization: `Bearer ${token}` }
  });
}
