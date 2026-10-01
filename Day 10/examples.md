START

DECLARE orderedDonut
DECLARE donutAvailable
walk into the cafe
read the menu
INPUT order a muffin

IF muffin available = 'yes' THEN
    INPUT pay for muffin
    wait for the cashier
    OUTPUT recieve muffin

ELSE
    INPUT order a donut
    SET orderedDonut = True
ENDIF

IF orderedDonut = True && donutAvailable = yes THEN
    INPUT pay for donut
    wait for cashier to wrap donut
    OUTPUT recieve donut
ELSE
    skip donut
ENDIF
    
OUTPUT want coffee
IF yes THEN
    INPUT pay for coffee
    wait for barista to prepare coffee
    OUTPUT recieve coffee
ELSE
    Skip coffee
ENDIF

leave cafe
END



_________________________________


START

DECLARE firstNumber
DECLARE secondNumber
notANumber = True

WHILE notANumber = True
    OUTPUT Please enter first number
    INPUT firstNumber

    IF firstNumber is a number THEN
        SET notANumber = False
    ELSE
        SET notANumber = True
    ENDIF
ENDWHILE

SET notANumber = True
OUTPUT prompt user to input second number

WHILE notANumber = True
    OUTPUT Please enter second number
    INPUT secondNumber

    IF secondNumber is a number THEN
        SET notANumber = False
    ELSE
        SET notANumber = True
    ENDIF
ENDWHILE

DECLARE remainder = firstNumber % secondNumber

IF remainder == 0
    OUTPUT Number is divisible
ELSE
    OUTPUT Number is not divisible
ENDIF


END





__________________________________________________


START

Navigate to website

IF login is required THEN
    DO
    INPUT username
    INPUT Password

    validate username/password

    UNTIL username/password are validated
ELSE
    skip validation
ENDIF

navigate to account settings

DECLARE subscribed = True

WHILE subscribed
    INPUT unsubscribe
    OUTPUT No! Please dont leave me
    SET subscribed = Fales
ENDWHILE

INPUT logout

END - (not start as seen in example)







