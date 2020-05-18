import sys
from Linked_List import *

class Stack(LinkedList):

    # class constructor
    def __init__(self):
        self.head = None

    # push method
    def push(self, x):
        self.add(x)

    # pop method
    def pop(self):
        # checks if stack is empty
        if self.is_empty():
            raise ("StackError")
        return (self.remove())
        
    # is_empty method
    def is_empty(self):
        return self.empty()

# function that creates a stack filled with the words wanting to find
def createStack(x):
    s = Stack()
    for i in range(len(x)):
        s.push(x[i])
    return s

# function that checks if the words wanting to find is in the list of words from a magazine
def compare(x, s):
    while True:
        if s.is_empty():
            break
        val = s.pop()
        if val not in x:
            return False
    return True

# this function runs the program according to the problem specification
def driver():
    with open(sys.argv[1]) as f:
        n = f.readline().strip()
        for i in range(2): 
            in_data = f.readline().strip().split()
            if i == 0:
                check_list = in_data
            else:
                s = createStack(in_data)
                collage = compare(check_list, s)
        if collage:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    driver()
