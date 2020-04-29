# Find the height of binary search tree

# Input Pointer to root node (Node has left right and data attributes)

# Output : Height of binary search tree

def getHeight(root):
    if root==None:
        return(-1)
    left=self.getHeight(root.left)
    right=self.getHeight(root.right)
    return(max(left,right)+1)