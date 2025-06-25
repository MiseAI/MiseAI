
<template>
  <div>
    <h2>Chat with AI</h2>
    <textarea v-model="userInput" placeholder="Type your message..." rows="4" cols="50"></textarea>
    <button @click="sendMessage">Send</button>
    <div v-if="response" class="response">
      <h3>Response:</h3>
      <p>{{ response }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const userInput = ref('')
const response = ref('')

async function sendMessage() {
  const res = await fetch('/api/ai', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message: userInput.value })
  })
  const data = await res.json()
  response.value = data.reply || 'No response.'
}
</script>

<style scoped>
.response {
  margin-top: 1em;
  padding: 1em;
  background-color: #f0f0f0;
}
</style>
