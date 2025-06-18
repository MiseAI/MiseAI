import axios from 'axios';

const API = axios.create({
  baseURL: process.env.REACT_APP_API_BASE || 'https://miseai-backend-production.up.railway.app',
});

// these return Promises
export function register({ username, email, password }) {
  return API.post('/auth/register', { username, email, password });
}
export function login({ email, password }) {
  return API.post('/auth/login', { email, password });
}

export default API;
