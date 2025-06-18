import axios from 'axios';
const API_BASE = import.meta.env.VITE_API_BASE_URL;

export const register = (data) => axios.post(`${API_BASE}/auth/register`, data).then(r => r.data);
export const login = (data) => axios.post(`${API_BASE}/auth/login`, data).then(r => r.data);
