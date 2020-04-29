from sys import stdin, stdout
t=int(input())
for _ in range(t):
    n,q=list(map(int,stdin.readline().split()))
    arr=list(map(int,stdin.readline().split()))
    first=int(stdin.readline())
    even=0
    odd=0
    for i in arr:
        if (bin(i^first)).count('1')%2==0:
            even+=1
        else:
            odd +=1
    stdout.write(str(even)+' '+str(odd)+'\n')
    for a in range(q-1):
        next1=int(stdin.readline())
        if (bin(next1^first)).count('1')%2==0:
            stdout.write(str(even)+' '+str(odd)+'\n')
        else:
            stdout.write(str(odd)+' '+str(even)+'\n')
    