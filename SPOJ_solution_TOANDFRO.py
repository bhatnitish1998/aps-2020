while True:
	n=int(input())
	if n==0:
		break
	string=input()
	k=len(string)//n
	res=[]
	for i in range(0,k):
		if i%2==0:
			res.append(string[i*n:(i+1)*n])
		else:
			temp=string[i*n:(i+1)*n]
			temp=temp[::-1]
			res.append(temp)
	res=list(zip(*res))
	final=""
	for i in res:
		final+="".join(i)
	print(final)
