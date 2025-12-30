import matplotlib.pyplot as plt
import time

class Node:
    def __init__(self, _value, _next=None):
        self.value = _value
        self.next = _next

class Stack:
    def __init__(self):
        self.head = None

    def push(self, new_value):
        new_node = Node(new_value, self.head)
        self.head = new_node

    def pop(self):
        if self.head is None:
            print("Lista nie zawiera żadnych elementów!")
            return None

        popped_value = self.head.value
        self.head = self.head.next
        return popped_value

    def top(self):
        if self.head is None:
            print("Lista nie zawiera żadnych elementów!")
            return None

        return self.head.value

def run_analysis():
    sizes = [1000, 5000, 10000, 50000, 100000, 200000]
    push_times = []
    pop_times = []

    for n in sizes:
        llist = Stack()

        start_push = time.time()
        for i in range(n):
            llist.push(i)
        end_push = time.time()
        push_times.append((end_push - start_push) / n * 1000000)

        start_pop = time.time()
        for i in range(n):
            llist.pop()
        end_pop = time.time()
        pop_times.append((end_pop - start_pop) / n * 1000000)

    plt.figure()
    plt.plot(sizes, push_times, label='Push (uśrednione)', marker='o')
    plt.plot(sizes, pop_times, label='Pop (uśrednione)', marker='s')

    plt.title('Złożoność obliczeniowa operacji na stosie (O(1))')
    plt.xlabel('Liczba elementów na stosie (n)')
    plt.ylabel('Czas operacji ($\mu $s)')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.ylim(0, max(max(push_times), max(pop_times)) * 1.5)

    plt.show()

if __name__ == "__main__":
    run_analysis()