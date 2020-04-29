# Kadanes algorithm for maximum sum subarray

# Input: Array of intergers

# Output: [Maximum sum , starting index , end index]

def kadane(arr):   
    n=len(arr)
    max1 = arr[0]
    start = 0
    end = 0
    mstart = 0
    mend = 0
    currmax = arr[0]
    
    for i in range(1,n):
        if arr[i] >= arr[i] + currmax :
            currmax = arr[i]
            start = i
            end = i
        else:   
            currmax = currmax + arr[i]
            end = i
            
        if currmax > max1 :      
            max1 = currmax
            mstart = start;
            mend = end;
    return[max1,mstart,mend]