# Anagram Groups — Coach Notes

- **Problem:** https://leetcode.com/problems/group-anagrams/
- **Pattern:** Arrays & Hashing
- **Difficulty:** Medium
- **Submissions:** 4 (Python)

## Verdict

Four submissions, but this one needs an honest read. Sub-0 is a genuine first attempt that stalled — good instinct on building a char map, but no strategy for *grouping*. Sub-2 landed on the correct approach (sorted string as key) but the comment says it clearly: saw the algorithm in English, then had GPT fix the errors. Sub-3 and sub-5 are NeetCode solutions copied in, not independently reached. The code in sub-5 is optimal, but the comments on both — "i do not know what a defaultdict is" and "also the tuple" — tell you the understanding isn't there yet. That's not a problem; it's exactly what these notes are for. The pattern is in reach, but it hasn't clicked independently yet.

## Submission-by-submission

### `submission-0.py` — Good instinct, no finish line

Building a per-string char frequency dict is the right first thought. But the loop builds `char` for each string and then does nothing with it — no grouping logic, no return, dead `final = [[]]` sitting at the top. The comment at the bottom shows the thinking was going in a reasonable direction (referencing the is-anagram counter approach), but the submission was abandoned before a strategy for *how to group* emerged. Credit for trying to connect to a prior pattern; the gap is not seeing that the key insight is *what to use as a grouping key*.

Also: `for j in range(len(string))` when you just want `string[j]` — use `for c in string` directly.

### `submission-2.py` — Correct approach, GPT-assisted

Sorted string as key is clean and works. `map[key] = []` then `map[key].append(string)` is the right structure. But: `map` shadows the builtin (open style debt), `final = [[]]` is leftover dead code that was never cleaned up, and the comment confirms this wasn't independently reached. The approach is good — the understanding of *why* it works is the open question.

### `submission-3.py` — Right tool, unknown why

`defaultdict(list)` with sorted key is clean and idiomatic. But the comment "i do not know what a defaultdict is" means this was typed without understanding what it does. See SYNTAX.md for the explanation — it's genuinely simple once you see it. The `list(res.values())` question: `res.values()` returns a *view* object, not a list. LeetCode expects a `List[List[str]]`, so you wrap it in `list()` to convert. That's all it is.

### `submission-5.py` — Optimal solution, still needs the "why"

The 26-char count array as key is the O(m·n) optimal approach — avoids the O(m·k·log k) sort cost. `count = [0] * 26`, increment by `ord(c) - ord('a')`, then `tuple(count)` as the key. The `tuple()` question: dict keys must be *hashable*, and lists are not (they're mutable). `tuple` is immutable, so it can be hashed. That's why `tuple(count)` works but `count` directly would throw a `TypeError`.

## The textbook version

Two approaches worth knowing:

**Approach 1 — Sorted string key** (O(m·k·log k) where m = number of strings, k = max string length):
```python
from collections import defaultdict

def groupAnagrams(strs):
    res = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))  # anagrams produce identical sorted strings
        res[key].append(s)
    return list(res.values())
```
Why it works: anagrams are the same letters in different order. Sorting them produces a canonical form. All strings with the same canonical form are anagrams of each other.

**Approach 2 — Count array key** (O(m·n), strictly better when strings are long):
```python
from collections import defaultdict

def groupAnagrams(strs):
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        res[tuple(count)].append(s)
    return list(res.values())
```
Why `tuple(count)`: the count array is the same for all anagrams (same letter frequencies). We use `tuple` because dict keys must be hashable and lists aren't.

The wrong instinct to watch for: trying to compare strings pairwise (O(m²·k)) or building nested loops. The insight is that you don't need to compare strings to each other — you just need a *canonical representation* that identical anagrams will agree on.

## Style fixes (apply going forward)

- **`map = {}`** — `map` is a Python builtin. Use `groups`, `res`, `freq`, anything else.
- **Dead code** — `final = [[]]` was never used; delete leftover scaffolding before submitting.
- **`for j in range(len(string))`** — when you just want the characters, `for c in string` is cleaner.
- Trailing semicolons: not present here — good.

## The pattern + where else it shows up

This is **hashing with a canonical key** — the same instinct as: "what representation will all equivalent items agree on?" Once you have that, a `defaultdict(list)` groups them automatically.

Same instinct in NC150:
- **Valid Anagram** — same pattern, single pair instead of a group
- **Top K Frequent Elements** — build a frequency map, then bucket/sort by value
- **Encode and Decode Strings** — canonical encoding so different strings don't collide

## Interview check

- Naming `map` blocks the builtin and signals Python unfamiliarity to an interviewer — worth fixing.
- When you reach for `defaultdict`, be ready to explain what it does in one sentence: "it's a dict that initializes missing keys automatically, so I don't need an explicit `if key not in d` check."
- The `tuple(count)` trick is worth explaining unprompted: "I'm using a tuple because dict keys need to be hashable, and lists aren't."

## Question for you

Sub-5 uses `ord(c) - ord('a')` to index into a 26-slot array. Walk through what happens with the string `"eat"` — what does `count` look like after the loop, and why does `tuple(count)` correctly identify it as an anagram of `"tea"`?

## Your turn — fill this in

**What I tried first:**
**Where I got stuck:**
**What made it click:**
**Revisit?** [ ] Mark for redo in 1 week
