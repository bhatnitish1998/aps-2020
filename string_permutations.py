# All the permutations of a given string with duplicates
# Time Complexity =O(n**2 * n!)


# Input a=list(string)
# 		l= starting index
# 		r= ending index


# Returns  a list containing all permutations of the given string

def string_permutations(a,l,r,res=[]):
	if l==r:
		res.append("".join(a))
	else:
		for i in range(l,r+1):
			a[l],a[i]=a[i],a[l]
			string_permutations(a,l+1,r)
			a[l],a[i]=a[i],a[l]
	return(res)