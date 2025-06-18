// src/components/RegisterForm.jsx
import React, { useState } from 'react';
import { register } from '../api';

export default function RegisterForm() {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async e => {
    e.preventDefault();
    const result = await register({ username, email, password });
    console.log(result);
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Register</h2>
      <input type="text" placeholder="Username" value={username}
             onChange={e => setUsername(e.target.value)} required />
      <input type="email" placeholder="Email" value={email}
             onChange={e => setEmail(e.target.value)} required />
      <input type="password" placeholder="Password" value={password}
             onChange={e => setPassword(e.target.value)} required />
      <button type="submit">Register</button>
    </form>
  );
}
