import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { register } from './api';

export default function RegisterForm() {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState(''); 
  const [password, setPassword] = useState('');
  const nav = useNavigate();

  const handle = async e => {
    e.preventDefault();
    await register({ username, email, password });
    nav('/login');
  };

  return <form onSubmit={handle}>
    <input value={username} onChange={e => setUsername(e.target.value)} placeholder="Username" />
    <input value={email} onChange={e => setEmail(e.target.value)} placeholder="Email" />
    <input type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Password" />
    <button>Register</button>
  </form>;
}
