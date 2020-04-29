# DFS 
# Input : The class is initialized with number of nodes
#         add edge(node1, node2)
#		  dfs(starting node,parent) 

# Output : The dfs traversal list


class Tree:
	def __init__(self,n):
		self.n=n
		self.tree=[[] for i in range(self.n+1)]
		self.res=[]

	def addedge(self,a,b):
		self.tree[a].append(b)
		self.tree[b].append(a)

	def dfs(self,s,p=0):
		self.res.append(s)
		for i in self.tree[s]:
			if i!=p:
				self.dfs(i,s)
