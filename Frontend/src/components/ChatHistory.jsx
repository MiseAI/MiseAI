
import React, { useEffect, useState } from 'react';
import { getAllSavedChats } from '../utils/chatHistory';

const ChatHistory = ({ onSelect }) => {
    const [chats, setChats] = useState([]);

    useEffect(() => {
        setChats(getAllSavedChats());
    }, []);

    return (
        <div>
            <h2>Previous Chats</h2>
            <ul>
                {chats.map((chat, index) => (
                    <li key={index} onClick={() => onSelect(chat)}>
                        Chat ID: {chat.id}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ChatHistory;
