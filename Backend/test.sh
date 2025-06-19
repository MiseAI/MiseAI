#!/usr/bin/env bash

BASE="https://miseai-backend-production.up.railway.app"

# 1) Log in and capture the full JSON response
LOGIN_RES=$(curl -s -X POST "${BASE}/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"email":"tester@example.com","password":"secret"}')
echo "Login response → ${LOGIN_RES}"

# 2) Extract the JWT
TOKEN=$(printf '%s' "$LOGIN_RES" | jq -r .access_token)
if [[ -z $TOKEN || $TOKEN == "null" ]]; then
  echo "❌ Failed to extract access_token. Check the /auth/login response above."
  exit 1
fi
echo "✅ Got JWT: ${TOKEN}"

# 3) Call the protected endpoint
curl -i -X GET "${BASE}/users/me" \
     -H "Authorization: Bearer ${TOKEN}"
