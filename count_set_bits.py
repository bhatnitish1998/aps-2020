# Count the mumber of set bits in a given number

#  Input : Number

# Returns count of set bits

def countsetbits(n):
	count=0
	while n!=0:
		n=n&n-1
		count+=1
	return count