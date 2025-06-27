import React from "react";
import HistoryExportButton from "../components/HistoryExportButton";

function ChatPage() {
  const filter = ""; // or connect this to your search bar value!

  return (
    <div>
      <h1>My Chat Page</h1>
      {/* add your chat UI here */}
      <HistoryExportButton filter={filter} />
    </div>
  );
}

export default ChatPage;