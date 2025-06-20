import React, { useState } from 'react';
import { login } from '../api';

export default function LoginForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      const res = await login({ email, password });
      localStorage.setItem('access_token', res.access_token);
      setMessage('Login successful!');
    } catch (err) {
      setMessage(err.response?.data?.detail || 'Error');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Login</h2>
      <input placeholder="Email" type="email" value={email} onChange={e=>setEmail(e.target.value)} required />
      <input placeholder="Password" type="password" value={password} onChange={e=>setPassword(e.target.value)} required />
      <button type="submit">Login</button>
      <div>{message}</div>
    </form>
  );
}