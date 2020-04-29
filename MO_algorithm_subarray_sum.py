
#  MO's algorithm for sub array sum range offline queries

# Input : list of numbers, list of queries [l,r] inclusive both  and zero indexed
# Output : list containing answers of queries

import math
def mo_subarray_sum(arr,queries):
	res=[0]*(len(queries))
	n=len(arr)
	block_size = math.floor(math.sqrt(n))

	# keeping track of order of queries
	for i in range(len(queries)):
		queries[i].extend([i])


	# sorting the queries
	queries.sort(key=lambda x:x[0]//block_size)

	current=0
	mo_left=0
	mo_right=-1

	for i in queries:

		while(mo_right<i[1]):
			mo_right+=1
			current+=arr[mo_right]

		while(mo_right>i[1]):
			current-=arr[mo_right]
			mo_right-=1

		while(mo_left<i[0]):
			current-=arr[mo_left]
			mo_left+=1

		while(mo_left>i[0]):
			mo_left-=1
			current+=arr[mo_left]

		res[i[2]]=current

	return res
