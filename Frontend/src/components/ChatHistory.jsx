import React from 'react';
import ChatMessage from './ChatMessage';
import SearchBar from './SearchBar';
import { useChatHistory } from '../hooks/useChatHistory';

export default function ChatHistory({ chats }) {
  const { query, setQuery, filteredChats } = useChatHistory(chats);

  return (
    <div className="w-full">
      <SearchBar query={query} setQuery={setQuery} />
      <div className="space-y-2 max-h-[500px] overflow-y-auto">
        {filteredChats.map((chat, idx) => (
          <ChatMessage key={idx} {...chat} />
        ))}
      </div>
    </div>
  );
}
