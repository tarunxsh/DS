#import pdb
#pdb.set_trace()

class Node:
	 def __init__(self, val):
		 self.data = val
		 self.next = None
	 def getData(self):
	 	return self.data
	 def getNext(self):
	 	return self.next
	 def setData(self, val):
	 	self.data = val
	 def setNext(self, val):
	 	self.next = val
class LinkedList:
	 def __init__(self):
	 	self.head = None
	 def isEmpty(self):
	 	"""Check if the list is empty"""
	 	return self.head is None
	 def add(self, item):
	 	"""Add the item to the list"""
	 	new_node = Node(item)
	 	#breakpoint()
	 	new_node.setNext(self.head)
	 	self.head = new_node

	 def size(self):
		 """Return the length/size of the list"""
		 count = 0
		 current = self.head
		 while current is not None:
		 	count += 1
		 	current = current.getNext()
		 return count



	 def append(self, item):
		 """Append item to the end of the list"""
		 current = self.head
		 previous = None
		 pos = 0
		 length = self.size()
		 while pos < length:
		 	previous = current
		 	current = current.getNext()
		 	pos += 1
		 new_node = Node(item)
		 if previous is None:
		 	new_node.setNext(current)
		 	self.head = new_node
		 else:
		 	previous.setNext(new_node)	

	 def printList(self):
		 """Print the list"""
		 current = self.head
		 while current is not None:
		 	print(current.getData(),end =' ')
		 	current = current.getNext()
		 	