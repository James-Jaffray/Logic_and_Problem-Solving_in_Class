---
aliases: [Logic and Problem-Solving - Day 16]
tags: [logic-and-problem-solving, term1, lecture-notes, debugging, modular-thinking, pseudocode]
course: "[[Logic and Problem-Solving]]"
day: 16
---

# Logic and Problem-Solving — Day 16: Debugging Modular Solutions

**Today's focus:** the errors that show up in modular solutions (flowcharts and pseudocode with functions), and a systematic way to track them down. Concept pages: [[Cohesion and Coupling]], [[Logical Errors and Debugging]]. Builds on [[Common Logical Errors and Debugging]] (Day 11) and [[Hands-On Modular Problem Solving]].

## Lesson Objectives
- Identify common errors in modular solutions
- Apply debugging strategies to modular flowcharts and pseudocode
- Improve modular solutions through systematic troubleshooting

## Common Errors
### Errors in programming
- **Logical errors**: the steps run but give the wrong result
- **Missing steps**
- **Improper function calls**: wrong function, wrong arguments, wrong order, or ignoring the returned value

### Errors in design: inefficiency
- Functions that **repeat logic**
- **Unused** code
- **Redundant** code
- **Poor naming**
- Logic that's **too complex**

### Errors in design: incohesion
**Cohesion** = how focused a function is on a single task.
- An incohesive function does several jobs
- Harder to debug, less readable

### Errors in design: coupling
Two or more modules **depend on each other**.
- Changing one can break another
- Testing and debugging get harder, more error-prone
- Very hard to scale

Good design is **high cohesion, low coupling**: each function does one thing and knows as little as possible about the others (pass things in as parameters, get things back as return values). See [[Cohesion and Coupling]].

## Debugging Strategies
| Strategy | What you do |
|---|---|
| **Logic tracing** | Read line by line, watch function calls and variable changes. Reading it out loud (or to a rubber duck) helps |
| **Testing** | Run the algorithm with different inputs, confirm each result, look for patterns in the failures |
| **Reviewing input** | Check what the function **receives**: correct parameters? Is the caller sending the right values? |
| **Reviewing output** | Check how the input is **used** and which conditions produce the output; is the caller receiving the right value? |
| **Print statements** | Add `PRINT` to show variable values and confirm each change. Quick check, handy in older languages |

## The Debugging Process
1. **Identify the problem module**: which function produces the wrong result?
2. **Test it with different inputs** (normal, boundary, invalid: see [[Logic Master Reference]])
3. **Read it line by line**
4. **Stepwise refinement**: fix one small thing, retest, repeat

Because each function is separate, you can test one in isolation instead of running the whole program. That's the payoff of modular design.

## Scheduling Diagram Example
The in-class flowchart is a doctor-appointment booker built from three functions:

| Function | Job |
|---|---|
| `checkSchedule(time)` | `INPUT time`, search the system for availability at that time, and return `true` or `false` (with a "doctor is unavailable, choose another time" message when it fails) |
| `getAppointmentDetails()` | `INPUT` the name, reason for visit and email, and return the email |
| `sendConfirmationEmail(time, emailAddress)` | create the confirmation email for the time and send it to the address |

Debug it with the process above: find which of the three gives the wrong result, feed that one function inputs of its own, and trace its decision paths. Check what each function **returns** and whether the caller actually uses it.

## To Know
- [ ] Error types: logical errors, missing steps, bad function calls; design problems: inefficiency, incohesion, coupling
- [ ] High cohesion (one job per function) and low coupling (modules don't depend on each other's details)
- [ ] Strategies: trace, test, review input, review output, print statements
- [ ] Process: find the problem module → test with different inputs → read line by line → refine step by step

## Homework
- Lesson 16 debugging examples (broken pseudocode and the scheduling diagram)

## Reflection
*What was the most surprising insight today?*
