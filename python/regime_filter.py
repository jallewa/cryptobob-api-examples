import requests

API_KEY = "YOUR_API_KEY"

def main():
    # Adjust endpoint/params to match your API if different.
    r = requests.get(
        "https://api.cryptobob.de/v1/regime",
        headers={"X-API-Key": API_KEY},
        params={"timeframe": "1h"},
        timeout=30,
    )
    r.raise_for_status()
    data = r.json()
    print(data)

    # Example: naive decision logic (replace with your actual fields)
    # if data.get("is_tradeable"):
    #     print("Tradeable regime: OK to run strategy")
    # else:
    #     print("Untradeable regime: skip")

if __name__ == "__main__":
    main()
