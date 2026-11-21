---
aliases: [Logic and Problem-Solving - Day 21]
tags: [logic-and-problem-solving, term1, lecture-notes, algorithms, searching, counting]
course: "[[Logic and Problem-Solving]]"
day: 21
---

# Logic and Problem-Solving — Day 21: Standard Algorithms, Part 1

**Today's focus:** [[Standard Algorithms]] are well-established, efficient solutions for searching, sorting and counting. Today: [[Search Algorithms|linear search, binary search]] and counting.

**Objectives:** explain standard algorithms · design search and counting algorithms

## Linear Search
Check each item **one at a time** until found. Use for **small or unsorted** data (e.g. finding the six of hearts in a shuffled deck). Easy to write, slow on big data.

```
START
INPUT listOfNumbers
INPUT numberToSearch
DECLARE numberExists = false
FOR each number in listOfNumbers
	IF numberToSearch == number
		SET numberExists = true
	ENDIF
ENDFOR
IF numberExists == true
	PRINT "The number is in the list"
ELSE
	PRINT "The number is not in the list"
ENDIF
END
```

## Binary Search
For **large, sorted** data. Compare the target to the **middle** item, throw away the half that can't contain it, repeat.
- Searching `3` took 3 steps (linear: 4). For `7`: 3 steps vs 8.
- With an even number of items, either middle item is fine
- Tells you *whether* a value exists, **not how many times** it appears
- Needs sorted data. See [[Sorting Algorithms]]

```
START
INPUT listOfNumbers        // sorted
INPUT numberToSearch
DECLARE low = 0
DECLARE high = length(listOfNumbers) - 1
DECLARE found = False
DECLARE mid
WHILE low <= high AND NOT found
	SET mid = (low + high) / 2 rounded down
	IF listOfNumbers[mid] == numberToSearch THEN
		SET found = True
	ELSE IF numberToSearch > listOfNumbers[mid] THEN
		SET low = mid + 1
	ELSE IF numberToSearch < listOfNumbers[mid] THEN
		SET high = mid - 1
	ENDIF
ENDWHILE
END
```

## Counting
A linear search that **counts** instead of flagging: it must check every item.
```
DECLARE count = 0
FOR each number in listOfNumbers
	IF numberToSearch == number
		SET count = count + 1
	ENDIF
ENDFOR
PRINT "There were " + count + " instances of the number " + numberToSearch
```
Pattern for **mode**: loop once to build a frequency dictionary (`IF number exists → +1 ELSE → 1`), loop over the dictionary keeping the highest count and its number.

## Choosing an algorithm
| Situation | Use |
|---|---|
| Unsorted data (e.g. store inventory with items appended at the end) | Linear search |
| Large sorted data, existence check | Binary search |
| How many times something appears | Counting (linear pass) |
| Counting values in a dictionary (cars by colour) | Loop over keys, compare `carDictionary[CarId]` |

## To Know
- [ ] Linear vs binary: when each applies, and why binary needs sorted data
- [ ] Counting = linear search + counter
- [ ] Write each in pseudocode and as a flowchart

## Homework
- Lesson 21 sample problems: antique store inventory search, count cars by colour, mode of a list, binary search pseudocode

## Reflection
*What was the most surprising insight today?*
