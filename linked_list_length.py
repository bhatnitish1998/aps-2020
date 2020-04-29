# Length of linked list
class Node: 
	def __init__(self, data): 
		self.data = data 
		self.next = None 


class LinkedList: 

	def __init__(self): 
		self.head = None

	def getlength(self): 
		temp = self.head 
		count = 0 
		while (temp): 
			count += 1
			temp = temp.next
		return count 