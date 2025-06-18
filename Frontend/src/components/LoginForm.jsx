import React, { useState } from 'react'
import axios from 'axios'

const BASE_URL = import.meta.env.VITE_API_BASE_URL

export default function LoginForm() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [message, setMessage] = useState(null)

  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      const res = await axios.post(`${BASE_URL}/auth/login`, { email, password })
      setMessage(res.data.message || 'Login successful')
      // TODO: Store token: res.data.access_token
    } catch (err) {
      setMessage(err.response?.data?.detail || 'Login failed')
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <h2>Login</h2>
      <div>
        <label>Email:</label>
        <input type="email" value={email} onChange={e => setEmail(e.target.value)} required />
      </div>
      <div>
        <label>Password:</label>
        <input type="password" value={password} onChange={e => setPassword(e.target.value)} required />
      </div>
      <button type="submit">Login</button>
      {message && <p>{message}</p>}
    </form>
  )
}
