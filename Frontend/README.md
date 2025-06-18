# MiseAI Frontend Auth Package

This package contains plug-and-play frontend files for user authentication.

## Files

- `register.html` – Registration page
- `login.html` – Login page
- `dashboard.html` – Protected dashboard page
- `auth.js` – JavaScript to handle API calls to your Backend

## Usage

1. Deploy your backend with CORS enabled for your frontend domain.
2. Copy these files into your static hosting directory (e.g. Railway Frontend).
3. Ensure your backend is available at `https://miseai-backend-production.up.railway.app`.
4. Open `register.html`, sign up, then log in via `login.html`. On success, you’ll be redirected to `dashboard.html`.
