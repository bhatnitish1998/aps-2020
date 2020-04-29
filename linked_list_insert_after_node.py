# Insert a node after the given node

# input : previous node, data to be inserted

class Node: 
	def __init__(self, data): 
		self.data = data 
		self.next = None 


class LinkedList: 
	def __init__(self): 
		self.head = None

	def insert_after_node(self, prev_node, new_data): 
		new_node = Node(new_data)  
		new_node.next = prev_node.next
		prev_node.next = new_node 
