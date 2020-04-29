# Minimum number of coins required for making a given sum

# input  n =Sum to make
#		 coins =list of available coins

# Output: The minimum number of coins required to make sum

def min_coin(n,coins):
	value=[0]*(n+1)
	value[0]=0
	for x in range(1,n+1):
		value[x]=float('inf')
		for c in coins:
			if x-c >=0:
				value[x]=min(value[x],value[x-c]+1)
	return(value[n])