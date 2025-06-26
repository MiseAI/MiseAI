import { useState } from 'react';
import api from '../api';

export default function MenuAnalyzer() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const handleUpload = async () => {
    const form = new FormData();
    form.append('file', file);
    const { data } = await api.post('/menu/analyze', form, {
      headers: { 'Content-Type': 'multipart/form-data' }
    });
    setResult(data);
  };
  return (
    <div>
      <h1 className="text-2xl mb-4">Menu Performance Analyzer</h1>
      <input type="file" onChange={e => setFile(e.target.files[0])} />
      <button onClick={handleUpload} className="ml-2 px-4 py-2 bg-blue-600 text-white rounded">Analyze</button>
      {result && <pre className="mt-4">{JSON.stringify(result, null, 2)}</pre>}
    </div>
);