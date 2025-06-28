import { Link } from 'react-router-dom';

function App() {
  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-4">Welcome to MiseAI Frontend!</h1>
      <Link
        to="/chat"
        className="bg-blue-600 text-white px-4 py-2 rounded"
      >
        Go to Chat
      </Link>
    </div>
  );
}

export default App;