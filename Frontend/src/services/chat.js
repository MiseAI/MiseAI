import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export async function sendMessage(message, token) {
  const res = await axios.post(
    `${API_BASE_URL}/api/chat`,
    { message },
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );
  return res.data;
}
