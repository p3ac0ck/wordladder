# Wordladder Problem

## Problem Statement

Find the smallest number of transformations needed to change an initial word to a target word of same length. In every transformation, change only one character and make sure word exists in the given dictionary.

For example:

Input: 

	Dictionary = {POON, PLEE, SAME, POIE, PLEA, PLIE, POIN} 
	start = TOON 
	target = PLEA 

Output: 6

	TOON - POON - POIN - POIE - PLIE - PLEE - PLEA 

The python program available in the repository is given below input: 

Input:
   
	Dictionary = {MAIN,MAIL,RUIN,RAIN} 
	start = SAIL
	target = RUIN
 
The expected results are shown below: 

output: 4
 
	SAIL – MAIL – MAIN – RAIN - RUIN
