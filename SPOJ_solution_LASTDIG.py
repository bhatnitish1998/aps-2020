cyclicity=[1,1,4,4,2,1,1,4,4,2]
t=int(input())
for _ in range(t):
	a,b=list(map(int,input().split()))
	l=a%10
	r=b%cyclicity[l]
	if r==0:
		if b==0:
			res=1
		else:
			res=(l**cyclicity[l])%10
	else:
		res=(l**r)%10
	print(res)

