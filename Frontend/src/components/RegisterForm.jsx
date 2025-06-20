import React, { useState } from 'react';
import { register } from '../api';

export default function RegisterForm() {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      const res = await register({ username, email, password });
      setMessage(res.message);
    } catch (err) {
      setMessage(err.response?.data?.detail || 'Error');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Register</h2>
      <input placeholder="Username" value={username} onChange={e=>setUsername(e.target.value)} required />
      <input placeholder="Email" type="email" value={email} onChange={e=>setEmail(e.target.value)} required />
      <input placeholder="Password" type="password" value={password} onChange={e=>setPassword(e.target.value)} required />
      <button type="submit">Register</button>
      <div>{message}</div>
    </form>
  );
}