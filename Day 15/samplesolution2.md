---
aliases: [Extreme Weather Warning Solution]
tags: [logic-and-problem-solving, term1, practice, pseudocode, functions, modular-thinking]
course: "[[Logic and Problem-Solving]]"
day: 15
---

# Extreme Weather Warning System

Pseudocode solution from [[Hands-On Modular Problem Solving]].

```
FUNCTION getWindSpeed()
	OUTPUT windspeed 	//get windspeed from satellite
	RETURN windspeed
ENDFUNCTION



FUNCTION getTornadoCategory(windspeed)
	DECLARE category
	IF windspeed > 200 THEN
		SET category = “EF5”
	ELSE IF windspeed > 165 THEN
		SET category = “EF4”
	ELSE IF windspeed > 135 THEN
		SET category = “EF3”
	ELSE IF windspeed > 110 THEN
		SET category = “EF2”
	ELSE IF windspeed > 85 THEN
		SET category = “EF1”
	ELSE 
		SET category = “EF0”
	ENDIF
	RETURN category
ENDFUNCTION
 


FUNCTION getHurricaneCategory(windspeed)
	DECLARE category
	IF windspeed > 156 THEN
		SET category = “Category 5”
	ELSE IF windspeed > 129 THEN
		SET category = “Category 4”
	ELSE IF windspeed > 110 THEN
		SET category = “Category 3”
	ELSE IF windspeed > 95 THEN
		SET category = “Category 2”
	ELSE 
		SET category = “Category 1”
	ENDIF
	RETURN category
ENDFUNCTION
FUNCTION getRainfall()
	OUTPUT rainfall 		//get rainfall from satellite
	RETURN rainfall
ENDFUNCTION




START
INPUT stormType		// input from user
OUTPUT likelihood	// output from system
DECLARE warningMessage	//message to be sent out
IF stormType != “thunderstorm” THEN 
	DECLARE windspeed = getWindSpeed()
	DECLARE category
	IF stormType == “tornado”
		SET category = getTornadoCategory(windspeed)
	ELSE
		SET category = getHurricaneCategory(windspeed)
	ENDIF
	SET warningMessage = “Warning! ” + likelihood + “ percent chance                    of Category” + category + stormType 

ELSE
	DECLARE rainfall = getRainfall()
	SET warningMessage = “Warning! ” + likelihood + “ percent chance of ”	+ stormType + “with rainfall of ” + rainfall
ENDIF

IF likelihood > 70 THEN
	sendWarningMessage(warningMessage)
ENDIF
END
```
