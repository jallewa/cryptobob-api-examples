/* eslint-disable no-console */
const url = new URL("https://api.cryptobob.de/v1/rankings");
url.searchParams.set("timeframe", "15m");
url.searchParams.set("limit", "10");

const API_KEY = "YOUR_API_KEY";

async function main() {
  const res = await fetch(url, {
    headers: { "X-API-Key": API_KEY },
  });

  if (!res.ok) {
    const text = await res.text();
    throw new Error(`HTTP ${res.status}: ${text}`);
  }

  const data = await res.json();
  console.log(data);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
