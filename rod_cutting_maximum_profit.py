#  Max profit which can be made by cutting the rod into pieces with each piece having different prices

# Input:
		# n: The length of the rod
		# price: an array of prices from 1 to n

# Returns the maximum profit 


def rodcutmaxprofit(n,price):
    result=[]
    for i in range(len(price)+1):
        result.append([0 for j in range(n+1)])
    
    for i in range(1,len(price)+1):
        for j in range(1,n+1):
            if j>=i:
                result[i][j]=max([result[i-1][j],price[i-1]+result[i][j-i]])
            else:
                result[i][j]=result[i-1][j]
    return result[len(price)][n]
