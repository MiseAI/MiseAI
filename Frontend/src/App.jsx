import React, { useState } from 'react';
import LoginForm from './components/LoginForm';
import RegisterForm from './components/RegisterForm';

export default function App() {
  const [view, setView] = useState('login');
  return (
    <div style={{ maxWidth: 400, margin: '2rem auto', padding: '1rem', border: '1px solid #ccc' }}>
      {view === 'login' ? <LoginForm /> : <RegisterForm />}
      <button onClick={() => setView(view === 'login' ? 'register' : 'login')}>
        {view === 'login' ? 'Go to Register' : 'Go to Login'}
      </button>
    </div>
  );
}
