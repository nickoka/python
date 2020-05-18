from heapq import *
import sys

class PriorityQueue:

    # class constructor
    def __init__(self):
        self.q = []

    # is_empty method
    def is_empty(self):
        if len(self.q) == 0:
            return True
        return False

    # insert method
    def insert(self, x):
        heappush(self.q, x)

    # remove_min method
    def remove_min(self):
        return heappop(self.q)

# sorts the given list using the PriorityQueue class 
def sort(original_list, queue):
    # insert each integer into the priority queue
    for x in original_list:
        queue.insert(x)

    # remove min until the priority queue is empty
    final_list = []
    while not queue.is_empty():
        final_list.append(queue.remove_min())

    return final_list

# calculates the median of a sorted list
def calc_median(original, half):
    # original.sort()
    size = len(original)
    if size == 1:
        return original[0]
    elif size % 2 == 1:
        return original[half]
    else:
        value = original[half - 1] + original[half]
        return float(value / 2)

# this function runs the program according to the problem specification
def driver():
    original = []
    i = 0
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            i += 1
            in_data = f.readline().strip().split()
            value = int(in_data[0])
            original.append(value)
            half = int(i/2)
            queue = PriorityQueue()
            original = sort(original, queue)
            print(calc_median(original, half))

if __name__ == "__main__":
    driver()