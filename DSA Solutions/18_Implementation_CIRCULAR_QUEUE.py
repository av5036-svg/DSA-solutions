class CircularQueue:
    def __init__(self, size):
        self.q = [None] * size
        self.size = size
        self.front = self.rear = -1

    def enqueue(self, x):
        if (self.rear + 1) % self.size == self.front:
            print("Queue Full")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.q[self.rear] = x

    def dequeue(self):
        if self.front == -1:
            print("Queue Empty")
            return
        val = self.q[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return val