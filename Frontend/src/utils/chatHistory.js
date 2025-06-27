
export const saveChatToLocal = (chatId, data) => {
    localStorage.setItem(`chat_${chatId}`, JSON.stringify(data));
};

export const loadChatFromLocal = (chatId) => {
    const data = localStorage.getItem(`chat_${chatId}`);
    return data ? JSON.parse(data) : null;
};

export const getAllSavedChats = () => {
    return Object.keys(localStorage)
        .filter(key => key.startsWith("chat_"))
        .map(key => ({ id: key, data: JSON.parse(localStorage.getItem(key)) }));
};
