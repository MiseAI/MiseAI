import React, { useState, useContext } from 'react';
import { AuthContext } from '../../context/AuthContext';

const LoginForm = () => {
  const { login } = useContext(AuthContext);
  const [form, setForm] = useState({ email: '', password: '' });
  const [error, setError] = useState(null);

  const handleChange = e => setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      await login(form);
      // optionally redirect after login
    } catch (err) {
      setError(err.message || 'Login failed');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Login</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <label>Email:
        <input type="email" name="email" value={form.email} onChange={handleChange} required />
      </label>
      <label>Password:
        <input type="password" name="password" value={form.password} onChange={handleChange} required />
      </label>
      <button type="submit">Login</button>
    </form>
  );
};

export default LoginForm;
