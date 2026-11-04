# Summary: Modular Programming & Debugging

This document consolidates key concepts, examples, and techniques covered across Lessons 11, 13, 14, and 16 on **Modular Thinking, Functions, Logical Errors, and Debugging**.

---

## Table of Contents
1. [Lesson 11: Common Logical Errors & Debugging Techniques](#lesson-11-common-logical-errors--debugging-techniques)
2. [Lesson 13: Introduction to Modular Thinking](#lesson-13-introduction-to-modular-thinking)
3. [Lesson 14: Functions & Modular Structures in Flowcharts & Pseudocode](#lesson-14-functions--modular-structures-in-flowcharts--pseudocode)
4. [Lesson 16: Debugging Issues in Modular Solutions](#lesson-16-debugging-issues-in-modular-solutions)

---

## Lesson 11: Common Logical Errors & Debugging Techniques

### 1. Key Concepts
* **Logical Errors**: Flaws in algorithm design that lead to incorrect or unexpected behavior (e.g., incorrect comparisons, wrong execution order, missing lines of code).
* **Infinite Loops**: Loops that run endlessly because the termination condition is never met.
* **Refactoring**: Rewriting or restructuring existing code to improve efficiency or readability. Note that refactoring can be time-consuming and risks introducing new bugs if not done carefully.

---

### 2. Common Pseudocode Errors & Fixes

#### A. Loop Termination Error
* **Bug**: `WHILE number < 10` stops at `9` instead of printing up to `10`.
* **Fix**: Change condition to `WHILE number <= 10`.

#### B. Summing a Series (Missing Variables & Logic)
* **Bug**: Using undeclared variables (`sum`) or missing accumulation statements inside a loop.
* **Fix**:
```text
START
  DECLARE counter = 1
  DECLARE sum = 0
  INPUT number
  DO
    sum = sum + counter
    counter = counter + 1
  UNTIL counter == number
  PRINT sum
END
```

---

### 3. Step-by-Step Debugging & Refinement: Generation Calculator

#### Initial Problematic Pseudocode
```text
START
  DO
    INPUT age
    IF age > 0 THEN
      PRINT "Enter a number > 0"
    ENDIF
  UNTIL age >= 0

  IF age > 60 THEN
    PRINT "You are a Baby Boomer"
  ELSE IF age > 34 THEN
    PRINT "You are Gen X"
  ELSE IF age >= 28 THEN
    PRINT "You are Gen Alpha"
  ELSE IF age >= 13 THEN
    PRINT "You are Gen Z"
  END
```

#### Key Issues Identified:
1. **Input Validation Logic**: The error message printed when `age > 0` instead of `age <= 0`.
2. **Loop Condition**: Loop exited incorrectly; `UNTIL age > 0` is required.
3. **Incorrect Ranges & Categories**:
   * Gen X: Age 45–60 (`age > 44`).
   * Millennial: Age 29–44 (`age > 28`).
   * Gen Z: Age 13–28 (`age > 12`).
   * Gen Alpha: Age 0–12 (`ELSE` fallback).
4. **Syntax**: Missing closing `ENDIF`.

#### Fully Debugged & Refined Pseudocode
```text
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

---

## Lesson 13: Introduction to Modular Thinking

### 1. Modularization Principles
* **Modular Thinking**: The practice of breaking complex problems down into small, independent sub-problems ("modules").
* **Decomposition**: The process of identifying logical, independent units within a overall problem.
* **Benefits**:
  * Faster development
  * Increased code reusability and readability
  * Simplified debugging and unit testing

---

### 2. Standard Criteria for a Good Module
Every module should ideally be:
1. **Reusable**: Callable from multiple places.
2. **Independent**: Self-contained without reliance on unintended external state.
3. **Single Purpose**: Focused on a single task.
4. **Separately Testable & Updatable**: Modifiable without breaking other modules.

---

### 3. Practical Decomposition Example: Building a Birdhouse

#### Individual Modules:
* **`MEASURE`**: Uses a ruler to mark exact board lengths.
* **`CUT`**: Calls `MEASURE`, then uses a saw to cut wood to size.
* **`DRILL`**: Calls `MEASURE`, then drills designated hole diameters.
* **`SCREW`**: Calls `DRILL` on two boards, aligns them, and fastens them together.

#### Main Program Logic:
```text
1. CUT two boards of size 30cm x 20cm (Boards A & B)
2. CUT two boards of size 30cm x 15cm (Boards C & D)
3. CUT two boards of size 20cm x 15cm (Boards E & F)
4. DRILL a 3cm hole in Board C
5. DRILL a 3cm hole in Board D
6. SCREW Board A to C and D
7. SCREW Board B to C and D (opposite side)
8. SCREW Boards E and F to top and bottom
```

---

## Lesson 14: Functions & Modular Structures in Flowcharts & Pseudocode

### 1. Anatomy of a Function
* **Name**: Descriptive identifier using `camelCase` (e.g., `calculateTax`).
* **Code Block**: Code executed whenever the function is invoked.
* **Parameters**: Input data passed from caller into the function (optional).
* **Return Value**: Output data sent back to caller (optional). Functions without return values are called **void functions**.

---

### 2. Flowchart Representation
* **Predefined Process Symbol**: A rectangle with double vertical lines on the sides represents a function call.

```text
  +---------------+
  |  Add(a, b)    |  <-- Predefined Process Symbol
  +---------------+
```

* **Defining a Predefined Process**:
  * Start symbol uses `Start FunctionName(parameters)`.
  * Output symbol returns values prior to the `End` terminator.

---

### 3. Pseudocode Function Standards
* Declare functions **at the top** of the program file (before main block).
* Enclose code between `FUNCTION` and `ENDFUNCTION`.
* Always include parentheses `()` during definition/invocation.
* Always explicitly include a `RETURN` statement where applicable.
* **Best Practice**: Avoid modifying global variables inside modular functions.

#### Example Pseudocode Structure
```text
// Function Declaration
FUNCTION add(num1, num2)
  DECLARE sum = num1 + num2
  RETURN sum
ENDFUNCTION

// Main Program
START
  INPUT input1
  INPUT input2
  DECLARE result = add(input1, input2)
  PRINT result
END
```

---

### 4. Advanced Concepts

#### Recursion
* Occurs when a function **calls itself**.
* Requires a well-defined **base case** to prevent infinite execution stacks.

```text
FUNCTION power(base, exponent)
  IF exponent == 0 THEN
    RETURN 1
  ELSE
    RETURN base * power(base, exponent - 1)
  ENDIF
ENDFUNCTION
```

#### Variable Scope
* **Function Scope**: Variables declared inside a function are local to that function.
* **Global Scope**: Variables declared outside main blocks and functions, accessible globally.

---

## Lesson 16: Debugging Issues in Modular Solutions

### 1. Categorization of Modular System Errors

#### Programmatic Errors
* **Logical Errors**: Algorithm flaw producing incorrect calculation.
* **Missing Steps / Improper Calls**: Forgetting to invoke functions or passing incorrect parameter values.

#### Architectural / Design Errors
* **Inefficiencies**: Duplicate logic across modules, redundant code, overly complex routines.
* **Incohesion**: Modules that tackle multiple unrelated responsibilities. High cohesion (single-task focus) is desired.
* **Tightly Coupled Modules**: Interdependent modules where changing one breaks others. High coupling makes testing and scalability difficult.

---

### 2. Systematic Debugging Strategies

* **Logic Tracing / Desk Checking**: Step-by-step reading of code, tracking variable state changes on paper (or rubber duck debugging).
* **Multi-Input Testing**: Running algorithms against boundary edge-cases to reveal hidden branch bugs.
* **Parameter Verification**: Auditing inputs passed to modules vs values returned to callers.
* **Print-Statement Tracing**: Placing temporary `PRINT` log statements throughout function call trees.

---

### 3. Standard Debugging Workflow for Modular Code

```text
[ Identify Problem Module ] 
            │
            ▼
[ Test with Varied Inputs ]
            │
            ▼
[ Trace Line-by-Line / Check Parameters ]
            │
            ▼
[ Stepwise Refinement & Testing ]
```