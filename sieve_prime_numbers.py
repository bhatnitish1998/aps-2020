# Sieve of erasthones for generating prime numbers

# Returns a list of prime numbers from 2 to n

def sieve(limit):
	primes=[]
	mark = [False]*(limit+1)  
	for i in range(2, limit+1): 
	    if not mark[i]: 
	        primes.append(i) 
	        for j in range(i, limit+1, i): 
	            mark[j] = True
	return primes


