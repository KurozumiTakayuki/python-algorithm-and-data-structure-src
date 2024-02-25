class MyQueue:
    def __init__(self):
        self.que = []

    def enqueue(self, value):
        self.que.append(value)

    def dequeue(self):
        return self.que.pop(0)

    def __str__(self):
        return str(self.que)
