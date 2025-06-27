// src/pages/ChatPage.jsx
import React from "react";
import HistoryExportButton from "../components/HistoryExportButton";

const ChatPage = () => {
  // If you’re implementing a search bar, you could wire it here.
  // For now, we’ll leave filter as an empty string or some test value.
  const filter = "";

  return (
    <div style={{ padding: "2rem", fontFamily: "sans-serif" }}>
      <h1>Chat Page</h1>
      <p>This is your chat page content.</p>
      {/* Add your chat messages UI here */}

      {/* Export button */}
      <HistoryExportButton filter={filter} />
    </div>
  );
};

export default ChatPage;