
import React, { useState } from 'react';
import ChatHistory from './ChatHistory';
import { saveChatToLocal } from '../utils/chatHistory';

const ChatUI = () => {
    const [messages, setMessages] = useState([]);

    const handleSend = (msg) => {
        const updatedMessages = [...messages, { role: 'user', content: msg }];
        setMessages(updatedMessages);
        saveChatToLocal(Date.now(), updatedMessages);
    };

    return (
        <div>
            <ChatHistory onSelect={(chat) => setMessages(chat.data)} />
            <div>
                {messages.map((msg, idx) => (
                    <div key={idx}><b>{msg.role}:</b> {msg.content}</div>
                ))}
            </div>
            <button onClick={() => handleSend("Hello AI")}>Send</button>
        </div>
    );
};

export default ChatUI;
