
<template>
  <div class="chat-container">
    <div class="chat-thread" ref="chatThread">
      <div v-for="(msg, index) in messages" :key="index" :class="['message', msg.sender]">
        <p>{{ msg.text }}</p>
      </div>
    </div>
    <div class="chat-input">
      <input v-model="userInput" @keyup.enter="sendMessage" placeholder="Ask me anything..." />
      <button @click="sendMessage">Send</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userInput: "",
      messages: [],
      loading: false,
    };
  },
  methods: {
    async sendMessage() {
      if (!this.userInput.trim()) return;
      const userMessage = { text: this.userInput, sender: "user" };
      this.messages.push(userMessage);
      this.userInput = "";
      this.loading = true;

      try {
        const response = await fetch("/ai/assistant", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ message: userMessage.text }),
        });
        const data = await response.json();
        this.messages.push({ text: data.response || "No reply", sender: "bot" });
      } catch (error) {
        this.messages.push({ text: "Error talking to assistant.", sender: "bot" });
      } finally {
        this.loading = false;
        this.$nextTick(() => {
          const el = this.$refs.chatThread;
          el.scrollTop = el.scrollHeight;
        });
      }
    },
  },
};
</script>

<style scoped>
.chat-container {
  display: flex;
  flex-direction: column;
  height: 100%;
}
.chat-thread {
  flex: 1;
  overflow-y: auto;
  padding: 1rem;
  background: #f5f5f5;
}
.message {
  margin: 0.5rem 0;
  max-width: 75%;
}
.message.user {
  align-self: flex-end;
  background: #dcf8c6;
  padding: 0.5rem;
  border-radius: 0.5rem;
}
.message.bot {
  align-self: flex-start;
  background: #fff;
  padding: 0.5rem;
  border-radius: 0.5rem;
}
.chat-input {
  display: flex;
  border-top: 1px solid #ccc;
}
.chat-input input {
  flex: 1;
  padding: 0.5rem;
}
.chat-input button {
  padding: 0.5rem 1rem;
}
</style>
