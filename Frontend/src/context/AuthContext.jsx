import React, { createContext, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import * as authService from '../services/auth';

const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [token, setToken] = useState(() => localStorage.getItem('token'));
  const navigate = useNavigate();

  async function login({ email, password }) {
    const res = await authService.login({ email, password });
    const jwt = res.data.access_token;
    localStorage.setItem('token', jwt);
    setToken(jwt);
    navigate('/dashboard');
  }

  async function register(creds) {
    await authService.register(creds);
    navigate('/login');
  }

  function logout() {
    localStorage.removeItem('token');
    setToken(null);
    navigate('/login');
  }

  return (
    <AuthContext.Provider value={{ token, login, register, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  return React.useContext(AuthContext);
}
