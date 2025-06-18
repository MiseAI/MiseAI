import React from 'react';
import ReactDOM from 'react-dom/client';
import LoginForm from './components/LoginForm';
import RegisterForm from './components/RegisterForm';

function App() {
  return (
    <div>
      <h1>MiseAI</h1>
      <RegisterForm />
      <LoginForm />
    </div>
  );
}

ReactDOM.createRoot(document.getElementById('root')).render(<App />);
