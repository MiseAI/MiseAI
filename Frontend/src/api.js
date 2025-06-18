import axios from 'axios';

const baseURL = import.meta.env.VITE_API_BASE_URL;

export const register = (data) =>
  axios.post(`${baseURL}/auth/register`, data).then(res => res.data);

export const login = (data) =>
  axios.post(`${baseURL}/auth/login`, data).then(res => res.data);
