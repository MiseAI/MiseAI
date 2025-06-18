import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

export default function RegisterForm() {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      await axios.post('https://miseai-backend-production.up.railway.app/auth/register', { username, email, password });
      alert('Registration successful. Please login.');
      navigate('/login');
    } catch (err) {
      alert(err.response?.data?.detail || 'Registration failed');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Register</h2>
      <label>Username:</label>
      <input value={username} onChange={e => setUsername(e.target.value)} required />
      <label>Email:</label>
      <input type="email" value={email} onChange={e => setEmail(e.target.value)} required />
      <label>Password:</label>
      <input type="password" value={password} onChange={e => setPassword(e.target.value)} required />
      <button type="submit">Register</button>
    </form>
  );
}