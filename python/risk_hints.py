import requests

API_KEY = "YOUR_API_KEY"

def main():
    # Adjust endpoint/params to match your API if different.
    r = requests.get(
        "https://api.cryptobob.de/v1/risk-hints",
        headers={"X-API-Key": API_KEY},
        params={"symbol": "BTCUSDT", "timeframe": "15m"},
        timeout=30,
    )
    r.raise_for_status()
    print(r.json())

if __name__ == "__main__":
    main()
