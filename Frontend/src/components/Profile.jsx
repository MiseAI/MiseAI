import React, { useContext } from 'react';
import { AuthContext } from '../AuthContext';

export default function Profile() {
  const { user, logout } = useContext(AuthContext);
  if (!user) return <div>Loading…</div>;
  return (
    <div>
      <h2>Welcome, {user.username}!</h2>
      <p>Email: {user.email}</p>
      <button onClick={logout}>Log out</button>
    </div>
  );
}
