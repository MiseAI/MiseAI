import { useState } from 'react';
import { postJson } from '../../api/config';

export default function Login({ onLogin }) {
  const [form, setForm] = useState({ email: '', password: '' });
  const [err, setErr] = useState(null);

  const handleChange = e => {
    setForm(f => ({ ...f, [e.target.name]: e.target.value }));
  };

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      const { access_token } = await postJson('/auth/login', form);
      onLogin(access_token);
    } catch (err) {
      setErr(err.message);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Login</h2>
      <input name="email"    value={form.email}    onChange={handleChange} placeholder="Email" />
      <input name="password" type="password" value={form.password} onChange={handleChange} placeholder="Password" />
      <button type="submit">Log In</button>
      {err && <p style={{ color: 'red' }}>{err}</p>}
    </form>
  );
}
