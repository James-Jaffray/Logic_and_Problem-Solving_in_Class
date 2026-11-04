---
aliases: [Block Sorting Solution]
tags: [logic-and-problem-solving, term1, practice, pseudocode, functions, modular-thinking]
course: "[[Logic and Problem-Solving]]"
day: 15
---

# Block Sorting System

Pseudocode solution from [[Hands-On Modular Problem Solving]].

```
FUNCTION getColorCode(color)
	DECLARE colorCode
	IF color == “Red” THEN
		SET colorCode = “R”
	ELSE IF color == “Blue” THEN
		SET colorCode = “B”
	ELSE
		SET colorCode = “G”
	ENDIF
	RETURN colorCode
ENDFUNCTION

FUNCTION getSizeCode(size)
	DECLARE sizeCode
	IF size >= 30 THEN
		SET sizeCode =”L”
	ELSE IF size >= 20 THEN
		SET sizeCode = “M”
	ELSE
		SET sizeCode = “S”
	ENDIF
	RETURN sizeCode
ENDFUNCTION

FUNCTION getShapeCode(numberOfSides)
	DECLARE shapeCode
	IF numberOfSides == 4 THEN
		SET shapeCode = “R”
	ELSE IF numberOfSides == 3 THEN
		SET shapeCode = “T”
	ELSE
		SET shapeCode = “C”
	ENDIF
	RETURN shapeCode
ENDFUNCTION



FUNCTION getBucketCode(color, size, numberOfSides)
	DECLARE sizeCode = getSizeCode(size)
	DECLARE colorCode = getColorCode(color)
	DECLARE shapeCode = getShapeCode(numberOfSides)
	RETURN sizeCode + colorCode + shapeCode
ENDFUNCTION

FUNCTION getBlockSize(block)
	OUTPUT width = scan width from block
	OUTPUT height = scan height from block
	RETURN width * height
ENDFUNCTION

FUNCTION getBlockColor(block)
	OUTPUT color = scan color from block
	RETURN color
ENDFUNCTION

FUNCTION getBlockSides(block)
	OUTPUT numSides = scan number of sides from block
	RETURN numSides
ENDFUNCTION


START
INPUT block // get block from the user
DECLARE blockSize = getBlockSize(block)
DECLARE blockColor = getBlockColor(block)
DECLARE blockNumSides = getBlockSides(block)
DECLARE bucketCode = getBucketCode(blockColor, blockSize,							 blockNumSides)
PRINT “The block’s bucket code is: ” + bucketCode
Place block into bucketCode bucket
END
```
