while True:
	n=int(input())
	if n==0:
		break
	arr=list(map(int,input().split()))
	arr.insert(0,0)
	flag=0
	for i in range(1,n+1):
		if arr[arr[i]]!=i:
			print("not ambiguous")
			flag=1
			break
	if not flag:
		print("ambiguous")
