import React, { useState } from 'react';
import { login } from '../api';
import { useNavigate } from 'react-router-dom';

export default function LoginForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      const { access_token } = await login({ email, password });
      localStorage.setItem('token', access_token);
      navigate('/profile');
    } catch (err) {
      console.error(err);
      alert('Login failed');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Login</h2>
      <input type='email' value={email} onChange={e => setEmail(e.target.value)} placeholder='Email' required />
      <input type='password' value={password} onChange={e => setPassword(e.target.value)} placeholder='Password' required />
      <button type='submit'>Login</button>
    </form>
  );
}
