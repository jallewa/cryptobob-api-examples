import requests

API_KEY = "YOUR_API_KEY"

def main():
    r = requests.get(
        "https://api.cryptobob.de/v1/rankings",
        headers={"X-API-Key": API_KEY},
        params={"timeframe": "15m", "limit": 10},
        timeout=30,
    )
    r.raise_for_status()
    print(r.json())

if __name__ == "__main__":
    main()
