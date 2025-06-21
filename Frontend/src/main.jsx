import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import { API } from './api';

// Rehydration for cookie-based auth isn't needed since cookies are sent automatically

ReactDOM.createRoot(document.getElementById('root')).render(<App />);