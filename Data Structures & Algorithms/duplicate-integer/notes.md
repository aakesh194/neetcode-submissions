# Contains Duplicate (NeetCode 217) — Coach Notes

- **Problem:** https://leetcode.com/problems/contains-duplicate/
- **Pattern:** Arrays & Hashing
- **Difficulty:** Easy
- **Your submissions:** 3 (2 Java, 1 Python)

---

## Honest verdict

You ended at a clean, correct one-liner. Good. But there's stuff worth dissecting across all three attempts — that's where the actual learning is.

## Submission-by-submission

### `submission-0.java` — broken (won't compile)

This one has Java/Python syntax fusion happening:

```java
for int i = 0, i > nums.length - 2, i++ {     // missing parens, commas not semicolons
    if i == j:                                  // Python's `:`, not Java's `{}`
```

That's a sign you were writing Java the way you write Python. Fine to attempt — but if you're going to use Java in interviews, drill the syntax in your head. The compiler errors here are blocking you from even checking if the *idea* was right.

### `submission-1.java` — compiles, but logic is broken

Syntax is fixed, but it still doesn't work. Three logic bugs:

1. **`i > nums.length - 2`** — this is `>` when you want `<`. Loop never runs. Function will always return `false`.
2. **Inner loop uses `i`**: `for (int j = 0; i > nums.length - 1; j++)` — you used `i` again instead of `j`. Infinite loop if it ever entered.
3. **`if (i == j)`** — you're comparing *indices*, not *values*. Should be `nums[i] == nums[j]`. Right now it just returns `true` whenever `i == j`, which is the diagonal of the matrix — useless.

This is the most important submission to learn from. The pattern of bugs (wrong direction, wrong variable, comparing the wrong thing) tells me you wrote it fast without tracing through one example by hand. **Before submitting, always walk through `nums = [1, 2, 3, 1]` on paper — does your code return `true`?** It would have caught all three.

### `submission-2.py` — correct, elegant

```python
return len(set(nums)) < len(nums)
```

- **Time:** O(n) — building the set is O(n)
- **Space:** O(n) — set in the worst case (all unique)
- **Correctness:** ✓

This is the "Python pro" answer. In an interview, **say it out loud first** before writing it: *"A set deduplicates, so if the set is smaller than the original list, there's at least one duplicate."* That demonstrates you understand WHY it works, not just that you memorized the trick.

## What an interviewer might push you on

After you write the one-liner, expect them to ask **"now do it without using `set()`."** Be ready with these in order of how "manual" they want:

```python
# 1. Hash set with early exit (slightly better in practice — bails on first dup)
def hasDuplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False
```

```python
# 2. Sorting (no extra space if you can mutate the input)
def hasDuplicate(nums):
    nums.sort()                          # O(n log n)
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False
```

```python
# 3. Brute force (only mention as the starting point, never as the answer)
# O(n²) — for every pair, check equality.
```

Knowing all three and being able to discuss the time/space tradeoff is the whole game on this problem.

## The pattern this teaches

**"Have I seen this before?"** A hash set turns that question into an O(1) lookup. The same trick shows up in:
- Cycle detection in linked lists (with extra space)
- Contains Duplicate II / III (duplicates within a window)
- Longest substring without repeating characters

Whenever you see "find/avoid duplicates," your default should be: *hash set unless space is constrained.*

## Question for you

If the array were 10 billion integers — way too big to fit a hash set in memory — but fits on disk as a sorted file, what's your approach? (Answer: sort-then-scan, comparing adjacent elements. That's why approach #2 above is worth knowing — it's the answer when memory is the constraint, not time.)

## Your turn — fill this in

> The whole reason this repo exists is the reflection. Two minutes, write honestly:

**What I tried first (before the working one):**

**Where I got stuck:**

**What made the Python one-liner click:**

**Revisit?** [ ] Mark if I want to redo this from scratch in a week.
