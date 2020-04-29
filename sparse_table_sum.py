# sparse table for sum of elements in the range

# Output : query returns the sum of elements in range 

import math

# k = math.ceil(math.log2(len(arr)))
# n = len(arr)

table=[[0]*(int(math.log2(n))+1) for i in range(n)]

def buildSparseTable(arr): 
	n=len(arr)
	global table, k 
	for i in range(n): 
		table[i][0] = arr[i] 

	for j in range(1,k+1): 
		for i in range(0,n-(1<<j)+1): 
			table[i][j] = table[i][j-1] + table[i + (1 << (j - 1))][j - 1] 

def query(L, R): 
	global table, k 
	answer = 0
	for j in range(k,-1,-1): 
		if (L + (1 << j) - 1 <= R): 
			answer = answer + table[L][j] 
			L+=1<<j 
	return answer 
