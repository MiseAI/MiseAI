import React, { createContext, useContext, useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [token, setToken] = useState(localStorage.getItem('token'));
  const navigate = useNavigate();

  const login = async (email, password) => {
    const response = await axios.post(\`\${process.env.REACT_APP_API_BASE_URL}/auth/login\`, { email, password });
    localStorage.setItem('token', response.data.access_token);
    setToken(response.data.access_token);
    navigate('/dashboard');
  };

  const register = async (username, email, password) => {
    await axios.post(\`\${process.env.REACT_APP_API_BASE_URL}/auth/register\`, { username, email, password });
    navigate('/login');
  };

  const logout = () => {
    localStorage.removeItem('token');
    setToken(null);
    navigate('/login');
  };

  return (
    <AuthContext.Provider value={{ token, login, register, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  return useContext(AuthContext);
}

export function ProtectedRoute({ children }) {
  const { token } = useAuth();
  if (!token) {
    return <Navigate to="/login" />;
  }
  return children;
}
