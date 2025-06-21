import axios from 'axios';

export const API = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  withCredentials: true, // include HttpOnly cookies
});

// Example usage:
// Login
export async function login({ email, password }) {
  const { data } = await API.post('/auth/login', { email, password });
  return data;
}

// Logout
export async function logout() {
  const { data } = await API.post('/auth/logout');
  return data;
}

// Fetch protected
export async function getCurrentUser() {
  const { data } = await API.get('/users/me');
  return data;
}
