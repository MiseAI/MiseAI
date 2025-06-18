import { useState } from 'react';
import { postJson } from '../../api/config';

export default function Register() {
  const [form, setForm] = useState({ username: '', email: '', password: '' });
  const [msg, setMsg] = useState(null);

  const handleChange = e => {
    setForm(f => ({ ...f, [e.target.name]: e.target.value }));
  };

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      const { message } = await postJson('/auth/register', form);
      setMsg(message);
    } catch (err) {
      setMsg(err.message);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Register</h2>
      <input name="username" value={form.username} onChange={handleChange} placeholder="Username" />
      <input name="email"    value={form.email}    onChange={handleChange} placeholder="Email" />
      <input name="password" type="password" value={form.password} onChange={handleChange} placeholder="Password" />
      <button type="submit">Sign Up</button>
      {msg && <p>{msg}</p>}
    </form>
  );
}
