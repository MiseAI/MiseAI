
<template>
  <div :class="['message', role]">
    <div class="bubble">{{ text }}</div>
  </div>
</template>

<script setup>
defineProps({
  role: String, // 'user' or 'assistant'
  text: String
});
</script>

<style scoped>
.message {
  display: flex;
  margin: 5px 0;
}
.message.user {
  justify-content: flex-end;
}
.message.assistant {
  justify-content: flex-start;
}
.bubble {
  max-width: 70%;
  padding: 10px;
  border-radius: 12px;
  background-color: #eee;
}
.user .bubble {
  background-color: #cce4ff;
}
.assistant .bubble {
  background-color: #f1f1f1;
}
</style>
