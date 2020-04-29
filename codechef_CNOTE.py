t=int(input())

for i in range(t):
    a=list(map(int,input().split()))
    x=a[0]
    y=a[0]-a[1]
    k=a[2]
    n=a[3]
    arr=[]
    for i in range(n):
        x=list(map(int,input().split()))
        arr.append(x)

    arr=sorted(arr,key=lambda x:x[1])
    flag=0
    for a,b in arr:
        if a>=y and b<=k:
          flag=1
          print("LuckyChef")
          break
    
    if flag==0:
        print("UnluckyChef")
    