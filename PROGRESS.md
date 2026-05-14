# PROGRESS.md — Running Coaching Log

Updated by the coach after each review session. Do not edit manually.

---

## Style debts — status

| Habit | First flagged | Last seen | Status |
|-------|--------------|-----------|--------|
| Trailing semicolons | duplicate-integer | two-integer-sum | 🔴 recurring |
| Shadowing builtins (`map`, `list`) | duplicate-integer | two-integer-sum | 🔴 recurring |
| `range(len())` instead of `enumerate` | duplicate-integer | two-integer-sum | 🔴 recurring |
| Two-pass when one-pass works | two-integer-sum | two-integer-sum | 🔴 recurring |

Status key: 🔴 recurring · 🟡 improving · 🟢 fixed (seen clean for 3+ problems)

---

## Pattern recognition — what's landed

| Pattern | Problems seen | Confidence |
|---------|--------------|------------|
| Hashmap for O(1) lookup | duplicate-integer, is-anagram, two-integer-sum | 🟡 building |
| Hash set for "have I seen this before?" | duplicate-integer | 🟡 building |
| Character counting (array vs hashmap) | is-anagram | 🟡 building |
| One-pass complement search | two-integer-sum | 🔴 shaky — two-pass used in sub-1/sub-2 |

Confidence key: 🔴 shaky · 🟡 building · 🟢 solid

---

## Problem log

| Problem | Submissions | Notes written | Revisit? |
|---------|-------------|---------------|----------|
| duplicate-integer | 3 (2 Java, 1 Python) | 2026-05-13 | not marked |
| is-anagram | 4 (Python) | 2026-05-13 | not marked |
| two-integer-sum | 3 (Python) | 2026-05-13 | not marked |

---

## Coach observations
<!-- append after each session, newest first -->

*2026-05-14 — Scheduled check-in. No new submissions since initial bulk sync. Notes are written and complete for all three problems. The "Your turn" sections in every notes.md are still blank — that reflection is the whole point of the exercise, and it's the one thing that hasn't happened yet. Until those are filled in, the learning is only half-done. Next session: check if "Your turn" got filled in, and flag it again if not.*

*2026-05-13 — Coach notes written for all three problems: duplicate-integer, is-anagram, two-integer-sum. All four style debts active (trailing semicolons, builtin shadowing, range(len()), two-pass preference). Two Sum one-pass complement pattern is the key thing to internalize. Initial PROGRESS.md setup.*
