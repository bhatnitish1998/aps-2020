# Check if a number is fibonacci number

# Returns True if it is a fibonacci number else False


import math 
def isPerfectSquare(x): 
	s = int(math.sqrt(x)) 
	return s*s == x 
def isFibonacci(n): 
	return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4) 
