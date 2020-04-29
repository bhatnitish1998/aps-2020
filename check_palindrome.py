# check if a number is palindrome or not

def palindrome(n):
	n=list(str(n))
	if n==n[::-1]:
		return True
	else:
		return False
