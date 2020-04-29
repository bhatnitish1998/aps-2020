# Powerset of a set

# Input : a list or a set

# Output : a list of all subsets or powerset

def powerset(s):
	res=[]
	x = len(s)
	for i in range(1 << x):
		temp=[]
		for j in range(x):
			if i&(1<<j):
				temp.append(s[j])
		res.append(temp)
	return res