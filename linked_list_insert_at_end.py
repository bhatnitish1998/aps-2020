# Insert a node at the end of the linked list

class Node: 
	def __init__(self, data): 
		self.data = data 
		self.next = None 


class LinkedList: 
	def __init__(self): 
		self.head = None


	def insert_at_end(self, new_data): 
		new_node = Node(new_data) 
		if self.head is None: 
			self.head = new_node 
			return
		last = self.head 
		while (last.next): 
			last = last.next
		last.next = new_node 