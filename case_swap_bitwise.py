# Swap the case of characters in a string
# Time complexity : O(n)

# Input : String

# Returns a string with cases swapped

def swapcase(sentence):

	# function to swapcase of a characeter
	def swapchar(c):
		a=ord(c)
		if a|32==a:
			a&=~32
		elif a&~32 ==a:
			a|=32
		return chr(a)

	res=""
	for i in sentence:
		res+=swapchar(i)
	return(res)