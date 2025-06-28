import axios from 'axios';

const API_URL = import.meta.env.VITE_BACKEND_URL || 'http://localhost:8000';

export async function login(email, password) {
  const res = await axios.post(`${API_URL}/api/auth/login`, { email, password });
  return res.data;
}
