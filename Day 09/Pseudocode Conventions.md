---
aliases: [Logic and Problem-Solving - Day 09 Pseudocode Conventions]
tags: [logic-and-problem-solving, term1, pseudocode, cheat-sheet]
course: "[[Logic and Problem-Solving]]"
---

# Pseudocode Conventions (SDEV1000)

Standards to follow in every assessment. Concepts: [[Logic and Problem-Solving - Day 09]] · [[Pseudocode]]

## General
- **Keywords are UPPERCASE** (`DECLARE`, `INPUT`, `SET`)
- **Indent nested logic by one tab** (inside `IF`, loops, functions)
- **Every main program begins with `START` and ends with `END`**
- `END FOR` (with a space) is acceptable

## Variables
- **camelCase** — first word lowercase, later words capitalized; **no underscores or spaces**
- Names describe the contents; Booleans get an `is` / `has` prefix (`isGreater = True`)

| Action | Syntax |
|---|---|
| Declare | `DECLARE variableName` (or `INITIALIZE`) |
| Declare + assign | `DECLARE number = 0` |
| Update | `SET variableName = newValue` |
| Combine text | Variable **outside** the string, joined with `+`: `OUTPUT "Hello " + name + " You are " + age + " years old."` |

## INPUT
- `INPUT variableName`; several at once: `INPUT variableName1, variableName2`
- **No need to `DECLARE` first** — INPUT creates the variable; it can also overwrite an existing one

## OUTPUT
- `OUTPUT`, `DISPLAY`, or `PRINT` for text messages
- Images or interfaces: `OUTPUT` or `DISPLAY` (`DISPLAY profilePicture`)
- Anything else: `OUTPUT`

## Conditionals
- Condition goes between `IF` and `THEN`; **always end with `ENDIF`**; indent the body
- `ELSE` needs no `THEN`; `ELSEIF` **does** need `THEN`
- `ELSE` / `ELSEIF` line up with their `IF`; not every `IF` needs an `ELSE`
- Nested IFs must be indented too

```
IF <condition> THEN
	<statements>
ELSEIF <different condition> THEN
	<statements>
ELSE
	<statements>
ENDIF
```

## Loops
| Loop | Syntax | Notes |
|---|---|---|
| WHILE | `WHILE <condition>` … `ENDWHILE` | Runs while the condition is TRUE; may never run |
| DO-WHILE | `DO` … `WHILE <condition>` | Runs at least once; **no END needed** |
| DO-UNTIL / REPEAT-UNTIL | `DO` … `UNTIL <condition>` | Runs at least once; **no END needed** |
| FOR | `FOR <start> TO <end>` … `ENDFOR` | Known number of iterations; counter goes up by 1 |
| FOR with index | `FOR i = 0 TO length(myList) - 1` | Iterate a list by index |

Use `length(list)` for the number of items.

## Operators
- **Math:** `+` `-` `*` `/` `MOD`
- **Comparison:** `==` `!=` `>` `>=` `<` `<=`
- **Logical:** `AND` `OR` `NOT`

## Functions
- `FUNCTION name(params)` … `ENDFUNCTION`
- camelCase name that says what it does; **always include `()`** even with no parameters; parameters are camelCase too
- **One purpose per function**
- **Always include `RETURN`**, even when returning no value (`RETURN` alone)
- Call by name: `printHello()   //call the printHello() function`

```
FUNCTION printHello()
	OUTPUT "Hello"
	RETURN
ENDFUNCTION

START
printHello()
END
```

## Collections

**Lists** — 0-indexed, integer indices
| Action | Syntax |
|---|---|
| Empty list | `DECLARE students = []` |
| With data | `DECLARE numbers = [20, 18, 33, 18, 51]` |
| Read | `SET newVariable = numbers[index]` |
| Update | `SET numbers[index] = newValue` |
| Length | `DECLARE lengthOfList = length(listName)` |

**Dictionaries** — key/value pairs; access a value by its key
| Action | Syntax |
|---|---|
| Empty | `DECLARE Dictionary dictionaryName = {}` |
| With data | `DECLARE Dictionary studentData = {"Gurpreet": 35, "Samantha": 23}` |
| Add | `SET dictionaryName[newKey] = newValue` |
| Read | `PRINT dictionaryName[key]` |
| Update | `SET dictionaryName[key] = newValue` |

## To Know
- The document's DO-UNTIL note says it runs until the condition is FALSE, while the Day 09 slides' coffee example stops when the condition becomes true — confirm with the instructor

## Reflection
*What was the most surprising insight today?*
