#  Josephus problem where alternate people are killed
#  The sequence starts with 1

#  Input : the number of people

# Output : Integer of the person surviving

import math
def josephus_alternate(n):
	return 2*(n-2**(math.floor(math.log2(n))))+1
