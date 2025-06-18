import axios from 'axios';

const API_BASE = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

export const register = async ({ username, email, password }) => {
  const res = await axios.post(`${API_BASE}/auth/register`, { username, email, password });
  return res.data;
};

export const login = async ({ email, password }) => {
  const res = await axios.post(`${API_BASE}/auth/login`, { email, password });
  return res.data;
};