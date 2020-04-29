n=int(input())
arr=[]
for i in range(n):
    arr.append(input())
arr.sort()
q=int(input())
for i in range(q):
    z=input()
    x=arr.index(z)+1
    sum1=0
    for j in z:
        sum1+=ord(j)-64
    print(sum1*x)
