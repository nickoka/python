import sys

class Node:

    # class constructor
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BST:

    # class constructor
    def __init__(self):
        self.root = None

    # insert method
    def insert(self, node):
        if self.root == None:
            self.root = node
        else:
            x = self.root
            while True:
                if node.value > x.value:
                    if x.right == None:
                        x.right = node
                        break
                    else:
                        x = x.right
                elif node.value <= x.value:
                    if x.left == None:
                        x.left = node
                        break
                    else:
                        x = x.left

    # remove method
    def remove(self, value):
        x = self.root
        while True:
            if x == None:
                print("TreeError")
                break
            else:
                if x.value == None:
                    print("TreeError")
                    break
                elif value < x.value:
                    x = x.left
                elif value > x.value:
                    x = x.right
                else:
                    if x.left == None and x.right != None:
                        temp_node = self.helper_min(x.right)
                        x.value = temp_node.value
                        temp_node = None
                        break
                    elif x.right == None and x.left != None:
                        temp_node = self.helper_max(x.left)
                        x.value = temp_node.value
                        temp_node = None
                        break
                    elif x.right != None and x.left != None:
                        temp_node = self.helper_min(x.right)
                        x.value = temp_node.value
                        temp_node = None
                        break
                    else:
                        x.value = None
                        x = None
                        break

    # search method
    def search(self, value):
        x = self.root
        while True:
            if x == None:
                return "NotFound"
            if x.value == value:
                return "Found"
            elif value > x.value:
                x = x.right
            else:
                x = x.left

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
        if node == None:
            return None
        while(node.right != None):
            node = node.right
        return node

    # min helper method
    def helper_min(self, x):
        node = x
        if node == None:
            return None
        while(node.left != None):
            node = node.left
        return node

    # best_path_value method
    def best_path_value(self):
        return self.best_path_helper(self.root)

    # best_path_value helper method - referenced in-lab example
    def best_path_helper(self, node):
        if node == None:
            return 0
        left = self.best_path_helper(node.left)
        right = self.best_path_helper(node.right)
        return max(left, right) + str(node.value).count('5')

# this function runs the program according to the problem specification
def driver():
    bst = BST()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, number = in_data[0], in_data[1:]
            if len(number) > 0:
                value = int(number[0])
            if action == "insert":
                node = Node(value)
                bst.insert(node)
            elif action == "remove":
                bst.remove(value)
            elif action == "bpv":
                result = bst.best_path_value()
                if result == 0:
                    print("TreeError")
                else:
                    print(result)
            
if __name__ == "__main__":
    driver()