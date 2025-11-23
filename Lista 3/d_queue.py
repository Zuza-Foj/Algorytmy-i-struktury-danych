class Empty(Exception):
    pass


class Dequeue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * Dequeue.DEFAULT_CAPACITY
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

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

    def add_first(self, item):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._front = (self._front - 1) % len(self._data) # nowy początkowy indeks bedzie odpowiadał itemowi (cykliczność)
        self._data[self._front] = item
        self._size += 1

    def add_last(self, item):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = item
        self._size += 1

    def delete_first(self):
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

    def delete_last(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        last_index = (self._front + self._size - 1) % len(self._data)
        value = self._data[last_index]
        self._data[last_index] = None
        self._size -= 1
        current_capacity = len(self._data)
        if self._size < current_capacity // 4 and current_capacity > self.DEFAULT_CAPACITY:
            new_capacity = max(self.DEFAULT_CAPACITY, current_capacity // 2)
            self._resize(new_capacity)
        return value

    def last(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        last_index = (self._front + self._size - 1) % len(self._data)
        return self._data[last_index]

if __name__ == '__main__':
    d = Dequeue()
    d.add_first(10)
    # d._front = (0 - 1) % 10 = 9
    # d._data[9] = 10
    d.add_last(20)
    # d._rear = (0 + 1) % 10 = 1
    # d._data[1] = 20
    d.add_first(5)
    # d._front = (9 - 1) % 10 = 8
    # d._data[8] = 5

    print(f"Pierwszy element: {d.first()}")
    print(f"Ostatni element: {d.last()}")