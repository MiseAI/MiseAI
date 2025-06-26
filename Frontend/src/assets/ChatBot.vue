
<template>
  <div class="chat-container">
    <div class="messages">
      <MessageBubble
        v-for="(msg, index) in messages"
        :key="index"
        :role="msg.role"
        :text="msg.content"
      />
    </div>
    <form @submit.prevent="sendMessage">
      <input v-model="input" placeholder="Ask me anything..." />
      <button :disabled="loading">Send</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import MessageBubble from './MessageBubble.vue';

const input = ref('');
const messages = ref([]);
const loading = ref(false);

const sendMessage = async () => {
  if (!input.value.trim()) return;

  messages.value.push({ role: 'user', content: input.value });
  const query = input.value;
  input.value = '';
  loading.value = true;

  try {
    const res = await fetch('/api/ai/ask', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt: query })
    });
    const data = await res.json();
    messages.value.push({ role: 'assistant', content: data.response });
  } catch (err) {
    messages.value.push({ role: 'assistant', content: '⚠️ Error: Could not reach AI' });
  }

  loading.value = false;
};
</script>

<style scoped>
.chat-container {
  border: 1px solid #ccc;
  padding: 12px;
  border-radius: 10px;
  max-width: 600px;
  margin: auto;
}
.messages {
  max-height: 400px;
  overflow-y: auto;
  margin-bottom: 10px;
}
form {
  display: flex;
  gap: 8px;
}
input {
  flex: 1;
  padding: 10px;
}
button {
  padding: 10px 16px;
}
</style>
