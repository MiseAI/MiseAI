import React, { useContext } from 'react';
import { AuthContext } from '../../context/AuthContext';
import { Redirect } from 'react-router-dom';

const AuthGuard = ({ children }) => {
  const { user } = useContext(AuthContext);
  if (!user) {
    return <Redirect to="/login" />;
  }
  return <>{children}</>;
};

export default AuthGuard;
