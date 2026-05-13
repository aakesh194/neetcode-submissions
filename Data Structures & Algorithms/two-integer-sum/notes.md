# Two Sum (NeetCode 1) — Coach Notes

- **Problem:** https://leetcode.com/problems/two-sum/
- **Pattern:** Arrays & Hashing
- **Difficulty:** Easy
- **Your submissions:** 3 (all Python)

---

## Honest verdict

The progression here is the most instructive of your three problems: **brute force → hashmap with a real bug → bug caught and fixed.** Catching your own bug between submission-1 and submission-2 is the single most important moment in this whole repo so far. That's the actual skill of being an engineer.

But each one has stuff to dig into.

## Submission-by-submission

### `submission-0.py` — brute force, slightly broken

```python
for i in range(len(nums)):
    for j in range(1, len(nums)):       # ← bug: should be range(i+1, len(nums))
        if i != j:
            if nums[i] + nums[j] == target:
                list = [i, j];          # ← `list` is a Python builtin, don't shadow it
                return list;
# ← no `return []` at the end if no pair found
```

**Three issues:**

1. **Inner loop should start at `i + 1`**, not `1`. As written, you're checking every pair *twice* (once as `(i, j)` and once as `(j, i)`). It still works because LeetCode accepts either order, but it's 2x slower than needed.
2. **`list = [i, j]`** — `list` is a builtin Python type. Shadowing it inside a function is mostly harmless here but it's a bad habit. Just `return [i, j]`.
3. **No final `return`.** If no pair is found, this returns `None`. LeetCode guarantees a solution so it passes, but defensively you should always have a fallback (`return []`).

**Complexity:** O(n²) time, O(1) space.

### `submission-1.py` — hashmap, with a real bug

```python
map = {};                                # ← `map` is a builtin too
for i in range(len(nums)):
    map[nums[i]] = i;
for i in range(len(nums)):
    comp = target - nums[i]
    if comp in map and comp != nums[i]:  # ← BUG: comparing values instead of indices
        return [i, map[comp]];
```

**The bug:** `comp != nums[i]` checks if the complement *value* differs from the current *value*. That sounds reasonable, but it breaks on duplicates.

**Example:** `nums = [3, 3]`, `target = 6`.
- `i = 0`, `nums[i] = 3`, `comp = 3`. `comp in map` ✓. But `comp != nums[i]` → `3 != 3` → False. Skipped.
- `i = 1`, same. Skipped. Returns nothing (bug).

The right check is **"don't pair an element with *itself by index*"** — `map[comp] != i`. You caught this in submission-2. Big credit. The lesson here: **always test your code mentally against `[3, 3, target=6]` or any case with duplicates** before assuming it works.

### `submission-2.py` — bug fixed, correct

```python
map = {};
for i in range(len(nums)):
    map[nums[i]] = i;
for i in range(len(nums)):
    comp = target - nums[i]
    if comp in map and map[comp] != i:   # ← fixed: index comparison
        return [i, map[comp]];
return [];
```

**This is correct.** Time O(n), space O(n).

But it's still two passes. The textbook Two Sum is **one pass**. Here's why one-pass is better, not just shorter:

```python
def twoSum(self, nums, target):
    seen = {}                            # value -> index of values we've already passed
    for i, num in enumerate(nums):
        comp = target - num
        if comp in seen:                 # comp must have been earlier (different index)
            return [seen[comp], i]
        seen[num] = i                    # add AFTER the check
    return []
```

**Why this avoids the duplicate trap automatically:** because you only check against elements you've *already seen*, the indices are guaranteed different. No need for the `map[comp] != i` check. Cleaner, faster (one pass instead of two), and the structure makes the correctness obvious.

This one-pass version is the answer interviewers expect. Memorize the shape of it — it's a template you'll reuse a dozen times in NeetCode 150.

## Style fixes (same as the other problems — let's make these stick)

1. **`map = {}` → `seen = {}`.** Don't shadow builtins.
2. **`list = [i, j]` → just `return [i, j]`.** Same reason.
3. **Drop trailing semicolons.** Pythonic code never has them.
4. **Use `enumerate(nums)`** instead of `range(len(nums))` when you need index + value. Faster and more readable:

```python
for i, num in enumerate(nums):       # ✓
    ...
# vs
for i in range(len(nums)):           # ✗ (works but reads as "I wrote this like Java")
    num = nums[i]
```

## The pattern this teaches

**Hashmap complement search.** This is THE pattern of Arrays & Hashing — possibly the most reused pattern in the entire 150. The shape is always:

> *"For each element, what would I need to pair with it? Have I already seen that?"*

Variations:
- **Two Sum** (this one): find pair summing to target
- **3Sum**: fix one number, then Two Sum on the rest
- **4Sum**: fix two numbers, then Two Sum on the rest
- **Longest substring without repeating characters**: "have I seen this char in my current window?"
- **Subarray sum equals K**: "for current prefix sum, have I seen a prefix sum that's `current - k`?"

Get *very* comfortable with one-pass hashmap-of-complements. You'll thank yourself in 40 problems.

## Question for you

If the input array is **sorted**, the hashmap is no longer optimal — you can do it in O(n) time with **O(1) space**. How? (This is literally the next problem on the NeetCode list: Two Sum II — Input Array Is Sorted. Hint: two pointers, one at each end, move based on whether sum is too small or too large.)

## Your turn — fill this in

**What I tried first (before the working one):**

**What was I thinking when I wrote `comp != nums[i]` — what made me catch it?**
> This is the most valuable thing to reflect on. The act of catching that bug is what good engineers do.

**Why does the one-pass version not need the `!= i` check?**
> If I can explain this in writing, I've actually learned the pattern.

**Revisit?** [ ] Mark to redo from scratch in a week.
