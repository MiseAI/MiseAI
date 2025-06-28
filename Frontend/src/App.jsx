import { Link } from 'react-router-dom';

function App() {
  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-4">Welcome to MiseAI Frontend!</h1>
      <div className="flex space-x-4">
        <Link
          to="/chat"
          className="bg-blue-600 text-white px-4 py-2 rounded"
        >
          Go to Chat
        </Link>
        <Link
          to="/upload-invoice"
          className="bg-green-600 text-white px-4 py-2 rounded"
        >
          Upload Invoice
        </Link>
      </div>
    </div>
  );
}

export default App;