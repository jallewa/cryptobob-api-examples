# CryptoBob API – Market Intelligence for Crypto Trading

CryptoBob provides deterministic market rankings, regime filters and risk hints to support algorithmic crypto trading systems.

## What problem does this solve?

Most crypto trading bots fail because they trade in the wrong market conditions.

CryptoBob helps you:
- avoid high-risk regimes
- rank markets by setup quality
- derive volatility-aware risk parameters

## Features

- Market regime detection (trend, volatility)
- Market rankings by setup quality
- ATR-based risk and stop hints
- Deterministic and backtest-safe outputs
- REST API with API key authentication

## Quick Start (cURL)

```bash
curl -H "X-API-Key: YOUR_API_KEY" \
  "https://api.cryptobob.de/v1/rankings?timeframe=15m&limit=5"
```

## Python Example

```python
import requests

url = "https://api.cryptobob.de/v1/rankings"
headers = {"X-API-Key": "YOUR_API_KEY"}
params = {"timeframe": "15m", "limit": 5}

response = requests.get(url, headers=headers, params=params, timeout=30)
response.raise_for_status()
print(response.json())
```

## Typical Use Case

Example: Filter markets before running your strategy

1. Get market rankings
2. Ignore markets with weak setup scores
3. Skip trading during unstable regimes
4. Apply your own entry logic

## API Documentation

- Website: https://cryptobob.de
- Docs: https://cryptobob.de/docs (adjust if your docs are hosted elsewhere)

## Disclaimer

This project does not provide financial advice. Use at your own risk.
