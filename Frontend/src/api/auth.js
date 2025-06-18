import axios from 'axios';

const API_BASE = process.env.REACT_APP_API_BASE || '';

export const register = async data => {
  const res = await axios.post(`${API_BASE}/auth/register`, data);
  return res.data;
};

export const login = async data => {
  const res = await axios.post(`${API_BASE}/auth/login`, data);
  return res.data;
};
