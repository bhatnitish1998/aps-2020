# The fibonnaci sequence using DP

# input the first term, second term and  n (n>2)

# Output: Returns list containing  first n fibonacci sequence

def fibonacci(t1, t2, n):
    dp=[0 for i in range(n+1)]
    dp[1]=t1
    dp[2]=t2
    for i in range(3,n+1):
        dp[i]=dp[i-2]+ dp[i-1]
    return(dp[1:])

