# Recursive program for binomial coefficinets
# Input : n,k where ,  bc of x**k  in expansion  (1+x)**n

def bc(n,k):
	if n==k or k==0:
		return 1
	else:
		return bc(n-1,k-1)+bc(n-1,k)
