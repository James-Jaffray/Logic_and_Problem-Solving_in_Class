---
aliases: [Logic and Problem-Solving - Day 24]
tags: [logic-and-problem-solving, term1, lecture-notes, algorithms, big-o]
course: "[[Logic and Problem-Solving]]"
day: 24
---

# Logic and Problem-Solving — Day 24: Applying Standard Algorithms

**Today's focus:** combine [[Standard Algorithms]] into bigger solutions and work out the [[Big-O Notation|Big-O]] of the combination with [[Sequential and Nested Complexity]]. Last topic of the course.

## Sequential operations
One operation after another (e.g. sort, then search). **Add** the complexities, then keep the **dominant term** (fastest-growing). As n grows, lower-order terms become negligible.

> Linear search O(n) + bubble sort O(n²) + binary search O(log n) = **O(n²)**

## Nested operations
One operation **inside** another (a loop containing a full algorithm). **Multiply** the complexities.
- Bubble sort: O(n) loop inside O(n) loop = **O(n²)**
- Binary search for each of n items in a sorted list: O(n) × O(log n) = **O(n log n)**

**Both together:** work **inside out**. Compute the nested part first, then use it in the sequential sum.

| | Sequential | Nested |
|---|---|---|
| Shape | Steps one after another | Loop inside a loop, or an algorithm run per element |
| Combine by | Adding, take dominant term | Multiplying |

## Worked designs
- **Restaurants:** merge sort by distance, take the 5 closest, linear search them for the best rating. O(n log n) + O(1) = **O(n log n)** (the 5-item search is constant)
- **Ambulances:** one linear pass that checks the 5-mile radius and tracks the most supplies as it goes. No sort needed, **O(n)**
- **Student lookup by ID (unsorted):** merge sort O(n log n), then binary search O(log n) → **O(n log n)**
- **Top 10 of a course (max 30 students):** filter by course code O(n), bubble sort the ≤30 students O(m²), take the first 10 O(1). Total O(n + m²), but m ≤ 30 so the sort is effectively constant → **O(n)**. Bubble sort was chosen on purpose to keep **cognitive complexity** low

Takeaway: the "best" algorithm depends on data size too. A simple one is fine when the data is small and bounded.

## To Know
- [ ] Sequential = add, keep dominant term; nested = multiply
- [ ] Combined: nested first, then sequential
- [ ] Justify algorithm choices in a design, not just name them

## Homework
- Lesson 24 problems: restaurant finder, emergency response, student database (parts 1 and 2). Each needs a plan, a defence of the algorithm choices and the Big-O
- In-class Assignment 4 (Lessons 19, 21–24): show all calculations and formulae, **bold** final answers, use the template

## Reflection
*What was the most surprising insight today?*
