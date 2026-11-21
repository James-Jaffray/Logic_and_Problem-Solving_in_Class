---
aliases: [Logic and Problem-Solving - Day 23]
tags: [logic-and-problem-solving, term1, lecture-notes, big-o, efficiency, optimization]
course: "[[Logic and Problem-Solving]]"
day: 23
---

# Logic and Problem-Solving — Day 23: Algorithmic Efficiency

**Today's focus:** measure how good an algorithm is with [[Big-O Notation]], then optimize it.

**Objectives:** discuss efficiency · use Big-O for time and space · identify complexities · optimize algorithms

## Why it matters
Time and memory cost money at scale, so an inefficient algorithm can cost millions. Big-O (asymptotic runtime) is the standard way to describe it.
- **Time complexity:** how long it takes as input grows
- **Space complexity:** how much memory it uses (array of size n = O(n); n × n grid = O(n²))

**Scenario:** sending a hard drive's files to a friend. Electronic transfer is O(n) (time grows with file size); mailing the drive is O(1) (constant). However big the constant, linear eventually overtakes it.

## Common complexities (fastest → slowest)
| Big-O | Name | Looks like |
|---|---|---|
| O(1) | Constant | Declaring a variable, basic arithmetic, fixed-size work. Means *consistent*, not *fast* |
| O(log n) | Logarithmic | Divide and conquer: halve the problem each step (binary search, integer square root). Doubling input adds only one step |
| O(n) | Linear | One loop, each element touched once (linear search, find the max). Best case for unsorted data |
| O(n²) | Quadratic | Nested loops, comparing all pairs (bubble sort). Double the input → 4× the time |

## Best, worst, expected case
- **Best:** optimal run, the lower bound, rarely useful
- **Worst:** poorest run, the upper bound, **what Big-O describes**
- **Expected:** typical real-world run, often equal to worst

## Optimization
Aim for the best solution, not just a working one (merge sort over bubble sort on large data).

**Loops**
- **Loop fusion:** merge loops into one
- **Loop fission:** split one loop into several smaller ones
- **Pre-calculation:** move work out of the loop so it runs once

**Memory**
- Rely less on global variables
- Process data in smaller batches
- Pick a better data structure (dictionary/hash table, binary search tree) for faster lookups

**Trade-offs:** you can swap space for time (or the reverse), and clever optimizations raise cognitive complexity (harder to read).

## Optimization examples (in-class)
| Problem | Slow | Fix | Result |
|---|---|---|---|
| Highest product in a list | Nested loops over all pairs, O(n²) | Find the max once, then `max * max` after the loop | O(n) |
| Is the list sorted? | Compare every pair, O(n²) | One pass checking `array[i] > array[i + 1]`, `BREAK` on first failure | O(n) |
| Common elements of two lists | Nested loops, O(n·m) | Put list1 in a dictionary, check each list2 item against it | O(n + m) |
| Peak index in a rising-then-falling list | Check every element's neighbours, O(n²) | Binary-search style: if `array[mid] < array[mid + 1]` go right, else go left | O(log n) |

## To Know
- [ ] Big-O for time and space, and that it describes the **worst case**
- [ ] Spot O(1), O(log n), O(n), O(n²) from the loop structure
- [ ] Loop and memory optimization techniques, and the trade-offs

## Homework
- Lesson 23 sample problems: for each inefficient algorithm, explain why it's inefficient (with Big-O), give an optimized version, and justify it (with Big-O)

## Reflection
*What was the most surprising insight today?*
