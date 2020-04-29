# Search for a node in BST

# Return None if not found else return the node 
 
def search(root,key): 
	if root is None or root.val == key: 
		return root 

	if root.val < key: 
		return search(root.right,key) 
	return search(root.left,key) 
