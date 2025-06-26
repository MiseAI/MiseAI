import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import Forecasting from "./pages/Forecasting";
import Assistant from "./pages/Assistant";

function App() {
  return (
    <div className="App">
      <main>
        <Router>
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/forecasting" element={<Forecasting />} />
            <Route path="/assistant" element={<Assistant />} />
          </Routes>
        </Router>
      </main>
    </div>
  );
}

export default App;
