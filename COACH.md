# COACH.md

If you're a Claude reading this — this is your full context. Start here, then check REVIEW_FORMAT.md before writing any notes.

---

## Who
- **User:** aakesh
- **Goal:** NeetCode 150 for interview prep, pattern recognition over problem count
- **Language:** Python
- **Where:** Arrays & Hashing, just starting

## Repo layout
```
neetcode-submissions/
  COACH.md                          ← this file
  REVIEW_FORMAT.md                  ← notes format + tone rules
  PROGRESS.md                       ← running log of trends, updated after each session
  README.md                         ← auto-generated, do NOT touch
  Data Structures & Algorithms/
    <problem-slug>/
      submission-0.<ext>            ← auto-pushed by NeetCode, do NOT modify
      submission-1.<ext>
      ...
      notes.md                      ← your job to write
```

## Workflow
1. `cd /Users/aakes/code/neetcode-submissions && git pull --rebase`
2. Identify scope:
   - *"review my latest"* → most recently modified problem folder
   - *"review X"* → folder matching that name
   - *"review everything"* → all folders missing a `notes.md`
3. Read REVIEW_FORMAT.md and PROGRESS.md
4. For each problem: read every `submission-N.<ext>` in order, read existing `notes.md` if any
5. Write `notes.md` per the format in REVIEW_FORMAT.md
6. Update `PROGRESS.md` — style debt statuses, pattern confidence, problem log, coach observations
7. Commit and push:
   ```bash
   git add . && git -c user.email="aakeshy@outlook.com" -c user.name="chaaz-ah" \
     commit -m "coach: notes for <problem-slug>"
   git push
   ```

## Open style debts
These habits are recurring — keep flagging until they stop showing up:
- **Trailing semicolons** (`return x;`) — drop them
- **Shadowing builtins** (`map = {}`, `list = []`) — use `seen`, `result`, `freq`
- **`range(len(arr))`** — use `enumerate` when you need both index and value
- **Two-pass when one-pass works** — if a hashmap can be built and checked in one loop, do that

Problems where these were flagged but not yet fixed: `duplicate-integer`, `is-anagram`, `two-integer-sum`