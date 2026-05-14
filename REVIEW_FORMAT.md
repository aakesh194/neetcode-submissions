# REVIEW_FORMAT.md

Format and tone rules for writing `notes.md`. Follow this every time.

---

## notes.md template

```markdown
# <Problem Name> — Coach Notes

- **Problem:** <leetcode URL>
- **Pattern:** <e.g. Arrays & Hashing, Two Pointers>
- **Difficulty:** Easy / Medium / Hard
- **Submissions:** <count> (<language>)

## Verdict
<One paragraph: what's actually going on across submissions. Be honest.>

## Submission-by-submission
### `submission-0.<ext>` — <one-line verdict>
<Correctness, bugs, complexity (name the operation causing it), style issues with line refs, edge cases missed>

### `submission-1.<ext>` — <one-line verdict>
...

## The textbook version
<Canonical optimal solution with explanation. Why does it work? Why do other approaches break down? Show the code.>
<If relevant: what wrong instincts does this problem punish — sorting when unnecessary, two pointers before ordering, etc.>

## Style fixes (apply going forward)
<Bullet list. Pull from open style debts in COACH.md plus anything new this submission introduced.>

## The pattern + where else it shows up
<Name the pattern explicitly. Connect to 2-3 other NC150 problems that use the same instinct.>

## Interview check
<Only include if there's something real to say. Skip if the submission is clean.>
- Did you explain brute force before optimizing?
- Did you justify your data structure choice?
- Could another engineer follow your variable names without asking?

## Question for you
<One specific question that tests whether they actually internalized it. Not a softball.>

## Your turn — fill this in
**What I tried first:**
**Where I got stuck:**
**What made it click:**
**Revisit?** [ ] Mark for redo in 1 week
```

---

## Tone

- Supportive but firm — senior who wants them to actually get good
- **Specific over generic:** "your `if x in seen_list` is O(n) because `seen_list` is a list — use a set" beats "this could be faster"
- **Credit real wins** — catching their own bugs, trying multiple approaches. Don't flatter; do acknowledge.
- **Push on shallow reflection.** Empty "Your turn" section = call it out kindly. That section is the whole point.
- No emoji unless aakesh uses one first. Use his name sparingly.

---

## What NOT to do

- Don't modify `submission-N.<ext>` or `README.md`
- Don't give solutions to problems they haven't attempted
- Don't overwrite a filled-in "Your turn" section — append or update other sections only
- Don't grade 10/10 — if everything is strong, push on interview framing or edge cases at scale
- Don't fill in "Interview check" or add sections when there's nothing real to say
- Don't suggest restructuring the repo, switching languages, or adding tooling