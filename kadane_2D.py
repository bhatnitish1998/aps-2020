# 2D Kadanes algorithm for maximum sum submatrix

# Input: matrix

# Output : [Maximum sum, left ,right ,top ,bottom]

def kadane2D(arr):
	def kadane(arr):   
	    n=len(arr)
	    max1 = arr[0]
	    start = 0
	    end = 0
	    mstart = 0
	    mend = 0
	    currmax = arr[0]
	    
	    for i in range(1,n):
	        if arr[i] >= arr[i] + currmax :
	            currmax = arr[i]
	            start = i
	            end = i
	        else:   
	            currmax = currmax + arr[i]
	            end = i
	            
	        if currmax > max1 :      
	            max1 = currmax
	            mstart = start;
	            mend = end;
	    return[max1,mstart,mend]
	n=len(arr)
	m=len(arr[0])
	currentmax=-999999999
	maxsofar=-999999999
	r=0
	l=0
	u=0
	d=0
	for left in range(m):
	    temp=[0 for i in range(n)]
	    for right in range(left,m):
	        for i in range(n):
	            temp[i]+=arr[i][right]
	        currentmax,x,y=kadane(temp)
	        if currentmax>maxsofar:
	            maxsofar=currentmax
	            r=right
	            l=left
	            u=x
	            d=y
	return([maxsofar,l,r,u,d])



