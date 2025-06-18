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
      const data = await login(form);
      setMsg(data.access_token || data.message);
    } catch (err) {
      setMsg(err.response?.data?.detail || 'Error');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Login</h2>
      <input name="email" type="email" placeholder="Email" onChange={handleChange} value={form.email} required />
      <input name="password" type="password" placeholder="Password" onChange={handleChange} value={form.password} required />
      <button type="submit">Login</button>
      <p>{msg}</p>
    </form>
  );
}