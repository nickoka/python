class Calculator:

    def __init__(self):
        self.running_total = 0
        self.all = {0: True}

    def add(self, a):
        self.running_total += a
        self.all[self.running_total] = True
        return self.running_total

    def mult(self, a):
        self.running_total *= a
        self.all[self.running_total] = True
        return self.running_total

    def seen(self, a):
        return a in self.all 
