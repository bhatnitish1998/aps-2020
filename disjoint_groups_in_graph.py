# Number of disjoint groups formed in the graph

# Input : n the number of nodes
#         edges = list of edges in the form of [u,v]


# Output : The number of disjoint groups in the graph

from collections import Counter

def Number_of_Groups(n, edges):
    
    def union(a,b,arr):
        a1=arr[a]
        b1=arr[b]
        for i in range(len(arr)):
            if arr[i]==a1:
                arr[i]=b1

    arr=[i for i in range(n)]
    for i in edges:
        union(i[0],i[1],arr)

    final=Counter(arr)
    keys=final.keys()
    return(len(keys))