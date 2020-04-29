# Rotate the linked list right by k

class Node: 
	def __init__(self, data): 
		self.data = data 
		self.next = None

class LinkedList: 

	def __init__(self): 
		self.head = None

	def rotate(self, k): 
		if k == 0: 
			return
	
		current = self.head 
		count = 1
		while(count <k and current is not None): 
			current = current.next
			count += 1
		if current is None: 
			return

		kthNode = current 
		while(current.next is not None): 
			current = current.next
		current.next = self.head  
		self.head = kthNode.next
		kthNode.next = None
