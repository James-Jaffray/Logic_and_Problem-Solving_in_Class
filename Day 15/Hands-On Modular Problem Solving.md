---
aliases: [Logic and Problem-Solving - Day 15]
tags: [logic-and-problem-solving, term1, lecture-notes, pseudocode, functions, modular-thinking]
course: "[[Logic and Problem-Solving]]"
day: 15
---

# Logic and Problem-Solving — Day 15: Hands-On Modular Problem Solving

**Today's focus:** building a modular solution **one piece at a time** — write it plain, pull a function out, simplify the main program, repeat — using a self-checkout system, then three more problems on your own. Concept pages: [[Functions in Pseudocode]], [[Cohesion and Coupling]], [[Modular Thinking]]. Follows [[Functions and Modular Structures]]; next: [[Debugging Modular Solutions]].

## The Method
1. Read the problem and list the **modules** (specific, single purpose, reusable)
2. **Don't** write everything and refactor at the end (slow). Build **piece by piece**, turning each piece into a function as you go
3. Each time a block moves into a function, replace it in the main program with a call, so the main program gets shorter and easier to read
4. Anything a function needs from outside comes in as a **parameter**; anything the main program needs back comes out as a **RETURN**

## Self-Checkout (guided example)
**Problem:** the customer scans barcodes (or presses "pay now"). On "pay now": add 5% GST to the total, print the final total. Payment is credit, debit or gift card. Credit/debit need a PIN validated with the bank; if validation fails, ask again. Gift cards are always valid. When valid, process the payment and finish.

**Modules found:** scan · validate pin · validate payment type · process payment

| Step | What changed |
|---|---|
| 1. Main with scanning | A `total` variable, a loop that scans an item, adds its price, and repeats until the user is done |
| 2. `scan()` | Moves the scan-one-item step out. No parameters; **returns the item price** |
| 3. `scanItems()` | Moves the whole scan loop out and returns `total * 1.05` (GST included). Main shrinks to one call |
| 4. `validatePin()` | PIN check becomes its own function that returns `true` / `false` |
| 5. Payment-type loop | Re-prompting on a bad PIN needs a `DO ... UNTIL` (we always ask at least once). The exit condition is a **flag** (`validPayment`) |
| 6. `validatePaymentType()` | The whole prompt-and-validate loop moves out and returns the payment type |
| 7. `processPayment(amount, paymentType)` | Takes **two parameters** (what to deduct, and from where); returns nothing |

**Scope:** `total` inside `scanItems()` isn't visible in main, so main declares its own `total` and assigns the returned value to it.

**Flag variable:** a true/false variable that starts in one state and flips when a condition is met. Here it controls the `DO ... UNTIL`. Refinement: start `validPayment` as **`true`** and delete the `ELSE`, since only the PIN check can make it `false`.

### Final solution
```
FUNCTION scan()
    Scan barcode on machine                     // customer scans item
    INPUT itemPrice                             // machine processes scan and returns price
    RETURN itemPrice
ENDFUNCTION

FUNCTION scanItems()
    DECLARE total = 0
    DECLARE continue = true
    DO
        total = total + scan()
        INPUT continue                          // false when they press "pay now"
    UNTIL continue == false
    RETURN total * 1.05                         // total with GST
ENDFUNCTION

FUNCTION validatePin()
    INPUT pinNumber
    INPUT pinIsValid                            // bank validates the pin
    IF pinIsValid == false THEN
        PRINT "Invalid pin!"
    ENDIF
    RETURN pinIsValid
ENDFUNCTION

FUNCTION validatePaymentType()
    DECLARE validPayment = true
    DO
        PRINT "How would you like to pay?"
        INPUT paymentType
        IF paymentType != "gift card" THEN
            validPayment = validatePin()        // credit and debit need a pin
        ENDIF
    UNTIL validPayment == true
    RETURN paymentType
ENDFUNCTION

FUNCTION processPayment(amount, paymentType)
    IF paymentType == "gift card" THEN
        Deduct amount from gift card
    ELSEIF paymentType == "debit" THEN
        Deduct amount from bank account
    ELSE
        Deduct amount from credit card
    ENDIF
    RETURN
ENDFUNCTION

START
    DECLARE total = scanItems()
    DECLARE paymentType = validatePaymentType()
    processPayment(total, paymentType)
END
```
Look at the main program: three lines that read like the problem statement. Every detail lives in a function that can be tested alone.

**Edge case:** `validPayment` is only changed inside the `IF`, and it's set to `true` once, before the loop. If someone fails a PIN (flag becomes `false`) and then picks "gift card" on the retry, the `IF` is skipped, the flag stays `false`, and the loop never ends. Setting `validPayment = true` at the **top of each pass** (inside the `DO`) fixes it.

## Practice Problems
All three: list the modules, then write the pseudocode with functions. (Problem text is in the Lesson 15 sample problems.)

### Smart Home
Washer, dryer, dishwasher (on/off) and a thermostat on one touch screen. Off → show "not on" and offer to turn it on; on → show time remaining. Thermostat shows current °C, lets you change it, and takes 20 minutes per degree.

Modules: `printOnOffMessage(systemIsOn)` · `turnOnSystem(systemChoice)` · `manageAppliances(appliance)` (uses the first two) · `getTempTimeRemaining(degreeChange)` (`degreeChange * 20`) · `manageThermostat()`. Main: `INPUT systemChoice`, then `manageThermostat()` if it's the thermostat, otherwise `manageAppliances(systemChoice)`.

Key idea: when the user turns a machine on, call `printOnOffMessage(true)` directly. You already know the state, so pass the value instead of asking again. The temperature difference is made positive (`difference * -1` when negative) so the time is never negative. Full pseudocode: [[Smart Home Solution]].

### Extreme Weather Warning System
Tornado, hurricane or thunderstorm. A satellite supplies likelihood (%), plus wind speed (tornado/hurricane) or rainfall (thunderstorm). Over 70% likelihood sends a warning to the region. Category comes from wind speed (EF0–EF5, Hurricane 1–5).

Modules: `getWindSpeed()` · `getRainfall()` · `getTornadoCategory(windspeed)` · `getHurricaneCategory(windspeed)`. The category functions are `IF / ELSEIF` chains checked from the **highest** threshold down. Main picks the branch by `stormType`, builds `warningMessage`, and sends it only `IF likelihood > 70`. Full pseudocode: [[Extreme Weather Warning Solution]].

### Block Sorting System
A camera gives number of sides, width × height and colour. The bucket code is `<size><color><shape>` (e.g. `LBR` = large blue rectangle). The size ranges in the problem (small < 10, medium 10–19, large ≥ 30) leave 20–29 undefined, and the sample solution uses large ≥ 30, medium ≥ 20, otherwise small, which doesn't match them. Check boundaries against the statement.

Modules: `getColorCode(color)` · `getSizeCode(size)` · `getShapeCode(numberOfSides)` · `getBucketCode(color, size, numberOfSides)`, which **calls the three code functions** and joins the letters · `getBlockSize` / `getBlockColor` / `getBlockSides` (read the camera). Main reads the block, calls the getters, calls `getBucketCode`, prints the code and places the block. Full pseudocode: [[Block Sorting Solution]].

## To Know
- [ ] Build piece by piece: write it, extract a function, replace with a call, repeat
- [ ] Return values come out; parameters go in; variables inside a function are out of scope in main
- [ ] A flag is a true/false variable that controls a loop (`DO ... UNTIL validPayment == true`)
- [ ] Higher-level functions (`getBucketCode`, `processOrder`) call small single-purpose ones
- [ ] The main program should read like the problem statement

## Homework
- Smart Home, Extreme Weather Warning System, Block Sorting System (Lesson 15 sample problems)

## Reflection
*What was the most surprising insight today?*
