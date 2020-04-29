import math
t=int(input())
for i in range(t):
    n=int(input())
    print(sum(map(int,str(math.factorial(n)))))