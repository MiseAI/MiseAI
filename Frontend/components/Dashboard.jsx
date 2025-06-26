import React, { useEffect, useState } from 'react';
import axios from 'axios';

export default function Dashboard() {
  const [data, setData] = useState(null);

  useEffect(() => {
    axios.get('/dashboard/summary').then(res => setData(res.data));
  }, []);

  if (!data) return <p>Loading...</p>;

  return (
    <div>
      <h2>📈 Top Profit Items</h2>
      <ul>
        {data.top_items.map(item => (
          <li key={item.dish}>
            {item.dish}: ${item.profit} profit ({item.margin_pct}% margin)
          </li>
        ))}
      </ul>

      <h2>🧯 Low Margin Items</h2>
      <ul>
        {data.low_margin.map(item => (
          <li key={item.dish}>
            {item.dish}: {item.margin_pct}% margin
          </li>
        ))}
      </ul>

      <h2>💵 Total Revenue: ${data.total_revenue}</h2>
      <h2>💰 Total Profit: ${data.total_profit}</h2>
    </div>
  );
}
