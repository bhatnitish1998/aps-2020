# Sum of digits from numbers 1 to n

import math 
def sumOfDigits(n): 
	d = int(math.log(n, 10)) 
	a = [0]*(d + 1) 
	a[0] = 0
	a[1] = 45
	for i in range(2, d + 1): 
		a[i] = a[i - 1] * 10 + 45 * int(math.ceil(pow(10, i - 1))) 
	return sumOfDigitsUtil(n, a)

def sumOfDigitsUtil(n, a): 
	if (n < 10):
		return (n * (n + 1)) // 2
	d = int(math.log(n,10)) 
	p = int(math.ceil(pow(10, d))) 
	msd = n // p 
	return (msd * a[d] + (msd * (msd - 1) // 2) * p +
	msd * (1 + n % p) + sumOfDigitsUtil(n % p, a))
