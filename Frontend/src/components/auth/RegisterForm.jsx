import React, { useState, useContext } from 'react';
import { AuthContext } from '../../context/AuthContext';

const RegisterForm = () => {
  const { register } = useContext(AuthContext);
  const [form, setForm] = useState({ username: '', email: '', password: '' });
  const [error, setError] = useState(null);

  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      await register(form);
      // optionally redirect after register
    } catch (err) {
      setError(err.message || 'Registration failed');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Register</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <label>Username:
        <input type="text" name="username" value={form.username} onChange={handleChange} required />
      </label>
      <label>Email:
        <input type="email" name="email" value={form.email} onChange={handleChange} required />
      </label>
      <label>Password:
        <input type="password" name="password" value={form.password} onChange={handleChange} required />
      </label>
      <button type="submit">Register</button>
    </form>
  );
};

export default RegisterForm;
