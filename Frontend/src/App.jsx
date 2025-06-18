import { useState, useEffect } from 'react';
import axios from 'axios';

const API_BASE = import.meta.env.VITE_API_BASE_URL;

function App() {
  const [user, setUser] = useState(null);
  const token = localStorage.getItem("token");

  useEffect(() => {
    if (!token) return;
    axios.get(`${API_BASE}/users/me`, { headers: { Authorization: `Bearer ${token}` } })
      .then(res => setUser(res.data))
      .catch(() => setUser(null));
  }, [token]);

  if (!token) return <div>Please log in first</div>;
  if (!user) return <div>Loading profile…</div>;

  return (
    <div>
      <h1>Welcome, {user.username}!</h1>
      <p>Your email is: {user.email}</p>
    </div>
  );
}

export default App;
