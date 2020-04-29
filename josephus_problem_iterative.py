#  Josephus problem iterative
#  n person stand in circle , kth person are killed until one survives

#  Input: number of people n
#         value of k

# Output: Integer of the survivor

def josephus_problem(n,k):
	res=0
	for i in range(1,n+1):
		res=(res+k)%i
	return res+1

