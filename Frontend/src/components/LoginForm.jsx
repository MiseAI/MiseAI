// src/components/LoginForm.jsx
import React, { useState } from 'react';
import { login } from '../api';

export default function LoginForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async e => {
    e.preventDefault();
    const result = await login({ email, password });
    console.log(result);
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Login</h2>
      <input type="email" placeholder="Email" value={email}
             onChange={e => setEmail(e.target.value)} required />
      <input type="password" placeholder="Password" value={password}
             onChange={e => setPassword(e.target.value)} required />
      <button type="submit">Login</button>
    </form>
  );
}
