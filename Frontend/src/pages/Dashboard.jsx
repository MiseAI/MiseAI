import { useState, useEffect } from 'react';
import api from '../api';

export default function Dashboard() {
  const [stats, setStats] = useState(null);

  useEffect(() => {
    api.get('/dashboard').then(res => setStats(res.data));
  }, []);

  return (
    <div>
      <h1 className="text-2xl mb-4">Profitability Dashboard</h1>
      {stats && <pre>{JSON.stringify(stats,null,2)}</pre>}
    </div>
);