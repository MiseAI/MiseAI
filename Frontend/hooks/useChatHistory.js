import { useState, useEffect } from 'react';

export function useChatHistory(initialChats = []) {
  const [allChats, setAllChats] = useState(initialChats);
  const [query, setQuery] = useState('');
  const [filteredChats, setFilteredChats] = useState(initialChats);

  useEffect(() => {
    const q = query.toLowerCase();
    const filtered = allChats.filter(chat =>
      chat.message.toLowerCase().includes(q)
    );
    setFilteredChats(filtered);
  }, [query, allChats]);

  return { query, setQuery, filteredChats };
}
