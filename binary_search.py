# Binary search in range

# Input : Array,left index,right index,key

# Output : index if the element is present in the array
#		   -1 if the element  is not present in the array

def binarySearch(arr, l, r, x): 
	while l <= r: 

		mid = l + (r - l) // 2; 
		if arr[mid] == x: 
			return mid 
		elif arr[mid] < x: 
			l = mid + 1

		else: 
			r = mid - 1

	return -1
