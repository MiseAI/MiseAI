import React, { createContext, useState, useContext, useEffect } from 'react'
import axios from 'axios'

const AuthContext = createContext()
export const useAuth = () => useContext(AuthContext)

const BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

const AuthProvider = ({ children }) => {
  const [token, setToken] = useState(localStorage.getItem('token') || null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    setLoading(false)
  }, [])

  const login = async (email, password) => {
    const res = await axios.post(`${BASE_URL}/auth/login`, { email, password })
    setToken(res.data.access_token)
    localStorage.setItem('token', res.data.access_token)
  }

  const register = async (username, email, password) => {
    await axios.post(`${BASE_URL}/auth/register`, { username, email, password })
  }

  const logout = () => {
    setToken(null)
    localStorage.removeItem('token')
  }

  const axiosInstance = axios.create()
  axiosInstance.interceptors.request.use(config => {
    if (token) config.headers.Authorization = `Bearer ${token}`
    return config
  })

  return (
    <AuthContext.Provider value={{ token, login, register, logout, axios: axiosInstance, loading }}>
      {children}
    </AuthContext.Provider>
  )
}

export default AuthProvider
