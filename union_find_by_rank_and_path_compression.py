# Union by rank and find with path compression
# Note : Node also keeps track of size  so find(x).size gives the total size of that component

class Node:
    def __init__(self,data):
        self.data=data
        self.parent=self
        self.rank=0
        self.size=1
    
class Graph:
    def makeset(data):
        return(Node(data))

    def find(node):
        if node.parent!=node:
            node.parent=Graph.find(node.parent)
        return(node.parent)

    def union(node1,node2):
        a=Graph.find(node1)
        b=Graph.find(node2)

        if a!=b:
            if a.rank>b.rank:
                b.parent=a
                a.size+=b.size
            else:
                a.parent=b
                b.size+=a.size
                if a.rank==b.rank:
                    a.rank+=1
