import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.analytics import (
    align_series,
    calculate_base_100,
    calculate_period_return,
    calculate_relative_performance,
)


def obs(date, ticker, close):
    return {"date": date, "ticker": ticker, "open": close, "high": close,
            "low": close, "close": close, "volume": 1000}


def last_value(base_100_series):
    last = base_100_series[-1]
    return float(last["value"]) if isinstance(last, dict) else float(last)


aapl = [obs("2026-11-01", "AAPL", 100.0),
        obs("2026-11-02", "AAPL", 105.0),
        obs("2026-11-03", "AAPL", 110.0)]
sp500 = [obs("2026-11-01", "SP500", 200.0),
         obs("2026-11-02", "SP500", 204.0),
         obs("2026-11-03", "SP500", 210.0)]

r_aapl = calculate_period_return(aapl)
r_sp500 = calculate_period_return(sp500)
assert math.isclose(r_aapl, 10.0), r_aapl
assert math.isclose(r_sp500, 5.0), r_sp500

assert math.isclose(last_value(calculate_base_100(aapl)), 110.0)
assert math.isclose(last_value(calculate_base_100(sp500)), 105.0)
assert math.isclose(last_value(calculate_base_100(sp500)[:1]), 100.0)

assert math.isclose(calculate_relative_performance(r_aapl, r_sp500), 5.0)

aapl_gap = [obs(f"2026-11-0{d}", "AAPL", 100.0 + d) for d in (1, 2, 3, 4, 5)]
sp500_gap = [obs(f"2026-11-0{d}", "SP500", 200.0 + d) for d in (5, 1, 2, 4)]

a, b = align_series(aapl_gap, sp500_gap)
expected_dates = ["2026-11-01", "2026-11-02", "2026-11-04", "2026-11-05"]
assert [r["date"] for r in a] == expected_dates
assert [r["date"] for r in b] == expected_dates
assert len(a) == len(b) == 4
assert all(r["ticker"] == "AAPL" for r in a)
assert all(r["ticker"] == "SP500" for r in b)

try:
    calculate_period_return([])
except ValueError:
    pass
else:
    raise AssertionError("Une série vide aurait dû lever ValueError.")

print("Tous les tests Analytics ont réussi.")
