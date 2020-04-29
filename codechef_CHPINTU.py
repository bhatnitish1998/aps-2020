from collections import defaultdict
t=int(input())
for _ in range(t):
    z=defaultdict(int)
    n,m=list(map(int,input().split()))
    fruit=list(map(int,input().split()))
    cost=list(map(int,input().split()))
    for a,b in zip(fruit,cost):
        z[a]+=b
    res=min(z.values())
    print(res)
    
