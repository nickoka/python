import sys
from Linked_List import *

class Queue(LinkedList):

    # enqueue method
    def enqueue(self, x):
        self.add(x, 2)

    # dequeue method
    def dequeue(self, y):
        # checks if queue is empty
        if self.is_empty():
            print("QueueError")
        else:
            if y == 0:
                print(self.remove())
            else:
                return (self.remove())
        return

    # is_empty method
    def is_empty(self):
        return self.empty()

# args: q, Queue
def print_queue(q):
    if q.is_empty():
        print("Empty")
    else:
        tempList = []
        while not q.is_empty():
            # dequeues items from the queue to be printed
            temp = q.dequeue(1)
            tempList.append(temp)
        for i in tempList:
            # enqueues the values that were printed and removed from the queue
            q.enqueue(i)
        word = str(tempList[0])
        for i in range (len(tempList) - 1):
            word += " " + str(tempList[i + 1])
        print(word)
    return

# this function runs the program according to the problem specification
def driver():
    q = Queue()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]
            if action == "enqueue":
                value = int(value_option[0])
                q.enqueue(value)
            elif action == "dequeue":
                q.dequeue(0)
            elif action == "print":
                print_queue(q)

if __name__ == "__main__":
    driver()
