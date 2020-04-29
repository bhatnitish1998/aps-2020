# Express P/Q mod m 

# Input : p , q , m

# Output: integer value representing P/Q modulo m

def mod(p,q,m):
    p = p % m 
    inv = pow(q, m-2, m) 
    ans=(inv*p) % m
    return ans