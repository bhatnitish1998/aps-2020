# Program to print first n catalan numbers using DP

# Input : n

# Output : list of first n catalan numbers

def catalan(n):
	c=[0]*(n)
	c[0] =1
	c[1]=1
	c[2]=2
	for i in range(3,n):
		c[i]=0
		for j in range(i):

			c[i]+=c[j] * c[(i-1)-j]
	return c

print(catalan(10))