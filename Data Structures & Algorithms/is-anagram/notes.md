# Valid Anagram (NeetCode 242) — Coach Notes

- **Problem:** https://leetcode.com/problems/valid-anagram/
- **Pattern:** Arrays & Hashing
- **Difficulty:** Easy
- **Your submissions:** 4 (all Python)

---

## Honest verdict

Four submissions, all functionally correct, exploring genuinely different approaches. **This is the right way to grind a problem** — solve it, then ask "can I do it differently?" That builds pattern fluency in a way "submit and move on" never will. Real credit for that.

Now let's break each one apart.

## Submission-by-submission

### `submission-0.py` — two-map hashmap

```python
seen = {}
teen = {}                       # cute, but rename: `t_count` is clearer
for char in s:
    if char in seen:
        seen[char] += 1;        # trailing semicolons — drop them, Python doesn't use them
    ...
return teen == seen
```

- **Works.** Two maps, compare at the end.
- **Missing length check.** If `s` and `t` have different lengths they obviously can't be anagrams — bail in O(1) instead of doing two full passes. You added this in later submissions. Good.
- **Style:** the trailing semicolons everywhere are not wrong, but they're a tell that you're not native to Python. Drop them. Same for `seen`/`teen` — it's funny, but `s_count`/`t_count` reads better.
- **Time:** O(n + m). **Space:** O(n + m), or O(1) if you can assume lowercase ASCII (bounded by 26 keys).

### `submission-1.py` — sort-and-compare

```python
if len(s) != len(t):
    return False
return sorted(s) == sorted(t)
```

- Length check added ✓
- Cleanest code, no question.
- **Trade-off:** O(n log n) time vs O(n) for the hashmap. In an interview, mention this trade — sorting is shorter to write but slower. They want to hear that you know.
- **Space:** O(n) because `sorted()` returns a new list.

### `submission-2.py` — one-pass dict counter

```python
mapS, mapT = {}, {}
for i in range(len(s)):
    mapS[s[i]] = 1 + mapS.get(s[i], 0)
    mapT[t[i]] = 1 + mapT.get(t[i], 0)
return mapS == mapT
```

- **Improvement over sub-0:** single loop (you can only do this because the length check guarantees `len(s) == len(t)`).
- **`.get(key, 0)` is good Pythonic** — cleaner than the if/else from sub-0.
- Even more pythonic: `from collections import defaultdict; mapS = defaultdict(int); mapS[c] += 1`. But honestly `.get()` is fine and arguably clearer.
- **Time:** O(n). **Space:** O(n), bounded by alphabet size.

### `submission-3.py` — array counter (best one)

```python
count = [0] * 26
for i in range(len(s)):
    count[ord(s[i]) - ord('a')] += 1
    count[ord(t[i]) - ord('a')] -= 1
for val in count:
    if val != 0:
        return False
return True
```

- **The interview-favorite version.** Constant space (26 slots regardless of input size), increment for one string + decrement for the other = clever inversion trick.
- **Time:** O(n). **Space:** O(1). This is genuinely better than the hashmap on space.
- **One constraint to call out:** assumes lowercase English only (a–z). If `s` or `t` could have uppercase, digits, unicode → this breaks. In an interview say: *"This works for the given constraint of lowercase letters. If we needed to handle Unicode, I'd switch to a hashmap."*

## The most pythonic version (worth knowing)

```python
from collections import Counter
return Counter(s) == Counter(t)
```

That's it. `Counter` is built specifically for this. In an interview, **mention it** ("the one-line solution is `Counter(s) == Counter(t)`"), then immediately offer to implement it manually. Interviewers like seeing that you know the stdlib AND can do it from scratch.

## Style fixes to apply going forward

1. **Drop the trailing semicolons.** `return True` not `return True;`. Python parses them, but no native writes them.
2. **Don't shadow builtins.** You used `map = {}` and `list = [...]` in other problems — both are Python builtins. Use `seen`, `idx`, `result`, etc.
3. **Use `enumerate` instead of `range(len(...))`** when you need both index and value. It's faster, more readable, and signals "I know Python."

```python
# Instead of:
for i in range(len(s)):
    count[ord(s[i]) - ord('a')] += 1

# Write:
for i, ch in enumerate(s):
    count[ord(ch) - ord('a')] += 1
```

## The pattern this teaches

**Character counting via hashmap or fixed-size array.** When you need to compare two collections by frequency, your tools are:
- `Counter` (most idiomatic)
- `dict` with `.get()` or `defaultdict`
- fixed-size array if the alphabet is bounded (best constant space)

The "increment then decrement" trick from sub-3 is a generalizable pattern — appears in Sliding Window problems too.

## Question for you

If the strings contained Unicode (emoji, accented chars, Chinese), your sub-3 array approach breaks because you can't fit Unicode into 26 slots. **Which of your four solutions would still work without modification?** (Answer: 0, 1, 2 — sub-3 is the only one that hard-codes the alphabet size.)

## Your turn — fill this in

**What I tried first (before the working ones):**

**Why I tried 4 different approaches:**

**Which approach do I think I'd reach for first if I saw this in an interview, and why:**

**Revisit?** [ ] Mark if I want to redo this from scratch in a week, *without looking at my code.*
