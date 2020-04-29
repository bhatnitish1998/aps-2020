# sum of digits of a given number

def sum_of_digits(number):
	sum1 = 0
	for digit in str(number):
	  sum1 += int(digit)
	return(sum1)

