# Hamming distance of  two numbers, when they are represented in binary

# Input : two integer numbers

def hamming(a,b):
	n=a^b 
	count = 0
	while n: 
		count += 1
		n &= (n-1) 
	return count 

