# PROGRESS.md — Running Coaching Log

Updated by the coach after each review session. Do not edit manually.

---

## Style debts — status

| Habit | First flagged | Last seen | Status |
|-------|--------------|-----------|--------|
| Trailing semicolons | duplicate-integer | two-integer-sum | 🔴 recurring |
| Shadowing builtins (`map`, `list`) | duplicate-integer | anagram-groups | 🔴 recurring |
| `range(len())` instead of `enumerate` | duplicate-integer | two-integer-sum | 🔴 recurring |
| Two-pass when one-pass works | two-integer-sum | two-integer-sum | 🔴 recurring |

Status key: 🔴 recurring · 🟡 improving · 🟢 fixed (seen clean for 3+ problems)

---

## Pattern recognition — what's landed

| Pattern | Problems seen | Confidence |
|---------|--------------|------------|
| Hashmap for O(1) lookup | duplicate-integer, is-anagram, two-integer-sum, anagram-groups | 🟡 building |
| Hash set for "have I seen this before?" | duplicate-integer | 🟡 building |
| Character counting (array vs hashmap) | is-anagram, anagram-groups | 🟡 building |
| One-pass complement search | two-integer-sum | 🔴 shaky — two-pass used in sub-1/sub-2 |
| Canonical key grouping (defaultdict) | anagram-groups | 🔴 shaky — solution looked up, defaultdict not yet understood |

Confidence key: 🔴 shaky · 🟡 building · 🟢 solid

---

## Problem log

| Problem | Submissions | Notes written | Revisit? |
|---------|-------------|---------------|----------|
| duplicate-integer | 3 (2 Java, 1 Python) | 2026-05-13 | not marked |
| is-anagram | 4 (Python) | 2026-05-13 | not marked |
| two-integer-sum | 3 (Python) | 2026-05-13 | not marked |
| anagram-groups | 4 (Python) | 2026-05-14 | not marked |

---

## Coach observations
<!-- append after each session, newest first -->

*2026-05-14 (second) — anagram-groups reviewed. 4 submissions. Sub-0 was a genuine attempt that stalled before a grouping strategy landed. Sub-2 reached the correct approach (sorted key) but comment confirms GPT-assisted ("kinda asking gpt to fix a lot of the errors"). Sub-3 and sub-5 are NeetCode solutions — comments on both explicitly say "i do not know what a defaultdict is" and ask about tuple/list(values()). Assist level: looked up solution. Two new SYNTAX.md entries added: tuple() as dict key, dict.values() + list(). Builtin shadowing (`map`) still showing up — that's four problems in a row now. "Your turn" sections across all previous problems (duplicate-integer, is-anagram, two-integer-sum) are still blank as of this session.*

*2026-05-14 — Scheduled check-in. No new submissions since initial bulk sync. Notes are written and complete for all three problems. The "Your turn" sections in every notes.md are still blank — that reflection is the whole point of the exercise, and it's the one thing that hasn't happened yet. Until those are filled in, the learning is only half-done. Next session: check if "Your turn" got filled in, and flag it again if not.*

*2026-05-13 — Coach notes written for all three problems: duplicate-integer, is-anagram, two-integer-sum. All four style debts active (trailing semicolons, builtin shadowing, range(len()), two-pass preference). Two Sum one-pass complement pattern is the key thing to internalize. Initial PROGRESS.md setup.*
