
# Longest increasing subsequence with time complexity of O(n**2)

# Input : List of nubmers

# Output: Integer denoting the length of longest increasing subsequence

def longestIncreasingSubsequence(arr):
    lis=[1 for _ in range(len(arr))]
    for i in range(1,len(arr)):
        for j in range(0,i):
            if arr[i]>arr[j] and lis[j]+1>lis[i]:
                lis[i]=lis[j]+1
    return(max(lis))