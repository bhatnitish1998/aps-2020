# Counting sort

# Input: List of unsorted numbers

# Output: List of sorted numbers

def countingSort(arr):
    sortedlist=[]
    maximum=max(arr)
    final=[0 for i in range(100)]
    for i in arr:
        final[i]+=1
    for i in range(100):
        for j in range(final[i]):
            sortedlist.append(i)
    return sortedlist