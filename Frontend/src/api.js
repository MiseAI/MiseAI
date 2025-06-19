import axios from 'axios';

const base = import.meta.env.VITE_API_BASE_URL;

export function register(data) {
  return axios.post(`${base}/auth/register`, data).then(res => res.data);
}

export function login(data) {
  return axios.post(`${base}/auth/login`, data).then(res => res.data);
}
