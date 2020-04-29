# Sparse table to calulate maximum element in range queries

# Input: Preprocess (array)   query(array, left limit , right limit both inclusive)

# Output : query = Maximum element in the given range

# n= len(arr)
table=[[0]*(int(math.log2(n))+1) for i in range(n)]

def preprocessmax(arr):
	n=len(arr)
	global table

	for i in range(n):
		table[i][0]=i
	j=1
	while(1<<j)<=n:
		i=0
		while(i+(1<<j)-1)<n:
			if arr[table[i][j-1]]>arr[table[i+(1<<(j-1))][j-1]]:
				table[i][j]=table[i][j-1]
			else:
				table[i][j]=table[i+(1<<(j-1))][j-1]
			i+=1
		j+=1

def querymax(arr,l,r):
	global table
	j=int(math.log2(r-l+1))

	if arr[table[l][j]]>=arr[table[r-(1<<j)+1][j]]:
		return arr[table[l][j]]
	else:
		return(arr[table[r-(1<<j)+1][j]])