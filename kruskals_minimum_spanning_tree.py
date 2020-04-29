# Kruskals minimum spanning tree algorithm

# Input:  n = the number of nodes
#         edges= a list of edges in form [u,v,weight]

# Output : The weight of the minimum spanning tree


def kruskals(n, edges):
    a=sorted(edges,key=lambda x :x[2])
    def union(u,v,arr):
        a1=arr[u]
        a2=arr[v]
        for i in range(len(arr)):
            if arr[i]==a1:
                arr[i]=a2

    def find(a,b,arr):
        if arr[a]==arr[b]:
            return True
        else:
            return False

    final=[i for i in range(n)]

    i=0
    res=0
    while(len(set(final))!=1):
        if not find(a[i][0]-1,a[i][1]-1,final):
            union(a[i][0]-1,a[i][1]-1,final)
            res+=a[i][2]
            i+=1
        else:
            i+=1
    return(res)