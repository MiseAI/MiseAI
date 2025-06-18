// src/components/auth.js
import React from 'react';
import LoginForm from './LoginForm';
import RegisterForm from './RegisterForm';

export default function Auth() {
  return (
    <div>
      <h1>Authentication</h1>
      <RegisterForm />
      <LoginForm />
    </div>
  );
}
