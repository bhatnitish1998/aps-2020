import math
n=int(input())
count=0
for i in range(1,math.floor(math.sqrt(n))+1):
	temp=n//i
	count+=temp-(i-1)
print(count)
