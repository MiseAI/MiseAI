# MiseAI React Register Component

This package contains a plug-and-play React component for user registration to your MiseAI backend.

## Installation

1. **Copy files**  
   - Copy `components/Register.jsx` into your React app under `src/components/`.

2. **Install dependencies**  
   ```bash
   npm install axios
   ```

3. **Configure environment**  
   At your project root, create a `.env` file:
   ```
   VITE_API_BASE=https://miseai-backend-production.up.railway.app
   ```

4. **Integrate into your Router**  
   In your routing setup (e.g. `src/main.jsx` or `src/App.jsx`):
   ```jsx
   import Register from './components/Register';

   // ... inside your <Routes>:
   <Route path="/register" element={<Register />} />
   ```

5. **Run your app**  
   ```bash
   npm run dev
   ```
   Then navigate to `http://localhost:3000/register` (or your deployed frontend URL `/register`) to see the registration form.
