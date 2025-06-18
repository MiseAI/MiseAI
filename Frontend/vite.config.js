// vite.config.js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    watch: {
      // don’t watch dependencies or your dist folder for changes
      ignored: ['**/node_modules/**', '**/dist/**']
    }
  }
})