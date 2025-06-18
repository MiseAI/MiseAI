import React, { useContext } from 'react';
import { Navigate } from 'react-router-dom';
import { UserContext } from './UserContext';

export default function PrivateRoute({ children }) {
  const { token } = useContext(UserContext);
  return token ? children : <Navigate to="/login" />;
}
