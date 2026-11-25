# Run MarketPulse

This guide explains how to run the MarketPulse terminal application in the current CSV / JSON stage.

## Requirements

- Python 3 (standard library only at this stage, no `pip install` needed)
- Git
- A terminal opened at the root of the team repository (GitHub Codespaces works out of the box)

## 1. Go to the repository root

```bash
pwd
ls
```

You should see `README.md`, `config`, `data`, `src` and `TEAM.md`.
If not, move back to the root, for example with `cd ..`.

## 2. Check the tools

```bash
python --version
git --version
```

If `python` is not found, use `python3` instead. Do not install another Python.

## 3. Inspect the input data (optional)

```bash
cat data/sample/instruments.json
head data/sample/prices.csv
grep AAPL data/sample/prices.csv
```

- `instruments.json` describes the instrument (AAPL - Apple Inc.) and the benchmark (SP500 - S&P 500).
- `prices.csv` contains one line per trading day and per ticker, for both series.

## 4. Run the application

```bash
python src/main.py
```

The terminal displays a MarketPulse summary with:

- the instrument `AAPL - Apple Inc.` and the benchmark `SP500 - S&P 500`;
- 21 daily observations for each series;
- the first and last closing prices;
- the period (1 month) and the interval (Daily).

The exact layout may evolve as the team merges new features.

## Troubleshooting

| Problem | What to check |
|---|---|
| `FileNotFoundError` / `No such file or directory` | Run the command from the repository root (`pwd`, `ls data/sample`). |
| `python: command not found` | Use `python3 src/main.py`. |
| `KeyError` | Check the spelling and capitals of the keys in `instruments.json` and the CSV header. |
| `TypeError` with `+` or `-` | A CSV value is still a string: convert it with `float()` first. |
| Repository not accessible | Check that you use your own GitHub account and accepted the collaborator invitation. |
