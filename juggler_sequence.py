#  Jugglers sequence    ak+1 = ak ** 1/2   if ak is eve
							 # ak ** 3/2   if ak is odd

#  Input : The starting number
#  Output : A list of jugger sequence

import math
def juggler_sequence(n):
	res=[]
	a=n
	res.append(a)
	while a!=1:
		b=0
		if a%2==0:
			b=math.floor(math.sqrt(a))
		else:
			b=math.floor(math.sqrt(a)*math.sqrt(a)*math.sqrt(a))
		res.append(b)
		a=b
	return res
