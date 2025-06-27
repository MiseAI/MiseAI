import React from "react";
import HistoryExportButton from "../components/HistoryExportButton.jsx";

function ChatPage() {
  const filter = ""; // or set dynamically
  return (
    <div>
      <h1>Chat Page</h1>
      {/* Chat UI goes here */}
      <HistoryExportButton filter={filter} />
    </div>
  );
}

export default ChatPage;