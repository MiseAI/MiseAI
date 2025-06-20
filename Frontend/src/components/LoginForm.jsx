import React, { useState } from 'react'
import { login } from '../api'

export default function LoginForm() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [message, setMessage] = useState('')

  const handleSubmit = async e => {
    e.preventDefault()
    try {
      const res = await login({ email, password })
      setMessage(`Logged in! Token: ${res.access_token}`)
    } catch (err) {
      setMessage('Login failed')
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <input value={email} onChange={e => setEmail(e.target.value)} placeholder="Email" />
      <input type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Password" />
      <button type="submit">Login</button>
      <div>{message}</div>
    </form>
  )
}
