---
aliases: [Logic and Problem-Solving - Day 22]
tags: [logic-and-problem-solving, term1, lecture-notes, algorithms, recursion, sorting]
course: "[[Logic and Problem-Solving]]"
day: 22
---

# Logic and Problem-Solving — Day 22: Standard Algorithms, Part 2

**Today's focus:** [[Recursion]] and two [[Sorting Algorithms]]: bubble sort and merge sort. Sorting is what makes the faster binary search from [[Standard Algorithms Part 1|Day 21]] possible. Visualize them at visualgo.net/en/sorting.

## Recursion
A function that **calls itself**. Every recursive function **must have an exit condition** (base case) or it runs forever, like a `WHILE` that never ends.

```
FUNCTION exp(num, pow)
	IF pow = 0
		RETURN 1
	ELSE
		RETURN num * exp(num, pow - 1)
	ENDIF
ENDFUNCTION
```
Trace `exp(2, 3)`: calls stack up (`2 * exp(2,2)` → `2 * exp(2,1)` → …) until the base case, then the return values **bubble back up** to the original caller → **8**. This replaces the `FOR` loop version.

## Bubble Sort
Simplest and **least efficient**. Repeatedly compare **adjacent** items and swap if out of order. Two nested `FOR` loops (`i` outer, `j` inner); the inner loop restarts and runs to completion each time `i` advances. Fine for small lists, avoid for large ones.
```
FOR i = 0 TO length(myList) - 2
	FOR j = 0 TO length(myList) - 2 - i
		IF (myList[j] > myList[j + 1])
			SWAP myList[j] and myList[j + 1]
		ENDIF
	ENDFOR
ENDFOR
```
**Descending order:** just flip the comparison to `<`.

## Merge Sort
**Divide and conquer** (like binary search): split the list in half repeatedly until each piece has 1 item, then recursively merge sorted pairs back together. Most efficient of the two, the choice for large data sets, but harder to write. Needs two functions:
- `MergeSort(list)`: base case `length <= 1`; sort left half, sort right half, `RETURN Merge(left, right)`
- `Merge(left, right)`: walk both lists with indexes `i` and `j`, append the smaller front item to `mergedList`, then append whatever is left over from either side

**Descending order:** change `left[i] <= right[j]` to `left[i] >= right[j]` in `Merge`.

| | Bubble sort | Merge sort |
|---|---|---|
| Approach | Compare/swap neighbours | Divide and conquer + recursion |
| Speed | Slowest | Fastest |
| Complexity to write | Low | Higher |
| Use for | Small lists | Large lists |

## To Know
- [ ] What recursion is, and why it needs an exit condition
- [ ] Write and trace bubble sort and merge sort
- [ ] How to flip either one to descending

## Homework
- Lesson 22 sample problems: recursive factorial (`num = 1` → `RETURN 1`, else `num * factorial(num - 1)`), recursive binary search (`BinarySearch(array, target, left, right)`, returns `-1` when `left > right`), descending bubble sort, descending merge sort

## Reflection
*What was the most surprising insight today?*
