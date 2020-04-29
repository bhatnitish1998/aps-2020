t=int(input())
for i in range(t):
    a=list(map(int,input().split()))
    n=a[0]
    k=a[1]
    arr= a=list(map(int,input().split()))
    res=0
    for i in range(n):
        res+=arr[i]%k
    print(res%k)