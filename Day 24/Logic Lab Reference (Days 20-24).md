---
aliases: [Logic Days 20-24 Reference Sheet]
tags: [logic-and-problem-solving, term1, reference-sheet, algorithms, big-o]
course: "[[Logic and Problem-Solving]]"
---

# Logic Lab Reference — Days 20–24

Quick lookup. Deeper notes: [[Maths for Data Analysis]] · [[Standard Algorithms Part 1]] · [[Standard Algorithms Part 2]] · [[Algorithmic Efficiency]] · [[Applying Standard Algorithms]]

## Data maths (Day 20)
| Need | Formula / Excel |
|---|---|
| Probability | favourable ÷ total (×100 for %) |
| Likelihood (odds) | `P / (1 − P)` |
| Correlation | `=CORREL(colA, colB)` → r (−1 to 1) |
| Matches in test data | pivot table of actual vs test columns |
| Trend | line chart (over time), pivot chart (by year) |

- r > 0 positive, r < 0 negative, r ≈ 0 independent. Closer to ±1 = stronger
- **Correlation ≠ causation.** Say "likely" and what more analysis is needed
- Show steps, formulae and a screenshot; **bold** the final answer

## Which algorithm? (Days 21–22)
| Task | Use | Big-O |
|---|---|---|
| Find in unsorted/small data | Linear search | O(n) |
| Find in large **sorted** data | Binary search | O(log n) |
| Count occurrences | Linear pass + counter | O(n) |
| Mode | Frequency dictionary, then max | O(n) |
| Sort small list | Bubble sort | O(n²) |
| Sort large list | Merge sort | O(n log n) |

## Pseudocode skeletons
**Linear search / count**
```
DECLARE count = 0
FOR each number in listOfNumbers
	IF numberToSearch == number
		SET count = count + 1
	ENDIF
ENDFOR
```
**Binary search**
```
low = 0 ; high = length(list) - 1 ; found = False
WHILE low <= high AND NOT found
	mid = (low + high) / 2 rounded down
	IF list[mid] == target THEN found = True
	ELSE IF target > list[mid] THEN low = mid + 1
	ELSE high = mid - 1
	ENDIF
ENDWHILE
```
**Bubble sort** (ascending; descending → `<`)
```
FOR i = 0 TO length(myList) - 2
	FOR j = 0 TO length(myList) - 2 - i
		IF myList[j] > myList[j + 1]
			SWAP myList[j] and myList[j + 1]
		ENDIF
	ENDFOR
ENDFOR
```
**Merge sort** (descending → `left[i] >= right[j]` in `Merge`)
```
FUNCTION MergeSort(myList)
	IF length(myList) <= 1
		RETURN myList
	ENDIF
	SET leftHalf = MergeSort(left half)
	SET rightHalf = MergeSort(right half)
	RETURN Merge(leftHalf, rightHalf)
ENDFUNCTION
```
`Merge`: indexes `i`, `j`; append the smaller front item to `mergedList`; then append leftovers from each side.

**Recursion** needs an exit condition:
```
FUNCTION factorial(num)
	IF num = 1
		RETURN 1
	ELSE
		RETURN num * factorial(num - 1)
	ENDIF
ENDFUNCTION
```

## Big-O (Day 23)
| Big-O | Spot it by |
|---|---|
| O(1) | No loop (variable, arithmetic) |
| O(log n) | Halves the problem each step |
| O(n) | One loop |
| O(n log n) | Loop containing a binary search; merge sort |
| O(n²) | Nested loops over the data |

- Big-O = **worst case**. Also measures **space** (array of n = O(n); n × n grid = O(n²))
- **Loops:** fuse, split (fission), pre-calculate outside the loop
- **Memory:** fewer globals, process in batches, dictionary/hash table/BST
- Trade-offs: space vs time, and readability (cognitive complexity)

**Common optimizations:** nested pair-check → single pass (O(n²) → O(n)) · two-list overlap → dictionary lookup (O(n·m) → O(n+m)) · peak finding → binary-style halving (O(log n))

## Combining algorithms (Day 24)
- **Sequential** (A then B): **add**, keep the **dominant term**. O(n) + O(n²) + O(log n) = **O(n²)**
- **Nested** (A inside B): **multiply**. O(n) × O(log n) = **O(n log n)**
- **Both:** nested first, then add
- A bounded small input (e.g. ≤ 30) is effectively constant

## Design answers: structure
1. **Plan** (which algorithm for each step, in order)
2. **Defend** (why: sorted or not, data size, readability)
3. **Big-O** (per step, then combine)

| Scenario | Plan | Big-O |
|---|---|---|
| 5 closest restaurants, best rated | Merge sort by distance → take 5 → linear search | O(n log n) |
| Ambulances in 5 miles, most supplies | One linear pass, track the best | O(n) |
| Student by ID, unsorted | Merge sort → binary search | O(n log n) |
| Top 10 in a class (≤ 30) | Filter → bubble sort → first 10 | O(n) |
