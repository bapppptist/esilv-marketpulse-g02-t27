import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.providers.yahoo_provider import fetch_prices_for_ticker


def check_series(rows, ticker):
    assert rows, f"{ticker}: empty series"
    for row in rows:
        assert row["ticker"] == ticker
        assert isinstance(row["date"], str) and len(row["date"]) == 10
        for key in ("open", "high", "low", "close"):
            assert isinstance(row[key], float)
        assert isinstance(row["volume"], int)


aapl = fetch_prices_for_ticker("AAPL")
check_series(aapl, "AAPL")
print(f"AAPL  (1mo, 1d): {len(aapl)} observations | {aapl[0]['date']} -> {aapl[-1]['date']}")

sp500 = fetch_prices_for_ticker("SP500")
check_series(sp500, "SP500")
print(f"SP500 (1mo, 1d): {len(sp500)} observations | {sp500[0]['date']} -> {sp500[-1]['date']}")

aapl_3mo = fetch_prices_for_ticker("AAPL", period="3mo", interval="1d")
check_series(aapl_3mo, "AAPL")
assert len(aapl_3mo) > len(aapl), "3mo should return more observations than 1mo"
print(f"AAPL  (3mo, 1d): {len(aapl_3mo)} observations | {aapl_3mo[0]['date']} -> {aapl_3mo[-1]['date']}")

try:
    fetch_prices_for_ticker("UNKNOWN")
except ValueError as error:
    print("UNKNOWN correctly rejected:", error)
else:
    raise AssertionError("UNKNOWN should raise ValueError")

print("All Yahoo provider checks passed.")
