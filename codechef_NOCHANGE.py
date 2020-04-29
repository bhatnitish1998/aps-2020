t=int(input())
for _ in range(t):
    a=list(map(int,input().split()))
    p=a[1]
    n=a[0]
    d=list(map(int,input().split()))
    
    flag=0
    flag2=0
    res=[0 for i in range(len(d))]
    
    for i in range(len(d)):
        if (p%d[i])!=0:
            index=p//d[i]
            res[i]=index+1
            print("YES", end=" ")
            print(*res)
            flag=1
            break
        

    if flag==0:
        for i in range(len(d)):
            for j in range(i+1):
                if d[i]%d[j]!=0:
                    res[i]=(p//d[i]-1)
                    res[j]=(d[i]//d[j])+1
                    flag2=1
                    print("YES", end=" ")
                    print(*res)
                    break
            if flag2==1:
                break
                    
        if flag2==0:
            print("NO")
        