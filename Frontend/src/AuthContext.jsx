import React, { createContext, useState, useEffect } from 'react';
import { getMe, login as apiLogin } from './api';

export const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const token = localStorage.getItem('jwt');
    if (token) {
      getMe().then(res => setUser(res.data)).catch(() => localStorage.removeItem('jwt'));
    }
  }, []);

  const login = async (creds) => {
    const token = await apiLogin(creds);
    const profile = await getMe();
    setUser(profile.data);
  };

  const logout = () => {
    localStorage.removeItem('jwt');
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}
