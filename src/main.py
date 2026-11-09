from pathlib import Path
import csv
import json


DATA_DIR = Path("data/sample")

# These starter values mirror config/settings.yml.
# settings.yml is a human-readable configuration contract in the CORE.
# Parsing YAML is optional and is not required by the 18-hour lab sequence.
LOOKBACK_LABEL = "1 month"
INTERVAL_LABEL = "Daily"


def load_instruments():
    with open(DATA_DIR / "instruments.json", encoding="utf-8") as file:
        return json.load(file)


def load_prices():
    with open(DATA_DIR / "prices.csv", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def filter_prices(prices, ticker):
    return [row for row in prices if row["ticker"] == ticker]

def get_first_close(prices):
    return float(prices[0]["close"])

def get_last_close(prices):
    return float(prices[-1]["close"])

def display_market_summary(asset, prices, show_currency=True):
    print(asset["ticker"], "-", asset["name"])
    print("Observations:", len(prices))
    if show_currency:
        print("First close:", get_first_close(prices), asset["currency"])
        print("Last close:", get_last_close(prices), asset["currency"])
    else:
        print("First close:", get_first_close(prices))
        print("Last close:", get_last_close(prices))
    print()


def main():
    instruments = load_instruments()
    prices = load_prices()   
    
    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    instrument_prices = filter_prices(prices, instrument["ticker"])
    benchmark_prices = filter_prices(prices, benchmark["ticker"])

    print(get_first_close(instrument_prices), get_last_close(instrument_prices))
    print(get_first_close(benchmark_prices), get_last_close(benchmark_prices))

    instrument_latest = instrument_prices[-1]
    benchmark_latest = benchmark_prices[-1]

    print("=== MarketPulse ===")
    print()
    display_market_summary(instrument, instrument_prices)
    display_market_summary(benchmark, benchmark_prices, show_currency=False)
    print()
    print(f"Period: {LOOKBACK_LABEL}")
    print(f"Interval: {INTERVAL_LABEL}")
    print()
    print("Observations")
    print(f"{instrument['ticker']}: {len(instrument_prices)}")
    print(f"{benchmark['ticker']}: {len(benchmark_prices)}")


if __name__ == "__main__":
    main()
