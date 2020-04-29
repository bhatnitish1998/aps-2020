t=int(input())
for _ in range(t):
	blank=input()
	n=int(input())
	res=0
	for i in range(n):
		res+=int(input())
	if res%n==0:
		print("YES")
	else:
		print("NO")
