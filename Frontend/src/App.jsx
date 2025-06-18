import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { UserProvider } from './UserContext';
import PrivateRoute from './PrivateRoute';
import LoginForm from './LoginForm';
import RegisterForm from './RegisterForm';

export default function App() {
  return (
    <UserProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/login" element={<LoginForm />} />
          <Route path="/register" element={<RegisterForm />} />
          <Route path="/" element={<PrivateRoute><h1>Welcome!</h1></PrivateRoute>} />
        </Routes>
      </BrowserRouter>
    </UserProvider>
  );
}
