import sys
from Linked_List import *

class Queue(LinkedList):

    # enqueue method
    def enqueue(self, x):
        self.add_tail(x)

    # dequeue method
    def dequeue(self):
        # checks if queue is empty
        if self.is_empty():
            raise ("QueueError")
        else:
            return (self.remove())
        
    # is_empty method
    def is_empty(self):
        return self.empty()

# function that checks if the string of brackets are well formed
def checkCorrect(q, size):
    start = ["(", "[", "<", "{"]
    end = [")", "]", ">", "}"]
    pairs = [q.dequeue()]
    if pairs[0] in end or size % 2 == 1:
        return False
    else:
        for _ in range(size - 1):
            val = q.dequeue()
            if val in start:
                pairs.append(val)
            else:
                if (val == (")")) and ("(" not in pairs):
                    return False
                elif (val == ("]")) and ("[" not in pairs):
                    return False
                elif (val == ("}")) and ("{" not in pairs):
                    return False
                elif (val == (">")) and ("<" not in pairs):
                    return False
                else:
                    if val == (")"):
                        pairs.remove("(")
                    elif val == ("]"):
                        pairs.remove("[")
                    elif val == (">"):
                        pairs.remove("<")
                    elif val == ("}"):
                        pairs.remove("{")
        return True

# this function runs the program according to the problem specification
def driver():
    q = Queue()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n): 
            in_data = f.readline().strip().split()
            i = 0
            size = (len(str(in_data[0])))
            for i in range(size):
                val = in_data[0][i]
                q.enqueue(val)
            valid = checkCorrect(q, size)
            if valid:
                print("YES")
            else:
                print("NO")

if __name__ == "__main__":
    driver()
