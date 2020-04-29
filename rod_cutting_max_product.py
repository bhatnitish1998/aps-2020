# Maximum product which can be obtained by cutting a rod into pieces

# Input :  The size of the initial rod

# Returns a number representing the maximum product

def rodcutmaxproduct(n):
    result=[0 for x in range(n+1)]
    for i in range(2,n+1):
        for j in range(1,int(i+1/2)):
            result[i]=max([result[i],j*(i-j),j*result[i-j]])
    return(result[n])
