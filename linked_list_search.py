# Search linked list for the given key

class Node: 
	def __init__(self, data): 
		self.data = data 
		self.next = None 


class LinkedList: 
	def __init__(self): 
		self.head = None

	def search(self, x): 
		current = self.head 
		while current != None: 
			if current.data == x: 
				return True 
			current = current.next
		return False 