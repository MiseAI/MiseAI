import React, { useState } from 'react'
import axios from 'axios'

const BASE_URL = import.meta.env.VITE_API_BASE_URL

export default function RegisterForm() {
  const [username, setUsername] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [message, setMessage] = useState(null)

  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      const res = await axios.post(`${BASE_URL}/auth/register`, { username, email, password })
      setMessage(res.data.message)
    } catch (err) {
      setMessage(err.response?.data?.detail || 'Registration failed')
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <h2>Register</h2>
      <div>
        <label>Username:</label>
        <input type="text" value={username} onChange={e => setUsername(e.target.value)} required />
      </div>
      <div>
        <label>Email:</label>
        <input type="email" value={email} onChange={e => setEmail(e.target.value)} required />
      </div>
      <div>
        <label>Password:</label>
        <input type="password" value={password} onChange={e => setPassword(e.target.value)} required />
      </div>
      <button type="submit">Register</button>
      {message && <p>{message}</p>}
    </form>
  )
}
