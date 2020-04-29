# The denominations of minimum nubmer of coins required to make sum

# input  n =Sum to make
#		 coins =list of available coins

# Output: list of coins making the optimal solution

def min_coin_optimal(n,coins):
	res=[]
	first=[0]*(n+1)
	value=[0]*(n+1)
	for x in range(1,n+1):
		value[x]=float('inf')
		for c in coins:
			if x-c >=0 and value[x-c]<value[x]:
				value[x]=value[x-c]+1
				first[x]=c
	while n>0:
		res.append(first[n])
		n-=first[n]
	return(res)