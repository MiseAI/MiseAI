import { useState } from 'react';
import api from '../api';

export default function RecipeCost() {
  const [name, setName] = useState('');
  const [ingredients, setIngredients] = useState('{}');
  const [result, setResult] = useState(null);

  const handleSubmit = async () => {
    const payload = { name, ingredients: JSON.parse(ingredients) };
    const { data } = await api.post('/recipe/cost', payload);
    setResult(data);
  };

  return (
    <div>
      <h1 className="text-2xl mb-4">Recipe Costing Assistant</h1>
      <input type="text" placeholder="Recipe Name" value={name} onChange={e => setName(e.target.value)} className="border p-2 w-full mb-2"/>
      <textarea placeholder='{"ingredient": quantity}' value={ingredients} onChange={e => setIngredients(e.target.value)} className="border p-2 w-full mb-2" rows={4}/>
      <button onClick={handleSubmit} className="px-4 py-2 bg-blue-600 text-white rounded">Calculate Cost</button>
      {result && <pre className="mt-4">{JSON.stringify(result,null,2)}</pre>}
    </div>
);