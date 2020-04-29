# BFS 

# Input : The class is initialized with number of nodes
#         add edge(node1, node2)
#		  bfs(starting node)

# Output : The bfs traversal list is stored in res of the class



class Graph:
	def __init__(self,n):
		self.n=n
		self.graph=[[] for i in range(self.n+1)]
		self.visited=[0]*(self.n+1)
		self.res=[]
		self.queue=[]
		self.distance=[0]*(self.n+1)

	def addedge(self,a,b):
		self.graph[a].append(b)
		self.graph[b].append(a)

	def bfs(self,x):
		self.visited[x]=1
		self.distance[x]=0
		self.queue.append(x)
		while self.queue:
			s=self.queue.pop(0)
			self.res.append(s)
			for i in self.graph[s]:
				if self.visited[i]:
					continue
				self.visited[i]=1
				self.distance[i]=self.distance[s]+1
				self.queue.append(i)