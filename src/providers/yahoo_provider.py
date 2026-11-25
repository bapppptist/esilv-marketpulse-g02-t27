"""Yahoo Finance provider: fetch daily prices and normalize them to MarketPulse canonical rows."""

import yfinance as yf


YAHOO_SYMBOL_MAPPING = {
    "AAPL": "AAPL",
    "SP500": "^GSPC",
}


def fetch_yahoo_prices(symbol, canonical_ticker, period="1mo", interval="1d"):
    """Return a list of canonical observations for one Yahoo Finance symbol.

    symbol: Yahoo Finance symbol (e.g. "^GSPC").
    canonical_ticker: MarketPulse ticker kept in every row (e.g. "SP500").
    """
    history = yf.Ticker(symbol).history(
        period=period,
        interval=interval,
        auto_adjust=False,
    )

    if history.empty:
        raise ValueError(f"No Yahoo Finance data returned for symbol {symbol}.")

    rows = []
    for timestamp, row in history.iterrows():
        rows.append({
            "date": timestamp.strftime("%Y-%m-%d"),
            "ticker": canonical_ticker,
            "open": float(row["Open"]),
            "high": float(row["High"]),
            "low": float(row["Low"]),
            "close": float(row["Close"]),
            "volume": int(row["Volume"]),
        })
    return rows


def fetch_prices_for_ticker(ticker, period="1mo", interval="1d"):
    """Fetch canonical observations for a MarketPulse ticker (e.g. "AAPL", "SP500").

    The Yahoo Finance symbol is resolved with YAHOO_SYMBOL_MAPPING.
    """
    if ticker not in YAHOO_SYMBOL_MAPPING:
        raise ValueError(
            f"Unknown MarketPulse ticker: {ticker}. "
            f"Expected one of {list(YAHOO_SYMBOL_MAPPING)}."
        )
    symbol = YAHOO_SYMBOL_MAPPING[ticker]
    return fetch_yahoo_prices(symbol, ticker, period=period, interval=interval)
