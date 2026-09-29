START

OUTPUT "Do you want crunchy or smooth peanut butter?
INPUT peanutButterChoice
SET peanutButterType = "none"

if peanutButterChoice == "crunchy" THEN
    SET peanutButterType = "crunchy"
ELSE peanutButterChoice == "smooth" THEN
    SET peanutButterType = "smooth"
ENDIF


OUTPUT "Spread peanutButterType peanut butter on one slice"
OUTPUT "Spread jelly on the other slice"
OUTPUT "Put the slices together"
OUTPUT "Eat the Sandwich"

END


___________________________________________


START
DECLARE seeBird
SET hasPhotograph = 0


IF you see the bird THEN
    SET seeBird = True
ELSE
    SET seeBird = False
ENDIF

WHILE seeBird == True && hasPhotograph == 0
    DO
        Take photograph of bird
        View the Photograph
        IF you want to keep the image
            save the image
            SET hasPhotograph = 1
        ELSE
            Delete image
        ENDIF
ENDWHILE

END



____________________________________________


START

INPUT instrumentOfChoice
SET daysPracticed = 0

WHILE daysPracticed <= 7
    practice 1 hour for the day
    daysPracticed ++
ENDWHILE

INPUT enjoyPlaying

If enjoyPlaying == True
    continue practicing
ELSE
    stop learning instrumentOfChoice
ENDIF

END








