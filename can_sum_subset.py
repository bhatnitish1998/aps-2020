#  Can a required sum be formed from subset of given array

# Input : required sum, the array of numbers

# Output : 1 if it is possible to make required sum else zero


def can_subset_sum(req,arr):
	n=len(arr)
	W=sum(arr)
	possible=[0]*(W+1)
	possible[0]=1
	for k in range(0,n):
		for x in range(W,-1,-1):
			if possible[x]:
				possible[x+arr[k]]=1
	print(possible)
	return possible[req]