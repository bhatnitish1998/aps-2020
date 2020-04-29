n=int(input())
for _ in range(n):
	a,b=list(map(int,input().split()))
	a=str(a)[::-1]
	b=str(b)[::-1]
	res=int(a)+int(b)
	final=str(res)[::-1]
	print(int(final))
