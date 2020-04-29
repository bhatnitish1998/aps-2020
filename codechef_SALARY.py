t=int(input())
for i in range(t):
    n=int(input())
    count=0
    arr=list(map(int,input().split()))
    
    while(len(set(arr))!=1):
        arr.sort()
        add=arr[-1]-arr[0]
        for i in range(len(arr)-1):
            arr[i]+=add
        count=count+add
    
    print (count)
        
    