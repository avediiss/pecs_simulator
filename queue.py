class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        # add item to the end
        self.items.append(item)

    def dequeue(self):
        # remove item from the front
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.items.pop(0)

    def peek(self):
        # view the front item
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)