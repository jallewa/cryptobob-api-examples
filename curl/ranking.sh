#!/usr/bin/env bash
set -euo pipefail

API_KEY="${API_KEY:-YOUR_API_KEY}"

curl -sS -H "X-API-Key: ${API_KEY}" \
  "https://api.cryptobob.de/v1/rankings?timeframe=15m&limit=5" | jq .
