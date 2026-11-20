# Checkpoint A - Loïc Bagourd

## Identity

- Full name: Loïc Bagourd
- GitHub username: @LOLO-dot-tech
- TD group: G02
- MarketPulse team: T27
- Team repository: `bapppptist/esilv-marketpulse-g02-t27`

## Scope

Checkpoint Phase A - TD01 to TD04 (Foundations).

## Evidence files

| File | What it shows |
|---|---|
| `01_terminal_python.png` | Python version and `python src/main.py` running from the repository root (AAPL vs S&P 500 summary). |
| `02_git_status_log.png` | Clean `git status` and `git log` showing my own commits. |
| `03_branch_merge.png` | `git branch`, `git branch --merged` and the Git graph after merging `feature/display-observation-dates` into `main`, captured before deleting the branch. |

## What I did

- **TD01 - Bootstrap + Linux:** opened a GitHub Codespace on the team repository, navigated with `pwd`, `ls`, `cd`, inspected data with `cat`, `head`, `grep`, ran MarketPulse.
- **TD02 - Python + CSV / JSON:** cleaned `src/main.py` (removed debug output and duplicated blocks) and aligned the output with the target: reusable `display_market_summary`, closes converted with `float()` and displayed with two decimals.
- **TD03 - Git local workflow:** configured my Git identity, used `git status`, `git diff`, `git add src/main.py`, `git diff --staged`, `git commit`, `git log`, `git show`.
  - `refactor: remove debug output from main`
  - `feat: align market summary with target output`
- **TD04 - Branches + Merge:** created `feature/display-observation-dates` from a clean `main`, added `get_first_date` / `get_last_date`, committed `feat: display first and last observation dates`, compared with `git diff main..feature/display-observation-dates`, merged into local `main`, then deleted the merged branch with `git branch -d`.

## Explanations

- **Working tree / staging area / commit:** editing a file does not put it in a commit; `git add` selects the change, `git commit` records a snapshot with author, date and message.
- **Branch:** isolates feature work so that `main` is not modified until the feature is ready.
- **Fast-forward:** `main` had no new commit since the branch was created, so Git simply moved `main` forward to the feature commit. No merge commit was needed, and the history stays linear.
- **Merge conflict:** happens when two branches change the same lines; Git cannot choose, so a human inspects both versions, chooses the final content, removes the markers, then runs `git add` and completes the merge.

## Validation

- `python src/main.py` runs after the merge.
- Instrument and benchmark both show 21 observations, first date 2026-09-01, last date 2026-09-30.
- No secret, token or personal e-mail appears in this evidence.
