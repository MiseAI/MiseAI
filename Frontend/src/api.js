import axios from 'axios';

const API_BASE = import.meta.env.VITE_API_BASE_URL;

export function register(data) {
  return axios.post(`${API_BASE}/auth/register`, data).then(res => res.data);
}

export function login(data) {
  return axios.post(`${API_BASE}/auth/login`, data).then(res => res.data);
}