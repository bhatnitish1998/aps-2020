# Insert a node at the beginning of the linked list

class Node: 
	def __init__(self, data): 
		self.data = data 
		self.next = None 

class LinkedList: 
	def __init__(self): 
		self.head = None

	def insert_at_beginning(self, new_data): 
		new_node = Node(new_data) 
		new_node.next = self.head 
		self.head = new_node