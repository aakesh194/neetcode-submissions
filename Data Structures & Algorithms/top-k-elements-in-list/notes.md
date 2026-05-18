# Top K Frequent Elements — Coach Notes

- **Problem:** https://leetcode.com/problems/top-k-frequent-elements/
- **Pattern:** Arrays & Hashing / Heap (Priority Queue)
- **Difficulty:** Medium
- **Submissions:** 4 (Python)

> **Carry-forward flag:** The anagram-groups "Question for you" (the `ord(c) - ord('a')` walkthrough for `"eat"`) was never answered — "Your turn" is still partially blank. Fill that in before you redo anagram-groups.

## Verdict

Sub-0 was a genuine independent attempt. The frequency-counting step was clean — `defaultdict(int)` used correctly, which is a real sign the anagram-groups pattern landed. But the extraction logic (how to get the top-k from that freq map) is fundamentally broken in a way that wouldn't produce correct output for any input. Subs 1, 2, and 3 all looked at the solution. Three different valid approaches — sort, min-heap, bucket sort — are represented across them. The comment in sub-2 shows the heap logic wasn't fully understood. The counting step has clicked. The extraction step has not been independently solved yet. **Assist level: sub-0 independent (broken) / sub-1, sub-2, sub-3 looked up solution.**

---

## Submission-by-submission

### `submission-0.py` — Right start, broken extraction

```python
freq = defaultdict(int)
for num in nums:
    freq[num] += 1

list = []
for j in range(0, k):
    for i in range(len(freq)):
        value = 0
        if freq[i] > value:
            value = i;
    list.append(value)
    i = i+1
```

- `defaultdict(int)` for freq counting — correctly applied. That's the anagram-groups pattern carrying over. Credit that.
- Everything after the freq build is broken. Walk through what happens:
  - `value = 0` resets inside the outer loop every pass, so you're never tracking a running max across iterations.
  - `freq[i]` iterates over indices 0, 1, 2, ... `len(freq)-1`. But `freq` is keyed by the *actual numbers in nums*, not by positional index. For `nums = [1,1,2,3]`, `freq = {1:2, 2:1, 3:1}`. `freq[0]` auto-creates a 0 entry — it doesn't mean "the number 0 appeared 0 times," it means you just created a spurious key.
  - `value = i` sets `value` to the *index* `i`, not the *frequency* `freq[i]`. So even if the loop ran correctly, you'd be collecting index numbers, not the actual top-k elements.
- The instinct to scan freq and extract the max in a loop is the right impulse — the implementation just missed that freq keys aren't positional integers.
- Open style debts all present: `list = []` shadows the builtin, `range(len(freq))` instead of iterating directly, trailing semicolon on `value = i;`.

**Time:** Broken — would be O(n·k) if corrected, but produces wrong output. **Space:** O(n) for freq.

**Interviewer take:**
- Using `defaultdict` cleanly and explaining *why* (vs. a manual `get()` guard) is a green flag — that's what an interviewer wants to see from the first step.
- `list = []` would get flagged immediately. It blocks a builtin and signals you haven't written Python recently.
- The extraction logic bug — iterating `range(len(freq))` against a non-integer-indexed dict — is the kind of thing an interviewer would probe with "walk me through what this returns for `nums = [1,1,2,3]`." You'd need to catch it yourself.

---

### `submission-1.py` — Correct, sorting approach

```python
count = {}
for num in nums:
    count[num] = 1 + count.get(num, 0)

arr = []
for num, cnt in count.items():
    arr.append([cnt, num])
arr.sort()

result = []
while len(result) != k:
    result.append(arr.pop()[1])
return result
```

- Comment says `#lwk looked at solution`. Noted.
- The approach is correct and readable: build `[count, num]` pairs, sort ascending, pop the last k entries (highest counts).
- `arr.pop()` on a sorted list gives you the largest — clean use of the default sort + reverse-pop pattern.
- `count.get(num, 0)` works fine, though `defaultdict(int)` is more idiomatic at this point.
- `arr.sort()` with no key sorts by first element (`cnt`) by default — that's what you want here.
- No style debt issues in this submission. Variable names are clear.

**Time:** O(n log n) — the sort dominates. **Space:** O(n) for `arr`.

**Interviewer take:**
- Explaining upfront "I'll sort by frequency and pop the k largest — it's O(n log n), but there's a faster way with a heap or bucket sort" is exactly the kind of tradeoff narration an interviewer rewards. Starting with the sorting solution and naming the alternatives shows range.
- Not stating the complexity unprompted means the interviewer has to ask. Answer before they do.

---

### `submission-2.py` — Heap approach, one conceptual gap

```python
heap = []
for num in count.keys():
    heapq.heappush(heap, (count[num], num))
    if len(heap) > k:
        heapq.heappop(heap)

res = []
for i in range(k):
    res.append(heapq.heappop(heap)[1])
return res
```

- This is a correct O(n log k) min-heap approach. Python's `heapq` is a min-heap — it keeps the *smallest* element at the root.
- The first `heappop` (inside the build loop): when the heap exceeds size k, remove the minimum. This keeps only the k *largest* counts in the heap at all times. After the loop, heap contains exactly the k most frequent elements.
- The second `heappop` (result extraction loop): now you're draining the heap to collect results. The comment `#why do we pop again if we did it on line 11 and then append` shows the two pops felt redundant — they're not. First pop = pruning (keep only top-k). Second pop = reading (extract what's left). Completely different purposes.
- Two `heappop`s, two jobs. See SYNTAX.md for the heapq pattern.

**Time:** O(n log k) — each push/pop into a size-k heap is O(log k). **Space:** O(n + k).

**Interviewer take:**
- Using a min-heap to solve a "top-k" problem is a pattern interviewers expect you to reach for. Naming it and stating the complexity improvement over sorting (O(n log k) vs O(n log n)) is the response that lands.
- The comment reveals the second heappop wasn't understood. In an interview, if you write code you can't explain line-by-line, an interviewer will ask — and "I'm not sure why" is a hard hole to dig out of.

---

### `submission-3.py` — Bucket sort, optimal, looked up

```python
count = {}
freq = [[] for i in range(len(nums) + 1)]

for num in nums:
    count[num] = 1 + count.get(num, 0)
for num, cnt in count.items():
    freq[cnt].append(num)

res = []
for i in range(len(freq) - 1, 0, -1):
    for num in freq[i]:
        res.append(num)
        if len(res) == k:
            return res
```

- Comment: `#both this submission and the one before i looked at solution`. Noted.
- `freq = [[] for i in range(len(nums) + 1)]` — a bucket at index `i` holds all numbers that appear exactly `i` times. Max possible frequency is `len(nums)` (every element is the same), so `len(nums) + 1` buckets covers all cases.
- Iterating `freq` from high to low collects the most frequent first — early return when k is hit.
- This is the optimal solution: no sorting, no heap, no comparisons beyond counting. Just two linear passes and a linear traversal.

**Time:** O(n) — counting is O(n), bucketing is O(n), collection is O(n). **Space:** O(n) for count + freq.

**Interviewer take:**
- Arriving at bucket sort independently would be a strong signal. The insight — "frequency is bounded by n, so I can use it as an array index" — is non-obvious and worth explaining explicitly.
- Since it was looked up, the test is whether you can reproduce it from memory and explain *why* `len(nums) + 1` buckets are sufficient. That's the follow-up question you should be ready for.

---

## The textbook version

Three approaches, in order of increasing sophistication:

**Approach 1 — Sort (O(n log n)):**
```python
from collections import defaultdict

def topKFrequent(nums, k):
    count = defaultdict(int)
    for num in nums:
        count[num] += 1
    return [num for num, cnt in sorted(count.items(), key=lambda x: x[1], reverse=True)[:k]]
```
Simple but slower — the sort dominates everything else.

**Approach 2 — Min-heap (O(n log k)):**
```python
import heapq
from collections import defaultdict

def topKFrequent(nums, k):
    count = defaultdict(int)
    for num in nums:
        count[num] += 1

    heap = []
    for num, cnt in count.items():
        heapq.heappush(heap, (cnt, num))
        if len(heap) > k:
            heapq.heappop(heap)   # drop the least frequent — pruning step

    return [num for cnt, num in heap]   # what's left is the top-k
```
Better when k is small relative to n. Each push/pop is O(log k).

**Approach 3 — Bucket sort (O(n)):**
```python
from collections import defaultdict

def topKFrequent(nums, k):
    count = defaultdict(int)
    for num in nums:
        count[num] += 1

    freq = [[] for _ in range(len(nums) + 1)]   # index = frequency
    for num, cnt in count.items():
        freq[cnt].append(num)

    res = []
    for i in range(len(freq) - 1, 0, -1):        # high freq to low
        for num in freq[i]:
            res.append(num)
            if len(res) == k:
                return res
```
Optimal. Works because frequency is bounded by n — so you can use it as an array index directly. No sort, no heap.

The wrong instinct: scanning the freq map repeatedly to find the next max (O(n·k)), or comparing elements pairwise. Frequency problems almost always want a map-then-extract structure, not nested scanning.

---

## Style fixes (apply going forward)

- **`list = []`** — `list` is a Python builtin. Use `result`, `res`, `output`. This is the fifth problem where a builtin has been shadowed (`map`, `list`).
- **Trailing semicolons** — `value = i;` in sub-0. Still showing up. Drop them.
- **`range(len(freq))` on a non-integer-indexed dict** — this was the root of the sub-0 bug. `defaultdict` keys are what you inserted; they're not guaranteed to be 0..n-1. Iterate `freq.items()` or `freq.keys()` if you need the actual keys.

---

## The pattern + where else it shows up

**Frequency map + extraction by rank.** The counting step (hashmap → freq) is one unit of work. The extraction step (how to pull top-k from that map) is a separate problem with multiple solutions at different complexity levels. Knowing all three extraction options (sort, heap, bucket) and when to reach for each is the real skill here.

Same build-then-extract instinct in NC150:
- **Anagram Groups** — build a canonical-key map, then extract grouped values
- **Two Integer Sum** — build a complement map, then extract matching pairs  
- **Kth Largest Element in a Stream** — ongoing top-k maintenance with a heap

---

## Interview check

- The counting step is solid. The bottleneck is the extraction step — know all three approaches and their tradeoffs before going into an interview.
- If you use the heap approach, be ready to explain both heappops in plain English without hesitating.
- If you use bucket sort, be ready to explain why `len(nums) + 1` buckets are sufficient.

---

## Question for you

In sub-0, you built `freq` with `defaultdict(int)` and then tried to extract the top-k by iterating `range(len(freq))`. Walk through what `freq` actually looks like for `nums = [3,3,1,2]` — what are its keys and values? Then explain why `freq[0]` and `freq[1]` give you something unexpected in that loop. What would you need to iterate over instead to look at every (number, count) pair?

---

## Your turn — fill this in

*(Pre-filled from your submission comments — finish the rest in your own words.)*

**What I tried first:** Built a freq map with `defaultdict(int)` (sub-0) — that part worked. Then tried to scan it by iterating `range(len(freq))` to find the top-k, which broke because freq keys are actual numbers, not positional indices.

**Where I got stuck:** After counting frequencies, the extraction step — how do you actually get the k most frequent out of a dict? Sub-0 shows the attempt stalled here.

**What made it click:** *(your words — was it seeing the [cnt, num] sort trick? the heap pruning logic? realizing frequency is bounded by n for bucket sort? write it here.)*

**Revisit?** [x] Mark for redo in 1 week — sub-1/2/3 all required looking at the solution. The counting instinct is solid; the extraction strategies (sort, heap, bucket sort) need to be independently reproducible.
