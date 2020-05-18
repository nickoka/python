import sys

class Node:

	# class constructor
	def __init__(self, value, left = None, right = None, parent = None, color = None):
		self.value = value
		self.left = left
		self.right = right
		self.parent = parent
		self.color = color 

class RBT(Node): 
	
	# class constructor
	def __init__(self):
		self.root = Node(None, None, None, None, "black")
		self.nil = Node(None, None, None, None, "black")
		self.inorder = []

	# insert method
	def insert(self, z):
		y = self.nil
		x = self.root
		while (x != self.nil) and (x.value != None):
			y = x
			if z.value < x.value:
				x = x.left
			else:
				x = x.right
		z.parent = y
		if y == self.nil:
			self.root = z
		elif z.value < y.value:
			y.left = z
		else:
			y.right = z
		z.left = self.nil
		z.right = self.nil
		z.color = "red"
		self.insert_fixup(z)

	# insert_fixup method
	def insert_fixup(self, node):
		while node.parent.color == "red":
			if node.parent == node.parent.parent.left:
				y = node.parent.parent.right
				if y.color == "red":
					node.parent.color = "black"
					y.color = "black"
					node.parent.parent.color = "red"
					node = node.parent.parent
				else:
					if node == node.parent.right:
						node = node.parent
						self.left_rotate(node)
					node.parent.color = "black"
					node.parent.parent.color = "red"
					self.right_rotate(node.parent.parent)
			elif node.parent == node.parent.parent.right:
				y = node.parent.parent.left
				if y.color == "red":
					node.parent.color = "black"
					y.color = "black"
					node.parent.parent.color = "red"
					node = node.parent.parent
				else:
					if node == node.parent.left:
						node = node.parent
						self.right_rotate(node)
					node.parent.color = "black"
					node.parent.parent.color = "red"
					self.left_rotate(node.parent.parent)
		self.root.color = "black"

	# transplant method
	def transplant(self, u, v):
		if u.parent == self.nil:
			self.root = v
		elif u == u.parent.left:
			u.parent.left = v
		else:
			u.parent.right = v
		v.parent = u.parent

	# remove method
	def remove(self, value):
		x = self.root
		while True:
			if x.value == None:
				print("TreeError")
				break
			else:
				# searching for the node to remove
				if int(value) < int(x.value):
					x = x.left
				elif int(value) > int(x.value):
					x = x.right
				else:
					# different conditions when the node needing to remove is found
					# the parent node only has a right child
					if x.left.value == None and x.right.value != None:
						temp_node = self.helper_min(x.right)
						x.value = temp_node.value
						temp_node.value = None
						break
					# the parent node only has a left child
					elif x.right.value == None and x.left.value != None:
						temp_node = self.helper_max(x.left)
						x.value = temp_node.value
						temp_node.value = None
						break
					# the node has no children and the right child is the successor
					elif x.right.value != None and x.left.value != None:
						temp_node = self.helper_min(x.right)
						x.value = temp_node.value
						temp_node.value = None
						break
					else:
						x.value = None
						break

	# remove_fixup method
	def remove_fixup(self, x):
		while (x != self.root) and (x.color == "black"):
			if x == x.parent.left:
				w = x.parent.right
				if w.color == "red":
					w.color = "black"
					x.parent.color = "red"
					self.left_rotate(x.parent)
					w = x.parent.right
				elif (w.left.color == "black") and (w.right.color == "black"):
					w.color = "red"
					x = x.parent
				else:
					if w.right.color == "black":
						w.left.color = "black"
						w.color = "red"
						self.right_rotate(w)
						w = x.parent.right
					w.color = x.parent.color
					x.parent.color = "black"
					w.right.color = "black"
					self.left_rotate(x.parent)
					x = self.root
			else:
				w = x.parent.left
				if w.color == "red":
					w.color = "black"
					x.parent.color = "red"
					self.right_rotate(x.parent)
					w = x.parent.left
				elif (w.right.color == "black") and (w.left.color == "black"):
					w.color = "red"
					x = x.parent
				else:
					if w.left.color == "black":
						w.right.color = "black"
						w.color = "red"
						self.left_rotate(w)
						w = x.parent.left
					w.color = x.parent.color
					x.parent.color = "black"
					w.left.color = "black"
					self.right_rotate(x.parent)
					x = self.root
		x.color = "black"

	# search method
	def search(self, value):
		x = self.root
		while True:
			if (x.value == None) or (x == self.nil):
				return "NotFound"
			else:
				if x.value == value:
					return "Found"
				elif x.value < value:
					x = x.right
				elif x.value > value:
					x = x.left
				else:
					return "NotFound"

	# min method
	def min(self):
		result = self.helper_min(self.root)
		if result == None:
			return "Empty"
		else:
			return result.value

	# max method
	def max(self):
		result = self.helper_max(self.root)
		if result == None:
			return "Empty"
		else:
			return result.value

	# max helper method
	def helper_max(self, x):
		node = x
		if node.value == None:
			return None
		while(node.right.value != None):
			node = node.right
		return node

	# min helper method
	def helper_min(self, x):
		node = x
		if node.value == None:
			return None
		while(node.left.value != None):
			node = node.left
		return node

	# inprint method
	def inprint(self):
		if self.root.value != None: 
			self.helper_inprint(self.root)
			output = ""
			for x in self.inorder:
				output += str(x) + " "
			return output.rstrip()
		else:
			return("Empty")
		
	# inprint helper method
	def helper_inprint(self, x):
		if x != None:
			self.helper_inprint(x.left)
			if x.value != None:
				self.inorder.append(x.value)
			self.helper_inprint(x.right)

	# left_rotate method
	def left_rotate(self, node):
		y = node.right
		node.right = y.left
		if y.left != self.nil:
			y.left.parent = node
		y.parent = node.parent
		if node.parent == self.nil:
			self.root = y
		elif node == node.parent.left:
			node.parent.left = y
		else:
			node.parent.right = y
		y.left = node
		node.parent = y

	# right_rotate method
	def right_rotate(self, node):
		y = node.left
		node.left = y.right
		if y.right != self.nil:
			y.right.parent = node
		y.parent = node.parent
		if node.parent == self.nil:
			self.root = y
		elif node == node.parent.right:
			node.parent.right = y
		else:
			node.parent.left = y
		y.right = node
		node.parent = y

# this function runs the program according to the problem specification
def driver():
    rbt = RBT()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, number = in_data[0], in_data[1:]
            if len(number) > 0:
                value = int(number[0])
            if action == "insert":
            	node = Node(value, rbt.nil, rbt.nil, rbt.nil, "black")
            	rbt.insert(node)
            elif action == "remove":
            	node = Node(value,rbt.nil,rbt.nil,rbt.nil,"black")
            	rbt.remove(value)
            elif action == "min":
            	print(rbt.min())
            elif action == "max":
            	print(rbt.max())
            elif action == "search":
                print(rbt.search(value))
            elif action == "inprint":
            	rbt.inorder = []
            	print(rbt.inprint())

if __name__ == "__main__":
    driver()




