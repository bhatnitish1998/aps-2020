t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    count=5
    flag=0
    for i in range(n):
        if arr[i]==1 and count>=5:
            count=0
        elif arr[i]==1 and count<5:
            print("NO")
            flag=1
            break
        elif arr[i]==0:
            count+=1
    if flag==0:
        print("YES")
        
