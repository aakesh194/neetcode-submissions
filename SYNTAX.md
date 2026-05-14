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