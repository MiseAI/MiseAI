import { Routes, Route, Link } from 'react-router-dom';
import MenuAnalyzer from './pages/MenuAnalyzer';
import RecipeCost from './pages/RecipeCost';
import InvoiceParser from './pages/InvoiceParser';
import ForecastTool from './pages/ForecastTool';
import Dashboard from './pages/Dashboard';
import ChatAssistant from './pages/ChatAssistant';

export default function App() {
  return (
    <div className="min-h-screen bg-gray-50">
      <nav className="bg-white shadow p-4 flex space-x-4">
        {['Menu Analyzer','Recipe Cost','Invoices','Forecast','Dashboard','Chat'].map((label, i) => (
          <Link key={i} to={`/${label.toLowerCase().replace(/\s+/g,'-')}`} className="text-blue-600">
            {label}
          </Link>
        ))}
      </nav>
      <main className="p-6">
        <Routes>
          <Route path="/menu-analyzer" element={<MenuAnalyzer />} />
          <Route path="/recipe-cost" element={<RecipeCost />} />
          <Route path="/invoices" element={<InvoiceParser />} />
          <Route path="/forecast" element={<ForecastTool />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/chat" element={<ChatAssistant />} />
        </Routes>
      </main>
    </div>
);