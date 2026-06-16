# math_utils.py
def add(a, b):
    return a + b

def safe_divide(a, b):
    return a / b

class Accumulator:
    def __init__(self):
        self.total = 0
    def add(self, n):
        self.total += n
        return self.total