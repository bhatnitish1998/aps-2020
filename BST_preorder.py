# Preorder traversal of BST

def printPreorder(root): 
	if root: 
		print(root.val), 
		printPreorder(root.left) 
		printPreorder(root.right) 