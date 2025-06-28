import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export async function signup(email, password) {
  const response = await axios.post(`${API_BASE_URL}/api/auth/signup`, {
    email,
    password,
  });
  return response.data;
}

export async function login(email, password) {
  const response = await axios.post(`${API_BASE_URL}/api/auth/login`, {
    email,
    password,
  });
  return response.data;
}
