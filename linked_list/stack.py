import sys
from Linked_List import *

class Stack(LinkedList):

    # class constructor
    def __init__(self):
        self.head = None

    # push method
    def push(self, x):
        self.add(x, 1)

    # pop method
    def pop(self, y):
        # checks if stack is empty
        if self.is_empty():
            print("StackError")
        else:
            if y == 0:
                print(self.remove())
            else:
                return (self.remove())
        return

    # is_empty method
    def is_empty(self):
        return self.empty()

# args: s, Stack
def print_stack(s):
    if s.is_empty():
        print("Empty")
    else:
        tempList = []
        while not s.is_empty():
            # pops the elements of the stack to be printed
            temp = s.pop(1)
            tempList.append(temp)
        for i in reversed(tempList):
            # pushes the values that were printed
            s.push(i)
        word = str(tempList[0])
        for i in range (len(tempList) - 1):
            word += " " + str(tempList[i + 1])
        print(word)
    return

# this function runs the program according to the problem specification
def driver():
    s = Stack()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]
            if action == "push":
                value = int(value_option[0])
                s.push(value)
            elif action == "pop":
                s.pop(0)
            elif action == "print":
                print_stack(s)

if __name__ == "__main__":
    driver()
