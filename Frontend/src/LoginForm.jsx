import React, { useState, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import { login } from './api';
import { UserContext } from './UserContext';

export default function LoginForm() {
  const [email, setEmail] = useState(''); 
  const [password, setPassword] = useState('');
  const { setToken } = useContext(UserContext);
  const nav = useNavigate();

  const handle = async e => {
    e.preventDefault();
    const data = await login({ email, password });
    setToken(data.access_token);
    nav('/');
  };

  return <form onSubmit={handle}>
    <input value={email} onChange={e => setEmail(e.target.value)} placeholder="Email" />
    <input type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Password" />
    <button>Login</button>
  </form>;
}
