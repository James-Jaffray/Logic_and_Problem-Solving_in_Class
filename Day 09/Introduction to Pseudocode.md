---
aliases: [Logic and Problem-Solving - Day 09]
tags: [logic-and-problem-solving, term1, pseudocode]
course: "[[Logic and Problem-Solving]]"
---

# Logic and Problem-Solving — Day 9: Introduction to Pseudocode

**Today's focus:** write solutions in [[Pseudocode]] — the five constructs, variables, input, and comments. Syntax rules are in [[Logic and Problem-Solving - Day 09 Pseudocode Conventions]].

## What Is Pseudocode?
A way of writing a solution that **mimics real code but isn't tied to any language** — halfway between a programming language and human language. Its job is to communicate algorithmic logic in a structured way, as a step-by-step guide a developer can turn into real code.

## Pseudocode vs. [[Flowcharts]]

| | Flowcharts | Pseudocode |
|---|---|---|
| Format | Visual symbols and arrows | Structured natural language |
| Best for | High-level overview; shared by technical and non-technical people | Detailed logic; aimed at developers |
| Changing it | Difficult | **Easier to change** |
| Complexity | Hard to show complex algorithms | **Better for complexity and scalability** |
| Translation to code | Indirect | Almost line by line |

Pseudocode must still be readable without technical knowledge.

## Writing Pseudocode
- **First understand the problem and define the requirements** (inputs, outputs, processes, constraints)
- Made of single-line **statements** — **one statement per line**
- **Never use precise programming syntax**

## The Five Constructs

| Construct | Use | Key rules |
|---|---|---|
| **Sequence** | Linear steps, one after another | Each line is one step (input, output, calculation…) |
| **IF-THEN-ELSE** | Decisions (the flowchart diamond) | Indent inside blocks; **end with `ENDIF`** |
| **WHILE** | Repeat while a condition is true | Condition **at the start** → **may never run**; end with `ENDWHILE` |
| **DO-UNTIL** (a.k.a. REPEAT-UNTIL) | Repeat, checking after each pass | Condition **at the end** → **always runs at least once** |
| **FOR** | Repeat a known number of times, often over a list | End with `ENDFOR` |

```
IF sky is blue THEN
	PRINT "The sky is blue"
ELSE
	PRINT "The sky is not blue"
ENDIF
```

**WHILE vs DO-UNTIL:** WHILE checks *before* the sequence runs; DO-UNTIL checks *after*. Traffic light = WHILE (only stop if it's red). Stop sign = DO-UNTIL (you always stop at least once). See [[Loops]].

> The slides describe DO-UNTIL as repeating "while a condition is true", but the coffee example (`DO scroll TikTok UNTIL coffee brewed`) stops once the condition **becomes** true. Check which wording the assessments expect.

## Variables
- Containers for a value that can change; used in place of an actual value
- **Declaration** = give it a name; **initialization** = give it a value
- **No data types** in pseudocode
- Use descriptive names (a variable for a user's name is `name`, not `x`)

```
DECLARE age
SET age = 40        // declare, then initialize

DECLARE age = 50    // both in one statement
```

- `SET` changes an existing variable's value
- A variable in a condition means its **value** is checked (`number = 10` → `10 > 20` is false)

## User Input
- `INPUT variableName` stores what the user enters in a variable (new or existing)
- `INPUT` both declares and initializes a new variable
- `INPUT` on an existing variable **overwrites** its value
- Several inputs in one statement: `INPUT firstName, lastName`; join strings with `+`

## Comments
- Start with `//` — everything to the right on that line is **not part of the logic**
- Can sit on their own line or **inline** after a statement

## Conventions (summary)
One statement per line · indent to show hierarchy and nesting · programming-language independent · simple, readable, structured

## Examples from Class
- **Brewing coffee** — sequence with `INPUT`, a `DO … UNTIL` loop while the coffee brews, and an `IF milk is wanted THEN`
- **Treadmill** — `INPUT personWantsToRun`, then `WHILE personWantsToRun` run on treadmill

## To Know
- Pseudocode is compared directly with flowcharts — know an advantage of each

## Homework
- 

## Reflection
*What was the most surprising insight today?*
