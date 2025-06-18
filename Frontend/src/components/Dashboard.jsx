import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useAuth } from './AuthContext';

const Dashboard = () => {
  const { token } = useAuth();
  const [message, setMessage] = useState('');

  useEffect(() => {
    axios
      .get('/users/me', {
        baseURL: import.meta.env.VITE_API_BASE_URL,
        headers: { Authorization: `Bearer ${token}` },
      })
      .then(res => setMessage(`Welcome, ${res.data.username}`))
      .catch(err => console.error(err));
  }, [token]);

  return <div>{message || 'Loading...'}</div>;
};

export default Dashboard;
