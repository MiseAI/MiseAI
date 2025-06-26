#!/usr/bin/env bash
set -e

BASE="https://miseai-backend-production.up.railway.app"

# 1) Ensure this user exists
curl -s -X POST "$BASE/auth/register" \
     -H "Content-Type: application/json" \
     -d '{"username":"tester","email":"tester@example.com","password":"secret"}' \
  | grep -v "Email already registered"  >/dev/null

# 2) Log in & capture full JSON
LOGIN_RES=$(curl -s -X POST "$BASE/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"email":"tester@example.com","password":"secret"}')
echo "Login response → $LOGIN_RES"

# 3) Extract the token
TOKEN=$(jq -r .access_token <<<"$LOGIN_RES")
if [[ -z "$TOKEN" || "$TOKEN" == "null" ]]; then
  echo "❌ Failed to extract access_token. Check the /auth/login response above."
  exit 1
fi

echo "✅ Got JWT: $TOKEN"

# 4) Call the protected endpoint
curl -i -X GET "$BASE/users/me" \
     -H "Authorization: Bearer $TOKEN"
