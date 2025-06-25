import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/auth': 'https://miseai.up.railway.app',
      '/users': 'https://miseai.up.railway.app'
    }
  }
});
