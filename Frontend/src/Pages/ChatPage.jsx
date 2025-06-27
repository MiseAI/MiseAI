import HistoryExportButton from "../components/HistoryExportButton";

function ChatPage() {
  const filter = ""; // eventually connected to a search bar
  return (
    <div>
      <h1>MiseAI Chat Page</h1>
      {/* Chat UI would go here */}
      <HistoryExportButton filter={filter} />
    </div>
  );
}

export default ChatPage;