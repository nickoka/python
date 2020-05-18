class Node:

	# class constructor
	def __init__(self, x):
		self.val = x
		self.next = None

class LinkedList:

	# class constructor
	def __init__(self):
		self.head = None
		self.tail = None

	# empty method
	def empty(self):
		if self.head == None:
			return True
		else:
			return False

	# add method
	def add(self, x):
		node = Node(x)
		# adds element to the head of the list (stack)
		if self.is_empty():
			self.head = node
			self.head.next = None
			self.tail = node
		else:
			temp = self.head
			self.head = node
			self.head.next = temp

	def add_tail(self, x):
		node = Node(x)
		if self.is_empty():
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node

	# remove method
	def remove(self):
		# list with only one element
		if self.head.next == None:
			temp = self.head.val
			self.head = self.head.next
			self.head = None
		else:
			temp = self.head.val
			self.head = self.head.next
		return temp
