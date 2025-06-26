import { useState, useEffect } from 'react';
import api from '../api';

export default function ForecastTool() {
  const [forecast, setForecast] = useState(null);
  useEffect(() => { api.get('/forecast/next-week').then(res => setForecast(res.data)); }, []);
  return (
    <div>
      <h1 className="text-2xl mb-4">Weekly Forecast</h1>
      {forecast && <pre>{JSON.stringify(forecast,null,2)}</pre>}
    </div>
);