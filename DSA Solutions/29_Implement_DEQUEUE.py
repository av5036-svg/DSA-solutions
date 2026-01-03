class Deque:
    def __init__(self):
        self.deque = []

    def insert_front(self, x):
        self.deque.insert(0, x)

    def insert_rear(self, x):
        self.deque.append(x)

    def delete_front(self):
        if not self.deque:
            return None
        return self.deque.pop(0)

    def delete_rear(self):
        if not self.deque:
            return None
        return self.deque.pop()

    def display(self):
        print(self.deque)

dq = Deque()
dq.insert_rear(10)
dq.insert_rear(20)
dq.insert_front(5)
dq.display()

dq.delete_front()
dq.display()
