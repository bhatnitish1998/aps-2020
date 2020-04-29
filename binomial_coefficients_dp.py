# DP program for binomial coefficinets
# Input : n,k where ,  bc of x**k  in expansion  (1+x)**n

# nspace
def ndp(n,k):
	c=[0 for i in range(n+1)]
	c[0]=1
	for i in range(n+1):
		for j in range(min(i,k),0,-1):
			c[j]+=c[j-1]
	return c[k]