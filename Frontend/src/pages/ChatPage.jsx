import React, { useState } from "react";

export default function ChatPage() {
  const [message, setMessage] = useState("");
  const [reply, setReply] = useState("");

  const sendMessage = async () => {
    const res = await fetch(
      "https://miseai.up.railway.app/api/chat",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message }),
      }
    );

    const data = await res.json();
    setReply(data.reply);
  };

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">Chat Page</h1>

      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        className="border px-2 py-1"
        placeholder="Type your message..."
      />

      <button
        onClick={sendMessage}
        className="bg-blue-500 text-white px-4 py-1 ml-2 rounded"
      >
        Send
      </button>

      {reply && (
        <div className="mt-4">
          <strong>Server replied:</strong> {reply}
        </div>
      )}
    </div>
  );
}