---
aliases: [Logic and Problem-Solving - Day 14]
tags: [logic-and-problem-solving, term1, lecture-notes, pseudocode, functions, modular-thinking]
course: "[[Logic and Problem-Solving]]"
day: 14
---

# Logic and Problem-Solving — Day 14: Functions and Modular Structures

**Today's focus:** turning the modules you found in [[Introduction to Modular Thinking]] into **functions** in pseudocode, then writing a main program that calls them. Concept pages: [[Functions in Pseudocode]], [[Modular Thinking]]. Same idea as [[Modules and Functions]] in Python. Next: [[Hands-On Modular Problem Solving]].

## Function Shape
```
FUNCTION functionName(parameter1, parameter2)    // one specific purpose
    ...steps...
    RETURN result                                // hand a value back
ENDFUNCTION

START
    DECLARE answer = functionName(value1, value2)   // call it; catch the returned value
END
```
- Name says what it does (`getCardDetails`, `travelCost`), in camelCase ([[Pseudocode Conventions]])
- **Parameters** = the inputs it needs. **RETURN** = what it hands back. Functions that just *do* something end with a plain `RETURN` (no value)
- A variable created inside a function is out of scope in the main program. To use the result, return it and assign it to a variable
- Define the functions first, then write `START ... END` as a short list of calls

## Finding the Functions
The instruction for every sample problem: **identify the processes that can be split into functions (each requirement may contain more than one function), then write the pseudocode.**

Ask for each chunk of the requirements:
1. Is it one clear task? (If it says "and", it's probably two functions)
2. What does it need in (parameters) and give back (return)?
3. Could another part of the program reuse it? (See the five questions in [[Introduction to Modular Thinking]])

## Worked Example 1 — Order Processing (e-commerce, one item per order)
Requirements: get payment details, confirm enough inventory, confirm shipping address; name/address/card can each be stored as one string; build an "order" and insert it into the database.

| Function | In → Out |
|---|---|
| `enterName()` | → full name string |
| `enterAddress()` | → address as one string (used for **both** billing and shipping: reuse) |
| `enterCreditCard()` | → number + expiry + CVC as one string |
| `checkInInventory(item)` | item → `true` / `false` |
| `submitOrder(name, creditCard, billingAddress, shippingAddress)` | builds the order and inserts it into the database, no return value |
| `processOrder()` | calls the three `enter...` functions, then `submitOrder` |

```
START
    INPUT itemToPurchase
    DECLARE itemInInventory = checkInInventory(itemToPurchase)
    IF itemInInventory THEN
        processOrder()
        PRINT "Order successful"
    ELSE
        PRINT "That item is not available."
    ENDIF
END
```
`processOrder()` is a function that **calls other functions**: modules calling modules, the same as CUT calling MEASURE in the birdhouse.

## Worked Example 2 — Cat Sitter
$50 per day + travel ($0 under 2 km, $5 per trip for 2–5 km, $10 for 5–10 km, $15 over 10 km) + a tip entered as a percentage of the final total.
```
FUNCTION costPerDay(daysGone)
    RETURN daysGone * 50
ENDFUNCTION

FUNCTION travelCost(daysGone, distance)
    DECLARE cost
    IF distance > 10 THEN
        SET cost = 15
    ELSEIF distance > 5 THEN
        SET cost = 10
    ELSEIF distance > 2 THEN
        SET cost = 5
    ELSE
        SET cost = 0
    ENDIF
    RETURN cost * daysGone                 // one trip per day
ENDFUNCTION

FUNCTION calculateTip(finalCost)
    INPUT tipPercentage                    // e.g. 15 means 15%
    RETURN finalCost * tipPercentage / 100
ENDFUNCTION

START
    DECLARE total
    INPUT daysGone
    SET total = costPerDay(daysGone)
    INPUT distance
    SET total = total + travelCost(daysGone, distance)
    SET total = total + calculateTip(total)       // tip is on the final total, so it goes last
    OUTPUT total
END
```
- Check the distance conditions from the **largest down**: `> 10`, then `> 5`, then `> 2`. Each branch is only reached if the earlier ones were false, so no need for `AND`
- A percentage typed in as `15` has to be divided by 100

## Worked Example 3 — Musical Instrument Repair Shop
Base $10 per day + repair (basic/deluxe by size small/medium/large) + optional cleaning by size.

| Function | Job |
|---|---|
| `getPerDiemCost(days)` | `RETURN 10 * days` |
| `getRepairCost(size, repairType)` | nested decision on size, then on `basic` / `deluxe` (30/50, 50/70, 75/125) |
| `getCleaningCost(size)` | 10 / 15 / 25 by size |

```
START
    DECLARE cost
    INPUT instrumentSize
    INPUT repairType
    INPUT dayEstimate
    INPUT wantsCleaning
    SET cost = getPerDiemCost(dayEstimate)
    SET cost = cost + getRepairCost(instrumentSize, repairType)
    IF wantsCleaning == "yes" THEN
        SET cost = cost + getCleaningCost(instrumentSize)     // optional, so it's inside an IF
    ENDIF
    OUTPUT cost
END
```
`getRepairCost` and `getCleaningCost` both decide on `size`, but each does **one** job, which keeps them separately testable.

## Practice Stubs
Two small input-gathering functions, in the same pattern as `enterCreditCard()` and `enterAddress()`:
```
FUNCTION getCardDetails()
    INPUT creditCardNumber
    INPUT cvcNumber
    INPUT expiryDate
    RETURN creditCardNumber + cvcNumber + expiryDate
ENDFUNCTION

FUNCTION getAddress()
    INPUT buildingNumber
    INPUT streetName
    INPUT city
    INPUT province
    INPUT country
    RETURN buildingNumber + streetName + city + province + country
ENDFUNCTION
```

## To Know
- [ ] Split a problem into functions first, then write the main program as a list of calls
- [ ] `FUNCTION name(params) ... RETURN value ... ENDFUNCTION`
- [ ] Return a value and assign it (`DECLARE total = scanItems()`); local variables don't leave the function
- [ ] Reuse: `enterAddress()` serves both billing and shipping
- [ ] One purpose per function; functions can call functions
- [ ] Optional steps (cleaning, tip) sit inside an `IF` in the main program

## Homework
- Lesson 14 sample problems: order processing, cat sitter, instrument repair shop

## Reflection
*What was the most surprising insight today?*
