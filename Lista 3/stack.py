class Empty(Exception):
    pass

class Queue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * Queue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        value = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        current_capacity = len(self._data)
        if self._size < current_capacity // 4 and current_capacity > self.DEFAULT_CAPACITY:
            new_capacity = max(self.DEFAULT_CAPACITY, current_capacity // 2)
            self._resize(new_capacity)
        return value

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0


class Stack_With_Queue(Queue):
    def push(self, element):  # złożoność O(1)
        self.enqueue(element)

    def pop(self):  # złożoność O(n)
        if self.is_empty():
            raise Empty('Stos jest pusty!')
        for k in range(len(self) - 1):
            self.enqueue(self.dequeue()) # przekłada elementy z początku kolejki na koniec
        return self.dequeue()

    def top(self):  # złożoność O(n)
        if self.is_empty():
            raise Empty('Stack is empty')
        for i in range(len(self) - 1):
            self.enqueue(self.dequeue())
        top_value = self.first()
        for i in range(len(self) - 1):
            self.enqueue(self.dequeue())

        return top_value