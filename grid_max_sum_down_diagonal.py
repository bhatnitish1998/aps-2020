# Maximum sum from start to end of grid only moving down or diagonally downward

# input : Grid

# Output : returns the maximum sum of the path


def findMaxPath(mat): 
	h=len(mat)
	w=len(mat[0])
	sum1=[[0]*w for i in range(h)]
	for i in range(h):
		for j in range(w):
			temp=-1
			if j-1>=0:
				temp=max(temp,sum1[i-1][j-1])
			if j+1<w:
				temp=max(temp,sum1[i-1][j+1])
			temp=max(temp,sum1[i-1][j])
			sum1[i][j]=temp+mat[i][j]
	return(max(sum1[-1]))