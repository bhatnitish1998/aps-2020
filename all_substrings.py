#  All substrings of a given string
#  Time Complexity : O(n**2)


# Input : list(String)

# Returns a list of all substrings


def substrings(a):
	res=[]
	n=len(a)
	for i in range(1,n+1):
		for j in range(n-i+1):
			k=j+i-1
			res.append("".join(a[j:k+1]))
			
	return(res)