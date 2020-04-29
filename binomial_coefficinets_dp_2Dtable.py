# DP program for binomial coefficinets using 2D table
# Input : n,k where ,  bc of x**k  in expansion  (1+x)**n

def dp2(n,k):
	c=[[0 for i in range(k+1)] for j in range(n+1)]
	for i in range(n+1):
		for j in range(min(i,k)+1):
			if i==j or j==0:
				c[i][j]=1
			else:
				c[i][j]=c[i-1][j-1]+c[i-1][j]
	return c[n][k]