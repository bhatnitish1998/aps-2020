#  The number of ways of creating change given the denominations of available coins

#  Input : n The number to make
# 		   c A list of availbale denominations

#  Output  : An integer representing the number of ways the change can be made 


def getWays(n, c):

	def loop(n,c,result):
	    for i in c:
	        for j in range(i,n+1):
	            result[j]=result[j-i]+result[j]
	    return result

	result=[0 for i in range(n+1)]
	result[0]=1
	result=loop(n,c,result)
	return(result[n])
