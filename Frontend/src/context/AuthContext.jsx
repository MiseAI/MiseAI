import React, { createContext, useState, useEffect } from 'react';
import { login as loginApi, register as registerApi } from '../api/auth';

const AuthContext = createContext();

const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(localStorage.getItem('token'));

  useEffect(() => {
    if (token) {
      // Optionally decode token to get user info
      setUser({ token });
    }
  }, [token]);

  const login = async ({ email, password }) => {
    const { access_token } = await loginApi({ email, password });
    localStorage.setItem('token', access_token);
    setToken(access_token);
    setUser({ token: access_token });
  };

  const register = async ({ username, email, password }) => {
    await registerApi({ username, email, password });
  };

  const logout = () => {
    localStorage.removeItem('token');
    setToken(null);
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, token, login, register, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export { AuthContext, AuthProvider };
