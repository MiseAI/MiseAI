import React, { useState } from 'react';
import { register } from '../api';
import { useNavigate } from 'react-router-dom';

export default function RegisterForm() {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      await register({ username, email, password });
      navigate('/login');
    } catch (err) {
      console.error(err);
      alert('Registration failed');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Register</h2>
      <input type='text' value={username} onChange={e => setUsername(e.target.value)} placeholder='Username' required />
      <input type='email' value={email} onChange={e => setEmail(e.target.value)} placeholder='Email' required />
      <input type='password' value={password} onChange={e => setPassword(e.target.value)} placeholder='Password' required />
      <button type='submit'>Register</button>
    </form>
  );
}
