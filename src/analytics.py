def index_by_date(prices):
    return {row["date"]: row for row in prices}


def align_series(instrument_prices, benchmark_prices):
    a = index_by_date(instrument_prices)
    b = index_by_date(benchmark_prices)
    common_dates = sorted(set(a) & set(b))
    aligned_a = [a[date] for date in common_dates]
    aligned_b = [b[date] for date in common_dates]
    return aligned_a, aligned_b


def calculate_period_return(prices):
    if not prices:
        raise ValueError("Cannot compute return on an empty series.")
    first_close = float(prices[0]["close"])
    last_close = float(prices[-1]["close"])
    if first_close == 0.0:
        raise ZeroDivisionError("Initial price cannot be zero.")
    return ((last_close / first_close) - 1.0) * 100.0


def calculate_base_100(prices):
    if not prices:
        raise ValueError("Cannot compute base 100 on an empty series.")
    first_close = float(prices[0]["close"])
    if first_close == 0.0:
        raise ZeroDivisionError("Initial price cannot be zero.")
    return [
        {
            "date": row["date"],
            "ticker": row["ticker"],
            "value": float(row["close"]) / first_close * 100.0,
        }
        for row in prices
    ]


def calculate_relative_performance(instrument_return, benchmark_return):
    return float(instrument_return) - float(benchmark_return)
