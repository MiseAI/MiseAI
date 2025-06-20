import React, { useState } from 'react'
import { login } from '../api'

export default function LoginForm() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const handleSubmit = async e => {
    e.preventDefault()
    try {
      const res = await login({ email, password })
      alert('Logged in: ' + res.access_token)
    } catch (err) {
      alert(err.response?.data?.detail || 'Error')
    }
  }
  return (
    <form onSubmit={handleSubmit}>
      <input placeholder="Email" value={email} onChange={e=>setEmail(e.target.value)} />
      <input type="password" placeholder="Password" value={password} onChange={e=>setPassword(e.target.value)} />
      <button>Login</button>
    </form>
  )
}
