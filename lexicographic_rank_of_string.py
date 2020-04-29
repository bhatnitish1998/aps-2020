
# Lexicographic rank of a string

import math
def right(st, low, high) : 
	countRight = 0
	i = low + 1
	while i <= high : 
		if st[i] < st[low] : 
			countRight = countRight + 1
		i = i + 1
	return countRight 
	
def findRank (st) : 
	ln = len(st) 
	mul = math.factorial(ln) 
	rank = 1
	i = 0

	while i < ln : 
		mul = mul // (ln - i) 
		countRight = right(st, i, ln-1) 
		rank = rank + countRight * mul 
		i = i + 1
	return rank