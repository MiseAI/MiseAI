// vite.config.js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    watch: {
      // Prevent endless restarts by ignoring generated files
      ignored: ['**/node_modules/**', '**/dist/**']
    }
  }
})