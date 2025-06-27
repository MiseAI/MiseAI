import React from "react";
import dayjs from "dayjs";

export default function ChatMessage({ message, isUser }) {
  const time = dayjs(message.timestamp || new Date()).format("HH:mm");

  return (
    <div className={`w-full my-2 flex ${isUser ? "justify-end" : "justify-start"}`}>
      <div
        className={`max-w-xs px-4 py-2 rounded-lg shadow-md ${
          isUser ? "bg-blue-600 text-white" : "bg-gray-200 text-black"
        }`}
      >
        <p className="whitespace-pre-wrap">{message.text}</p>
        <span className="block text-xs text-right mt-1 opacity-60">{time}</span>
      </div>
    </div>
  );
}
