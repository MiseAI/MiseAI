import { useEffect, useRef, useState } from 'react';

export default function ChatView() {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const chatEndRef = useRef(null);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const sendMessage = async (message) => {
    setLoading(true);
    const newMessages = [...messages, { sender: 'user', text: message }];
    setMessages(newMessages);

    const response = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ messages: newMessages, user_id: 'demo', org_id: 'miseai' })
    });

    const reader = response.body.getReader();
    let decoder = new TextDecoder();
    let aiMessage = '';
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      aiMessage += decoder.decode(value);
      setMessages([...newMessages, { sender: 'ai', text: aiMessage }]);
    }
    setLoading(false);
  };

  return (
    <div>
      <div className="chat">
        {messages.map((msg, idx) => (
          <div key={idx} className={msg.sender}>
            {msg.text}
          </div>
        ))}
        {loading && <div className="ai">MiseAI is typing...</div>}
        <div ref={chatEndRef} />
      </div>
      {/* Add input component here */}
    </div>
  );
}
