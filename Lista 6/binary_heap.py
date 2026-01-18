import graphviz

class BinaryHeap:
    def __init__(self):
        self.heap = []

    def get_parent_idx(self, i): return (i - 1) // 2
    def get_left_idx(self, i): return 2 * i + 1
    def get_right_idx(self, i): return 2 * i + 2

    def insert(self, key):
        self.heap.append(key)
        curr_idx = len(self.heap) - 1

        while curr_idx > 0:
            parent_idx = self.get_parent_idx(curr_idx)
            if self.heap[curr_idx] < self.heap[parent_idx]:
                self.heap[curr_idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[curr_idx]
                curr_idx = parent_idx
            else:
                break

    def heapify(self, i=0):
        smallest = i
        left = self.get_left_idx(i)
        right = self.get_right_idx(i)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def remove(self):
        if len(self.heap) == 0:
            print("Kopiec jest pusty!")
            return
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop() # ostatni element, to nowy root
        self.heapify(0)
        return root

    def display(self):
        if self.heap is None:
            print("Kopiec jest pusty!")
            return

        dot = graphviz.Digraph(comment='Binary Heap')
        for i in range(len(self.heap)):
            dot.node(str(i), label=str(self.heap[i]))

            left = self.get_left_idx(i)
            right = self.get_right_idx(i)

            if left < len(self.heap): # sprawdza, czy na liście mieści się element o tym indeksie (lewe dziecko rodzica)
                dot.edge(str(i), str(left))
            if right < len(self.heap): # jak wyżej
                dot.edge(str(i), str(right))

        dot.render(filename='bt_output', view=True, format='png')
        return dot

    def sort(self):
        if len(self.heap) == 0:
            print("Kopiec jest pusty!")
            return

        sorted_list = []
        while len(self.heap) > 0:
            sorted_list.append(self.remove())

        for element in sorted_list:
            self.insert(element)

        return sorted_list

if __name__ == '__main__':
    heap = BinaryHeap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(7)
    heap.insert(1)
    heap.display()

    sorted_result = heap.sort()
    print(sorted_result)

    print(heap.remove())