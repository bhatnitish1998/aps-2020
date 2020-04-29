# Level Order traversal of BST

# Input : Pointer to root (node has left, right, data attributes)

# Output : Returns a list of level order traversal

def levelOrder(root):
	res=[]
    queue=[]
    queue.append(root)
    while queue:
        current=queue[0]
        res.append(current.data)
        print(current.data,end=' ')
        if current.left!=None:
            queue.append(current.left)
        if current.right!=None:
            queue.append(current.right)
        queue.pop(0)
    return(res)