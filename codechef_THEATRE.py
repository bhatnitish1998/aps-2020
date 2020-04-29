import itertools
t=int(input())
final=[]
for i in range(t):
    n=int(input())
    twl=[]
    three=[]
    six=[]
    nine=[]
    firstsum=0
    count=[]
    for j in range(n):
        a=input().split()
        if(a[1])=='12':
            twl.append(a[0])
        if(a[1])=='3':
            three.append(a[0])
        if(a[1])=='6':
            six.append(a[0])
        if(a[1])=='9':
            nine.append(a[0])
            
    count.append([twl.count("A"),three.count("A"),six.count("A"),nine.count("A")])
    count.append([twl.count("B"),three.count("B"),six.count("B"),nine.count("B")])
    count.append([twl.count("C"),three.count("C"),six.count("C"),nine.count("C")])
    count.append([twl.count("D"),three.count("D"),six.count("D"),nine.count("D")])
        
    string1=[0,1,2,3]
    string2=[1,2,3,4]
    res=[]
    c1=list(itertools.permutations(string1))
    c2=list(itertools.permutations(string2))
    
    sum0=[]
    for i in c1:
        sum1=[]
        for j in c2:
            sum2=0
            for k in range(0,4):
                a11=count[k][i[k]]*j[k]*25
                if a11!=0:
                    sum2+=a11
                else:
                    sum2-=100
            sum1.append(sum2)
        sum0.append(max(sum1))
    
    a111=(max(sum0))
    print(a111)
    final.append(a111)
print(sum(final))

