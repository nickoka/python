import sys

class Heap():
    
    # class constructor
    def __init__(self):
        self.heap = []

    # insert method
    def insert(self, x):
        self.heap.append(x)
        size = self.size()
        i = size - 1
        # applies the heap property after inserting
        while True:
            parent = int((i / 2) - 1)
            if parent < 0:
                break
            else:
                if self.heap[parent] > x:
                    self.heap[i] = self.heap[parent]
                    self.heap[parent] = x
                    i = parent
                else:
                    break

    # remove method
    def remove(self):
        if self.is_empty():
            return "HeapError"
        best = self.look()
        last = self.heap[self.size() - 1]
        self.heap[0] = last
        del(self.heap[self.size() - 1])
        i = 0
        # applies the heap property after removing
        while True:
            if i >= (self.size() - 1):
                break
            c1 = (2 * i) + 1
            c2 = (2 * i) + 2
            if (self.size() % 3 != 0):
                if (self.heap[i] > self.heap[c1]):
                    temp = self.heap[i]
                    self.heap[i] = self.heap[c1]
                    self.heap[c1] = temp
                    i = c1
                else:
                    break
            elif (self.heap[i] > self.heap[c1]) or (self.heap[i] > self.heap[c2]):
                temp = self.heap[i]
                if self.heap[c1] < self.heap[c2]:
                    self.heap[i] = self.heap[c1]
                    self.heap[c1] = temp
                    i = c1
                elif self.heap[c2] < self.head[i]:
                    self.heap[i] = self.heap[c2]
                    self.heap[c2] = temp
                    i = c2
        return best

    # look method
    def look(self):
        return self.heap[0]

    # size method
    def size(self):
        return len(self.heap)

    # is_empty method
    def is_empty(self):
        if self.size() == 0:
            return True
        return False

    # to_string method
    def to_string(self):
        size = self.size()
        string = str(self.heap[0])
        if size > 1:
            for i in range(size - 1):
                string += (" " + self.heap[i + 1])
        return string

# this function runs the program according to the problem specification
def driver():
    h = Heap()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n): 
            in_data = f.readline().strip().split()
            option, value = in_data[0], in_data[1:]
            if option == "insert":
                h.insert(value[0])
            elif option == "remove":
                print(h.remove())
            elif option == "print":
                if h.is_empty():
                    print("Empty")
                else:
                    print(h.to_string())
            elif option == "size":
                print(h.size())
            elif option == "best":
                if h.is_empty():
                    print("HeapError")
                else:
                    print(h.look())


if __name__ == "__main__":
    driver()