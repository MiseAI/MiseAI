import { useEffect, useState } from "react";
import axios from "axios";

export default function Dashboard() {
  const [sales, setSales] = useState([]);

  useEffect(() => {
    axios.get("https://your-backend-url.com/sales/?restaurant_id=1", {
      headers: { Authorization: `Bearer your_token_here` }
    })
    .then(res => setSales(res.data))
    .catch(err => console.error("Failed to load sales", err));
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Dashboard</h1>
      <ul className="bg-white shadow p-4 rounded-xl space-y-2">
        {sales.map(s => (
          <li key={s.id} className="border-b py-1">{s.dish_id} — {s.quantity_sold} sold on {s.date}</li>
        ))}
      </ul>
    </div>
  );
}
