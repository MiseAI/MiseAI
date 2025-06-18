export const API_BASE = import.meta.env.VITE_API_BASE || 'https://miseai-backend-production.up.railway.app';

export async function postJson(path, body) {
  const res = await fetch(`${API_BASE}${path}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  const data = await res.json();
  if (!res.ok) throw new Error(data.detail || data.message || res.statusText);
  return data;
}

export async function authFetch(path, opts = {}) {
  const token = localStorage.getItem('token');
  const res = await fetch(`${API_BASE}${path}`, {
    ...opts,
    headers: {
      ...(opts.headers || {}),
      Authorization: `Bearer ${token}`,
    },
  });
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}
