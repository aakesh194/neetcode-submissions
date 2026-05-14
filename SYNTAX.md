# SYNTAX.md — Python patterns aakesh has gaps in

Maintained by the coach. Added to when submission comments or code reveal a syntax gap. Never edited by the user.

---

## defaultdict
Use when you want a dict that auto-initializes missing keys — no need to check if key exists first.
```python
# instead of:
if key not in d:
    d[key] = 0
d[key] += 1

# use:
from collections import defaultdict
d = defaultdict(int)   # int → default 0
d[key] += 1

# also useful:
d = defaultdict(list)  # list → default []
d[key].append(val)
```

---

## ''.join(sorted(s))
Sorts a string's characters alphabetically and rejoins as a new string. Common for anagram checks.
```python
# sorted(s) → list of chars in alphabetical order
# ''.join(...) → collapses list back into a string

''.join(sorted("anagram"))  # → 'aaaganmr'
''.join(sorted("nagaram"))  # → 'aaaganmr'  (same → anagram)
```

---

## tuple() as a dict key
Use when you need to use a list as a dict key — lists aren't hashable, tuples are.
```python
# instead of: res[count]  → TypeError: unhashable type: 'list'

# use:
res[tuple(count)]  # tuple is immutable → hashable → valid dict key

# common pattern: fixed-size count array as a canonical key
count = [0] * 26
for c in s:
    count[ord(c) - ord('a')] += 1
res[tuple(count)].append(s)
```

---

## dict.values() and list()
`dict.values()` returns a *view* — a live reference to the dict's values, not a standalone list.
```python
# if the return type needs List[...], wrap it:
return list(res.values())   # converts view → actual list

# res.values() alone works for iteration, but not when a list is required
```

---