#  Josephus problem iterative
#  n person stand in circle , kth person are killed until one survives

#  Input: number of people n
#         value of k

# Output: Integer of the survivor

def josephus_problem(n,k):
	if n==1:
		return 1
	return  (josephus_problem(n-1,k)+(k-1))%n+1