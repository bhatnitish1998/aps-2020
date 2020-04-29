t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    fib0=0
    fib1=2
    fib2=8
    sum1=2
    while(fib2<=n):
        sum1+=fib2
        fib0=fib1
        fib1=fib2
        fib2=(fib1*4)+fib0
    print(sum1)

