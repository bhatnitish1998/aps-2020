# Check if a graph is connected

# Input : The class is initialized with number of nodes
#         add edge(node1, node2)
#		  connected()

# Output : True if graph is connected else false


class Graph:
	def __init__(self,n):
		self.n=n
		self.graph=[[] for i in range(self.n+1)]
		self.visited=[0]*(self.n+1)

	def addedge(self,a,b):
		self.graph[a].append(b)
		self.graph[b].append(a)

	def dfs(self,s):
		if self.visited[s]:
			return
		self.visited[s]=1
		for i in self.graph[s]:
			self.dfs(i)

	def connected(self):
		self.dfs(0)
		if sum(self.visited)==self.n:
			return True
		else:
			return False