import { useState } from 'react';
import Register from './components/auth/Register';
import Login    from './components/auth/Login';

export default function App() {
  const [token, setToken] = useState(localStorage.getItem('token'));

  const handleLogin = tok => {
    localStorage.setItem('token', tok);
    setToken(tok);
  };

  return (
    <div>
      {!token ? (
        <>
          <Register />
          <Login onLogin={handleLogin}/>
        </>
      ) : (
        <p>🎉 You’re logged in! Token: {token}</p>
      )}
    </div>
  );
}
