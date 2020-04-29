# Longest increasing subsequence with time complexity of O(n logn)

# Input : List of nubmers

# Output: Integer denoting the length of longest increasing subsequence

import bisect
def longestIncreasingSubsequence(arr):
    lis=[]
    lis.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i]>lis[-1]:
            lis.append(arr[i])
        else:
            index=bisect.bisect_left(lis,arr[i],0,len(lis))
            lis[index]=arr[i]
    return(len(lis))