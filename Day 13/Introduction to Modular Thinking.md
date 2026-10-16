---
aliases: [Logic and Problem-Solving - Day 13]
tags: [logic-and-problem-solving, term1, lecture-notes, modular-thinking, decomposition]
course: "[[Logic and Problem-Solving]]"
day: 13
---

# Logic and Problem-Solving — Day 13: Introduction to Modular Thinking

**Today's focus:** breaking a complex problem into small, independent, reusable *modules* — and why that makes solutions faster to build, read, test and debug. Concept page: [[Modular Thinking]]. Follows [[Common Logical Errors and Debugging]] (and refinement) and the second in-class assignment (flowchart + problem statement → pseudocode, debug and refine).

## Lesson Objectives
- Define modular thinking and its benefits in problem-solving
- Identify logical units in a program that can be modularized
- Apply modular thinking to decompose a problem into independent components

## What Is Modular Thinking?
- Complex problems are nearly impossible to solve in one look — smaller problems are much easier
- **Modules** = small, independent pieces of logic
- **Modular thinking** = looking at a complex problem and seeing the modules inside it
- Especially valuable in software development; nearly every programming language relies on it

| Step | Meaning |
|---|---|
| **Decomposition** | First step: understand the problem and break it into independent components (see [[Problem Decomposition]]) |
| **Modularization** | Turn one of those components into a smaller reusable piece that plugs into the wider solution |

## Benefits of Modularization
- **Faster development** — small tasks can be delegated to several people at once
- **Reusability** — no duplicated effort
- **Readability** — less time to understand and debug
- **Easier debugging** — narrow a problem to one module
- **Easier testing** — automated tests on small modules keep the app stable as it grows

## What Makes a Good Module?
Ask these five questions of every candidate module:

| Question | Meaning |
|---|---|
| Reusable? | Works for any input of its kind, not one special case |
| Independent? | Doesn't depend on the details of other steps |
| Specific purpose? | Does one clear job |
| Separately testable? | Can be run and checked alone |
| Separately updated? | Can change (e.g. add safety steps) without breaking the rest |

## Worked Example — Build a Birdhouse
**Problem statement:** build a four-sided birdhouse, 30 cm tall, 20 cm wide, 15 cm deep, with a 3 cm hole in two of the four sides. You're given a basket of screws and two planks of wood.

**Requirements/constraints:** 30 × 20 × 15 cm · two 3 cm holes · only screws · only two planks

**Decomposed processes:** measure · cut the wood into four sides · drill the holes · screw the pieces together

### MEASURE
1. Get a ruler
2. Take the piece of wood to measure
3. Place the ruler on the wood
4. Use a pencil to mark the desired length

Passes all five checks → keep it.

### CUT
1. Get a wood saw
2. **MEASURE** the length of wood
3. Place the saw on the marked location
4. Saw back and forth with downward pressure until the board is cut

First reuse: CUT doesn't rewrite the measuring steps, it calls MEASURE.

### DRILL
First draft: get a ruler → take the wood → mark the length → grab a drill → drill the hole. The first three steps repeat MEASURE, so refine:
1. **MEASURE** the diameter of the hole
2. Grab a drill
3. Drill the hole

### SCREW
First draft was 12 steps (measure and drill each board by hand, align, grab a screwdriver, screw). Refined with DRILL:
1. **DRILL** a hole the width of the screw into the first board
2. **DRILL** a hole the width of the screw into the second board
3. Align the two boards along the holes
4. Grab a screwdriver
5. Screw the screw into the wood

### Build the Birdhouse (using the modules)
1. CUT two boards 30 × 20 cm (A, B)
2. CUT two boards 30 × 15 cm (C, D)
3. CUT two boards 20 × 15 cm (E, F)
4. DRILL a 3 cm hole in board C
5. DRILL a 3 cm hole in board D
6. SCREW board A to boards C and D
7. SCREW board B to boards C and D on the opposite side
8. SCREW boards E and F to the top and bottom

8 steps with modules vs. 50+ lines written out — hard to read and easy to get lost in or make mistakes in.

## Connections
- Modules calling modules (CUT → MEASURE, DRILL → MEASURE, SCREW → DRILL) is exactly how functions call functions in code — see [[Python Functions]]
- Writing the final steps in [[Pseudocode]]: each module becomes a named block you invoke by name

## To Know
- Module = small, independent, reusable piece of logic; modular thinking = spotting them
- Decomposition first, then modularization
- A good module is reusable, independent, single-purpose, separately testable and separately updatable
- If a module repeats another module's steps, replace them with a call to that module
- Benefits: faster development, reuse, readability, easier debugging, easier testing

## Reflection
*What was the most surprising insight today?*
