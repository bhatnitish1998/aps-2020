t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort(reverse=True)
    arr1=[(arr[i]-i) for i in range(n)]
    temp=[i for i in arr1 if i>0]
    res=sum(temp)
    print(res%((10**9)+7))