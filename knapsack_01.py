# KnapSack 01 Problem. Given list of items with weights and value, find the maximum value with weight <=capacity

# Input : 	capacity, list of weights, list of values for each weights

# Output : the maximum value with weight less than or equal to capacity

def KnapSack(capacity, weight, value): 
	n=len(value)
	dp = [[0 for x in range(capacity+1)] for x in range(n+1)] 
	for i in range(n+1): 
		for w in range(capacity+1): 
			if i==0 or w==0: 
				dp[i][w] = 0
			elif weight[i-1] <= w: 
				dp[i][w] = max(value[i-1] + dp[i-1][w-weight[i-1]], dp[i-1][w]) 
			else: 
				dp[i][w] = dp[i-1][w] 

	return dp[n][capacity] 
