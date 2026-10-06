## Q1

START
INPUT numberOfBooks
DECLARE counter = 0
WHILE counter < numBooks
	INPUT bookCategory	
	IF bookCategory == “Fiction” THEN
		Place book on Shelf A
	ELSE IF bookCategory == “Non-Fiction” THEN
		Place book on Shelf B
	ELSE IF bookCategory == “Cooking” THEN
		Place book on Shelf C
	ELSE
		Place book on Shelf B
	ENDIF 
END

### Logical Errors

- infinite loop as the counter will always be below 0
- else - place bookon shelf B will mix non-fiction with many different catagories
- while counter will stop while there is still 1 book (should be <= numberofbooks>)

START
INPUT numberOfBooks
DECLARE counter = 0

WHILE counter <= numBooks
	INPUT bookCategory
	IF bookCategory == “Fiction” THEN
		Place book on Shelf A
        SET counter = counter + 1
	ELSE IF bookCategory == “Non-Fiction” THEN
		Place book on Shelf B
        SET counter = counter + 1
	ELSE IF bookCategory == “Cooking” THEN
		Place book on Shelf C
        SET counter = counter + 1
	ELSE
		Place book on Shelf D
        SET counter = counter + 1
	ENDIF 
END




## Q2

START
INPUT numHouses
DECLARE total = 0
DO
	INPUT donation
	total = donation + donation
	counter = counter + 1
UNTIL counter > numHouses
IF total > 200 THEN
	OUTPUT Receive gold medal 
ELSE IF total = 100 THEN
	OUTPUT Receive silver medal
ELSE IF total > 50 THEN	
	OUTPUT Receive bronze medal
ELSE
	OUTPUT Receive ribbon
ENDIF
END


### Logical Errors
- no counter declared
- total should equal total + donation, not donation + donation
- counter > numHouses - would run the program 1 additional time after house total

- total should be inclusive of 200 for gold medal
- total >= for 50 & 100 aswell

START
INPUT numHouses
DECLARE total = 0
DECLARE counter = 0

DO
	INPUT donation
	total = total + donation
	counter = counter + 1
UNTIL counter >= numHouses

IF total >= 200 THEN
	OUTPUT Receive gold medal 
ELSE IF total >= 100 THEN
	OUTPUT Receive silver medal
ELSE IF total >= 50 THEN	
	OUTPUT Receive bronze medal
ELSE
	OUTPUT Receive ribbon
ENDIF
END


## Q3

START
INPUT propertyValueInThousands
DECLARE actualPropertyValue = propertyValueInThousands


IF propertyValueInThousands > 1000 THEN
	DECLARE taxAmount
	taxAmount = actualPropertyValue * 1.1
ELSE IF propertyValueInThousands > 500 THEN
	taxAmount = actualPropertyValue * 1.12
ELSE IF actualPropertyValue > 200 THEN
	taxAmount = actualPropertyValue * 1.15
ELSE
	taxAmount = actualPropertyValue * 1.18
ENDIF

PRINT “Total tax is: ” + taxAmount
END


### Logical Errors

- actualPropertyValue should be actualPropertyValue = propertyValueInThousands * 1000
- the tax amount should be 0.1 not 1.1 (that is including the property price in the tax amount)
- second else if statement is checking the actualpropertyvalue - should still be checking against propertyvalueinthousands
- comparitors should be inclusive >=


START
INPUT propertyValueInThousands
DECLARE actualPropertyValue
SET actualPropertyValue = (propertyValueInThousands * 1000)

IF propertyValueInThousands >= 1000 THEN
	DECLARE taxAmount
	taxAmount = actualPropertyValue * 0.1
ELSE IF propertyValueInThousands >= 500 THEN
	taxAmount = actualPropertyValue * 0.12
ELSE IF propertyValueInThousands >= 200 THEN
	taxAmount = actualPropertyValue * 0.15
ELSE
	taxAmount = actualPropertyValue * 0.18
ENDIF

PRINT “Total tax is: ” + taxAmount
END