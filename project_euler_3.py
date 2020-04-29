import math
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    num=n
    while(n%2==0):
        n=n//2
    if n==1:
        print(2)
        break
    i=3
    maxprime=1
    step1=n
    while i<=int(math.sqrt(n)):
        if n%i==0:
            n=n//i
            maxprime=i
            i-=2
        i+=2
    if n>2:
        print(n)
    else:
        print(maxprime)
        
    