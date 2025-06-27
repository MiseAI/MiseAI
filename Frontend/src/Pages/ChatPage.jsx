import React from "react";
import HistoryExportButton from "../components/HistoryExportButton";

const ChatPage = () => {
  const filter = ""; // you can link this to a search bar later

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Mise AI Chat</h1>
      {/* Chat UI here */}
      <HistoryExportButton filter={filter} />
    </div>
  );
};

export default ChatPage;
