import React, { useEffect, useState } from 'react'
import { useAuth } from '../context/AuthContext'

const Dashboard = () => {
  const { axios, logout } = useAuth()
  const [data, setData] = useState(null)

  useEffect(() => {
    axios.get('/dashboard-data').then(res => setData(res.data))
  }, [])

  return (
    <div>
      <h2>Dashboard</h2>
      <button onClick={logout}>Logout</button>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  )
}

export default Dashboard
