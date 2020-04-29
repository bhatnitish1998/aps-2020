# Maximum sum from start to end of grid only moving right or down

# input : Grid

# Output : the maximum sum of the path

def grid_path(mat):
	n=len(mat)
	m=len(mat[0])
	sum1=[[0]*(m) for i in range(n)]
	for y in range(0,n):
		for x in range(0,m):
			sum1[y][x]=max(sum1[y][x-1],sum1[y-1][x])+mat[y][x]
	return(sum1[n-1][m-1])