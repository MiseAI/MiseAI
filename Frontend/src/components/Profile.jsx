import { useEffect, useState } from "react";
import axios from "axios";

export default function Profile() {
  const [user, setUser] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    const token = localStorage.getItem("access_token");
    if (!token) {
      setError("Not authenticated");
      return;
    }

    axios
      .get(\`\${import.meta.env.VITE_API_BASE_URL}/users/me\`, {
        headers: { Authorization: \`Bearer \${token}\` },
      })
      .then((res) => setUser(res.data))
      .catch((err) => {
        setError(err.response?.data?.detail || "Failed to fetch profile");
      });
  }, []);

  if (error) return <div className="error">{error}</div>;
  if (!user) return <div>Loading…</div>;

  return (
    <div>
      <h2>My Profile</h2>
      <p><strong>ID:</strong> {user.id}</p>
      <p><strong>Username:</strong> {user.username}</p>
      <p><strong>Email:</strong> {user.email}</p>
    </div>
  );
}
