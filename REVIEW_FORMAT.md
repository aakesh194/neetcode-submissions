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
<2-4 sentences max: what's actually going on across submissions. Be honest. No fluff.>

## Submission-by-submission
### `submission-0.<ext>` — <one-line verdict>
```python
<paste the relevant snippet being critiqued — not the whole file, just the key part>
```
<Commentary: correctness, bugs, style issues quoting actual code, edge cases missed. Bullets where natural, inline where it flows better. Time and space complexity must be stated — name the exact operation causing it.>

**Interviewer take:**
<What's going through the interviewer's head watching this code get written live. Concrete — not vibes. Examples: "They'd pause at `if x in seen_list` and ask you to walk through the complexity, expecting you to catch it yourself." / "Writing `map = {}` would get flagged immediately — signals you haven't coded in Python recently." / "No explanation of why a set vs list — interviewer has to ask, which costs you points." / "Clean variable names, correct on first try, explained the tradeoff upfront — this is the submission that gets offers." Keep it 2-4 bullets max. If there's nothing real to say, skip the section entirely — don't fabricate interviewer reactions.>

### `submission-1.<ext>` — <one-line verdict>
```python
<relevant snippet>
```
<Same format.>

**Interviewer take:**
<Same format.>
...

## The textbook version
<Canonical optimal solution with code. Why does it work? Why do other approaches break down?>
<Call out wrong instincts this problem punishes.>
<Time and space complexity required here too.>

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

## Writing the "Interviewer take" section

This is not a vibe check — it's grounded in what actually signals red/green to interviewers. Use this rubric:

**Red flags interviewers actually care about:**
- Naming builtins (`map`, `list`, `set`) — signals inattention
- O(n) lookup in a list where a set would do — and not catching it yourself when asked
- Jumping to optimal without explaining brute force — interviewer has to drag it out of you
- No justification for data structure choice — they'll ask "why a dict here?" and you need a ready answer
- Variable names that require explanation (`a`, `tmp2`, `res2`) — slows the read, hurts signal
- Fixing bugs silently without narrating what you found — interviewer can't tell if you understood it

**Green flags interviewers remember:**
- Stating time/space upfront without being asked
- Catching your own complexity issue before they point it out
- Saying "I'll start with brute force so we're aligned on the tradeoff" before writing anything
- Clean names that make the logic self-documenting
- Explaining *why* a set over a list, not just using one

Keep the section tight — 2-4 bullets, only what's real for this specific submission. Don't manufacture feedback when the submission is clean.

---

## Before writing notes

Check PROGRESS.md. If the previous problem's "Question for you" was never answered in their "Your turn" section, call it out at the top of the new notes before moving on.

---

## What NOT to do

- Don't modify `submission-N.<ext>` or `README.md`
- Don't give solutions to problems they haven't attempted
- Don't overwrite a filled-in "Your turn" section — append or update other sections only
- Don't grade 10/10 — if everything is strong, push on interview framing or edge cases at scale
- Don't fill in "Interview check" or "Interviewer take" when there's nothing real to say
- Don't suggest restructuring the repo, switching languages, or adding tooling
- **Never skip Time/Space complexity** — required for every submission and the textbook version, no exceptions
- **Never write a submission critique without a code snippet** — anchor every comment to actual code
- **No pure prose paragraphs in submission critiques** — commentary should be tight, specific, and use bullets where natural