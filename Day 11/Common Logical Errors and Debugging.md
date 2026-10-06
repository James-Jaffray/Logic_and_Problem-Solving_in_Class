---
aliases: [Logic and Problem-Solving - Day 11]
tags: [logic-and-problem-solving, term1, pseudocode, debugging]
course: "[[Logic and Problem-Solving]]"
---

# Logic and Problem-Solving — Day 11: Common Logical Errors and Debugging Techniques

**Today's focus:** spot [[Logical Errors and Debugging|logical errors]] in [[Pseudocode]], fix them with a structured debugging approach, then refine the result.

**Objectives:** identify common logical errors · apply systematic debugging to locate and fix them · verify pseudocode is correct

## Logical Errors
A flaw in the **algorithm's design** that causes incorrect or unexpected behaviour. Pseudocode has no language syntax to break, so logic errors are the main kind you'll hit. Typical causes:
- Incorrect comparisons
- Logic in the wrong order
- A single missing line

Some are obvious, some are subtle — exposure to more examples makes them easier to spot.

### Example 1 — Count to 10 (off-by-one)
```
WHILE number < 10        // prints 1–9, never 10
```
Loop exits the moment `number` reaches 10. **Fix:** `<` → `<=`.

### Example 2 — Sum 1 to N (user enters 5 → 1+2+3+4+5 = 15)
Two errors:
1. `sum` was **never declared** (can't use a variable before declaring/initializing it)
2. The loop **never adds** to `sum`

```
DECLARE counter = 1
DECLARE sum = 0              // fix 1: initialize to 0
INPUT number
DO
	sum = sum + counter      // fix 2: accumulate
	counter = counter + 1
UNTIL counter == number
PRINT sum
```
> Check the exit condition: with `UNTIL counter == number` the loop stops *before* adding `number` (5 → 10, not 15). `UNTIL counter > number` gives the correct total.

### Infinite Loops
A loop with **no way out**, usually from a logic error. Can crash an application (eats memory).
```
DECLARE counter = 1
WHILE counter > 0          // always true...
	PRINT "Hello"
	counter = counter + 1  // ...because counter only goes up
ENDWHILE
```
If the loop condition is always true, the loop always runs. See [[Loops]].

## Debugging
The process of troubleshooting code — finding the cause of errors and fixing them. A core developer skill. (Name comes from a moth found inside a 1940s computer; removing it "debugged" the machine.)

### Debugging Steps
1. **Understand the problem**
2. **Determine the requirements** — inputs, processes, outputs, constraints ([[IPO Model]])
3. **Focus on small pieces at a time** — fix one issue, then the next
4. **Verify** the solution meets every requirement, one at a time
5. **Refine** the solution if necessary (use this liberally)

Errors can be one line (count-to-10) or spread over several places (sum example).

## Worked Example — Generation Calculator
**Problem:** user enters their age; repeatedly ask until it's positive (print an error on a negative number); then print their generation.

| Generation | Age |
|---|---|
| Baby Boomer | 60+ |
| Gen X | 45–60 |
| Millennial | 29–44 |
| Gen Z | 13–28 |
| Gen Alpha | 0–12 |

**Requirements:** Input = age · Process = validate input, repeat until positive, conditionals on age · Output = generation message · Constraints = age > 0, ranges above.

### Debugging — age input
| Bug | Fix |
|---|---|
| Error prints if age is **greater** than 0 | `IF age <= 0 THEN` |
| Loop repeats `UNTIL age >= 0` — 0 isn't positive | `UNTIL age > 0` |

### Debugging — generation check
| Bug | Fix |
|---|---|
| Gen X check used `> 34` | `> 44` |
| Millennial check included 28; missing `THEN`; printed "Gen Alpha" | `> 28` (or `>= 29`); add `THEN`; print "Millennial" |
| Gen Alpha message missing | Use a plain `ELSE` — no other conditions left (an `ELSE IF age >= 0` also works but is unnecessary) |
| No `ENDIF` | Every `IF` block needs one |

Baby Boomer (`> 60`) and Gen Z checks were already correct.

### Refinement (works, but could be better)
- **Indent** everything inside the `DO … UNTIL` loop
- Make the error message **user-friendly** — words, not `>` symbols
- Be **consistent** — pick all `>` or all `>=` across the IF chain (when the operator changes, the number must change too: `>= 45` becomes `> 44`)

### Final Solution
```
START
DECLARE age
DO
	INPUT age
	IF age <= 0 THEN
		PRINT "You must enter a number greater than 0"
	ENDIF
UNTIL age > 0
IF age > 60 THEN
	PRINT "You are a Baby Boomer"
ELSE IF age > 44 THEN
	PRINT "You are Gen X"
ELSE IF age > 28 THEN
	PRINT "You are a Millennial"
ELSE IF age > 12 THEN
	PRINT "You are Gen Z"
ELSE
	PRINT "You are Gen Alpha"
ENDIF
END
```

## Refactoring
Going back to **working code and improving it**. Needed as apps grow and old design patterns stop fitting.
- Time consuming (a major refactor can take weeks or months)
- Risk of introducing new errors
- Partly avoidable by writing code right the first time — think **scalability, efficiency, ease of understanding**

## Practice Problems (Lesson 11)
Identify the errors, fix each one, write the completed pseudocode.
1. **Librarian sorting books** — `numberOfBooks` vs `numBooks` mismatch; no `counter` increment; `ENDWHILE` missing (`END` used instead); "Other" category shelved on B instead of D
2. **Charity donations** — `total` never accumulates (`donation + donation`); `counter` never declared; `UNTIL counter > numHouses` overshoots by one; silver check uses `=` instead of a range; bronze/silver/gold ranges and the gold gift certificate don't match the problem
3. **Property tax** — `actualPropertyValue` never converted from thousands (× 1000); tax is `value * 1.1` (adds tax to the value) instead of `value * 0.10`; the 500–999 and 200–499 branches don't match the ranges; `ELSE IF` branches mix up which variable they test; `DECLARE taxAmount` is buried inside one branch

## To Know
- **Quiz 3** is released after class and **due Friday**; there's also an **in-class assessment Friday** (similar format to the first). Both cover content **including today**
- `=` is assignment (`counter = counter + 1`, `DECLARE total = 23`); `==` is comparison
- An `IF` that belongs in a loop must be **inside** the loop
- Debug one small piece at a time against the requirements, then refine
- Related: [[Translating Flowcharts to Pseudocode]], [[Loops]], [[Conditionals]]

## Homework
- Quiz 3 (due Friday)

## Reflection
*What was the most surprising insight today?*
