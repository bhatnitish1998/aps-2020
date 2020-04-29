# Fenwick tree to calculate the sum in range queries

# Input : Update(index,value) array is 1 indexed
#		  qlr(left index, right index both inclusive)  Note it is 1-indexed

# Output: qlr=The sum of elements in the range


#n= len(arr)
fenwik=[0]*(n+1)

def update(i,value):
	global fenwik
	global n
	while(i<=n):
		fenwik[i]+=value
		i+=i&-i
		
def query(x):
	global fenwik
	global n
	qsum=0
	while(x>=1):
		qsum+=fenwik[x]
		x-=x&-x
	return qsum

def qlr(l,r):
	return(query(r)-query(l-1))