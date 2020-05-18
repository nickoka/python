import sys

class Node:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BST:

    # class constructor
    def __init__(self):
        self.root = None
        self.inorder = []
        self.postorder = []
        self.preorder = []

    # insert method
    def insert(self, node):
        if self.root == None:
            self.root = node
        else:
            x = self.root
            while True:
                # walks the tree comparing if the value of the nodes are smaller or larger
                if int(node.value) <= int(x.value):
                    if x.left == None:
                        x.left = node
                        break
                    else:
                        x = x.left
                else:
                    if x.right == None:
                        x.right = node
                        break
                    else:
                        x = x.right

    # remove method
    def remove(self, value):
        x = self.root
        while True:
            if x == None:
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
                    if x.left == None:
                        temp_val = x.right
                        x.value = temp_val
                        x.right == None
                        break
                    # the parent node only has a left child
                    elif x.right == None:
                        temp_val = x.left
                        x.value = temp_val
                        x.left = None
                        break
                    # the node has no children and the right child is the successor
                    else:
                        temp_val = x.right
                        x.value = temp_val
                        x.right == None
                        break

    # search method
    def search(self, value):
        x = self.root
        while True:
            if x == None:
                return "NotFound"
            if x.value == value:
                return "Found"
            elif int(value) > int(x.value):
                x = x.right
            else:
                x = x.left

    # maximum method
    def maximum (self, x):
        x = self.root
        while True:
            if x == None:
                return "Empty"
            elif x.right == None:
                return x.value
                break
            else:
                x = x.right
        return x.value

    # minimum method
    def minimum (self, x):
        x = self.root
        while True:
            if x == None:
                return "Empty"
            elif x.left == None:
                break
            x = x.left
        return x.value

    # to_list_preorder method
    def to_list_preorder(self):
        self.preorder = []
        if self.root == None:
            print("Empty", end = "")
            return
        self.getPreorderList(self.root)

    # recursively walks the tree in preorder and adds to the preorder list
    def getPreorderList(self, node):
        if node != None:
            self.preorder.append(node.value)
            self.getPreorderList(node.left)
            self.getPreorderList(node.right)

    # to_list_inorder method
    def to_list_inorder(self):
        self.inorder = []
        if self.root == None:
            print("Empty".rstrip(), end = "")
            return
        self.getInorder(self.root)

    # recursively walks the tree in inorder and adds to the inorder list
    def getInorder(self, node):
        if node != None:
            self.getInorder(node.left)
            self.inorder.append(node.value)
            self.getInorder(node.right)

    # to_list_postorder method
    def to_list_postorder(self):
        self.postorder = []
        if self.root == None:
            print("Empty", end = "")
            return
        self.getPostorder(self.root)

    # recursively walks the tree in postorder and adds to the postoder list
    def getPostorder(self, node):
        if node != None:
            self.getPostorder(node.left)
            self.getPostorder(node.right)
            self.postorder.append(node.value)


# this function runs the program according to the problem specification
def driver():
    bst = BST()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, number = in_data[0], in_data[1:]
            if len(number) > 0:
                value = number[0]
            if action == "insert":
                node = Node(value)
                bst.insert(node)
            elif action == "remove":
                bst.remove(value)
            elif action == "search":
                print(bst.search(value))
            elif action == "max":
                print(bst.maximum(value))
            elif action == "min":
                print(bst.minimum(value))
            elif action == "preprint":
                bst.to_list_preorder()
                output = ""
                for x in bst.preorder:
                    if type(x) == str:
                        output += (x + " ")
                print(output.rstrip())
            elif action == "inprint":
                bst.to_list_inorder()
                output = ""
                for x in bst.inorder:
                    if type(x) == str:
                        output += (x + " ")
                print(output.rstrip())
            elif action == "postprint":
                bst.to_list_postorder()
                output = ""
                for x in bst.postorder:
                    if type(x) == str:
                        output += (x + " ")
                print(output.rstrip())
            
if __name__ == "__main__":
    driver()