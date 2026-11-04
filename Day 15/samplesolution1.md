---
aliases: [Smart Home Solution]
tags: [logic-and-problem-solving, term1, practice, pseudocode, functions, modular-thinking]
course: "[[Logic and Problem-Solving]]"
day: 15
---

# Smart Home

Pseudocode solution from [[Hands-On Modular Problem Solving]].

```
FUNCTION printOnOffMessage(systemIsOn)
	IF systemIsOn THEN
		OUTPUT timeRemaining  	// comes from the system
		PRINT timeRemaining
	ELSE
		PRINT “The system is off”
	ENDIF
	RETURN
ENDFUNCTION

FUNCTION turnOnSystem(systemChoice)
	Smart home targets systemChoice
	Smart home turns on systemChoice
	RETURN
ENDFUNCTION

FUNCTION manageAppliances(appliance)
	OUTPUT systemIsOn		// true or false, comes from the 							// system
	printOnOffMessage(systemIsOn)
	IF systemIsOn == false THEN
		INPUT turnSystemOn	// true or false, input from user to 							// turn on system
		IF turnSystemOn THEN
			turnOnSystem(appliance)
			printOnOffMessage(true)	// system is on so we can 									// just pass the value 									// “true” as an argument
		ENDIF
	ENDIF
	RETURN
ENDFUNCTION


FUNCTION getTempTimeRemaining(degreeChange)
	RETURN degreeChange * 20
ENDFUNCTION


FUNCTION manageThermostat()
	OUTPUT currentTemp
	PRINT currentTemp
	INPUT newTemp 	// new temperature from user
	IF newTemp != currentTemp THEN
		DECLARE difference = currentTemp – newTemp 
		IF difference < 0 THEN
			SET difference = difference * -1 //make sure number is										//positive to get 										//accurate time 											//remaining
		ENDIF
		DECLARE timeRemaining = getTempTimeRemaining(difference)
		PRINT “Time remaining: ” + timeRemaining
	ENDIF
	RETURN
ENDFUNCTION

START
INPUT systemChoice	// input from the user
IF systemChoice != “thermostat” THEN
	manageAppliances(systemChoice)
ELSE
	manageThermostat()
ENDIF
END
```
