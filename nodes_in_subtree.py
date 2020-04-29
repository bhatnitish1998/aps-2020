# Number of nodes in the subtree of each node

# Input : The class is initialized with number of nodes
#         add edge(node1, node2)
#		  nodes_in_subtree(starting node,parent) 

# Output : The number of nodes in subtree of each node is stored in count list of the class


class Tree:
	def __init__(self,n):
		self.n=n
		self.tree=[[] for i in range(self.n+1)]
		self.count=[0]*(n+1)

	def addedge(self,a,b):
		self.tree[a].append(b)
		self.tree[b].append(a)

	def nodes_in_subtree(self,s,p=0):
		self.count[s]=1
		for i in self.tree[s]:
			if i==p:
				continue
			self.nodes_in_subtree(i,s)
			self.count[s]+=self.count[i]
