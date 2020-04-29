# Find the lowest commmon ancestor of two nodes n1 and n2

def lca_iterative(root, n1, n2): 
	temp=root
	while temp: 
		if temp.data > n1 and temp.data > n2: 
			temp = temp.left 
		elif temp.data < n1 and temp.data < n2: 
			temp = temp.right 
		else: 
			break
	return temp 

