---
aliases: [Logic and Problem-Solving - Day 09 Pseudocode Cheat Sheet]
tags: [logic-and-problem-solving, term1, pseudocode, cheat-sheet]
course: "[[Logic and Problem-Solving]]"
---

# Pseudocode Cheat Sheet

Full rules: [[Logic and Problem-Solving - Day 09 Pseudocode Conventions]] · Concepts: [[Logic and Problem-Solving - Day 09]]

## Accepted Keywords (always UPPERCASE)

| Purpose | Accepted words |
|---|---|
| Program boundaries | `START` … `END` |
| Create a variable | `DECLARE`, `INITIALIZE` |
| Change a variable | `SET` |
| Get input | `INPUT` |
| Show output | `OUTPUT`, `DISPLAY`, `PRINT` |
| Decisions | `IF` `THEN` `ELSEIF` `ELSE` `ENDIF` |
| While loop | `WHILE` … `ENDWHILE` |
| Do-while loop | `DO` … `WHILE` |
| Do-until loop | `DO` … `UNTIL`, or `REPEAT` … `UNTIL` |
| For loop | `FOR` `TO` … `ENDFOR` (`END FOR` also OK) |
| Functions | `FUNCTION` … `ENDFUNCTION`, `RETURN` |
| Collections | `DECLARE Dictionary` |
| Logical operators | `AND` `OR` `NOT` |
| Math operators | `+` `-` `*` `/` `MOD` |
| Comparison operators | `==` `!=` `>` `>=` `<` `<=` |
| Helper function | `length(list)` |
| Comment | `//` |

## Which Word Ends What

| Structure | Ender |
|---|---|
| Whole program | `END` |
| `IF` (incl. `ELSEIF` / `ELSE`) | `ENDIF` |
| `WHILE` | `ENDWHILE` |
| `FOR` | `ENDFOR` |
| `FUNCTION` | `ENDFUNCTION` |
| `DO … WHILE` / `DO … UNTIL` / `REPEAT … UNTIL` | none needed |

## Syntax Skeletons

```
START
	DECLARE count = 0          // declare + assign
	SET count = count + 1      // update
	INPUT firstName, lastName  // no DECLARE needed
	OUTPUT "Hi " + firstName   // variable outside the string

	IF count > 5 THEN
		PRINT "big"
	ELSEIF count == 5 THEN
		PRINT "five"
	ELSE
		PRINT "small"
	ENDIF

	WHILE isRunning
		<statements>
	ENDWHILE

	DO
		<statements>
	UNTIL isDone

	FOR i = 0 TO length(myList) - 1
		myList[i]
	ENDFOR
END
```

```
FUNCTION addNumbers(firstNumber, secondNumber)
	RETURN firstNumber + secondNumber
ENDFUNCTION
```

Lists: `DECLARE numbers = [20, 18, 33]` · read `numbers[0]` · update `SET numbers[0] = 5`
Dictionaries: `DECLARE Dictionary ages = {"Sam": 23}` · read `ages["Sam"]` · add/update `SET ages["Ali"] = 30`

## Quick Rules
- **camelCase** names, no underscores or spaces; Booleans start with `is` / `has`
- **One statement per line**; indent nested logic by **one tab**
- **No data types**, no real programming syntax
- Functions: **one purpose**, **always `()`**, **always `RETURN`** (even empty)
- `ELSEIF` needs `THEN`; `ELSE` doesn't
- Lists are **0-indexed**
