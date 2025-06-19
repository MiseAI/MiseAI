import React, { useState } from 'react';
import { login } from '../api';

export default function LoginForm() {
  const [form, setForm] = useState({ email: '', password: '' });
  const [msg, setMsg] = useState('');

  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      const res = await login(form);
      setMsg('Logged in! Token: ' + res.access_token);
    } catch (err) {
      setMsg(err.response?.data?.detail || 'Error');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Login</h2>
      <input name="email" placeholder="Email" onChange={handleChange} />
      <input name="password" type="password" placeholder="Password" onChange={handleChange} />
      <button type="submit">Login</button>
      {msg && <p>{msg}</p>}
    </form>
  );
}
