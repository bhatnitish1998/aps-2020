import datetime
arr=[]
for i in range(2000,2400):
    d=datetime.datetime(i,2,1)
    if d.strftime("%a")=="Sat":
        arr.append(1)
    elif d.strftime("%a")=="Sun" and not ((i%4==0 and i%100!=0) or i%400==0):
        arr.append(1)
    else:
        arr.append(0)

t=int(input())
for i in range(t):
    m=list(map(int,input().split()))
    y=list(map(int,input().split()))
    m1=m[0]
    if m1>2:
        m[1]+=1
    m2=y[0]
    if m2==1:
        y[1]-=1
    count=0

    y1=m[1]
    y2=y[1]
    sub=(y2-y1)%400
    for i in range(y1,y1+sub+1):
        count+=arr[i%400]

    count+=((y[1]-m[1])//400)*sum(arr)
    print(count)
    
