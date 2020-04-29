t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    res=0
    oddno=0
    for i in range(n):
        flag=0
        if arr[i]%4==0:
            res+=n-i
            temp=((oddno)*(oddno+1))//2
            res+=temp
            res+=oddno*(n-i)
            oddno=0
    
        elif arr[i]%2==0:
            for j in range(i+1,n):
                if arr[j]%2==0:
                    res+=n-j
                    flag=1
                    break
            temp=((oddno)*(oddno+1))//2
            res+=temp
            if flag==1:
                res+=oddno*(n-j)
            oddno=0
        else:
            oddno+=1
            
    temp=((oddno)*(oddno+1))//2
    res+=temp

    print(res)