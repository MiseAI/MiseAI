import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import RegisterForm from './RegisterForm';
import LoginForm from './LoginForm';

export default function Auth() {
  return (
    <div>
      <nav>
        <Link to="register">Register</Link> | <Link to="login">Login</Link>
      </nav>
      <Routes>
        <Route path="register" element={<RegisterForm />} />
        <Route path="login" element={<LoginForm />} />
      </Routes>
    </div>
  );
}