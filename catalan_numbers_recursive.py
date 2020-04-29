# Program to find the nth catalan numbers (1,1,2,5,14,42,132.....)

# Input: n

# Output : The nth catalan number


def catalan(n):
	if n<=1:
		return 1
	res=0
	for i in range(n):
		res+=catalan(i)*catalan(n-i-1)

	return res
