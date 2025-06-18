import { useState } from "react";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await fetch(
      `${import.meta.env.VITE_API_BASE}/auth/login`,
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      }
    );

    if (res.ok) {
      const data = await res.json();
      setMessage(`✅ Success: ${JSON.stringify(data)}`);
    } else {
      const err = await res.json();
      setMessage(`❌ Error: ${err.detail || JSON.stringify(err)}`);
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ maxWidth: 320, margin: "auto" }}>
      <h2>Login</h2>
      <label>
        Email
        <br />
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
      </label>
      <br />
      <label>
        Password
        <br />
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
      </label>
      <br />
      <br />
      <button type="submit">Log In</button>
      {message && (
        <p style={{ whiteSpace: "pre-wrap", marginTop: 16 }}>{message}</p>
      )}
    </form>
); }
