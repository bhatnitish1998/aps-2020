#  Longest common subsequence among two strings

#  Input : Two strings

# Returns a string represnting the longest common subsequence

def lcsstring(s1,s2):
    lcs=[]
    result=[]
    for i in range(len(s1)+1):
        lcs.append([0 for j in range(len(s2)+1)])
        
    
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1] == s2[j-1]:
                lcs[i][j]=lcs[i-1][j-1]+1
            else:
                lcs[i][j]=max([lcs[i-1][j],lcs[i][j-1]])

    x=len(s1)
    y=len(s2)
    current=lcs[x][y]
    while (current!=0):
        if lcs[x][y]==lcs[x][y-1]:
            y=y-1
        elif lcs[x][y]==lcs[x-1][y]:
            x=x-1
        else:
            result.append(s1[x-1])
            current=current-1
            x=x-1
            y=y-1
    result.reverse()
    return("".join(result))
