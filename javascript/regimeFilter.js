/* eslint-disable no-console */
const url = new URL("https://api.cryptobob.de/v1/regime");
url.searchParams.set("timeframe", "1h");

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

  // Example decision stub:
  // if (data.is_tradeable) console.log("Tradeable regime");
  // else console.log("Skip trading");
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
