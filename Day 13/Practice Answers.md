---
tags: [logic-and-problem-solving, term1, practice, modular-thinking, pseudocode]
course: "[[Logic and Problem-Solving]]"
day: 13
---

1.	You are developing a library management system. This system allows users to search for books and retrieve information about each book, including the amount in stock, the section of the library it belongs to, and if there are any copies checked out. Librarians log in to this system using a username and a password. Once logged in they can check out books for customers, manage returns, and send out notification emails to books that are past due.


Requirments:
## search for books
START
INPUT bookTitle
OUTPUT bookQty
OUTPUT bookSection
OUTPUT bookCheckedOut
END


## credentials
  - username
  - password

## Check-out
START
INPUT bookTitle
    IF book qty > then checkedOutStatus THEN
        SET checkedOutStatus = checkedOutStatus + 1
        SET userInventory += bookTitle
        SET bookDueDate = currentDate + 14 days
    ELSE
        OUTPUT 'bookTitle is unavailable'
    ENDIF
END

## Returns
START
INPUT userID
OUTPUT userInventory
INPUT bookTitle

IF bookTitle is in userInventory
    remove bookTitle from userInventory
    SET checkedOutStatus = checkedOutStatus - 1
ELSE
    OUTPUT "invalid Return'
ENDIF
END

## notifications

START
INPUT userID
IF currentDate >= bookDueDate
    OUTPUT email notification that bookTitle is overdue
ENDIF
END


# Problem 2

Modules:
- Sign In
- printBadge

Sign In
1. fill out form
    - INPUT name
    - INPUT type
    - INPUT tainer
    - INPUT battle t/f


printBadge
1. Sign In
2. INPUT details into confrence mgmt system
3. OUTPUT pokemon badge


# Problem 3

Modules:
- Offensive Play
- Defensive Play
- Hail Mary Play

offensivePlay
1. must complete 3+ passes
2. Take a shot
   

defensivePlay:
1. 2 players guard against opponent with the ball
2. 1 player guards the net
3. 2 players cover assigned man-to-man opponents
   

hailMaryPlay
1. 4 players sheild the ball handler
2. 1 player brings the ball to the 3 pt line
3. player with ball takes the shot

