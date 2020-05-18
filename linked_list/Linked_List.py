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
	def add(self, x, y):
		node = Node(x)
		# adds element to the head of the list (stack)
		if y == 1:
			if self.is_empty():
				self.head = node
				self.head.next = None
				self.tail = node
			else:
				temp = self.head
				self.head = node
				self.head.next = temp
		# adds element to the tail of the list (queue)
		elif y == 2:
			if self.is_empty():
				self.head = node
				self.tail = node
			else:
				self.tail.next = node
				self.tail = node
		return

	# remove method
	def remove(self):
		# list with only one element
		if self.head.next == None:
			temp = self.head.val
			self.head = self.head.next
			self.head = None
			self.tail = None
		else:
			temp = self.head.val
			self.head = self.head.next
		return temp
