
import math
import functools

def lcm(a,b):
    return((a*b)//math.gcd(a,b))

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    res=functools.reduce(lcm,range(1,n+1))
    print(res)
    
