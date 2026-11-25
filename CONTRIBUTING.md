# Contributing to MarketPulse

This repository is used to learn Python, Git and Linux through a progressive financial market-data project.

The workflow is intentionally simple.

## 1. General rule

Do not create unnecessary Git complexity.

The common workflow is:

```text
main
  |
  v
feature branch
  |
  v
changes
  |
  v
commit
  |
  v
push
  |
  v
Pull Request
  |
  v
review
  |
  v
merge
```

The exact steps are introduced progressively during the labs.

## 2. Branch naming

Use short descriptive branch names.

Recommended patterns:

```text
feature/<short-description>
fix/<short-description>
docs/<short-description>
```

Examples:

```text
feature/display-benchmark
feature/yahoo-provider
feature/base-100-comparison
fix/invalid-ticker
docs/update-readme
```

Avoid:

```text
my-branch
student1
test
work
final-final
```

Branch names describe the work, not the student.

## 3. Commits

Commits should be understandable.

Examples:

```text
feat: display benchmark metadata
feat: add Yahoo Finance provider
fix: handle missing ticker
docs: update MarketPulse setup
```

Avoid messages such as:

```text
update
changes
work
final
test
```

Do not optimize for the number of commits. A good history is more useful than many meaningless commits.

## 4. Pull Requests

Once Pull Requests are introduced in the labs, feature work should not be merged directly into `main`.

A Pull Request should contain:

- a clear title;
- a short description of the change;
- the feature or issue addressed;
- any useful execution or validation information.

Example title:

```text
feat: add benchmark comparison
```

## 5. Review

Once code review is introduced, another team member should review the Pull Request.

A useful review may:

- verify that the requested feature works;
- identify an error;
- suggest a correction;
- ask for clarification;
- approve a correct change.

A reaction without technical content is not considered a meaningful review.

## 6. Individual contribution

The repository is shared by the team, but contributions remain individual.

Each student should have identifiable:

- commits;
- branches;
- Pull Requests;
- reviews;
- functional contributions;
- checkpoint evidence.

Being listed in `TEAM.md` is not sufficient evidence of contribution.

## 7. main branch

During the earliest Git exercises, the instructor may temporarily allow direct operations on `main`.

Once branches and Pull Requests have been introduced:

```text
No direct feature development on main.
```

## 8. Security

Never commit:

- passwords;
- API keys;
- access tokens;
- SSH private keys;
- Bloomberg credentials;
- cloud credentials;
- payment information.

If a secret is committed accidentally, notify the instructor immediately.

## 9. Scope

The common course repository focuses on:

```text
Python
+
Git
+
Linux
+
financial market data
```

Do not add unnecessary infrastructure or frameworks unless requested by the instructor.

## 10. Command quick reference

Start from an up-to-date `main`:

```bash
git switch main
git fetch origin
git pull
git status
```

Create a branch, commit and push it to the team repository:

```bash
git switch -c feature/<short-description>
git add <file>
git commit -m "feat: <meaningful message>"
git push -u origin feature/<short-description>
```

Then open a Pull Request on GitHub:

- base repository: the team repository (not the instructor repository);
- base branch: `main`;
- compare branch: your feature branch.

Do not merge your own Pull Request before the review.
