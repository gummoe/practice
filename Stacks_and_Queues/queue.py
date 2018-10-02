
class Queue:

    def __init__(self):
        self.queue = []

    def remove(self):
        if self.is_empty():
            return None
        else:
            val = self.queue[0]
            del self.queue[0]
            return val

    def add(self, item):
        self.queue.append(item)

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0
