#  Program for factorial of a number

# Input : The number n

# Output: An integer which the factorial of the given number

def Factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return(fact)