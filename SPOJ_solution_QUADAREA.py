import math
t=int(input())
for _ in range(t):
	a,b,c,d=list(map(float,input().split()))
	s=(a+b+c+d)/2
	res=math.sqrt((s-a)*(s-b)*(s-c)*(s-d))
	print(res)