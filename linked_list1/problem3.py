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

# function that finds the first valid restaurant
def check(g, l, size):
    counter = 1
    energy = 0
    loop = 0
    while True:
        new_gain = g.dequeue()
        new_lose = l.dequeue()
        energy += new_gain
        if new_lose > energy:
            energy = 0
            loop = 0
        else:
            energy -= new_lose
            loop += 1
            if loop == size:
                return counter
        g.enqueue(new_gain)
        l.enqueue(new_lose)
        counter += 1

# this function runs the program according to the problem specification
def driver():
    gain_q = Queue()
    lost_q = Queue()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for i in range(n):
            in_data = f.readline().strip().split()
            gain_val, lose_val = int(in_data[0]), int(in_data[1:][0])
            gain_q.enqueue(gain_val)
            lost_q.enqueue(lose_val)
    value = n + check(gain_q, lost_q, n)
    print(value % n)

if __name__ == "__main__":
    driver()
