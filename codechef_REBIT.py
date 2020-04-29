import math
from fractions import Fraction

def and1(l,r):
    zero=l[0] + (l[1]*r[0])
    one=l[1]*r[1]
    return[zero,one]
    
def or1(l,r):
    zero=l[0]*r[0]
    one=(l[0]*r[1]) +l[1]
    return [zero,one]

def xor1(l,r):
    zero=(l[0]*r[0]) + (l[1]*r[1])
    one=(l[0]*r[1])  + (r[0]*l[1])
    return[zero,one]
    
def mod(a):
    a[0] = a[0] % 998244353 
    inv = pow(a[1], 998244351, 998244353) 
    ans=(inv*a[0]) % 998244353
    return ans
    
def answer(x,y):
    zero=mod([(x*x).numerator,(x*x).denominator])
    one=mod([(y*y).numerator,(y*y).denominator])
    a=mod([(x*y).numerator,(x*y).denominator])
    print(zero,one,a,a)
    

def parse(l):
    
    temp1=[]
    i=0
    while(i<len(l)):
        if l[i]=='&':
            temp1.pop()
            catch=and1(l[i-1],l[i+1])
            temp1.append(catch)
            l[i+1]=catch
            i+=1
        else:
            temp1.append(l[i])
        i+=1
        
    temp2=[]
    i=0
    while(i<len(temp1)):
        if temp1[i]=='^':
            temp2.pop()
            catch=xor1(temp1[i-1],temp1[i+1])
            temp2.append(catch)
            temp1[i+1]=catch
            i+=1
        else:
            temp2.append(temp1[i])
        i+=1
    
    temp3=[]
    i=0
    while(i<len(temp2)):
        if temp2[i]=='|':
            temp3.pop()
            catch=or1(temp2[i-1],temp2[i+1])
            temp3.append(catch)
            temp2[i+1]=catch
            i+=1
        else:
            temp3.append(temp2[i])
        i+=1
    
    return temp3[0]

t=int(input())
for _ in range(t):
    l=list(input())
    if(len(l)==1):
        print(748683265,748683265,748683265,748683265)
        continue
    
    arr=[[Fraction(1,2),Fraction(1,2)] if x=='#' else x for x in l]
    stack=[]
    for i in range(len(arr)):
        if arr[i]==')':
            temp=[]
            while(stack[-1]!='('):
                temp.append(stack.pop())
            stack.pop()
            if temp:
                stack.append(parse(temp))
        else:
            stack.append(arr[i])
    
    if len(stack)==1:
        answer(stack[0][0],stack[0][1])
    else:
        t=parse(stack)
        answer(t[0],t[1])
        
    
    



    