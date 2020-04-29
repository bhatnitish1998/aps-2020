t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    temp1=(n*(n+1))//2
    temp2=(n*(n+1)*((2*n)+1))//6
    print(temp1**2-temp2)
