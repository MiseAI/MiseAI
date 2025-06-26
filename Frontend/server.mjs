
import { createServer } from 'vite'

createServer({
  root: '.',
  server: {
    host: '0.0.0.0',
    port: process.env.PORT || 3000
  }
}).then(server => {
  server.listen()
})
