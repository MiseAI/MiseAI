import React from 'react';
import RegisterForm from './components/RegisterForm';
import LoginForm from './components/LoginForm';

export default function App() {
  return (
    <div style={{ maxWidth: 400, margin: 'auto', padding: 20 }}>
      <h1>Welcome to MiseAI</h1>
      <RegisterForm />
      <hr />
      <LoginForm />
    </div>
  );
}