---
aliases: [Logic and Problem-Solving - Day 10]
tags: [logic-and-problem-solving, term1, pseudocode]
course: "[[Logic and Problem-Solving]]"
---

# Logic and Problem-Solving — Day 10: Translating Flowcharts to Pseudocode

**Today's focus:** turn a finished flowchart into [[Pseudocode]] using the SDEV1000 conventions.

## [[Translating Flowcharts to Pseudocode|Translation]]

| Flowchart | Pseudocode |
|---|---|
| Start / End oval | `START` / `END` |
| Input parallelogram | `INPUT variable` |
| Output parallelogram | `OUTPUT message` |
| Process rectangle | `SET variable = …` |
| Decision diamond | `IF … THEN … ELSE … ENDIF` |
| Loop-back arrow | `WHILE … ENDWHILE` or `DO … UNTIL` |

## Practice Problems (Lesson 10)
1. **Going to the café** — order a muffin; if unavailable order a donut; then decide on coffee, pay and collect at each step
2. **Divisibility check** — validate two numbers with loops, then use `MOD` to see if one divides the other
3. **Unsubscribe from a streaming service** — log in if required (`DO … UNTIL` validated), go to settings, unsubscribe, log out

## Reminders From Marking Your Own Drafts
- Use `==` to compare and `SET` to assign; `AND` instead of `&&`
- `ELSEIF` needs a condition and `THEN`; plain `ELSE` has neither
- Every program ends with `END` (not a second `START`)
- Full rules: [[Logic and Problem-Solving - Day 09 Pseudocode Conventions]] · [[Logic and Problem-Solving - Day 09 Pseudocode Cheat Sheet]] · [[Logic and Problem-Solving - Master Reference]]

## To Know
- Translate symbol-by-symbol, then re-read each loop arrow to pick `WHILE` vs `DO … UNTIL`

## Reflection
*What was the most surprising insight today?*
