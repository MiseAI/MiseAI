import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import ChatPage from "./pages/ChatPage";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/chat" element={<ChatPage />} />
        {/* other routes */}
      </Routes>
    </BrowserRouter>
  );
}

export default App;