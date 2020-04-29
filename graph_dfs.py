# DFS 

# Input : The class is initialized with number of nodes
#         add edge(node1, node2)
#		  dfs(starting node)

# Output : The dfs traversal list is stored in res of the class



class Graph:
	def __init__(self,n):
		self.n=n
		self.graph=[[] for i in range(self.n+1)]
		self.visited=[0]*(self.n+1)
		self.res=[]

	def addedge(self,a,b):
		self.graph[a].append(b)
		self.graph[b].append(a)

	def dfs(self,s):
		if self.visited[s]:
			return
		self.visited[s]=1
		self.res.append(s)
		for i in self.graph[s]:
			self.dfs(i)