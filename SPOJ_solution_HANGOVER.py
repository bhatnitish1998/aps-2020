while True:
    x=float(input())
    if x==0:
        break
    n=2
    while x>0:
        x-=1.0/n
        n+=1
    print(n-2,'card(s)')