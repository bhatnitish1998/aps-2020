# Inorder traversal of BST
def printInorder(root): 
	if root: 
		printInorder(root.left) 
		print(root.val), 
		printInorder(root.right) 
