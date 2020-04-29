# check if a given number is armstrong number

def armstrong(n):
	sum1=0
	temp=n
	while temp > 0:  
	   digit = temp % 10  
	   sum1 += digit ** 3  
	   temp //= 10  
	if n == sum1:
		return True
	else:  
	   return False
