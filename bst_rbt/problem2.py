import sys

# started using the given starter code

class STNode:

    # class contsuctor
    def __init__(self, x: str):
        self.key = x
        self.left = None
        self.right = None


class SyntaxTree:

    # class constructor 
    def init_helper(self, i: int, l: 'list of strings') -> STNode:
        if i >= len(l):
            return None

        node = STNode(l[i])
        node.left = self.init_helper(2 * i, l)
        node.right = self.init_helper(2 * i + 1, l)
        return node

    def __init__(self, l: 'list of strings') -> 'complete syntax tree':
        self.root = self.init_helper(1, l)
        self.inorder_list = []
        self.expression = ""

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
            self.inorder_list.append(node.key)
            self.getInorder(node.right)

    # create_expression method: creates a fully parenthesized expression
    def create_expression(self):
        return self.expression_helper(self.root)

    # create_expression helper method
    def expression_helper(self, node):
        expression = ""
        if node == None:
            return expression
        elif (node.left == None) and (node.right == None):
            expression += node.key
        else:
            expression += "(" + self.expression_helper(node.left)
            expression += str(node.key)
            expression += self.expression_helper(node.right) + ")"
        return expression


    # evaluates the expression
    def evaluate_expression(self):
        return self.evaluate_helper(self.root)

    # evaluate_expression helper method
    def evaluate_helper(self, node):
        if node == None:
            return 0
        elif (node.left == None) and (node.right == None):
            return int(node.key)
        left = self.evaluate_helper(node.left)
        right = self.evaluate_helper(node.right)
        # syntax tree for operations: +, -, *
        if node.key == '+':
            return left + right
        elif node.key == '-':
            return left - right
        elif node.key == '*':
            return left * right

# this function runs the program according to the problem specification
def driver():
    syntax_list = []
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        in_data = f.readline().strip().split()
        syntax_list.append(in_data)
        syntax_list = syntax_list[0]
        syntax_list.insert(0, None)
        ST = SyntaxTree(syntax_list)
    print(ST.create_expression())
    print(ST.evaluate_expression())
            
if __name__ == "__main__":
    driver()