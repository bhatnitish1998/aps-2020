t=int(input())
a=[(1,1),(8,8),(7,7),(8,6),(3,1),(4,2),(5,1),(8,4),(7,3),(8,2),(7,1),
   (3,5),(1,3),(6,8),(5,7),(4,8),(1,5),(2,6),(1,7),(2,8),(5,5)]
for _ in range(t):
    count=0
    x,y=list(map(int,input().split()))
    u=x
    v=y
    
    if x!=8 or y!=8:
        while x<8 and y<8:
            x+=1
            y+=1
    index=0
    for i in range(len(a)):
        if a[i][0]==x and a[i][1]==y:
            index=i
            break
    final=a[index:]+a[:index]
    count+=len(final)
    if final[0][0] ==u and final [0][1]==v:
        final=final[1:]+final[0:1]
    print(count+1)
    for p,q in final:
        print(p,q)
    print(final[0][0],final[0][1])
            
    