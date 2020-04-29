# Segment tree range query maximum element

# Input : build(array)
#         update(position , value )
#	      query(left,right)  left inclusive right excluisve

# Output : query= maximum element in range

# n = len(arr)
tree = [0]*(2*n); 
def build(arr): 
	global tree
	for i in range(n): 
		tree[n+i]=arr[i]
	for i in range(n-1,0,-1): 
		tree[i] = max(tree[i<<1],tree[i<<1|1])

def update(p,value):
	global tree 
	tree[p+n]=value 
	p=p+n
	i=p
	while i>1: 
		tree[i>>1]=max(tree[i],tree[i^1])
		i>>=1

def query(l,r): 
	res=float('inf')
	l+=n
	r+=n
	while l<r : 
		if (l&1) : 
			res=max(res,tree[l])
			l+=1
		if (r&1) : 
			r-=1
			res=max(res,tree[r])
		l>>=1
		r>>=1
	return res