# Post order traversal of BST

def printPostorder(root): 
	if root: 
		printPostorder(root.left) 
		printPostorder(root.right) 
		print(root.val), 
