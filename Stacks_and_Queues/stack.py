
class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if self.is_empty():
            return None
        else:
            val = self.stack[0]
            del self.stack[0]
            return val

    def push(self, item):
        self.stack.insert(0, item)

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack[0]

    def is_empty(self):
        return len(self.stack) == 0
