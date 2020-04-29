while True:
	n=int(input())
	if n==-1:
		break
	res=[]
	sum1=0
	for i in range(n):
		temp=int(input())
		res.append(temp)
		sum1+=temp
	if sum1%n!=0:
		print(-1)
	else:
		final=0
		avg=sum1//n
		for i in range(n):
			if res[i]>avg:
				final+=res[i]-avg
		print(final)
