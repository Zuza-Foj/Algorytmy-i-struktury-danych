class Queue_out_of_Stacks:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def en_queue(self, item):
        self.stack_in.append(item)

    def de_queue(self):
        if len(self.stack_out) == 0:
            if len(self.stack_in) == 0:
                raise IndexError("Kolejka jest pusta")

        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())

        return self.stack_out.pop()

    def peek(self):
        if len(self.stack_out) == 0:
            if len(self.stack_in) == 0:
                raise IndexError("Kolejka jest pusta")

        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())

        return self.stack_out[-1] #najstarszy element w kolejce


if __name__ == '__main__':
    queue = Queue_out_of_Stacks()

    queue.en_queue(10)
    queue.en_queue(20)
    queue.en_queue(30)
    queue.en_queue(40)

    print(f"Stos Wejściowy (Stack_in): {queue.stack_in}")
    print(f"Stos Wyjściowy (Stack_out): {queue.stack_out}")

    #usuwanie najstarszego elementu kolejki
    item = queue.de_queue()
    print(f"Usunięto (FIFO): {item}")

