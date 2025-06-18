import React, { useState } from 'react';
import { register } from '../api';

export default function RegisterForm() {
  const [form, setForm] = useState({ username: '', email: '', password: '' });
  const [msg, setMsg] = useState('');

  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      const data = await register(form);
      setMsg(data.message);
    } catch (err) {
      setMsg(err.response?.data?.detail || 'Error');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Register</h2>
      <input name="username" placeholder="Username" onChange={handleChange} value={form.username} required />
      <input name="email" type="email" placeholder="Email" onChange={handleChange} value={form.email} required />
      <input name="password" type="password" placeholder="Password" onChange={handleChange} value={form.password} required />
      <button type="submit">Register</button>
      <p>{msg}</p>
    </form>
  );
}