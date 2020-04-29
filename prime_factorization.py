# Prime factorization

# Input: Number n

# Output : Prime factorized list

def primefactors(n):
    res=[]
    while(n%2==0):
        n=n/2
        res.append(2)
    
    for i in range(3,math.ceil(math.sqrt(n))+1,2):
        while(n%i==0):
            n=n//i
            res.append(i)
    if n>2:
        res.append(int(n))
    return(res)