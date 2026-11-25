# Checkpoint B

## Student

- Name: Baptiste Caris
- GitHub: @bapppptist

## Contribution

- Branch: fix/remove-debug-prints
- Main commit: 367ac96
- Pull Request: #5 (fix: remove debug prints from terminal output), reviewed by @maxime123456789517 and merged
- Reviewed Pull Requests: #7 (analytics module, approved and merged), #4 (requested changes, then approved after the fix)

## Work completed

Removed leftover debug prints from src/main.py (PR #5).
Reviewed the analytics module PR #7: checked out the branch, ran tests/validate_analytics.py and compared results with notebook 01 (AAPL +6.48 %, SP500 +2.15 %).
Ran notebook 02: real Yahoo Finance retrieval of AAPL and S&P 500 (1 month, daily).

## Main difficulty

Understanding that git fetch does not update local main (found during review of PR #4), and handling a rejected push when a teammate had already pushed the same feature branch.

## Evidence

- 01_pull_request.png
- 02_code_review.png
- 03_yahoo_market_data.png
- 04_instrument_benchmark.png