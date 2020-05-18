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

def create_prioritzed_list(Alist, Blist):
    queue1 = PriorityQueue()
    queue2 = PriorityQueue()
    # sorts Alist and Blist in order using the priority queue
    Alist = (sort(Alist, queue1))
    Blist = (sort(Blist, queue2))

    # list of prioritized IP addresses
    prioritized_list = []
    prev_value = 0
    prev_address = ""

    # adding contents of Alist and Blist into prioritized_list in order of priority
    for i in Alist:
        number, address = i
        if number != prev_value:
            prioritized_list.append(address)
        else:
            prioritized_list.append(address)
            prioritized_list[-2] = prev_address
        prev_value = number
        prev_address = address
    for n in Blist:
        number, address = n
        if number == prev_value:
            prioritized_list.append(prev_address)
            prioritized_list[-2] = address
        else:
            prioritized_list.append(address)
        prev_value = number
        prev_address = address
    return prioritized_list

def driver():
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        # Alist and Blist to make sure the Alist gets prioritzed
        Alist = []
        Blist = []
        for _ in range(n):
            in_data = f.readline().strip().split()
            ip_add, prio, val = in_data[0], in_data[1], in_data[2:]
            if in_data[1] == "A":
                item = int(val[0]), ip_add
                Alist.append(item)
            else:
                item = int(val[0]), ip_add
                Blist.append(item)
    prioritized_list = create_prioritzed_list(Alist, Blist)
    for i in prioritized_list:
        print(i)

if __name__ == "__main__":
    driver()

