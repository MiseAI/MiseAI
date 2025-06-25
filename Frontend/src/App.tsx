import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import ChatAssistant from './pages/ChatAssistant';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/assistant" element={<ChatAssistant />} />
      </Routes>
    </Router>
  );
}

export default App;