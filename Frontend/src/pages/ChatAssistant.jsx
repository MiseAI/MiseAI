import { useState } from 'react';
import api from '../api';

export default function ChatAssistant() {
  const [message, setMessage] = useState('');
  const [reply, setReply] = useState('');
  const sendChat = async () => {
    const { data } = await api.post('/ai/chat', { messages: [{ role: 'user', content: message }] });
    setReply(data.reply);
  };
  return (
    <div>
      <h1 className="text-2xl mb-4">AI Chat Assistant</h1>
      <textarea value={message} onChange={e => setMessage(e.target.value)} className="border p-2 w-full mb-2" rows={4}/>
      <button onClick={sendChat} className="px-4 py-2 bg-blue-600 text-white rounded">Send</button>
      {reply && <pre className="mt-4">{reply}</pre>}
    </div>
);