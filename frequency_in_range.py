# Finding the frequency of a given element in range

# Input : array, left index, right index, element whose frequency is to be found


from collections import defaultdict
from bisect import bisect_left,bisect_right

store = defaultdict(list) 

def preproces(arr):
	global store
	n=len(arr)
	for i in range(n): 
		store[arr[i]].append(i + 1) 

def findFrequency(arr, left, right, element): 
	n=len(arr)
	a = bisect_left(store[element], left) 
	b = bisect_right(store[element], right) 
	return b - a 
