t=int(input())
for i in range(t):
    a=list(map(int,input().split()))
    n=a[0]
    c=a[1]

    req=list(map(int,input().split()))
    
    total=sum(req)
    if total<=c:
        print("Yes")
    else:
        print("No")